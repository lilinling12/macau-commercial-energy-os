# MVP Application and Event Contract Catalog v0.1

**Status:** Logical contract catalog proposal; product owner and architecture review required.  
**Scope:** Application and asynchronous boundaries for the research-derived SHADOW MVP workflows, mapped to PR-01…PR-09 and VS-001…VS-008.  
**Authority:** D-065 governs cross-language contract ownership/versioning; product requirements, user roles and workflows remain hypotheses pending WP-4; G1/G3/G6/G6.9-R2 dependencies remain open.  
**Production status:** This catalog defines capability and state semantics only. It selects no API protocol, endpoint, message broker, schema format, authentication provider, generated binding or production runtime.

## 1. Purpose

Existing project artifacts define most capability-level behavior, but no single catalog links the user's product tasks to application operations and asynchronous state transitions. This design makes those logical boundaries reviewable before a wire format or framework is selected.

It complements, and does not replace:

- VS-001 Detailed Design for component responsibilities and processing;
- VS-001 Cost Result and Replay Manifest proposal for cost-result and replay-manifest shapes;
- Telemetry Ingestion and Data Quality Detailed Design for telemetry receipt/publication/consumer states;
- Identity and Tenant Authorization Design for principal/action/resource enforcement;
- Data Persistence and Schema Evolution Detailed Design for durable boundaries and migration requirements.

The operation labels in this document are catalog identifiers for discussion. They are not endpoint paths, public event names, contract IDs or a final API design.

## 2. Contract layers

Keep the following concerns separate so a change in one cannot silently redefine another:

1. **Product capability:** the user-visible task, such as seeing site health or requesting a replay.
2. **Logical operation:** the query, command or state transition owned by one capability.
3. **Wire contract:** encoded field names, schema dialect, protocol and compatibility version, governed by D-065.
4. **Persistence contract:** durable commit boundary and recoverable state, defined by the persistence and ingestion designs.
5. **Domain semantics:** tariff, evidence, result, forecast, recommendation and replay meaning, versioned by their owning design and decision authority.
6. **Authorization contract:** verified principal plus explicit action/resource entitlement; client-supplied organization/site values are selectors, not authority.
7. **Transport behavior:** protocol acknowledgement, delivery, ordering, retry and connection details, defined only after a source/protocol is selected.

A schema validates structure; it does not itself prove authorization, data quality, settlement correctness, durable receipt, completion, or user permission.

## 3. Logical operation catalog

| Catalog ID / user task | Operation kind and owner | Required authorization boundary | Required logical outcome and status | Linked design / slice |
|---|---|---|---|---|
| **APP-01 — Select organization, portfolio and site** | Query; platform access boundary | Return only the exact organizations/sites granted to the authenticated principal; administrator membership does not imply data access | Distinguish no authorized sites from an empty/zero-data site; never reveal foreign site existence | Identity & Tenant Authorization; VS-002 |
| **APP-02 — Review site and integration health** | Query; Telemetry/Data Health | Explicit site read and relevant telemetry-summary action; raw payload access is separate | Return freshness, coverage, mapping/quality state, processing lag and blocked reason with observed/received/processed times kept distinct | Telemetry Ingestion; Deployment/Recovery; VS-003 |
| **APP-03 — Submit source telemetry** | Producer command followed by internal asynchronous progression; Ingestion | Authenticated machine principal bound to one tenant/site/source/device/point set; event-body scope must match trusted registration | Distinguish protocol acknowledgement, application durable-capture receipt, publication state, normalized-durable state and economic eligibility. Receipt semantics and connector mapping remain owner decision #12 / source-dependent | Telemetry Ingestion §§6.5/9; Persistence §§4.1–4.2; VS-003 |
| **APP-04 — Inspect site model and mapping** | Query plus separate propose/review commands; Energy Graph | Explicit site-model read; mapping-propose and mapping-approve are separate candidate grants; each change carries scope, actor, effective time and evidence | Expose resolved, unresolved, ambiguous, stale and conflicting mapping states. Never guess a point, meter, contract or cross-site PV right | Energy Graph; Identity; VS-002/VS-004 |
| **APP-05 — Request an economic assessment** | Command, potentially asynchronous; Tariff/Cost Analysis | Explicit site cost-analysis action and access to the required meter/account/contract inputs | Request identifies the intended analysis kind and period conceptually. Bill reconstruction, interval assessment and baseline comparison stay distinct; monetary labels/components remain subject to owner decision #8 and G1 evidence | Tariff & Settlement; Cost Analysis; VS-001/VS-006 |
| **APP-06 — Read a cost result and its explanation** | Query; Cost Analysis | Explicit site/account result access; authorize the result and each referenced input/artifact | Use the proposed result/evidence states only if approved; show component status, missing/excluded inputs and provenance. A partial/scenario/blocked outcome is not a verified bill or realized savings | Cost Result & Replay proposal; Persistence §§3/4.3/6; VS-006 |
| **APP-07 — Review a SHADOW recommendation** | Query and append-only annotation command; Recommendation Review | Site-scoped recommendation-read and separately granted review-annotation action | Return immutable proposal/version, evidence refs, forecast/constraint state and SHADOW authority. A review annotation is not a device command, approval to execute or measured outcome | Recommendation & Operator Review; VS-007 |
| **APP-08 — Inspect evidence and request replay** | Query plus replay request and asynchronous run state; Evidence/Replay | Authorize the evidence record and every source/result reference; replay inherits the originating authorized tenant/site scope | Distinguish replay request acceptance from replay completion. Return reproducible, incomplete, invalidated, blocked or divergent state only under the approved result/replay vocabulary; missing inputs never silently use current rules | Cost Analysis & Evidence Replay; Persistence §§4.3/5–8; VS-005/VS-006 |
| **APP-09 — Manage organization membership and site entitlement** | Privileged commands; Access Administration | Separate membership-management and site-entitlement grants, with exact organization/site scope and audit | Report applied, pending-review, denied or failed changes without implying data access merely because a membership changed; approval/revocation policy remains owner/customer decision #14 | Identity & Tenant Authorization; VS-002 |
| **APP-10 — Read operational audit and integration status** | Query; Operations/Audit | Explicit site or organization audit scope; sensitive source payloads and secrets are not returned by default | Distinguish operational health, delivery progress and evidence status; expose actor/action/time/policy references for privileged changes under approved retention | Deployment/Recovery; Persistence §§3/8; VS-003/VS-005 |

