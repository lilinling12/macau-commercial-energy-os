# Security Threat Model v0.1 — Macau Commercial Energy OS

**Status:** Stack-neutral threat-model draft for owner/security review. No security approval, G6 closure, production-readiness finding, penetration-test result or field-control authorization is implied.
**Prepared:** 2026-10-04
**Scope:** Product architecture and proposed SHADOW MVP, including browser/API, tenant/site authorization, ingestion, asynchronous processing, economic results, AI/optimization inputs, evidence/replay and site Edge boundary.
**Method:** STRIDE threat elicitation across repository-defined trust boundaries; risks are ordered by consequence and architectural importance, not by a completed likelihood score.
**Authority:** Logical Architecture Design, VS-001 detailed design, Identity/Tenant Authorization, Telemetry Ingestion/Data Quality, Deployment/Operability/Recovery, G6 Safety & Control, current PRD and Gate status.

## 1. Security objectives and boundaries

Protect customer/site confidentiality; preserve integrity and provenance of telemetry, tariffs, contracts, calculations and audit evidence; make every action attributable and authorized; prevent shared-resource abuse from degrading another tenant; and ensure cloud analytics cannot cross the site-local safety authority.

The MVP is SHADOW/advisory. It has no device-write authorization. The future Edge command route is included only to preserve the architecture boundary and threat coverage; command execution remains disabled until separate G6/G7 evidence and explicit site/customer authorization.

### Trust boundaries

| Boundary | Data/actions crossing it | Assumed trust |
|---|---|---|
| End user/browser → cloud API | Session/token, site selection, filters, mapping/configuration and review events | Client is untrusted. IDs, role labels and tenant/site values from the client are selectors, never authorization proof. |
| Tenant/site → shared cloud services | Telemetry, contracts, tariffs, results, jobs, caches, queues and evidence | Tenant-owned data and work must stay scoped across every synchronous and asynchronous path. Internal network location does not confer trust. |
| Connector/Edge → ingress | Machine identity, event payload, timestamps, quality and device/point references | Payload is untrusted until producer identity and registered site/device/point scope are verified. |
| Cloud worker ↔ broker/workflow/storage | Events, scheduled work, replay inputs, artifacts and service credentials | Authenticate workload identities; re-authorize tenant/site operation at consumption; do not trust message tenant fields by themselves. |
| Cloud ↔ site Edge | Telemetry, policy/configuration and any future command proposal | Separate identities and authority. Cloud may propose; only site-local policy/Safety Kernel can veto/authorize execution after G6. |
| Operator/support and recovery paths | Tenant administration, exports, logs, backups, restore, break-glass | Privileged path; least privilege, explicit scope, approval, audit and recovery-specific authorization are required. |
| AI/model or external evidence processing | Bills, contracts, tariff sources, telemetry summaries and generated recommendations | Inputs and generated text are untrusted data. They cannot change system authority, disclose other tenants, invoke tools/secrets, or create a command path. Exact model/provider/data boundary remains open. |

## 2. Assets and security objectives

- **Identity and authority:** user sessions, memberships, service identities, site scopes, connector identities, Edge/device keys, policy versions and revocation state.
- **Customer information:** organization/site topology, operational telemetry, meter/account relationships, building configuration, contracts, bills and tariff data.
- **Economic/evidence integrity:** raw and normalized measurements, source timestamps, unit/mapping versions, tariff/contract versions, calculation results, recommendations, review events, replay manifests, exports and audit history.
- **Operational integrity:** workflow/event state, idempotency identity, deployment artifacts/configuration, backup/restore, Edge buffer and future command acknowledgements.
- **Shared service availability:** API capacity, queues, worker concurrency, database/object storage, model/solver capacity and connector resources.

## 3. STRIDE threat register

