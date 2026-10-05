# Source-and-Load Economic Dispatch — Product Design Proposal v0.1

**Date:** 2026-10-04  
**Status:** additive product proposal for owner and domain review; not an approved production requirement, tariff model, algorithm, site capability or control authorization.  
**Scope:** make commercial-site source/load scheduling an explicit first-class Energy OS task while preserving the existing research and safety authority.

## Research source trace

The early G7.1 market/ROI and G7.2 energy-economics packages establish a candidate market framework and high-level dispatch objective, not validated customer ROI, Macau site parameters, or a complete calibrated model. See [G7.1/G7.2 research-to-product trace](G7.1-G7.2-RESEARCH-TO-DISPATCH-PRODUCT-TRACE-v0.1.md) for archive fingerprints, what those packages do and do not establish, and the link to main decisions and the open PR #8 product baseline.

## 1. Why this proposal exists

The current `main` mission and D-001/D-002 define a commercial Energy Orchestrator whose objective is total economic energy cost/value. D-003 prioritizes HVAC/chiller as the first controllable-asset hypothesis; D-004 makes ESS optional and site-economics-dependent; D-005 requires PV treatment to follow verified settlement contracts; D-006 makes Demand Guard a hard veto; D-009 includes the Energy Graph, tariff/contract and meter/settlement twins, HVAC model, SHADOW and M&V; D-013 separates physical from economic topology; D-055 limits initial bill-grade truth; D-056 requires deterministic tariff-aware supervisory logic before MPC; D-060 makes rebound/recovery explicit; D-061 denies MPC a privileged control path; D-077/U-025 prevent assuming cross-site PV settlement rights.

At the initial comparison snapshot for this proposal, PR #8 described data connection, site context, economics, recommendations and replay without a first-class schedule comparison. PR #8 has since been updated on its still-unmerged branch: `PRODUCT-DESIGN.md`, PRD requirement PR-10 and the IA now carry the user's dispatch-first direction and S-10, and the architecture traceability matrix maps that requirement to this PR #10 study and G1–G5 evidence. The logical application/event catalog still contains APP-01…APP-10; APP-11 remains a proposal in this PR's boundary map pending semantic/owner review. Prototype v0.11 remains a distinct synthetic core-flow stimulus; it is not replaced by the six-stage v0.4 dispatch study.

> Given the evidence for this site and planning horizon, compare a feasible baseline and candidate schedule across energy sources and flexible loads, understand its economic basis and constraints, then review it as a non-executable SHADOW recommendation.

This is a proposal to complete that product task. It does not claim that the task, current product scope or visual direction has been approved. The existing source/load and cost workflows remain necessary; the dispatch workspace connects them into an operational decision.

## 2. User and job hypotheses

| User hypothesis | Dispatch job | Validate before pilot commitment |
|---|---|---|
| Energy/facilities manager | Understand which schedule best meets site economics and operating limits; find what evidence is missing | Decision cadence, objectives, escalation and accepted economics |
| Building operator/control-room staff | Review an advisory schedule against comfort, equipment and site constraints; report unsafe or impractical assumptions | Shift workflow, authority, local terminology and preferred review action |
| Finance/asset owner | Inspect tariff/contract inputs and distinguish modeled cost from bill result or realized value | Bill evidence, cost components, approval responsibility and M&V method |
| Energy-service/integration partner | Configure verified meter/asset mappings and explain readiness blockers | Delegation, permission boundaries, connector effort and responsibility |

The D-010 first-site archetype is still a GTM hypothesis. This proposal does not turn a hotel/resort or any specific Macau site into a committed pilot.

## 3. Core end-to-end task flow

