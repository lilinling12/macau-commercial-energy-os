# MVP Vertical Slice Plan v0.1

**Status:** Candidate delivery plan; product scope, user roles, architecture and G6.9-R2 technology selection remain unapproved.
**Purpose:** Break the research-derived PRD into dependency-ordered, reviewable end-to-end product increments with explicit acceptance evidence.
**Authority:** PRD v0.1, USER-FLOWS-AND-IA v0.1, G0–G7, G6.9-R2, CURRENT handoff and PRD-to-architecture traceability.
**Boundary:** This plan organizes work; it does not authorize implementation against an unapproved stack, close a research Gate, relax G6, claim bill-grade value or authorize field control.

## Planning assumptions and current state

- The nine PRD requirements and nine screen responsibilities are research-derived hypotheses, not customer-approved scope.
- The current VS-001 Energy Intelligence Loop is the end-to-end target outcome. The source/contract/adapter path is a scaffold with static gaps; the current audit does not show it meeting the VS-001 acceptance boundary.
- Product user roles, target segment, commercial promise, information hierarchy and final visual direction remain subject to customer validation and owner review.
- G6.9-R2 Step 3D/4 has not selected a production runtime. These slices remain logical and technology-neutral until its decision is reviewed.
- Slice sequencing may be revised as G1–G7 evidence or customer discovery changes scope.

## Candidate delivery sequence

| Increment | Product outcome and PRD mapping | Research / architecture dependencies | Acceptance evidence |
|---|---|---|---|
| **VS-002 — Site identity, scope and access** | Establish an organization/site context and enforce authorized scope across the user/API/job/evidence paths. PR-01; screens S-01/S-02/S-09. | Owner-reviewed target roles and site boundary; identity/tenant design; G6-09 security evidence; deployment context. No identity provider or role set is selected by this plan. | Authorized user can access only granted site data; negative cross-tenant/site cases fail without leaking records; organization membership administration is not an implicit site-data grant; delegated partner grants are scoped, attributable, expiring and revocable; replay source references remain inside persisted authorized scope; revocation takes effect across API/jobs/evidence; changes are attributable and auditable. |
| **VS-003 — Source onboarding, telemetry and data health** | Connect an approved read-only source, ingest telemetry, show freshness/coverage/mapping/quality and integration health. PR-02/PR-09; screens S-03/S-09; Flow A. | Site-approved source and permission; canonical contract authority and cross-runtime parity; retention and failure policy; G2/G3 site evidence as applicable. | Preserve source identity and raw/rejected evidence; validate units/time/quality; expose observed/received time, telemetry freshness/quality state, Energy Graph mapping state and downstream impact as separate dimensions; a stale measurement and an expired mapping have different causes and remedies; retries/corrections are traceable; outages do not create false healthy status. Implement and verify the telemetry state model in `TELEMETRY-INGESTION-AND-DATA-QUALITY-DETAILED-DESIGN-v0.1.md` §9: issue the application-level capture receipt only after durable raw capture; track protocol/broker ACK separately (MQTT PUBACK is not that receipt unless the broker is the recovery-verified authoritative raw store); recover pending publication after crashes; acknowledge consumers only after durable effects, and expose captured/published/normalized/blocked as distinct states. Preserve source retries as separate captures when no stable source event ID exists; do not deduplicate by value/time/hash heuristics. Apply `DATA-PERSISTENCE-AND-SCHEMA-EVOLUTION-DETAILED-DESIGN-v0.1.md` §§4.1–4.2/7 for raw payload/receipt durability, recoverable publication, consumer effects and compatible migration; physical mechanisms remain pending stack selection. Do not infer mappings or bill values. |
| **VS-004 — Site model and Energy Graph resolution** | Configure site assets, meter/point mappings, physical/electrical relationships and separately evidenced settlement relationships. PR-03; screen S-04; Flow A. | G3 site evidence; G1 meter/account/contract semantics; reviewed canonical identity, effective-time and provenance rules. | Authorized mappings produce a versioned path from source point to physical/electrical context and, only when supported, settlement context; for PV, keep host, site-use right, system owner/operator, producer/export contract and consumer/import account distinct; missing, ambiguous, conflicting, expired (`EXPIRED_MAPPING`) or unauthorized mapping fails closed; telemetry freshness/quality remains separate; no cross-account credit is inferred; historical correction can be explained and replayed. |
| **VS-005 — Evidence, audit and deterministic replay foundation** | Preserve the input/configuration/version lineage for material results and review events; replay an unchanged snapshot. PR-07; screen S-08; cross-cuts every later slice. | Canonical event/result identity and contract authority; tenant-scoped durable storage; retention, correction, canonicalization and digest decisions; security review. | Same pinned business inputs and versions reproduce the same semantic result identity; operational trace IDs do not alter it; corrected evidence creates a new lineage; missing or changed inputs yield explicit incomplete/unavailable replay; no silent substitution. |
| **VS-006 — Tariff, bill and cost analysis** | Resolve effective-dated tariff/contract rules and explain bill reconstruction, interval assessment and baseline comparison as distinct result kinds. PR-04/PR-05; screens S-05/S-06; Flow B. | G1 rules and applicable real Golden Bills; G3 settlement mapping; VS-005 evidence lineage; owner-reviewed result semantics. | For each approved tariff scope, show component/source/rule provenance and coverage; unresolved rules withhold bill-grade output; Golden Bill acceptance is ≤0.5% error with zero unexplained adjustment for the declared scope; PV producer export is separate from consumer import; modeled differences are not realized savings. |
| **VS-007 — Shadow forecast/recommendation and operator review** | Present a forecast-backed, constrained SHADOW proposal and record review dispositions separately from authorization, command and observed outcome. PR-06/PR-08; screen S-07; Flow C. | G2 asset/flexibility evidence; G3 mapping; G1 cost semantics; G4/G5 evidence; G6 safety boundary; VS-005 replay/audit. | Show baseline, horizon, constraints, assumptions, uncertainty, evidence coverage and model/configuration; permit reviewed/dismissed/needs-data annotation; no device-write path exists in this MVP; review never implies command approval or measured savings. |
| **VS-008 — Pilot measurement, operational readiness and handoff** | Deliver a site-scoped SHADOW/advisory pilot with an agreed baseline, evidence export/replay, operator workflow and expand/remediate/stop decision. PR-01–PR-09 as approved; Flow D; G7. | G0 customer/site confirmation; G1–G5 scoped evidence; G6 controls for any authorized live action; G7.2 baseline/no-op and applicable M&V; deployment/recovery design and explicit site authorization. | Named site/customer approves scope, access and measures; baseline and data quality are accepted; simulated and live results are separated; outcome method and confounders are documented; recovery/support ownership and operational handoff are accepted; owner/customer records proceed, remediate or stop. |

