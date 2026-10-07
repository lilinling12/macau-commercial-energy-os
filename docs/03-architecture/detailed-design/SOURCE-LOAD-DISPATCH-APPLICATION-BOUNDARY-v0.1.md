# Source/Load Dispatch — Application Boundary Proposal v0.1

**Date:** 2026-10-04  
**Status:** Proposed logical contract and service-boundary extension for review; no wire schema, endpoint, event name, module split, migration, optimizer, or production technology is approved here.  
**Purpose:** connect the source/load dispatch product task in PR #10 to the existing G7.9 Step 2 domain/data contracts and the PR #8 logical application/event catalog without silently changing either.

## 1. Why this addendum is needed

The G7.9 Step 2 package identifies these existing entities: Tenant, Organization, Site, Building, Energy Asset, Device, Telemetry Point/Record, Optimization Run and Recommendation. It lists telemetry ingestion plus building, asset and recommendation reads as baseline API contracts; its events include OptimizationCompleted and RecommendationGenerated. Step 2 marks itself complete and names **Step 3 Service Boundary and Implementation Design** as the next gate. The supplied Step 2 package says no business implementation code yet.

PR #8's `MVP-APPLICATION-AND-EVENT-CONTRACT-CATALOG-v0.1.md` expands the logical user operations as APP-01…APP-10. APP-05 is an economic assessment request; APP-07 is SHADOW recommendation review. Neither defines an interval-aligned, baseline-versus-candidate source/load schedule assessment. Those catalog rows are discussion identifiers, not selected wire APIs. PR #8 itself is still an open review branch and is not main authority.

The proposed product design in PR #10 makes that scheduling comparison a first-class operator task. This document adds **APP-11** as a proposed logical capability and maps it to service boundaries and G7.9 Step 3 outputs. It does not claim the entire Step 3 gate is complete.

## 2. Proposed APP-11 capability

**APP-11 — Request and review a source/load dispatch assessment**

The operator selects an authorized site, horizon and objective, reviews the evidence/readiness state, requests a reproducible assessment, compares baseline and candidate schedules, examines constraints and economic evidence, then records a SHADOW review disposition. A missing or unverified tariff may withhold cost claims while a separately valid physical comparison remains possible. An assessment or review never creates device-write authority.

| Operation | Logical owner | Proposed responsibility | Result semantics |
|---|---|---|---|
| Inspect assessment readiness | Site Model + Telemetry + Forecast + Tariff/Settlement | Resolve current evidence references and validity separately for physical, operational and economic claim classes. | Return ready/partial/blocked state per claim class, source versions, freshness and reason codes. No optimizer run is implied. |
| Request assessment | Optimization application boundary | Authorize tenant/site, pin immutable evidence/model/rule refs, validate horizon/objective/constraints and idempotency, then schedule bounded work. | Return stable assessment reference and `ACCEPTED`/`BLOCKED`; accepted means durable request only, never completed result. |
| Read assessment | Optimization / result query | Return immutable input refs, baseline/candidate series, feasibility, terms, uncertainty, withheld claims and evidence links. | Distinguish `RUNNING`, `COMPLETED`, `INFEASIBLE`, `FAILED`, `PARTIAL`, and `BLOCKED`; never translate these into “approved” or “saved.” |
| Review recommendation | Recommendation Review | Record authorized, append-only `REVIEWED`, `REQUEST_EVIDENCE` or `DISMISSED` disposition against a recommendation version. | Disposition does not change optimizer output, authorize execution, or assert measured outcome. |
| Replay assessment | Evidence & Replay | Recompute using original pinned versions or report why replay cannot be reproduced. | Preserve original result and report divergence/version drift separately. |

The eventual HTTP operations might be `POST /dispatch-assessments` and `GET /dispatch-assessments/{id}`; these are illustrative names only, not approved endpoints. The existing APP-05 bill/economic analysis, APP-06 result explanation and APP-07 recommendation review retain their own semantics. APP-11 may link to those results without merging their authority boundaries.

## 3. Bounded logical responsibilities

Keep modules logical until evidence supports independent deployment. This proposal does not require one service per row.

