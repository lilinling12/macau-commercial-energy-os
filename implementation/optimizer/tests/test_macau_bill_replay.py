import unittest
from datetime import date
from decimal import Decimal as D

from macau_energy_optimizer.dispatch_assessment import EvidenceRef, EvidenceState
from macau_energy_optimizer.macau_bill_replay import (
    BillRateCard,
    BillReplayRequest,
    MeterRegisterBlock,
    PeriodChargeRate,
    ReactiveKind,
    replay_b1_c1_bill_component,
)
from macau_energy_optimizer.macau_tariff_periods import EnergyPeriod, TariffVariant


ASSUMED = EvidenceRef("fixture:bill-registers", EvidenceState.PROJECT_ASSUMPTION)
CARD_EVIDENCE = EvidenceRef("fixture:published-tariff-parameters", EvidenceState.PROJECT_ASSUMPTION)
WINDOW_START = date(2026, 1, 1)
WINDOW_END = date(2027, 1, 1)


def card(tariff):
    periods = (
        (EnergyPeriod.B1_BUSY, EnergyPeriod.B1_LOW_LOAD)
        if tariff is TariffVariant.B1
        else (
            EnergyPeriod.C1_LOW_SEASON_BUSY,
            EnergyPeriod.C1_LOW_SEASON_LOW_LOAD,
            EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD,
            EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD_PEAK,
            EnergyPeriod.C1_HIGH_SEASON_LOW_LOAD,
        )
    )
    if tariff is TariffVariant.B1:
        active = (D("0.874"), D("0.767"))
        reactive = (D("0.348"), D("0.116"))
        demand = D("19.797")
    else:
        active = (D("0.776"), D("0.724"), D("1.432"), D("0.885"), D("0.749"))
        reactive = (D("0.348"), D("0.116"), D("0.348"), D("0.348"), D("0.116"))
        demand = D("19.797")
    return BillRateCard(
        tariff=tariff,
        effective_from=WINDOW_START,
        effective_to_exclusive=WINDOW_END,
        demand_rate_mop_per_kw=demand,
        demand_weight_k=D("0.20"),
        active_energy_rates=tuple(PeriodChargeRate(p, r) for p, r in zip(periods, active)),
        reactive_energy_rates=tuple(PeriodChargeRate(p, r) for p, r in zip(periods, reactive)),
        tariff_evidence=CARD_EVIDENCE,
    )


def block(period, active, reactive, tca="0.10", kind=None):
    return MeterRegisterBlock(period, D(active), D(reactive), D(tca), ASSUMED, kind)


def replay_b1(registers):
    return replay_b1_c1_bill_component(
        BillReplayRequest(
            billing_period_start=date(2026, 7, 1),
            billing_period_end_exclusive=date(2026, 8, 1),
            tariff=TariffVariant.B1,
            subscribed_demand_pc_kw=D("120"),
            measured_max_average_pu_kw=D("100"),
            registers=tuple(registers),
            contract_evidence=ASSUMED,
            demand_evidence=ASSUMED,
        ),
        card(TariffVariant.B1),
    )


