# Data Persistence and Schema Evolution Detailed Design v0.1

**Status:** Stack-neutral logical design proposal; owner/security/data review required.  
**Scope:** Durable data responsibilities and evolution rules across the SHADOW MVP's identity, telemetry, Energy Graph, tariff/settlement, cost/evidence/replay, recommendation review and operations paths.  
**Authority:** PR-01/02/03/04/05/07/08/09; D-013/D-014, D-022–D-029, D-065, D-073–D-075; G1/G3/G6.9-R2/G6.  
**Production status:** No physical schema, database, ORM, object store, event broker, retention period or migration has been approved or implemented by this document. PostgreSQL + Timescale remains an evaluation baseline, not a production choice.

## 1. Purpose and design boundary

The product must retain enough scoped, versioned evidence to explain what it knew when it produced a cost analysis or recommendation, recover after partial failure, and reproduce or explicitly refuse a replay. Data persistence is therefore part of product correctness, economic provenance, tenant isolation and safety boundaries.

This document consolidates logical data ownership and durability requirements already distributed across the architecture and detailed designs. It does not prescribe microservices, event sourcing, a specific database, or a physical storage topology. The design distinguishes:

- **Source facts:** accepted raw payloads and source documents, preserved with receipt/provenance.
- **Operational state:** current workflow, integration health and configuration projections, which may evolve while retaining an audit history where required.
- **Versioned domain knowledge:** mappings, contracts, tariffs, policies and models with effective-time and recorded-time provenance.
- **Derived evidence:** cost assessments, replay manifests, recommendation proposals and human-review events, each linked to exact input/version lineage.
- **Transport and job state:** publication, retry, consumer and workflow progress, which must not be mistaken for source identity or domain truth.

## 2. Non-negotiable logical invariants

1. **Acknowledge only recoverable facts.** A receipt, completed processing status or material result is reported only after the corresponding required data and lineage can be recovered under the declared durability boundary. Protocol acknowledgement, platform raw capture, publication and consumer completion remain distinct.
2. **Preserve original source evidence.** Do not overwrite an accepted payload or source document to apply normalization, correction or redaction. Keep a controlled reference to the original and record each derived version. Retention, deletion and legal-hold rules must still permit applicable law and customer agreements; “append-only” is not “retain forever.”
3. **Keep facts separate from projections.** A mutable current-state/read projection must be rebuildable from its authoritative records or have a documented reconciliation source. A cache or dashboard row is not the authority for settlement, identity, or audit.
4. **Version every result-affecting input.** Contract, tariff, graph mapping, quality policy, metric/unit conversion, model, code/build, schema and calculation logic versions are explicit replay inputs where they affect results.
5. **Separate event identity from storage identity.** Internal capture references support platform retry/replay. They do not prove two distinct first-seen source publications are duplicates. Do not collapse records by timestamp/value/hash heuristics.
6. **Scope every object and operation.** Every tenant-owned record, reference, background job, cache entry, export, replay and audit view preserves the authenticated and authorized organization/site/account scope. IDs are not capabilities.
7. **Keep time meanings distinct.** Observation/effective time, platform acceptance/recording time, processing time and publication time are separate. Bitemporal records distinguish when a fact applies from when the platform learned or changed it.
8. **Do not mutate prior economic evidence.** A correction, new rule, mapping or replay creates a new versioned assessment linked to the superseded or parent record. A newer answer must not erase what an earlier run used.
9. **Do not claim distributed atomicity.** If a logical operation spans independent stores or services, specify recoverable intermediate states, reconciliation and externally visible status. No cross-store transaction is assumed.
10. **No persistence path grants control authority.** Stored recommendations, approval annotations, queued jobs or replay results do not authorize device writes. SHADOW remains read/analysis/review only.

## 3. Logical data authorities and lifecycle