1. **Qualify data and settlement evidence.** Select tenant/site and horizon. Inspect source connection, meter/point mapping, units, clock, data quality/freshness, contract/account applicability, tariff version and unresolved G1 items. A physical comparison may remain possible when economics is not; the screen must state which result types are blocked.
2. **Review the site energy model.** Inspect the versioned electrical/physical graph separately from the settlement/economic graph. Trace grid import, site load, PV plant, ESS and load assets to meters and evidence. Missing/ambiguous edges remain explicit.
3. **Inspect forecasts and capability.** Compare measured history and forecasts with issue time, horizon, uncertainty and source. Show only asset flexibility backed by verified points, response limits, schedule, operating authority and constraints. Never infer controllability from a device name.
4. **Build the baseline and candidate schedules.** Use the same horizon, resolution, timezone, evidence snapshot and sign/unit conventions. A schedule is `READY` only for the claims supported by the available model and evidence; otherwise return `PARTIAL`, `BLOCKED` or `INFEASIBLE` with actionable reasons.
5. **Compare physical quantities and economics.** Align grid import, PV use/export/curtailment where evidenced, ESS charge/discharge/SOC, total load, flexible-load movement and binding limits. Keep kW/kWh and physical balance distinct from bill components, demand settlement, contract value and projected cost. A single blended “savings” score is not the default view.
6. **Inspect explanation and evidence.** Selecting an interval/resource exposes source/mapping, rule and contract version, forecast/model version, assumptions, uncertainty, active constraints, excluded terms, feasibility result and why each claim is allowed or withheld.
7. **Review in SHADOW.** User can mark reviewed, request evidence or dismiss with an optional reason. These append review context only; they do not approve, authorize, send or execute a device command.
8. **Monitor and replay later.** Show input/integration health and schedule validity. After separately authorized site activity or approved passive observation, compare actual response and recovery against a customer-approved baseline/M&V method. Keep proposed, approved, authorized, executed, acknowledged, observed and measured-outcome states distinct; MVP does not expose device writing.

## 4. Physical schedule and economic result boundaries

### Physical schedule model

For each site-defined interval and declared topology, a simplified balance is:

`grid import + PV used on site + ESS discharge = site load + ESS charge + export + conversion/loss terms`

The exact equation depends on meter boundary, onsite use, conversion losses and topology. The schedule must not count a PV quantity twice as self-use and export, double-allocate one producer to multiple consumers, or infer a missing branch. Export/curtailment is shown only if the equipment, connection, measurement and operation are evidenced. Energy balance in kW or kWh is a physical statement, not a bill calculation.

### Economic evaluation

A separate settlement/cost evaluator consumes eligible metered quantities, the applicable account/site/meter relationship, effective-dated contract/tariff rules and the approved settlement interval. It returns componentized results and traceable rules or an explicit unavailable state. Do not equate the optimizer's time grid with CEM's unresolved Pu averaging window (U-001). CEM's public Group B page now documents billed demand as 0.2Pc + 0.8Pu, with Pc the subscribed active demand and Pu the highest measured demand in the billing period; this does not establish the account's applicable tariff class or Pu measurement interval. See the 2026-10-05 public-source snapshot in PR #12's G1 readout. Under D-055, initial R0 bill-grade truth remains restricted to verified C1 active-energy TOU plus effective-dated TCA; Pu/demand, tax, PV, ESS and EV settlement stay disabled or scenario-only until their evidence gates permit them.

- Physical PV generation or grid injection does not prove producer payment received by the consuming account.
- Cross-site PV credit, netting, procurement right, saving or allocation requires separate verified legal, CEM, meter, account and contract evidence under D-077/U-025.
- When tariff applicability or component rules are missing, the UI may display a physical or explicitly assumed scenario result, but must withhold bill-grade amounts and label the exact assumptions.
- A modeled baseline delta is not realized savings. Savings/M&V requires an agreed baseline, measurement window, adjustment rules, uncertainty and customer review.

## 5. Resources, objective and constraints

| Resource / rule | Proposed scheduling representation | Evidence gate before it is a site fact |
|---|---|---|
| Grid import | Metered/forecast import series; site/customer import limit and demand guard when verified | Meter-to-account mapping, time quality, capacity/contract evidence, applicable Pu rule |
| On-site PV | Available generation; use, curtailment and export only as distinct flows | Inverter/point mapping, interconnection boundary, meter/account and settlement terms |
| ESS | Charge/discharge power, efficiency, SOC trajectory, usable capacity, reserve/degradation and cycle limits | Registered asset, measured/verified state, manufacturer/site bounds, operating rules and economic treatment |
| HVAC/chiller | Service/comfort-bounded load or allowed setpoint schedule; show rebound/recovery | Mapped points, qualified controllability, equipment constraints, comfort/occupancy/service schedule and live response evidence where the claim requires it |
| EV / hot water / other flexible load | Availability window, energy/service deadline, power bounds and rebound/recovery | Site asset and point evidence, authorized policy, user/service requirement, controllable response and measurement |
| Forecast inputs | Per-resource versioned intervals, issue/valid time, uncertainty and missing horizon | Source/model provenance, freshness and calibrated use scope |
| Objective | Total economic cost/value where eligible; otherwise a clearly named physical or scenario objective with separate terms | Versioned objective and tariff/contract evidence. Never silently replace unknown money with zero. |

