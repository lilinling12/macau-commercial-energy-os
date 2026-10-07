# G1 CEM Public Tariff Rate Snapshot — 2026-10-04

**Status:** Public-source snapshot for research and design only; not a bill-grade tariff package or legal opinion.  
**Captured:** 2026-10-04. Public CEM pages can change; re-check before each rule-package publication and against the bill period.  
**Scope:** CEM-published A/B/C/D base charges and the separately published quarterly Tariff Clause Adjustment (TCA).

## Finding

CEM presents the published tariff-group rates and quarterly TCA as separate bill components. The currently listed **2026 Q3 TCA is MOP 0.36/kWh, effective 2026-07-22**, for Group A and Groups B/C/D. CEM’s Group A illustrative bill still uses 0.340; that example value is not the current quarterly TCA and must not be copied as a live price.

The snapshot below records public page values. It does not establish the complete legal effective-date chain or customer-specific applicability. Executive Decree 105/2022 is cited by CEM as the source for tariff rates; the official Gazette page should be checked for applicable amendments and the exact billing period.

## Publicly listed base charges

| Group / class | Demand charge | Active energy (MOP/kWh) | Reactive energy (MOP/kvarh) | Publicly described periods |
|---|---:|---|---|---|
| A1 | MOP 8.224 up to 3.4 kVA; MOP 18.796 up to 6.9 kVA; above 6.9 kVA MOP 3.372/kVA | 0.963 | — | A1 published flat energy rate |
| A2 | — | 0.858 | — | Eligibility: subscribed demand ≤6.9 kVA and monthly use ≤120 kWh for each of latest six months |
| A3 | MOP 8.224 up to 3.4 kVA; MOP 18.796 up to 6.9 kVA; above 6.9 kVA MOP 3.372/kVA | 0.884 | — | Social-welfare eligibility applies |
| A4 | — | 0.429 | — | Eligibility restricted to qualifying social-assistance residential customers |
| B1 | 19.797/kW | Full-load 0.874; low-load 0.767 | Full-load 0.348; low-load 0.116 | Full-load 09:00–20:00; low-load 00:00–09:00 and 20:00–24:00 |
| B2/B3 | 21.484/kW | Same listed energy rates, with class-specific loss adjustments | Same listed reactive rates; class-specific treatment applies | B2/B3 transformer/network adjustments apply |
| C1 | 19.797/kW | High season: peak 1.432, full 0.885, low 0.749; low season: peak/full 0.776, low 0.724 (shared C1/C2 schedule) | Peak/full 0.348; low 0.116 (shared C1/C2 schedule) | High season June–September; low season October–May; CEM publishes separate time bands |
| C2 | 21.484/kW | Same published C1/C2 schedule; C2 loss treatment is a separate adjustment | Same published C1/C2 schedule; verify any bill-specific adjustments | MV supply with LV metering; CEM describes 1% transformer-loss adjustments |
| D | 21.980/kW | Busy 0.770; non-busy 0.530 | Busy 0.350; non-busy 0.120 | Busy 08:00–23:00; non-busy 23:00–08:00 |

All amounts are MOP. The official Gazette resolves the merged CEM table: Executive Decree 105/2022 Article 7(3) states that C1 and C2 use the same energy-period schedule and parameter values. C1 demand parameter is MOP 19.797/kW and C2 is MOP 21.484/kW (Article 7(1)–(2)). CEM separately describes C2 loss treatment; preserve that as a class-specific adjustment rather than changing the shared energy-rate table. Customer-specific contract and bill applicability still require confirmation.

## Quarterly TCA snapshot

| CEM quarter | Effective date | Group A (MOP/kWh) | Groups B/C/D (MOP/kWh) |
|---|---|---:|---:|
| 2026 Q3 | 2026-07-22 | 0.36 | 0.36 |
| 2026 Q2 | 2026-04-23 | 0.35 | 0.35 |
| 2026 Q1 | 2026-01-21 | 0.35 | 0.35 |

The public page describes the TCA as a quarterly adjustment reflecting generation-cost fluctuation. It is a separately versioned input, not a permanent base-rate value. Confirm the actual period-effective TCA against the customer's invoice.

## Source hierarchy and design implications

1. Use the applicable Gazette instrument and amendments as legal tariff authority; CEM’s current tariff pages are operational/public explanations and rate listings.
2. Use the CEM TCA history page for its published quarterly amount and effective date; pin a dated capture and verify the customer's actual billing period.
3. Use an issued customer bill/contract and meter evidence to establish customer-specific class, subscribed demand, meter treatment and invoice applicability.
4. Keep base schedule, TCA, class/loss modifiers, tax/installation-use charge, Pu policy, and invoice rounding/carry-forward as separate versioned components.
5. Never construct an “all-in” energy price by adding a stale example TCA to a base rate. Never infer an unresolved monthly installation-use formula or Pu interval from these pages.

## Remaining G1 unknowns

This snapshot does not resolve U-001 (Pu integration interval/register semantics), U-009 (B/C/D monthly installation-use charge formula and basis), U-010 (real Golden Bills), U-011 (invoice arithmetic/carry-forward details), or customer-specific contract applicability. G1 remains OPEN. No bill-grade claim, customer saving claim or Gate closure follows from this public snapshot.

## Sources

- CEM A tariff page: https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-a/
- CEM B tariff page: https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-b/
- CEM C tariff page: https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-c/
- CEM D tariff page: https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-d/
- CEM Tariff Clause Adjustment (TCA) history: https://www.cem-macau.com/zh/customer-service/billing-service/tariff-clause-adjustment/
- Administrative Regulation 25/2022: https://bo.dsaj.gov.mo/bo/i/2022/26/regadm25_cn.asp
- Executive Decree 105/2022 (official Gazette, Article 7(1)–(3), C1/C2 demand and shared seasonal energy parameters): https://bo.dsaj.gov.mo/bo/i/2022/26/despce_cn.asp?printer=1
- Administrative Regulation 25/2022 (official Gazette): https://bo.dsaj.gov.mo/bo/i/2022/26/regadm25_cn.asp?printer=1