| Data domain | Logical authority and scope | Change / lineage semantics | Current unresolved physical choices |
|---|---|---|---|
| Organization, membership, site entitlements and policy | Energy OS authorization policy is authoritative for grants; identity provider only authenticates the principal | Grant/revoke changes are attributable and policy-versioned; each decision records the scope and effective/revocation state | Identity source, storage, revocation propagation, audit retention and access-policy implementation |
| Site, asset, meter, point and settlement relationships | Versioned Energy Graph facts, scoped to an organization and explicit site/account relationships | Bitemporal relationship/mapping revisions; conflict, unknown and superseded states remain visible; no destructive replacement of historical lineage | Physical schema, mapping review workflow, graph/ontology and source evidence |
| Raw telemetry receipt | The designated raw-capture authority holds original bytes/payload plus immutable receipt metadata and authorized source context | A platform capture reference supports internal retries; independent first-seen source publications are retained unless stable source identity proves redelivery | Database versus object/blob placement, transaction boundary, compression, partitioning, retention and broker custody |
| Normalized observations and quality | Versioned canonical event/observation plus references to raw capture, contract, resolver and quality policy | Append-only corrections/reprocessing; source time, platform time and processing time remain separate; duplicate suspicion is diagnostic unless source identity supports safe idempotency | Relational/time-series split, hypertable/partition strategy, metric registry and aggregation/retention policy |
| Tariffs, contracts and settlement configuration | Verified source artifact plus versioned normalized interpretation; uncertainty status is part of the record | Keep source language/document reference, applicability/effective period, recorded time, reviewer and parser/rule version; corrections create a new interpretation | Artifact store, source-document access, data classification, approval and legal-retention rules |
| Cost/demand analyses and replay manifests | Versioned evaluation record references exact observations, mapping, contract/tariff, policy, code/model and excluded inputs | Results and replay attempts are immutable/versioned; replay is marked reproduced, divergent, incomplete, blocked or not reproducible with explanation | Result schema, digest canonicalization, large artifact placement, precision/retention and replay equality policy |
| Forecasts, optimizations and recommendations | Versioned model/solver/evaluation run and SHADOW proposal; no implicit command authority | Inputs, horizon, uncertainty, constraints, objective, build and evidence refs are pinned; replacement creates a new proposal | Model artifact placement, training/data lineage, solver runs and product monetary semantics |
| Operator review and authorization audit | Append-only review/privileged-action event plus current read projection | Actor, action, target, scope, policy version and result are attributable; annotations never rewrite a proposal or authorize execution | Audit store, tamper evidence, retention, export and privacy policy |
| Publication, consumer and workflow progress | Durable transport/outbox/inbox/workflow metadata linked to internal capture/result IDs | At-least-once retries are visible; idempotent durable consumer effects use an approved stable internal/source key; status is reconcilable | Broker/workflow/database topology, transaction mechanism, backlog limits and operational ownership |
| Integration health and UI read models | Derived projections over source, receipt, processing and policy records | Rebuild/reconcile from the authoritative records; show freshness, missing coverage, backlog and blocked reasons rather than inventing zero/healthy | Projection store/cache, update latency, site-specific thresholds and SLOs |

The record authority is logical and does not require a separate service or database per row. A selected physical architecture may colocate domains if it preserves their ownership, scope, lifecycle and failure semantics.

## 4. Durability and transaction boundaries

### 4.1 Raw capture and capture receipt

The logical invariant proposed for owner decision #12 is: do not issue the platform capture receipt until the authorized source payload **and** the receipt metadata needed to identify and recover it are durable under the declared raw-capture authority. This is a recommendation for review, not a recorded owner decision.

If payload bytes and metadata share one transactional system, commit them with a recoverable pending-publication record before acknowledging. If payload and metadata use separate systems, their commits are not assumed atomic. The selected design must define observable states for staged, payload-durable, metadata-linked, recoverable, orphaned and failed work, plus a reconciliation process. Do not issue a receipt while the payload reference is missing, unreadable or not guaranteed recoverable.

A raw-capture reference is generated once and reused for internal retries. It must not be used to infer that separately received publications represent the same source event. Where a producer supplies a stable, authenticated event identity, its namespace and uniqueness scope must be defined before it becomes an idempotency key.

### 4.2 Publication and downstream consumer effects

A capture may be durable while downstream publication is pending. A recoverable publication marker/outbox or equivalent mechanism must be committed with the logical capture state so process restart can discover unpublished records. A broker acknowledgement proves only the broker's documented protocol boundary unless that broker is formally designated and verified as the raw-capture authority.

A consumer records the capture/event reference, durable domain effect and consumed/idempotency marker in a single selected transactional boundary where possible, then acknowledges delivery. If these are separate systems, use an explicit recoverable inbox/reconciliation protocol; do not state exactly-once processing. At-least-once delivery and duplicate attempts are expected.

### 4.3 Derived evidence, reviews and projections

A calculation/recommendation is shown as complete only when its result, input/version references, run identity and required evidence can be recovered. A large report or artifact may live in a separate store, but metadata must not point to an unverified or expired artifact while presenting the result as complete.

A user review annotation is persisted as an attributable event before the UI reports it saved. It does not mutate the source recommendation or imply approval to execute. Read models and dashboards may update asynchronously, but must expose their last-update/freshness state where it affects user decisions.

### 4.4 Failure/recovery matrix

