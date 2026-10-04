# Product, Architecture and Delivery Readiness Audit v0.1

**Status:** Evidence-based consolidation for owner review; not an approval, Gate closure, technology selection, implementation authorization or completion claim.
**As of:** 2026-10-04
**Authority:** Current repository state on PR #8 branch docs/product-architecture-roadmap, especially CURRENT, OWNER-DECISION-SUMMARY, PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET, PRD-ARCHITECTURE-TRACEABILITY and MVP-VERTICAL-SLICE-PLAN.
**Purpose:** Define what “complete product design, technical architecture, detailed design and delivery” means; distinguish draft artifacts from validated/approved results; provide a dependency-aware path to completion.

## 1. Lifecycle objective and completion claim

The project objective is an end-to-end lifecycle: validate the Macau commercial-building problem and intended users; approve a coherent product experience; establish an evidence-backed technical architecture and detailed designs; implement and verify the approved MVP; then run an authorized pilot, measure outcomes and make an expand/remediate/stop decision.

The objective is not complete when a PRD, prototype, architecture diagram, detailed-design document or green documentation workflow exists. Completion requires the user-facing product, its operating boundary, engineering behavior and pilot evidence to agree with each other and with recorded decisions.

## 2. Current readiness snapshot

| Workstream | Evidence in repository | Current state | Completion evidence still required |
|---|---|---|---|
| Macau domain research | G0–G7 Gates, evidence register, G1/G2/PV evidence notes, open-question register | Mixed; G0 thesis substantially complete; other Gates retain open evidence as recorded in CURRENT | Close or explicitly bound every Gate that supports an approved product claim. No bill-grade, cross-site PV credit, flexibility, control-safety or Macau-pilot claim may outrun evidence. |
| Product intent and market | Thesis, candidate roles/sites, commercial hypotheses and WP-4 discovery/usability protocol | Draft; target user, buying authority, willingness to pay and primary job unvalidated | Authorized interviews/observations and artifact review with relevant Macau roles/sites; anonymized findings; owner-reviewed product promise, lead role/site and primary workflow. |
| Requirements and acceptance | PRD v0.1 with PR-01–PR-09; PRD-to-architecture traceability | Complete draft structure; requirements unvalidated and acceptance partly Gate-dependent | Approve scope, exclusions, roles, user-visible states and claim boundaries; define measurable acceptance evidence for each in-scope requirement. |
| Interaction and IA | Four task flows, nine screen responsibilities, core-workflow prototype v0.11 (v0.10 retained as prior stimulus), IA-comparison prototype v0.9, Pro Max-informed review | Research-derived draft. v0.10 was observed at 320/375/768/1024/1440 CSS px without document-level horizontal overflow; v0.11 preserves this flow and clarifies that review feedback is page-only and non-persistent; all nine destinations synchronized view and URL, Browser Back restored the prior view, and narrow-selector keyboard input moved focus to the new heading. v0.9 compares three organizations on one synthetic demand case. Neither has target-user findings; 200% zoom, assistive technology, localization, design-token approval and final interaction direction remain open | Authorized WP-4 sessions; screen-reader/full keyboard/200% zoom and language review; revise and obtain Owner approval. |
| Visual system and accessibility | Provisional A/B/C directions; v0.4 sampled contrast review; v0.5 HTML | No approved design system; only a limited browser accessibility-tree render was inspected; measured responsive layout, screenshot visual, keyboard, assistive-technology and user review remain outstanding | Render/inspect supported viewports and zoom; keyboard and assistive-technology review; applicable WCAG 2.2 AA evaluation; owner approval and user comprehension evidence. |
| Logical architecture | Stack-neutral domain, cloud/Edge/Safety and trust-boundary proposals; a logical runtime view maps browser/API, core, ingress/async workers, persistence, AI jobs and Edge without fixing process counts or deployment placement, and specifies durable raw capture before async publication with recoverable pending events | Review draft; owner approval pending | Confirm product/operating responsibilities, then record context/container/deployment decisions and quality attributes against actual workflows, security, data governance and support needs. U-027 requires actual data-flow/vendor-location review before customer-data intake or external AI processing. The runtime view does not select provider, process topology or production stack. |
| Production technology | G6.9-R2 candidates A/B/C+ and layer proposals | No winner. C+ is provisional; Node/NestJS is existing Candidate B evidence; React/TS, Temporal, PostgreSQL/Timescale, NATS, Python, Go Edge and Wasm/WASI retain candidate status. Next.js is not approved. The Step 3D pack calls C+ a product BFF/UI surface; whether that includes browser rendering remains unresolved, so it must not be read as a frontend framework decision. | Resolve Step 3D UI scope and runner blockers; execute comparable pinned workloads; preserve raw results; satisfy Step 4 rule; owner-review ADR/Decision Record. |
| Contracts and data authority | V1 telemetry schema/TS/Go consumers; CostResult/ReplayManifest proposal; contract-format comparison | Noncanonical and incomplete. Static comparison found consumer differences; source-event identity, deduplication, replay canonicalization/storage unresolved. | Choose contract authority/generation after domain semantics; use the same versioned contract in actual runtimes; prove equivalent fixtures, evolution and semantic replay identity; record compatibility policy. |
| Capability detailed designs | VS-001, identity/tenant, telemetry, Energy Graph, Tariff & Settlement, Cost/Evidence Replay, Forecasting/Optimization, Recommendation/Review, Deployment/Recovery, traceability | Substantial stack-neutral drafts exist; the telemetry design now distinguishes durable capture/publication/consumer states, acknowledgement semantics and crash recovery, but no approved contracts, runtime topology or Gate acceptance exists | Cross-review with approved product scope and evidence; resolve data, identity, time/money, replay, retention, failure, security and operations decisions; approve each implementation-slice design. |
| Security and safety | G6 evidence/checklist, tenant authorization, command-boundary proposals, stack-neutral STRIDE threat model v0.1, and command arbitration / Edge Safety Kernel detailed design v0.1 | G6 OPEN; U-022 and U-024 open. Threat scenarios/invariants and a future controlled-mode lifecycle are drafted, including cloud/human/site authority separation, local physical veto, separate settlement guard, offline/manual behavior, durable command intent, unknown-outcome reconciliation, key lifecycle, and G6-01–G6-10 traceability. These are review designs only: controls are not verified, the inspected tree lacks an executable Safety Kernel/command runtime, and no field command is authorized. | Owner/security risk review; deployment-specific mitigations; tenant-isolation/revocation evidence; Edge key lifecycle; site-local veto/limits, manual/offline behavior, signed/idempotent commands, audit and recovery before field writes. A candidate ASVS 5.0.0 control-to-evidence map is drafted and linked from G6-08/G6-09, but target scope/level and all runtime evidence remain open. |
| Implementation | Phase B/C scaffold and static source/tree audit | Partial scaffold, not accepted product. UI, durable migrations/storage, live adapters and executable Safety Kernel are absent or incomplete as recorded in traceability/CURRENT. | Implement approved vertical slices; prove functional, negative, isolation, security, recovery, data-quality and operational acceptance in target environment. |
| Pilot and outcomes | G7 Gate and vertical-slice plan | Not complete; G7.2 live R0 baseline/no-op and U-017 open; no Macau customer result claimed. | Named site/customer authorization; accepted baseline, access, measures and operating owners; fresh no-op and applicable M&V evidence; separate simulation from field results; owner/customer expand/remediate/stop decision. |

