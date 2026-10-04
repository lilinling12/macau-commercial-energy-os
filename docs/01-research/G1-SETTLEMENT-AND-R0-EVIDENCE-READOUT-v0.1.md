# G1 Settlement and G7.2 R0 Evidence Readout v0.1

**Checked:** 2026-10-04  
**Status:** Source-based evidence reconciliation; not bill-grade validation, Gate closure, customer validation, or tariff advice.  
**Primary source:** supplied `macau-commercial-energy-os-research-authority-v1.6.2.zip`, snapshot 2026-10-03, especially `handoff/CURRENT.md`, `OPEN-QUESTIONS.md`, `tariff/TARIFF-AUTHORITY.md`, `reference-building/G7.2-R0-HARNESS-PREFLIGHT.md`, `reference-building/G7.3-SITEPOWER-ECONOMIC-REPLAY.md`, and `reference-building/G7.4-TARIFF-AWARE-SUPERVISORY-CONTROLLER.md`.  
**Cross-check:** [`G7.1-7.5-RESEARCH-READOUT-v0.1.md`](G7.1-7.5-RESEARCH-READOUT-v0.1.md), [`G7.6-7.9-DELIVERY-TRACE-v0.1.md`](G7.6-7.9-DELIVERY-TRACE-v0.1.md), and [`RESEARCH-TIMELINE-AND-AUTHORITY-v0.1.md`](RESEARCH-TIMELINE-AND-AUTHORITY-v0.1.md).

## Finding

The tariff and dispatch design has a meaningful, executable specification, but the evidence does **not** establish a production-ready Macau bill engine or a validated Macau building controller. The defensible near-term product is an evidence-labelled source/load assessment and schedule comparison with unresolved settlement components surfaced, followed by SHADOW recommendations. It must not claim bill-grade savings, PV export revenue, ESS grid export, or a physical control capability without site, meter, contract, and operating evidence.

## Gate status versus evidence

| Area | Source says / evidence found | What this permits us to claim |
|---|---|---|
| G1.1 and G1.2 | `handoff/CURRENT.md` lists both sub-gates complete. Earlier authority specifies a tariff rule engine, effective dating, immutable tariff versions, deterministic evaluation and separation of electrical topology from settlement topology. | The tariff domain and implementation architecture have been designed. This does not close G1 or verify bill reconstruction. |
| G1 overall | v1.6.2 `CURRENT.md`: **OPEN**. It names U-001/U-009/U-010/U-011 as blockers. | Macau commercial tariffs cannot be called bill-grade or production verified on this evidence. |
| G7.2 R0 | Static preflight complete; live BOPTEST runs not executed in the stated environment. Two live baselines and one full-trajectory no-op identity run remain required. | Point bindings and no-op semantics have source-fixture support; the controller/economic trajectory has not been run. |
| G7.3 | Design complete and offline reference implemented; live R0 trajectory pending. Initial replay deliberately limits bill-grade scope to C1 active-energy TOU plus effective-dated TCA. | A bounded replay design exists; this is not full bill reconstruction or customer ROI. |
| G7.4 | Controller design complete and offline policy tests pass; live closed-loop execution pending. U-017 response sign, magnitude, comfort impact and rebound remain unknown. | TariffShaper is a falsifiable research controller, not a proven Macau operating policy. |

## Settlement unknowns and product consequences

