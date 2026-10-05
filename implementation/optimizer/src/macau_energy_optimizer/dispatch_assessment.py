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
    PARTIAL = "PARTIAL"
    BLOCKED = "BLOCKED"
    INFEASIBLE = "INFEASIBLE"


class EconomicStatus(StrEnum):
    COMPONENT_AVAILABLE = "COMPONENT_AVAILABLE"
    PARTIAL = "PARTIAL"
    SCENARIO_ONLY = "SCENARIO_ONLY"
    BLOCKED = "BLOCKED"


class ClaimScope(StrEnum):
    VERIFIED_BOUNDED = "VERIFIED_BOUNDED"
    SCENARIO_ONLY = "SCENARIO_ONLY"
    PARTIAL = "PARTIAL"
    NONE = "NONE"


class ClaimType(StrEnum):
    GRID_IMPORT_PROFILE = "GRID_IMPORT_PROFILE"
    HORIZON_PEAK = "HORIZON_PEAK"
    DISPATCH_FEASIBILITY = "DISPATCH_FEASIBILITY"
    ESS_DISPATCH = "ESS_DISPATCH"
    FLEXIBLE_LOAD_DISPATCH = "FLEXIBLE_LOAD_DISPATCH"
    GRID_IMPORT_GUARD = "GRID_IMPORT_GUARD"
    GRID_IMPORT_ENERGY_COMPONENT = "GRID_IMPORT_ENERGY_COMPONENT"
    DEMAND_CHARGE = "DEMAND_CHARGE"
    EXPORT_COMPENSATION = "EXPORT_COMPENSATION"
    FULL_BILL = "FULL_BILL"
    SAVINGS = "SAVINGS"
    CONTROLLABILITY = "CONTROLLABILITY"
    COMFORT_SERVICE = "COMFORT_SERVICE"
    CROSS_SITE_CREDIT = "CROSS_SITE_CREDIT"
    DEVICE_CONTROL = "DEVICE_CONTROL"


class ClaimStatus(StrEnum):
    ALLOWED = "ALLOWED"
    WITHHELD = "WITHHELD"


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
class ClaimReadiness:
    claim: ClaimType
    status: ClaimStatus
    scope: ClaimScope
    reasons: tuple[str, ...]
    subject: str | None = None


@dataclass(frozen=True, slots=True)
class AssessmentResult:
    tenant_id: str
    site_id: str
    physical_status: PhysicalStatus
    economic_status: EconomicStatus
    claim_scope: ClaimScope
    claim_readiness: tuple[ClaimReadiness, ...]
    reasons: tuple[str, ...]
    baseline_import_energy_kwh: Decimal | None
    candidate_import_energy_kwh: Decimal | None
    baseline_peak_grid_import_kw: Decimal | None
    candidate_peak_grid_import_kw: Decimal | None
    interval_comparisons: tuple[IntervalComparison, ...]
    baseline_import_energy_charge_mop: Decimal | None
    candidate_import_energy_charge_mop: Decimal | None
    import_energy_charge_delta_mop: Decimal | None
    economic_covered_intervals: tuple[tuple[datetime, datetime], ...]
    economic_total_interval_count: int
    economic_component: str | None


