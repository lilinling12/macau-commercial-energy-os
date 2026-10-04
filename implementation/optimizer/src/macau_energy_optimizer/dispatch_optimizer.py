"""Exact finite-horizon SHADOW schedule search over a bounded discrete domain.

This is an executable research prototype, not a continuous optimizer or a
production dispatch engine. It enumerates discrete flexible-load and ESS actions
and minimizes grid-import energy charges over a short supplied horizon.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from itertools import product

from macau_energy_optimizer.dispatch_assessment import (
    AssessmentRequest,
    AssessmentResult,
    EconomicContext,
    EssLimits,
    EvidenceRef,
    EvidenceState,
    FlexibleLoadFlow,
    FlexibleLoadKind,
    FlexibleLoadLimit,
    ImportEnergyRate,
    Schedule,
    ScheduleInterval,
    assess_schedule,
)


class DispatchSearchError(ValueError):
    """The bounded search cannot safely construct a schedule for this request."""


@dataclass(frozen=True, slots=True)
class FlexibleEnergyTask:
    asset_id: str
    kind: FlexibleLoadKind
    required_energy_kwh: Decimal
    available_intervals: tuple[bool, ...]
    min_on_power_kw: Decimal
    max_power_kw: Decimal
    evidence: EvidenceRef


@dataclass(frozen=True, slots=True)
class DispatchSearchRequest:
    tenant_id: str
    site_id: str
    site_timezone: str
    baseline: Schedule
    flexible_tasks: tuple[FlexibleEnergyTask, ...]
    fixed_flexible_load_limits: tuple[FlexibleLoadLimit, ...]
    physical_evidence: tuple[EvidenceRef, ...]
    economic_context: EconomicContext
    power_step_kw: Decimal
    soc_step_kwh: Decimal
    ess_limits: EssLimits | None = None
    initial_soc_kwh: Decimal | None = None
    grid_import_limit_kw: Decimal | None = None
    grid_import_limit_evidence: EvidenceRef | None = None
    max_states_per_interval: int = 100_000
    max_transitions: int = 1_000_000


@dataclass(frozen=True, slots=True)
class DispatchSearchResult:
    candidate: Schedule
    assessment: AssessmentResult
    transitions_examined: int
    scenario_only: bool
    search_scope: str = "EXACT_WITHIN_DECLARED_DISCRETE_ACTION_SPACE"


@dataclass(frozen=True, slots=True)
class _Path:
    objective: Decimal
    actions: tuple[tuple[tuple[Decimal, ...], Decimal, Decimal, Decimal | None], ...]


def generate_candidate(request: DispatchSearchRequest) -> DispatchSearchResult:
    """Find a least-import-energy-charge candidate in the declared discrete space."""
    rows = request.baseline.intervals
    if not rows:
        raise DispatchSearchError("A non-empty baseline schedule is required.")
    if (
        not isinstance(request.max_states_per_interval, int)
        or isinstance(request.max_states_per_interval, bool)
        or not isinstance(request.max_transitions, int)
        or isinstance(request.max_transitions, bool)
        or request.max_states_per_interval < 1
        or request.max_transitions < 1
    ):
        raise DispatchSearchError("Search bounds must be positive integers.")
    if not _positive(request.power_step_kw) or not _positive(request.soc_step_kwh):
        raise DispatchSearchError("Power and SOC discretization steps must be positive finite Decimals.")
    if len(request.physical_evidence) == 0 or any(not _usable_evidence(ref) for ref in request.physical_evidence):
        raise DispatchSearchError("Required physical evidence is missing, unknown, or stale.")
    if request.ess_limits is not None and not isinstance(request.ess_limits, EssLimits):
        raise DispatchSearchError("ESS limits must use the declared EssLimits model.")
    if len(request.economic_context.import_energy_rates) != len(rows):
        raise DispatchSearchError("One tariff rate must align with each baseline interval.")
    rates = _aligned_rates(rows, request.economic_context.import_energy_rates)
    if any(not _usable_evidence(rate.evidence) for rate in request.economic_context.import_energy_rates):
        raise DispatchSearchError("Unknown or stale import-rate evidence cannot guide schedule search.")
    economic_identity = (
        request.economic_context.account_meter_mapping,
        request.economic_context.contract,
        request.economic_context.tariff,
    )
    if any(not _usable_evidence(ref) for ref in economic_identity):
        raise DispatchSearchError("Unknown or stale account, contract, or tariff evidence cannot guide schedule search.")
    if request.grid_import_limit_kw is not None:
        if not _nonnegative(request.grid_import_limit_kw) or not _usable_evidence(request.grid_import_limit_evidence):
            raise DispatchSearchError("A grid-import guard requires a finite non-negative limit and usable evidence.")

    duration = rows[0].duration_hours
    if any(row.duration_hours != duration for row in rows):
        raise DispatchSearchError("This prototype supports equal-duration intervals only.")
    if any(row.start.tzinfo is None or row.start.utcoffset() is None for row in rows):
        raise DispatchSearchError("Schedule timestamps must be timezone-aware.")
    if len({task.asset_id for task in request.flexible_tasks}) != len(request.flexible_tasks):
        raise DispatchSearchError("Flexible task asset IDs must be unique.")
    if any(len(task.available_intervals) != len(rows) for task in request.flexible_tasks):
        raise DispatchSearchError("Each task availability mask must align with the schedule horizon.")
    if any(not isinstance(value, bool) for task in request.flexible_tasks for value in task.available_intervals):
        raise DispatchSearchError("Task availability masks must contain boolean values.")

    limits = {limit.asset_id: limit for limit in request.fixed_flexible_load_limits}
    if len(limits) != len(request.fixed_flexible_load_limits):
        raise DispatchSearchError("Fixed-load envelope asset IDs must be unique.")
    for task in request.flexible_tasks:
        if not _usable_evidence(task.evidence):
            raise DispatchSearchError(f"Task evidence is missing, unknown, or stale for {task.asset_id}.")
        if not task.asset_id.strip() or not isinstance(task.kind, FlexibleLoadKind):
            raise DispatchSearchError("Each flexible task requires an asset ID and known load kind.")
        if not _nonnegative(task.required_energy_kwh) or not _nonnegative(task.min_on_power_kw) or not _nonnegative(task.max_power_kw):
            raise DispatchSearchError(f"Task values must be finite and non-negative for {task.asset_id}.")
        if task.required_energy_kwh < 0 or task.min_on_power_kw > task.max_power_kw:
            raise DispatchSearchError(f"Task energy or power bounds are invalid for {task.asset_id}.")
        if any(row.duration_hours <= 0 for row in rows):
            raise DispatchSearchError("Each interval must have positive duration.")
        energy_step = request.power_step_kw * duration
        if not _multiple(task.required_energy_kwh, energy_step):
            raise DispatchSearchError(f"Required energy must be a multiple of {energy_step} kWh for {task.asset_id}.")
        if not _multiple(task.min_on_power_kw, request.power_step_kw) or not _multiple(task.max_power_kw, request.power_step_kw):
            raise DispatchSearchError(f"Task power limits must align to the declared power step for {task.asset_id}.")
        if task.required_energy_kwh > 0 and not any(task.available_intervals):
            raise DispatchSearchError(f"Task {task.asset_id} has required energy but no available intervals.")
        if any(flow.asset_id == task.asset_id for row in rows for flow in row.flexible_loads):
            observed = sum((flow.power_kw * row.duration_hours for row in rows for flow in row.flexible_loads if flow.asset_id == task.asset_id), Decimal("0"))
            if observed != task.required_energy_kwh:
                raise DispatchSearchError(f"Baseline energy for {task.asset_id} does not equal its required service energy.")

    ess = request.ess_limits
    if ess is not None:
        if request.initial_soc_kwh is None or not _nonnegative(request.initial_soc_kwh):
            raise DispatchSearchError("An ESS requires a finite initial SOC.")
        if request.initial_soc_kwh < ess.min_soc_kwh or request.initial_soc_kwh > ess.max_soc_kwh:
            raise DispatchSearchError("Initial ESS SOC is outside its evidenced operating range.")
        if not _usable_evidence(ess.evidence):
            raise DispatchSearchError("ESS limits require usable evidence.")
        baseline_start_soc = rows[0].ess_soc_start_kwh
        baseline_end_soc = rows[-1].ess_soc_end_kwh
        if baseline_start_soc is None or baseline_end_soc is None:
            raise DispatchSearchError("ESS optimization requires evidenced baseline SOC at both schedule-window boundaries.")
        if request.initial_soc_kwh != baseline_start_soc:
            raise DispatchSearchError("Candidate initial SOC must match the baseline schedule-window start SOC.")
        if baseline_end_soc < ess.min_soc_kwh or baseline_end_soc > ess.max_soc_kwh:
            raise DispatchSearchError("Baseline terminal SOC is outside the evidenced ESS operating range.")
        if not _multiple(baseline_end_soc - ess.min_soc_kwh, request.soc_step_kwh):
            raise DispatchSearchError("Baseline terminal SOC does not align with the SOC discretization step.")
        if not _multiple(request.initial_soc_kwh - ess.min_soc_kwh, request.soc_step_kwh):
            raise DispatchSearchError("Initial ESS SOC does not align with the SOC discretization step.")
        for limit in (ess.max_charge_kw, ess.max_discharge_kw):
            if not _nonnegative(limit) or not _multiple(limit, request.power_step_kw):
                raise DispatchSearchError("ESS power ratings must be non-negative and align to the power step.")
        for direction, efficiency in (("charge", ess.charge_efficiency), ("discharge", ess.discharge_efficiency)):
            if not _unit_interval(efficiency):
                raise DispatchSearchError("ESS efficiencies must be greater than zero and no greater than one.")
            max_power = ess.max_charge_kw if direction == "charge" else ess.max_discharge_kw
            for power in _steps(max_power, request.power_step_kw):
                if power and not _multiple(_soc_delta(power, duration, efficiency, direction), request.soc_step_kwh):
                    raise DispatchSearchError("ESS efficiency, interval duration, power step and SOC step must produce aligned SOC transitions.")
    elif request.initial_soc_kwh is not None:
        raise DispatchSearchError("Initial SOC was supplied without an ESS model.")

    _check_baseline_service(request)
    task_envelopes = tuple(
        FlexibleLoadLimit(task.asset_id, Decimal("0"), task.max_power_kw, task.evidence)
        for task in request.flexible_tasks
    )
    all_limits = task_envelopes + request.fixed_flexible_load_limits
    if any(not _usable_evidence(limit.evidence) for limit in request.fixed_flexible_load_limits):
        raise DispatchSearchError("Fixed flexible loads require usable evidence.")
    baseline_check = assess_schedule(AssessmentRequest(
        tenant_id=request.tenant_id,
        site_id=request.site_id,
        site_timezone=request.site_timezone,
        baseline=request.baseline,
        candidate=request.baseline,
        physical_evidence=request.physical_evidence,
        flexible_load_limits=all_limits,
        ess_limits=ess,
        economic_context=request.economic_context,
    ))
    if baseline_check.physical_status.value in ("BLOCKED", "INFEASIBLE"):
        raise DispatchSearchError("Baseline schedule failed the bounded physical assessment: " + "; ".join(baseline_check.reasons))
    actions = _task_action_sets(request.flexible_tasks, request.power_step_kw)
    ess_actions = _ess_action_set(ess, request.power_step_kw)
    initial_soc = request.initial_soc_kwh if ess is not None else None
    initial_state = (initial_soc, tuple(Decimal("0") for _ in request.flexible_tasks))
    frontier: dict[tuple[Decimal | None, tuple[Decimal, ...]], _Path] = {initial_state: _Path(Decimal("0"), ())}
    transitions = 0

    for index, row in enumerate(rows):
        next_frontier: dict[tuple[Decimal | None, tuple[Decimal, ...]], _Path] = {}
        for (soc, delivered), path in frontier.items():
            interval_flex_actions = product(*[task_actions[index] for task_actions in actions]) if actions else ((),)
            for flex_powers in interval_flex_actions:
                next_delivered = tuple(delivered[i] + flex_powers[i] * duration for i in range(len(flex_powers)))
                if any(next_delivered[i] > request.flexible_tasks[i].required_energy_kwh for i in range(len(flex_powers))):
                    continue
                for charge_kw, discharge_kw in ess_actions:
                    transitions += 1
                    if transitions > request.max_transitions:
                        raise DispatchSearchError("Search transition limit exceeded; reduce horizon, tasks, or resolution.")
                    next_soc = soc
                    if ess is not None:
                        assert soc is not None
                        next_soc = soc + _soc_delta(charge_kw, duration, ess.charge_efficiency, "charge")
                        next_soc -= _soc_delta(discharge_kw, duration, ess.discharge_efficiency, "discharge")
                        if next_soc < ess.min_soc_kwh or next_soc > ess.max_soc_kwh:
                            continue
                    fixed_load_kw = sum((flow.power_kw for flow in row.flexible_loads if flow.asset_id not in {task.asset_id for task in request.flexible_tasks}), Decimal("0"))
                    task_load_kw = sum(flex_powers, Decimal("0"))
                    demand_kw = row.base_load_kw + fixed_load_kw + task_load_kw + row.losses_kw
                    residual_kw = demand_kw + charge_kw - discharge_kw
                    if residual_kw < 0:
                        continue
                    if discharge_kw and row.pv_generation_kw >= demand_kw + charge_kw:
                        continue
                    pv_used_kw = min(row.pv_generation_kw, residual_kw)
                    grid_import_kw = max(Decimal("0"), residual_kw - row.pv_generation_kw)
                    if request.grid_import_limit_kw is not None and grid_import_kw > request.grid_import_limit_kw:
                        continue
                    curtailed_kw = row.pv_generation_kw - pv_used_kw
                    rate = rates[(row.start, row.end)].rate_mop_per_kwh
                    objective = path.objective + grid_import_kw * duration * rate
                    new_state = (next_soc, next_delivered)
                    action = (tuple(flex_powers), charge_kw, discharge_kw, next_soc)
                    candidate_path = _Path(objective, path.actions + (action,))
                    previous = next_frontier.get(new_state)
                    if previous is None or candidate_path.objective < previous.objective:
                        next_frontier[new_state] = candidate_path
        if not next_frontier:
            raise DispatchSearchError(f"No feasible candidate reaches interval {index + 1} within the declared discrete action space.")
        if len(next_frontier) > request.max_states_per_interval:
            raise DispatchSearchError("Search state limit exceeded; reduce horizon, tasks, or resolution.")
        frontier = next_frontier

    target_delivered = tuple(task.required_energy_kwh for task in request.flexible_tasks)
    terminal_soc = rows[-1].ess_soc_end_kwh if ess is not None else None
    terminal_candidates = [
        path for (soc, delivered), path in frontier.items()
        if delivered == target_delivered and (ess is None or soc == terminal_soc)
    ]
    if not terminal_candidates:
        raise DispatchSearchError("No feasible candidate satisfies all required flexible-load energy and baseline terminal SOC conditions.")
    best = min(terminal_candidates, key=lambda item: item.objective)
    candidate = _materialize_candidate(request, best.actions)
    assessment_request = AssessmentRequest(
        tenant_id=request.tenant_id,
        site_id=request.site_id,
        site_timezone=request.site_timezone,
        baseline=request.baseline,
        candidate=candidate,
        physical_evidence=request.physical_evidence,
        flexible_load_limits=all_limits,
        ess_limits=ess,
        grid_import_limit_kw=request.grid_import_limit_kw,
        grid_import_limit_evidence=request.grid_import_limit_evidence,
        economic_context=request.economic_context,
    )
    assessment = assess_schedule(assessment_request)
    assumptions = list(request.physical_evidence)
    assumptions.extend(task.evidence for task in request.flexible_tasks)
    assumptions.extend(limit.evidence for limit in request.fixed_flexible_load_limits)
    if ess is not None:
        assumptions.append(ess.evidence)
    assumptions.extend((request.economic_context.account_meter_mapping, request.economic_context.contract, request.economic_context.tariff))
    assumptions.extend(rate.evidence for rate in request.economic_context.import_energy_rates)
    scenario_only = any(item.state is not EvidenceState.VERIFIED for item in assumptions)
    return DispatchSearchResult(candidate, assessment, transitions, scenario_only)


def _check_baseline_service(request: DispatchSearchRequest) -> None:
    rows = request.baseline.intervals
    duration = rows[0].duration_hours
    if any(row.duration_hours != duration for row in rows):
        raise DispatchSearchError("This prototype supports equal-duration intervals only.")
    task_ids = {task.asset_id for task in request.flexible_tasks}
    for task in request.flexible_tasks:
        baseline_energy = sum(
            (flow.power_kw * row.duration_hours for row in rows for flow in row.flexible_loads if flow.asset_id == task.asset_id),
            Decimal("0"),
        )
        if baseline_energy != task.required_energy_kwh:
            raise DispatchSearchError(f"Baseline energy for {task.asset_id} must equal required service energy.")
        for index, row in enumerate(rows):
            power = sum((flow.power_kw for flow in row.flexible_loads if flow.asset_id == task.asset_id), Decimal("0"))
            if power and (not task.available_intervals[index] or power < task.min_on_power_kw or power > task.max_power_kw):
                raise DispatchSearchError(f"Baseline operation for {task.asset_id} violates its availability or power envelope.")
    if any(not isinstance(row.base_load_kw, Decimal) or not row.base_load_kw.is_finite() or row.base_load_kw < 0 for row in rows):
        raise DispatchSearchError("Baseline non-flexible load must be a finite, non-negative Decimal kW value.")
    if any(not isinstance(row.pv_generation_kw, Decimal) or not row.pv_generation_kw.is_finite() or row.pv_generation_kw < 0 for row in rows):
        raise DispatchSearchError("PV generation must be a finite, non-negative Decimal kW value.")
    task_fixed_flows = {flow.asset_id for row in rows for flow in row.flexible_loads} - task_ids
    known_fixed = {limit.asset_id for limit in request.fixed_flexible_load_limits}
    if task_fixed_flows - known_fixed:
        raise DispatchSearchError("Every fixed flexible load needs an operating-envelope evidence reference.")


def _task_action_sets(tasks: tuple[FlexibleEnergyTask, ...], step_kw: Decimal) -> tuple[tuple[tuple[Decimal, ...], ...], ...]:
    by_task: list[tuple[tuple[Decimal, ...], ...]] = []
    for task in tasks:
        on_values = tuple(_steps(task.max_power_kw, step_kw, start=task.min_on_power_kw))
        per_interval = tuple((Decimal("0"), *on_values) if task.available_intervals[index] else (Decimal("0"),) for index in range(len(task.available_intervals)))
        by_task.append(per_interval)
    return tuple(by_task)


def _ess_action_set(ess: EssLimits | None, step_kw: Decimal) -> tuple[tuple[Decimal, Decimal], ...]:
    if ess is None:
        return ((Decimal("0"), Decimal("0")),)
    charges = tuple((power, Decimal("0")) for power in _steps(ess.max_charge_kw, step_kw) if power)
    discharges = tuple((Decimal("0"), power) for power in _steps(ess.max_discharge_kw, step_kw) if power)
    return ((Decimal("0"), Decimal("0")), *charges, *discharges)


def _aligned_rates(rows: tuple[ScheduleInterval, ...], rates: tuple[ImportEnergyRate, ...]) -> dict[tuple[object, object], ImportEnergyRate]:
    result = {(rate.start, rate.end): rate for rate in rates}
    if len(result) != len(rates) or any((row.start, row.end) not in result for row in rows):
        raise DispatchSearchError("Tariff rates must uniquely cover the exact schedule intervals.")
    if any(not _nonnegative(rate.rate_mop_per_kwh) for rate in rates):
        raise DispatchSearchError("This prototype requires finite, non-negative import rates.")
    return result


def _materialize_candidate(request: DispatchSearchRequest, actions: tuple[tuple[tuple[Decimal, ...], Decimal, Decimal, Decimal | None], ...]) -> Schedule:
    task_ids = {task.asset_id for task in request.flexible_tasks}
    candidate_rows: list[ScheduleInterval] = []
    previous_soc = request.initial_soc_kwh
    for row, (task_powers, charge_kw, discharge_kw, next_soc) in zip(request.baseline.intervals, actions, strict=True):
        fixed_flows = tuple(flow for flow in row.flexible_loads if flow.asset_id not in task_ids)
        task_flows = tuple(
            FlexibleLoadFlow(task.asset_id, task.kind, power)
            for task, power in zip(request.flexible_tasks, task_powers, strict=True)
        )
        total_load = row.base_load_kw + sum((flow.power_kw for flow in fixed_flows + task_flows), Decimal("0"))
        residual = total_load + charge_kw - discharge_kw
        pv_used = min(row.pv_generation_kw, residual)
        grid_import = max(Decimal("0"), residual - row.pv_generation_kw)
        candidate_rows.append(ScheduleInterval(
            start=row.start,
            end=row.end,
            grid_import_kw=grid_import,
            pv_generation_kw=row.pv_generation_kw,
            pv_used_kw=pv_used,
            pv_export_kw=Decimal("0"),
            pv_curtailed_kw=row.pv_generation_kw - pv_used,
            ess_charge_kw=charge_kw,
            ess_discharge_kw=discharge_kw,
            base_load_kw=row.base_load_kw,
            flexible_loads=fixed_flows + task_flows,
            losses_kw=row.losses_kw,
            ess_soc_start_kwh=previous_soc,
            ess_soc_end_kwh=next_soc,
        ))
        previous_soc = next_soc
    return Schedule(tuple(candidate_rows))


def _steps(maximum: Decimal, step: Decimal, *, start: Decimal = Decimal("0")) -> tuple[Decimal, ...]:
    count = int((maximum / step).to_integral_value())
    first = int((start / step).to_integral_value())
    return tuple(step * index for index in range(first, count + 1))


def _soc_delta(power: Decimal, duration: Decimal, efficiency: Decimal, direction: str) -> Decimal:
    energy = power * duration
    return energy * efficiency if direction == "charge" else energy / efficiency


def _multiple(value: Decimal, quantum: Decimal) -> bool:
    return (value / quantum) == (value / quantum).to_integral_value()


def _positive(value: object) -> bool:
    return isinstance(value, Decimal) and value.is_finite() and value > 0


def _nonnegative(value: object) -> bool:
    return isinstance(value, Decimal) and value.is_finite() and value >= 0


def _unit_interval(value: object) -> bool:
    return isinstance(value, Decimal) and value.is_finite() and Decimal("0") < value <= Decimal("1")


def _usable_evidence(ref: EvidenceRef) -> bool:
    return isinstance(ref, EvidenceRef) and bool(ref.ref.strip()) and isinstance(ref.state, EvidenceState) and ref.state not in (EvidenceState.UNKNOWN, EvidenceState.STALE)

