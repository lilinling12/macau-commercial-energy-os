# APP-11 Assessment Result Projection and UI Adapter Proposal v0.1

**Status:** Stack-neutral design proposal. Not an approved APP-11 catalog decision, wire contract, API, storage model, service split, or production implementation.  
**Date:** 2026-10-06  
**Repository baseline:** PR #10 `product/source-load-economic-dispatch`, head `71bfcb1b5e8467a684e2b82c45b4bfa5cf5df51f` (Draft/open/unmerged).  
**Implementation comparison:** PR #14 `poc/shadow-dispatch-assessment`, head `236c75a0eaecbff4bfc2099896a14efef7d4d704` (Draft/open/unmerged).  
**Purpose:** Define a reviewable mapping from the actual bounded optimizer output to a future dispatch-result view, without treating prototype dataclasses as an approved API or conflating physical, service, economic, evidence, review, and control states.

## 1. Why a separate projection is needed

The current repository has three related but distinct artifacts:

1. PR #10's `DISPATCH-CLAIM-STATE-PRESENTATION-CONTRACT-v0.1.md` proposes UI dimensions and safe display rules. It deliberately leaves canonical enums and wire fields open.
2. PR #14 implements a Python supplied-schedule assessor and a bounded finite-horizon discrete search. Its outputs are experiment-local Python dataclasses, not an application contract.
3. PR #10's v2.6 prototype has four synthetic evidence/status examples and a separate fixed synthetic schedule example. Neither is populated from PR #14.

The UI therefore needs a **result projection** that preserves the meanings and provenance of a real application result after owner and contract decisions. It must not imply that v2.6 is already connected to the optimizer. This proposal describes the mapping and gaps; it does not define JSON, OpenAPI, Protobuf, database rows, event envelopes, or endpoint names.

## 2. Evidence inspected

Exact code and design evidence at the revisions above:

- PR #14 `dispatch_assessment.py`, blob `4986bb546d675c469646881ab151dfd847725790`: `AssessmentRequest`, `AssessmentResult`, interval comparisons, import-energy component, claim ledger, validation and assessment behavior.
- PR #14 `dispatch_optimizer.py`, blob `2d3256801f0ddce6b849c648c160f5a32fd90a27`: `DispatchSearchRequest`, `DispatchSearchResult`, finite search, declared search scope, and candidate schedule.
- PR #14 `SHADOW-ASSESSMENT-PROTOTYPE.md`, blob `731dc465a5d23ef94d40b124a6e07c9ef7dbfe45`: prototype boundaries and limitations.
- PR #10 `DISPATCH-CLAIM-STATE-PRESENTATION-CONTRACT-v0.1.md`, blob `3d621c51c8eb34c0642eb56dada938fd0903fb47`.
- PR #10 `PR14-TO-DISPATCH-UI-RESULT-ADAPTER-TRACE-2026-10-05.md`, blob `234695728693e14a6b320d466bc382c24dc1c665`.
- PR #10 `G7.9-STEP3-DISPATCH-CONTRACT-IMPLEMENTATION-MAP-v0.1.md`, blob `9cc5acec84d13e8cb255f9eb4381c32b9a98829b`.

These are proposals and an isolated experiment on unmerged PRs. Passing their branch checks does not make their model canonical.

## 3. Authority and mapping rules

### 3.1 Keep the result projection separate from the optimizer DTO

The application boundary should own a versioned assessment identity, authorization, input-snapshot pin, lifecycle, persistence/replay, and human-review linkage. The optimizer may return bounded domain findings; it must not become the owner of tenant authorization, audit lifecycle, settlement scope authorization, or equipment-control authority.

A future adapter should be deterministic and side-effect free:

`application input + optimizer result + pinned provenance -> result projection`

It may qualify or withhold presentation claims according to application evidence and authorization policy. It must not upgrade a claim, mark caller evidence VERIFIED, infer missing contracts, or turn a partial component into a bill total.

### 3.2 Illustrative view-model shape (not a schema)

The names below are explanatory placeholders to make ownership reviewable. They are not approved field names or serialization requirements.

