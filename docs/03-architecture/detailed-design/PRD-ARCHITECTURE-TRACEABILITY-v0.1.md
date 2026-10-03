# PRD-to-Architecture Traceability v0.1

**Status:** Draft gap analysis; requirements remain research-derived and customer-unvalidated. A preliminary source audit of VS-001/Edge/optimizer scaffolding is recorded below; this is not a full implementation or runtime audit.  
**Purpose:** Make the path from product requirements to architecture, contracts, evidence, and implementation auditable. This document does not approve scope, close a Gate, or assert implementation completion.  
**Authority:** `docs/02-product/PRD-v0.1.md`, `PRODUCT-DESIGN.md`, logical architecture, VS-001 detailed-design draft, current contracts, and current handoff.

## Coverage scale

- **Partial:** a logical principle or partial contract exists, but at least one required behavior lacks a complete design/contract or validation evidence.
- **Gap:** no sufficiently specific design/contract is currently linked.
- **Not audited:** implementation-to-requirement mapping and runtime acceptance evidence have not yet been reviewed in this matrix.

No row is considered complete solely because a concept or schema exists.

## Requirement traceability

| PRD requirement | Logical owner / design reference | Current contract or evidence | Design status | Missing work before acceptance |
|---|---|---|---|---|
| **PR-01 Tenant/site scope** | API/auth boundary, telemetry ingress, Energy Graph, persistence and evidence access; VS-001 identity/tenant authorization design v0.1; VS-001 detailed design §5 | telemetry contract carries tenant/site selectors; service compares resolved context; current HTTP path has no auth guard | Partial; detailed auth design draft added | Validate identity provider, roles and delegated access; implement authN/authZ and scoped repositories/cache/jobs; provide cross-tenant negative tests, audit and revocation evidence; no production identity implemented
| **PR-02 Data quality/provenance** | Telemetry ingress, point resolver, data-health read model; VS-001 §§3.1–3.2 | `telemetry-event.v1` includes quality, observedAt, receivedAt and source as optional fields | Partial | Decide required/optional semantics, freshness policy, mapping status and normalization envelope; define stale/missing/invalid behavior and UI evidence; implementation mapping not audited |
| **PR-03 Energy Graph context** | Physical/electrical graph and separate settlement/economic graph; VS-001 §2 and §3.3 | D-013 and product design; no complete versioned graph-resolution contract linked here | Partial | Specify canonical entities, stable IDs, temporal relationship/mapping contract, provenance, conflict rules and resolution result; validate actual site topology; implementation mapping not audited |
| **PR-04 Tariff and bill analysis** | Settlement resolver and exact cost evaluator; VS-001 §3.3–3.4 | D-012, D-015, D-019, D-022–D-029; G1; tariff rules and Golden Bill fixtures | Partial / G1 blocked | Resolve U-001/U-009/U-010/U-011 for the applicable customer tariff; define evaluator request/result and rule-package contract; prove applicable Golden Bill criteria before bill-grade acceptance |
| **PR-05 Cost/demand explanation** | Cost analysis read model and evaluation trace; VS-001 §§3.4; result/replay proposal v0.1 | Current implementation returns one synthetic amount and refs; draft proposal adds decimal amounts, status, components, coverage, provenance, clock-policy identity, and explicit consumer/PV/site-scenario scopes | Partial; draft proposal added | Review the draft's settlement-stream and clock-policy semantics; define required component catalogue, decimal grammar/scale/rounding and cross-stream aggregation rules; approve/version canonical schema and verify against real tariff/G1 evidence; implementation remains synthetic
| **PR-06 Shadow recommendation** | Forecast/optimizer adapter, recommendation builder; VS-001 §3.4 | `recommendation.v1` supports SHADOW/HUMAN_APPROVAL/CONTROLLED_EXECUTION, objective, actions and evidenceRefs | Partial | Pin forecast/optimizer input/output versions, baseline, constraints, uncertainty, model identity and reason codes; prevent shadow outputs from entering command path by architecture and runtime evidence; G2/G4/G5 evidence remains required |
| **PR-07 Evidence, audit and replay** | Evidence/replay store; VS-001 §3.5; result/replay proposal v0.1 | Current EvidenceRecordV1 is generic and persistence is in-memory; proposal defines a version-pinned ReplayManifest with explicit clock/boundary policy reference | Partial; draft proposal added | Approve immutable source references, event identity, digest/canonicalization, storage/retention/correction policy and replay equality; implement durable store and verify against persistent data
| **PR-08 Operator review and authority** | Operator workflow/read model, approval service, command arbitration, Edge Safety Kernel; logical architecture; G6 | Recommendation mode enum and D-006–D-008/D-041/D-046/D-049 | Partial for shadow; Gap for controlled workflow | Define recommendation lifecycle, reviewer identity, approval scope/expiry/revocation, manual override, command/ack/effect states and audit contract. G6 is not closed; U-022 remains open. Do not expose controlled execution as authorized |
| **PR-09 Integration and run health** | Edge connector health, ingestion quality and operator read model; logical architecture | Edge responsibilities described in module README; telemetry contract | Partial | Define connector heartbeat/health and source-quality contracts, degraded-state propagation, operator-facing impact, alerting and operational runbooks/SLOs; validate against site integrations; implementation mapping not audited |

