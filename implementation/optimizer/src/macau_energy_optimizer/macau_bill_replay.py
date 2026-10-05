"""Historical Macau B1/C1 tariff component replay for SHADOW validation.

This replays an evidence-qualified historical bill component from already
classified meter registers. It is not a complete bill or forecast dispatch
settlement engine. It supports only B1/C1, whose tariff periods do not require
the B2/B3/C2 transformer-loss corrections described by the applicable rules.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import StrEnum

from .dispatch_assessment import EvidenceRef
from .macau_tariff_periods import EnergyPeriod, TariffVariant


ZERO = Decimal("0")
SIXTY_PERCENT = Decimal("0.6")


class ReactiveKind(StrEnum):
    INDUCTIVE = "INDUCTIVE"
    CAPACITIVE = "CAPACITIVE"


@dataclass(frozen=True, slots=True)
class PeriodChargeRate:
    period: EnergyPeriod
    mop_per_unit: Decimal


@dataclass(frozen=True, slots=True)
class BillRateCard:
    tariff: TariffVariant
    effective_from: date
    effective_to_exclusive: date
    demand_rate_mop_per_kw: Decimal
    demand_weight_k: Decimal
    active_energy_rates: tuple[PeriodChargeRate, ...]
    reactive_energy_rates: tuple[PeriodChargeRate, ...]
    tariff_evidence: EvidenceRef

    def __post_init__(self) -> None:
        if self.effective_to_exclusive <= self.effective_from:
            raise ValueError("Rate-card effective window must be non-empty.")
        if not isinstance(self.demand_rate_mop_per_kw, Decimal) or self.demand_rate_mop_per_kw < ZERO:
            raise ValueError("Demand rate must be a non-negative Decimal.")
        if not isinstance(self.demand_weight_k, Decimal) or not ZERO <= self.demand_weight_k <= Decimal("1"):
            raise ValueError("Demand weighting factor must be a Decimal in [0, 1].")
        _validate_rates(self.active_energy_rates, _periods(self.tariff), "active")
        _validate_rates(self.reactive_energy_rates, _periods(self.tariff), "reactive")

    def active_rate(self, period: EnergyPeriod) -> Decimal:
        return _rate_for(self.active_energy_rates, period)

    def reactive_rate(self, period: EnergyPeriod) -> Decimal:
        return _rate_for(self.reactive_energy_rates, period)


@dataclass(frozen=True, slots=True)
class MeterRegisterBlock:
    period: EnergyPeriod
    active_kwh: Decimal
    reactive_kvarh: Decimal
    tca_mop_per_kwh: Decimal
    evidence: EvidenceRef
    reactive_kind: ReactiveKind | None = None


@dataclass(frozen=True, slots=True)
class BillReplayRequest:
    billing_period_start: date
    billing_period_end_exclusive: date
    tariff: TariffVariant
    subscribed_demand_pc_kw: Decimal
    measured_max_average_pu_kw: Decimal
    registers: tuple[MeterRegisterBlock, ...]
    contract_evidence: EvidenceRef
    demand_evidence: EvidenceRef


@dataclass(frozen=True, slots=True)
class PeriodReplay:
    period: EnergyPeriod
    active_kwh: Decimal
    active_energy_charge_mop: Decimal
    billable_reactive_kvarh: Decimal
    reactive_energy_charge_mop: Decimal
    tca_charge_mop: Decimal


@dataclass(frozen=True, slots=True)
class BillReplayResult:
    tariff: TariffVariant
    billed_demand_pf_kw: Decimal
    demand_charge_mop: Decimal
    active_energy_charge_mop: Decimal
    reactive_energy_charge_mop: Decimal
    tca_charge_mop: Decimal
    subtotal_excluding_tax_mop: Decimal
    period_breakdown: tuple[PeriodReplay, ...]
    excluded_components: tuple[str, ...] = (
        "government tax",
        "PV export/feed-in settlement",
        "full-bill rounding/adjustments",
        "B2/B3/C2 transformer loss corrections",
    )


def replay_b1_c1_bill_component(
    request: BillReplayRequest,
    card: BillRateCard,
) -> BillReplayResult:
    """Replay the B1/C1 demand + active/reactive energy + TCA subtotal.

    Values are from historical meter/bill evidence. The function does not
    authenticate evidence or estimate a candidate bill from a dispatch.
    """
    if request.tariff is not card.tariff:
        raise ValueError("Request tariff and rate-card tariff do not match.")
    if request.billing_period_end_exclusive <= request.billing_period_start:
        raise ValueError("Billing period must be non-empty.")
    if (
        request.billing_period_start < card.effective_from
        or request.billing_period_end_exclusive > card.effective_to_exclusive
    ):
        raise ValueError("Rate card does not cover the full billing period.")
    _require_decimal_nonnegative(request.subscribed_demand_pc_kw, "Pc")
    _require_decimal_nonnegative(request.measured_max_average_pu_kw, "Pu")
    if request.measured_max_average_pu_kw > request.subscribed_demand_pc_kw:
        raise ValueError("Pu exceeds Pc; reconcile the tariff/contract demand update before replay.")

    required = _periods(request.tariff)
    if not request.registers:
        raise ValueError("At least one meter register block is required.")
    for block in request.registers:
        if block.period not in required:
            raise ValueError(f"Register period {block.period} does not belong to {request.tariff}.")
        _require_decimal_nonnegative(block.active_kwh, "active kWh")
        _require_decimal_nonnegative(block.reactive_kvarh, "reactive kvarh")
        if not isinstance(block.tca_mop_per_kwh, Decimal):
            raise TypeError("TCA must be Decimal.")
        if card.active_rate(block.period) + block.tca_mop_per_kwh < ZERO:
            raise ValueError("Active-energy rate plus TCA cannot be negative.")
        if request.tariff is TariffVariant.C1:
            expected_kind = _c1_reactive_kind(block.period)
            if block.reactive_kind is not expected_kind:
                raise ValueError(
                    f"{block.period} requires reactive kind {expected_kind}; "
                    "a missing or mismatched reactive register blocks replay."
                )

    supplied = {block.period for block in request.registers}
    missing = required - supplied
    if missing:
        raise ValueError(f"Missing tariff-period register blocks: {', '.join(sorted(p.value for p in missing))}.")

    billed_pf = request.measured_max_average_pu_kw + card.demand_weight_k * (
        request.subscribed_demand_pc_kw - request.measured_max_average_pu_kw
    )
    demand_charge = billed_pf * card.demand_rate_mop_per_kw

    replay_rows: list[PeriodReplay] = []
    for period in sorted(required, key=lambda item: item.value):
        rows = [block for block in request.registers if block.period is period]
        active_kwh = sum((row.active_kwh for row in rows), ZERO)
        reactive_kvarh = sum((row.reactive_kvarh for row in rows), ZERO)
        tca = sum((row.active_kwh * row.tca_mop_per_kwh for row in rows), ZERO)
        active_charge = active_kwh * card.active_rate(period)
        if request.tariff is TariffVariant.B1 or _c1_reactive_kind(period) is ReactiveKind.INDUCTIVE:
            billable_reactive = max(ZERO, reactive_kvarh - SIXTY_PERCENT * active_kwh)
        else:
            # C1 off-peak capacitive reactive energy is charged in full.
            billable_reactive = reactive_kvarh
        reactive_charge = billable_reactive * card.reactive_rate(period)
        replay_rows.append(
            PeriodReplay(
                period=period,
                active_kwh=active_kwh,
                active_energy_charge_mop=active_charge,
                billable_reactive_kvarh=billable_reactive,
                reactive_energy_charge_mop=reactive_charge,
                tca_charge_mop=tca,
            )
        )

    active_total = sum((row.active_energy_charge_mop for row in replay_rows), ZERO)
    reactive_total = sum((row.reactive_energy_charge_mop for row in replay_rows), ZERO)
    tca_total = sum((row.tca_charge_mop for row in replay_rows), ZERO)
    subtotal = demand_charge + active_total + reactive_total + tca_total
    return BillReplayResult(
        tariff=request.tariff,
        billed_demand_pf_kw=billed_pf,
        demand_charge_mop=demand_charge,
        active_energy_charge_mop=active_total,
        reactive_energy_charge_mop=reactive_total,
        tca_charge_mop=tca_total,
        subtotal_excluding_tax_mop=subtotal,
        period_breakdown=tuple(replay_rows),
    )


def _periods(tariff: TariffVariant) -> set[EnergyPeriod]:
    if tariff is TariffVariant.B1:
        return {EnergyPeriod.B1_BUSY, EnergyPeriod.B1_LOW_LOAD}
    return {
        EnergyPeriod.C1_LOW_SEASON_BUSY,
        EnergyPeriod.C1_LOW_SEASON_LOW_LOAD,
        EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD,
        EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD_PEAK,
        EnergyPeriod.C1_HIGH_SEASON_LOW_LOAD,
    }


def _c1_reactive_kind(period: EnergyPeriod) -> ReactiveKind:
    if period in {
        EnergyPeriod.C1_LOW_SEASON_BUSY,
        EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD,
        EnergyPeriod.C1_HIGH_SEASON_FULL_LOAD_PEAK,
    }:
        return ReactiveKind.INDUCTIVE
    return ReactiveKind.CAPACITIVE


def _validate_rates(
    rates: tuple[PeriodChargeRate, ...],
    required: set[EnergyPeriod],
    label: str,
) -> None:
    periods = [rate.period for rate in rates]
    if len(periods) != len(set(periods)):
        raise ValueError(f"Duplicate {label} tariff-period rate.")
    if set(periods) != required:
        raise ValueError(f"Rate card must define every {label} tariff period exactly once.")
    if any(not isinstance(rate.mop_per_unit, Decimal) or rate.mop_per_unit < ZERO for rate in rates):
        raise ValueError(f"{label.title()} rates must be non-negative Decimal values.")


def _rate_for(rates: tuple[PeriodChargeRate, ...], period: EnergyPeriod) -> Decimal:
    for rate in rates:
        if rate.period is period:
            return rate.mop_per_unit
    raise ValueError(f"No rate configured for period {period}.")


def _require_decimal_nonnegative(value: Decimal, label: str) -> None:
    if not isinstance(value, Decimal) or value < ZERO:
        raise ValueError(f"{label} must be a non-negative Decimal.")
