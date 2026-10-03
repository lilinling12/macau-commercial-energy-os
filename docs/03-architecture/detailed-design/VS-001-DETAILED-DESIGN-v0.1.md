# VS-001 Detailed Design v0.1 — Energy Intelligence Loop

**Status:** Draft, research-derived; not an approved production design.  
**Scope:** Detailed logical design for the existing VS-001 shadow-mode vertical slice.  
**Authority:** VS-001, current handoff, D-006–D-009, D-012–D-029, D-069–D-076, G6.9-R2 Step 3C evidence, and contracts under `implementation/contracts/`.  
**Stack:** No production framework or cloud-core candidate is selected by this document. The pinned framework-native bake-off (G6.9-R2 Step 3D/4) remains authoritative.

## 1. Purpose and boundary

VS-001 proves a deterministic, evidence-producing economic intelligence path from site telemetry to an advisory recommendation. It is SHADOW-only. It does not authorize field commands, produce bill-grade settlement while G1 inputs are unresolved, or claim Macau customer savings from synthetic fixtures.

The logical path is:

```
Ingress → Identity/Schema Validation → Point & Asset Resolution
  → Energy Graph / Settlement Context → Tariff Rule Resolution
  → Deterministic Cost Evaluation → Shadow Recommendation
  → Evidence Record + Replay Manifest → Operator Read Model
```

The implementation may deploy these as modules in one service or separate runtimes after the stack decision. The boundaries below are logical ownership boundaries, not a mandate for microservices.

## 2. Component responsibilities

| Component | Owns | Must not do |
|---|---|---|
| Telemetry ingress | Validate schema, tenant/site scope, source time, quality and provenance; assign receipt metadata; persist accepted/rejected outcome | Infer missing identity, silently convert units, or treat receipt time as measurement time |
| Point resolver | Resolve device/point identity and effective-dated mapping to canonical asset/metric/unit | Guess an unmapped point or cross a tenant/site boundary |
| Energy Graph context | Resolve physical/electrical and settlement/economic relationships as distinct graphs, with explicit links and effective times (D-013) | Store an asset-level electricity price or collapse PV producer revenue into load (D-020/D-021) |
| Settlement resolver | Resolve meter, contract, tariff package/version, demand policy, and applicable interval | Substitute a guessed contract, tariff, or Pu window |
| Exact cost evaluator | Pure deterministic calculation with decimal monetary values, explicit units, versioned rules, and traceable intermediate values (D-022–D-028) | Mutate contract state or emit an executable control command |
| Recommendation builder | Produce a versioned SHADOW proposal with objective, validity interval, constraints/assumptions and evidence references | Claim realized savings or enter CONTROLLED_EXECUTION |
| Evidence/replay store | Preserve source references, mapping/rule/model versions, input identities, outputs, evaluation status and replay manifest | Rewrite past evidence when a rule or mapping changes |
| Operator read model | Present calculation status, uncertainty, missing inputs, and recommendation rationale | Hide UNKNOWN/PROJECT_ASSUMPTION status or represent an estimate as a verified bill result |

## 3. Processing contract

### 3.1 Ingress and canonicalization

The input is the existing `TelemetryEventV1` contract. Validate JSON Schema before domain processing. Required tenant/site/device/point, metric, value, unit and observedAt fields must be present. `receivedAt` records platform receipt time when available; it must not replace `observedAt`.

Authorization must bind the authenticated producer identity to the event tenant and site. Reject unauthorized scope, invalid schema, impossible timestamps under the configured policy, and unsupported unit/metric combinations. Preserve the original event or a content-addressed immutable reference so normalization can be audited.

The current contract does not define a producer event ID, idempotency key, mapping version, or normalization result envelope. Until a versioned contract adds these, ingress deduplication semantics and durable exactly-once claims remain OPEN; do not invent those fields as if they were current authority.

### 3.2 Resolution and time semantics

Resolve the point using tenant, site, device, point, metric, unit, and the event's `observedAt`. The mapping must be valid at that time and return a canonical asset/metric/unit plus the mapping version. An absent, ambiguous, expired, or conflicting mapping yields a non-billable/non-actionable result with an explicit reason.

Establish aggregation buckets from the declared clock and boundary policy before applying quality filters (D-074). Quality determines sample eligibility; it must not slide a fixed bucket. Keep event time, receipt time, and processing time distinct. Late/out-of-order handling and correction horizons require an explicit policy decision before production aggregation.