## 3. Designed versus not yet complete

### Product design

A coherent first product hypothesis exists: traceable cost intelligence, evidence-linked analysis and explainable SHADOW recommendations, with data quality, site topology and replay context. The PRD and IA describe role hypotheses, task flows, result categories, unknown states and safety boundaries. Prototype v0.6 is a synthetic review surface; limited browser accessibility-tree output is available, but this is not visual, responsive, accessibility or user validation.

This is enough for focused owner review and formative research. It is not validated product design: lead role/site, commercial promise, first-release scope, actual access workflow, language, final navigation and visual direction remain open. The prototype is not the production UI and has not been validated with target users.

### Technical architecture

A stack-neutral logical architecture and candidate map exist. The current layer proposal is not a confirmed production architecture. C+ remains provisional; Step 3D and Step 4 have not selected a winner. The runner manifest has executionReady=false. React + TypeScript remains a separate browser-UI proposal with no framework approval. The G6.9-R2 pack's C+ “product BFF/UI” wording and whether browser rendering enters the stack score require an explicit owner decision before runner freeze. No decision may be inferred from Next.js mentions, the Node/NestJS scaffold, historical Node 22.16 Step 3C evidence, or draft recommendations.

### Detailed design

Detailed-design drafts cover the primary loop and major capabilities, including a stack-neutral command arbitration and Edge Safety Kernel proposal. That proposal defines a future controlled-mode authority split, command lifecycle, local veto and recovery behavior, but does not implement the Safety Kernel or close G6. Topic coverage is not implementation readiness. Canonical contracts, security policy, storage/retention, operational targets, site-specific evidence and failure/recovery acceptance remain unresolved where identified in those designs and Open Questions.