| Failure point | Required recoverable state | User/operations status | Prohibited implication |
|---|---|---|---|
| Before durable raw payload and metadata | No accepted capture; request may be retried under protocol rules | Capture failed/not received; apply backpressure if capacity is unavailable | No durable receipt |
| Payload stored but metadata/receipt linkage incomplete across stores | Staged/orphaned item discoverable for reconciliation or cleanup under policy | Pending/incomplete; no successful capture receipt | No captured/processable claim |
| After raw capture, before publish | Durable capture plus discoverable pending publication | Captured; downstream processing pending | Not processed or economically eligible |
| After publish, before publish-state update | Recover/reconcile by capture reference; tolerate another publish attempt | Pending/reconciling; backlog visible | Not exactly once |
| Consumer effect committed, before broker acknowledgement | Redelivery resolves to the already-recorded durable effect using approved identity | Processed once at the domain-effect boundary if verified; delivery may repeat | No transport-level exactly-once claim |
| During analysis/evidence artifact write | Incomplete run remains recoverable or explicitly failed; no partial result presented as complete | Blocked/incomplete with stable reason | No final result/replay success |
| During mapping/tariff/schema migration | Old and new compatible state remain identifiable; migration resumes or rolls back without deleting source history | Degraded/maintenance status as scoped by runbook | No silent reinterpretation of historical output |
| During backup restore | Restore manifest states source snapshot, RPO/RTO and missing ranges; compare integrity before reopening writes | Recovery in progress, then verified/partial with reason | No claim of full continuity before reconciliation |

## 5. Tenant scope and data integrity