```text
AssessmentView
  identity
    assessmentRef?                  # application-issued; absent in PR #14
    assessmentRevision?             # immutable result revision; absent in PR #14
    siteRef
    planningWindow                  # [start, end), site timezone and interval grid
    createdAt?
  provenance
    origin                          # SYNTHETIC | SCENARIO | SITE_EVIDENCED, by application policy
    inputSnapshotRef?               # immutable; absent in PR #14
    mapping / tariff / model refs?  # effective-dated and authorized; absent or caller-only in PR #14
    algorithm / policy version?
  physical
    status                          # raw bounded status preserved
    claimScope                      # qualification, not a global readiness badge
    reasons[]
    baseline / candidate metrics
    intervalComparisons[]
    resourceElectricalClaims[]
  serviceByResource[]
    subjectRef
    outcome                         # NOT_ASSESSED | PASS | VIOLATION | UNKNOWN, only when modeled
    evidenceRefs[]
    reasons[]
  economicEvaluations[]
    settlementScopeRef?             # independently authorized; PR #14 has one context, no scope identity
    status
    component                       # e.g. GRID_IMPORT_ENERGY_ONLY
    currency / period / coverage
    componentTotals
    intervalComponents[]
    claims[]
  claimLedger[]
    claimType
    subjectRef?
    disposition                     # ALLOWED | WITHHELD
    scope                           # VERIFIED_BOUNDED | SCENARIO_ONLY | PARTIAL | NONE
    reasons[]
    supportRefs[]
  search?
    scope / scenarioOnly / transitionsExamined
  review?                           # APP-07 or chosen owner; distinct, append-only lifecycle
  controlAuthority                  # UNAVAILABLE in this MVP
```

A renderer may create labels or grouped summaries from these dimensions. It must retain the underlying status, scope, source and reason for assistive technology, export, replay, and audit.

### 3.3 Exact PR #14 source-to-view mapping

| Current PR #14 output | Future view treatment | Boundary / missing information |
|---|---|---|
| `AssessmentResult.physical_status`: `VALIDATED_WITHIN_SCOPE`, `SCENARIO_ONLY`, `PARTIAL`, `BLOCKED`, `INFEASIBLE` | Preserve raw value. Suggested labels: “Validated within declared scope,” “Scenario only,” “Partial,” “Blocked,” and “Infeasible under stated constraints.” Keep BLOCKED (unknown/unavailable inputs) distinct from INFEASIBLE (known constraints cannot be met). | Do not remap `VALIDATED_WITHIN_SCOPE` to unqualified “COMPLETE” or “site feasible.” A transport/runtime failure is not an `INFEASIBLE` result. |
| `AssessmentResult.claim_scope` | A coarse qualification for summary only. Show per-claim scopes from the ledger beside each claim. | Never synthesize a single green “ready” badge or let the top-level scope override a narrower claim. |
| `AssessmentResult.claim_readiness[]`: `claim`, `status`, `scope`, `reasons`, optional `subject` | Render a claim ledger: allowed/withheld disposition, qualification, affected subject and reason. | `ALLOWED + PARTIAL` means “allowed for partial scope”; it is not status PARTIAL. Reason strings are prototype text, not canonical reason codes. The `subject` is optional and does not resolve an authorized site asset identity by itself. |
| `AssessmentResult.interval_comparisons[]` | Source/load schedule rows and chart series, when the relevant profile claim is allowed. Preserve interval [start,end), source/load components, and units. | Each interval can be hidden or qualified by claim policy. Do not render unsupported intervals as zero. Baseline and candidate are supplied/assessed schedules; they are not evidence of an executed schedule. |
| `baseline_import_energy_kwh`, `candidate_import_energy_kwh`, `baseline_peak_grid_import_kw`, `candidate_peak_grid_import_kw` | Show only with the corresponding allowed profile/peak claim, site boundary and horizon. | A horizon peak is not tariff Pu without tariff meter-window and billing-period mapping. Energy is not money. |
| `economic_status`: `COMPONENT_AVAILABLE`, `PARTIAL`, `SCENARIO_ONLY`, `BLOCKED` | Label the named economic component and its coverage. | This enum describes the prototype import-energy component only. It is not a full-bill status. `NOT_CALCULATED` is an application/UI orchestration state when no economic child evaluation was requested or produced; it is not a PR #14 enum. |
| `economic_component`, currently `GRID_IMPORT_ENERGY_ONLY` when priced | Use the explicit component name: grid-import energy charge. | Do not label it total cost, full bill, savings, ROI, export revenue, demand charge, or PV credit. |
| `economic_covered_intervals`, `economic_total_interval_count`, `economic_interval_components[]` | Show coverage (for example, 4 of 6 intervals) and expose covered intervals with their rate evidence reference and MOP/kWh rate. | Uncovered intervals are withheld, not zero-filled. A boundary inside a schedule interval is withheld rather than priced at one side's rate. |
| `baseline_import_energy_charge_mop`, `candidate_import_energy_charge_mop`, `import_energy_charge_delta_mop` | If eligible, display values under “grid-import energy charge component,” with MOP, matched period, coverage and evidence. | Delta is candidate-minus-baseline for that component; never rename it “savings” or imply other bill components. |
| `reasons[]` / per-claim `reasons[]` | Present near the affected result; identify missing/unknown/stale/assumed evidence and next evidence needed. | These are caller/prototype text, not localized, canonical, typed, or guaranteed to be stable across versions. |
| `tenant_id`, `site_id` echoes | Use only after independent application authorization and site resolution. | They are request values echoed by the experiment, not proof of principal, tenancy, permission or site existence. Do not treat them as trusted authorization. |
| `EvidenceRef.ref/state` inputs | Show evidence state and human-readable provenance only after application-side lookup/authorization. | PR #14 does not authenticate, resolve, or pin those references to an immutable source snapshot. A caller label `VERIFIED` is not independently verified evidence. |
| `DispatchSearchResult.search_scope`, `scenario_only`, `transitions_examined`, `candidate` | Show algorithm scope and “scenario only” qualification; preserve the generated candidate alongside its assessment. | `EXACT_WITHIN_DECLARED_DISCRETE_ACTION_SPACE` is exact only within the declared discretization, horizon, objective, inputs and search budget. It does not mean a global optimum or production-feasible plan. |
| `DispatchSearchError` / validation rejection | Application-level error with correlation and safe retry/remediation semantics, if later designed. | Do not relabel an exception as physical INFEASIBLE, economic BLOCKED, or an optimizer “no solution” without typed error semantics. |
| No PR #14 field | Keep absent or explicitly unknown in projection; do not fabricate. | Assessment reference/version, trusted principal, input snapshot, independent physical and settlement scope IDs, effective-dated mappings, model freshness, reviewer record, audit replay reference, persisted idempotency, forecast uncertainty, full tariff components, and device-control authorization are not present. |

