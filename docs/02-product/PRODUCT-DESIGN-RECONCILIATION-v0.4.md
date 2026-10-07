# Macau Commercial Energy OS — Product Design Reconciliation v0.4

**Status:** Consolidated design proposal for owner/domain review; not an approved PRD, UX, tariff interpretation, optimizer, or control authorization.  
**Date:** 2026-10-07  
**Authority:** Reconciles local `PRODUCT-DESIGN-v0.2.md`, `PRODUCT-SOURCE-DISPATCH-FLOW-v0.1.md`, `SOURCE-AND-LOAD-DISPATCH-DESIGN-v0.1.md`, the full workflow prototype v1.9/review and locale study v0.2, claim-state prototype v2.7/review, and available PR #10 / PR #14 evidence.  
**Repository state:** This version is a review-only addition to PR #10; it is not merged and does not approve or freeze product scope.

## 1. Product definition

Macau Commercial Energy OS is a proposed evidence-led commercial-site decision workspace. Its central job is to help an authorized operator compare **time-aligned energy-source and flexible-load schedules** against a baseline, while seeing the physical constraints, economic evidence, and uncertainty that determine whether a result can be trusted.

The product task is not “view energy KPIs” in isolation. It is:

> For a selected site and planning horizon, determine which combinations of grid import, on-site PV, ESS charge/discharge, and evidenced flexible loads could meet site services while reducing the applicable energy cost/value exposure; explain why a candidate is feasible, blocked, or economically unqualified; review the advisory result in SHADOW; and later compare it with measured outcomes.

Economic comparison is conditional on verified account, meter, contract, tariff, settlement period and calculation rules. Physical energy flow and bill settlement are separate models. A physical export does not establish an export credit; a connected PV system does not establish cross-building sharing; an interval reduction does not establish a lower billing-period demand charge; and a SHADOW review is not a device command.

### Status vocabulary used in this proposal

| Label | Meaning |
|---|---|
| **Observed / measured** | Site-backed reading with point mapping, time, quality and provenance. Not present in the synthetic prototypes. |
| **Forecast** | Model projection with issue/valid time, model version and uncertainty. Not equivalent to a measurement or candidate schedule. |
| **Baseline** | Explicit reference trajectory with its construction method and inputs. |
| **Scenario** | A user or system alternative under declared assumptions; not necessarily optimized or feasible. |
| **Candidate** | A schedule returned by an identified optimizer/runtime and its constraints. The synthetic prototype's “candidate” is only a presentation fixture. |
| **Recommendation** | Advisory, evidence-linked explanation attached to an assessment version. |
| **SHADOW disposition** | Human review state on an immutable advisory result; no execution authority. |
| **Executed / acknowledged / observed response** | Separate future operational states, outside the MVP authorization boundary. |
| **Verified economic outcome** | Result computed from eligible billing evidence and an agreed measurement/settlement method. Not established by a scenario or synthetic data. |

## 2. Users, jobs and context

The first named pilot customer, site archetype and accountable user are still unresolved. These are working personas, not validated roles:

| Candidate role | Core job | Product decision rights to validate |
|---|---|---|
| Site energy/facilities manager | Compare source/load arrangements and understand what evidence or site action is needed | Owns planning horizon, acceptable objective, and schedule review? |
| Building operator | Check operating/service limits and investigate equipment or data issues | Which bounds can the operator attest to? Can they mark a schedule reviewed? |
| Finance / asset owner | Verify account/contract/tariff basis and understand eligible cost exposure | Which bill components, approval thresholds and reporting methods matter? |
| Integration / energy-service partner | Map meters/assets and maintain data/contract evidence | Who is authorized to create/change mappings and effective dates? |

### Primary scenario hypothesis

Begin with one authorized commercial site where the customer can provide a redacted bill/contract, meter mapping, interval telemetry and an operations contact. C-group large commercial/hotel/mall and C1/C2 non-gaming sites appear in historical research as target hypotheses, not a confirmed pilot commitment. HVAC/chiller is the leading flexible-load hypothesis; ESS, PV, EV charging and hot water participate only where that site's topology, equipment and service constraints are evidenced.

## 3. Product principles and boundaries

