# Deployment, Operability and Recovery — Detailed Design v0.1

**Status:** Stack-neutral review draft; deployment mode, SLOs, cloud provider and production topology are not selected.  
**Scope:** PR-01/PR-07/PR-09 operating boundary; G6-08/G6-09/G6-10 and roadmap WP-5/WP-7 readiness.  
**Authority:** G6.8 enterprise deployment and safety boundaries; G6 safety-control gate; D-008/D-070/D-073–D-075; PR-01/PR-07/PR-09; logical architecture and current handoff.

## 1. Purpose and boundary

Define the production questions and invariants needed to operate Macau Commercial Energy OS safely across cloud services and customer sites. This design separates:

- **Cloud product plane:** identity, tenant/site administration, telemetry ingestion, Energy Graph, tariff/economic evaluation, forecasts, optimization, recommendations and evidence/replay.
- **Site Edge plane:** protocol adapters, local telemetry buffering, site identity, local safety/policy enforcement, command arbitration and device-facing operation only after G6 and site authorization.
- **Operator/support plane:** dependency health, alerts, audit access, runbooks, incident response, release/rollback and evidence-preserving recovery.

Logical responsibilities do not imply that each component is a separate service. Module/process placement follows validated domain, scaling, security and failure boundaries after G6.9-R2 and deployment decisions. Shadow mode remains the current operating boundary; the MVP does not enable device writes.

## 2. Deployment-mode decision framework

Shared, Dedicated and Private are product/operations options, not selected architectures. Compare them against:

| Dimension | Questions and required evidence |
|---|---|
| Tenant isolation | What identities, authorization checks, data partitions, caches, jobs, queues, keys and evidence references are isolated? Which controls are logical vs infrastructure-enforced? |
| Customer requirements | What data-residency, network-connectivity, procurement, security-review, vendor-access, retention and deletion requirements apply? |
| Operational ownership | Who patches, monitors, backs up, restores, rotates credentials, responds to incidents and approves upgrades? |
| Failure isolation | Can one tenant or site overload, corrupt, expose or delay another tenant's workload? What rate/resource boundaries are enforceable? |
| Upgrade and support | How are versions, migrations, compatibility, rollback, emergency fixes and end-of-support handled across tenant deployments? |
| Cost and service level | What are the measured infrastructure/support costs and customer-approved availability/recovery objectives? No SLA is inferred from this draft. |

Each proposed mode must document a threat model and isolation evidence before a customer contract or deployment baseline is approved. Do not assume separate infrastructure automatically proves tenant isolation; do not assume shared infrastructure is acceptable without explicit customer and security evidence.

## 3. Trust boundaries and identity

- Derive interactive user scope from authenticated identity and approved organization/site memberships. Ignore client-supplied tenant/site IDs as authority.
- Bind service identities, event producers, scheduled workflows, caches, object storage, database access and support tooling to least-privilege tenant/site scope.
- Bind Edge device identity to an authorized site and credential lifecycle. Cloud messages are authenticated, scoped, versioned, expiring and replay-protected before any future command path.
- Separate operational observability metadata from business/control identity; trace IDs cannot affect deterministic proposals, tariff results, command idempotency or evidence identity (D-073).
- Protect secrets with an approved secret/key service and explicit provisioning, rotation, revocation, recovery and compromise process. Product framework and crypto choices remain open under G6/G6.9-R2.
- Log access to sensitive evidence and administrative changes. Redact credentials, personal information and unnecessary site/network detail from routine telemetry and logs.
- Review vendor/support access, break-glass access, approval, expiry, session recording/audit, and customer notification requirements before selecting a deployment mode.

## 4. Availability, health and observability

### 4.1 Health semantics

Expose separate process liveness and dependency readiness. A process being alive is not evidence that authenticated APIs, queues, databases, evidence storage, model workers or site connectors can serve their required function. Readiness reports dependency and degraded capability state without exposing secrets or cross-tenant data.

For each site/source and product workflow, surface last observed time, last received time, freshness policy, quality/coverage, backlog/lag, mapping status and downstream impact. Do not collapse partial or stale sources into a green portfolio badge. Health projection is operator context; it must not rewrite evidence status or tariff truth.