| ID | Category / priority | Threat scenario and impact | Draft controls and required proof |
|---|---|---|---|
| TM-01 | Elevation of privilege / cross-tenant access — **critical boundary** | User or worker changes tenant/site/resource IDs, follows a foreign evidence link, reuses a cache entry, or invokes an internal endpoint to read/change another tenant's telemetry, contract, result or review. | Derive scope from verified identity and current membership; authorize each resource/action; carry scope into repositories, caches, jobs, events, object paths, exports and replay; fail closed. Prove a tenant authorization matrix through the actual request role, connection-pool reuse and all data paths. |
| TM-02 | Spoofing — **critical boundary** | Forged connector, service or Edge identity submits plausible telemetry or a future command proposal; body tenant/site fields appear consistent but producer is unauthorized. | Separate human, connector, workload and Edge identities; bind machine identities to registered site/device/point scopes; authenticate producers and authorize consumers; define credential issuance/rotation/revocation. U-022 and production key lifecycle remain open. |
| TM-03 | Tampering — **high** | Attacker or defective integration alters telemetry, timestamps, units, mappings, tariff/contract rules, result lineage or replay inputs; output appears verified despite changed or missing evidence. | Preserve raw source/provenance and valid/received times; version mappings/rules/contracts; immutable evidence lineage; strict contract/unit/time validation; correction creates new lineage; replay pins semantic inputs. Define canonicalization/digest and durable store before claiming tamper evidence or deterministic replay. |
| TM-04 | Information disclosure — **high** | Cross-tenant API, cache, search, logs, support tooling, exports, backup or restore reveals site identity, bills, tariffs, network details or evidence references. | Classify data; least-privileged access; tenant-scoped cache/storage/jobs; redact logs; explicitly authorize export/support/restore; retention/deletion across replicas and backups. Exact isolation topology, residency, retention and support policy remain open. |
| TM-05 | Repudiation / audit gaps — **high** | User or service denies changing mappings, accessing sensitive evidence, approving a future action, or operating a privileged recovery path; logs cannot connect actor, scope, policy and outcome. | Record authenticated actor/service, action, tenant/site scope, target, policy/version, outcome and correlation metadata while excluding secrets/raw payloads; protect audit from ordinary mutation; restrict and retain logs under an approved policy. Audit retention and immutable-storage mechanism remain open. |
| TM-06 | Denial of service / noisy neighbor — **high** | One tenant, connector, malformed producer or expensive replay/model request exhausts shared queue, worker, database, API or storage capacity and degrades other sites. | Bound payloads, rate, per-tenant queue/concurrency/storage/compute; isolate critical ingestion and security functions; backpressure and bounded retries; alert on per-tenant saturation without exposing tenant data. Targets and resource limits require measured deployment evidence and owner-approved SLOs. |
| TM-07 | Spoofing/tampering via external evidence and AI — **high** | Malicious or corrupted bill, contract, tariff page, vendor payload or prompt-like text is interpreted as an instruction or authoritative rule; AI produces an unsupported monetary claim or recommendation. | Treat imported material and model output as untrusted evidence; retain source/version; require explicit rules and eligibility checks outside generative text; make uncertainty and source visible; no model-controlled secrets, arbitrary tools, code execution or device action; require human review. Product model/provider and data handling boundary remain open. |
| TM-08 | Supply-chain tampering / vulnerable component — **high** | Compromised dependency, build action, generator, container image or plugin changes runtime behavior or leaks customer evidence. | Pin and verify dependencies/images/toolchains; produce build provenance/SBOM; review generators and release artifacts; vulnerability response and signed release process; isolate any future plugin/Wasm execution. Bake-off pinning, CI trust and release-signing decisions remain open. |
| TM-09 | Edge command spoofing/replay or unsafe degradation — **future high-consequence; disabled in MVP** | A stale, duplicated, forged, mis-scoped or replayed proposal reaches a device, or loss of cloud connectivity bypasses local policy. | Keep the route absent/disabled for MVP; future path requires scoped authenticated identity, expiry, sequence/idempotency, replay protection, local limits/veto, manual/offline fallback, audit and separate acknowledgement/physical-effect evidence. G6 remains OPEN; U-022 is unresolved. |

**Priority meaning:** “Critical boundary” identifies an invariant whose failure breaks tenant or identity separation; “high” identifies material confidentiality, integrity or availability risk. This is not a quantitative risk score. A formal likelihood/impact and risk-acceptance review needs product, customer, security and deployment context.

## 4. Required architecture invariants

1. Caller-supplied tenant/site IDs never grant access. Resolve authenticated principal and active membership/service authorization before loading tenant-owned resources.
2. Every API, domain port, repository, event consumer, scheduled job, cache, object/evidence reference, export, support and restore path enforces an explicit scope. Internal service calls are authenticated and authorized.
3. Missing, malformed, expired, revoked or ambiguous identity/scope fails closed; no empty-scope fallback and no cross-tenant retry.
4. Producer identity is checked independently of event payload fields; mapping, metric, unit, quality and time policy are versioned and traceable.
5. A published economic result identifies its evidence and rule lineage and cannot be labeled verified solely because computation succeeded.
6. Generated AI/model text is not an authority source and cannot grant permission, change tariff policy, suppress an unresolved state, access secrets, or reach the Edge command path.
7. Privileged human/service actions, denials and data access produce access-controlled audit evidence without putting credentials, raw bills or unnecessary sensitive site detail in general logs.
8. Shared-service limits are tenant-aware; retry and replay behavior is bounded and cannot create duplicate economic records or future physical writes.
9. Cloud outage never relaxes site-local safety. MVP has no device-write capability; future control requires independent G6/G7 authorization and Edge validation.
10. Security controls are verified using the same role, identity, pool, job and deployment paths used in production; privileged test credentials cannot mask missing tenant enforcement.

