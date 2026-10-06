# APP-11 result projection review — PR #14 generated candidate v2.8

**Review date:** 2026-10-07  
**Status:** Source-grounded UI/result cross-check on PR #10; review proposal only. No canonical contract, architecture or G7.9 approval is implied.  
**PR #10 baseline before this review:** `85e32d781acc91a7b6f30b30fd35063123eaba2e`  
**PR #14 source:** `d5180703df3730779f1f180a89d07c620e7e349d`  
**v2.8 fixture source blobs:** optimizer `2d3256801f0ddce6b849c648c160f5a32fd90a27`; assessor `4986bb546d675c469646881ab151dfd847725790`.

## Source facts

The pinned optimizer's `generate_candidate()` requires an `EconomicContext` and one aligned import rate per interval (source lines 83–109). Its objective is the sum of grid-import kWh multiplied by supplied interval rates (lines 253–259); the module docstring describes it as minimizing short-horizon grid-import energy charges. `_usable_evidence()` rejects UNKNOWN and STALE but accepts PROJECT_ASSUMPTION, and `scenario_only` is derived when any search input is a project assumption (lines 301–304, 425–426).

The pinned assessor separately blocks monetary output unless account/meter mapping, contract and tariff applicability are VERIFIED (assessor lines 766–774). It also withholds each interval whose import-rate evidence is not VERIFIED (lines 793–831). This explains how the optimizer can generate a scenario candidate using assumed prices while its economic assessment correctly returns BLOCKED with no charge or delta.

The v2.8 fixture has six assumed rates, marks its inputs `PROJECT_ASSUMPTION`, records physical status `SCENARIO_ONLY`, economic status `BLOCKED`, and leaves all monetary fields null. It reports 44 kWh for both schedules and a 10→11 kW horizon peak. The candidate is therefore an illustration of the search under that synthetic price shape, not evidence of an economically optimal Macau schedule.

## Result-to-presentation mapping

| Pinned result field / claim | v2.8 presentation | Semantic boundary |
|---|---|---|
| Search objective and assumed interval rates | Prominent objective caveat in the primary result panel; detailed rates remain in the assumptions disclosure | Identifies why this candidate was generated; it is not a verified customer economic result |
| `physical.status = SCENARIO_ONLY`; physical profile claims `ALLOWED` with `SCENARIO_ONLY` scope | Explicit “physical result · synthetic scenario only”; each displayable physical claim remains scenario-scoped | Does not assert Macau site validation or safety/service feasibility |
| `HORIZON_PEAK` | Baseline/candidate horizon maximum | Explicitly not billing-period demand or Pu |
| `economic.status = BLOCKED`; monetary fields null; charge/demand/full-bill/savings claims withheld | “Not calculated”; no numeric placeholder or zero amount | Missing/assumed evidence does not become a favorable cost estimate |
| `COMFORT_SERVICE`, `CONTROLLABILITY`, `DEVICE_CONTROL`, `EXPORT_COMPENSATION`, `CROSS_SITE_CREDIT` withheld | Human-readable withheld reasons | No comfort, device authority, export credit or cross-site settlement implied |
| Local review buttons | Page-local message, cleared on reload | Not a persisted APP-11 review disposition, approval or execution command |

The visible UI remains a static JSON projection. It does not call the optimizer, implement an APP-11 adapter, persist an assessment/review, authenticate evidence, or establish canonical status names. The app-owned contract still needs to keep search objective/provenance separate from physical assessment, settlement assessment, claim disposition/scope, resource service outcomes and human review lifecycle.

## Finding and corrective action

The original v2.8 main result panel clearly blocked economic output, but left the fact that the search *used assumed rates as its optimization objective* in a collapsed details area. That made the generated schedule too easy to misread as a Macau economic recommendation. v2.8 now states the search objective and its unverified-price limitation in the primary result panel, and exposes physical scenario scope separately from economic status. A fresh browser accessibility-tree review confirmed these labels and the 44→44 kWh / 10→11 kW values.

## Remaining G7.9 / integration work

1. Review and approve application-owned meanings for search objective, physical assessment, economic assessment, claim disposition/scope, service outcome, evidence provenance and persisted human review; current names remain proposals.
2. Define a canonical APP-11 request/result/review contract and generated bindings only after authority/catalog ownership and product/domain/security decisions.
3. Add adapter-level acceptance cases for a candidate generated with assumed rates, blocked verified economics, service-not-assessed outcomes, scenario-only feasibility scope, absent/stale data, and non-persistent versus durable review behavior.
4. Implement and inspect a read-only, contract-backed vertical slice before treating the result page as integrated. G7.9 Step 3 remains OPEN until its designated design and acceptance evidence are satisfied.

## Verification limits