### 4.2 Observability signals

Define SLIs and dashboards before setting SLO targets:

- API request availability/latency/error by operation and tenant-safe aggregate;
- telemetry accepted/rejected counts, freshness lag, quality, backlog and recovery delay;
- workflow scheduled/start/completion/timeout/retry/duplicate/replay outcomes;
- forecast/optimization readiness, run duration, feasibility, solver gap and blocked reasons;
- tariff/economic assessment completeness, replay reproducibility and evidence persistence failure;
- Edge connectivity, buffer pressure, clock drift and synchronization state;
- security events, access denials, key lifecycle, policy vetoes and administrative changes.

Metrics and traces support operations but are not the replay record. Do not put raw bills, secrets, identifiers or high-cardinality customer payloads in metric labels. Define tenant-safe incident visibility and access controls.

### 4.3 SLO and alert policy

Availability, latency, ingestion freshness, recovery, support coverage, retention, RPO and RTO remain product/customer decisions. Derive targets from validated workflows, contracts, operational capability and measured candidate runtime behavior. For each proposed SLO specify measurement scope, window, exclusions, data source, alert threshold, owner, error-budget action and customer communication. Averages must not hide one site's safety/evidence degradation.

### 4.4 Proposed SLI measurement contract (thresholds intentionally open)

The following catalog makes measurement boundaries reviewable without inventing availability, latency, freshness, recovery or support targets. It is a logical measurement proposal, not a production telemetry schema or SLO approval.

| Concern | Proposed indicator and measurement boundary | Required segmentation / interpretation | Target status |
|---|---|---|---|
| API service health | Eligible authorized request success and latency from service ingress to response; count authorization denials and validation errors separately from service failures. | Operation and deployment; tenant-safe aggregate. Do not expose tenant IDs in high-cardinality labels. | Threshold, window and exclusions require workflow/customer evidence. |
| Telemetry arrival | (a) source-observed-to-platform-received lag only where source clock quality is known; (b) platform-received-to-durable-raw-acceptance duration; (c) age of oldest unprocessed durable event. | Site/source/connector and quality state. Never merge source-clock uncertainty with platform processing delay. | Freshness policy and bounds require source cadence and product task evidence. |
| Workflow service | Accepted trigger to terminal workflow outcome, with scheduled-to-start delay, retries, timeout, duplicate/replay outcome and blocked reason reported separately. | Workflow type, result status and site-safe scope. Blocked/incomplete is not success. | End-to-end target depends on the validated user task and failure budget. |
| Economic assessment | Coverage/completeness and outcome-state distribution for reconstruction, interval assessment and baseline comparison; separately record provenance gaps and unresolved-rule blocks. | Result kind, tariff scope and evidence version. Availability does not prove bill correctness. | Golden Bill accuracy and zero-unexplained-adjustment remain G1 acceptance, not an uptime SLO. |
| Replay/evidence | Durable evidence write/read availability; replay outcome and semantic digest equality for an identical pinned input/version set; record mismatch as a correctness incident. | Assessment version and tenant-safe scope. Correlation IDs are excluded from semantic identity (D-073). | Determinism is a correctness invariant; durability/restore targets require owner-approved retention and RPO/RTO. |
| Site Edge | Last authenticated heartbeat age, buffer occupancy/oldest buffered age, clock synchronization status, and cloud-link availability; measure policy veto and rejected-command reasons separately if G6 later authorizes command paths. | Per site with fail-closed local status; do not average away one site's loss of safety/evidence capability. | Thresholds depend on site operations, buffer policy and G6 evidence; no command SLO is approved. |
| Identity/security | Authorization-denial counts, credential/key lifecycle events, revocation propagation time and tenant-isolation verification outcomes. | Role, boundary and deployment mode with restricted security access. | Baseline and response targets require security-owner review and G6-08/G6-09 evidence. |
| Backup/recovery | Point of recoverable data and elapsed restoration-to-validated-service, measured per data class and failure scenario. | Raw telemetry, tariff/contract versions, graph versions, assessment/evidence, workflow and audit records; preserve separate RPO/RTO evidence. | RPO/RTO values require customer, legal-retention, operational and deployment decisions. |