def _claim_readiness(
    request: AssessmentRequest,
    physical_status: PhysicalStatus,
    economic_status: EconomicStatus,
    scope: ClaimScope,
    reasons: tuple[str, ...],
    *,
    metrics_available: bool,
    economic_component_available: bool,
    unqualified: tuple[str, ...] = (),
) -> tuple[ClaimReadiness, ...]:
    claims: list[ClaimReadiness] = []

    def add(
        claim: ClaimType,
        status: ClaimStatus,
        claim_scope: ClaimScope,
        explanation: str,
        subject: str | None = None,
    ) -> None:
        claims.append(ClaimReadiness(claim, status, claim_scope, (explanation,), subject))

    qualified_scope = (
        ClaimScope.SCENARIO_ONLY
        if scope is ClaimScope.SCENARIO_ONLY
        else ClaimScope.VERIFIED_BOUNDED
    )
    profile_scope = qualified_scope if metrics_available else ClaimScope.NONE
    profile_state = ClaimStatus.ALLOWED if metrics_available else ClaimStatus.WITHHELD
    profile_reason = (
        "Profile is bounded to the supplied schedule window and evidence; the horizon peak is not billing-period Pu."
        if metrics_available
        else (reasons[0] if reasons else "Required physical inputs are unavailable.")
    )
    add(ClaimType.GRID_IMPORT_PROFILE, profile_state, profile_scope, profile_reason)
    add(ClaimType.HORIZON_PEAK, profile_state, profile_scope, profile_reason)

    feasibility_qualified = (
        metrics_available
        and physical_status in (PhysicalStatus.VALIDATED_WITHIN_SCOPE, PhysicalStatus.SCENARIO_ONLY)
        and not unqualified
    )
    add(
        ClaimType.DISPATCH_FEASIBILITY,
        ClaimStatus.ALLOWED if feasibility_qualified else ClaimStatus.WITHHELD,
        qualified_scope if feasibility_qualified else ClaimScope.NONE,
        "All applicable schedule constraints are evidenced within this bounded prototype."
        if feasibility_qualified
        else "Schedule feasibility is withheld because one or more required resource constraints are unresolved.",
    )

    uses_ess = any(
        row.ess_charge_kw > 0 or row.ess_discharge_kw > 0
        for schedule in (request.baseline, request.candidate)
        for row in schedule.intervals
    )
    if uses_ess:
        ess_issue = next((item for item in unqualified if item.startswith("ESS:")), None)
        ess_ready = metrics_available and ess_issue is None and physical_status in (
            PhysicalStatus.VALIDATED_WITHIN_SCOPE,
            PhysicalStatus.SCENARIO_ONLY,
            PhysicalStatus.PARTIAL,
        )
        add(
            ClaimType.ESS_DISPATCH,
            ClaimStatus.ALLOWED if ess_ready else ClaimStatus.WITHHELD,
            qualified_scope if ess_ready else ClaimScope.NONE,
            "ESS schedule is bounded by its supplied evidence."
            if ess_ready
            else (ess_issue or "ESS feasibility is withheld because the physical assessment is unavailable."),
        )

    changed_loads = _changed_flexible_load_ids(request)
    load_limits = {item.asset_id: item for item in request.flexible_load_limits}
    for asset_id in sorted(changed_loads):
        issue = next((item for item in unqualified if item.startswith(f"Flexible load {asset_id}:")), None)
        load_ready = metrics_available and issue is None and physical_status in (
            PhysicalStatus.VALIDATED_WITHIN_SCOPE,
            PhysicalStatus.SCENARIO_ONLY,
            PhysicalStatus.PARTIAL,
        )
        add(
            ClaimType.FLEXIBLE_LOAD_DISPATCH,
            ClaimStatus.ALLOWED if load_ready else ClaimStatus.WITHHELD,
            qualified_scope if load_ready else ClaimScope.NONE,
            "The changed flexible-load schedule is within its supplied evidence."
            if load_ready
            else (issue or f"Flexible-load feasibility for {asset_id} is withheld."),
            asset_id,
        )

    if request.grid_import_limit_kw is not None:
        guard_issue = next((item for item in unqualified if item.startswith("Grid import guard:")), None)
        guard_ready = metrics_available and guard_issue is None and physical_status in (
            PhysicalStatus.VALIDATED_WITHIN_SCOPE,
            PhysicalStatus.SCENARIO_ONLY,
            PhysicalStatus.PARTIAL,
        )
        add(
            ClaimType.GRID_IMPORT_GUARD,
            ClaimStatus.ALLOWED if guard_ready else ClaimStatus.WITHHELD,
            qualified_scope if guard_ready else ClaimScope.NONE,
            "The candidate remains within its supplied grid-import guard."
            if guard_ready
            else (guard_issue or "Grid-import guard compliance is withheld."),
        )

    economic_scope = (
        ClaimScope.SCENARIO_ONLY
        if economic_status is EconomicStatus.SCENARIO_ONLY
        else ClaimScope.PARTIAL
        if economic_component_available and economic_status is EconomicStatus.PARTIAL
        else ClaimScope.VERIFIED_BOUNDED
        if economic_component_available and economic_status is EconomicStatus.COMPONENT_AVAILABLE
        else ClaimScope.NONE
    )
    add(
        ClaimType.GRID_IMPORT_ENERGY_COMPONENT,
        ClaimStatus.ALLOWED if economic_component_available else ClaimStatus.WITHHELD,
        economic_scope,
        "Only the interval-matched grid-import energy component is available; this is not a full bill or realized savings."
        if economic_component_available
        else (reasons[0] if reasons else "Eligible economic evidence is unavailable."),
    )

    withheld_claims = (
        (ClaimType.DEMAND_CHARGE, "Billing-period Pu and demand-charge rules are not evaluated by this prototype."),
        (ClaimType.EXPORT_COMPENSATION, "Export remuneration, payee, and account applicability are not evaluated."),
        (ClaimType.FULL_BILL, "Taxes, demand components, and other bill items are outside the calculated energy component."),
        (ClaimType.SAVINGS, "A modeled import-energy component is not measured or realized savings."),
        (ClaimType.CONTROLLABILITY, "No site-qualified equipment capability or control authorization is established."),
        (ClaimType.COMFORT_SERVICE, "Thermal comfort and other service constraints are not modeled."),
        (ClaimType.CROSS_SITE_CREDIT, "No cross-building or cross-account credit is established."),
        (ClaimType.DEVICE_CONTROL, "This assessment has no equipment command path."),
    )
    for claim, reason in withheld_claims:
        add(claim, ClaimStatus.WITHHELD, ClaimScope.NONE, reason)
    return tuple(claims)