- Every customer-owned record and durable artifact carries or inherits an explicit organization/site/account ownership scope; cross-site portfolio objects enumerate or resolve their exact allowed member set.
- Foreign keys and query boundaries must prevent a record in one tenant/site scope from linking to another unless a separately authorized cross-site relationship is verified and deliberately modeled (for example a PV asset's physical host and producer/consumer settlement accounts remain distinct).
- Tenant scope propagates into transactions, outbox/inbox entries, workflow payloads, caches, exports, replay manifests and backup/restore procedures.
- Administrative membership changes are distinct from permission to read the sites. Candidate role/site grants are in the identity design and remain unapproved.
- Database row-level security, composite keys, schemas, partitions, per-tenant encryption or dedicated stores are physical controls to evaluate after deployment mode and G6.9-R2; none alone replaces application authorization.
- Malformed, unresolved or quarantined source data remains separated from eligible normalized/economic inputs. Corrections and mapping changes preserve prior interpretations and result references.

## 6. Bitemporal, version and replay behavior

For facts whose applicability changes over time (site topology, asset mapping, tariff/contract terms, policy configuration), retain both:

- **Valid/effective time:** when the fact applies in the physical, contractual or operational world.
- **System/recorded time:** when the platform received, recorded or superseded that knowledge.

For measurement records, keep source observation time distinct from accepted and processed time; do not invent a valid-time value from platform time. Record source clock/quality uncertainty separately where available.

A replay manifest should pin, at minimum, the capture/observation identities and hashes, tenant/site scope, source and contract versions, resolver/mapping revision, tariff/contract versions, quality and unit policy, algorithm/model/solver versions, configuration, time boundaries, build identity and any user-selected overrides. The exact canonical digest algorithm and fields remain open under the result/replay proposal. When an input is missing or retention has expired, mark replay unavailable or partial with a reason; do not silently substitute current rules.

## 7. Schema, contract and migration policy

Keep three kinds of version separate:

1. **External wire-contract version:** producer/consumer compatibility governed by D-065; a database migration does not change the wire contract automatically.
2. **Internal persistence schema version:** storage layout and indexes; a schema migration does not change the meaning of historical domain facts.
3. **Domain policy/logic version:** tariff, mapping, quality, unit, calculation, forecast or model semantics; these are pinned into affected results and replay lineage.

For a backward-compatible release, use an expand–migrate–contract sequence:

1. Add new nullable/additive fields, tables or indexes without removing old readers/writers.
2. Deploy code that can read the old and new form; write the new form only when all required consumers are compatible.
3. Backfill deterministically in bounded, restartable batches with checkpoints, rate limits, tenant scope, counts and reconciliation.
4. Validate counts, constraints, sampled lineage and financial/domain invariants; keep the old representation available during the rollback window.
5. Switch readers and writers deliberately, observe error/backlog/integrity signals, and retain a tested rollback path.
6. Remove the old representation only in a later change after compatibility is proven, backups are verified and the owner-approved retention/legal policy permits it.

For a breaking external contract, define the version, support window, producer rollout, dual-read/dual-write bounds, replay compatibility and retirement plan before implementation. Never “fix” old data in place to make it appear as if the new rules were always known. A backfill that changes economic interpretation produces a new versioned assessment and explicit lineage.

Migrations must be reviewable, deterministic, idempotent where feasible and safe to resume. Every migration packet names lock/downtime behavior, expected data volume, tenant impact, forward and rollback strategy, backup prerequisite, integrity checks and the exact application versions compatible during rollout. A destructive rollback that discards accepted telemetry, evidence or audit history is not an acceptable default.

## 8. Retention, privacy, backup and operations

- Classify raw telemetry, bills/contracts, access/audit events, derived assessments, model inputs and logs before customer-data intake. U-027 requires dataset and vendor-flow review; no data residency, cross-border transfer, retention period, legal-hold or deletion policy is approved here.
- Define data minimization and per-domain retention/deletion rules with applicable Macau law, customer contract and operational recovery needs. Where deletion or anonymization is required, record what can be removed, what lineage becomes unavailable, and how aggregate/audit records avoid retaining prohibited personal data.
- Backup scope includes metadata, raw payloads or their verified references, versioned domain rules/mappings, workflow/outbox state, evidence artifacts and identity/audit state. A database backup alone may not restore a cross-store replay.
- Restore is complete only after manifest checks, referential/integrity checks, backlog reconciliation, scope isolation checks and a documented partial/missing-range report. RPO/RTO, backup cadence, restore ownership and drill frequency remain owner/SLO decisions.
- Define capacity and backpressure for raw capture, time-series retention, outbox backlog, quarantine, replay and evidence artifacts before a pilot; do not discard evidence silently when capacity is exhausted.
- Logs and observability carry correlation and record references, not unrestricted raw customer payloads or credentials.

## 9. Slice-level acceptance evidence

| Slice / requirement | Minimum evidence implied by this design |
|---|---|
| VS-001 / PR-01/03/04/05/07/08 | Tenant-scoped domain records; versioned graph/settlement and tariff inputs; immutable assessment/replay references; review event durability; exact reconstruction of a selected synthetic/evidence fixture; denial across another tenant/site |
| VS-003 / PR-02/09 | Raw payload and receipt recoverability; separate protocol ACK/capture receipt/publication/consumer status; crash recovery at each matrix point; duplicate delivery without duplicate durable effect; backpressure/quarantine/health projection |
| Migration/release | Forward migration and compatibility evidence; interruption/resume and rollback plan; backup/restore integrity; no loss or silent reinterpretation of prior evidence |
| Pilot readiness | Owner-approved data classification/retention/residency and access policy; restore/operability owner; site-scoped authorization; agreed RPO/RTO/capacity thresholds and evidence retention |

These are proposed acceptance criteria. No application test, migration, backup/restore drill, data classification or pilot validation has been performed by writing this design.

## 10. Open decisions and dependencies

- Owner decision #12: confirm logical receipt invariant and connector-specific ACK mapping; no response is recorded.
- Owner decision #8: select/retain monetary-result semantics and result boundary before finalizing result schemas.
- Owner decision #14: validate role/action/site grants and review separation; all candidate grants remain denied.
- G1: tariff/demand/tax/Golden Bill evidence determines which settlement facts can be treated as verified and how long source artifacts must remain available.
- G3/U-027: site topology, source identity, customer-data classification, privacy/cross-border flows and authorized intake remain open.
- G6.9-R2 Step 3D/4: evaluate actual database, time-series, broker, workflow and deployment candidates with the same versioned contracts/workload; this design is not a candidate score.
- Physical data model, database isolation feature, partitioning, raw/evidence store, encryption/key scope, retention/deletion, legal hold, backup/restore RPO/RTO and migration tooling require separate review and decisions.
- No human or machine data model confers field-command authority; G6/G7/site authorization remain prerequisites.

## 11. Traceability and review status

- PRD: PR-01 tenant/site scope; PR-02 quality/provenance; PR-03 Energy Graph; PR-04 tariff/bill; PR-05 cost analysis; PR-07 evidence/replay; PR-08 review/audit; PR-09 integration health.
- Architecture: Logical Architecture Design; VS-001 Detailed Design; Identity and Tenant Authorization; Telemetry Ingestion and Data Quality; Energy Graph; Tariff and Settlement; Cost Analysis and Evidence Replay; Deployment/Operability/Recovery.
- MVP: VS-001 and VS-003; implementation task packets must identify the selected physical transaction boundaries and exact migrations.
- Review status: architecture draft for product owner, architecture, data and security review. No technology selected, requirement accepted, Gate closed, customer data authorized or runtime behavior verified.