1. **Make the schedule the main task.** Source/load comparison must occupy the primary work area; generic portfolio KPIs cannot replace it.
2. **Show physical and economic truth separately.** Site graph and interval energy balance do not imply the applicable bill calculation or export settlement.
3. **Gate each claim on its own evidence.** Physical schedule, service/comfort, economics, recommendation review and replay have independent readiness states. A single green badge must not imply all are ready.
4. **Keep comparisons aligned.** Baseline and candidate share site, horizon, time zone, interval grid and pinned input snapshots. The utility billing-demand window is not inferred from the scheduler interval.
5. **Treat unknown constraints as unknown.** Do not substitute zero, unlimited capacity, assumed export rights, absent rebound, or comfortable operation.
6. **Make missing evidence actionable.** Identify the affected asset/claim/interval, missing source and next verification task.
7. **Keep MVP advisory.** Do not provide or imply a control command, closed loop or autonomous dispatch. Reviewing an item does not authorize a physical action.
8. **Keep data classes legible.** Measured, forecast, baseline, scenario and synthetic fixture values use labels, shapes/line styles and accessible descriptions, not color alone.
9. **Design for repeated analytical work.** Dense information should remain readable; motion is subtle and purposeful. Marketing-site visuals are a separate design problem.
10. **Localize the entire task, if approved.** Locale selection must not alter site, schedule, review state or calculation inputs. A few translated labels do not qualify as multilingual support.

## 4. Proposed MVP scope

### Include, subject to owner and domain review

- Authorized tenant/site context and role-aware access.
- Evidence inventory and mapping for site boundary, meters, PV, ESS, HVAC/chiller, and any enabled EV/hot-water loads.
- Data quality/freshness/completeness and effective-dated mapping status.
- Site physical model and an inspectable interval energy balance.
- Forecast/baseline distinction and a common-horizon source/load scenario comparison.
- Only evidence-backed equipment and service constraints; unknown capabilities block or exclude the affected resource explicitly.
- Separate economic readiness. Compute bill-grade costs only where the account, meter, contract, tariff and interval rules are verified; otherwise withhold amount/ranking/savings and retain only permitted physical/scenario views.
- Evidence-linked SHADOW recommendations and append-only human dispositions, after identity, authorization and durable persistence are designed.
- Version-pinned inputs, rules/models/build metadata and replay status sufficient to explain or reproduce a bounded assessment.
- Post-period monitoring only with measured data and a pre-agreed baseline/M&V method.

### Exclude

- Device-write credentials, command endpoints, automatic control, safety-critical operation or BMS replacement.
- LLM as tariff authority, optimizer, safety kernel or command path.
- Unsupported CEM tariff/Pu assumptions, export compensation, netting, cross-site allocation, savings/ROI or bill reduction claims.
- Treating PV exports as income or another building's supply absent contract, topology, metering and rule evidence.
- Declaring HVAC comfort, EV readiness, hot-water service or ESS feasibility without site-specific constraints and capability evidence.
- Portfolio causal savings claims without a defined baseline, adjustment method, measurement window and customer approval.

## 5. Core workflow and module map

The six-stage workflow is the product's main task spine. The full workflow study v1.1 represents all six stages; the v2.7 claim-state study examines a narrower slice of result disclosure. They are complementary studies, not one integrated implementation.

| Stage / area | Operator task | Required product behavior and output |
|---|---|---|
| **1. Data & contract evidence** | Select site and horizon; check source records and data readiness | Identify meter/account/site association, contract/effective dates, tariff source and billing intervals, telemetry freshness/quality, missing inputs and permissions. Separate physical readiness from economic readiness. |
| **2. Physical site model** | Verify the energy topology and participating assets | Show grid boundary, meters, PV, ESS, loads, point mappings and evidence. Unknown or ambiguous links remain visible and affect only dependent claims. Keep economic account links separate from physical edges. |
| **3. Schedule comparison** | Compare baseline and source/load arrangements | Align interval chart and accessible table for grid import, total load, PV, ESS power/SOC and participating flexible loads; show forecast/scenario/synthetic provenance. Explain shift/rebound across the full horizon. |
| **4. Cost, constraints & evidence** | Understand why a candidate is eligible, blocked or changed | Show constraint ownership, value/effective period, binding intervals, missing evidence and economic components independently. No money, savings, export credit or demand-fee change when evidence is incomplete. |
| **5. SHADOW review** | Review, request evidence, or dismiss an advisory proposal | Record actor/time/result version and disposition in a future persistent API. Prototype page-only clicks must be clearly described as non-persistent. No execute action. |
| **6. Monitoring & replay** | Compare actual measured response with the reviewed reference | Distinguish predicted schedule, any separately authorized action, observed meter response, bill settlement and M&V. Replay an immutable input/rule/model/build manifest; surface missing or divergent evidence. |

