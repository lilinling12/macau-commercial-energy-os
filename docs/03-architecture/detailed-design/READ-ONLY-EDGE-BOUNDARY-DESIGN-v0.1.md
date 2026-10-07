# G7.9 Step 3 T5 — Read-only Edge Boundary Design v0.1

**Status:** Review proposal; not an approved protocol profile, deployment topology, security design, or site integration.  
**Date:** 2026-10-05  
**Purpose:** Define the data and trust boundary needed for read-only source/load assessment without presuming field protocols or equipment capability.

## 1. Evidence baseline

The current main branch has an Edge Runtime README describing protocol adapters, point normalization, local buffering, retry/reconnect, secure telemetry transport, and local health/audit signals. It says Go is the runtime direction and excludes tariff truth, optimization policy, and safety execution. The checked-in `cmd/edge/main.go` only emits a JSON startup log with `mode=bootstrap`; `go.mod` declares the module and Go version. This is bootstrap evidence, not evidence of protocol adapters, buffering, authenticated transport, field mapping, or a read-only deployment profile.

| Main source | Revision evidence | Directly observed |
|---|---|---|
| `implementation/edge-runtime/README.md` | blob `7ec8850b88529569ea81667382af6401c1b8436d` | States intended initial responsibilities and Go runtime direction. |
| `implementation/edge-runtime/cmd/edge/main.go` | blob `ee671a01e41f9325658bb2a98243936bc31825f4` | Startup logger only; no listener, protocol, credentials, queue or command path. |
| `implementation/edge-runtime/go.mod` | blob `f2869eb831a7380015e5a3d1bee1e1d5d290b805` | Declares the Go module/runtime version; no dependency or protocol decision. |

## 2. MVP boundary

The Edge is a site data-plane adapter for approved, read-only measurements. It normalizes and forwards observations; it does not choose tariff interpretation, optimize schedules, decide legal/account applicability, or write to devices. The platform computes source/load scenarios and presents SHADOW review. Any future control capability requires a separately authorized safety architecture and Gate.

For an MVP read-only profile, explicitly exclude:

- device-write credentials, actuator APIs, setpoint writes, command queues/topics, remote-control RPCs and cloud-triggered control configuration;
- tariff, contract, PV compensation, savings or demand-charge conclusions at the Edge;
- inferred asset/point mappings, invented quality values or substitution of a stale measurement with a recent value;
- selecting MQTT, HTTPS, Modbus, BACnet, a vendor protocol, broker, certificate authority, or deployment topology before site and security evidence support it.

The existing Go runtime direction can be retained for evaluation. Language does not prove that the above boundary is enforced.

## 3. Identity, mapping and trust

1. Provision a unique Edge instance identity through an approved enrollment process. Bind that identity to tenant, organization and authorized site in a trusted registry. Tenant/site values received inside telemetry are selectors/data and cannot grant access.
2. Authenticate the Edge to the platform using a per-instance credential held and rotated under an approved secret/key lifecycle. The exact mechanism (for example, mutual TLS) is a security decision, not selected by this document.
3. Resolve each source point through a versioned mapping: source identity, canonical point/asset identity, measurement kind, unit, aggregation, physical boundary, quality policy, and effective interval. Preserve the mapping revision with every forwarded observation or batch.
4. Reject or quarantine unmapped, multiply mapped, unauthorized, unit-incompatible, or out-of-validity points. Do not label them as validated physical inputs. Keep diagnostics auditable without leaking secrets or unrelated tenant data.
5. Downstream evidence readiness remains claim-specific. An untrusted or stale reading cannot qualify a schedule interval; independent measurements may be retained if their provenance and affected scope are explicit.

## 4. Observation envelope requirements (semantic, not wire schema)

Before choosing a schema format, define a reading with these meanings:

- stable observation/source-point identity and source sequence where available;
- canonical quantity and unit, sign convention, and instantaneous versus interval-average/aggregate semantics;
- interval start/end as half-open instants when the source is interval-valued; retain source timezone/offset representation and the site's IANA timezone as separate context;
- source-measured time, Edge-received time, and platform-received time as distinct provenance; never replace the source time with ingestion time;
- quality/freshness/clock-confidence classification, mapping revision, device/adapter version and batch identity;
- tenant/site authorization derived from enrolled identity and mapping, not trusted from payload claims.

Use UTC instants for cross-system ordering and preserve original source timestamps. A timezone conversion does not make an ambiguous or low-confidence source clock valid. Tariff and settlement windows are interpreted by the separately governed site/account rule, not by Edge defaults.

## 5. Buffering and delivery behavior

Store-and-forward is an intended responsibility in the main README, but no implementation or delivery guarantee is currently evidenced. The following behavior is proposed for review:

