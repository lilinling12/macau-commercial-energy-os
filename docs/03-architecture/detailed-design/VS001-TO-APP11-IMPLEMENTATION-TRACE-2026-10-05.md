# VS-001 to APP-11 Implementation Trace — 2026-10-05

**Status:** implementation-grounded addendum to the proposed G7.9 Step 3 map. It clarifies the current main-branch baseline; it does not approve a production design, close G7.9, or authorize equipment control.

**Compared revisions:** main `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`; PR #10 dispatch proposal `b2be14de8c87e9be9803887ab8e6946a94898532`. Main source blob IDs are listed below. This supplements Section 11 of `G7.9-STEP3-DISPATCH-CONTRACT-IMPLEMENTATION-MAP-v0.1.md`.

## What VS-001 actually executes

The controller is mounted at `/api/v1/vs001/evaluate` after the global `api` prefix. It passes an untrusted request body to a service that parses one `TelemetryEventV1`, resolves one Energy Graph context, evaluates tariff cost, records evidence and asks an optimizer for a SHADOW recommendation. The service compares resolved graph tenant/site IDs with event IDs and rejects a mismatch. It does **not** demonstrate authorization of the principal or site selector; that must be established at the application/security boundary.

The service's successful path in unit tests is created by static test doubles. The test's 10 kWh synthetic event and MOP 12.500000 amount do not come from a live meter, verified CEM settlement terms or a physical dispatch calculation. The recommendation fixture has an empty `actions` array. The replay CLI uses another set of fixed adapters, including a side-effect-free evidence repository.

The running application's default dependency bindings are different from those test doubles: the graph adapter returns `null`, the tariff adapter returns `UNRESOLVED`, the optimizer refuses to run without resolved tariff context, and the evidence repository is an in-memory map. Therefore the checked-in default API configuration does not complete a successful assessment against authoritative site data; it is intentionally fail-closed.

## Source evidence

| Main source (blob) | Direct observation | APP-11 implication |
|---|---|---|
| `implementation/platform-api/src/vs001/vs001.controller.ts` — `de93bc59354890f1e8be6274123ecf51f24fb3ca` | One POST handler at controller path `v1/vs001/evaluate`; no principal/site authorization is expressed in this controller. | Does not satisfy authorized assessment intake, durable ACCEPTED state, status/result reads, review or replay operations. |
| `implementation/platform-api/src/main.ts` — `e4937fe3c6e33caf86d3b439f192034671d8290f` | Adds global `api` prefix. | Combined route is `/api/v1/vs001/evaluate`; this remains a VS-001 route, not a selected APP-11 endpoint. |
| `implementation/platform-api/src/vs001/contracts.ts` — `12d52da087a96f7c7249d183e85fb404fb3b9414` | Scalar telemetry event with number/boolean/string value, free string metric/unit and one observed timestamp. | Needs a separate interval-series/snapshot contract with strict quantity, unit, sign, quality, temporal and source semantics. |
| `implementation/platform-api/src/vs001/ports.ts` — `4dc5303af249f9a5e8f55592063eacc64bba5b32` | Graph context has asset/meter/contract refs; optimizer consumes one event, one context, one settled cost and evidence ID. | No baseline/candidate horizon, topology, forecast, ESS state, controllable load limits, comfort/rebound constraints or typed feasibility result. |
| `implementation/platform-api/src/vs001/vs001.service.ts` — `a35cf74b4587fad75415689341de40d88e623ede` | Fail-closed resolution paths; graph tenant/site comparison; deterministic evidence ID; runtime assertion that returned recommendation mode is SHADOW. | Useful safety and evidence behavior to retain. Does not itself establish auth, durable evidence, schedule feasibility or independent physical/economic readiness dimensions. |
| `implementation/platform-api/src/vs001/adapters.ts` — `d4b0872fd9a52dedf8745cc45bdcbcd2fb3e83d6` | Default graph/tariff adapters fail closed; default optimizer refuses; repository stores records in memory. | No production site/settlement adapter or durable evidence/replay implementation is proven. |
| `implementation/platform-api/src/vs001/vs001.service.spec.ts` — `9d1449cc1aa40bdf81af0119cd0f31833b86493a` | Four service tests use static graph/tariff/optimizer and memory evidence doubles; include unresolved tariff, mismatch and stable evidence ID. | Keep these as unit-level behavior tests. Add contract, integration, persistence, authorization and dispatch fixtures before claiming APP-11 acceptance. |
| `implementation/platform-api/src/vs001/replay.ts` — `197068edb60ef342ed6cd26844fb2a02fcf89911`; fixture `b5f24ac2c9c5921e45b1f674a8722ac1559f2cd9` | Replays one fixed synthetic telemetry event through fixed adapters. | Deterministic fixture output does not prove persisted assessment replay or schedule reconstruction from pinned historical inputs. |
| `implementation/platform-api/package.json` — `c42fcbca6b423c392c920080999b0d3c6022a2cc` | Nest 12 + Express, Node 24.21.x, TypeScript 6.0.3, npm scripts for typecheck/test/replay. | Implementation fact only; not a framework bake-off result or production stack approval. |
| `.github/workflows/runtime-bootstrap.yml` — `c2ecdb3cddd5373f79872b8fe6bc8082f3bf4f2c` | Runs typecheck/tests, compares repeated synthetic replay output, plus Go/Python/contract checks. | CI coverage is bounded to existing bootstrap packages and fixtures; it does not exercise APP-11 acceptance scenarios or a live integration. |