The catalog's operation kind is logical. A selected implementation may make an operation synchronous or asynchronous only when it preserves its defined acceptance and completion meaning. Long-running work must return a stable operation reference and an explicit in-progress/terminal state; it must not make “accepted” look like “completed.”

## 4. Asynchronous state and event boundaries

The platform needs durable state transitions, whether implemented by messages, a workflow engine, database polling or an in-process worker. The labels below are semantic categories, not approved wire event names.

| Semantic transition | Evidence required before reporting the transition | What it does not prove |
|---|---|---|
| **Source capture committed** | Authorized source payload and receipt metadata can be recovered from the declared raw-capture authority | Schema validity, normalization, settlement eligibility or downstream processing |
| **Publication accepted** | A downstream transport has accepted a reference to the durable capture and the outcome is recorded/recoverable | Consumer processing or economic eligibility |
| **Telemetry normalized and stored** | Canonical result, quality/mapping status and raw lineage are durably linked under the selected consumer boundary | Bill-grade suitability or valid tariff mapping |
| **Economic assessment completed** | Result and required input/version manifest are recoverable; unresolved inputs are represented in result status | Golden Bill acceptance, verified savings or approval of monetary semantics |
| **Recommendation proposed/reviewed** | Proposal and/or append-only actor-attributed review event is durable | Physical execution, authorization to control, or measured outcome |
| **Replay completed** | Replay outcome, pinned manifest and comparison status are durable | Equality to the original if inputs/build/logic differ; a missing source cannot be replaced silently |

Any emitted event or callback must identify the state transition it reports and link to an internal durable record. It must preserve tenant/site scope and source/actor provenance. Correlation IDs are observability metadata, not business/event identity (D-073). The project has no approved global ordering guarantee. If a consumer needs ordering, its key and scope must be specified for that capability and tested under retries.

## 5. Cross-cutting request, status and error semantics

### 5.1 Authorization

- Derive the principal and allowed action/resource scope at a trusted server boundary.
- Re-authorize resource references and background jobs; a service identity cannot widen the initiating user's scope.
- Do not expose the existence or identifying details of an unauthorized site, meter, contract, result or evidence item.
- Apply the candidate role/action matrix only after owner/customer/security review. Until then, all candidate grants remain denied.
- No operation in this catalog gives a caller or worker command authority. A future control contract requires separate G6/G7 design and site authorization.

### 5.2 Status vocabulary

Keep distinct state dimensions rather than one overloaded status field:

- **Request lifecycle:** received, rejected, accepted/pending, completed or failed.
- **Data lifecycle:** raw-durable, quarantined, publication-pending, published, normalized-durable, replayable/blocked.
- **Evidence quality:** verified, derived, hypothesis, project assumption, unknown or the repository-approved equivalent.
- **Economic result (when a result exists):** COMPLETE, PARTIAL or BLOCKED plus evidence/settlement readiness; a scenario is carried by PROJECT_ASSUMPTION and SCENARIO_ONLY, not by an overloaded result status. If execution ends without a result, the request lifecycle is FAILED and no CostResult/amount is emitted. Canonical vocabulary remains subject to owner and G1 review.
- **Recommendation lifecycle:** SHADOW proposal and append-only review disposition; no execution transition is present in the MVP.
- **Replay outcome:** preserve the result/replay proposal's statuses and its compatibility with the data/version pins.

