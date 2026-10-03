# Telemetry Ingestion & Data Quality Detailed Design v0.1

**Status:** Stack-neutral design draft; contract ownership, product/site inputs and production operations remain open.  
**Scope:** Edge/BMS/utility integration boundary through authenticated raw-event acceptance, canonicalization, quality status, Energy Graph resolution and operator-visible integration health.  
**Authority:** D-013/D-014, D-024, D-038–D-040, D-065, PR-01/PR-02/PR-09, VS-001, G3/G6.9-R2.  
**Production status:** Not an approved canonical contract, transport, broker, storage or framework selection. No exactly-once ingestion guarantee is claimed.

## 1. Purpose and boundaries

Provide a controlled path for measured data from meters, BMS, Edge adapters and authorized utility sources into the Energy OS. Preserve what the source actually sent, establish authenticated origin and tenant/site scope, validate the wire contract, attach explicit provenance, resolve canonical point/asset semantics, and expose quality/freshness/coverage to downstream economics and operators.

This capability is not responsible for inventing measurement values, estimating missing intervals silently, deciding CEM demand settlement windows, or converting raw input into bill-grade quantities without an approved policy. It does not issue control commands. Exact cost evaluation remains owned by Tariff & Settlement; asset and settlement identity resolution remains owned by the Energy Graph; Edge command authority remains behind G6/Safety Kernel.

The ingestion topology may be a local Edge buffer plus a cloud ingress/API/event transport, a direct site connector, or another G6.9 candidate. Logical responsibilities remain the same; no broker, workflow engine or cloud service is selected here.

## 2. Required invariants

1. **Authentication is outside payload claims.** Derive producer identity, tenant/site authorization and connection identity from a verified principal/certificate/session. Payload tenantId/siteId are requested scope selectors and must match authorization; they are not credentials.
2. **Preserve source truth.** Retain the raw accepted payload and source/transport metadata or a durable immutable reference before normalization. Corrections create a new event/version; do not overwrite historical evidence.
3. **Separate clocks.** Keep source observation time, source-provided receipt time (if trustworthy), platform acceptance time and processing time distinct. Never substitute platform time for observed time.
4. **Fail closed for unusable semantics.** Invalid schema, unauthorized scope, unknown unit/metric, unresolved mapping or conflicting identity cannot feed exact tariff evaluation or optimization.
5. **Missing quality is not GOOD.** Missing, UNKNOWN, BAD and UNCERTAIN remain distinguishable. Eligibility is defined by an approved metric/site policy; it is not inferred from a clean parse.
6. **Freshness is policy-based.** Compare observed time to a metric/site freshness threshold and clock-skew policy; a successful API response alone does not make data current.
7. **No false exactly-once claim.** Current V1 lacks a stable producer event ID/idempotency contract. Ingestion is treated as potentially at-least-once; do not deduplicate by value/time/device heuristics where that could discard a valid measurement.
8. **No inferred settlement interval.** Transport/sample cadence, ingestion window, optimizer grid, control cadence and tariff demand policy are separate time semantics (D-027/D-040).
9. **Trace every transformation.** Contract, adapter, unit conversion, mapping and quality-policy revisions that affect a result are versioned and referenceable for replay.

## 3. Logical pipeline and responsibilities

| Stage | Responsibility | Output |
|---|---|---|
| **Site adapter / Edge collector** | Read protocol-specific registers or BMS points; preserve source IDs, units, source quality and source timestamps where available | Raw source record + adapter/source identity |
| **Authenticated ingress** | Verify producer principal and connection; authorize tenant/site scope; rate-limit and bound payload size | Authenticated request context |
| **Raw capture** | Persist original payload and immutable receipt metadata; assign platform event/receipt reference | Durable raw-event reference or explicit storage failure |
| **Wire-contract validator** | Validate selected contract version and required/optional/unknown-field behavior identically across runtimes | Accepted-to-canonicalization or quarantined validation error |
| **Canonicalizer** | Parse timestamp under one pinned rule, normalize enums/units only through explicit mappings, retain raw values and transformation versions | Canonical event envelope |
| **Identity/point resolver** | Resolve source namespace/device/point to canonical measurement and Energy Graph snapshot at event valid time | Resolved mapping or explicit unresolved result |
| **Quality and freshness evaluator** | Apply versioned source/metric/site policy for quality, range, clock skew, staleness, coverage and late arrival | Eligibility status plus reason codes |
| **Normalized event store / downstream publisher** | Persist append-only normalized event and emit it to downstream consumers with contract/mapping/policy references | Durable accepted event or retryable failure |
| **Data-health read model** | Aggregate connector heartbeat, arrival lag, missing/late/error counts, point coverage and policy status | Operator-visible health and impact |
| **Quarantine/replay workflow** | Retain rejected/unresolved records for authorized correction and controlled reprocessing | Reviewable reason, lineage and new processing result |