### Engineering and pilot

Governance, task-packet, vertical-slice and Gate acceptance frameworks exist. Production behavior, target-environment acceptance and authorized Macau pilot results have not been demonstrated. Documentation validation checks documents; it does not validate the running application.

## Detailed-design interface cross-review (2026-10-04)

**Method:** Static cross-reading of the telemetry ingestion, Energy Graph, Tariff & Settlement, Cost Analysis/Evidence Replay, Recommendation/Operator Review, CostResult/ReplayManifest proposal, tenant authorization, deployment/recovery and security threat-model drafts. This checks semantic handoffs only; it does not validate implementation or approve a contract.

### Cross-capability rules that currently agree

- Telemetry preserves source identity, observed/received time and quality; Energy Graph keeps physical/electrical relationships separate from settlement/economic relationships; Tariff & Settlement uses explicit account/site scope, tariff period and boundary policy. None should infer settlement demand from raw sample cadence.
- Cost Analysis distinguishes bill reconstruction, interval assessment and baseline comparison. Recommendation design does not convert RecommendationV1 `estimatedValue` into monetary truth, a savings claim or an authorized action.
- Analytical replay pins evidence and semantic inputs, while Edge command replay/idempotency remains a separate G6 concern. The drafts do not conflate a reproducible calculation with exactly-once physical control.
- Tenant scope is intended to derive from verified identity and current authorization across synchronous and asynchronous paths; caller-supplied tenant/site selectors are not authority.

No direct semantic contradiction was found in these reviewed handoffs. They remain proposals, not canonical runtime interfaces.

### Cross-capability blockers before implementation

1. **Telemetry identity and contract authority:** V1 has no stable producer event ID/idempotency contract, and the inspected TypeScript/Go consumers differ. This blocks safe durable deduplication, generated bindings and the event-to-replay lineage proof; do not deduplicate by value/time heuristics.
2. **Cost/replay contract:** CostResult/ReplayManifest remains noncanonical. Result meaning, scope, decimal grammar/scale/rounding, status roll-up, semantic canonicalization/digest, durable reference and retention need domain/owner decisions before generators or production persistence are committed.
3. **Recommendation economics:** RecommendationV1 carries an untyped numeric `estimatedValue`. Keep it out of monetary claims. A versioned typed assessment reference can proceed only after the owner chooses how the interface should communicate absolute expected cost versus baseline-relative effect (or omit monetary display until evidence is ready).
4. **Identity and deployment:** The stack-neutral tenant design has no selected provider/role lifecycle or isolation topology, and the audited HTTP path lacks an auth guard. VS-002 must prove authorization through the actual API, repositories, jobs, caches and evidence paths in the selected runtime.
5. **Verification boundary:** G6-08/G6-09 security controls need deployment-equivalent execution evidence. The proposed ASVS mapping is an acceptance checklist candidate, not proof that these controls exist.
6. **Data governance and external processing:** the Law 8/2005/GPDP review is recorded, but project datasets, controller/processor roles, purposes, provider/subprocessor regions, remote support, backups and AI/API recipients have not been inventoried or reviewed. U-027 remains open; complete that review before customer-data intake or external processing.