## Cross-requirement dependencies

1. **G1 economics:** PR-04/PR-05 acceptance depends on applicable tariff, demand-window, tax, rounding and Golden Bill evidence. Unknown rules must remain visible and fail closed.
2. **G2–G5 operational value:** PR-03/PR-06 need verified asset, flexibility, comfort, forecast and optimization semantics before predicted value can be represented as realizable.
3. **G6 Safety & Control:** PR-08 controlled workflow and any field write require independently reviewed safety, identity, key lifecycle, offline/manual behavior and replay evidence. The current SHADOW slice does not satisfy that gate.
4. **G6.9-R2:** implementation technology remains candidate-state pending Step 3D/4. Contract semantics may be designed now, but runtime-specific production architecture must not be presented as selected.
5. **G7 pilot evidence:** PR-06 and customer value acceptance depend on reproducible baselines and live evidence; simulation and Macau-site measurements remain distinct.
6. **Product validation:** role permissions, usability, deployment mode, SLOs, localization and commercial acceptance remain unvalidated and must feed PRD revision before scope is frozen.

## Preliminary source audit: existing VS-001 scaffold

The following source files were inspected on the PR branch. This is static code inspection only; no tests were run in this turn. The findings describe repository code, not successful runtime behavior.

| Requirement | Inspected source evidence | Preliminary implementation finding |
|---|---|---|
| **PR-01** | `implementation/platform-api/src/vs001/vs001.controller.ts`, `vs001.service.ts`, `ports.ts` | The service checks that resolved graph tenant/site IDs match the event. The HTTP controller accepts a request body without an authentication/authorization guard in this path. A caller-controlled tenantId is not identity or authorization proof. No end-to-end isolation evidence was reviewed. **Partial; security-critical gap.** |
| **PR-02** | `implementation/platform-api/src/vs001/contracts.ts`, `implementation/contracts/telemetry-event.v1.schema.json`, `implementation/edge-runtime/internal/telemetry/event.go` | TypeScript validates shape, allowed fields, basic types and parseable timestamps; event quality is optional. The Go Edge type serializes a telemetry shape. No freshness, metric/unit mapping, quality eligibility, normalization provenance or ingestion-health behavior was found in these inspected paths. **Partial.** |
| **PR-03** | `implementation/platform-api/src/vs001/ports.ts`, `adapters.ts`, `replay.ts` | A graph port exists. The default adapter always returns unresolved; the replay adapter returns hard-coded synthetic context. No durable/effective-dated Energy Graph implementation was found in these inspected files. **Interface/fixture only.** |
| **PR-04** | `ports.ts`, `adapters.ts`, `replay.ts`, `vs001.service.ts` | A tariff-resolution port and fail-closed adapter exist. Replay returns a fixed synthetic MOP amount and synthetic tariff/calculation refs. No authoritative tariff engine, effective-date rule resolution, demand-window policy, bill component calculation or Golden Bill evidence is present in this scaffold. **Interface/fixture only; G1 remains blocking for bill-grade claims.** |
| **PR-05** | `vs001.service.ts`, `ports.ts` | The result contains one currency/amount plus tariff/calculation references. It has no component breakdown, calculation trace structure, input coverage or explicit cost-result contract. **Partial contract gap.** |
| **PR-06** | `ports.ts`, `vs001.service.ts`, `implementation/optimizer/src/macau_energy_optimizer/recommendation.py` | The platform service rejects a recommendation unless mode is SHADOW; the Python code is a small recommendation data model with a SHADOW default, not an optimizer. Tests use a static optimizer stub. No baseline/constraint/forecast optimization behavior is evidenced here. **Shadow boundary scaffold exists; optimization capability not implemented by these files.** |
| **PR-07** | `ports.ts`, `adapters.ts`, `replay.ts`, `vs001.service.ts` | Stable evidence IDs are computed for a subset of event fields and an outcome suffix; the default repository is in-memory. Replay uses fixed synthetic dependencies and side-effect-free persistence. No durable evidence store, full input/version manifest, content digest or retention/correction behavior is evidenced. **Partial; deterministic fixture only.** |
| **PR-08** | `recommendation.v1.schema.json`, `ports.ts`, `vs001.service.ts` | The external schema enumerates SHADOW, HUMAN_APPROVAL and CONTROLLED_EXECUTION, while the current service type accepts only SHADOW. This is an appropriate boundary for VS-001, but no approval lifecycle, command arbitration, Edge Safety Kernel, signing/key lifecycle or command acknowledgement path is implemented by the inspected VS-001 code. **Shadow-only slice; G6 remains OPEN.** |
| **PR-09** | `implementation/edge-runtime/README.md`, `implementation/edge-runtime/internal/telemetry/event.go`, `event_test.go` | README lists intended adapters, buffering, retry and health responsibilities; inspected code defines/serializes an event structure. The inspected files do not demonstrate protocol adapters, persistent buffering, reconnect/retry, health reporting or an operator integration-health view. **Responsibility stated; runtime capability not evidenced.** |