A logical stage may be implemented as a module, process or service after the bake-off. If raw persistence and normalized-event publication are separate, the selected architecture must prove their retry/reconciliation behavior; never drop a raw accepted payload merely because a downstream broker or consumer is unavailable.

## 4. Current V1 contract and observed gaps

The repository currently has implementation/contracts/telemetry-event.v1.schema.json, a manually maintained TypeScript parseTelemetryEventV1, and Go telemetry.Event. Static inspection on the current PR branch found:

- Schema V1 requires tenant/site/device/point/metric/value/unit/observedAt and disallows additional properties; quality, receivedAt and source are optional. Unit is a string but may be empty. format=date-time is declared.
- TypeScript mirrors most fields and rejects unknown keys, but the hand parser uses JavaScript Date.parse rather than a demonstrated strict shared date-time grammar. It requires the unit to be a string but does not reject an empty string.
- Go Event lacks receivedAt and source; no schema validator was found in the inspected type file. Default JSON decoding does not establish parity with the JSON Schema plus TypeScript rules.
- V1 has no producer event ID, sequence/cursor, source clock-quality field, normalization record, metric/unit registry version, authenticated producer reference, or mapping revision.
- The payload itself carries tenant/site strings; it cannot prove authorization.
- V1 value permits heterogeneous number/integer/boolean/string values. Downstream metric typing and unit semantics are not fully encoded here.

These are static design findings, not runtime test results. Do not claim cross-language contract equivalence, durable deduplication, trusted source time, or valid unit semantics from the presence of this V1 schema alone.

## 5. Canonical event envelope (proposal, not V1 schema)

After authentication and raw capture, an internal normalized envelope should logically retain:

- original V1/source payload and immutable raw reference;
- authenticated producer/principal reference and verified tenant/site scope;
- source namespace, source device/point IDs, source sequence/event ID if the integration supplies them;
- received connection/adapter identity and adapter build/version;
- observation time, platform acceptance time, processing time, timestamp parse result and clock-quality status;
- original value/unit/quality and canonical value/unit only when an approved conversion exists;
- canonical metric/measurement role, Energy Graph entity/mapping revision or explicit unresolved status;
- wire contract version, validator implementation/version, conversion registry version, quality policy version and provenance refs;
- duplicate/replay classification, stable reason codes, and accepted/quarantined status.

This envelope is a design target for a future contract revision. No field absent from V1 may be represented as if currently guaranteed. Decide source-event identity and compatibility policy before issuing V2; migration must preserve old payload replay.

## 6. Validation, normalization and quality semantics

### 6.1 Contract validation

Contract validation answers whether the message is structurally valid under one pinned version. It does not answer whether the measurement is accurate, authorized for the stated tenant, mapped to an asset or fit for billing.

Validation policy must define and pin:

- JSON/schema dialect and validator version or generated binding source;
- required, optional, null and unknown-field behavior;
- numeric bounds, finite values, string grammar and maximum payload sizes;
- strict date-time grammar, required timezone/offset semantics, precision and leap-second handling;
- unit non-emptiness and approved metric-to-unit compatibility;
- enum evolution and whether forward-compatible fields are rejected or retained in an extension envelope.

V1 currently rejects unknown JSON properties in the schema and TypeScript parser, but this behavior and Go parity must be established through the contract-authority experiment. Do not independently relax one consumer.

### 6.2 Time and ordering

Retain raw timestamp text and parsed instant. Proposed cross-runtime rule for review: require an explicit UTC offset and normalize to UTC for ordering while preserving original text/offset. This is not yet canonical; it must be approved and encoded in the source contract plus cross-language fixtures.

Clock skew is measured against trusted platform receive time with a source/site-specific tolerance. Future-dated, unparsable or implausibly old events are quarantined or marked non-actionable according to a reviewed policy; do not silently clamp timestamps. Late arrival is distinct from out-of-order observation. Correction horizon/watermark is a deployment/data policy, not part of the CEM Pu rule.

### 6.3 Values, units and measurement role

A metric registry binds canonical metric ID to dimension, allowed source types, canonical unit, expected range, precision, sampling/freshness expectations and settlement/action eligibility. Explicit conversion functions carry versioned source/target units and provenance. Unknown/incompatible units are rejected from canonical calculations; raw data remains inspectable.

Boolean state, enumerated state, scalar measurement and cumulative register are different value semantics. A cumulative register requires register identity, rollover/reset handling, multiplier and delta policy before energy deltas are derived. Do not convert a cumulative kWh register to interval power by assuming sample intervals or smoothing behavior.