### 3.4 Physical schedule and settlement are separate children

One physical baseline/candidate schedule may later support zero or more independently authorized economic evaluations. Each evaluation must identify its own account/meter mapping, contract, tariff revision, effective period and component coverage. The application must not copy one site-wide total to multiple accounts or combine account results unless an approved objective defines that aggregation.

PR #14 is strictly narrower: one site ID, one caller-supplied account-meter/contract/tariff context and one rate series. Its result does not identify or authorize a settlement account. The view must show “single-scope prototype context” or equivalent and must not imply multi-meter/account support.

## 4. State rendering and lifecycle

1. **No assessment yet:** show an explicit empty/request state; do not render old results as current.
2. **Assessment queued/running:** application lifecycle only; distinguish it from physical/economic assessment statuses.
3. **Physical BLOCKED:** withhold metrics whose claims are withheld; show the missing mapping/input and affected scope. Do not show a balanced synthetic chart as the blocked site's output.
4. **Physical PARTIAL:** preserve only allowed claims and their partial scope. Mark each omitted/withheld interval or resource; do not infer completion.
5. **Physical INFEASIBLE:** show the known violated constraints and time/resource; never call it missing data.
6. **Scenario-only:** label the origin near every material result and in the result summary. Do not pass scenario values into verified economics.
7. **Economic NOT_CALCULATED:** show the reason and keep physical output independent. Do not show zero charges.
8. **Economic PARTIAL:** show exact covered intervals and component. Do not extrapolate to uncovered time, full billing period or savings.
9. **Human review:** review is a separate record linked to an immutable assessment revision. Reviewed, accepted for SHADOW monitoring, dismissed, or evidence requested do not mean approved execution.
10. **Control:** unavailable in the MVP. No execution CTA, command endpoint, or success state is implied.
11. **Replay:** replay the pinned inputs, policies and algorithm version; create a new immutable assessment result if any semantic input/version changes. Review history is append-only and separately attributable.