| Boundary | Owns | Explicitly does not own |
|---|---|---|
| Platform/API application boundary | Principal-to-tenant/site authorization, request validation, stable operation references, idempotency, status reads and audit correlation. | Trusting tenant/site IDs from request body; tariff interpretation; direct equipment commands. |
| Site Energy Model | Versioned physical nodes, meter/asset/point mapping, topology validation, effective time and evidence provenance. | Financial settlement links inferred from electrical connectivity. |
| Telemetry & Forecast | Time-stamped observations and predictions, quality/freshness/provenance, immutable query/snapshot references. | Treating a forecast as measured history or inventing missing constraints. |
| Tariff/Contract & Settlement | Effective-dated applicable rules, account/site/meter eligibility and componentized economic results. | Rewriting physical flows or inferring export credits from kWh alone. |
| Dispatch Assessment (capability within Optimization) | Readiness, common-horizon baseline/candidate construction, explicit objective/constraints, feasibility diagnostics and result provenance. | Contract-law authority, tenant authorization bypass, or command execution. |
| Optimizer adapter | Calculate bounded candidate schedules from normalized immutable inputs; return algorithm/version, feasibility and diagnostics. | Database ownership, access to device credentials, tariff applicability decisions, relaxing constraints silently. |
| Recommendation Review | SHADOW recommendation version and append-only operator disposition. | Turning review into approval-to-execute or mutating an assessment. |
| Evidence & Replay | Immutable references and reproducibility/difference results. | Replacing original inputs with current state during replay. |
| Edge integration | Read-only configured acquisition and forwarding of validated source data for this MVP. | Remote control writes or dispatch optimization policy. |

## 4. Assessment input and output semantics

### Required request meaning

The canonical contract must identify authenticated principal context, tenant/site, assessment horizon, site timezone, interval start/end and resolution, declared objective, immutable energy-model and input references, explicit constraint set, requested claim classes, and an idempotency key. If a tariff/settlement snapshot is requested, it must bind the tariff/contract revision to the account, site, meter, and effective period. Client-supplied scope fields are selectors only; authorization comes from the authenticated principal and stored grants.

Telemetry/forecast references must preserve measurement versus forecast, source and received times, units/sign, quality, provenance and coverage. A run cannot use a mutable `latest` pointer as historical evidence. Missing references are not silently substituted with current values or assumed zero.

### Required result meaning

Each assessment result records the pinned inputs, horizon/timezone, interval convention, topology/model version, constraint version, objective and supported terms, optimizer/model version, status, diagnostics, and evidence references. Baseline and candidate use identical interval sets, units, signs and input basis.

For each interval, a physical balance is checked against the declared meter boundary, conversion/loss terms and topology. A generic form is:

`grid import + on-site generation used + ESS discharge = site load + ESS charge + export + declared conversion/loss terms`

The site-specific meter topology determines which terms are observable. Unknown export, loss, meter placement or ESS state produces an explicit gap; the equation is not proof that every term is measurable. The same PV energy cannot be counted as both local use and export or as supply to multiple sites without independently evidenced topology.

Economic settlement is evaluated separately against eligible interval quantities and an applicable, versioned contract/tariff. The result must distinguish bill-grade, scenario-only, unavailable and synthetic evidence classes. The applicable main decisions remain controlling, including D-005, D-013, D-019, D-055, D-056, D-060 and D-077/U-025. In particular, grid-connected PV injection does not establish a cross-site credit or customer settlement right.

### Feasibility and claims

- `BLOCKED`: required inputs/evidence invalid or absent; do not run the affected claim class.
- `PARTIAL`: only explicitly permitted claim classes can be evaluated; list all withheld outputs and reasons.
- `INFEASIBLE`: evidenced constraints conflict; do not silently relax bounds.
- `COMPLETED`: a calculation completed; this does not establish site feasibility, economic truth, approval or execution.
- `FAILED`: bounded calculation failed; return typed reason and no stale candidate.

Physical scenario comparison, economic cost evaluation and operational service/comfort claims are separate claim classes. Unknown tariff applicability blocks bill-grade totals but need not block an otherwise valid physical-only comparison. Unsupported demand, export, degradation, comfort or rebound effects are omitted/withheld or explicitly labelled scenario assumptions, never silently assigned zero.

## 5. State, event and persistence boundaries

The operation must expose request acceptance separately from work completion. Candidate semantic states are `REQUESTED`, `VALIDATING`, `BLOCKED`, `QUEUED`, `RUNNING`, `PARTIAL`, `COMPLETED`, `INFEASIBLE` and `FAILED`; final state names and transition rules require contract review. Human review disposition is a separate append-only record. MVP has no `APPROVED`, `EXECUTED`, `DEVICE_ACKNOWLEDGED` or `MEASURED_SAVINGS` transition.

Any eventual event envelope must define schema version, tenant/site scope, stable assessment ID, aggregate/version, occurred/recorded times, causation/correlation, producer identity, and deduplication semantics. Publishing an event must correspond to a durable state transition. Events are notifications, not the source of truth by assumption. G7.9 Step 2 lists domain event types but does not select NATS, Kafka, MQTT or a delivery guarantee; transport choice remains separate.