A mapped point is not automatically a utility settlement meter. Graph resolution must state measurement boundary and role; the Tariff Engine separately confirms whether the resulting quantity is admissible for settlement.

### 6.4 Quality and freshness

Represent source-reported quality separately from platform eligibility:

| Source/processing state | Default interpretation |
|---|---|
| GOOD | Source reports good; still subject to mapping, range, freshness and clock checks |
| UNCERTAIN | Preserve; include only if an approved metric-specific policy permits and propagate status |
| BAD | Preserve in raw history; exclude from calculations unless a reviewed diagnostic use explicitly permits |
| UNKNOWN or missing | Preserve as unknown; never upgrade to GOOD by default |
| Parse/schema failure | Quarantine; not a usable canonical measurement |
| Freshness timeout | Mark stale relative to policy; retain for historical analysis if otherwise valid |
| Mapping unresolved | Preserve raw; no asset/settlement attribution |
| Source gap/coverage incomplete | Report missing coverage; do not interpolate silently |

Freshness thresholds and range/plausibility limits are source-, metric- and use-specific. Keep separate eligibility statuses for (a) dashboard display, (b) engineering trend analysis, (c) bill reconstruction, (d) forecasting/optimization and (e) any future control path. Passing one does not imply passing another.

### 6.5 Duplicate, replay and correction semantics

With no stable producer event identity in V1, use append-only ingestion and report likely duplicates as a diagnostic where a source-specific safe key exists. Do not collapse two records solely because tenant/device/point/value/timestamp match. If a future source contract provides stable event IDs, scope idempotency to authenticated producer + source namespace + event ID and retain collision evidence.

**Identity evidence and transport boundary (research note, 2026-10-04):** CloudEvents requires the producer to make `source + id` unique for each distinct event and permits a redelivery of the same event to reuse the same ID. This supports a source-scoped business-event identity invariant, but does not require adopting the CloudEvents wire format. MQTT 5 Packet Identifiers belong to a client/server session flow and become reusable after the corresponding acknowledgement; they are transport delivery identifiers, not durable event identity. Therefore, do not use MQTT Packet Identifier, connection ID, trace ID, timestamp, or payload hash as the cross-retry business event key. A future producer contract should supply a stable event ID in its authenticated source namespace. If a connector cannot supply one, the platform may assign an ingress ID at the first durable raw capture and reuse it for internal retry/replay; that does not identify duplicate source publications received as separate first captures, which must remain uncollapsed absent stronger source evidence. This is an evidence-backed design recommendation, not an approved V2 schema, CloudEvents adoption, or exactly-once guarantee.

A correction is a new event linked to the superseded source observation. Downstream recomputation creates a new assessment and evidence record; it never edits previously published economic evidence. Broker delivery retries must be idempotent at the consumer boundary only after the event identity contract and persistence/outbox behavior are specified.

## 7. Health, completeness and operator presentation

Integration health is not one green/red heartbeat. The read model should separate:

- connection/adapter state and last successful poll/heartbeat;
- event arrival lag (platform accepted time minus observed time) and clock skew;
- accepted, quarantined, malformed, unmapped, stale and duplicate-suspect counts;
- per-point coverage against the expected schedule and declared meter/BMS cadence;
- current quality distribution and last usable observation;
- mapped-point and settlement-boundary coverage;
- downstream queue/consumer backlog and persistence errors;
- impact on PRD tasks: affected cost period, unavailable component, stale recommendation or blocked evaluation.

State transitions should include HEALTHY, DEGRADED, STALE, UNAVAILABLE, CONFIGURATION_ERROR and UNKNOWN with explicit conditions and last-change times. Exact thresholds are site and service SLO decisions; none are invented here.

User-facing explanations identify source, measurement time, unit, freshness and mapping/evidence status. A partial dataset must show both the available time range and excluded/missing range. “No data” and “zero consumption” are never interchangeable.

## 8. Security, reliability and data governance

- Authenticate each connector/Edge workload; provision, rotate and revoke credentials under the deployment identity design. Production key lifecycle remains G6/U-022.
- Authorize producer principal to tenant/site/device scope before any normalized event is visible to downstream consumers.
- Apply per-tenant resource limits and bounded payloads; protect ingestion from malformed payloads and replay floods.
- Quarantine contains potentially sensitive operational data: access is tenant-scoped, audited and retention-limited under a policy still to be approved.
- Encrypt transport and stored raw/normalized data; select concrete controls, key custody and retention after deployment-mode/security review.
- Use durable buffering with bounded disk/storage and an explicit full-buffer policy. On loss of durable capacity, surface unavailable/backpressure state and do not acknowledge acceptance.
- Record correlation IDs as observability metadata, not event identity. Logs should avoid raw values/customer identifiers unless access-controlled and required.
- Define backup/restore and reprocessing procedures that preserve original payloads and version references.
- Exactly-once effects are not assumed. Duplicates, retries, late data and corrections remain explicit data states.

