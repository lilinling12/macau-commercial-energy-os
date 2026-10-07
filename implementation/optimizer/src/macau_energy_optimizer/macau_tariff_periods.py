"""Effective-dated Macau Group B1/C1 active-energy rate mapping.

This is a narrow SHADOW input adapter, not a tariff bill calculator. It maps
half-open intervals that do not cross tariff boundaries to caller-supplied,
evidence-referenced rates. B2/B3/C2 transformer-loss corrections and all
demand, reactive, tax, export, and full-bill calculations remain out of scope.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal
from enum import StrEnum

from .dispatch_assessment import EvidenceRef, ImportEnergyRate


_MACAU = timezone(timedelta(hours=8), name="Asia/Macau")
_UTC = timezone.utc


class TariffVariant(StrEnum):
    B1 = "B1"
    C1 = "C1"


class EnergyPeriod(StrEnum):
    B1_BUSY = "B1_BUSY"
    B1_LOW_LOAD = "B1_LOW_LOAD"
    C1_LOW_SEASON_BUSY = "C1_LOW_SEASON_BUSY"
    C1_LOW_SEASON_LOW_LOAD = "C1_LOW_SEASON_LOW_LOAD"
    C1_HIGH_SEASON_FULL_LOAD = "C1_HIGH_SEASON_FULL_LOAD"
    C1_HIGH_SEASON_FULL_LOAD_PEAK = "C1_HIGH_SEASON_FULL_LOAD_PEAK"
    C1_HIGH_SEASON_LOW_LOAD = "C1_HIGH_SEASON_LOW_LOAD"


@dataclass(frozen=True, slots=True)
class PeriodRate:
    period: EnergyPeriod
    base_mop_per_kwh: Decimal


@dataclass(frozen=True, slots=True)
class RateCard:
    tariff: TariffVariant
    effective_from: date
    effective_to_exclusive: date
    periods: tuple[PeriodRate, ...]
    tariff_clause_adjustment_mop_per_kwh: Decimal
    evidence: EvidenceRef

    def __post_init__(self) -> None:
        if self.effective_to_exclusive <= self.effective_from:
            raise ValueError("Rate-card effective window must be non-empty.")
        if not isinstance(self.tariff_clause_adjustment_mop_per_kwh, Decimal):
            raise TypeError("TCA must be Decimal.")
        required = _required_periods(self.tariff)
        supplied = [row.period for row in self.periods]
        if len(supplied) != len(set(supplied)):
            raise ValueError("Rate card contains duplicate tariff periods.")
        if set(supplied) != required:
            raise ValueError("Rate card must define every required period exactly once.")
        for row in self.periods:
            if not isinstance(row.base_mop_per_kwh, Decimal):
                raise TypeError("Base tariff rates must be Decimal.")
            if row.base_mop_per_kwh < 0:
                raise ValueError("Base tariff rates cannot be negative.")
            if row.base_mop_per_kwh + self.tariff_clause_adjustment_mop_per_kwh < 0:
                raise ValueError("Base rate plus TCA cannot be negative.")

    def rate_for(self, period: EnergyPeriod) -> Decimal:
        for row in self.periods:
            if row.period is period:
                return row.base_mop_per_kwh + self.tariff_clause_adjustment_mop_per_kwh
        raise ValueError(f"No rate configured for period {period}.")


def build_import_energy_rates(
    intervals: tuple[tuple[datetime, datetime], ...],
    card: RateCard,
) -> tuple[ImportEnergyRate, ...]:
    """Map tariff periods into the existing per-interval SHADOW rate input.

    Macau tariff time bands are interpreted in Asia/Macau local time. Any
    interval crossing midnight, an effective-date edge, or a tariff boundary
    is rejected so the caller must split and align it before optimization.
    Evidence is carried through; it is not authenticated by this function.
    """
    result: list[ImportEnergyRate] = []
    for start, end in intervals:
        if start.tzinfo is None or start.utcoffset() is None:
            raise ValueError("Interval start must be timezone-aware.")
        if end.tzinfo is None or end.utcoffset() is None:
            raise ValueError("Interval end must be timezone-aware.")
        start_utc = start.astimezone(_UTC)
        end_utc = end.astimezone(_UTC)
        if end_utc <= start_utc:
            raise ValueError("Tariff interval must have positive duration.")

        local_start = start_utc.astimezone(_MACAU)
        local_last = (end_utc - timedelta(microseconds=1)).astimezone(_MACAU)
        if not (card.effective_from <= local_start.date() < card.effective_to_exclusive):
            raise ValueError("Interval start is outside the rate-card effective window.")
        if not (card.effective_from <= local_last.date() < card.effective_to_exclusive):
            raise ValueError("Interval end is outside the rate-card effective window.")
        _reject_crossed_boundaries(start_utc, end_utc, local_start.date(), local_last.date(), card.tariff)
        period = _period_at(card.tariff, local_start)
        result.append(
            ImportEnergyRate(
                start=start,
                end=end,
                rate_mop_per_kwh=card.rate_for(period),
                evidence=card.evidence,
            )
        )
    return tuple(result)


def _required_periods(tariff: TariffVariant) -> set[EnergyPeriod]:
    if tariff is TariffVariant.B1:
        return {EnergyPeriod.B1_BUSY, EnergyPeriod.B1_LOW_LOAD}
    return {
        EnergyPeriod.C1_LOW_SEASON_BUSY,
        EnergyPeriod.C1_LOW_SEASON_LOW_LOAD,
        EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD,
        EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD_PEAK,
        EnergyPeriod.C1_HIGH_SEASON_LOW_LOAD,
    }


def _period_at(tariff: TariffVariant, local: datetime) -> EnergyPeriod:
    clock = local.timetz().replace(tzinfo=None)
    if tariff is TariffVariant.B1:
        if time(9, 0) <= clock < time(20, 0):
            return EnergyPeriod.B1_BUSY
        return EnergyPeriod.B1_LOW_LOAD

    high_season = 6 <= local.month <= 9
    if not high_season:
        if time(9, 30) <= clock < time(20, 30):
            return EnergyPeriod.C1_LOW_SEASON_BUSY
        return EnergyPeriod.C1_LOW_SEASON_LOW_LOAD

    if time(10, 30) <= clock < time(13, 0) or time(14, 30) <= clock < time(16, 0):
        return EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD
    if (
        time(9, 30) <= clock < time(10, 30)
        or time(13, 0) <= clock < time(14, 30)
        or time(16, 0) <= clock < time(20, 30)
    ):
        return EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD_PEAK
    return EnergyPeriod.C1_HIGH_SEASON_LOW_LOAD


def _reject_crossed_boundaries(
    start_utc: datetime,
    end_utc: datetime,
    first_date: date,
    last_date: date,
    tariff: TariffVariant,
) -> None:
    if tariff is TariffVariant.B1:
        daily_boundaries = (time(0, 0), time(9, 0), time(20, 0))
    else:
        daily_boundaries = (
            time(0, 0),
            time(9, 30),
            time(10, 30),
            time(13, 0),
            time(14, 30),
            time(16, 0),
            time(20, 30),
        )

    day = first_date
    while day <= last_date:
        for clock in daily_boundaries:
            boundary = datetime.combine(day, clock, tzinfo=_MACAU).astimezone(_UTC)
            if start_utc < boundary < end_utc:
                raise ValueError("Split intervals at every Macau tariff/effective-date boundary.")
        day += timedelta(days=1)