### Implementation sequencing consequence

Keep the current technology-neutral slice order: identity/scope → telemetry/source identity → graph resolution → durable evidence/replay → tariff/cost → SHADOW recommendation/review → authorized pilot. Contract experiments and Step 3D runner preparation can progress in parallel, but a production stack, canonical schema, monetary recommendation display, and live command path cannot be inferred from these drafts.

**Evidence boundary:** Source-level review only; no application tests, user sessions, threat workshop, database/runtime verification or Gate closure was performed in this cross-review.

## 4. Dependency-aware completion path

| Stage | Work and deliverable | Exit evidence / decision |
|---|---|---|
| A. Owner direction and user discovery | Review the owner decision summary and synchronized review queue. Decide or defer the directional product promise, lead-user/site discovery hypothesis, operating/architecture authority boundaries and initial PV scope; review recommendation monetary semantics before labels/contracts freeze, and review the proposed telemetry durable-capture acknowledgement boundary before connector/API contracts freeze. Conduct authorized WP-4 discovery and formative sessions using v0.5. Keep visual-system approval evidence-led; decide telemetry identity after connector inventory; revisit D-003 after site/G2 evidence; resolve U-027 by inventorying datasets and provider, subprocessor, support, backup and AI/API flows and obtaining responsible privacy/legal review before customer-data intake or external processing. | Dated owner decisions or explicit deferrals with timing/dependencies; interview/task evidence; updated PRD, IA and prototype; remaining hypotheses explicit. A deferral preserves provisional status and does not delay independent research. |
| B. Research and product acceptance | Close evidence questions needed by the intended release. Reconcile Macau tariff/settlement, site topology, flexibility, forecasting/optimization and safety against in-scope claims/workflows. | Gate decisions with sources, scope and limits; no product claim exceeds passed evidence or an explicit bounded-pilot limit. |
| C. Step 3D/4 technology decision | Resolve runner-only Temporal persistence and UI-contract/browser scope; freeze images/digests, locks, configuration, resources and BOPTEST build; execute A/B/C+ comparably under G6.9-R2. | Reproducible runner and raw results; Step 4 decision rule; owner-reviewed ADR/Decision Record. Production stack remains unselected before this. |
| D. Architecture and detailed-design approval | Reconcile approved workflows, Gate evidence, contract decision and runtime results. Complete context/container/deployment/security/data views and slice-specific designs. | Owner-approved architecture/ADRs; canonical versioned contracts; reviewed threat/failure/recovery model; migration/rollback and operational ownership; requirement-to-design-to-acceptance traceability. |
| E. Approved MVP implementation | Deliver dependency-ordered slices from the approved vertical-slice plan; label work outside production authority as exploratory. | Running target-environment product; acceptance, security, reliability, accessibility and operational results; migrations, observability, recovery and rollback evidence; all in-scope PRD requirements traced to accepted behavior. |
| F. Authorized pilot and learning | Operate only within named site/customer approval, permissions, safety boundary and agreed measurement plan. | G7 evidence; measured outcomes with confounders/limits; operations handoff; incident/recovery evidence; expand/remediate/stop decision. |

