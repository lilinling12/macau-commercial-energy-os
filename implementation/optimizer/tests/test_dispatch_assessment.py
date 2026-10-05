import unittest
from dataclasses import replace
from datetime import datetime, timedelta, timezone
from decimal import Decimal as D
from zoneinfo import ZoneInfo

from macau_energy_optimizer.dispatch_assessment import (
    AssessmentRequest,
    ClaimScope,
    ClaimStatus,
    ClaimType,
    EconomicContext,
    EconomicStatus,
    EssLimits,
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
from macau_energy_optimizer.dispatch_optimizer import DispatchSearchError, DispatchSearchRequest, FlexibleEnergyTask, generate_candidate


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
        ess_state_evidence=VERIFIED,
    )
    values.update(changes)
    return AssessmentRequest(**values)


class DispatchAssessmentTests(unittest.TestCase):
    def test_balanced_verified_schedule_returns_bounded_physical_result(self):
        result = assess_schedule(request())
        self.assertEqual(result.physical_status, PhysicalStatus.VALIDATED_WITHIN_SCOPE)
        self.assertEqual(result.baseline_import_energy_kwh, D("10.0"))
        self.assertIsNone(result.import_energy_charge_delta_mop)

    def test_missing_unknown_and_stale_candidate_pv_curtailment_withhold_feasibility(self):
        candidate = interval(
            grid="10", load="15",
            pv_generation_kw=D("7"), pv_used_kw=D("5"), pv_curtailed_kw=D("2"),
        )
        unresolved = (
            None,
            EvidenceRef("pv-curtailment:unknown", EvidenceState.UNKNOWN),
            EvidenceRef("pv-curtailment:stale", EvidenceState.STALE),
        )
        for evidence in unresolved:
            with self.subTest(evidence=evidence):
                result = assess_schedule(request(candidate=candidate, pv_curtailment_evidence=evidence))
                claims = {item.claim: item for item in result.claim_readiness}

                self.assertEqual(result.physical_status, PhysicalStatus.PARTIAL)
                self.assertEqual(claims[ClaimType.PV_CURTAILMENT].status, ClaimStatus.WITHHELD)
                self.assertEqual(claims[ClaimType.DISPATCH_FEASIBILITY].status, ClaimStatus.WITHHELD)
                self.assertIn("PV curtailment:", " ".join(result.reasons))

    def test_verified_candidate_pv_curtailment_is_bounded_and_zero_curtailment_needs_no_capability(self):
        candidate = interval(
            grid="10", load="15",
            pv_generation_kw=D("7"), pv_used_kw=D("5"), pv_curtailed_kw=D("2"),
        )
        verified = EvidenceRef("pv-curtailment:verified", EvidenceState.VERIFIED)
        result = assess_schedule(request(candidate=candidate, pv_curtailment_evidence=verified))
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(result.physical_status, PhysicalStatus.VALIDATED_WITHIN_SCOPE)
        self.assertEqual(claims[ClaimType.PV_CURTAILMENT].status, ClaimStatus.ALLOWED)
        self.assertEqual(claims[ClaimType.DISPATCH_FEASIBILITY].status, ClaimStatus.ALLOWED)

        assumed = EvidenceRef("pv-curtailment:assumption", EvidenceState.PROJECT_ASSUMPTION)
        scenario = assess_schedule(request(candidate=candidate, pv_curtailment_evidence=assumed))
        scenario_claims = {item.claim: item for item in scenario.claim_readiness}
        self.assertEqual(scenario.physical_status, PhysicalStatus.SCENARIO_ONLY)
        self.assertEqual(scenario_claims[ClaimType.PV_CURTAILMENT].scope, ClaimScope.SCENARIO_ONLY)
        self.assertEqual(scenario_claims[ClaimType.DISPATCH_FEASIBILITY].scope, ClaimScope.SCENARIO_ONLY)

        no_curtail = assess_schedule(request())
        no_curtail_claims = {item.claim: item for item in no_curtail.claim_readiness}
        self.assertEqual(no_curtail_claims[ClaimType.PV_CURTAILMENT].status, ClaimStatus.ALLOWED)

    def test_interval_comparison_exposes_source_load_and_storage_components(self):
        baseline = interval(
            grid="10", pv="5", load="15",
            ess_soc_start_kwh=D("4"), ess_soc_end_kwh=D("4"),
        )
        hvac = FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("1"))
        candidate = interval(
            grid="12", pv="5", load="14",
            pv_generation_kw=D("7"), pv_export_kw=D("2"),
            flexible_loads=(hvac,),
            ess_soc_start_kwh=D("4"), ess_soc_end_kwh=D("4"),
        )
        unknown_limit = FlexibleLoadLimit(
            "hvac-1", D("0"), D("2"), EvidenceRef("hvac:unknown", EvidenceState.UNKNOWN)
        )
        result = assess_schedule(request(
            baseline, candidate, flexible_load_limits=(unknown_limit,)
        ))
        row = result.interval_comparisons[0]
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(
            (row.baseline_pv_generation_kw, row.candidate_pv_generation_kw), (D("5"), D("7"))
        )
        self.assertEqual((row.baseline_pv_export_kw, row.candidate_pv_export_kw), (D("0"), D("2")))
        self.assertEqual((row.baseline_pv_curtailed_kw, row.candidate_pv_curtailed_kw), (D("0"), D("0")))
        self.assertEqual((row.baseline_base_load_kw, row.candidate_base_load_kw), (D("15"), D("14")))
        self.assertEqual(row.baseline_flexible_loads, ())
        self.assertEqual(row.candidate_flexible_loads, (hvac,))
        self.assertEqual(
            (row.baseline_ess_soc_start_kwh, row.baseline_ess_soc_end_kwh), (D("4"), D("4"))
        )
        self.assertEqual(
            (row.candidate_ess_soc_start_kwh, row.candidate_ess_soc_end_kwh), (D("4"), D("4"))
        )
        self.assertEqual(claims[ClaimType.FLEXIBLE_LOAD_DISPATCH].status, ClaimStatus.WITHHELD)

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

    def test_missing_unknown_and_stale_ess_soc_evidence_withhold_feasibility(self):
        baseline = interval(
            grid="10", load="15",
            ess_soc_start_kwh=D("5"), ess_soc_end_kwh=D("5"),
        )
        candidate = interval(
            grid="8", load="15", ess_discharge_kw=D("2"),
            ess_soc_start_kwh=D("5"), ess_soc_end_kwh=D("3"),
        )
        limits = EssLimits(D("5"), D("5"), D("0"), D("10"), D("1"), D("1"), VERIFIED)
        unresolved = (
            None,
            EvidenceRef("ess-soc:unknown", EvidenceState.UNKNOWN),
            EvidenceRef("ess-soc:stale", EvidenceState.STALE),
        )
        for evidence in unresolved:
            with self.subTest(evidence=evidence):
                result = assess_schedule(request(
                    baseline, candidate, ess_limits=limits, ess_state_evidence=evidence
                ))
                claims = {item.claim: item for item in result.claim_readiness}

                self.assertEqual(result.physical_status, PhysicalStatus.PARTIAL)
                self.assertEqual(claims[ClaimType.ESS_DISPATCH].status, ClaimStatus.WITHHELD)
                self.assertEqual(claims[ClaimType.DISPATCH_FEASIBILITY].status, ClaimStatus.WITHHELD)
                self.assertIn("ESS state of charge:", " ".join(result.reasons))

    def test_unknown_ess_constraint_keeps_import_profile_and_withholds_ess_claim(self):
        unknown = EvidenceRef("ess:unknown", EvidenceState.UNKNOWN)
        limits = EssLimits(D("5"), D("5"), D("0"), D("10"), D("1"), D("1"), unknown)
        baseline = interval(grid="10", load="15")
        candidate = interval(
            grid="8", load="15", ess_discharge_kw=D("2"),
            ess_soc_start_kwh=D("5"), ess_soc_end_kwh=D("3")
        )

        result = assess_schedule(request(baseline, candidate, ess_limits=limits))
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(result.physical_status, PhysicalStatus.PARTIAL)
        self.assertEqual(result.baseline_import_energy_kwh, D("10.0"))
        self.assertEqual(result.candidate_import_energy_kwh, D("8.0"))
        self.assertEqual(claims[ClaimType.GRID_IMPORT_PROFILE].status, ClaimStatus.ALLOWED)
        self.assertEqual(claims[ClaimType.ESS_DISPATCH].status, ClaimStatus.WITHHELD)
        self.assertEqual(claims[ClaimType.DISPATCH_FEASIBILITY].status, ClaimStatus.WITHHELD)
        self.assertIsNone(result.import_energy_charge_delta_mop)

    def test_missing_ess_limits_keeps_profile_and_withholds_ess_claim(self):
        baseline = interval(grid="10", load="15")
        candidate = interval(
            grid="8", load="15", ess_discharge_kw=D("2"),
            ess_soc_start_kwh=D("5"), ess_soc_end_kwh=D("3")
        )

        result = assess_schedule(request(baseline, candidate))
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(result.physical_status, PhysicalStatus.PARTIAL)
        self.assertEqual(result.candidate_import_energy_kwh, D("8.0"))
        self.assertEqual(claims[ClaimType.GRID_IMPORT_PROFILE].status, ClaimStatus.ALLOWED)
        self.assertEqual(claims[ClaimType.ESS_DISPATCH].status, ClaimStatus.WITHHELD)
        self.assertEqual(claims[ClaimType.DISPATCH_FEASIBILITY].status, ClaimStatus.WITHHELD)

    def test_unknown_flexible_load_limit_keeps_profile_but_cost_is_scenario_only(self):
        base_flow = FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("4"))
        candidate_flow = FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("3"))
        baseline = interval(grid="10", load="11", flexible_loads=(base_flow,))
        candidate = interval(grid="8", load="10", flexible_loads=(candidate_flow,))
        unknown = EvidenceRef("hvac-limit:stale", EvidenceState.STALE)
        limit = FlexibleLoadLimit("hvac-1", D("0"), D("5"), unknown)
        context = EconomicContext(
            account_meter_mapping=VERIFIED,
            contract=VERIFIED,
            tariff=VERIFIED,
            import_energy_rates=(ImportEnergyRate(START, END, D("1.25"), VERIFIED),),
        )

        result = assess_schedule(request(
            baseline, candidate, flexible_load_limits=(limit,), economic_context=context
        ))
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(result.physical_status, PhysicalStatus.PARTIAL)
        self.assertEqual(result.candidate_import_energy_kwh, D("8.0"))
        self.assertEqual(result.economic_status, EconomicStatus.SCENARIO_ONLY)
        self.assertEqual(result.candidate_import_energy_charge_mop, D("10.000"))
        self.assertEqual(claims[ClaimType.GRID_IMPORT_PROFILE].status, ClaimStatus.ALLOWED)
        self.assertEqual(claims[ClaimType.FLEXIBLE_LOAD_DISPATCH].status, ClaimStatus.WITHHELD)
        self.assertEqual(claims[ClaimType.GRID_IMPORT_ENERGY_COMPONENT].status, ClaimStatus.ALLOWED)
        self.assertEqual(claims[ClaimType.GRID_IMPORT_ENERGY_COMPONENT].scope, ClaimScope.SCENARIO_ONLY)
        self.assertEqual(claims[ClaimType.SAVINGS].status, ClaimStatus.WITHHELD)

    def test_missing_changed_flexible_load_limit_keeps_profile_and_withholds_claim(self):
        base_flow = FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("4"))
        candidate_flow = FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("3"))
        baseline = interval(grid="10", load="11", flexible_loads=(base_flow,))
        candidate = interval(grid="8", load="10", flexible_loads=(candidate_flow,))

        result = assess_schedule(request(baseline, candidate))
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(result.physical_status, PhysicalStatus.PARTIAL)
        self.assertEqual(result.candidate_import_energy_kwh, D("8.0"))
        self.assertEqual(claims[ClaimType.GRID_IMPORT_PROFILE].status, ClaimStatus.ALLOWED)
        self.assertEqual(claims[ClaimType.FLEXIBLE_LOAD_DISPATCH].status, ClaimStatus.WITHHELD)
        self.assertEqual(claims[ClaimType.DISPATCH_FEASIBILITY].status, ClaimStatus.WITHHELD)

    def test_electrical_feasibility_does_not_assert_comfort_service(self):
        baseline_flow = FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("4"))
        candidate_flow = FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("3"))
        baseline = interval(grid="10", load="11", flexible_loads=(baseline_flow,))
        candidate = interval(grid="9", load="11", flexible_loads=(candidate_flow,))
        limit = FlexibleLoadLimit("hvac-1", D("0"), D("5"), VERIFIED)

        result = assess_schedule(request(
            baseline, candidate, flexible_load_limits=(limit,)
        ))
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(result.physical_status, PhysicalStatus.VALIDATED_WITHIN_SCOPE)
        self.assertEqual(
            claims[ClaimType.DISPATCH_FEASIBILITY].status, ClaimStatus.ALLOWED
        )
        self.assertEqual(
            claims[ClaimType.COMFORT_SERVICE].status, ClaimStatus.WITHHELD
        )
        self.assertEqual(claims[ClaimType.COMFORT_SERVICE].scope, ClaimScope.NONE)
        self.assertIn("not modeled", " ".join(claims[ClaimType.COMFORT_SERVICE].reasons))

    def test_unknown_grid_guard_withholds_only_guard_compliance_claim(self):
        unknown = EvidenceRef("guard:unknown", EvidenceState.UNKNOWN)
        result = assess_schedule(request(
            grid_import_limit_kw=D("9"),
            grid_import_limit_evidence=unknown,
        ))
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(result.physical_status, PhysicalStatus.PARTIAL)
        self.assertEqual(result.candidate_import_energy_kwh, D("10.0"))
        self.assertEqual(claims[ClaimType.GRID_IMPORT_PROFILE].status, ClaimStatus.ALLOWED)
        self.assertEqual(claims[ClaimType.GRID_IMPORT_GUARD].status, ClaimStatus.WITHHELD)
        self.assertEqual(claims[ClaimType.DISPATCH_FEASIBILITY].status, ClaimStatus.WITHHELD)

    def test_missing_configured_grid_guard_evidence_withholds_only_guard_claim(self):
        result = assess_schedule(request(grid_import_limit_kw=D("9")))
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(result.physical_status, PhysicalStatus.PARTIAL)
        self.assertEqual(result.candidate_import_energy_kwh, D("10.0"))
        self.assertEqual(claims[ClaimType.GRID_IMPORT_PROFILE].status, ClaimStatus.ALLOWED)
        self.assertEqual(claims[ClaimType.GRID_IMPORT_GUARD].status, ClaimStatus.WITHHELD)
        self.assertEqual(claims[ClaimType.DISPATCH_FEASIBILITY].status, ClaimStatus.WITHHELD)

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

    def test_partial_rate_coverage_prices_only_exactly_covered_intervals(self):
        second_end = END + (END - START)
        baseline_first = interval()
        baseline_second = replace(interval(), start=END, end=second_end)
        candidate_first = interval(grid="9", load="14")
        candidate_second = replace(interval(), start=END, end=second_end)
        context = EconomicContext(
            account_meter_mapping=VERIFIED,
            contract=VERIFIED,
            tariff=VERIFIED,
            import_energy_rates=(ImportEnergyRate(START, END, D("1.25"), VERIFIED),),
        )

        req = request(economic_context=context)
        req = replace(
            req,
            baseline=Schedule((baseline_first, baseline_second)),
            candidate=Schedule((candidate_first, candidate_second)),
        )
        result = assess_schedule(req)
        claims = {item.claim: item for item in result.claim_readiness}

        self.assertEqual(result.economic_status, EconomicStatus.PARTIAL)
        self.assertEqual(result.baseline_import_energy_charge_mop, D("12.500"))
        self.assertEqual(result.candidate_import_energy_charge_mop, D("11.250"))
        self.assertEqual(result.import_energy_charge_delta_mop, D("-1.250"))
        self.assertEqual(result.economic_covered_intervals, ((START, END),))
        self.assertEqual(result.economic_total_interval_count, 2)
        self.assertEqual(len(result.economic_interval_components), 1)
        component = result.economic_interval_components[0]
        self.assertEqual((component.start, component.end), (START, END))
        self.assertEqual(component.rate_evidence_ref, VERIFIED.ref)
        self.assertEqual(component.rate_mop_per_kwh, D("1.25"))
        self.assertEqual(component.baseline_import_kwh, D("10.0"))
        self.assertEqual(component.candidate_import_kwh, D("9.0"))
        self.assertEqual(component.baseline_charge_mop, D("12.500"))
        self.assertEqual(component.candidate_charge_mop, D("11.250"))
        self.assertIn("1 of 2 schedule intervals", result.reasons[0])
        self.assertEqual(claims[ClaimType.GRID_IMPORT_ENERGY_COMPONENT].status, ClaimStatus.ALLOWED)
        self.assertEqual(claims[ClaimType.GRID_IMPORT_ENERGY_COMPONENT].scope, ClaimScope.PARTIAL)
        self.assertEqual(claims[ClaimType.SAVINGS].status, ClaimStatus.WITHHELD)

    def test_rate_boundary_inside_schedule_interval_is_withheld(self):
        midpoint = START + (END - START) / 2
        context = EconomicContext(
            account_meter_mapping=VERIFIED,
            contract=VERIFIED,
            tariff=VERIFIED,
            import_energy_rates=(
                ImportEnergyRate(START, midpoint, D("1.00"), VERIFIED),
                ImportEnergyRate(midpoint, END, D("2.00"), VERIFIED),
            ),
        )

        result = assess_schedule(request(economic_context=context))

        self.assertEqual(result.economic_status, EconomicStatus.BLOCKED)
        self.assertIsNone(result.baseline_import_energy_charge_mop)
        self.assertEqual(result.economic_covered_intervals, ())
        self.assertEqual(result.economic_interval_components, ())
        self.assertEqual(result.economic_total_interval_count, 1)
        self.assertIn("missing exact-interval import rate", result.reasons[1])

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

    def test_utc_instants_are_accepted_for_site_scoped_schedule(self):
        utc_start = START.astimezone(timezone.utc)
        utc_end = END.astimezone(timezone.utc)
        baseline = replace(interval(), start=utc_start, end=utc_end)
        candidate = replace(interval(), start=utc_start, end=utc_end)

        result = assess_schedule(request(baseline, candidate))

        self.assertEqual(result.physical_status, PhysicalStatus.VALIDATED_WITHIN_SCOPE)
        self.assertEqual(result.baseline_import_energy_kwh, D("10.0"))
        self.assertEqual(result.interval_comparisons[0].start.astimezone(TZ), START)

    def test_dst_fold_interval_uses_elapsed_utc_duration(self):
        zone = ZoneInfo("America/New_York")
        start = datetime(2026, 11, 1, 1, 30, tzinfo=zone, fold=0)
        end = datetime(2026, 11, 1, 1, 0, tzinfo=zone, fold=1)
        row = interval(start=start, end=end)

        result = assess_schedule(request(row, row))

        self.assertEqual(result.physical_status, PhysicalStatus.VALIDATED_WITHIN_SCOPE)
        self.assertEqual(row.duration_hours, D("0.5"))
        self.assertEqual(result.baseline_import_energy_kwh, D("5.0"))

    def test_dst_fold_gap_is_not_mistaken_for_contiguous_intervals(self):
        zone = ZoneInfo("America/New_York")
        first = interval(
            start=datetime(2026, 11, 1, 0, 30, tzinfo=zone),
            end=datetime(2026, 11, 1, 1, 0, tzinfo=zone, fold=0),
        )
        second = interval(
            start=datetime(2026, 11, 1, 1, 0, tzinfo=zone, fold=1),
            end=datetime(2026, 11, 1, 1, 30, tzinfo=zone, fold=1),
        )

        req = replace(
            request(),
            baseline=Schedule((first, second)),
            candidate=Schedule((first, second)),
        )
        result = assess_schedule(req)

        self.assertEqual(result.physical_status, PhysicalStatus.BLOCKED)
        self.assertIn("contiguous", result.reasons[0])

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