def _changed_flexible_load_ids(request: AssessmentRequest) -> set[str]:
    changed: set[str] = set()
    for baseline, candidate in zip(request.baseline.intervals, request.candidate.intervals):
        base = {flow.asset_id: flow.power_kw for flow in baseline.flexible_loads}
        proposed = {flow.asset_id: flow.power_kw for flow in candidate.flexible_loads}
        for asset_id in base.keys() | proposed.keys():
            if base.get(asset_id, Decimal("0")) != proposed.get(asset_id, Decimal("0")):
                changed.add(asset_id)
    return changed


def _unqualified_resource_claims(request: AssessmentRequest) -> tuple[str, ...]:
    issues: list[str] = []
    uses_ess = any(
        row.ess_charge_kw > 0 or row.ess_discharge_kw > 0
        for schedule in (request.baseline, request.candidate)
        for row in schedule.intervals
    )
    if uses_ess and (
        request.ess_limits is None
        or request.ess_limits.evidence.state in (EvidenceState.UNKNOWN, EvidenceState.STALE)
    ):
        issues.append("ESS: active ESS schedule has no current verified operating evidence; its feasibility claim is withheld.")
    load_limits = {item.asset_id: item for item in request.flexible_load_limits}
    for asset_id in sorted(_changed_flexible_load_ids(request)):
        limit = load_limits.get(asset_id)
        if limit is None or limit.evidence.state in (EvidenceState.UNKNOWN, EvidenceState.STALE):
            issues.append(f"Flexible load {asset_id}: changed load has no current verified operating envelope; its feasibility claim is withheld.")
    if request.grid_import_limit_kw is not None and (
        request.grid_import_limit_evidence is None
        or request.grid_import_limit_evidence.state in (EvidenceState.UNKNOWN, EvidenceState.STALE)
    ):
        issues.append("Grid import guard: limit evidence is missing, unknown, or stale; compliance claim is withheld.")
    return tuple(issues)


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
        if not request.physical_evidence:
            raise _Blocked("No core physical evidence was supplied for the schedule profile.")
        if any(item.state in (EvidenceState.UNKNOWN, EvidenceState.STALE) for item in request.physical_evidence):
            raise _Blocked("Core physical evidence is unknown or stale.")
        unqualified = _unqualified_resource_claims(request)

        _validate_schedule(request.baseline, request, is_candidate=False)
        _validate_schedule(request.candidate, request, is_candidate=True)
        comparisons = _comparisons(request.baseline, request.candidate)
        baseline_energy = _import_energy(request.baseline)
        candidate_energy = _import_energy(request.candidate)
        baseline_peak = max(row.grid_import_kw for row in request.baseline.intervals)
        candidate_peak = max(row.grid_import_kw for row in request.candidate.intervals)
        assumed = any(item.state is EvidenceState.PROJECT_ASSUMPTION for item in evidence)
        physical_status = (
            PhysicalStatus.SCENARIO_ONLY
            if assumed
            else PhysicalStatus.PARTIAL
            if unqualified
            else PhysicalStatus.VALIDATED_WITHIN_SCOPE
        )
        scope = (
            ClaimScope.SCENARIO_ONLY
            if assumed
            else ClaimScope.PARTIAL
            if unqualified
            else ClaimScope.VERIFIED_BOUNDED
        )
        economic = _evaluate_economics(request.economic_context, request, assumed or bool(unqualified))
        reasons = economic[1] + unqualified
        if assumed:
            reasons += ("One or more physical inputs use project assumptions; resulting comparisons are scenario-only.",)
        return AssessmentResult(
            tenant_id=request.tenant_id,
            site_id=request.site_id,
            physical_status=physical_status,
            economic_status=economic[0],
            claim_scope=scope,
            claim_readiness=_claim_readiness(
                request,
                physical_status,
                economic[0],
                scope,
                reasons,
                metrics_available=True,
                economic_component_available=economic[2] is not None,
                unqualified=unqualified,
            ),
            reasons=reasons,
            baseline_import_energy_kwh=baseline_energy,
            candidate_import_energy_kwh=candidate_energy,
            baseline_peak_grid_import_kw=baseline_peak,
            candidate_peak_grid_import_kw=candidate_peak,
            interval_comparisons=comparisons,
            baseline_import_energy_charge_mop=economic[2],
            candidate_import_energy_charge_mop=economic[3],
            import_energy_charge_delta_mop=economic[4],
            economic_covered_intervals=economic[5],
            economic_total_interval_count=len(request.baseline.intervals),
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
        claim_readiness=_claim_readiness(
            request,
            status,
            EconomicStatus.BLOCKED,
            ClaimScope.NONE,
            reasons,
            metrics_available=False,
            economic_component_available=False,
        ),
        reasons=reasons,
        baseline_import_energy_kwh=None,
        candidate_import_energy_kwh=None,
        baseline_peak_grid_import_kw=None,
        candidate_peak_grid_import_kw=None,
        interval_comparisons=(),
        baseline_import_energy_charge_mop=None,
        candidate_import_energy_charge_mop=None,
        import_energy_charge_delta_mop=None,
        economic_covered_intervals=(),
        economic_total_interval_count=len(request.baseline.intervals),
        economic_component=None,
    )