- Locally queue accepted observations with stable batch/sequence identity and integrity metadata. Define data-at-rest protection, retention, disk quota and secret storage in the threat model before field deployment.
- Prefer at-least-once forwarding with idempotent downstream deduplication; do not claim exactly-once delivery across a network partition.
- Retain source and receive timestamps, preserve per-source ordering where available, and mark gaps, duplicates and late arrivals. Out-of-order data may be stored as late evidence but must not silently rewrite a previously pinned assessment.
- On disconnect, queue within the approved capacity and expose oldest-item age, depth and last successful send. On capacity exhaustion, follow a reviewed, explicit backpressure/eviction policy and emit a durable loss/gap marker; never silently discard while reporting healthy/current data.
- On reconnect, use bounded concurrency and rate limiting so replay bursts do not overwhelm the site device or platform. Rotate credentials without discarding queued observations; reject expired credentials and alert.
- Every assessment pins the accepted input snapshot/version. Later arrivals create a new assessment or explicit replay difference; they do not mutate an earlier result.

Exact queue capacity, retention duration, retry schedule, freshness thresholds, resource limits and encryption/key requirements are unknown pending site workload, threat and legal-retention review.

## 6. Failure and acceptance matrix

These are required simulation cases before a read-only Edge slice can be accepted. They are not test results.

| Scenario | Required behavior | Evidence to retain |
|---|---|---|
| Network partition and restart | Queue survives the declared restart model; resume forwarding without converting offline time to source time. | Batch IDs, sequence/gap markers, restart and delivery trace. |
| Duplicate delivery/retry | Deduplicate by stable source identity while recording duplicate counts; never double-count energy. | Original and duplicate references, one accepted logical reading. |
| Out-of-order/late data | Preserve source times and mark late; do not silently rewrite pinned inputs or present chronology as complete. | Arrival order, source order, late/gap status. |
| Clock drift or invalid timestamp | Retain raw timestamp and receive time; downgrade/block affected time-sensitive claims under an approved tolerance. | Offset estimate, quality status, affected intervals and threshold revision. |
| Unmapped/conflicting/expired point mapping | Quarantine the point and expose a mapping-resolution issue; no fallback guessed meter/site association. | Source point, mapping revision/validity and withheld scope. |
| Invalid unit/sign/aggregation | Reject or quarantine before canonicalization; do not infer kW vs kWh or import vs export sign. | Validation reason and source payload reference with sensitive fields protected. |
| Queue full / disk unavailable | Emit explicit degraded/loss state and gap evidence; stop claiming freshness. | Capacity status, first/last lost sequence and recovery action. |
| Reconnect burst | Bounded replay; device polling remains within approved load and the server is not flooded. | Rate-limit and queue-age telemetry. |
| Credential expiry, revocation or rotation | Fail closed for forwarding; surface health state; rotation preserves queued observations and site binding. | Identity lifecycle and auth audit event without secret material. |
| Identity/site mismatch | Deny forwarding and alert; payload tenant/site cannot override enrollment. | Authenticated identity, attempted selector, denial and tenant-safe audit. |
| Any attempted control/write request | No write transport or credential exists in the MVP profile; request is unavailable/denied and audited. | Build/config inspection, negative integration test and audit record. |

The acceptance suite must distinguish source adapter tests, queue/reconnect tests, transport/auth tests, tenant-isolation tests and end-to-end snapshot/readiness tests. A passing Go build alone is insufficient.

## 7. Operational health and observability

Expose per-instance health for identity state, adapter connectivity, last source sample, last platform delivery, queue depth/oldest age, dropped/gap counts, duplicate/late counts, clock confidence, mapping rejects, credential expiry horizon and software/config revision. Apply tenant/site authorization to health details. Never include credentials or unrestricted raw building/occupant data in routine logs.

Do not choose SLO thresholds until the pilot's measurement cadence, tolerated outage, local storage limits, tariff intervals and operator response expectations are known. Preserve privacy, retention and data-residency requirements as explicit unresolved decisions.

## 8. Decisions still open

- Site device/protocol inventory and read-only access authorization.
- Canonical point/asset mapping ownership, evidence source and effective-date process.
- Enrollment/identity authority, certificate/key lifecycle, platform trust roots and revocation behavior.
- Message/transport protocol, broker (including whether MQTT/NATS is needed), envelope and compatibility policy.
- Store-and-forward durability, encryption, retention, disk capacity, retry/rate limits and freshness/clock tolerances.
- Edge-to-platform tenancy/site enforcement and immutable input snapshot integration.
- Pilot cybersecurity, privacy/legal basis, threat model, deployment/upgrade/rollback and support ownership.

Do not resolve these from the current `main.go`, a language choice, or the existence of NATS/MQTT in a candidate stack.

## 9. Source-to-Gate trace and next proof

This proposal responds to G7.9 Step 2 `TELEMETRY_CONTRACT.md`, `MULTI_TENANT_STRATEGY.md`, `MIGRATION_STRATEGY.md` and the Step 3 required Edge boundary output. It aligns with the repository's read-only telemetry and no cloud/device safety-write boundary. Exact source package contents and the G7.9 task sequence should be linked from the PR review record.

Next T5 evidence: security/domain review of identity and mapping authority; one synthetic simulator covering disconnect, duplicate, stale/out-of-order, clock drift, reconnect burst, queue exhaustion, unit mismatch and unauthorized site; a build/configuration check proving no write capability; and an explicit decision list for the pilot protocol and retention. No actual site connection is authorized or evidenced by this document.

**Gate status:** T5 design proposal only. This does not prove the Edge boundary is implemented, close G7.9 Step 3, approve the production stack, or authorize equipment control.