### Proposed information architecture

- **Portfolio and site selection:** authorized site scope and open readiness work; no unsupported savings leaderboard.
- **Dispatch workspace:** selected site/horizon, physical/economic readiness, baseline/candidate canvas, scenario controls, constraints, claim states, review and next action.
- **Site model:** physical topology, meter and point mappings, asset capabilities, evidence and effective dates.
- **Data and integrations:** connector freshness, data quality, unmapped points, processing status and repair workflow.
- **Contract and economics:** account applicability, tariff source/version, billing interval, settlement rules and explainable component results.
- **Evidence and replay:** source snapshots, transformations, model/rule/optimizer/build versions, review history and replay differences.
- **Monitoring:** measured period outcomes and M&V protocol; unavailable until eligible measurements exist.

Do not split the core decision across unrelated menu destinations. Site, horizon, comparison and snapshot context must persist when navigating to supporting evidence.

## 6. Result state model and disclosure rules

The UI should model at least five independent dimensions:

1. **Input/request lifecycle:** not submitted, rejected, pending, running, complete, failed, expired.
2. **Physical readiness/result:** not assessed, blocked, partial, balanced-within-model, infeasible. “Balanced” means only the declared inputs balance; it does not prove service or field feasibility.
3. **Service/constraint result:** not assessed, partial, feasible within evidenced limits, violated, unknown. Keep comfort, safety, demand guard, ESS limits and service obligations visible.
4. **Economic eligibility/result:** not calculated, blocked, partial, eligible. Each bill component includes applicable account/meter, rule version, evidence and withheld reason.
5. **Recommendation/review/replay:** advisory status; append-only disposition; replay reproducible/divergent/incomplete/unavailable.

### Disclosure matrix exercised in v2.7 (synthetic UI evidence)

| Case | Physical projection | Candidate/economic display | Required copy/boundary |
|---|---|---|---|
| Partial tariff/rate coverage | Fixed synthetic schedule may be shown with partial coverage | No monetary amount or savings; disclose covered interval count | Schedule is supplied synthetic input, not a tariff-qualified optimization result. |
| No applicable tariff/contract | Physical evidence may be separately shown if mapping allows | Do not generate/show optimized candidate or candidate cost ranking under the studied policy | Explain missing applicability and next evidence needed. |
| Core meter mapping missing | Hide affected schedule curve, numeric KPIs and interval table | Block impacted physical and economic claims | Name the missing mapping; do not leave plausible-looking stale numbers. |
| HVAC service-limit violation | Electrical example may remain as an explanatory scenario | No overall-feasibility, comfort or execution claim | Keep the service warning prominent and linked to its bound. |

The v2.7 reviewer reports these four cases across five widths with no document overflow and selected interactions. It is a static synthetic fixture whose selected case gates presentation; it does not call a service, generate a schedule or prove that product APIs enforce the same rules. The policy distinction between “physical-only scenario allowed without tariff” and “no candidate generated” needs product/domain approval and must match the actual objective and site permission model.

## 7. Key interface requirements

- Persistent selected-site, local-time horizon, interval grid, source snapshot and synthetic/site-backed indicator.
- A dominant aligned time canvas with direct labels, uncertainty/provenance, and table/text alternative.
- Separate counters/statuses for physical, service and economic readiness; no blended “optimization ready” indicator.
- Scenario comparison on the same inputs and version, with changes by source, ESS SOC trajectory, flexible load shift/rebound, and full-horizon peak.
- Constraint inspector that shows owner, measured/configured source, value/range, effective interval, confidence, binding impact and proof needed.
- Claim ledger for what may be displayed, withheld and why (physical, cost, savings, export, service feasibility, control).
- An evidence panel that can be opened from every material value and return to the same interval/scenario.
- SHADOW review controls with explicit non-persistence boundary in prototype; production workflow requires identity, authorization, immutable result reference and audit evidence.
- Empty, loading, stale, partial, blocked, infeasible, error and replay-unavailable states, each with an actionable explanation.
- Responsive behavior that preserves core comparison and claim status; wide tables/charts may scroll only inside named, keyboard-accessible regions with clear instructions.