def _validate_request_shape(request: AssessmentRequest) -> None:
    if not request.tenant_id.strip() or not request.site_id.strip() or not request.site_timezone.strip():
        raise _Blocked("Tenant, site, and site timezone are required.")
    try:
        ZoneInfo(request.site_timezone)
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
    if active_ess and request.ess_limits is not None:
        items.append(request.ess_limits.evidence)
    active_load_ids = {flow.asset_id for s in (request.baseline, request.candidate) for row in s.intervals for flow in row.flexible_loads}
    load_limits = {item.asset_id: item for item in request.flexible_load_limits}
    if len(load_limits) != len(request.flexible_load_limits):
        raise _Blocked("Flexible-load operating envelopes must have unique asset IDs.")
    for asset_id in active_load_ids:
        limit = load_limits.get(asset_id)
        if limit is not None:
            items.append(limit.evidence)
    if request.grid_import_limit_kw is not None and request.grid_import_limit_evidence is not None:
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
            limit = load_limits.get(flow.asset_id)
            if limit is None:
                continue
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
            if limit.evidence.state not in (EvidenceState.UNKNOWN, EvidenceState.STALE) and (
                flow.power_kw < limit.min_power_kw or flow.power_kw > limit.max_power_kw
            ):
                raise _Infeasible(f"Flexible load {flow.asset_id} is outside its evidenced power envelope.")

        if row.ess_charge_kw > 0 and row.ess_discharge_kw > 0:
            raise _Infeasible("ESS cannot charge and discharge simultaneously in one interval.")
        active_ess = row.ess_charge_kw > 0 or row.ess_discharge_kw > 0
        has_soc_pair = row.ess_soc_start_kwh is not None and row.ess_soc_end_kwh is not None
        if (row.ess_soc_start_kwh is None) != (row.ess_soc_end_kwh is None):
            raise _Blocked("ESS SOC endpoints must be supplied as a pair.")
        if has_soc_pair:
            start_soc, end_soc = row.ess_soc_start_kwh, row.ess_soc_end_kwh
            if (
                not isinstance(start_soc, Decimal)
                or not isinstance(end_soc, Decimal)
                or not start_soc.is_finite()
                or not end_soc.is_finite()
                or start_soc < 0
                or end_soc < 0
            ):
                raise _Blocked("ESS SOC values must be finite, non-negative Decimal kWh values.")
            if ess is not None and ess.evidence.state not in (EvidenceState.UNKNOWN, EvidenceState.STALE):
                if start_soc < ess.min_soc_kwh or end_soc < ess.min_soc_kwh or start_soc > ess.max_soc_kwh or end_soc > ess.max_soc_kwh:
                    raise _Infeasible("ESS SOC is outside its evidenced minimum/maximum range.")
                if previous_soc is not None and start_soc != previous_soc:
                    raise _Blocked("ESS SOC is discontinuous between adjacent intervals.")
                expected_soc = start_soc + row.ess_charge_kw * row.duration_hours * ess.charge_efficiency - row.ess_discharge_kw * row.duration_hours / ess.discharge_efficiency
                _check_equal(expected_soc, end_soc, "ESS SOC transition does not match AC power, duration, and efficiency.")
                previous_soc = end_soc
                soc_tracking_started = True
        elif soc_tracking_started:
            raise _Blocked("ESS SOC continuity is missing after SOC tracking has started.")
        elif active_ess and ess is not None and ess.evidence.state is EvidenceState.VERIFIED:
            raise _Blocked("ESS activity with verified limits requires SOC endpoints.")

        if ess is not None and ess.evidence.state not in (EvidenceState.UNKNOWN, EvidenceState.STALE):
            if row.ess_charge_kw > ess.max_charge_kw or row.ess_discharge_kw > ess.max_discharge_kw:
                raise _Infeasible("ESS power exceeds its evidenced charge/discharge rating.")

        guard_evidence = request.grid_import_limit_evidence
        guard_qualified = guard_evidence is not None and guard_evidence.state not in (EvidenceState.UNKNOWN, EvidenceState.STALE)
        if is_candidate and request.grid_import_limit_kw is not None and guard_qualified and row.grid_import_kw > request.grid_import_limit_kw:
            raise _Infeasible("Candidate grid import exceeds the evidenced import guard.")