For every SLI selected for the pilot, record its owner, clock source, numerator/denominator or aggregation rule, evaluation window, excluded states, data source, tenant/site segmentation, alert/runbook, customer-visible consequence and validation artifact before setting an SLO. The same metric name must not silently change meaning between candidate stacks. Numeric targets remain unapproved until the product workflow, site operating boundary, deployment mode and support ownership are reviewed.

## 5. Failure domains and degradation

| Failure | Required behavior to design and validate |
|---|---|
| Cloud API or dependency unavailable | Show capability-specific degraded/unavailable state; do not return a stale result as current |
| Broker/database/object storage unavailable | Bound queues and retries; preserve source/evidence identity; expose backlog and recovery progress |
| Site network/cloud connection lost | Edge behavior is governed by site-local G6 policy; buffer permitted telemetry; reject stale/unauthorized cloud commands |
| Forecast/optimizer worker stalled | Mark runs delayed/blocked; avoid treating prior output as a current recommendation |
| Partial regional/provider outage | Scope impact, prevent cross-tenant leakage and avoid unsafe automated retries |
| Clock drift or boundary-policy mismatch | Quarantine or block affected calculation/control use; expose time-health diagnostic |
| Recovery after partial write/workflow crash | Reconcile idempotently; Edge replay protection prevents duplicate physical writes (D-075); record outcome separately |
| Evidence store unavailable | Do not claim durable audit/replay; queue only under an explicit durability policy or block material workflows |

Every failure behavior requires an owner, observable signal, runbook, recovery condition and evidence of safe return to service. Shadow-only behavior must not silently become control behavior during degraded operation.

## 6. Data durability, backup and restore

For each persisted class—raw/normalized telemetry, Energy Graph versions, tariff/contract rules, forecasts, optimization runs, recommendations, review events, evidence/replay manifests, user/access audit and Edge state—decide:

- authoritative source and retention period;
- mutability/correction/deletion and legal-hold semantics;
- backup scope, encryption, frequency and cross-region/site placement;
- recovery ordering and dependencies;
- acceptable RPO/RTO by product operation;
- restoration validation and evidence/replay continuity;
- customer export and verified deletion behavior.

Restore tests must cover tenant/site scope, effective-dated history, immutable evidence references, schema compatibility, message offsets/replay positions and Edge reconciliation. A backup job reporting success is not proof of recoverability. Do not silently substitute latest mappings, tariff versions, model artifacts or telemetry during replay.

### 6.1 Proposed data-class lifecycle matrix (retention horizons open)

This matrix defines behaviors that the selected storage/deployment design must support; it sets no retention duration and does not decide legal holds, customer rights or evidence retention. Those inputs require the dataset-specific governance review in the Security Threat Model §6B and the applicable customer/site agreement.