Safety, comfort, equipment, contract and Demand Guard conditions are feasibility constraints, not just optimizer penalties. D-006 may veto a candidate. D-056 supports a deterministic tariff-aware supervisor before any MPC promotion; no solver or optimizer is selected by this proposal. Any later optimizer must pass the same policy/safety boundary under D-061. Rebound/recovery is represented over the full relevant horizon under D-060; a peak-hour reduction that shifts load into a later peak is not reported as an unqualified benefit.

## 6. Product areas, workspace structure and states

Proposed core navigation/task areas:

1. Portfolio/site context and evidence readiness
2. Data health and source integrations
3. Site energy model (physical/electrical) and settlement/economic relationships
4. Tariff/contract evidence and separate economics results
5. **Dispatch planning** — baseline/candidate source and load timeline, constraint/readiness panel, evidence explanation and comparison table
6. Recommendations (SHADOW) and append-only review history
7. Outcome monitoring and evidence/replay

### Dispatch workspace states

- **NO SITE / NO ACCESS:** no site details are disclosed beyond authorized scope.
- **DATA INCOMPLETE:** missing/stale/unmapped/invalid inputs named; affected assets and result types explained.
- **MODEL REVIEW REQUIRED:** topology, meter, contract or asset links are ambiguous, expired or conflicting.
- **PHYSICAL SCENARIO ONLY:** a clearly synthetic or project-assumption schedule may be compared; no tariff-grade value is shown.
- **PARTIAL:** only explicitly supported assets/claims are included; omitted resources and claims have reasons.
- **READY FOR SHADOW REVIEW:** inputs, limits, objective and candidate pass defined checks; this still does not authorize field action.
- **INFEASIBLE / BLOCKED:** constraint conflict or missing mandatory evidence prevents candidate result; do not relax or fabricate constraints.
- **EXPIRED / STALE:** data or candidate validity window has elapsed; preserve last-known evidence but require re-evaluation.
- **REVIEWED / NEEDS EVIDENCE / DISMISSED:** append-only user disposition; distinct from execution and outcomes.
- **MEASURED OUTCOME AVAILABLE:** only after agreed post-period measurements and M&V evidence; display alongside prediction with lineage.

The page should keep a clear active-site/time context, a dominant schedule comparison, compact reasoned readiness, visible source labels, direct units and a data-table alternative. Keep physical schedule, settlement result and model assumptions in separately inspectable layers. Do not bury missing evidence in global health badges or decorative KPI cards.

## 7. MVP scope and explicit exclusions

### Proposed MVP scope

- Evidence/readiness model for grid import, site load, HVAC/chiller and other resources only when mapped and verified.
- Same-horizon baseline/candidate scenario comparison with explicit objective, unit/sign convention, intervals, provenance and constraints.
- PV and ESS scenario participation only when their site evidence supports the represented flow/capability; otherwise show blocked/optional state.
- Deterministic bounded assessment through versioned, stack-neutral contracts; recommendation persisted and reviewed as SHADOW.
- Evidence drill-down, reason codes, input/version references and replay status; user feedback append-only.
- Read-only collection and view in the first MVP increment. No equipment write credential, execute endpoint, “apply” affordance or claim of closed-loop operation.

### Excluded until separate evidence and authorization

- Autonomous or remote device control; any implication that this prototype's buttons operate equipment.
- Bill-grade settlement for unresolved rules and claims of guaranteed saving/ROI.
- Cross-building PV netting/credit; unsupported export, curtailment, third-party/rooftop PV rights or source sharing.
- Treating ESS as mandatory/first asset, or HVAC/EV/hot-water flexibility as available without evidence.
- Unvalidated MPC/AI decision automation, user-configurable relaxation of safety/comfort constraints, or optimizer paths that bypass Demand Guard/Safety Kernel.
- Production solver choice, framework choice, API protocol, wire schema, database deployment, event broker or runtime topology; those remain architecture decisions.

## 8. Acceptance criteria for design and MVP slices

Before this design may guide an implementation slice, a representative user with correct site access must be able to:

1. State the site, timezone, planning horizon and schedule resolution; distinguish measured, forecast, estimated, scenario and synthetic values.
2. Explain grid import, PV production/use/export, ESS charge/discharge and site load as separate physical series, and open the table/narrative alternative to the graph.
3. Compare a baseline and candidate on identical intervals, then identify the source of a selected change and the constraints it uses.
4. Identify why missing tariff/contract evidence prevents bill-grade calculation while a limited physical scenario may remain visible.
5. Identify missing mapping, freshness, forecast, PV permission, ESS SOC or HVAC comfort/rebound evidence and explain which claim or resource is blocked.
6. Explain the binding Demand Guard/comfort/service/ESS constraints; an infeasible candidate is surfaced without silent relaxation.
7. Distinguish review from approval, authorization, execution, physical acknowledgement and measured outcome.
8. Use the workflow by keyboard and screen-reader semantics, understand chart states without color alone, and complete the task at agreed desktop and narrow viewports for each validated locale.

An implementation test fixture must include a physically balanced synthetic baseline and candidate, same time basis, a binding constraint, a rebound/recovery period, optional ESS with SOC feasibility, a missing-tariff case that withholds bill claims, an infeasible case, an incomplete/stale-data case, and tenant/site rejection cases. A domain reviewer must approve the fixture arithmetic and signs before using it as algorithm acceptance evidence. Synthetic passing fixtures do not prove Macau tariff correctness, customer flexibility or savings.

## 9. Validation plan and open questions

| Unknown | Evidence needed | Do not infer meanwhile |
|---|---|---|
| First paid-pilot site, buyer and operator roles | WP-4 interviews, site access and real point list, owner-approved recruitment | D-010 does not commit a site or purchaser |
| Meter access cadence, quality and account links | Customer-authorized sample exports/API/interval data and matched bill/account identifiers under G1/G3 | CEM consumer summaries do not establish an external high-frequency API |
| CEM Pu demand window and exact settlement logic | The public Group B formula is 0.2Pc + 0.8Pu, with Pu described as the period's highest measured demand; actual tariff class, customer Pc, meter configuration, Pu measurement window and paired bill remain needed under U-001/G1 | Do not hard-code a 15-minute settlement window or assume the schedule interval is the billing demand interval |
| PV deployment, export, host and consumer rights | Site-specific approval, connection point, producer/consumer accounts and contracts under D-077/U-025 | Grid interconnection or FIT alone does not prove another account's credit |
| Asset controllability and response | Point map, authority, static bounds, commissioned read-only data, later approved response/rebound evidence under G2/G3/G7 | Device presence does not prove available flexible kW/kWh |
| ESS SOC/effectiveness and economics | Verified telemetry, power/energy/efficiency/degradation/reserve evidence and applicable settlement model | Do not assume SOC, round-trip efficiency, warranty cost or bill value |
| Comfortable HVAC flexibility/rebound | Site-approved comfort/service schedule and measured response evidence; G7.2/U-017 | Do not infer that SAT/CHWS perturbations reduce site power |
| Launch locales | Per-role/site WP-4 language preference, terminology review and realistic written artifacts | Official-language status alone does not prove that all three locales are required in each workflow |
| Visual composition and responsive operation | Render and compare schedule-first/evidence-first alternatives; task observation, contrast/keyboard/assistive checks by locale | Existing palette study or awards references do not equal approval or user validation |

## 10. UI/UX study boundary

The local schedule-first prototype is an interaction hypothesis, not a design-system freeze. `ui-ux-pro-max` and the project UI/UX skill are inputs to responsive/accessible structure; Apple HIG, Material guidance and WCAG inform interaction quality; Awwwards/Webby/FWA inform craft and originality only. Do not copy a marketing landing template into an operations console. Compare alternatives on the real schedule/evidence task, not a hero section.

The current study is Traditional-Chinese-only and synthetic. It has no user study, no multi-locale coverage, no measured contrast, no certified assistive-technology review and no pixel-verified 1440/1024/768/375 viewport pass. Text layout, chart labels, direction, date/number/currency localization and small-screen evidence navigation still need rendered review for every selected language.

## 11. Relationship to existing repository requirements

This proposal is additive and should be reconciled, not silently substituted:

| Existing source | Existing scope | Proposed connection |
|---|---|---|
| Main `CURRENT.md`, D-001/002/003/004/005/006/009/013/019/055/056/060/061/077 | Product category/objective, boundaries, R0 economics, supervisor/recovery/safety and PV rights | Provides authority for a source/load scheduling task and its limits |
| PR #8 `PRD-v0.1.md`, PR-01…PR-10 | PR-10 now states the dispatch-first user direction and evidence-bounded source/load schedule comparison on the open PR #8 branch; it remains unmerged and unapproved | This proposal supplies detailed workflow/acceptance hypotheses; owner review and site/user evidence still gate baseline approval |
| PR #8 `USER-FLOWS-AND-IA-v0.1.md`, Flow A–D, S-01…S-10 | Flow B/C/D and S-10 now put dispatch planning in the site workspace on the open PR #8 branch; it remains unmerged/unapproved | This proposal details same-horizon comparison and six-stage workflow; no new control authority |
| PR #8 `MVP-APPLICATION-AND-EVENT-CONTRACT-CATALOG-v0.1.md`, APP-01…APP-10 | Logical operations, no dispatch assessment operation; no wire/runtime decision | Candidate APP-11 dispatch assessment and status/reason vocabulary require contract review under D-065 |
| PR #8 prototype v0.11 | Nine-destination synthetic information-architecture/core-flow study, retained as supporting stimulus | PR #10 v0.4 and directions/v0.1 add separate dispatch-study stimuli; neither replaces v0.11 nor claims user validation |
| G7.9 Step 2 domain/data/contract package | Step 1 and Step 2 complete in that source; Step 3 service boundary and implementation design named next | This product proposal is one input to Step 3, not Gate closure or implementation proof |

## 12. Decision boundary

Continue using source/load economic dispatch as the working product direction because it is directly requested and matches current `main` authority. Before product, visual or technical freeze, the owner still needs to review the lead user/site hypothesis, launch-language scope, result types and M&V rules, UI composition after rendering, contract/API semantics and the unresolved G6.9 production stack. This file itself approves none of them.

**Source references:** GitHub `main` `docs/00-authority/handoff/CURRENT.md` (snapshot 2026-10-03) and `docs/00-authority/decisions/DECISIONS.md` D-001…D-077; PR #8 at head `010643f0611896ec13ef0117c860c77b9f53ab56` (`PRD-v0.1.md`, `PRODUCT-DESIGN.md`, `USER-FLOWS-AND-IA-v0.1.md`, `MVP-APPLICATION-AND-EVENT-CONTRACT-CATALOG-v0.1.md`, prototype v0.11); G7.9 Step 2 source package `macau-commercial-energy-os-g7.9-step2-domain-data-contract-design-v0.1.zip`; local design study `macau-energy-os-dispatch-prototype-v0.3.html` and `DISPATCH-PROTOTYPE-REVIEW-v0.3.md`. G7.9 source package is on D: and has not been committed to GitHub; all prototype/design claims remain synthetic or proposed unless stated otherwise.

## Addendum — Prototype coverage and information-hierarchy study (2026-10-04)

The branch now contains a three-direction layout study at prototype/source-load-dispatch/directions/v0.1/index.html and its review record at prototype/source-load-dispatch/directions/v0.1/REVIEW.md. All directions show the same six synthetic hourly intervals, site assumptions, evidence status and SHADOW-only review affordance:

- **Timeline first** foregrounds whole-horizon grid import, including the later HVAC rebound.
- **Difference first** foregrounds the aligned baseline/candidate interval table.
- **Evidence first** foregrounds readiness and the claims each missing input blocks.

The chart uses step series aligned to interval boundaries, with an 18:00 planning boundary and no implied endpoint measurement. Its coordinates follow the displayed 300–540 kW scale. The correct synthetic example shows 480→430 kW at 15:00–16:00, but the candidate maximum rises from 485 kW to 510 kW at 17:00–18:00. This does not estimate bill cost or savings.

**Coverage against the workflow in §3:** the v0.4 prototype expresses the six-stage path and the new direction study exercises schedule comparison → economics/constraints/evidence → page-only SHADOW review. The synthetic evidence/readiness panels demonstrate how missing inputs withhold claims. Neither artifact implements or validates site ingestion, contract onboarding, a real Energy Graph, forecast production, schedule generation, constraint feasibility, persistence, monitoring or M&V replay. Those are product/architecture requirements, not completed functionality.