The Step 3C 15-minute semantic fixture is not the CEM Pu settlement interval. U-001 remains open: never hard-code 15 minutes as Macau demand settlement policy.

### 3.3 Context and tariff resolution

Resolve the settlement meter and contract from the effective-dated settlement graph, independently from physical topology. Resolve the immutable tariff and contract versions for each relevant interval (D-012, D-015, D-017, D-024). Store both valid/effective time and system/knowledge time.

If required contract, meter, tax, rounding, demand-window, PV or ESS settlement inputs are unresolved, return `UNKNOWN` or explicitly authorized `PROJECT_ASSUMPTION`; do not label output exact or bill-grade (D-019). Unknown/contradictory settlement context blocks bill-grade cost and economic ranking. The system may produce a clearly labelled partial engineering analysis only if its excluded components and assumptions are shown.

Keep grid-export/feed-in revenue as a separate producer-side stream. Do not allocate off-site PV production as another customer's bill credit without verified authority and contract evidence (D-077/U-025).

### 3.4 Cost evaluation and recommendation

The evaluator is a pure function over a pinned input set:
- canonical, quality-qualified quantities and their units;
- effective-dated meter/contract/tariff versions;
- declared settlement policies and provenance;
- evaluator/rule package version;
- evaluation interval and explicit clock boundary policy.

Return component values, intermediate quantities, input coverage, unresolved items, and the full version/reference set. Use decimal arithmetic for monetary truth (D-026); do not apply undocumented per-interval rounding (U-011). No mutable demand state is committed during evaluation (D-025).

The recommendation builder consumes evaluated context and forecasts/optimizer output, but emits the existing `OptimizationRecommendationV1` in `SHADOW` mode. `evidenceRefs` must resolve to persisted evidence. Objective values must identify their currency and status; when required settlement inputs are unknown, omit authoritative monetary claims or label the result as a project assumption. The current schema's numeric estimatedValue is not itself proof of settlement validity.

VS-001 recommendations are advisory and cannot call the Edge command path. This enforces D-006–D-008 and D-009.

### 3.5 Evidence and replay

Write an `EvidenceRecordV1` for each evaluation/recommendation outcome, including failed resolution and blocked calculation outcomes. Use status values according to evidence strength (`VERIFIED`, `DERIVED`, `HYPOTHESIS`, `PROJECT_ASSUMPTION`, `UNKNOWN`, `CONTRACT_VERIFIED`). Store immutable references to the input events, mapping/context versions, tariff package, evaluator build, optimizer/model version where applicable, output, and reason codes.

A replay manifest must pin all semantic inputs and versions. Correlation/trace IDs are observability metadata only and must not alter business identity or command identity (D-073). Replay with the same pinned inputs and versions must reproduce the same semantic output; if a dependency is missing, report replay as incomplete rather than silently using its latest version.

The current evidence schema supports source references and a derivation string but does not formally define a replay-manifest structure, immutable storage mechanism, or content digest. These are contract/design gaps for a follow-up decision and schema revision.

## 4. State and failure behavior

| Stage outcome | Required behavior |
|---|---|
| Schema or producer authorization fails | Reject/quarantine with stable reason; no downstream evaluation |
| Point/mapping is unknown or ambiguous | Preserve the event; create unresolved evidence; do not attach to a guessed asset |
| Cross-tenant/site reference appears | Deny and audit; never retry under another scope |
| Required settlement context is unknown/conflicting | Mark evaluation blocked/unknown; no bill-grade output or savings claim |
| Samples are BAD/UNKNOWN or insufficient | Keep fixed bucket boundaries; exclude per declared quality policy; mark coverage and result limitations |
| Evaluator/rule version is unavailable | Fail replay/evaluation explicitly; never substitute current latest |
| Optimizer unavailable or invalid | Retain valid analysis if available; emit no recommendation |
| Persistence fails | Do not acknowledge durable completion; retry only under a later approved idempotency contract |
| Duplicate/reordered delivery | Behavior is not fully specified by current telemetry contract; record as an open contract issue, do not assert exactly-once processing |
| Operator view unavailable | Processing/evidence remains authoritative; no effect on field controls because this slice has no control path |

Every failure should be observable with tenant/site-safe identifiers, stage, reason, source reference and trace ID. Sensitive payloads and credentials must not be written to general logs.