class DispatchOptimizerTests(unittest.TestCase):
    def test_exact_discrete_search_shifts_hvac_energy_to_lower_rate_window(self):
        start2 = START + timedelta(hours=1)
        baseline = Schedule((
            interval(grid="7", pv="0", load="5", start=START, end=END, pv_generation_kw=D("0"), flexible_loads=(FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("2")),)),
            interval(grid="5", pv="0", load="5", start=END, end=start2 + timedelta(hours=1), pv_generation_kw=D("0"), flexible_loads=()),
        ))
        rates = (
            ImportEnergyRate(START, END, D("3"), VERIFIED),
            ImportEnergyRate(END, start2 + timedelta(hours=1), D("1"), VERIFIED),
        )
        context = EconomicContext(VERIFIED, VERIFIED, VERIFIED, rates)
        task = FlexibleEnergyTask("hvac-1", FlexibleLoadKind.HVAC, D("2"), (True, True), D("1"), D("2"), VERIFIED)
        result = generate_candidate(DispatchSearchRequest(
            tenant_id="tenant-demo", site_id="site-demo", site_timezone="Asia/Macau",
            baseline=baseline, flexible_tasks=(task,), fixed_flexible_load_limits=(),
            physical_evidence=(VERIFIED,), economic_context=context,
            power_step_kw=D("1"), soc_step_kwh=D("1"),
        ))
        self.assertEqual(result.candidate.intervals[0].flexible_loads[0].power_kw, D("0"))
        self.assertEqual(result.candidate.intervals[1].flexible_loads[0].power_kw, D("2"))
        self.assertEqual(result.assessment.import_energy_charge_delta_mop, D("-4"))
        self.assertEqual(result.search_scope, "EXACT_WITHIN_DECLARED_DISCRETE_ACTION_SPACE")
        self.assertGreater(result.transitions_examined, 0)
        repeated = generate_candidate(DispatchSearchRequest(
            tenant_id="tenant-demo", site_id="site-demo", site_timezone="Asia/Macau",
            baseline=baseline, flexible_tasks=(task,), fixed_flexible_load_limits=(),
            physical_evidence=(VERIFIED,), economic_context=context,
            power_step_kw=D("1"), soc_step_kwh=D("1"),
        ))
        self.assertEqual(result.candidate, repeated.candidate)

    def test_search_coordinates_hvac_ev_and_hot_water_windows(self):
        ends = tuple(START + timedelta(hours=index) for index in range(1, 5))
        starts = (START, *ends[:-1])
        baselines = (
            (FlexibleLoadFlow("hvac-1", FlexibleLoadKind.HVAC, D("2")),),
            (FlexibleLoadFlow("ev-1", FlexibleLoadKind.EV, D("2")),),
            (FlexibleLoadFlow("water-1", FlexibleLoadKind.HOT_WATER, D("2")),),
            (),
        )
        baseline = Schedule(tuple(
            interval(grid=str(5 + sum((flow.power_kw for flow in flows), D("0"))), pv="0", load="5",
                     start=start, end=end, pv_generation_kw=D("0"), flexible_loads=flows)
            for start, end, flows in zip(starts, ends, baselines, strict=True)
        ))
        rates = tuple(ImportEnergyRate(start, end, rate, VERIFIED) for start, end, rate in zip(starts, ends, (D("4"), D("3"), D("2"), D("1")), strict=True))
        tasks = (
            FlexibleEnergyTask("hvac-1", FlexibleLoadKind.HVAC, D("2"), (True, True, False, False), D("2"), D("2"), VERIFIED),
            FlexibleEnergyTask("ev-1", FlexibleLoadKind.EV, D("2"), (False, True, True, False), D("2"), D("2"), VERIFIED),
            FlexibleEnergyTask("water-1", FlexibleLoadKind.HOT_WATER, D("2"), (False, False, True, True), D("2"), D("2"), VERIFIED),
        )
        result = generate_candidate(DispatchSearchRequest(
            tenant_id="tenant-demo", site_id="site-demo", site_timezone="Asia/Macau",
            baseline=baseline, flexible_tasks=tasks, fixed_flexible_load_limits=(),
            physical_evidence=(VERIFIED,), economic_context=EconomicContext(VERIFIED, VERIFIED, VERIFIED, rates),
            power_step_kw=D("2"), soc_step_kwh=D("1"),
        ))
        candidate_by_asset = {
            task.asset_id: tuple(index for index, row in enumerate(result.candidate.intervals)
                                 if any(flow.asset_id == task.asset_id and flow.power_kw > 0 for flow in row.flexible_loads))
            for task in tasks
        }
        self.assertEqual(candidate_by_asset, {"hvac-1": (1,), "ev-1": (2,), "water-1": (3,)})
        self.assertEqual(result.assessment.import_energy_charge_delta_mop, D("-6"))

    def test_search_dispatches_pv_surplus_through_storage_with_terminal_soc(self):
        end2 = END + timedelta(hours=1)
        baseline = Schedule((
            interval(grid="0", pv="3", load="3", start=START, end=END,
                     pv_generation_kw=D("5"), pv_curtailed_kw=D("2"), ess_soc_start_kwh=D("0"), ess_soc_end_kwh=D("0")),
            interval(grid="3", pv="0", load="3", start=END, end=end2,
                     pv_generation_kw=D("0"), pv_used_kw=D("0"), ess_soc_start_kwh=D("0"), ess_soc_end_kwh=D("0")),
        ))
        rates = (ImportEnergyRate(START, END, D("0.1"), VERIFIED), ImportEnergyRate(END, end2, D("1"), VERIFIED))
        limits = EssLimits(D("2"), D("2"), D("0"), D("2"), D("1"), D("1"), VERIFIED)
        result = generate_candidate(DispatchSearchRequest(
            tenant_id="tenant-demo", site_id="site-demo", site_timezone="Asia/Macau",
            baseline=baseline, flexible_tasks=(), fixed_flexible_load_limits=(),
            physical_evidence=(VERIFIED,), economic_context=EconomicContext(VERIFIED, VERIFIED, VERIFIED, rates),
            power_step_kw=D("2"), soc_step_kwh=D("2"), ess_limits=limits,
            ess_state_evidence=VERIFIED, initial_soc_kwh=D("0"),
        ))
        first, second = result.candidate.intervals
        self.assertEqual((first.ess_charge_kw, first.pv_used_kw, first.pv_curtailed_kw), (D("2"), D("5"), D("0")))
        self.assertEqual((second.ess_discharge_kw, second.grid_import_kw), (D("2"), D("1")))
        self.assertEqual((first.ess_soc_start_kwh, second.ess_soc_end_kwh), (D("0"), D("0")))
        self.assertEqual(result.assessment.import_energy_charge_delta_mop, D("-2"))

    def test_candidate_import_guard_does_not_reject_higher_baseline_import(self):
        end2 = END + timedelta(hours=1)
        baseline = Schedule((
            interval(grid="3", pv="0", load="1", start=START, end=END, pv_generation_kw=D("0"),
                     flexible_loads=(FlexibleLoadFlow("ev-1", FlexibleLoadKind.EV, D("2")),)),
            interval(grid="0", pv="1", load="1", start=END, end=end2, pv_generation_kw=D("2"),
                     pv_curtailed_kw=D("1"), flexible_loads=()),
        ))
        rates = (ImportEnergyRate(START, END, D("3"), VERIFIED), ImportEnergyRate(END, end2, D("1"), VERIFIED))
        task = FlexibleEnergyTask("ev-1", FlexibleLoadKind.EV, D("2"), (True, True), D("1"), D("2"), VERIFIED)
        result = generate_candidate(DispatchSearchRequest(
            tenant_id="tenant-demo", site_id="site-demo", site_timezone="Asia/Macau",
            baseline=baseline, flexible_tasks=(task,), fixed_flexible_load_limits=(),
            physical_evidence=(VERIFIED,), economic_context=EconomicContext(VERIFIED, VERIFIED, VERIFIED, rates),
            power_step_kw=D("1"), soc_step_kwh=D("1"), grid_import_limit_kw=D("2"),
            grid_import_limit_evidence=VERIFIED,
        ))
        self.assertEqual(result.assessment.physical_status, PhysicalStatus.VALIDATED_WITHIN_SCOPE)
        self.assertGreater(result.assessment.baseline_peak_grid_import_kw, D("2"))
        self.assertLessEqual(result.assessment.candidate_peak_grid_import_kw, D("2"))

    def test_search_rejects_unknown_rate_provenance(self):
        baseline = Schedule((interval(),))
        context = EconomicContext(VERIFIED, VERIFIED, VERIFIED, (ImportEnergyRate(START, END, D("1"), EvidenceRef("unknown", EvidenceState.UNKNOWN)),))
        with self.assertRaises(DispatchSearchError):
            generate_candidate(DispatchSearchRequest(
                tenant_id="tenant-demo", site_id="site-demo", site_timezone="Asia/Macau",
                baseline=baseline, flexible_tasks=(), fixed_flexible_load_limits=(),
                physical_evidence=(VERIFIED,), economic_context=context,
                power_step_kw=D("1"), soc_step_kwh=D("1"),
            ))

    def test_assumption_tagged_inputs_produce_scenario_only_result(self):
        baseline = Schedule((interval(),))
        scenario = EvidenceRef("scenario:load-profile", EvidenceState.PROJECT_ASSUMPTION)
        context = EconomicContext(VERIFIED, VERIFIED, VERIFIED, (ImportEnergyRate(START, END, D("1"), VERIFIED),))
        result = generate_candidate(DispatchSearchRequest(
            tenant_id="tenant-demo", site_id="site-demo", site_timezone="Asia/Macau",
            baseline=baseline, flexible_tasks=(), fixed_flexible_load_limits=(),
            physical_evidence=(scenario,), economic_context=context,
            power_step_kw=D("1"), soc_step_kwh=D("1"),
        ))
        self.assertTrue(result.scenario_only)
        self.assertEqual(result.assessment.claim_scope.value, "SCENARIO_ONLY")
        self.assertEqual(result.assessment.economic_status.value, "SCENARIO_ONLY")
        self.assertIn("scenario-only", " ".join(result.assessment.reasons))

    def test_search_enforces_transition_budget(self):
        baseline = Schedule((interval(),))
        baseline = Schedule((replace(baseline.intervals[0], ess_soc_start_kwh=D("0"), ess_soc_end_kwh=D("0")),))
        context = EconomicContext(VERIFIED, VERIFIED, VERIFIED, (ImportEnergyRate(START, END, D("1"), VERIFIED),))
        with self.assertRaises(DispatchSearchError):
            generate_candidate(DispatchSearchRequest(
                tenant_id="tenant-demo", site_id="site-demo", site_timezone="Asia/Macau",
                baseline=baseline, flexible_tasks=(), fixed_flexible_load_limits=(),
                physical_evidence=(VERIFIED,), economic_context=context,
                power_step_kw=D("1"), soc_step_kwh=D("1"), max_transitions=1,
                ess_limits=EssLimits(D("1"), D("1"), D("0"), D("1"), D("1"), D("1"), VERIFIED),
                ess_state_evidence=VERIFIED,
                initial_soc_kwh=D("0"),
            ))


if __name__ == "__main__":
    unittest.main()