VS-001 remains the integration-level outcome formed by the accepted increments above. It must not be labelled complete merely because a synthetic path or one vertical component runs.

## Dependency order

`VS-002 → VS-003 → VS-004 → VS-005 → VS-006 → VS-007 → VS-008`

Evidence/replay primitives and audit hooks should be designed into VS-002–VS-004, even though VS-005 makes the full replay capability independently reviewable. Work can overlap where dependencies are genuinely independent, but acceptance cannot borrow evidence from a later or unapproved increment.

## Detailed-design handoff by slice

This matrix connects the candidate implementation order to the detailed-design work already in the repository. Each referenced design is a draft input, not an implementation authorization or proof that its acceptance criteria have passed. The task packet for a slice must narrow these references to the exact approved scope and identify unresolved decisions before coding.

| Increment | Detailed-design inputs | Slice-specific readiness constraint |
|---|---|---|
| **VS-001 — Integration-level Energy Intelligence Loop** | `docs/03-architecture/detailed-design/VS-001-DETAILED-DESIGN-v0.1.md`; use the capability designs below for owning details. | End-to-end target only; do not treat the scaffold or synthetic flow as satisfying acceptance. Its acceptance depends on the accepted capability slices and open Gates. |
| **VS-002 — Site identity, scope and access** | `docs/03-architecture/detailed-design/VS-001-IDENTITY-AND-TENANT-AUTHORIZATION-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/DEPLOYMENT-OPERABILITY-AND-RECOVERY-DETAILED-DESIGN-v0.1.md`. | Select an identity/deployment context and validate role/site entitlements before production auth implementation. |
| **VS-003 — Source onboarding, telemetry and data health** | `docs/03-architecture/detailed-design/TELEMETRY-INGESTION-AND-DATA-QUALITY-DETAILED-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/VS-001-DETAILED-DESIGN-v0.1.md`. | Resolve canonical contract authority, consumer parity, source permission and site quality/freshness policies; implement the telemetry detailed design §9 protocol-ACK/application-capture-receipt/publication/consumer state model and crash recovery. The current V1 parity gap remains open. |
| **VS-004 — Site model and Energy Graph resolution** | `docs/03-architecture/detailed-design/ENERGY-GRAPH-DETAILED-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/VS-001-DETAILED-DESIGN-v0.1.md`. | Validate site topology, point identity and settlement relationships; synthetic graph fixtures do not close G3. |
| **VS-005 — Evidence, audit and deterministic replay foundation** | `docs/03-architecture/detailed-design/COST-ANALYSIS-AND-EVIDENCE-REPLAY-DETAILED-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/VS-001-RESULT-AND-REPLAY-CONTRACT-PROPOSAL-v0.1.md`; `docs/03-architecture/detailed-design/DEPLOYMENT-OPERABILITY-AND-RECOVERY-DETAILED-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/DATA-PERSISTENCE-AND-SCHEMA-EVOLUTION-DETAILED-DESIGN-v0.1.md`. | Settle immutable input identity, semantic digest, tenant-scoped persistence, retention/correction and restore requirements before claiming deterministic or durable replay. Apply the persistence design's §§4.3/5–8 acceptance criteria; all physical choices and owner policies remain open. |
| **VS-006 — Tariff, bill and cost analysis** | `docs/03-architecture/detailed-design/TARIFF-SETTLEMENT-DETAILED-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/COST-ANALYSIS-AND-EVIDENCE-REPLAY-DETAILED-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/VS-001-RESULT-AND-REPLAY-CONTRACT-PROPOSAL-v0.1.md`. | Resolve applicable G1 rules and Golden Bill evidence; leave unknown tariff/settlement behavior blocked and scenario-only until then. |
| **VS-007 — Shadow forecast/recommendation and operator review** | `docs/03-architecture/detailed-design/FORECASTING-AND-OPTIMIZATION-DETAILED-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/RECOMMENDATION-AND-OPERATOR-REVIEW-DETAILED-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/COST-ANALYSIS-AND-EVIDENCE-REPLAY-DETAILED-DESIGN-v0.1.md`. | Resolve product economics semantics and G2/G4/G5 evidence. Preserve SHADOW-only behavior; G6 remains an independent command authority. |
| **VS-008 — Pilot measurement, operational readiness and handoff** | `docs/03-architecture/detailed-design/DEPLOYMENT-OPERABILITY-AND-RECOVERY-DETAILED-DESIGN-v0.1.md`; `docs/03-architecture/detailed-design/COMMAND-ARBITRATION-AND-EDGE-SAFETY-KERNEL-DETAILED-DESIGN-v0.1.md` (only if a later controlled-mode scope is approved); `docs/02-product/CUSTOMER-DISCOVERY-AND-USABILITY-RESEARCH-PLAN-v0.1.md`; `docs/01-research/gates/G7-pilot-validation.md`. | Requires a named, authorized pilot site and accepted outcome/operational evidence; planning artifacts alone cannot satisfy G7. Keep a SHADOW/advisory pilot device-write-free. Any later controlled-mode pilot additionally requires site-specific hazard/commissioning evidence, G6 closure for its scope, and explicit customer/site authorization; the draft design itself grants none. |