| ID | Status in v1.6.2 | Required evidence | Product / architecture rule until resolved |
|---|---|---|---|
| U-001: Pu averaging/integration interval | Unknown; G1 blocker | Actual B/C/D load-profile and bill, CEM meter configuration, or authoritative technical documentation | Never assume 15 minutes. Do not compute bill-grade demand charges or present demand savings as settled value. |
| U-002: PV settlement topology | Contract-specific | PV purchase agreement, meter diagram, CEM interconnection/settlement evidence | Keep physical PV generation/self-consumption distinct from invoice credit/export. Do not assume “PV first”, gross FIT, netting, or surplus export. |
| U-003: third-party CEM AMI access | Unknown | CEM technical/commercial confirmation | First pilot must remain viable on customer-authorized local meters/BMS; do not make CEM API access a prerequisite or capability claim. |
| U-004: ESS grid export | Unknown | Project-specific CEM and interconnection approval plus settlement terms | Default `ESS_EXPORT=false`. Model charge/discharge behind the meter only when metering and site evidence support it. |
| U-005: transformer compensation | Partially verified | Real C1/C2/B2/B3 invoices, contract and meter topology | Carry uncertainty at the site/tariff rule level; avoid asserting a generic loss compensation result. |
| U-009: B/C/D government tax formula | Unknown; G1 blocker | Applicable legislation/CEM billing evidence and exceptions | Do not label the total invoice/tax reconstruction complete. Keep unresolved tax outside a “bill-grade total”. |
| U-010: Golden Bills | Not acquired; G1 blocker | At least one real B/C bill paired with interval/load-profile evidence and a second tariff-class case | Required tariff-engine acceptance: reconstruction error ≤0.5%, with zero unexplained balancing adjustment. No source evidence currently demonstrates that acceptance. |
| U-011: rounding / Odd Amount carry-forward | Open; Golden Bill validation required | Real B/C/D bills plus authoritative billing explanation/contract evidence | Rounding must be an explicit settlement policy. Do not round every interval by default or tune a hidden balancing item to force a match. |
| U-017: supervisory response/rebound | Open; live G7.2/G7.4 required | R0-00/R0-01 identity gates followed by R0-02 response sweep, with site-like power and comfort metrics | Do not assume raising SAT/CHWS lowers total power. Treat comfort, capacity, response sign and rebound as measured outcomes, not optimizer priors. |

Other important calibration gaps: U-006 BMS quality, U-007 Macau HVAC flexibility, U-008 comfort/humidity SLA, U-012 Macau reference-building calibration, U-014 lack of zone humidity measurements in R0, U-015 weather validation beyond TMYx, and U-016 real absolute non-HVAC site-load composition. These prevent describing the synthetic office harness as representative Macau hotel evidence.

## What the R0 experiment does and does not prove

The pinned harness is IBPSA BOPTEST v0.9.0 `multizone_office_complex_air`. The preflight cites official API regression fixtures and an official no-op override fixture; it identifies 182 inputs, 204 measurements, 134 forecast points and 15 zone temperatures. It also correctly distinguishes those static fixture checks from live test runs.

R0's initial economic replay intentionally enables only:

```text
C1 active-energy TOU + effective-dated TCA
```

It leaves Pu/demand, Pc state transitions, reactive energy, government tax, PV settlement, ESS settlement/export and EV tariff disabled. The design separates **paired incremental dispatch value** (same exogenous non-HVAC profile) from **absolute synthetic site cost**. The linear cancellation argument applies only to the bounded active-energy/TCA case and only absent import/export regime change; it must not be generalized to demand charges, PV/ESS settlement, nonlinear taxes or differing schedules.

The preflight explicitly records live R0-00 baseline run #1/#2 and R0-01 full-trajectory identity as **not executed**. Offline policy tests do not establish live site power response, comfort impact, tariff correctness, Macau representativeness, savings, or control safety.

## Implications for source/load dispatch MVP

1. Make physical flow and settlement views separate but linked. Show grid import, PV production/use/export, ESS charge/discharge, and flexible load only when the corresponding meter, asset and permission evidence exists. Separately show which of those flows affect the customer's bill and under what versioned contract rule.
2. Give every scenario a settlement coverage label: `verified`, `assumption`, `excluded`, or `unresolved`, with the evidence source and effective period. An unresolved component must lower the confidence and prevent a bill-grade savings claim.
3. Keep deterministic constraint and safety outcomes explicit. Demand Guard may veto independently of the optimizer; comfort, equipment, meter quality, export permission and contract rights are not silently converted into soft economic penalties.
4. Run an advisory/SHADOW schedule review: proposed source/load trajectory, baseline comparison, tariff coverage, constraints, uncertainty, evidence and replay. The interface must not imply device writes are enabled.
5. Permit bounded research calculations such as C1 active-energy/TCA replay only when the scenario clearly states that scope. Never present synthetic non-HVAC composition or office model results as a Macau hotel bill or ROI.

## Verification path and evidence required to advance