## 8. Product acceptance criteria (proposal)

Before product design approval, representative users should demonstrate that they can:

1. Identify site, horizon, interval length, snapshot time and whether data are measured, modeled or synthetic.
2. Explain the distinction among grid import, total load, PV generation/use, ESS charge/discharge/SOC and flexible-load demand.
3. Compare the same baseline/candidate intervals and locate the interval where an HVAC shift or rebound changes the schedule.
4. Find source evidence for one meter mapping, one asset limit and one tariff rule—or correctly identify it as unknown/blocked.
5. Tell physical schedule readiness apart from service/comfort feasibility and bill-grade economic eligibility.
6. Explain why an unknown tariff, account, Pu window or export clause withholds a corresponding economic claim.
7. Explain that a scenario/recommendation/SHADOW review does not issue or authorize a device command.
8. Find input/model/rule versions and determine whether a prior result can be replayed.
9. Complete core compare/inspect/review tasks by keyboard and at agreed widths/languages without relying only on color.

These are proposed validation tasks, not user-tested results. A protocol still needs a participant profile, target task set, error/comprehension thresholds, language and environment.

## 9. Unknowns and validation plan

| Unknown | Impact | Evidence required / next action |
|---|---|---|
| First paying customer/site and accountable operator | Defines onboarding, cadence, roles and first release | Interview target-site energy/facilities, operations and finance roles; name one pilot decision owner. |
| Initial site archetype/assets | Determines topology, load model and integration priority | With consent, inventory meters, BMS points, PV interconnection, ESS, HVAC/chiller, EV/hot-water and available history. |
| Operational horizon and schedule granularity | Drives UX and optimizer interface | Observe day-ahead/intraday decisions; record source latency and utility billing intervals separately. |
| Whether tariff evidence is adequate | Determines whether product can compare economics | Obtain redacted bill, contract, effective dates, account/meter mapping and official/contract tariff rule; independently reconcile Golden Bill cases. |
| Export and cross-building treatment | Could reverse source allocation economics | Verify site interconnection, meter boundaries, CEM/contract terms and authorized settlement rule per customer/site. |
| Asset controllability, response and comfort/service envelope | Determines whether assets may participate in candidate schedules | Approved point list and equipment specs, operator sign-off, read-only observation and controlled response/rebound validation under separate safety gate. |
| Which locale set is required | Changes product copy, terminology and legal/help content | Ask actual operators/finance/owners; decide Traditional Chinese/Portuguese/English; confirm regional number/time/currency and Macau terminology review. |
| Preferred schedule/evidence layout and visual direction | Affects sustained-use speed and comprehension | Compare meaningfully different layouts using the same dispatch task and synthetic evidence state; run observed operator sessions. |
| M&V method and savings definition | Determines outcome reporting and commercial claim limits | Agree baseline, adjustments, measurement periods, uncertainty, tariff settlement mapping and reviewer with pilot owner. |

## 10. Prototype and repository reconciliation

| Artifact | What it currently demonstrates | Not demonstrated |
|---|---|---|
| Repository/PR #8 v0.10/v0.11 product workspace (per local trace) | Broad site, data, model, economics, recommendation and evidence destinations; synthetic/advisory limits | Source/load dispatch is not the dominant complete task in the inspected view. |
| PR #10 full workflow v1.1 local copy and review | Six-stage task spine, synthetic interval schedule, HVAC shift/rebound, ESS example, responsive stage disclosure and page-local SHADOW review | Portuguese/English, real data, actual optimizer output, backend persistence, complete accessibility or operator research. |
| PR #10 claim-state v2.7 local review copy | Claim/evidence-state disclosure rules under four cases and five viewport widths; selected keyboard/contrast checks | Complete six-stage workflow, API-enforced policy, real model/contract/site evidence or locale switch. |
| Locale inventories v1.8/v1.9 | Translation surface has hundreds of workflow strings and accessible/dynamic copy | Keyed production catalog, approved language set, human-reviewed translations and rendered end-to-end locales. |
| PR #14 bounded optimizer experiment (per local G7.9 review) | Small finite-horizon synthetic SHADOW search and repeatability within tested action space | Production solver, authenticated evidence, full service/tariff semantics, persistence/replay or site validity. |