## APP-11 gap-to-evidence map

| APP-11 responsibility in the proposal | Existing VS-001 contribution | Required design/implementation proof before acceptance |
|---|---|---|
| Inspect readiness by claim class | Graph/tariff failures can return fail-closed codes. | Typed readiness for physical schedule, operations and settlement separately; freshness/quality/evidence reasons; no invented values. |
| Request an assessment | A single event can be submitted to an evaluation handler. | Principal-derived authorization, authorized site resolution, idempotency, immutable input snapshot, durable acceptance and stable assessment reference. |
| Build common-horizon baseline/candidate | None demonstrated. | Versioned topology and interval inputs for grid/PV/ESS/loads; same-horizon physical balance; supported and missing constraints; typed feasible/infeasible/partial states. |
| Calculate economic outcome | A tariff port returns one event cost. | Independent settlement context bound to account/meter/site/effective period; componentized result, rounding semantics, blocked claims when evidence is unresolved. |
| Review recommendation | Response type includes SHADOW and safety review required. | Append-only authorized review disposition linked to immutable assessment/recommendation version; explicitly no command authority. |
| Persist and replay | Stable evidence ID and deterministic fixture replay. | Durable tenant-safe evidence, pinned model/input/tariff/solver versions, repeatable schedule replay, drift/unavailable-reference result. |
| Read-only Edge data | Go event type and bootstrap exist in main (per Section 11). | Protocol/source adapter, trusted identity, quality/freshness, authenticated forwarding/store-and-forward; no write capability in APP-11. |
| Operator workflow | Proposed prototypes in PR #10. | Bind UI states to actual API result semantics and persisted evidence; keep synthetic/demo values visibly distinct; rendered locale/accessibility and operator validation remain separate proof. |

## Recommended sequencing clarification

Preserve VS-001 as the small telemetry/economic-intelligence vertical slice and do not retrofit its scalar event into a schedule contract. The next APP-11 implementation-ready design should:

1. Reconcile APP-11 ownership with the PR #8 APP catalog and D-065/G7.8 contract-format authority.
2. Define separate versioned physical interval input/schedule and economic settlement result semantics, with valid/invalid synthetic fixtures.
3. Specify trusted authorization, idempotent durable intake, version-pinned snapshots and typed readiness before asynchronous execution.
4. Define deterministic physical baseline/candidate behavior and constraint diagnostics before selecting an optimizer.
5. Define durable result, append-only SHADOW review, replay and integration acceptance before connecting the prototype to real services.
6. Keep PR #10's technology-neutral service map provisional until the competing G6.9/G7.6/G7.8/Deep Research authority conflict is explicitly reconciled.