**UI/UX method:** UI/UX Pro Max searches were run for a dispatch operations console and for chart/accessibility concerns; project UI/UX guidance was applied. The generic style search returned a real-time operations landing-page pattern and unrelated glass/OLED/academic styling; these were rejected as poor product fit. Chart and UX results support paired direct labels/line styles, a visible table, keyboard focus and scroll handling for wide tables. This does not approve a final palette or claim visual polish, WCAG conformance, Apple/Material compliance, award quality or usability validation.

**Source-level checks recorded:** three direction buttons are present; they preserve one scenario and reorder workspace panels. A source audit found the 860-unit desktop chart would shrink 10px labels to about 4px in a ~341px mobile chart area. The page now switches to a compact 360-unit chart with larger axis labels and direct labels for 430/510 kW; the full six-hour interval values remain in the table. Keyboard focus styles, skip navigation, live announcements, reduced-motion rules and narrow-screen layout rules are present in source. No browser-rendered viewport review, keyboard walkthrough, screen-reader review, contrast measurement, multi-language layout review or operator test has yet been performed.

This addendum refines the existing product proposal only. It does not supersede PR #8's general PRD/IA, approve the dispatch-first product baseline, choose one layout, close a Gate, or approve a production stack.


## Cross-branch product and architecture reconciliation — 2026-10-04

The latest PR #8 head `010643f0611896ec13ef0117c860c77b9f53ab56` now reflects the user's dispatch-first direction in PRODUCT-DESIGN, PRD PR-10, Flow B/C/D and S-10, and PRD-to-architecture traceability. The PR #8 APP catalog remains at APP-01…APP-10. PR #10 head at the time of this review is `e54fc8d2d7910e2776e77dcb24828c0308605b40`; its APP-11 and G7.9 Step 3 mapping remain a separate Draft proposal. Both PRs are open and unmerged.

**Consistent boundary:** PR-10 proposes a dispatch-first product requirement and logical capability; it does not canonically extend the application catalog, approve an API/schema, or close G7.9 Step 3. The six-stage flow and PR #8's supporting economics/replay workflows align at the product level. The implementation contract still needs an explicit review decision on whether APP-11 is a separate catalog operation or a composed workflow over APP-05/06/07/08; this must reconcile D-065, G7.8's contract-authoring record, and `implementation/contracts/README.md` before schema or runtime implementation.

**Current G7.9 Step 3 next action:** resolve the contract-authority/APP-11 ownership question with a reviewed logical ER model and valid/invalid fixtures; then map the accepted contract to implementation modules, authorization, idempotency, durable state transitions, migration/recovery, and acceptance checks. Step 3 remains open; the PR #10 static fixture validator demonstrates internal synthetic consistency only.

### 2026-10-05 — Tariff profile and EV charging settlement boundary

The CEM public-rule comparison in PR #12's G1 readout shows why the economic model must resolve a tariff profile per verified account/meter boundary rather than assume one site-wide formula. Group A's charge structure differs from Groups B/C/D; although B/C/D pages share the 0.2Pc + 0.8Pu demand form, their eligibility, metering/loss adjustments, energy calendars and reactive-energy provisions differ. Group C is seasonal and time-of-use; Group D has its own Pc/Pu update rules and full/low periods. These published descriptions are not customer-specific billing evidence.

An EV charger remains a physical flexible load in the site energy balance. CEM also publishes a transport-charging tariff, with a general/private class for applicable charging facilities outside its public-tariff scope. The product must not presume that every charger inherits the building tariff, nor that a separate EV tariff or savings allocation applies. Bind charger energy to the verified serving meter, account, contract and tariff profile; represent a distinct settlement boundary only when actual evidence supports it. Keep the physical schedule and the bill calculation linked through evidence, not conflated.

This updates the product model and evidence requirements only. Tariff classification, account/bill inputs, applicable EV tariff and multi-building allocation remain site/customer validation items. No public-rate fixture or savings claim is added to synthetic v0.5.


### Macau grid-connected PV evidence — 2026-10-05

Current CEM documentation describes PV interconnection at public LV/MV levels, directly or through distribution systems; a bidirectional meter is installed at the interconnection point; CEM buys PV electricity under a feed-in tariff. Its published process requires installation-site rights, technical design and approval/testing steps, DSSCU acceptance, an application to CEM, a connection-point meter and a signed PV interconnection contract. The government DSPA page describes a 20-year purchase period and the treatment of agreements already signed when the 2018 tariff revision took effect. See [MACAU-PV-GRID-SETTLEMENT-RESEARCH-v0.1](MACAU-PV-GRID-SETTLEMENT-RESEARCH-v0.1.md).