The local workspace contains v2.7 review evidence and v1.1 workflow review, but no proof in this document that these exact files are merged to `main`. Verify current PR #10 head, file paths, review status and CI before claiming repository implementation. Product design is therefore **research-derived and partially prototyped; not owner-approved or implemented as one end-to-end product**.

## 11. Decisions to request after dependent work is complete

The following choices need a consolidated owner review; no answer is inferred here:

1. **Initial release locale set:** Traditional Chinese only for first pilot, or Traditional Chinese + Portuguese + English at launch. Evidence/impact: language needs change translation and usability workload; legal/commercial requirement is not established by the existing inventory.
2. **MVP economics boundary:** physical/scenario comparison when economics are incomplete versus no candidate generation when no applicable contract/tariff exists. Evidence/impact: v2.7 implements a conservative no-candidate case; source research centers economic dispatch, so the rule must not accidentally convert the MVP into a generic physical simulator.
3. **Initial site/assets:** one named customer archetype and supported assets after discovery; current hotel/C1/C2 and HVAC-leading language remains a hypothesis.
4. **Visual direction:** approve only after same-task visual comparison, full locale layouts, accessibility review and operator task observation.

These decisions can be prepared in one packet after repository/current-head verification and full product/architecture trace; they are not a reason to pause evidence work now.

## 12. Evidence limits

- The original shared ChatGPT page has been only partially readable in prior review; do not describe this product definition as a complete transcript reconstruction.
- Deep Research reports, source archives, GitHub `main` and PRs were reviewed in separate local audit records. This reconciliation does not claim a fresh complete GitHub diff review.
- The two prototypes are synthetic and separately scoped; browser measurements establish only the recorded DOM/layout interactions at the tested state/viewport set.
- No operator or customer interview, Macau site data, valid bill reconstruction, production accessibility review, owner decision or field trial is evidenced here.

## Current repository and product-design reconciliation — 2026-10-07

This section supersedes earlier “local-only” and prototype-current statements in the 2026-10-06 snapshot above. The earlier sections are retained as a dated design record.

### Exact source snapshot checked

- `main` tree: `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`.
- PR #8 branch `docs/product-architecture-roadmap`: head `9e3dec0bccf5acb5122f94c688814e7f4e026a1b`; open, non-draft, unmerged.
- PR #10 branch `product/source-load-economic-dispatch`: head `dd6bdfa92af4a501c57eebd17da77b3d03c24f78`; open, Draft, unmerged.
- Current `main` product directory contains only its high-level README and brief README files for commercial model, customer segments, MVP, pilot design and product thesis. The substantive product designs and prototypes listed below are in PR branches, not in `main`.
- PR #8 carries `PRODUCT-DESIGN.md`, `PRD-v0.1.md`, `USER-FLOWS-AND-IA-v0.1.md`, `VISUAL-DESIGN-PRINCIPLES-v0.1.md`, discovery/usability protocol, Owner decision summary and review brief, prototype v0.1–v0.11, visual-direction studies, detailed designs, and the Macau Energy OS UI/UX skill draft. These are research-derived proposals, not approved baselines.
- PR #10 carries the focused source/load dispatch design, product/research traces, G7.9 crosswalks, the six-stage full-workflow prototype family through v1.9, locale study v0.2, mixed claim-state studies through v2.7, and responsive layout-direction experiments. These supplement PR #8; they do not replace its PRD and IA.

### Current product interpretation

The primary product task remains dispatch-first: compare a same-site, same-horizon baseline and candidate arrangement for grid import, evidenced on-site PV, ESS charging/discharging and only site-qualified flexible loads such as HVAC/chillers, EV charging or hot water. The product must keep physical energy balance separate from account/contract/tariff settlement and expose independent physical, service/comfort, economic, recommendation and replay states.

The six-stage task spine is represented in PR #10's v1.9 source: evidence qualification → physical site model → schedule comparison → costs/constraints/evidence → SHADOW review → monitoring/replay. PR #8's v0.11 remains a broader supporting product-workspace study and is explicitly not the dispatch-first workflow. The separate claim-state v2.7 study covers only mixed readiness/result disclosure; it is not the six-stage application.