Persist immutable run references/results, status transitions, recommendation version and human disposition with tenant-safe queries, retention and replay policy. Repeating the same idempotency key and identical semantic request should return the same operation reference; different inputs/objective/version create a distinct assessment. The precise transaction/outbox/workflow mechanics are implementation decisions for Step 3 and depend on the production architecture decision.

## 6. G7.9 Step 3 work-package mapping

| Required Step 3 output | Proposed artifact from this boundary | Still required for actual gate exit |
|---|---|---|
| Platform API modules | APP-11 operation, responsibilities, request/result semantics, authorization and status boundaries. | Reconcile with canonical API catalog; select schema source/generation; define auth, errors, pagination, compatibility and durable acceptance; reviewed examples/fixtures. |
| Edge boundary | Read-only acquisition of registered points/assets and forwarding provenance/quality/units; no optimizer or command authority. | Map to concrete adapter/input/output contract and validate against existing Go Edge implementation and integration threat model. |
| Optimizer boundary | Normalized immutable snapshots, objective/constraints, baseline/candidate and typed feasibility/diagnostics. | Pin supported algorithm/objectives and solver version; prove units, temporal semantics, bounded execution, deterministic/replay behavior and failure contract with executable fixtures. |
| Repository implementation tasks | Sequence schema/contracts → readiness/application operation → optimizer adapter → result/replay → operator UI → operational evidence. | Confirm owner scope/stack decisions, map each task to existing modules and migrations, add CI/security/test gates and obtain review before coding. |

## 7. Proposed implementation and verification sequence

1. Reconcile APP-11 with APP-01…APP-10, PRD, product flow and G7.9 Step 2 source package; architecture owner reviews whether this belongs under Optimization or a separate bounded context.
2. Define canonical logical schemas and examples for request, input refs, interval series, result, constraints, withheld claims and review disposition. Add unit/timezone/sign/evidence semantics and backward-compatibility tests before choosing wire transport.
3. Add a deterministic synthetic fixture with grid/PV/ESS/HVAC values, a same-horizon baseline, candidate and rebound window. Prove interval balance and an infeasible case. Keep tariff evidence explicitly absent in the physical-only fixture; verify bill-grade cost is withheld.
4. Implement tenant/site authorization, idempotent durable assessment request/status, immutable input/result refs and audit transitions before connecting any advanced optimizer.
5. Integrate one evidenced read-only Edge telemetry path; verify quality, freshness, mapping and replay references. Do not include device writes.
6. Add repeatable CI checks for schema compatibility, tenant isolation, physical balance, blocked/partial/infeasible behavior, retry/idempotency and no command side effect.
7. Map results to operator flow/prototype and record exact build, fixture, CI and manual review evidence. Gate exit remains a separate explicit decision.

## 8. Proposed acceptance cases

1. Valid same-horizon fixture balances each interval and makes units, signs, timezone and interval boundaries explicit.
2. A missing or ambiguous meter/topology mapping prevents fabricated balance and returns a typed blocked/withheld explanation.
3. Missing tariff applicability withholds bill-grade cost and savings while preserving only explicitly permitted physical claims.
4. Unverified PV export or cross-site rights never produce assumed compensation or credit.
5. Missing ESS SOC/efficiency or HVAC comfort/rebound bounds are visible as missing evidence or scenario-only assumptions; the solver never relaxes them silently.
6. Conflicting evidenced constraints return `INFEASIBLE` with reason codes, not a fabricated candidate.
7. Cross-tenant assessment/result/evidence/review access is rejected without leaking another site's existence or data.
8. Identical retry yields the same operation reference; changed inputs or objective yield a distinct versioned assessment.
9. Operator disposition is append-only and leaves the computed assessment unchanged.
10. Replay pins the original topology, telemetry, forecast, tariff, constraint, optimizer and schema versions; version drift is reported.
11. Assessment, review and replay produce no device-write request or control side effect.

These are proposed test requirements, not test results. They require domain, security, architecture and product review before becoming a gate.

## 9. Decisions deliberately left open

- Whether APP-11 is an extension of APP-05/APP-07 or a separate logical catalog row, and who approves it.
- Whether the first supported objective is physical peak/import shaping, verified economic cost, or both under distinct readiness.
- First site archetype and actual meter/asset topology; available temporal resolution and timezone/DST rules.
- Which assets and constraints have evidence: PV self-consumption/export, ESS SOC/efficiency/reserve/degradation, HVAC comfort/rebound, EV/thermal flexibility.
- Canonical API/event schema format and compatibility enforcement.
- Runtime/module allocation, durable workflow mechanics, database/time-series layout, event transport and replay retention.
- User roles, localization scope, security/privacy retention and MVP rollout criteria.

Until those items are reviewed, this document is a stack-neutral design proposal only. It does not establish the final MVP, production architecture, economic result, pilot readiness or G7.9 Step 3 completion.