| Work item | Gate evidence required | Result unlocked |
|---|---|---|
| G1 closeout | Resolve U-001, U-009, U-010 and U-011 with authoritative source + real Golden Bill fixtures; meet the stated ≤0.5% / zero-unexplained-adjustment criterion across the required cases. | Bill-grade tariff evaluation only for the explicitly covered tariff classes, components and effective periods. |
| G7.2 live R0 | Reproduce pinned harness metadata hashes/counts in the live environment; execute two baselines, full-trajectory no-op identity, persist outputs/hashes and confirm trajectory tolerance. | Reproducible harness evidence for the reference model, not Macau validation. |
| G7.4 R0-02 onward | Execute setpoint response/aggressiveness, guarded, uncertainty and rebound cases; retain power, comfort and trace evidence. | Falsifiable controller behavior for the pinned office model, not an automatic hotel policy. |
| Site pilot readiness | Acquire site-specific bills, meter topology, PV/ESS rights, BMS history/quality, comfort and humidity rules, and measured load/asset capability; agree M&V baseline and responsibilities. | Site-bounded schedule economics and shadow comparison. Field control remains a separate safety/approval gate. |

## Research-source limitations

The original 2026-10-04 readout directly extracted the named files from the supplied v1.6.2 archive and cross-checked the existing G7.1–G7.5 readout; at that time it did not independently re-verify current CEM tariff values, so archived prices were treated as historical snapshots. The 2026-10-05 public-source addendum below now checks selected current CEM pages and official Gazette records. Neither review claims to have read every file in all archives or the full original ChatGPT shared conversation. The exact current branch and PR are verified separately in the current GitHub audit.



## Public CEM tariff and PV source snapshot — 2026-10-05

This update checks public first-party CEM pages and Macao Official Gazette sources. It adds current public context to, but does not resolve, the site- and invoice-specific G1 blockers above. Public tariffs are versioned/effective-dated inputs; the prototype still has no customer account, meter mapping, contract, bill, or settlement result.

### What official public sources establish

| Topic | Public-source observation | Product interpretation and boundary |
|---|---|---|
| Tariff classification | Administrative Regulation 25/2022 defines groups A–D. Group B covers medium/low voltage where subscribed apparent demand is at least 69 kVA and monthly use at least 10,000 kWh; if a customer meets multiple groups, the regulation provides a choice and a 12-month hold after choosing. CEM's Group B page repeats the eligibility and lists B1/B2/B3 metering classes. | Site onboarding must verify the actual tariff group, voltage, metering class, subscribed demand, consumption, contract/account and chosen-group effective period. Do not infer a group's tariff from a building type or the word “commercial”. |
| Group B demand | CEM describes billed demand as (0.2Pc + 0.8Pu), with Pc the subscribed active demand and Pu the highest measured demand in a billing period. CEM also lists active and reactive-energy components, time bands and class-specific loss adjustments. | A schedule's optimizer interval is not automatically the Pu measurement interval. The exact meter/configuration and U-001 averaging/integration details remain unverified; do not derive bill-grade demand cost or savings from the six synthetic hourly intervals. |
| Tariff-clause adjustment | CEM describes TCA as a quarterly adjustment. Its public table shows 2026 Q3 at MOP 0.36/kWh, effective 2026-07-22, for Tariff A and for B/C/D. | This is a dated public parameter snapshot, not the customer's complete bill, contract applicability, subsidy/tax treatment, or a timeless constant. Store source, class, effective-from/to and retrieval time if used in a future calculation. |
| PV grid interconnection | Administrative Regulation 20/2014 establishes safety/installation conditions for PV systems in public or private buildings and connection directly or through the distribution system to the public grid. It requires technical and documentary conditions; grid interconnection is not automatic for an arbitrary installation. | The physical model may represent a site-specific, evidenced PV-to-grid connection after approved topology, equipment, metering and commissioning evidence. A city-level rule does not prove any candidate building's capacity or interconnection state. |
| PV feed-in payment | CEM's PV page states a feed-in-tariff system effective 2018-07-01 and currently displays four installed-capacity tiers: below 10 kW at MOP 3.7/kWh; 10–100 kW at 3.4; over 100–500 kW at 3.0; over 500 kW at 2.8. | This documents a public purchase mechanism and schedule on CEM's page. It does not establish the eligibility, contracted rate, metering, commissioning, export volume or payee/account for a particular installation. It does not create a credit for a different building's account or a cross-site netting right. U-002/U-004/U-025 and site contracts remain necessary. |

### Implications for the dispatch product