| Data class | Lifecycle and replay requirement | Deletion/correction behavior to design | Horizon / authority |
|---|---|---|---|
| Raw source payloads and source documents | Preserve provenance and the exact accepted original only for an approved purpose; distinguish raw evidence from normalized output. | Corrections append a superseding version. On an authorized deletion, remove or restrict the payload and dependent copies; any retained tombstone/receipt metadata must be minimized and lawful. | Customer contract, legal/privacy review and evidence purpose; duration open. |
| Normalized telemetry and derived features | Retain source-event lineage, transformation versions and quality/mapping state while needed for approved assessment or operations. | Delete/recompute derived features when source deletion or correction requires it; prevent deleted source content from reappearing through replay or materialized views. | Pilot workflow, site source rights and privacy review; duration open. |
| Site graph, mappings and contracts | Preserve effective/system-time history needed to explain authorized past results while the underlying records may lawfully be retained. | Corrections create new versions; deletion/restriction must update references and make affected results unavailable or appropriately redacted instead of silently substituting current records. | Customer/site agreement, legal hold and G1/G3 evidence; duration open. |
| Tariff rules and public source evidence | Retain public/version provenance needed to reproduce published calculations; separate it from private customer contract data. | Public source history may remain under its own use basis; customer-specific annotations/attachments follow the customer data deletion policy. | Source licence, applicable authority and separate customer-data policy; duration open. |
| Assessments, recommendations and replay manifests | Preserve immutable input/version references for authorized reproducibility; do not claim a replay remains complete after required evidence is removed. | Authorized deletion can require deleting/redacting result payloads and invalidating dependent replay; retain only the minimum lawful audit record, with explicit status explaining that replay is unavailable. | Owner-approved evidence purpose, customer agreement and legal review; duration open. |
| Identity, access, security and support audit | Preserve actor/scope/action evidence required for security, accountability and incident handling; minimize direct identifiers in routine metrics/logs. | Separate security/audit record policy from customer energy-data retention; support deletion/subject-right requests through an approved, auditable process. | Security/legal owner and customer requirements; duration open. |
| AI prompts, retrieved context, outputs and provider traces | Prefer not to persist source payloads in model traces; record only approved references and necessary provenance. | Propagate source deletion to prompts, caches, vector indexes, evaluation sets and provider retention paths where applicable; verify provider behavior before use. | Explicit provider terms, model settings, customer authority and privacy/legal review; duration open. |
| Backups, exports, replicas and disaster-recovery copies | Backups must support approved restore/replay objectives and have a bounded, documented expiry policy. | Deletion/restriction must survive restore: reconcile a deletion ledger/tombstone or equivalent before restored data becomes available; verify expiry across replicas, exports and support copies. | Approved retention schedule and tested RPO/RTO; duration open. |

Before production design freeze, define a data-class registry that binds each class to owner, purpose, source, tenant scope, location/processor path, retention event/clock, legal hold, deletion SLA, backup expiry, replay consequence and verification evidence. Do not use one global retention period for materially different data classes or claim erasure until restored and replicated copies are covered.

### 6.2 Target-free restore and recovery scenario catalog

Use these scenarios to select deployment/storage boundaries and to plan recovery verification. They define integrity outcomes, not numeric RPO/RTO targets or a claim that any scenario has already passed.

| Scenario | Required recovery invariant | Evidence to retain |
|---|---|---|
| Primary database/object store loss with point-in-time restore | All records acknowledged as durable meet the owner-approved recovery point; tenant/site scope, effective-dated versions, audit/evidence references and deletion restrictions remain consistent. | Recovery point, restore timeline, row/object consistency results, affected/inaccessible records, replay sample and owner decision against approved RPO/RTO. |
| Broker/worker state diverges from business persistence | Reconcile outbox/inbox or equivalent offsets against durable business state; retries cannot duplicate evidence, assessment or physical field effects. | Broker offsets, workflow histories, idempotency/replay outcomes, duplicate-effect count and reconciliation record; any field effect remains gated by G6/site authorization. |
| Raw capture succeeds but normalization/publication partially fails | Reprocess from the preserved raw reference using pinned contract/adapter/policy versions; never acknowledge an event as fully available while its durability state is ambiguous. | Raw receipt, transformation versions, retry attempts, terminal status and downstream availability boundary. |
| Correction/deletion occurs before backup restore | Apply the current authorized correction/deletion state before restored data becomes accessible; stale copies are not exposed by replay, search, cache, export or AI traces. | Deletion/correction ledger reconciliation across primary, replicas, backup, index, cache and export paths, plus verification of replay status after removal. |
| Single-tenant/site export or restore | Restore/export only the approved tenant/site scope, preserve provenance and prevent cross-scope records or references from becoming visible. | Scope manifest, authorization principal, included/excluded record counts, reference-integrity check and negative isolation evidence. |
| Edge reconnects after a prolonged disconnection/restart | Reconcile locally buffered telemetry without unsafe deduplication; preserve source identity, event time, ordering uncertainty and clock status. Any future command state is reconciled without repeating a physical write. | Edge buffer bounds/age, sequence/cursor state, accepted/quarantined records, duplicate classification, command replay state and site operator confirmation. |
| Failed schema/contract/Edge rollout and rollback | Restore a compatible release set without silently rewriting historical contracts/results, losing audit evidence or breaking tenant isolation; use forward-fix when rollback would corrupt state. | Release manifest, migration state, compatibility results, rollback/forward-fix procedure, data integrity checks and user-visible degraded/recovery status. |