def _evaluate_economics(
    context: EconomicContext | None,
    request: AssessmentRequest,
    scenario_only: bool,
) -> tuple[
    EconomicStatus,
    tuple[str, ...],
    Decimal | None,
    Decimal | None,
    Decimal | None,
    tuple[tuple[datetime, datetime], ...],
]:
    total_count = len(request.baseline.intervals)
    if context is None:
        return EconomicStatus.BLOCKED, ("No account/meter/contract/tariff evidence was supplied; monetary output is withheld.",), None, None, None, ()
    context_evidence = (context.account_meter_mapping, context.contract, context.tariff)
    rate_evidence = tuple(rate.evidence for rate in context.import_energy_rates)
    if any(not _is_well_formed_evidence(item) for item in (*context_evidence, *rate_evidence)):
        return EconomicStatus.BLOCKED, ("Every economic evidence reference must have a non-empty ID and a recognized state.",), None, None, None, ()
    if any(item.state is not EvidenceState.VERIFIED for item in context_evidence):
        return EconomicStatus.BLOCKED, ("Account, contract, and tariff applicability evidence must be verified.",), None, None, None, ()

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
            return EconomicStatus.BLOCKED, ("Comparable ESS economics require evidenced SOC at the schedule-window start and end for both schedules.",), None, None, None, ()
        if base_start != candidate_start or base_end != candidate_end:
            return EconomicStatus.BLOCKED, ("ESS economics are withheld because baseline and candidate SOC boundary conditions differ.",), None, None, None, ()

    rates_by_interval: dict[tuple[datetime, datetime], list[ImportEnergyRate]] = {}
    for rate in context.import_energy_rates:
        rates_by_interval.setdefault((rate.start, rate.end), []).append(rate)
    covered_rows: list[ScheduleInterval] = []
    covered_rates: dict[tuple[datetime, datetime], ImportEnergyRate] = {}
    withheld: list[str] = []
    for row in baseline_rows:
        key = (row.start, row.end)
        matching = rates_by_interval.get(key, [])
        if len(matching) != 1:
            reason = "missing" if not matching else "ambiguous duplicate"
            withheld.append(f"{row.start.isoformat()}–{row.end.isoformat()}: {reason} exact-interval import rate")
            continue
        rate = matching[0]
        if rate.evidence.state is not EvidenceState.VERIFIED:
            withheld.append(f"{row.start.isoformat()}–{row.end.isoformat()}: import-rate evidence is not verified")
            continue
        if not rate.rate_mop_per_kwh.is_finite() or rate.rate_mop_per_kwh < 0:
            withheld.append(f"{row.start.isoformat()}–{row.end.isoformat()}: import rate is invalid")
            continue
        covered_rows.append(row)
        covered_rates[key] = rate

    covered_intervals = tuple((row.start, row.end) for row in covered_rows)
    if not covered_rows:
        summary = "No schedule interval has exactly matched, verified, valid import-rate evidence."
        return EconomicStatus.BLOCKED, (summary, *withheld), None, None, None, ()

    covered_schedule = Schedule(tuple(covered_rows))
    baseline = _import_charge(covered_schedule, covered_rates)
    candidate_schedule = Schedule(tuple(candidate_rows[index] for index, row in enumerate(baseline_rows) if (row.start, row.end) in covered_rates))
    candidate = _import_charge(candidate_schedule, covered_rates)
    delta = candidate - baseline
    if scenario_only:
        status = EconomicStatus.SCENARIO_ONLY
        summary = "The import-energy component is scenario-only because at least one physical input or resource constraint is unresolved."
    elif len(covered_rows) < total_count:
        status = EconomicStatus.PARTIAL
        summary = f"Import-energy component covers {len(covered_rows)} of {total_count} schedule intervals; uncovered intervals are excluded, not treated as zero."
    else:
        status = EconomicStatus.COMPONENT_AVAILABLE
        summary = "Only the evidenced grid-import energy component is calculated; demand, tax, export credit, and full-bill settlement are excluded."
    reasons = (summary, *withheld)
    return status, reasons, baseline, candidate, delta, covered_intervals


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