Product semantics: model measured PV generation and grid import/export at each evidenced site/meter boundary. Keep feed-in proceeds as an independent account/agreement settlement component. Grid connection and a published feed-in schedule alone do not establish cross-building bill netting, peer allocation, or a direct physical schedule from one building's PV to another building's load. This preserves D-005 and D-077/U-025; any cross-account treatment requires the applicable signed agreement, accounts, meters and interval rules. Public policy is not a substitute for a site's executed contract or operating authority.


### Site / meter / account boundary model — 2026-10-05

The dispatch workflow now cross-references [SITE-METER-ACCOUNT-SETTLEMENT-MODEL-v0.1](../03-architecture/detailed-design/SITE-METER-ACCOUNT-SETTLEMENT-MODEL-v0.1.md). CEM's bill guide distinguishes contract holder, installation address, contract number, billing period, meter multiplier, subscribed demand and tariff group; Group B/C/D tariff pages define account-class conditions and period-demand charges, while the tariff-clause adjustment changes by effective quarter. Accordingly, calculate each evidenced supply-installation/account at its own bill boundary before any portfolio roll-up. Do not equate a product tenant, site, building, meter, utility account and PV purchase payee. Retain separate gross import/export and component charges; demand peaks are not combined across accounts absent a contract rule. Pu window and settlement interval remain evidence-dependent under G1/U-001. This design does not expand initial R0 bill-grade eligibility beyond D-055.


### Demand-window and billing-period boundary — 2026-10-05

CEM's public tariff summary describes Pu as the highest measured demand in a billing period. Macau Administrative Regulation 25/2022 Article 10 defines Group B Pu as the greatest average active power periodically measured by the meter; Group D has the same highest-average-periodic concept, and Group C refers to the Group B method. The public sources reviewed do not identify this pilot account's meter averaging duration/alignment. The dispatch product must keep schedule timestep, source observation interval, Pu averaging window, tariff time band, billing period and quarterly TCA effective period distinct. A short-horizon peak is not automatically bill-period Pu or a demand saving. See DISPATCH-METERING-AND-SETTLEMENT-TIME-BOUNDARIES-v0.1.md. Demand-charge claims remain blocked under U-001 unless the account/meter window and billing-period context are evidenced.


### 2026-10-05 — Settlement scope, partial coverage and snapshot identity in the operator workflow

The operator must be able to tell which physical boundary a schedule describes and which independently evidenced settlement boundary supports each economic component. A product tenant, site, building, service installation, meter, utility account and payee are distinct identities. Physical aggregation follows verified topology; bill calculation follows each verified supply-installation/account and its applicable contract. A portfolio roll-up is allowed only when its component scope and aggregation rule are explicit.

| Workflow stage | What the operator sees | Missing, conflicting or changed evidence | Required behavior / acceptance |
|---|---|---|---|
| 1. Data and contract qualification | Authorized site and horizon; each settlement scope available to the current role; scope label, serving meter/register, account reference, applicable contract/tariff profile, effective dates, evidence status, freshness and “as of” time | Unmapped meter, conflicting account link, expired mapping, unavailable or unauthorized scope | Do not expose whether an inaccessible account exists. Mark an authorized but unverified scope as unresolved; keep physical readiness separate from economic readiness. |
| 2. Site energy model | Physical nodes and directed import, PV, ESS and load paths; settlement edges in a separate layer, each with its own evidence and effective period | Parent/submeter overlap, duplicate register, topology/account mapping conflict or unknown cross-boundary allocation | Detect and withhold dependent totals instead of double-counting. A conflict in one scope blocks only outputs dependent on that scope; do not infer cross-building sharing or netting. |
| 3. Forecast and schedule comparison | Site boundary, site timezone, horizon, interval convention, baseline/candidate pair, input snapshot reference and forecast/optimizer versions | Evidence changes after snapshot; baseline and candidate use different snapshots, horizons or time grids | Bind both schedules to the same immutable input manifest. A changed input creates a new assessment; never silently replace the basis of an existing result. |
| 4. Economic explanation | Separate component results by settlement scope and time interval; component status; covered/total interval count; rate/evidence reference and withheld reason | Missing, overlapping, unverified or conflicting rate; tariff boundary falls inside an unsplittable interval; account boundary not established | Price only exact eligible intervals. Show PARTIAL with eligible / total and named withheld intervals. Never zero-fill missing prices. Withhold a component total if its declared aggregation rule requires complete coverage. Keep demand/Pu, full bill, export proceeds, savings and cross-account allocation withheld unless their own evidence and calculation rules are satisfied. |
| 5. SHADOW review | Recommendation version, physical boundary, settlement-scope references, snapshot reference, model versions, evidence and claim status; actor identity/authority from trusted server context | Review references stale or superseded recommendation, scope or snapshot | Append review against the immutable recommendation and scope. “Reviewed” is not command authorization or device execution. |
| 6. Monitoring and replay | Original assessment and snapshot references; inputs/rules/model/optimizer versions; review history; later measured outcomes shown separately | Referenced snapshot, rule version or artifact is unavailable; actual operation record absent | Replay the pinned basis or report INCOMPLETE/UNAVAILABLE; never substitute latest data. Distinguish proposal, external operation and measured result. |