## 9. Failure behavior

| Failure | Required response | Downstream result |
|---|---|---|
| Authentication or tenant/site authorization fails | Reject and audit without exposing other tenant graph records | No event reaches normalized consumers |
| Raw capture unavailable | Do not acknowledge durable acceptance; signal backpressure | No tariff/recommendation use |
| Contract invalid/unsupported | Quarantine raw payload with contract/version and stable reason | No normalization |
| Timestamp invalid or timezone ambiguous | Quarantine or mark non-actionable under pinned policy; retain raw text | No time-dependent aggregation |
| Unit/metric mismatch | Preserve raw and quarantine mapping error | No economic/optimizer input |
| Energy Graph missing/ambiguous | Preserve raw, emit unresolved status and operator mapping task | No settlement/asset attribution |
| Source quality BAD/UNKNOWN or stale | Retain observation; exclude per use-specific policy and publish coverage reason | No silent zero-fill |
| Broker/consumer unavailable after raw capture | Retry from durable source with idempotent consumer reconciliation; expose backlog | No event loss or premature success claim |
| Clock skew/source reset/register rollover | Mark diagnostic state; require explicit correction/rollover policy | No derived consumption until resolved |
| Late correction after prior evaluation | Append correction, link prior evidence and schedule a new evaluation | Historic evidence remains reproducible |

## 10. Acceptance and design-exit evidence

Before PR-02/PR-09 can be declared implementation-ready:

1. Approve one source contract authority and pinned TypeScript/Go validators or generated bindings; prove identical positive/negative fixtures for presence/null/unknown fields, values, units, quality, date-time/timezone, and malformed inputs.
2. Resolve producer identity/event ID and delivery/idempotency contract; document whether each connector is at-most-once, at-least-once or has a stronger verified boundary.
3. Validate representative Macau meter/BMS connector inventories, metric/unit mappings, source clocks, multipliers/register semantics, sampling cadence and quality codes.
4. Establish authenticated producer-to-tenant/site/device authorization and negative cross-tenant evidence.
5. Demonstrate durable raw capture, quarantine, backpressure, restart/retry, duplicate-suspect handling and correction/replay lineage under the selected topology.
6. Set metric/site-specific quality, freshness, late-data, range and coverage policies with product/operator owners.
7. Define operator data-health tasks, screen requirements and alert/SLO thresholds based on user research and pilot operating model.
8. Prove downstream fail-closed behavior: unresolved, stale, BAD/UNKNOWN or unauthorized inputs cannot produce exact settlement, monetary savings claims or control proposals.
9. Complete security review for raw-data retention, encryption, audit, key lifecycle, deletion/retention obligations and incident handling.
10. Record implementation topology only after G6.9-R2 evidence and owner-approved architecture Decision Record.

This document is a logical design proposal and a list of evidence gates; no application tests were run for this documentation change.

## 11. Open decisions and evidence dependencies

- Canonical source contract: JSON Schema/OpenAPI/Protobuf experiment outcome and ownership.
- V1 compatibility vs V2 normalized envelope, event ID and correction identity.
- Strict timestamp grammar and timezone/precision policy across languages.
- Metric registry and unit-conversion governance, including registers, multipliers and flow direction.
- Source-specific quality codes, freshness thresholds, clock-skew tolerance and missing-data behavior.
- Expected event rate, retention, latency, durability, regional availability and SLO targets.
- Edge/offline buffer size and full-buffer behavior for the selected pilot.
- Tenant/site producer provisioning, certificate/key lifecycle and delegated integration partner access.
- Which source systems provide utility-settled quantities vs inferred/submeter quantities.
- User-facing data-health priorities and operator remediation workflow.

## References

- V1 contract: implementation/contracts/telemetry-event.v1.schema.json.
- V1 TypeScript parser: implementation/platform-api/src/vs001/contracts.ts.
- V1 Go event structure: implementation/edge-runtime/internal/telemetry/event.go.
- Existing VS-001 ingress semantics: docs/03-architecture/detailed-design/VS-001-DETAILED-DESIGN-v0.1.md.
- Authority: D-038–D-040, D-065, G3/G6 and OPEN questions U-003/U-006/U-021/U-022.
- CloudEvents Core Specification, event identity and duplicate redelivery: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
- OASIS MQTT Version 5.0, Packet Identifier scope and reuse: https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