The existing G7.9 map already lists similar work packages. This addendum ties them to exact current source boundaries and shows why passing unit/replay/bootstrap evidence is insufficient to claim APP-11 delivery. The design remains a proposal; product, security and architecture owners still need to review the scope and authority decisions.


## Exact-head code-to-multi-scope reconciliation — 2026-10-05

**Rechecked PR heads:** PR #10 `ebc6fe581666e94ba8c2aa0e43d8e67c79c5a8eb` (open Draft, unmerged); PR #14 `b7ae02fe8dd4b346961235a7db523471c239b883` (open Draft, unmerged). The current PR #10 stack-neutral G7.9 map has blob `c374d678483df8ce816a2cdafa5b4aceed9c39c0`. This is a new comparison point; the earlier “Compared revisions” header above remains the historical source pair for its original audit.

The current PR #10 map proposes one physical `DispatchAssessment` with **zero or more** economic children, each evaluating that same schedule against exactly one separately authorized `SettlementScopeRevision` and its own settlement input manifest. The actor is authorized per child action; each scope has independent coverage, economic status, evidence lineage and replay. It further says child-by-child valuation does not define a site-wide optimization objective: a cross-scope optimum or combined savings claim needs a separately authorized and versioned aggregation policy. This is logical design text only; the APP-11 versus APP-05/06/07/08 decision remains unresolved.

At PR #14's current code head, direct source inspection confirms the optimizer remains a **single economic scope** experiment:

| Current code source | Directly observed shape | Gap relative to the proposal |
|---|---|---|
| PR #14 `dispatch_assessment.py`, blob `85ce0f2ac9a12bb30b7214b1caeb4a69b8edd53e` | `AssessmentRequest` has one `site_id` and optional `EconomicContext`; that context has one `account_meter_mapping`, one `contract`, one `tariff` and a rate series. `AssessmentResult` carries one site, no settlement-scope identifier/list/child result. | No independent account-child authorization, per-scope result cardinality, scope-specific replay or visibility filtering. |
| PR #14 `dispatch_optimizer.py`, blob `4c360a30f6c1b031cb42a4f7789007c07e795032` | `DispatchSearchRequest` has one `site_id` and one `EconomicContext`; the bounded search aligns that context's rate series to the supplied schedule intervals. | No list of settlement scopes, child valuations or approved cross-scope objective. It must not rank a combined multi-account total. |
| Main `implementation/platform-api/src/vs001/vs001.controller.ts`, blob `de93bc59354890f1e8be6274123ecf51f24fb3ca` | One `POST evaluate` request for VS-001. | It is not APP-11 assessment intake and does not declare action-specific settlement-scope authorization. |
| Main `implementation/platform-api/src/vs001/contracts.ts`, blob `12d52da087a96f7c7249d183e85fb404fb3b9414` | One scalar `TelemetryEventV1` record with one observed timestamp/value/metric/unit. | It is not an interval-series horizon snapshot, physical schedule contract or per-meter/settlement-child result contract. |

The caller-supplied `EvidenceRef` values in PR #14 are prototype readiness markers; the code does not authenticate them by resolving a trusted source manifest. PR #14 also has no immutable snapshot storage, multi-account replay, APP-11 API or durable lifecycle. Its partial per-interval import-energy evidence improves local explanation but does not close these trust and scope gaps.

**Implementation consequence:** keep this code as an explicitly bounded experiment. Do not map `EconomicContext` directly to a production contract or count an optimizer test as multi-scope acceptance. Before any APP-11 implementation is accepted, resolve catalog ownership/contract authority; authorize each requested settlement child from trusted grants; resolve and pin one physical input snapshot plus each child manifest; keep physical and economic statuses separate; persist idempotently; and replay/re-authorize each child without substituting current inputs. If the product later chooses a cross-scope optimization objective, approve its included scopes, monetary components, demand treatment, effective periods, missing-child behavior and roll-up semantics first. No schema, endpoint, database, runtime or production optimizer is selected here.
