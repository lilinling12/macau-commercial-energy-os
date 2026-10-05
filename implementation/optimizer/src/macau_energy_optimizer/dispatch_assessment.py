"""Bounded, deterministic SHADOW assessment for source/load schedules.

This module validates a supplied schedule. It does not generate or optimize one.
All power values are average kW over half-open, timezone-aware intervals. Costs,
when eligible, cover only an explicitly evidenced grid-import energy component.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from enum import StrEnum
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


class EvidenceState(StrEnum):
    VERIFIED = "VERIFIED"
    PROJECT_ASSUMPTION = "PROJECT_ASSUMPTION"
    UNKNOWN = "UNKNOWN"
    STALE = "STALE"


class PhysicalStatus(StrEnum):
    VALIDATED_WITHIN_SCOPE = "VALIDATED_WITHIN_SCOPE"
    SCENARIO_ONLY = "SCENARIO_ONLY"
    BLOCKED = "BLOCKED"
    INFEASIBLE = "INFEASIBLE"


class EconomicStatus(StrEnum):
    COMPONENT_AVAILABLE = "COMPONENT_AVAILABLE"
    SCENARIO_ONLY = "SCENARIO_ONLY"
    BLOCKED = "BLOCKED"


class ClaimScope(StrEnum):
    VERIFIED_BOUNDED = "VERIFIED_BOUNDED"
    SCENARIO_ONLY = "SCENARIO_ONLY"
    NONE = "NONE"


class FlexibleLoadKind(StrEnum):
    HVAC = "HVAC"
    EV = "EV"
    HOT_WATER = "HOT_WATER"
    OTHER = "OTHER"


@dataclass(frozen=True, slots=True)
class EvidenceRef:
    ref: str
    state: EvidenceState


@dataclass(frozen=True, slots=True)
class FlexibleLoadFlow:
    asset_id: str
    kind: FlexibleLoadKind
    power_kw: Decimal


@dataclass(frozen=True, slots=True)
class ScheduleInterval:
    start: datetime
    end: datetime
    grid_import_kw: Decimal
    pv_generation_kw: Decimal
    pv_used_kw: Decimal
    pv_export_kw: Decimal
    pv_curtailed_kw: Decimal
    ess_charge_kw: Decimal
    ess_discharge_kw: Decimal
    base_load_kw: Decimal
    flexible_loads: tuple[FlexibleLoadFlow, ...]
    losses_kw: Decimal = Decimal("0")
    ess_soc_start_kwh: Decimal | None = None
    ess_soc_end_kwh: Decimal | None = None

    @property
    def total_load_kw(self) -> Decimal:
        return self.base_load_kw + sum((load.power_kw for load in self.flexible_loads), Decimal("0"))

    @property
    def duration_hours(self) -> Decimal:
        # Duration is elapsed time between instants, even across local clock changes.
        seconds = Decimal(str((self.end.astimezone(timezone.utc) - self.start.astimezone(timezone.utc)).total_seconds()))
        return seconds / Decimal("3600")


@dataclass(frozen=True, slots=True)
class Schedule:
    intervals: tuple[ScheduleInterval, ...]


@dataclass(frozen=True, slots=True)
class FlexibleLoadLimit:
    asset_id: str
    min_power_kw: Decimal
    max_power_kw: Decimal
    evidence: EvidenceRef


@dataclass(frozen=True, slots=True)
class EssLimits:
    max_charge_kw: Decimal
    max_discharge_kw: Decimal
    min_soc_kwh: Decimal
    max_soc_kwh: Decimal
    charge_efficiency: Decimal
    discharge_efficiency: Decimal
    evidence: EvidenceRef


@dataclass(frozen=True, slots=True)
class ImportEnergyRate:
    start: datetime
    end: datetime
    rate_mop_per_kwh: Decimal
    evidence: EvidenceRef


@dataclass(frozen=True, slots=True)
class EconomicContext:
    account_meter_mapping: EvidenceRef
    contract: EvidenceRef
    tariff: EvidenceRef
    import_energy_rates: tuple[ImportEnergyRate, ...]


@dataclass(frozen=True, slots=True)
class AssessmentRequest:
    tenant_id: str
    site_id: str
    site_timezone: str
    baseline: Schedule
    candidate: Schedule
    physical_evidence: tuple[EvidenceRef, ...]
    flexible_load_limits: tuple[FlexibleLoadLimit, ...] = ()
    ess_limits: EssLimits | None = None
    grid_import_limit_kw: Decimal | None = None
    grid_import_limit_evidence: EvidenceRef | None = None
    economic_context: EconomicContext | None = None


@dataclass(frozen=True, slots=True)
class IntervalComparison:
    start: datetime
    end: datetime
    baseline_grid_import_kw: Decimal
    candidate_grid_import_kw: Decimal
    baseline_total_load_kw: Decimal
    candidate_total_load_kw: Decimal
    baseline_pv_used_kw: Decimal
    candidate_pv_used_kw: Decimal
    baseline_ess_charge_kw: Decimal
    candidate_ess_charge_kw: Decimal
    baseline_ess_discharge_kw: Decimal
    candidate_ess_discharge_kw: Decimal


@dataclass(frozen=True, slots=True)
class AssessmentResult:
    tenant_id: str
    site_id: str
    physical_status: PhysicalStatus
    economic_status: EconomicStatus
    claim_scope: ClaimScope
    reasons: tuple[str, ...]
    baseline_import_energy_kwh: Decimal | None
    candidate_import_energy_kwh: Decimal | None
    baseline_peak_grid_import_kw: Decimal | None
    candidate_peak_grid_import_kw: Decimal | None
    interval_comparisons: tuple[IntervalComparison, ...]
    baseline_import_energy_charge_mop: Decimal | None
    candidate_import_energy_charge_mop: Decimal | None
    import_energy_charge_delta_mop: Decimal | None
    economic_component: str | None


class _Blocked(Exception):
    pass


class _Infeasible(Exception):
    pass


def assess_schedule(request: AssessmentRequest) -> AssessmentResult:
    """Validate one baseline/candidate pair and optionally price an eligible component.

    This assessment is advisory and bounded. It does not optimize, establish site
    comfort/service feasibility, reconstruct a complete bill, or authorize control.
    """
    try:
        _validate_request_shape(request)
        evidence = _applicable_evidence(request)
        if not evidence:
            raise _Blocked("No evidence references were supplied for the physical assessment.")
        if any(item.state in (EvidenceState.UNKNOWN, EvidenceState.STALE) for item in evidence):
            raise _Blocked("Required physical evidence is unknown or stale.")

        _validate_schedule(request.baseline, request, is_candidate=False)
        _validate_schedule(request.candidate, request, is_candidate=True)
        comparisons = _comparisons(request.baseline, request.candidate)
        baseline_energy = _import_energy(request.baseline)
        candidate_energy = _import_energy(request.candidate)
        baseline_peak = max(row.grid_import_kw for row in request.baseline.intervals)
        candidate_peak = max(row.grid_import_kw for row in request.candidate.intervals)
        assumed = any(item.state is EvidenceState.PROJECT_ASSUMPTION for item in evidence)
        physical_status = PhysicalStatus.SCENARIO_ONLY if assumed else PhysicalStatus.VALIDATED_WITHIN_SCOPE
        scope = ClaimScope.SCENARIO_ONLY if assumed else ClaimScope.VERIFIED_BOUNDED
        economic = _evaluate_economics(request.economic_context, request, assumed)
        reasons = economic[1]
        if assumed:
            reasons += ("One or more physical inputs use project assumptions; all resulting comparisons are scenario-only.",)
        return AssessmentResult(
            tenant_id=request.tenant_id,
            site_id=request.site_id,
            physical_status=physical_status,
            economic_status=economic[0],
            claim_scope=scope,
            reasons=reasons,
            baseline_import_energy_kwh=baseline_energy,
            candidate_import_energy_kwh=candidate_energy,
            baseline_peak_grid_import_kw=baseline_peak,
            candidate_peak_grid_import_kw=candidate_peak,
            interval_comparisons=comparisons,
            baseline_import_energy_charge_mop=economic[2],
            candidate_import_energy_charge_mop=economic[3],
            import_energy_charge_delta_mop=economic[4],
            economic_component="GRID_IMPORT_ENERGY_ONLY" if economic[2] is not None else None,
        )
    except _Infeasible as error:
        return _empty_result(request, PhysicalStatus.INFEASIBLE, (str(error),))
    except _Blocked as error:
        return _empty_result(request, PhysicalStatus.BLOCKED, (str(error),))
    except (ArithmeticError, TypeError, ValueError) as error:
        return _empty_result(request, PhysicalStatus.BLOCKED, (f"Invalid assessment input: {error}",))


def _empty_result(request: AssessmentRequest, status: PhysicalStatus, reasons: tuple[str, ...]) -> AssessmentResult:
    return AssessmentResult(
        tenant_id=request.tenant_id,
        site_id=request.site_id,
        physical_status=status,
        economic_status=EconomicStatus.BLOCKED,
        claim_scope=ClaimScope.NONE,
        reasons=reasons,
        baseline_import_energy_kwh=None,
        candidate_import_energy_kwh=None,
        baseline_peak_grid_import_kw=None,
        candidate_peak_grid_import_kw=None,
        interval_comparisons=(),
        baseline_import_energy_charge_mop=None,
        candidate_import_energy_charge_mop=None,
        import_energy_charge_delta_mop=None,
        economic_component=None,
    )


def _validate_request_shape(request: AssessmentRequest) -> None:
    if not request.tenant_id.strip() or not request.site_id.strip() or not request.site_timezone.strip():
        raise _Blocked("Tenant, site, and site timezone are required.")
    try:
        site_zone = ZoneInfo(request.site_timezone)
    except (ZoneInfoNotFoundError, ValueError) as error:
        raise _Blocked("Site timezone must be a valid IANA timezone.") from error
    if request.grid_import_limit_kw is not None and (
        not isinstance(request.grid_import_limit_kw, Decimal)
        or not request.grid_import_limit_kw.is_finite()
        or request.grid_import_limit_kw < 0
    ):
        raise _Blocked("Grid-import limit must be a finite, non-negative Decimal kW value.")
    baseline = request.baseline.intervals
    candidate = request.candidate.intervals
    if not baseline or len(baseline) != len(candidate):
        raise _Blocked("Baseline and candidate must contain the same non-empty interval count.")
    if tuple((row.start, row.end) for row in baseline) != tuple((row.start, row.end) for row in candidate):
        raise _Blocked("Baseline and candidate must use identical half-open time intervals.")
    for schedule in (request.baseline, request.candidate):
        rows = schedule.intervals
        for index, row in enumerate(rows):
            if row.start.tzinfo is None or row.start.utcoffset() is None or row.end.tzinfo is None or row.end.utcoffset() is None:
                raise _Blocked("All interval timestamps must be timezone-aware.")
            if row.end <= row.start:
                raise _Blocked("Each interval must have positive duration.")
            # Timestamps identify instants and may be encoded in UTC or another
            # explicit offset. site_timezone is the business/tariff clock, not a
            # requirement that every timestamp retain that local wall-clock form.
            # Validate the named zone above, preserve the input instant, and use
            # the site zone only when interpreting local calendars/boundaries.
            if index and rows[index - 1].end != row.start:
                raise _Blocked("Schedule intervals must be ordered, contiguous, and non-overlapping.")


def _applicable_evidence(request: AssessmentRequest) -> tuple[EvidenceRef, ...]:
    items = list(request.physical_evidence)
    active_ess = any(row.ess_charge_kw > 0 or row.ess_discharge_kw > 0 for s in (request.baseline, request.candidate) for row in s.intervals)
    if active_ess:
        if request.ess_limits is None:
            raise _Blocked("ESS power/SOC/efficiency limits are required when the schedule uses storage.")
        items.append(request.ess_limits.evidence)
    active_load_ids = {flow.asset_id for s in (request.baseline, request.candidate) for row in s.intervals for flow in row.flexible_loads}
    load_limits = {item.asset_id: item for item in request.flexible_load_limits}
    if len(load_limits) != len(request.flexible_load_limits):
        raise _Blocked("Flexible-load operating envelopes must have unique asset IDs.")
    for asset_id in active_load_ids:
        limit = load_limits.get(asset_id)
        if limit is None:
            raise _Blocked(f"No evidenced operating envelope was supplied for flexible load {asset_id}.")
        items.append(limit.evidence)
    if request.grid_import_limit_kw is not None:
        if request.grid_import_limit_evidence is None:
            raise _Blocked("A grid-import limit requires a supporting evidence reference.")
        items.append(request.grid_import_limit_evidence)
    if any(not _is_well_formed_evidence(item) for item in items):
        raise _Blocked("Every evidence reference must have a non-empty ID and a recognized state.")
    return tuple(items)


def _validate_schedule(schedule: Schedule, request: AssessmentRequest, *, is_candidate: bool) -> None:
    load_limits = {item.asset_id: item for item in request.flexible_load_limits}
    ess = request.ess_limits
    previous_soc: Decimal | None = None
    soc_tracking_started = False
    if ess is not None:
        ess_values = (ess.max_charge_kw, ess.max_discharge_kw, ess.min_soc_kwh, ess.max_soc_kwh)
        if any(not isinstance(value, Decimal) or not value.is_finite() or value < 0 for value in ess_values):
            raise _Blocked("ESS ratings and SOC bounds must be finite, non-negative Decimal values.")
        if ess.min_soc_kwh > ess.max_soc_kwh or not _unit_interval(ess.charge_efficiency) or not _unit_interval(ess.discharge_efficiency):
            raise _Blocked("ESS SOC bounds or charge/discharge efficiencies are invalid.")
    for row in schedule.intervals:
        values = (
            row.grid_import_kw, row.pv_generation_kw, row.pv_used_kw, row.pv_export_kw,
            row.pv_curtailed_kw, row.ess_charge_kw, row.ess_discharge_kw,
            row.base_load_kw, row.losses_kw,
        )
        if any(not isinstance(value, Decimal) or not value.is_finite() or value < 0 for value in values):
            raise _Blocked("Power values must be finite, non-negative Decimal kW values.")
        if row.duration_hours <= 0:
            raise _Blocked("Each interval must have positive duration.")
        _check_equal(
            row.pv_generation_kw,
            row.pv_used_kw + row.pv_export_kw + row.pv_curtailed_kw,
            "PV generation must equal on-site use + export + curtailment.",
        )
        supply = row.grid_import_kw + row.pv_used_kw + row.ess_discharge_kw
        demand = row.total_load_kw + row.ess_charge_kw + row.pv_export_kw + row.losses_kw
        _check_equal(supply, demand, "Physical AC power balance does not reconcile for an interval.")

        flow_ids = [flow.asset_id for flow in row.flexible_loads]
        if len(set(flow_ids)) != len(flow_ids):
            raise _Blocked("A flexible-load asset may appear only once per interval.")
        for flow in row.flexible_loads:
            if (
                not flow.asset_id.strip()
                or not isinstance(flow.kind, FlexibleLoadKind)
                or not isinstance(flow.power_kw, Decimal)
                or not flow.power_kw.is_finite()
                or flow.power_kw < 0
            ):
                raise _Blocked("Flexible-load flows require an asset ID and finite non-negative Decimal kW.")
            limit = load_limits[flow.asset_id]
            if (
                not isinstance(limit.min_power_kw, Decimal)
                or not isinstance(limit.max_power_kw, Decimal)
                or not limit.min_power_kw.is_finite()
                or not limit.max_power_kw.is_finite()
                or limit.min_power_kw < 0
                or limit.max_power_kw < 0
                or limit.min_power_kw > limit.max_power_kw
            ):
                raise _Blocked(f"Invalid operating envelope for flexible load {flow.asset_id}.")
            if flow.power_kw < limit.min_power_kw or flow.power_kw > limit.max_power_kw:
                raise _Infeasible(f"Flexible load {flow.asset_id} is outside its evidenced power envelope.")

        if row.ess_charge_kw > 0 and row.ess_discharge_kw > 0:
            raise _Infeasible("ESS cannot charge and discharge simultaneously in one interval.")
        active_ess = row.ess_charge_kw > 0 or row.ess_discharge_kw > 0
        if active_ess and (row.ess_soc_start_kwh is None or row.ess_soc_end_kwh is None or ess is None):
            raise _Blocked("ESS activity requires SOC endpoints and evidenced ESS limits.")
        if row.ess_soc_start_kwh is not None or row.ess_soc_end_kwh is not None:
            if row.ess_soc_start_kwh is None or row.ess_soc_end_kwh is None or ess is None:
                raise _Blocked("ESS SOC endpoints must be paired with an evidenced ESS model.")
            start_soc, end_soc = row.ess_soc_start_kwh, row.ess_soc_end_kwh
            if not isinstance(start_soc, Decimal) or not isinstance(end_soc, Decimal):
                raise _Blocked("ESS SOC values must be Decimal kWh values.")
            if not start_soc.is_finite() or not end_soc.is_finite() or start_soc < ess.min_soc_kwh or end_soc < ess.min_soc_kwh or start_soc > ess.max_soc_kwh or end_soc > ess.max_soc_kwh:
                raise _Infeasible("ESS SOC is outside its evidenced minimum/maximum range.")
            if previous_soc is not None and start_soc != previous_soc:
                raise _Blocked("ESS SOC is discontinuous between adjacent intervals.")
            expected_soc = start_soc + row.ess_charge_kw * row.duration_hours * ess.charge_efficiency - row.ess_discharge_kw * row.duration_hours / ess.discharge_efficiency
            _check_equal(expected_soc, end_soc, "ESS SOC transition does not match AC power, duration, and efficiency.")
            previous_soc = end_soc
            soc_tracking_started = True
        elif soc_tracking_started:
            raise _Blocked("ESS SOC continuity is missing after SOC tracking has started.")

        if ess is not None:
            if row.ess_charge_kw > ess.max_charge_kw or row.ess_discharge_kw > ess.max_discharge_kw:
                raise _Infeasible("ESS power exceeds its evidenced charge/discharge rating.")

        if is_candidate and request.grid_import_limit_kw is not None and row.grid_import_kw > request.grid_import_limit_kw:
            raise _Infeasible("Candidate grid import exceeds the evidenced import guard.")


def _evaluate_economics(context: EconomicContext | None, request: AssessmentRequest, assumed: bool) -> tuple[EconomicStatus, tuple[str, ...], Decimal | None, Decimal | None, Decimal | None]:
    if context is None:
        return EconomicStatus.BLOCKED, ("No account/meter/contract/tariff evidence was supplied; monetary output is withheld.",), None, None, None
    evidence = (context.account_meter_mapping, context.contract, context.tariff, *(rate.evidence for rate in context.import_energy_rates))
    if any(not _is_well_formed_evidence(item) for item in evidence):
        return EconomicStatus.BLOCKED, ("Every economic evidence reference must have a non-empty ID and a recognized state.",), None, None, None
    if any(item.state is not EvidenceState.VERIFIED for item in evidence):
        return EconomicStatus.BLOCKED, ("Account, contract, tariff, and import-rate evidence must all be verified.",), None, None, None
    if len(context.import_energy_rates) != len(request.baseline.intervals):
        return EconomicStatus.BLOCKED, ("A verified import-energy rate is required for every schedule interval.",), None, None, None
    baseline_rows = request.baseline.intervals
    candidate_rows = request.candidate.intervals
    uses_ess = any(
        row.ess_charge_kw > 0 or row.ess_discharge_kw > 0
        for schedule in (request.baseline, request.candidate)
        for row in schedule.intervals
    )
    if uses_ess:
        base_start = baseline_rows[0].ess_soc_start_kwh
        candidate_start = candidate_rows[0].ess_soc_start_kwh
        base_end = baseline_rows[-1].ess_soc_end_kwh
        candidate_end = candidate_rows[-1].ess_soc_end_kwh
        if None in (base_start, candidate_start, base_end, candidate_end):
            return EconomicStatus.BLOCKED, ("Comparable ESS economics require evidenced SOC at the schedule-window start and end for both schedules.",), None, None, None
        if base_start != candidate_start or base_end != candidate_end:
            return EconomicStatus.BLOCKED, ("ESS economics are withheld because baseline and candidate SOC boundary conditions differ.",), None, None, None
    rates = {(rate.start, rate.end): rate for rate in context.import_energy_rates}
    if len(rates) != len(context.import_energy_rates):
        return EconomicStatus.BLOCKED, ("Import-energy rates contain duplicate intervals.",), None, None, None
    for row in request.baseline.intervals:
        rate = rates.get((row.start, row.end))
        if rate is None or rate.rate_mop_per_kwh < 0 or not rate.rate_mop_per_kwh.is_finite():
            return EconomicStatus.BLOCKED, ("Import-energy rates do not cover the exact schedule intervals.",), None, None, None
    baseline = _import_charge(request.baseline, rates)
    candidate = _import_charge(request.candidate, rates)
    status = EconomicStatus.SCENARIO_ONLY if assumed else EconomicStatus.COMPONENT_AVAILABLE
    return status, ("Only the evidenced grid-import energy component is calculated; demand, tax, export credit, and full-bill settlement are excluded.",), baseline, candidate, candidate - baseline


def _import_energy(schedule: Schedule) -> Decimal:
    return sum((row.grid_import_kw * row.duration_hours for row in schedule.intervals), Decimal("0"))


def _import_charge(schedule: Schedule, rates: dict[tuple[datetime, datetime], ImportEnergyRate]) -> Decimal:
    return sum((row.grid_import_kw * row.duration_hours * rates[(row.start, row.end)].rate_mop_per_kwh for row in schedule.intervals), Decimal("0"))


def _comparisons(baseline: Schedule, candidate: Schedule) -> tuple[IntervalComparison, ...]:
    return tuple(
        IntervalComparison(
            start=left.start,
            end=left.end,
            baseline_grid_import_kw=left.grid_import_kw,
            candidate_grid_import_kw=right.grid_import_kw,
            baseline_total_load_kw=left.total_load_kw,
            candidate_total_load_kw=right.total_load_kw,
            baseline_pv_used_kw=left.pv_used_kw,
            candidate_pv_used_kw=right.pv_used_kw,
            baseline_ess_charge_kw=left.ess_charge_kw,
            candidate_ess_charge_kw=right.ess_charge_kw,
            baseline_ess_discharge_kw=left.ess_discharge_kw,
            candidate_ess_discharge_kw=right.ess_discharge_kw,
        )
        for left, right in zip(baseline.intervals, candidate.intervals, strict=True)
    )


def _check_equal(actual: Decimal, expected: Decimal, message: str) -> None:
    if actual != expected:
        raise _Blocked(message)


def _unit_interval(value: Decimal) -> bool:
    return isinstance(value, Decimal) and value.is_finite() and Decimal("0") < value <= Decimal("1")


def _is_well_formed_evidence(item: EvidenceRef) -> bool:
    return isinstance(item, EvidenceRef) and bool(item.ref.strip()) and isinstance(item.state, EvidenceState)