A single success response or green badge must never flatten these distinctions.

### 5.3 Failure and retry

- Separate authentication failure, authorization denial, malformed contract, unresolved domain input, stale/conflicting version, capacity/backpressure, transient dependency failure and terminal processing failure as stable logical error categories.
- Do not leak resource existence, raw payloads, secrets or another tenant's values in errors.
- State whether a caller may retry, must refresh a version, or needs operator correction. The exact transport code, error envelope and retry header remain wire-contract choices.
- Repeated delivery is expected. Do not promise exactly-once processing or deduplicate by payload hash, timestamp/value, trace ID or transport packet identifier.
- A retry that might create a second material effect must use a stable identity/idempotency rule owned by that operation. Until producer identity and operation-key semantics are approved, separate first-seen telemetry captures remain separate records.
- Backpressure means no durable receipt is issued when the raw-capture authority is unavailable.

## 6. Contract ownership, versioning and compatibility

- D-065 requires a single versioned contract authority and generated cross-language bindings rather than independent hand-maintained definitions. The catalog does not choose its authoring format or generator.
- Keep external wire-contract version, internal persistence-schema version and domain-policy/calculation version distinct. A storage migration does not silently redefine a public event, and a contract version change does not rewrite historical evidence.
- Breaking wire changes require a new version, an explicit producer/consumer rollout, bounded compatibility period, replay compatibility plan and fixture updates.
- Existing V1 telemetry contract, hand-maintained TypeScript parsing and Go event type have not been shown equivalent; this catalog does not close the static parity gap.
- The result/replay shape is a proposal, not canonical contract. Monetary view semantics, decimal precision/rounding and result identity still require owner/G1 evidence.
- Keep contract fixtures for valid, invalid, boundary, unknown-enum, cross-tenant, stale-version, duplicate-delivery, partial-evidence and recovery cases; execute those only against an approved contract/runtime packet.

## 7. Lifecycle examples

### Telemetry to data-health view

1. Connector authenticates as a machine principal and is authorized for a registered source/site/point set.
2. Ingress validates bounds and scope; it preserves raw data and receipt metadata under the selected durable boundary.
3. Only after raw durability may the application issue a platform receipt; connector/broker protocol acknowledgements remain separately mapped.
4. Publication and normalization advance asynchronously with recoverable state. Quarantine, mapping ambiguity, freshness and backlog remain explicit.
5. Site health reads display received/observed/processed times and their impact; they do not treat a successful transport request as current or usable data.

### Cost assessment to SHADOW recommendation

1. An authorized user requests an assessment for an explicit site/account and analysis kind.
2. The cost capability resolves exact meter, contract, tariff, time and data-quality versions; unresolved G1/G3 semantics return blocked/partial/assumption states allowed by reviewed product semantics.
3. A durable result stores its inputs and version references before completion is reported.
4. A SHADOW proposal may consume eligible assessment/forecast evidence; the API exposes a proposal and review path only.
5. A reviewer annotation persists as an attributable append-only event; no call or state here dispatches to equipment.

### Evidence replay

1. An authorized user requests replay for one visible evidence record.
2. The operation validates access to the result and all referenced inputs, then records actor/scope, request and pinned manifest.
3. Replay runs with recorded versions and reports progress.
4. The terminal result is durable and linked to the request and original result; changed/missing inputs produce explicit divergent/incomplete/unavailable status.
5. Replaying cannot broaden tenant scope or modify the original evidence or recommendation.

## 8. Traceability and open decisions

| PRD / slice | Catalog contribution | Still required before wire-contract freeze or implementation |
|---|---|---|
| PR-01 / VS-002 | Site-scoped access to portfolio, site and evidence operations | Owner/customer role validation; identity provider and entitlement choices; security acceptance |
| PR-02/09 / VS-003 | Receipt, publication, normalization and health are separate statuses | Owner decision #12; first authorized source/protocol; V1/V2 and event-identity decision; persistence and source quality |
| PR-03 / VS-004 | Resolved/unresolved/conflict mapping state is explicit | G3 site evidence, graph contract and PV/right relationships |
| PR-04/05 / VS-006 | Assessment kind and result status separate from a request acknowledgement | Owner decision #8; G1 tariff and Golden Bill evidence; result/decimal contract review |
| PR-06/08 / VS-007 | SHADOW proposal and human annotation remain non-authorizing | G2/G4/G5 evidence; user-tested review tasks; G6 remains open |
| PR-07 / VS-005 | Replay request, progress, manifest and terminal outcome are distinct | Canonical manifest/identity; retention/privacy; persistence and restore tests |
| Localization / cross-cutting | Locale formatting and source-language metadata cannot alter domain contract identity | Language/product decision, canonical localized content and wire compatibility policy |

Open decisions are owned by their existing authority records. This catalog does not invent new Gate results or close owner decisions. It is a product/architecture review proposal; no client, source connector, deployment, production API, schema generator or control path is approved by its existence.