**Design acceptance examples for the next contract and service review**

1. Two separately metered, separately contracted accounts at one product site produce independent cost components; no combined demand peak is shown without an evidenced rule.
2. A parent meter and a child meter cannot both be added into a site total unless the topology establishes non-overlapping registers.
3. A meter with unknown or conflicting account mapping can appear as a physical measurement only when its physical mapping is verified; its economic component remains withheld.
4. Site authorization does not grant account-scope authorization. An unauthorized scope is omitted without disclosing its existence.
5. With one missing/unverified rate among six intervals, show partial coverage and the excluded intervals; do not present the missing value as zero.
6. If a tariff boundary falls inside an interval, withhold that interval unless measured quantity can be split under an approved rule.
7. A mapping or tariff revision after assessment creates a new snapshot/revision and does not mutate the prior result.
8. Replay with a missing immutable input artifact is unavailable/incomplete, not a rerun against current inputs.

**Prototype coverage and resulting gap**

v1.1 is a single synthetic physical-site flow. It says account relationship needs verification, economics is blocked, review is page-only and replay is synthetic; it does not present a list of independent settlement scopes, per-scope economic status, partial interval coverage, an input-snapshot identifier/manifest, or replay availability tied to that identifier. v1.2 adds clearly labeled synthetic UI-state examples for scope visibility, partial coverage and unavailable snapshot. These examples describe interface semantics only; they are not connected to the schedule values above, a Macau account, customer tariff or implemented persistence.

**UX acceptance for an operator review**

For any displayed result, an operator must be able to answer: (a) which physical boundary and settlement scope it applies to, (b) which intervals are included, (c) what is withheld and why, and (d) which evidence/version snapshot the result uses. Physical feasibility and economic completeness must have separate status labels. At compact widths the status and scope identity remain visible before explanatory detail. Review controls remain non-executable SHADOW actions. Current prototype localization remains Traditional Chinese only; complete Traditional Chinese, Portuguese and English task coverage, terminology review and locale-specific formats are still open, not implied by this mock.

This addendum applies the project UI/UX skill's explicit-status, provenance, unit, responsive-disclosure and no-unsupported-claim rules alongside the UI/UX Pro Max interaction/accessibility review. It does not claim complete WCAG conformance, representative-operator validation, an approved palette, or an award-level result.


### G7.9 implementation boundary cross-reference — 2026-10-05

The product's one-physical-schedule / multiple-account-result requirement maps to the stack-neutral APP-11 cardinality in [G7.9 Step 3 Dispatch Contract and Implementation Map, multi-scope section](../03-architecture/detailed-design/G7.9-STEP3-DISPATCH-CONTRACT-IMPLEMENTATION-MAP-v0.1.md): one parent assessment and physical schedule, with zero or more independently authorized one-scope economic evaluations. Per-account grants and the role/action matrix remain unresolved under the PR #8 identity design and Owner decision #14. PR #14's implementation remains a single-scope experiment and does not implement this product acceptance. This cross-reference does not approve the API, persistence schema, role grants or deployment boundary.

## G7.3–G7.9 archive and repository trace

The design is a review proposal against a longer research lineage. See [G7.3–G7.9 research and repository status crosswalk](G7.3-G7.9-RESEARCH-AND-REPOSITORY-TRACE-v0.1.md) for each package's stated completion/next step, current main implementation boundary, open PR status and unresolved product/architecture authority conflicts. The crosswalk distinguishes package-complete design from live execution, adoption and site validation.
