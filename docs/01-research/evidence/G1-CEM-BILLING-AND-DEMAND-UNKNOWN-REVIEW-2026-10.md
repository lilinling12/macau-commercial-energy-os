# G1 Evidence Note — CEM Billing Rounding, Demand, Tax and Smart Meter Boundaries

**Evidence checked:** 2026-10-04 (Asia/Shanghai)  
**Status:** Partial public-source evidence. This note does not close G1 or establish bill-grade reconstruction.

## Findings from official public sources

### Invoice amount rounding and odd-amount carry-forward

CEM's “Understand My Bill” page describes for tariff groups A and B/C/D that an odd amount is automatically carried forward to the next bill and the amount payable is rounded down to the nearest ten. The public explanation therefore supports a limited conclusion about the displayed amount due and carry-forward concept across the listed tariff groups.

It does not define the complete accounting algorithm: the exact denomination meant by “ten” in all contexts, the order of tax/charge/credit aggregation and rounding, the ledger representation and direction of carry-forward, treatment of negative adjustments/refunds, or the exact B/C/D component-level calculation. No real commercial bill has been reconciled against meter data. U-011 is therefore **PARTIALLY RESOLVED / GOLDEN-BILL VALIDATION REQUIRED**, not closed.

### Demand (Pu) averaging window

CEM's public B/C/D tariff pages describe Pu as the highest measured demand during the billing period. Administrative Regulation 25/2022 defines the B-group quantity by reference to the maximum periodically measured average active power. The cited public materials do not state the numeric averaging/integration interval. U-001 remains **UNKNOWN / G1 BLOCKER**; do not hard-code a 15-minute interval.

CEM's simplified Standard Conditions of Supply separately say that energy-consumption readings are monthly and bills are issued monthly. This describes the customer reading/billing cycle; it does not supply the internal Pu averaging interval. Likewise, CEM's B-tariff full-load/low-load clock bands are energy-price periods, not a stated Pu demand interval. Keep these three concepts separate: monthly read/billing period, tariff energy-price periods, and the meter's periodic average-power measurement interval. The last remains unspecified in the reviewed public sources.

### Government tax / installation-use charge

CEM's Chinese B-group tariff page labels the invoice line “政府稅” and describes it as the tax payable for monthly use of the electrical installation; its Portuguese bill guide and current B/C/D tariff pages call it “Taxa de Exploração” and describe a monthly installation-use charge. These are CEM's billing labels/descriptions, not by themselves proof of the charge's current legal classification. The current CEM B/C/D pages show the line but publish no formula. Administrative Regulation 25/2022 defines the supply-tariff components as power and active/reactive energy (Article 3), and its Group B formula is set out in Article 8; Article 36 repeals Decree-Law 35/86/M. Executive Order 105/2022 defines the tariff periods, subgroups, tariff parameters and specified subsidy measures; its published B/C/D rate tables do not state a separate `Taxa de Exploração` amount or formula. This is a bounded review of these tariff instruments, not proof that no other current legal, concession or contractual basis exists. The later amendments located (66/2024 and 1/2026) amend Article 10 on transport-charging tariffs. A historical CEM Group A leaflet under the former regime said this fee reverted to the SAR Government and that its formula depended on installation type, but that historical statement does not establish the current legal basis or B/C/D treatment after the 2022 reform. Current CEM A-group/EV examples show `0.75 × √subscribed demand`; this is scope-specific and must not be extrapolated to B/C/D. The line's current legal/contractual characterization, authority and exact B/C/D calculation remain unknown. U-009 remains **UNKNOWN / G1 BLOCKER**.

### Smart meter deployment and data access

CEM's January 2025 press release says smart-meter coverage is complete, remote readings and real-time monitoring/data recording are available to CEM, and its app lets customers view daily electricity consumption for the previous 30 days. CEM's Smart Meter page (May 2025) reports more than 280,000 meters and full residential, commercial and industrial coverage; it also says CEM is studying further use of real-time data for service processes. These claims establish utility-side AMI deployment and a customer-facing daily summary, not the customer's raw interval resolution, an external third-party API, export format, retention, or commercial access terms. U-003 remains **UNKNOWN** for third-party high-frequency AMI access. The first pilot must remain viable through authorized local meters/BMS or another documented data path.

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
- CEM — Standard Conditions of Supply (simplified): https://www.cem-macau.com/en/about-cem/power-supply-technical-information/standard-condition-of-supply

- Official Gazette — Administrative Regulation 25/2022 (current tariff system; Articles 3, 8, 36): https://bo.dsaj.gov.mo/bo/i/2022/26/regadm25.asp
- Official Gazette — Executive Order 105/2022 (tariff parameters and annex): https://bo.dsaj.gov.mo/bo/i/2022/26/despce.asp

- CEM — current Tariff Group B (Chinese): https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-b/
- Official Gazette — Executive Order 105/2022 (official Portuguese instrument and annex): https://bo.dsaj.gov.mo/bo/i/2022/26/despce.asp
- Official Gazette — Chief Executive Order 66/2024 (amends Order 105/2022 Article 10, transport-charging tariff): https://bo.dsaj.gov.mo/bo/i/2024/17/despce.asp
- Official Gazette — Chief Executive Order 1/2026 (amends Order 105/2022 Article 10, transport-charging tariff): https://bo.dsaj.gov.mo/bo/i/2026/02/despce.asp
- CEM — historical Group A tariff leaflet (former legal framework; not evidence of current B/C/D rule): https://www.cem-macau.com/uploads/pdf_education_Tariff_A_eng_e2e7123386.pdf
- CEM — Smart-meter coverage and customer daily-use summary (2025-01-16): https://www.cem-macau.com/en/press-release/681/
- CEM — Smart Energy Management press release (2025-01-16): https://www.cem-macau.com/en/press-release/681/