1. **Keep the physics and settlement layers separate.** A PV installation may be physically interconnected to the public network under the applicable requirements, and CEM publicly describes feed-in remuneration. Neither fact means a consuming building can claim that generation as its own bill credit. Show site import, PV generation/use/export only where meter topology supports each flow; show the relevant account settlement as a separately evidenced mapping.
2. **Model tariff applicability, not a single Macau tariff constant.** The schedule/economic record will need tariff group/class, voltage/metering class, customer choice where applicable, Pc, bill period, tariff calendar, measured demand evidence, active/reactive quantities, effective-dated TCA and any applicable account/contract terms. These are proposed data requirements, not approved schema names.
3. **Keep unresolved settlement fail-closed.** Public descriptions can guide candidate rules and evidence requests, but U-001 measurement-window details and U-009/U-010/U-011 tax/Golden-Bill/rounding evidence still block a complete bill-grade claim. The existing R0 boundary remains C1 active-energy TOU + effective-dated TCA only, with its stated exclusions; do not generalize the Group B formula or PV feed-in page into a validated optimizer or customer result.
4. **Do not put these public rates into the synthetic v0.5 schedule.** Its no-tariff/no-savings state remains correct. A later public-tariff research fixture must be explicitly labeled as a published-rule calculation, use an effective period and verified class, and remain separate from a customer's actual contract and bill reconstruction.

### Sources checked