## 5. Verification scenarios to become acceptance evidence

### SHADOW MVP

- Tenant A cannot list, read, mutate or infer Tenant B's sites, points, mappings, tariffs, contracts, calculations, recommendations, evidence, exports or audit records by changing IDs or following references.
- A Tenant A request body that names Tenant B is rejected before graph, tariff, optimizer, storage or cache ports are called.
- A producer authorized for one site cannot submit a different tenant/site/device/point; forged, expired and revoked credentials are rejected; denial is attributable without logging credentials.
- Two tenant requests over reused pooled connections, concurrent jobs, shared queues, caches and evidence links cannot inherit each other's scope.
- Unauthorized export, support access and tenant-scoped backup restore are rejected and audited. A two-tenant restore can recover the selected tenant without exposing the other.
- Invalid units, timestamps, mappings, source identities or contract versions cannot become authoritative economic output. A corrected input creates new lineage; old results remain explainable.
- A malicious evidence document or prompt-like data cannot change system instructions, request secrets, call tools, bypass evidence eligibility or produce an executable recommendation.
- Per-tenant rate/queue/worker/storage limits prevent an abusive tenant from consuming unbounded shared resources; degraded health is visible and recovery is bounded.
- Logs and metrics contain enough security context for incident response without raw bills, credentials, personal data or unnecessary high-cardinality site payloads.
- Build/release records identify source revision, dependencies, generated bindings and container artifacts; unapproved plugin execution is absent.

### Future controlled operation — separate G6/G7 gate

- A forged, expired, duplicated, wrong-site or replayed command is denied at Edge; cloud API, optimizer and support identities cannot bypass the local Safety Kernel.
- Cloud/broker loss, clock anomaly, Edge restart and recovery preserve local limits/manual override and do not replay a physical action unintentionally.
- Command request, approval, acknowledgement and measured physical effect are distinct, scoped and audit-linked.
- Site owner/operator authorizes the exact assets, operating envelope, schedule, stop condition and recovery plan before field use.

These are acceptance scenarios to implement and execute later. This document records no test results.

## 6. Decisions and evidence still required

- Validate user types, organization/site membership lifecycle, delegated connector access, approval responsibilities and denial/404 disclosure behavior.
- Select deployment and data-isolation model from customer/security evidence; decide whether database row-level security is appropriate. If PostgreSQL RLS is used, verify least-privileged deployed request roles, transaction-local tenant context, classified table coverage and connection reuse; do not assume RLS exists before a database decision.
- Approve data classification, data residency, retention/deletion, backup/export and incident evidence policy for bills, telemetry, contracts, topology, model inputs and logs.
- Define identity provider/session policy, workload identity, secret/key storage, rotation/revocation, emergency access, audit retention and support access. Edge signing/key lifecycle remains U-022.
- Set per-tenant quotas, queue/worker limits, availability/freshness SLOs, alert owners and recovery targets from the approved deployment mode and pilot workflow.
- Decide whether and which external AI/model service processes customer data, what data may leave the tenant/site boundary, and what human validation is required.
- Complete a product- and deployment-specific threat workshop, likelihood/impact scoring and named risk owners; this draft is not the final risk acceptance.
- Map applicable controls to an owner-approved security verification baseline. OWASP ASVS 5.0.0 is a candidate web/API control catalog, not yet a project-approved conformance target.

## 7. Traceability and status

- PRD: PR-01 site/tenant scope; PR-02 provenance; PR-07 evidence; PR-08 authority/review; PR-09 integration health.
- Architecture: Logical Architecture Design trust boundaries; Identity/Tenant Authorization; Telemetry Ingestion/Data Quality; Deployment/Operability/Recovery; G6 Safety & Control.
- Gates: G6-05 Edge identity/key lifecycle and G6-09 tenant/site isolation remain open; G1/G3/G7 evidence remains necessary for the economic and pilot claims that depend on it.
- Implementation status: existing scaffold findings are in PRD-ARCHITECTURE-TRACEABILITY. No executable threat controls are implied by this model.

## References

- Microsoft Threat Modeling Tool — STRIDE categories: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
- OWASP Application Security Verification Standard (ASVS): https://owasp.org/projects/asvs
- OWASP Multi Tenant Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html
- NIST SP 800-218 Secure Software Development Framework: https://csrc.nist.gov/pubs/sp/800/218/final
- Project identity and tenant design: docs/03-architecture/detailed-design/VS-001-IDENTITY-AND-TENANT-AUTHORIZATION-DESIGN-v0.1.md
- Project deployment and recovery design: docs/03-architecture/detailed-design/DEPLOYMENT-OPERABILITY-AND-RECOVERY-DETAILED-DESIGN-v0.1.md
- Project G6 authority: docs/01-research/gates/G6-safety-control.md