### Additional repository-level implementation inventory

The recursive source tree and module entrypoints were also checked:

| Product capability | Repository evidence | Finding |
|---|---|---|
| User-facing product UI | No frontend/application UI source tree or UI package is present under `implementation/` in the inspected recursive tree | Product screens and interaction workflows are not implemented in the inspected implementation tree |
| Persistent domain storage / migrations | No database module, ORM models, migration files or durable evidence adapter appears in the inspected implementation tree | No evidence for production persistence, schema migration, tenant-scoped storage or recovery |
| API authentication and readiness | `platform-api/src/main.ts`, `app.module.ts`, `vs001.controller.ts`, `health.controller.ts` | Platform starts an HTTP server; no auth guard/provider is wired in AppModule. Health endpoint returns UP unconditionally; no dependency/readiness checks are evidenced |
| Edge runtime | `edge-runtime/cmd/edge/main.go`, `internal/telemetry/event.go` | Executable only logs that bootstrap started; event type exists, but no protocol adapter, broker/network transport, buffering, key management, command execution or local Safety Kernel appears in this tree |
| Command arbitration / Safety Kernel | `docs/03-architecture/command-arbitration/README.md`, `safety-kernel/README.md`; no corresponding implementation package in `implementation/` | Principles are documented, but policy evaluation, veto, command lifecycle, offline fallback, manual override, signing, replay protection and actuator writes are not implemented in the inspected tree |
| Simulator / live harness | `implementation/simulator/README.md` | Responsibilities and G7.2 constraint are documented; no simulator executable, BOPTEST adapter, run manifest generator or live R0 evidence is present in the implementation tree |
| CI evidence | `.github/workflows/runtime-bootstrap.yml`, `contracts-validation.yml` | Workflows define build/typecheck/unit/fixture/replay checks when triggered. They are not production integration, security, resilience, UI or pilot acceptance evidence |

### Scope and limits of this audit

This audit did not inspect every file or dependency in the repository, execute the application, run existing tests, review database migrations, verify deployment behavior, or conduct penetration/reliability tests. Tests present in the repository use in-memory/static fakes for the VS-001 service path; the Edge test inspected verifies event serialization. These are useful scaffold checks but do not establish product acceptance, persistent replay, site integration, G6 closure, or pilot readiness.

The implementation phase must extend this audit with code-level evidence for all modules, migrations, API handlers, workflow execution, UI screens, end-to-end acceptance evidence, production security and pilot behavior. For every PRD requirement, record:
- code location and owning module;
- approved contract/version and architecture decision;
- acceptance scenario and observed evidence;
- negative/failure-path evidence, including tenant isolation and recovery where applicable;
- review and status (pass, partial, blocked, not applicable with reason).

## Recommended sequencing

1. Validate user/task ownership and acceptance for each PRD requirement.
2. Resolve or explicitly bound G1/G2/G3 dependencies before claiming economic or asset semantics.
3. Close design gaps in contracts and component-level designs; record decisions and open questions.
4. Select the runtime topology only after G6.9-R2 Step 3D/4 evidence.
5. Audit current implementation against each requirement and close gaps in dependency order.
6. Complete security, reliability, G6 and G7 evidence before controlled pilot claims.
7. Keep this matrix updated with evidence links; do not change a status to complete based on planned work.