For each scenario, record the measured recovery point and elapsed recovery time separately from the target, then obtain product/operations/customer approval for the target and residual loss window. A successful backup command, green health check or synthetic replay is not acceptance evidence by itself; execute the scenario in an environment representative of the approved deployment and retain raw recovery artifacts.

## 7. Release, migration and rollback

- Version service artifacts, API/event contracts, model/solver artifacts, tariff rule packages and site Edge software independently but record compatible release sets.
- Use explicit compatibility policy and staged rollout rings; shadow-only capability flags remain the default for unapproved functions.
- Database/schema changes use reviewed migrations with preflight checks, backup/restore implications, expand/contract where compatible, and tenant/site-scoped validation.
- Deployments preserve an immutable release manifest: artifact digests, configuration versions, migration versions, feature flags, model/solver/rule versions and rollout scope.
- Define rollback/forward-fix strategy for code, schema, contract and Edge agent changes. A rollback must not erase audit/evidence or make a command retry non-idempotent.
- Roll out to synthetic/reference environments before customer sites; require site authorization, maintenance window, operator notification, health watch, abort thresholds and recovery owner for field-connected changes.
- Verify rollback by observing product behavior and data/evidence integrity, not solely by deployment tool status.

No CI/CD tool, cloud provider, container topology or release schedule is selected by this draft.

## 8. Incident, support and operational ownership

Before pilot, define on-call/service ownership for cloud, tenant administration, tariff/evidence correctness, site integration, Edge/security, optimizer/model quality and customer communication. Runbooks must cover stale data, incorrect mapping/rule, evidence/replay failure, tenant access incident, key compromise, Edge offline, command veto/replay, failed upgrade, backup restore and suspected safety event.

Incident records preserve timeline, affected tenant/site scope, evidence references, operational decisions, customer notification, recovery proof and follow-up Decision/Open Question updates. A support operator must not have broader data/command authority than their approved role.

## 9. Acceptance evidence and open decisions

This area is not accepted until:

- owner selects a deployment mode after segment/customer/security/operations evidence;
- tenant/site isolation and privileged support access pass positive and negative verification across APIs, storage, jobs, caches, events, evidence and Edge identity;
- health/readiness semantics correctly expose dependency and site-source degradation;
- SLI/SLO, alert ownership, incident and support procedures are approved for the pilot scope;
- backup/restore and evidence replay survive realistic failure injection at the approved RPO/RTO;
- migrations, staged rollout and rollback preserve tenant data, audit/evidence and Edge idempotency;
- cloud outage, broker partition, worker restart, clock issue and post-upgrade recovery have runbooks and tested evidence;
- product/operations owner approves residual risk and G6-08/G6-09/G6-10 closure evidence for the declared deployment scope.

Still open: Shared/Dedicated/Private choice, data residency, provider, isolation implementation, availability objectives, RPO/RTO, retention/deletion, incident coverage, support access, upgrade cadence, Edge fleet lifecycle and customer pilot operating agreement. This draft asserts no production readiness or G6 closure.

## 10. References

- docs/03-architecture/ARCHITECTURE-DESIGN.md
- docs/03-architecture/detailed-design/VS-001-IDENTITY-AND-TENANT-AUTHORIZATION-DESIGN-v0.1.md
- docs/03-architecture/detailed-design/TELEMETRY-INGESTION-AND-DATA-QUALITY-DETAILED-DESIGN-v0.1.md
- docs/03-architecture/detailed-design/COST-ANALYSIS-AND-EVIDENCE-REPLAY-DETAILED-DESIGN-v0.1.md
- docs/01-research/gates/G6-safety-control.md
- docs/00-authority/decisions/DECISIONS.md and OPEN-QUESTIONS.md
- docs/00-authority/ROADMAP.md