## 5. Proposed acceptance examples (not yet implemented)

| Case | Required projection behavior | Rejection condition |
|---|---|---|
| Valid physical profile, no economic evaluation | Show physical claims within declared scope; economic child is NOT_CALCULATED with reason. | Any bill amount or zero-valued charge appears. |
| Exact verified import-rate coverage for all assessed intervals | Show only the grid-import energy component, MOP, period, coverage and rate evidence. | UI calls it full bill, total cost or savings. |
| Partial rate coverage | Preserve eligible intervals and show partial coverage; list excluded intervals and reasons. | Missing rates are treated as zero or period total is extrapolated. |
| Core meter mapping missing | Physical claims depending on that mapping are blocked/withheld. | UI continues to show affected physical profile as site fact. |
| ESS limits/state missing, core electrical profile still supported | Preserve only allowed profile claims; withhold ESS/dispatch-feasibility claims. | An overall “feasible” state appears. |
| Electrical profile validates, HVAC service model absent | Electrical and service dimensions remain separate; service is NOT_ASSESSED/withheld. | “Electrically balanced” is shown as comfortable or service-feasible. |
| HVAC service violation with balanced AC power | Keep physical balance and service violation both visible. | One replaces or hides the other. |
| `ClaimStatus.ALLOWED` with `ClaimScope.PARTIAL` | Show allowed with partial scope. | Map to all-clear or invent a third claim status. |
| `PhysicalStatus.INFEASIBLE` | Explain known constraint failure. | Map to BLOCKED due to no evidence. |
| Project-assumption evidence or `scenario_only=true` | Mark scenario-only in header, affected metrics, chart legend and export. | Any site-validated or verified-cost wording appears. |
| Multiple settlement scopes introduced later | Independently authorize and evaluate each; display separate children. | Duplicate site total or cross-credit without approved aggregation rules. |
| Optimizer request rejected or runtime fails | Show a typed operational error/retry state at application layer. | Map it to an infeasible physical plan. |
| Review disposition recorded | Append review event tied to assessment revision and actor. | Mutate historical result or imply device execution. |
| Any MVP state | Device-control action absent/disabled with clear SHADOW wording. | Any available command path or “executed” status. |

## 6. Contract-owner decisions and sequencing

This proposal can be reviewed without settling a technology choice. A future implementation freeze still requires:

1. T0: reconcile the archived G7.8 Node/Fastify/contract-authoring completion label with current-main G6.9-R2 Step 3D pending and provisional C+ authority; decide whether APP-11 is a catalog capability or a composed workflow.
2. T1: approve domain status/reason semantics, evidence provenance and independently authorized physical/settlement scope boundaries.
3. T2: select the contract authoring/versioning profile under active D-065/D-068 authority; only then create canonical schemas/fixtures.
4. T3/T4: decide application ownership, trusted authorization, durable result/review identity, idempotency and immutable replay.
5. T5/T6: preserve read-only Edge and optimizer boundaries; complete claim, safety, settlement and service acceptance corpus.
6. T7: implement a single vertical slice that uses one pinned synthetic input manifest, an application-owned result DTO/projection and the dispatch UI. Verify replays, scope isolation, reviewer audit and disabled command path.
7. T8: only after real site, tariff, service and operational evidence exists, evaluate pilot readiness.

Do not mark G7.9 Step 3 complete from this proposal or PR #14's passing tests. The current research authority and owner decision packet remain controlling until reviewed decisions are recorded.

## 7. Current gap and next action

PR #14's bounded assessment can inform the physical/economic/claim mapping but lacks application identity, authenticated evidence, multi-scope settlement, canonical errors, durable review/replay and service outcomes. PR #10's v2.6 presents unconnected synthetic examples. This proposal makes the missing adapter boundary explicit, but the product is not yet a usable MVP.

Next stack-neutral work is to review this projection against the existing APP-11 map and claim-state presentation contract, then create one agreed semantic fixture set for:
- allowed physical profile + no economic child;
- partial import-energy component coverage;
- physical profile with a withheld resource/service claim;
- missing core mapping that blocks dependent claims;
- scenario-only assumptions;
- separate human review and control-unavailable states.

Only after product/domain/security semantics are accepted should that fixture become a canonical cross-language contract. No current view-model name, field, enum mapping or sample here is approved as a wire contract.