### Exact prototype evidence boundary

- v1.9 records an original Traditional-Chinese prototype check across six stages and four viewports (320, 375, 768 and 1440 CSS px), 24 combinations. That review reports no page-level overflow and limited page-only interactions; it is not operator research, complete accessibility testing or site validation.
- The v1.9 localization-study v0.2 uses a 337-unit contextual translation draft. Browser accessibility-tree text was reviewed for all six stages in English and Portuguese and stage 3 in Traditional Chinese. Its own review explicitly records that CSS viewport screenshots, selector-driven locale switching, localized formatting, translation quality review, and locale approval were not established.
- v2.7 is a separate synthetic claim-state prototype. Its review reports four synthetic evidence cases at 1440, 1024, 768, 375 and 320 CSS px (20 case/viewport combinations), selected state-button/table/local-only review interactions, no page errors, and measurements for selected foreground/background token pairs. It does not implement or call an optimizer, API, persistence, site data, or equipment controls. The fixed schedule is presentation data; the selected state only gates what the page shows.
- Directions v0.2.3 compares two schedule layouts under a matched palette across nine widths. This is a bounded information-hierarchy experiment; neither direction nor palette has been selected.
- Project and Pro Max guidance, Apple HIG, Material 3, WCAG 2.2, Awwwards, Webby and FWA are used as review references. Award criteria are self-review lenses; no winning-site transfer study, award assessment, user validation or WCAG conformance is claimed.

### Decisions still open

1. **First supported product outcome:** choose between physical/scenario comparison with economics withheld when incomplete; economic comparison only for evidence-qualified sites; or two explicitly gated modes. No-tariff behavior in v2.7 currently withholds the optimized candidate. This is a prototype policy, not a confirmed product rule.
2. **First pilot user/site and resource scope:** roles and site archetypes are hypotheses. HVAC/chiller is a research priority hypothesis, not verified controllable capacity. PV/ESS/EV/hot-water participation and cross-site settlement require site-specific rights, meter, contract, capability and operational evidence.
3. **Information architecture and visual system:** dispatch-first hierarchy is the current proposal; evidence-first vs interval/timeline-first layout and palette remain unselected. A portfolio palette study does not decide the dispatch workspace visual system.
4. **Locale policy:** Traditional Chinese, Portuguese and English remain candidate locales. Draft strings and accessibility-tree checks are not complete human-reviewed localization or a launch decision.
5. **Acceptance thresholds:** proposed user tasks need a participant profile, observed success/error/comprehension criteria, domain reviewers and field evidence before the workflow is validated.

### Next design work that does not require freezing production architecture

- Keep PRD and IA as drafts; reconcile the dispatch workspace as the primary task while retaining site readiness, evidence, tariff, recommendation and replay as supporting areas.
- Compare the alternative schedule/evidence layouts on identical dispatch tasks and readiness cases; carry only evidence-supported concepts into the full six-stage flow.
- Finish rendered locale/state/viewport checks with reviewable captures and human terminology review; clearly label any machine-assisted translation.
- Prepare moderated discovery/usability tasks using real, authorized, redacted artifacts when available; until then keep all values synthetic.
- Map each user-visible status/claim to its supporting product rule and domain contract. Do not implement a disagreement between UI, optimizer and evidence policy as if it were settled.

This reconciliation records the available design evidence and proposals. It does not resolve the open Owner decisions, approve the pilot, select a visual system or production stack, close G7.9, or authorize device control.


## v3.3 fixture-backed dispatch prototype review — 2026-10-07

### Exact source snapshot and proposal state

The design review was refreshed against main tree a897bf0b1e7e6ceea3862d7d87fa288ecca08203, PR #8 head 1dbcad2dd31d6e5aa749851bff0fcb297f8d7425 (open, unmerged), PR #10 head a7bef59f2cdb2466dd08397dd6ffe880ec66f07d (open, draft, unmerged), and PR #14 head deed7683a8b0ce3a811966ab8fc3b030695debad (open, draft, unmerged). These are proposal/research branches; no owner approval is inferred.

### What v3.3 demonstrates and does not demonstrate