Stages may overlap only where dependencies are independent. Product discovery, Macau tariff research and runner preparation can proceed in parallel. Production technology-specific implementation cannot be treated as selected before Step 4 and owner approval. A Gate may remain open only when the release scope explicitly excludes the dependent claim/capability and the owner-approved acceptance boundary says so.

## 5. Immediate next work

1. **Owner review:** use docs/02-product/OWNER-DECISION-SUMMARY-v0.1.md and docs/02-product/PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md to record each directional choice or explicit deferral. The queue states when each choice is due: some choices guide discovery now, others depend on connector/site/Gate evidence, and privacy/security/deployment decisions precede customer-data intake or production. Recommendation text is not approval.
2. **WP-4 validation:** after recruitment/access is authorized, select the study instrument to match the question: use the current v0.11 core workflow tasks for task comprehension and completion, and/or the v0.9 comparative IA protocol for evidence-first, exception-led and guided-assessment organization. Keep scenario content/task-critical facts equivalent, counterbalance order where needed, report task behavior separately from preference, and do not declare an IA winner from a small formative sample. No participant contact or customer-data collection is authorized by this audit.
3. **Architecture evidence:** continue G1/G2/G3/G6/G7 and G6.9-R2 under their prerequisites. Step 3D blockers and runner prerequisites are listed in its readiness plan/manifest; CURRENT records Docker/Compose, Bun and Go as unavailable on the task host.
4. **Detailed-design convergence:** after owner direction and applicable evidence, resolve contract authority, event identity, result/replay semantics, tenant authorization and deployment/operability before canonical schemas or production adapters.
5. **Implementation:** start only from an approved, ready slice packet. The current VS-001 scaffold is not accepted end-to-end behavior.

## 6. Completion audit checklist

Do not report the lifecycle objective complete until current evidence proves all applicable statements below:

- [ ] Product problem, lead user/site and first-release promise have owner decisions supported by Macau user/customer evidence.
- [ ] In-scope PRD requirements and workflows are validated; exclusions and unresolved claims are visible.
- [ ] Visual/interaction decisions have owner review, relevant user evidence, rendered accessibility/responsive review and approved design-system artifacts.
- [ ] Production architecture is selected by G6.9-R2 evidence/decision process and owner-approved records; candidates/prototypes are not mistaken for decisions.
- [ ] Detailed designs and canonical contracts cover every in-scope requirement, including authorization, tenancy, time/money semantics, failure/retry/idempotency, lineage, observability, deployment, recovery, migration and rollback.
- [ ] U-027 dataset classification, recipient/location inventory and responsible privacy/legal review are recorded before any customer-data intake or external processing; the chosen deployment follows those reviewed constraints.
- [ ] Required Macau domain/security Gates pass for the claimed release scope or the owner-approved scope explicitly excludes the dependent capability/claim.
- [ ] MVP is implemented and functional, negative, security, reliability, accessibility and operational acceptance passes in the target environment.
- [ ] A named pilot has site/customer authorization, accepted baseline/outcome method, operations ownership and recoverable deployment.
- [ ] Pilot outcomes, limitations and confounders are recorded; an owner/customer expand/remediate/stop decision and handoff are complete.
- [ ] Repository, Decision Records, evidence register, release artifacts and CURRENT handoff agree with verified state.

## 7. Authority and limitations

This audit consolidates the current PR branch; it does not replace research Gates, owner decisions, G6.9-R2 authority, PRD, architecture records, detailed designs or implementation checks. Resolve conflicts in the owning authority document before relying on this summary. PR #8 is open and unmerged; these changes are not on main.

## 8. Primary records