- CEM, [Tariff Group B](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-b/) (eligibility, Pc/Pu demand description, energy components and tariff periods; accessed 2026-10-05).
- Macao Official Gazette, [Administrative Regulation 25/2022](https://bo.io.gov.mo/bo/i/2022/26/regadm25.asp) (public electricity tariff system and tariff-group rules).
- CEM, [Tariff Clause Adjustment](https://www.cem-macau.com/pt/customer-service/billing-service/tariff-clause-adjustment/) (quarterly published TCA; 2026 Q3 snapshot).
- Macao Official Gazette, [Administrative Regulation 20/2014, Chinese text](https://bo.dsaj.gov.mo/isapi/go.asp?d=rega-20-2014cn) (PV installation and public-grid interconnection requirements).
- CEM, [PV Feed-in Tariff](https://twww.cem-macau.com/en/go-green/photovoltaic-system-%28pv%29/feed-in-tariff/) (published capacity tiers and rates; page states system effective 2018-07-01).

This source review updates public-rule context only. It does not resolve site-specific tariff classification, actual Pu interval, contract applicability, PV ownership/interconnection, payment assignment, cross-building credit, actual bills or customer economics.


### Public tariff-class and EV-charging boundary — 2026-10-05

A second pass across CEM's official tariff pages shows that a Group B-only representation would be too narrow for a Macau site model. The product/settlement profile must carry the applicable CEM tariff group and class, account/contract and meter boundary, voltage/metering arrangement, billing period and effective-dated rule source. Public pages describe:

| Public tariff scope | Publicly documented shape | Design consequence / limit |
|---|---|---|
| Group A | Low-voltage supply; charges include subscribed demand (kVA), energy (kWh), quarterly TCA and government tax; A1–A4 classes have different applicability/price structures. | Do not apply the Group B/C/D demand formula. Resolve the actual A class and account evidence. |
| Group B | Eligible MV/LV accounts; demand uses 0.2Pc + 0.8Pu, with class-specific transformer/network loss treatment; time-of-use energy and reactive-energy provisions also apply. | Pc, Pu, meter/class, billing period, measured-peak interval and loss treatment need evidence. The published description alone does not reconstruct a bill. |
| Group C | MV with subscribed demand at least 1,000 kVA or 857 kW; demand uses 0.2Pc + 0.8Pu, with C2 transformer-winding loss adjustment; seasonal peak/full/low energy periods and reactive-energy charges apply. | Reuse of the algebraic demand expression does not make the whole tariff interchangeable with B; model class, seasonal calendar, energy periods and reactive components separately. |
| Group D | HV supply; demand uses 0.2Pc + 0.8Pu with D-specific Pc/Pu update rules; full/low energy periods and reactive-energy rules apply. | Preserve D-specific eligibility, Pc/Pu update and reactive rules; do not infer these from B/C. |
| Private EV charging tariff | The CEM transport-charging tariff covers applicable MV/LV electricity used for transport charging; the general/private class applies to charging facilities not covered by the public tariff and has subscribed-demand and time-of-use energy components. | EV charging can be a flexible physical load, but its settlement profile may be a distinct tariff/account boundary. Determine actual supply contract, metering and tariff before assigning the building tariff or savings. The public-charging class has a separate stated scope. |

**Product rule:** represent physical site energy flow and each settlement/account boundary as linked but distinct models. An EV charger remains a physical load in site power balance; its bill/cost belongs to the verified tariff and meter boundary that serves it. Do not assume that an EV submeter creates an independent tariff, or that a separate EV tariff automatically applies, without contract/account evidence.

**Source boundaries:** Group B, C and D public descriptions all expose a 0.2Pc + 0.8Pu form, but use different eligibility, components and operating rules; Group A is structurally different. The 2026 Q3 TCA page currently reports MOP 0.36/kWh effective 2026-07-22 for tariff A, B/C/D and transport charging. Treat it only as effective-dated public data, not as a customer rate until class and period are verified. CEM's bill guide identifies contract number, tariff group, subscribed demand, consumption period, meter multiplier, demand/energy and tax fields as account-level evidence items.

### Sources checked for tariff-class comparison

- CEM, [Tariff Group A](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-a/) (LV scope, subscribed demand, energy, TCA/tax, tariff classes; accessed 2026-10-05).
- CEM, [Tariff Group B](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-b/) (eligibility, demand, energy periods and class adjustments; accessed 2026-10-05).
- CEM, [Tariff Group C](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-c/) (MV threshold, seasonal TOU, demand, reactive energy and C2 adjustment; accessed 2026-10-05).
- CEM, [Tariff Group D](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-d/) (HV scope, demand update rules, TOU and reactive energy; accessed 2026-10-05).
- CEM, [General Charging Tariff (Private Charging)](https://www.cem-macau.com/en/customer-service/billing-service/transportation-charging---general-/) and [Public Charging Tariff](https://www.cem-macau.com/en/customer-service/billing-service/transportation-charging---public/) (transport charging tariff scope; accessed 2026-10-05).
- CEM, [Understand My Bill](https://www.cem-macau.com/en/customer-service/billing-service/understand-my-bill/) (account/bill evidence fields; accessed 2026-10-05).
- CEM, [Tariff Clause Adjustment](https://www.cem-macau.com/en/customer-service/billing-service/tariff-clause-adjustment/) (effective-dated quarterly TCA table; accessed 2026-10-05).

This is a public-rule comparison, not a customer tariff ruling, site classification, bill reconstruction, optimizer calculation or approval of multi-building settlement.


## Demand measurement and time-axis clarification — 2026-10-05

A closer read of Administrative Regulation 25/2022 strengthens the public-rule statement without resolving U-001. Article 10 states that Group B Pu is the greatest value of the periodically measured **average active power** P; Article 24 applies the same highest-average-periodic-measurement concept to Group D, with Group C referring to the relevant Group B provisions. The rule/public summaries reviewed do not specify the candidate customer's averaging duration, subinterval alignment, meter configuration or read-quality/missing-data handling. So “Pu averaging details unknown” is not “the law says only max instantaneous kW”; the legally described quantity is an average over periodic measurements, while the exact meter period remains to be evidenced.

The regulation's Article 3 says energy charges may vary by tariff periods/season and that concrete periods/times are defined by Chief Executive dispatch. Thus dispatch timestep, meter observation interval, Pu averaging window, tariff time band, billing period and TCA effective period are separate temporal axes. The new PR #10 design artifact DISPATCH-METERING-AND-SETTLEMENT-TIME-BOUNDARIES-v0.1.md turns this into product/domain acceptance requirements. It does not change current G1 closure criteria or D-055's initial R0 scope.

Official primary sources: [Regulation 25/2022 Chinese text](https://bo.dsaj.gov.mo/bo/i/2022/26/regadm25_cn.asp), [Regulation 25/2022 Portuguese text](https://bo.io.gov.mo/bo/i/2022/26/regadm25.asp), [CEM Group B](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-b/), [CEM Group D](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-d/), and [CEM tariff-clause adjustments](https://www.cem-macau.com/en/customer-service/billing-service/tariff-clause-adjustment/). Accessed 2026-10-05.