The v3.3 six-stage study now reads the exact PR #10 v2.9 fixture blob 0e746cbe54532e58221529f38c7a2583d1787c4b. The fixture pins optimizer commit 9b80adca9243a0ae9a7bd666f0efee1acfc6309a, optimizer blob 2d3256801f0ddce6b849c648c160f5a32fd90a27 and assessment blob 534ae269a7949601bd4504271e0076369807a68f.

| Stage | Current prototype evidence | Product/implementation boundary |
|---|---|---|
| Data and contract qualification | Shows required site, meter, contract, asset, measurement and forecast evidence as unverified. | No authenticated intake, evidence repair, contract resolution or site data. |
| Physical energy model | Shows a conceptual source/load topology and a separate settlement mapping. | No verified site topology, meter overlap, interconnection or account applicability. |
| Schedule comparison | Displays six baseline/candidate intervals from the synthetic optimizer fixture. Both total 44 kWh; the horizon peak is 10 kW baseline and 11 kW candidate. | Every input is a project assumption. Flexible-load service, comfort, EV departure, hot-water delivery and real ESS efficiency/state evidence are not established. |
| Costs, constraints and evidence | Shows fixture-scoped claims and economic assessment BLOCKED. A distinct interface-only partial-rate view represents 4/6 covered intervals without an amount and keeps uncovered intervals, whole-window bill, demand charge and savings withheld. | Partial coverage is not optimizer output. No Macau tariff, bill, savings, export remuneration or cross-account credit is established. |
| SHADOW review | Page-local choice can be selected. | Not durable, authenticated, submitted or authorizing; no equipment command path. |
| Monitoring and replay | Describes the future evidence and version inputs. | No measured outcome ingestion, immutable assessment history, replay runtime or M&V. |

The optimizer fixture uses assumed sample import rates in its objective. This is an important distinction: the physical schedule output is bounded to that synthetic fixture, while the economic assessment is BLOCKED because tariff/account applicability is not evidenced. The fixture does not establish that a real site's candidate is economically optimal.

### Product decision consistency

The existing G7.9 owner decision packet's Decision D recommends D1 for the interim SHADOW MVP: assess explicitly supplied schedules, do not generate an optimized candidate without an approved objective/economic context, and keep economics BLOCKED/NOT_CALCULATED when ineligible. D2 (separately approved physical-only objective) and D3 (assumed-tariff research mode) remain choices, not adopted product behavior. v3.3 shows a D3-like research fixture output for source fidelity; it must not be read as resolving or implementing the MVP policy. This discrepancy is now surfaced in the UI and remains an owner decision.

### UI/UX evidence and status

The prototype was reviewed with the UI/UX Pro Max skill's targeted searches for visible labels, evidence/status messaging and mobile table overflow. Rendered checks covered 320×900, 375×900, 768×900, 1024×900 and 1440×900 CSS pixels; the page/body had no horizontal overflow, while the workflow rail and wide table use contained horizontal scrolling at narrow widths. The fixture output, UI-only partial view, schedule values, page-local review, and Traditional Chinese, English and Portuguese draft copy were exercised. The Portuguese copy remains explicitly draft. See docs/02-product/prototype/source-load-dispatch/v3.3/REVIEW.md for exact limits and fingerprints.

This is not a complete human localization review, screen-reader audit, measured all-state contrast audit, WCAG conformance result, operator usability study, or product visual-system decision. UI/UX Pro Max suggestions and Apple/Material/WCAG/award references remain evaluation inputs; no award-level or user-validated claim is made.

### Current conclusion and next work

The dispatch-first task is materially represented in a review prototype, but product design remains an unapproved proposal and is not an integrated operator application. The broad v0.10 workspace still contributes readiness/evidence/tariff concepts; it does not replace the dispatch-first primary task. The palette study remains exploratory and does not select the dispatch console palette.

Before the first product behavior is frozen, the owner review should decide: (1) D1/D2/D3 behavior when no eligible tariff context exists; (2) first pilot user/site and resource scope; (3) what physical/service/economic claim each evidence type supports; (4) complete Traditional Chinese/Portuguese/English launch scope and Portuguese locale; and (5) observed user acceptance thresholds. Until then, keep v3.3 as a synthetic study, preserve SHADOW-only review, and defer production UI/API/persistence integration.