- Current project state: docs/00-authority/handoff/CURRENT.md
- Owner decision queue: docs/02-product/OWNER-DECISION-SUMMARY-v0.1.md
- Product/architecture review: docs/02-product/PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md
- Research-to-delivery roadmap: docs/00-authority/ROADMAP.md
- Research Gates: docs/01-research/gates/README.md
- Step 3D readiness and runner manifest: docs/01-research/G6.9-technology-research/STEP-3D-READINESS-AND-EXECUTION-PLAN-v0.1.md and STEP-3D-RUNNER-MANIFEST-v0.1.json
- Logical architecture: docs/03-architecture/ARCHITECTURE-DESIGN.md
- Security threat model: docs/03-architecture/detailed-design/SECURITY-THREAT-MODEL-v0.1.md
- Command arbitration and Edge Safety Kernel detailed design (review draft; G6 open, no control authorization): docs/03-architecture/detailed-design/COMMAND-ARBITRATION-AND-EDGE-SAFETY-KERNEL-DETAILED-DESIGN-v0.1.md
- Detailed-design and implementation traceability: docs/03-architecture/detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md
- Candidate delivery slices: docs/05-mvp/vertical-slices/MVP-VERTICAL-SLICE-PLAN-v0.1.md
- Product and engineering governance: docs/04-engineering/PRODUCT-DESIGN-AND-DELIVERY-GOVERNANCE-v0.1.md

## Follow-up: consolidated PRD-to-product evidence map — 2026-10-04

Added a joined traceability view connecting PR-01–PR-09 to proposed user flows/screens, planned WP-4 probes, detailed-design authorities, candidate vertical slices, and current evidence gaps. This closes an artifact-linking gap in the traceability package, not the lifecycle evidence gap: WP-4 remains unperformed, v0.9 covers one synthetic IA case, PRD scope is unapproved, and G1/G2/G3/G4/G5/G6/G7 and G6.9-R2 remain subject to their recorded gates. No readiness category is advanced by adding the map.


## Follow-up: PV settlement boundary cross-design review — 2026-10-04

A bounded static cross-review compared the G1 PV evidence note and U-025 with the Energy Graph, Tariff & Settlement, Cost Analysis/Evidence Replay, VS-001 result design, PRD-to-architecture traceability and VS-004/VS-006 acceptance.

- **Consistent boundary:** all reviewed designs separate (1) the physical PV/grid/export flow, (2) the producer's CEM feed-in settlement, (3) the consumer's import meter and retail account, and (4) any explicitly authorized site-economic aggregation. No reviewed design infers a remote customer's bill credit from grid connection or feed-in payment.
- **Consistent topology rule:** host/site-use rights, PV system owner/operator, producer account/export meter, and consumer account/import meter are represented as distinct evidence-backed relationships. Cross-parcel physical distribution and cross-account allocation require their own authorization, contract, metering and settlement evidence; an interconnection-capacity limit is not treated as settlement authority.
- **Public-source count context:** DSPA's 2026-09-01 update says that 12 systems were interconnected and selling electricity as of 2026-08-31, while CEM's PV page reports 12 grid-connected systems, 4,193 kWp and more than 6 million kWh generated as of January 2026. The unit counts agree across those reported statements, but the dates and status wording differ. DSPA's later update gives no corresponding capacity or production total, so these values do not establish a capacity/generation trend. See the [DSPA PV page](https://www.dspa.gov.mo/energytopics/solar/c1.html) and [CEM PV introduction](https://www.cem-macau.com/zh/smart-living/photovoltaic-system-%28pv%29/pv-introduction/).
- **Finding and limit:** no semantic contradiction was found in the reviewed drafts. This is static document review only; it does not validate a schema, site graph, customer contract, legal interpretation, meter mapping, runtime calculation, user understanding or implementation.
- **Status:** U-025 remains UNKNOWN for third-party host/PPA and remote-account settlement rights. U-026 remains partially resolved: the public count statements agree at 12 but remain non-contemporaneous and do not provide comparable capacity/production totals. G1 remains OPEN. The prepared U-025 request bundle E has not been sent; owner authorization and secure intake are still prerequisites.
