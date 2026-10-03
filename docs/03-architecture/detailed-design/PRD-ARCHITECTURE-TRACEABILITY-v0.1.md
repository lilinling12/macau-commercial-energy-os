# PRD-to-Architecture Traceability v0.1

**Status:** Draft gap analysis; requirements remain research-derived and customer-unvalidated.  
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
| **PR-01 Tenant/site scope** | API/auth boundary, telemetry ingress, Energy Graph, persistence and evidence access; `ARCHITECTURE-DESIGN.md`; VS-001 detailed design §5 | `telemetry-event.v1` carries tenant/site IDs; product acceptance requires isolation | Partial | Define authenticated principal and tenant/site authorization model; propagate scope through API, events, jobs, storage, evidence reads and operator views; specify negative tests and audit evidence; implementation mapping not audited |
| **PR-02 Data quality/provenance** | Telemetry ingress, point resolver, data-health read model; VS-001 §§3.1–3.2 | `telemetry-event.v1` includes quality, observedAt, receivedAt and source as optional fields | Partial | Decide required/optional semantics, freshness policy, mapping status and normalization envelope; define stale/missing/invalid behavior and UI evidence; implementation mapping not audited |
| **PR-03 Energy Graph context** | Physical/electrical graph and separate settlement/economic graph; VS-001 §2 and §3.3 | D-013 and product design; no complete versioned graph-resolution contract linked here | Partial | Specify canonical entities, stable IDs, temporal relationship/mapping contract, provenance, conflict rules and resolution result; validate actual site topology; implementation mapping not audited |
| **PR-04 Tariff and bill analysis** | Settlement resolver and exact cost evaluator; VS-001 §3.3–3.4 | D-012, D-015, D-019, D-022–D-029; G1; tariff rules and Golden Bill fixtures | Partial / G1 blocked | Resolve U-001/U-009/U-010/U-011 for the applicable customer tariff; define evaluator request/result and rule-package contract; prove applicable Golden Bill criteria before bill-grade acceptance |
| **PR-05 Cost/demand explanation** | Cost analysis read model and evaluation trace; VS-001 §3.4 | PRD acceptance plus current telemetry/evidence schemas; no canonical cost-result schema linked | Gap | Define component/result schema with decimal representation, physical/economic units, input coverage, demand policy, tariff/rule versions, reason codes and source/evidence references; link UI journey and acceptance evidence |
| **PR-06 Shadow recommendation** | Forecast/optimizer adapter, recommendation builder; VS-001 §3.4 | `recommendation.v1` supports SHADOW/HUMAN_APPROVAL/CONTROLLED_EXECUTION, objective, actions and evidenceRefs | Partial | Pin forecast/optimizer input/output versions, baseline, constraints, uncertainty, model identity and reason codes; prevent shadow outputs from entering command path by architecture and runtime evidence; G2/G4/G5 evidence remains required |
| **PR-07 Evidence, audit and replay** | Evidence/replay store; VS-001 §3.5 | `evidence-record.v1` supports status, sourceRefs, derivation and notes; D-073–D-075 | Partial | Define immutable replay manifest, content identity/digest, retention and correction policy; pin mapping/rule/model/build versions; specify deterministic equality and incomplete-replay behavior; implementation mapping not audited |
| **PR-08 Operator review and authority** | Operator workflow/read model, approval service, command arbitration, Edge Safety Kernel; logical architecture; G6 | Recommendation mode enum and D-006–D-008/D-041/D-046/D-049 | Partial for shadow; Gap for controlled workflow | Define recommendation lifecycle, reviewer identity, approval scope/expiry/revocation, manual override, command/ack/effect states and audit contract. G6 is not closed; U-022 remains open. Do not expose controlled execution as authorized |
| **PR-09 Integration and run health** | Edge connector health, ingestion quality and operator read model; logical architecture | Edge responsibilities described in module README; telemetry contract | Partial | Define connector heartbeat/health and source-quality contracts, degraded-state propagation, operator-facing impact, alerting and operational runbooks/SLOs; validate against site integrations; implementation mapping not audited |

## Cross-requirement dependencies

1. **G1 economics:** PR-04/PR-05 acceptance depends on applicable tariff, demand-window, tax, rounding and Golden Bill evidence. Unknown rules must remain visible and fail closed.
2. **G2–G5 operational value:** PR-03/PR-06 need verified asset, flexibility, comfort, forecast and optimization semantics before predicted value can be represented as realizable.
3. **G6 Safety & Control:** PR-08 controlled workflow and any field write require independently reviewed safety, identity, key lifecycle, offline/manual behavior and replay evidence. The current SHADOW slice does not satisfy that gate.
4. **G6.9-R2:** implementation technology remains candidate-state pending Step 3D/4. Contract semantics may be designed now, but runtime-specific production architecture must not be presented as selected.
5. **G7 pilot evidence:** PR-06 and customer value acceptance depend on reproducible baselines and live evidence; simulation and Macau-site measurements remain distinct.
6. **Product validation:** role permissions, usability, deployment mode, SLOs, localization and commercial acceptance remain unvalidated and must feed PRD revision before scope is frozen.

## Implementation audit status

This matrix has **not** audited code paths, migrations, API handlers, workflow execution, UI screens, end-to-end acceptance evidence, production security, or pilot behavior. Repository presence of a module or contract is not proof that its PRD requirement is implemented.

For every PRD requirement, the implementation phase must add:
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