## 5. Security and trust boundaries

- Authenticate telemetry producers and authorize tenant/site scope at ingress.
- Enforce tenant/site filters in every lookup, workflow, persistence query and evidence reference.
- Treat BMS payloads and point names as untrusted input; validate size, type, unit, timestamps and schema version.
- Apply least privilege between ingress, evaluation, evidence persistence and operator read access.
- Protect secrets in a managed secret store; never place credentials or signing keys in events, logs or source control.
- Audit administrative changes to point mappings, contracts, tariff versions and evidence access.
- Use TLS in transit and encryption at rest according to the selected deployment environment; concrete key, identity, retention and rotation policies require a security design decision.

**G6 status:** this design does not close G6. The VS-001 path is shadow-only and contains no device write. The repository's G6 exit criteria additionally require verified local safety veto/limits, offline fallback, manual override, authenticated/idempotent command behavior, audit and replay, plus production command signing and Edge key lifecycle. U-022 remains OPEN / G6 SECURITY; Step-3C semantic evidence is not production cryptographic authority. A separate G6 evidence and closure record is required before any controlled deployment.

## 6. Observability and operational evidence

For each evaluation, record stage outcomes and durations, accepted/rejected event counts, mapping coverage, quality coverage, unresolved settlement inputs, tariff/evaluator versions, replay completeness, recommendation count, and evidence persistence outcome. Metrics and logs must respect tenant isolation and avoid high-cardinality raw point identifiers where inappropriate.

Operational targets (availability, latency, throughput, retention, RPO/RTO, late-event correction horizon, backup/restore, alert thresholds) are not established by current product authority. They must be set from validated pilot requirements and deployment mode before production readiness; this draft deliberately does not invent SLO numbers.

## 7. Current contract gaps and decisions needed

1. Telemetry producer event identity, deduplication/idempotency, mapping-version snapshot, and normalized-event result contract.
2. Stable evaluation request/result and reason-code contract; explicit evidence links and status propagation.
3. Replay manifest shape, content digest, immutable retention and correction policy.
4. Timezone/clock source, bucket boundary, late/out-of-order policy and retention horizon.
5. Exact monetary decimal representation and serialization policy across candidate runtimes.
6. Tenant/site authorization model and service-to-service identity details.
7. Pilot-derived SLOs, retention, restore, and operational support policy.
8. G1 settlement unknowns before bill-grade output; G6 proof before controlled execution; G6.9-R2 Step 3D/4 before production framework commitment.

These are design tasks, not implied decisions. Update the relevant Open Questions and versioned contracts before treating them as production authority.

## 8. Traceability

- Product requirement draft: `docs/02-product/PRD-v0.1.md`
- Logical architecture: `docs/03-architecture/ARCHITECTURE-DESIGN.md`
- Vertical slice: `docs/05-mvp/vertical-slices/VS-001-energy-intelligence-loop.md`
- Contracts: `implementation/contracts/telemetry-event.v1.schema.json`, `recommendation.v1.schema.json`, `evidence-record.v1.schema.json`
- Identity and tenant authorization design: docs/03-architecture/detailed-design/VS-001-IDENTITY-AND-TENANT-AUTHORIZATION-DESIGN-v0.1.md (draft; no identity provider or roles selected)\n- Cost-result and replay-manifest contract proposal: docs/03-architecture/detailed-design/VS-001-RESULT-AND-REPLAY-CONTRACT-PROPOSAL-v0.1.md (proposal only; not a canonical contract)
- Gate and decision authority: `docs/00-authority/handoff/CURRENT.md`, `docs/00-authority/decisions/DECISIONS.md`, `docs/00-authority/decisions/OPEN-QUESTIONS.md`, G6 and G6.9-R2 records.

## 9. Approval and exit criteria

This draft can advance only after:
- product owners validate the VS-001 workflow and acceptance criteria with target users;
- contract gaps are resolved or explicitly accepted as bounded MVP limitations;
- architecture decision records pin implementation choices after G6.9-R2 Step 4;
- G1 inputs are sufficient for the exact economic claims exposed by the product;
- G6 security/control evidence is separately reviewed and closed before any controlled execution;
- deployment, SLO, support, rollback and data-retention requirements are approved for the pilot.

Until then, the design is an implementation-planning artifact, not production authorization.
