import unittest
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal as D

from macau_energy_optimizer.dispatch_assessment import EvidenceRef, EvidenceState
from macau_energy_optimizer.macau_tariff_periods import (
    EnergyPeriod,
    PeriodRate,
    RateCard,
    TariffVariant,
    build_import_energy_rates,
)


TZ = timezone(timedelta(hours=8), name="Asia/Macau")
ASSUMED = EvidenceRef("fixture:scenario-rate-card", EvidenceState.PROJECT_ASSUMPTION)


def card(tariff, *, valid_from=date(2026, 1, 1), valid_to=date(2027, 1, 1), tca=D("0.10")):
    if tariff is TariffVariant.B1:
        periods = (
            PeriodRate(EnergyPeriod.B1_BUSY, D("0.874")),
            PeriodRate(EnergyPeriod.B1_LOW_LOAD, D("0.767")),
        )
    else:
        periods = (
            PeriodRate(EnergyPeriod.C1_LOW_SEASON_BUSY, D("0.776")),
            PeriodRate(EnergyPeriod.C1_LOW_SEASON_LOW_LOAD, D("0.724")),
            PeriodRate(EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD, D("1.432")),
            PeriodRate(EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD_PEAK, D("0.885")),
            PeriodRate(EnergyPeriod.C1_HIGH_SEASON_LOW_LOAD, D("0.749")),
        )
    return RateCard(tariff, valid_from, valid_to, periods, tca, ASSUMED)


def mapped(tariff, start, end):
    return build_import_energy_rates(((start, end),), card(tariff))[0].rate_mop_per_kwh


class MacauTariffPeriodsTests(unittest.TestCase):
    def test_b1_full_load_window_and_tca(self):
        self.assertEqual(mapped(TariffVariant.B1, datetime(2026, 7, 1, 9, 0, tzinfo=TZ),
                                datetime(2026, 7, 1, 10, 0, tzinfo=TZ)), D("0.974"))
        self.assertEqual(mapped(TariffVariant.B1, datetime(2026, 7, 1, 19, 0, tzinfo=TZ),
                                datetime(2026, 7, 1, 20, 0, tzinfo=TZ)), D("0.974"))

    def test_b1_low_load_boundary(self):
        self.assertEqual(mapped(TariffVariant.B1, datetime(2026, 7, 1, 20, 0, tzinfo=TZ),
                                datetime(2026, 7, 1, 21, 0, tzinfo=TZ)), D("0.867"))
        self.assertEqual(mapped(TariffVariant.B1, datetime(2026, 7, 1, 8, 0, tzinfo=TZ),
                                datetime(2026, 7, 1, 9, 0, tzinfo=TZ)), D("0.867"))

    def test_c1_low_season_boundaries(self):
        self.assertEqual(mapped(TariffVariant.C1, datetime(2026, 5, 31, 9, 30, tzinfo=TZ),
                                datetime(2026, 5, 31, 10, 0, tzinfo=TZ)), D("0.876"))
        self.assertEqual(mapped(TariffVariant.C1, datetime(2026, 5, 31, 20, 30, tzinfo=TZ),
                                datetime(2026, 5, 31, 21, 0, tzinfo=TZ)), D("0.824"))

    def test_c1_high_season_all_period_edges(self):
        expected = (
            (time(10, 30), "1.532"),
            (time(13, 0), "0.985"),
            (time(14, 30), "1.532"),
            (time(16, 0), "0.985"),
            (time(20, 30), "0.849"),
        )
        for start_clock, expected_rate in expected:
            start = datetime.combine(date(2026, 6, 1), start_clock, tzinfo=TZ)
            self.assertEqual(mapped(TariffVariant.C1, start, start + timedelta(minutes=15)), D(expected_rate))

    def test_c1_season_switches(self):
        low = mapped(TariffVariant.C1, datetime(2026, 5, 31, 12, 0, tzinfo=TZ),
                     datetime(2026, 5, 31, 12, 15, tzinfo=TZ))
        high = mapped(TariffVariant.C1, datetime(2026, 6, 1, 12, 0, tzinfo=TZ),
                      datetime(2026, 6, 1, 12, 15, tzinfo=TZ))
        september = mapped(TariffVariant.C1, datetime(2026, 9, 30, 12, 0, tzinfo=TZ),
                           datetime(2026, 9, 30, 12, 15, tzinfo=TZ))
        october = mapped(TariffVariant.C1, datetime(2026, 10, 1, 12, 0, tzinfo=TZ),
                         datetime(2026, 10, 1, 12, 15, tzinfo=TZ))
        self.assertEqual(low, D("0.876"))
        self.assertEqual(high, D("1.532"))
        self.assertEqual(september, D("1.532"))
        self.assertEqual(october, D("0.876"))

    def test_intervals_crossing_tariff_boundaries_are_rejected(self):
        start = datetime(2026, 6, 1, 10, 0, tzinfo=TZ)
        with self.assertRaisesRegex(ValueError, "Split intervals"):
            build_import_energy_rates(((start, start + timedelta(hours=5)),), card(TariffVariant.C1))

    def test_interval_crossing_midnight_is_rejected(self):
        start = datetime(2026, 6, 1, 23, 30, tzinfo=TZ)
        with self.assertRaisesRegex(ValueError, "Split intervals"):
            build_import_energy_rates(((start, start + timedelta(hours=1)),), card(TariffVariant.C1))

    def test_naive_or_nonpositive_interval_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            build_import_energy_rates(((datetime(2026, 6, 1, 10), datetime(2026, 6, 1, 11, tzinfo=TZ)),),
                                      card(TariffVariant.C1))
        instant = datetime(2026, 6, 1, 10, tzinfo=TZ)
        with self.assertRaisesRegex(ValueError, "positive duration"):
            build_import_energy_rates(((instant, instant),), card(TariffVariant.C1))

    def test_outside_effective_window_is_rejected(self):
        start = datetime(2025, 12, 31, 23, 30, tzinfo=TZ)
        with self.assertRaisesRegex(ValueError, "outside the rate-card effective window"):
            build_import_energy_rates(((start, start + timedelta(minutes=15)),), card(TariffVariant.C1))

    def test_evidence_reference_is_preserved(self):
        start = datetime(2026, 6, 1, 10, 30, tzinfo=TZ)
        result = build_import_energy_rates(((start, start + timedelta(minutes=15)),), card(TariffVariant.C1))[0]
        self.assertEqual(result.evidence, ASSUMED)


if __name__ == "__main__":
    unittest.main()