class MacauBillReplayTests(unittest.TestCase):
    def test_b1_demand_active_reactive_and_tca_subtotal(self):
        result = replay_b1((
            block(EnergyPeriod.B1_BUSY, "1000", "700"),
            block(EnergyPeriod.B1_LOW_LOAD, "500", "100"),
        ))
        self.assertEqual(result.billed_demand_pf_kw, D("104.00"))
        self.assertEqual(result.demand_charge_mop, D("2058.88800"))
        self.assertEqual(result.active_energy_charge_mop, D("1257.500"))
        self.assertEqual(result.reactive_energy_charge_mop, D("139.200"))
        self.assertEqual(result.tca_charge_mop, D("150.00"))
        self.assertEqual(result.subtotal_excluding_tax_mop, D("3605.58800"))
        self.assertIn("government tax", result.excluded_components)

    def test_b1_reactive_excess_is_clamped_to_zero(self):
        result = replay_b1((
            block(EnergyPeriod.B1_BUSY, "100", "20"),
            block(EnergyPeriod.B1_LOW_LOAD, "100", "20"),
        ))
        self.assertEqual(result.reactive_energy_charge_mop, D("0.0"))

    def test_c1_seasonal_energy_rates_and_reactive_rules(self):
        rows = (
            block(EnergyPeriod.C1_LOW_SEASON_BUSY, "100", "80", kind=ReactiveKind.INDUCTIVE),
            block(EnergyPeriod.C1_LOW_SEASON_LOW_LOAD, "50", "10", kind=ReactiveKind.CAPACITIVE),
            block(EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD, "30", "30", kind=ReactiveKind.INDUCTIVE),
            block(EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD_PEAK, "40", "30", kind=ReactiveKind.INDUCTIVE),
            block(EnergyPeriod.C1_HIGH_SEASON_LOW_LOAD, "60", "5", kind=ReactiveKind.CAPACITIVE),
        )
        request = BillReplayRequest(
            billing_period_start=date(2026, 5, 1),
            billing_period_end_exclusive=date(2026, 10, 1),
            tariff=TariffVariant.C1,
            subscribed_demand_pc_kw=D("1000"),
            measured_max_average_pu_kw=D("800"),
            registers=rows,
            contract_evidence=ASSUMED,
            demand_evidence=ASSUMED,
        )
        result = replay_b1_c1_bill_component(request, card(TariffVariant.C1))
        self.assertEqual(result.billed_demand_pf_kw, D("840.00"))
        self.assertEqual(result.demand_charge_mop, D("16629.48000"))
        self.assertEqual(result.active_energy_charge_mop,
                         D("77.600+36.200+42.960+35.400+44.940"))
        self.assertEqual(result.reactive_energy_charge_mop,
                         D("6.960+1.160+4.176+2.088+0.580"))
        self.assertEqual(result.tca_charge_mop, D("28.50"))

    def test_c1_requires_direction_for_reactive_registers(self):
        rows = (
            block(EnergyPeriod.C1_LOW_SEASON_BUSY, "100", "80", kind=None),
            block(EnergyPeriod.C1_LOW_SEASON_LOW_LOAD, "50", "10", kind=ReactiveKind.CAPACITIVE),
            block(EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD, "30", "30", kind=ReactiveKind.INDUCTIVE),
            block(EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD_PEAK, "40", "30", kind=ReactiveKind.INDUCTIVE),
            block(EnergyPeriod.C1_HIGH_SEASON_LOW_LOAD, "60", "5", kind=ReactiveKind.CAPACITIVE),
        )
        request = BillReplayRequest(date(2026, 5, 1), date(2026, 10, 1), TariffVariant.C1,
                                    D("1000"), D("800"), rows, ASSUMED, ASSUMED)
        with self.assertRaisesRegex(ValueError, "requires reactive kind"):
            replay_b1_c1_bill_component(request, card(TariffVariant.C1))

    def test_missing_register_bucket_blocks_replay(self):
        with self.assertRaisesRegex(ValueError, "Missing tariff-period register blocks"):
            replay_b1((block(EnergyPeriod.B1_BUSY, "100", "0"),))

    def test_rate_card_must_cover_entire_bill_period(self):
        request = BillReplayRequest(date(2026, 12, 20), date(2027, 1, 20), TariffVariant.B1,
                                    D("120"), D("100"),
                                    (block(EnergyPeriod.B1_BUSY, "100", "0"),
                                     block(EnergyPeriod.B1_LOW_LOAD, "100", "0")),
                                    ASSUMED, ASSUMED)
        with self.assertRaisesRegex(ValueError, "does not cover"):
            replay_b1_c1_bill_component(request, card(TariffVariant.B1))

    def test_mixed_tariff_and_rate_card_is_rejected(self):
        request = BillReplayRequest(date(2026, 7, 1), date(2026, 8, 1), TariffVariant.B1,
                                    D("120"), D("100"),
                                    (block(EnergyPeriod.B1_BUSY, "100", "0"),
                                     block(EnergyPeriod.B1_LOW_LOAD, "100", "0")),
                                    ASSUMED, ASSUMED)
        with self.assertRaisesRegex(ValueError, "do not match"):
            replay_b1_c1_bill_component(request, card(TariffVariant.C1))


if __name__ == "__main__":
    unittest.main()