This review checked exact GitHub source blobs, the exact v2.8 JSON projection, browser-visible text and accessibility tree. It does not validate the actual Macau tariff, site, comfort/service models, complete localization, production app integration, operator usability, savings or pilot readiness.



## Current PR #14 implementation and UI lineage reconciliation — 2026-10-07

This addendum compares the live PR #14 head and the current PR #10 result fixture. It supplements the historical v2.8/v2.9 review above; it does not claim an integrated adapter or approve G7.9 Step 3.

### Exact revisions inspected

- PR #14 remains open, Draft and unmerged at head 9b80adca9243a0ae9a7bd666f0efee1acfc6309a.
- Current PR #14 assessment source: dispatch_assessment.py, blob 534ae269a7949601bd4504271e0076369807a68f.
- Current PR #14 optimizer source: dispatch_optimizer.py, blob 2d3256801f0ddce6b849c648c160f5a32fd90a27.
- Current PR #14 B1/C1 interval tariff-period mapper: macau_tariff_periods.py, blob f3f2e7db37ad7b502788335b282596d7dca5aa41.
- Current PR #14 historical bill-component replay: macau_bill_replay.py, blob dd31ae5fd6e5f9938e19ee6e22c29e0e38823c78.
- Current PR #10 v2.9 projection fixture: blob fec75272470155c531a1747ddf00db91ec00c583. Its embedded source manifest points to earlier PR #14 commit d5180703df3730779f1f180a89d07c620e7e349d and earlier assessor blob 4986bb546d675c469646881ab151dfd847725790. The optimizer blob matches the current optimizer blob, but the assessor lineage does not.
- On exact PR #14 head 9b80adca9243a0ae9a7bd666f0efee1acfc6309a, GitHub reported Optimizer, Contract Fixtures, Platform API, Edge Runtime, Repository hygiene and Validate authority structure checks completed successfully.

### Current experiment scope

The latest assessor adds independently scoped physical claims, resource-specific withholding, exact interval matching for import-energy rates, partial covered-interval reporting, and a per-interval trace for the eligible import-energy component. It deliberately withholds an interval if its rate boundary splits that interval because the input has no finer-grained energy quantity for exact allocation. The optimizer remains exact only over its declared short-horizon discrete action space and requires aligned import rates plus account/contract/tariff evidence to guide candidate generation.

The PR #14 branch additionally contains an effective-dated B1/C1 active-energy interval-rate mapper and historical B1/C1 bill-component replay over already classified meter/register evidence. The mapper is a narrow SHADOW input adapter, not a bill calculator. The replay is historical subtotal arithmetic, not candidate-schedule settlement or a complete bill. These functions do not establish a customer's tariff applicability, authenticate source evidence, calculate Pu from raw interval data, evaluate demand charges for dispatch, reproduce a full bill, or validate Macau site outcomes. The B1/C1 fixture rates are synthetic assumptions unless independently evidenced.

### Cross-layer finding

The v2.9 page fetches a local JSON fixture and renders that fixture; it has no optimizer API call, APP-11 DTO adapter, persistence, or authenticated evidence lookup. Its fixture is explicitly synthetic and economically BLOCKED, which is the correct presentation boundary. However, its embedded lineage names an earlier assessor commit/blob than the live PR #14 head. Therefore:

1. Treat v2.9 as a pinned historical synthetic projection, not as a projection of the current PR #14 implementation.
2. Before using it as exact current-head integration evidence, regenerate the fixture from current PR #14 source and update the manifest, or keep the older pin and state that limitation visibly in the review.
3. Add a reproducible UI/adapter contract check that compares the current optimizer/assessor output fixture with what the UI renders, including partial rate coverage, boundary-withheld intervals, verified versus assumption-tagged rates, scenario-only physical claims, unmodeled service, and all permanently withheld control/full-bill claims.
4. Preserve an explicit orchestration/application state for “no economic evaluation / not calculated”; do not fabricate this as an assessor enum or turn an assumed-rate search objective into verified customer economics.

### Remaining G7.9 Step 3 work

The evidence moves the optimizer from prose-only design into a bounded, CI-exercised research experiment, but the gate remains open. The next implementation slice still needs an approved APP-11 ownership and contract decision; immutable/authenticated input and evidence references; durable assessment lifecycle and tenant/site authorization; a canonical output DTO mapping physical/economic/claim/service/review states; and a UI client bound to that contract. Add adapter acceptance cases against the live PR #14 head, then inspect the runtime boundary and failure/recovery behavior. No device-command path belongs in this SHADOW slice.

The current green PR #14 checks prove their bounded job coverage at that exact head. They do not validate G7.9 gate completion, product approval, production architecture, bill-grade settlement, operator acceptance, or pilot readiness.
