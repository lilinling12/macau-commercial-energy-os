# G1 Evidence Note — CEM Billing Rounding, Demand, Tax and Smart Meter Boundaries

**Evidence checked:** 2026-10-04 (Asia/Shanghai)  
**Status:** Partial public-source evidence. This note does not close G1 or establish bill-grade reconstruction.

## Findings from official public sources

### Invoice amount rounding and odd-amount carry-forward

CEM's “Understand My Bill” page describes for tariff groups A and B/C/D that an odd amount is automatically carried forward to the next bill and the amount payable is rounded down to the nearest ten. The public explanation therefore supports a limited conclusion about the displayed amount due and carry-forward concept across the listed tariff groups.

It does not define the complete accounting algorithm: the exact denomination meant by “ten” in all contexts, the order of tax/charge/credit aggregation and rounding, the ledger representation and direction of carry-forward, treatment of negative adjustments/refunds, or the exact B/C/D component-level calculation. No real commercial bill has been reconciled against meter data. U-011 is therefore **PARTIALLY RESOLVED / GOLDEN-BILL VALIDATION REQUIRED**, not closed.

### Demand (Pu) averaging window

CEM's public B/C/D tariff pages describe Pu as the highest measured demand during the billing period. Administrative Regulation 25/2022 defines the B-group quantity by reference to the maximum periodically measured average active power. The cited public materials do not state the numeric averaging/integration interval. U-001 remains **UNKNOWN / G1 BLOCKER**; do not hard-code a 15-minute interval.

### Government tax

CEM's B/C/D tariff pages identify a monthly government tax but do not publish the general B/C/D formula in the materials reviewed. A formula found in CEM's A-group tariff guide is not evidence of the B/C/D rule and must not be generalized. U-009 remains **UNKNOWN / G1 BLOCKER**.

### Smart meter deployment and data access

CEM reports full smart-meter coverage and describes customer access to daily consumption history in its app. These facts do not establish an external third-party API, high-frequency data interval, export format, retention, or commercial access terms. U-003 remains **UNKNOWN** for third-party high-frequency AMI access. The first pilot must remain viable through authorized local meters/BMS or another documented data path.

## Product and architecture implications

- Keep the CEM commercial tariff calculation explicit and versioned; do not encode an assumed demand interval, B/C/D tax formula, or per-interval rounding rule.
- Separate known invoice-level rounding/carry-forward behavior from unresolved reconstruction details.
- Preserve local meter/BMS as a pilot data path until third-party AMI access is confirmed.
- Do not claim billing accuracy until at least two real Golden Bill cases, matched meter/load-profile evidence, <=0.5% reconstruction error, and zero unexplained balancing adjustment satisfy the G1 criterion.
- These findings do not affect technology selection or approve a product/architecture decision.

## Sources

- CEM — Understand My Bill (Chinese): https://www.cem-macau.com/zh/customer-service/billing-service/understand-my-bill/
- CEM — Understand My Bill (English): https://www.cem-macau.com/en/customer-service/billing-service/understand-my-bill/
- CEM — Tariff Group B: https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-b/
- CEM — Tariff Group C: https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-c/
- CEM — Tariff Group D: https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-d/
- Official Gazette — Administrative Regulation 25/2022: https://bo.io.gov.mo/bo/i/2022/26/regadm25.asp
- CEM — Smart Meters: https://www.cem-macau.com/en/smart-living/smartcity/smartmeters/
- CEM — Smart Energy Management press release (2025-01-16): https://www.cem-macau.com/en/press-release/681/
