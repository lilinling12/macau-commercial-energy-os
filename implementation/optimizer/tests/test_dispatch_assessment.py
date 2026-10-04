import unittest
from dataclasses import replace
from datetime import datetime, timedelta
from decimal import Decimal as D
from zoneinfo import ZoneInfo

from macau_energy_optimizer.dispatch_assessment import (
    AssessmentRequest,
    EconomicContext,
    EvidenceRef,
    EvidenceState,
    FlexibleLoadFlow,
    FlexibleLoadKind,
    FlexibleLoadLimit,
    ImportEnergyRate,
    PhysicalStatus,
    Schedule,
    ScheduleInterval,
    assess_schedule,
)


TZ = ZoneInfo("Asia/Macau")
START = datetime(2026, 1, 5, 10, tzinfo=TZ)
END = START + timedelta(hours=1)
VERIFIED = EvidenceRef("fixture:verified", EvidenceState.VERIFIED)


def interval(*, grid="10", pv="5", load="15", **changes):
    row = ScheduleInterval(
        start=START,
        end=END,
        grid_import_kw=D(grid),
        pv_generation_kw=D("5"),
        pv_used_kw=D(pv),
        pv_export_kw=D("0"),
        pv_curtailed_kw=D("0"),
        ess_charge_kw=D("0"),
        ess_discharge_kw=D("0"),
        base_load_kw=D(load),
        flexible_loads=(),
    )
    return replace(row, **changes)


def request(baseline=None, candidate=None, **changes):
    values = dict(
        tenant_id="tenant-demo",
        site_id="site-demo",
        site_timezone="Asia/Macau",
        baseline=Schedule((baseline or interval(),)),
        candidate=Schedule((candidate or interval(),)),
        physical_evidence=(VERIFIED,),
    )
    values.update(changes)
    return AssessmentRequest(**values)


class DispatchAssessmentTests(unittest.TestCase):
    def test_balanced_verified_schedule_returns_bounded_physical_result(self):
        result = assess_schedule(request())
        self.assertEqual(result.physical_status, PhysicalStatus.VALIDATED_WITHIN_SCOPE)
        self.assertEqual(result.baseline_import_energy_kwh, D("10.0"))
        self.assertIsNone(result.import_energy_charge_delta_mop)

    def test_unbalanced_power_is_blocked_and_withholds_metrics(self):
        result = assess_schedule(request(candidate=interval(grid="9")))
        self.assertEqual(result.physical_status, PhysicalStatus.BLOCKED)
        self.assertIsNone(result.candidate_import_energy_kwh)

    def test_unknown_physical_evidence_blocks_assessment(self):
        result = assess_schedule(request(physical_evidence=(EvidenceRef("meter:unknown", EvidenceState.UNKNOWN),)))
        self.assertEqual(result.physical_status, PhysicalStatus.BLOCKED)

    def test_empty_evidence_reference_blocks_assessment(self):
        result = assess_schedule(request(physical_evidence=(EvidenceRef("  ", EvidenceState.VERIFIED),)))
        self.assertEqual(result.physical_status, PhysicalStatus.BLOCKED)

    def test_flexible_load_outside_verified_envelope_is_infeasible(self):
        flow = FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("4"))
        base = interval(grid="10", load="11", flexible_loads=(flow,))
        limits = (FlexibleLoadLimit("hvac-1", D("0"), D("3"), VERIFIED),)
        result = assess_schedule(request(base, base, flexible_load_limits=limits))
        self.assertEqual(result.physical_status, PhysicalStatus.INFEASIBLE)

    def test_grid_guard_is_applied_only_to_candidate(self):
        baseline = interval(grid="10")
        candidate = interval(grid="10")
        result = assess_schedule(request(baseline, candidate, grid_import_limit_kw=D("9"), grid_import_limit_evidence=VERIFIED))
        self.assertEqual(result.physical_status, PhysicalStatus.INFEASIBLE)

    def test_verified_exact_interval_rate_prices_only_import_energy_component(self):
        baseline = interval(grid="10", load="15")
        candidate = interval(grid="8", load="13")
        context = EconomicContext(
            account_meter_mapping=VERIFIED,
            contract=VERIFIED,
            tariff=VERIFIED,
            import_energy_rates=(ImportEnergyRate(START, END, D("1.25"), VERIFIED),),
        )
        result = assess_schedule(request(baseline, candidate, economic_context=context))
        self.assertEqual(result.candidate_import_energy_charge_mop, D("10.000"))
        self.assertEqual(result.import_energy_charge_delta_mop, D("-2.5000"))
        self.assertEqual(result.economic_component, "GRID_IMPORT_ENERGY_ONLY")
        self.assertIn("full-bill settlement are excluded", result.reasons[0])

    def test_unverified_tariff_withholds_all_money(self):
        context = EconomicContext(
            account_meter_mapping=VERIFIED,
            contract=VERIFIED,
            tariff=EvidenceRef("tariff:draft", EvidenceState.PROJECT_ASSUMPTION),
            import_energy_rates=(ImportEnergyRate(START, END, D("1.25"), VERIFIED),),
        )
        result = assess_schedule(request(economic_context=context))
        self.assertIsNone(result.baseline_import_energy_charge_mop)
        self.assertIsNone(result.import_energy_charge_delta_mop)

    def test_bad_site_timezone_is_blocked(self):
        result = assess_schedule(replace(request(), site_timezone="Mars/Olympus"))
        self.assertEqual(result.physical_status, PhysicalStatus.BLOCKED)

    def test_ess_soc_boundary_mismatch_withholds_economic_comparison(self):
        from macau_energy_optimizer.dispatch_assessment import EssLimits

        limits = EssLimits(D("5"), D("5"), D("0"), D("10"), D("1"), D("1"), VERIFIED)
        baseline = interval(
            grid="10", pv="5", load="15", ess_soc_start_kwh=D("5"), ess_soc_end_kwh=D("5")
        )
        candidate = interval(
            grid="8", pv="5", load="15", ess_discharge_kw=D("2"),
            ess_soc_start_kwh=D("4"), ess_soc_end_kwh=D("2")
        )
        context = EconomicContext(
            account_meter_mapping=VERIFIED,
            contract=VERIFIED,
            tariff=VERIFIED,
            import_energy_rates=(ImportEnergyRate(START, END, D("1"), VERIFIED),),
        )
        result = assess_schedule(request(baseline, candidate, ess_limits=limits, economic_context=context))
        self.assertEqual(result.physical_status, PhysicalStatus.VALIDATED_WITHIN_SCOPE)
        self.assertIsNone(result.import_energy_charge_delta_mop)
        self.assertIn("SOC boundary conditions differ", result.reasons[0])


if __name__ == "__main__":
    unittest.main()