## Ready and done rules

A slice is **ready** only when:

1. its user outcome and in-scope PRD requirement have been reviewed;
2. relevant Authority, Gate state, contracts and Open Questions are linked;
3. the required product-owner decisions and external/site permissions are satisfied;
4. module/API/data boundaries, failure behavior, security, migration/rollback and telemetry are designed;
5. acceptance scenarios and exact evidence artifacts are specified; and
6. the approved runtime/contract boundary is known for technology-specific implementation.

A slice is **done** only when:

1. the user-visible path works end to end for its approved scope;
2. positive, negative, failure, authorization/isolation and recovery cases have required evidence;
3. acceptance checks and exact results are recorded; no application validation is implied by documentation CI;
4. contracts and architecture remain aligned with approved decisions;
5. PRD traceability, Gate/evidence status and CURRENT handoff are updated; and
6. review approval and next dependency-ready work are recorded.

## Stop conditions

Do not advance a slice into production claims when its required Gate is open or its evidence is missing. In particular:

- G1 unknowns block bill-grade reconstruction and unsupported monetary ranking.
- G3 ambiguity blocks authoritative site/settlement attribution.
- G6 remains the independent safety authority; no optimizer bypass or field command is authorized.
- G6.9-R2 Step 4 must be recorded before selecting the production stack.
- G7 fixture/simulation evidence never becomes Macau customer evidence by relabeling.
- A slice marked `proposed`, `draft` or `blocked` is not accepted functionality.

## Next review

Review this sequencing alongside the product/architecture owner packet and PRD. Confirm or revise the product promise, lead user/site, MVP outcome and role/approval boundary first; then review the logical slice boundaries. Keep framework and production topology provisional until G6.9-R2 Step 3D/4 evidence and an explicit decision record are complete.

## Related records

- PRD and interaction design: `docs/02-product/PRD-v0.1.md`, `docs/02-product/USER-FLOWS-AND-IA-v0.1.md`
- Product/architecture owner review: `docs/02-product/PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md`
- Existing end-to-end target: `docs/05-mvp/vertical-slices/VS-001-energy-intelligence-loop.md`
- Research-to-delivery roadmap: `docs/00-authority/ROADMAP.md`
- Requirement and implementation gap audit: `docs/03-architecture/detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md`
- Logical application and event operation/state catalog (review draft; no wire schema selected): `docs/03-architecture/detailed-design/MVP-APPLICATION-AND-EVENT-CONTRACT-CATALOG-v0.1.md`
- Current status: `docs/00-authority/handoff/CURRENT.md`
