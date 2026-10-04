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
| Requirements and acceptance | PRD v0.1 with PR-01–PR-10; PRD-to-architecture traceability | Complete draft structure; requirements unvalidated and acceptance partly Gate-dependent | Approve scope, exclusions, roles, user-visible states and claim boundaries; define measurable acceptance evidence for each in-scope requirement. |
| Interaction and IA | Dispatch-first Flow B/C/D and S-10 proposal, plus four task flows, ten screen responsibilities, core-workflow prototype v0.11 (v0.10 retained as prior stimulus), IA-comparison prototype v0.9, Pro Max-informed review | Research-derived draft. v0.10 was observed at 320/375/768/1024/1440 CSS px without document-level horizontal overflow; v0.11 preserves this flow and clarifies that review feedback is page-only and non-persistent; all nine destinations synchronized view and URL, Browser Back restored the prior view, and narrow-selector keyboard input moved focus to the new heading. v0.9 compares three organizations on one synthetic demand case; PR #10 v0.4 is a separate six-stage synthetic dispatch study. Neither has target-user findings; 200% zoom, assistive technology, localization, design-token approval and final interaction direction remain open | Authorized WP-4 sessions; screen-reader/full keyboard/200% zoom and language review; revise and obtain Owner approval. |
| Visual system and accessibility | Provisional A/B/C directions; v0.4 sampled contrast review; v0.5 HTML | No approved design system; only a limited browser accessibility-tree render was inspected; measured responsive layout, screenshot visual, keyboard, assistive-technology and user review remain outstanding | Render/inspect supported viewports and zoom; keyboard and assistive-technology review; applicable WCAG 2.2 AA evaluation; owner approval and user comprehension evidence. |
| Logical architecture | Stack-neutral domain, cloud/Edge/Safety and trust-boundary proposals; a logical runtime view maps browser/API, core, ingress/async workers, persistence, AI jobs and Edge without fixing process counts or deployment placement, and specifies durable raw capture before async publication with recoverable pending events | Review draft; owner approval pending | Confirm product/operating responsibilities, then record context/container/deployment decisions and quality attributes against actual workflows, security, data governance and support needs. U-027 requires actual data-flow/vendor-location review before customer-data intake or external AI processing. The runtime view does not select provider, process topology or production stack. |
| Production technology | Local G7.6/G7.8 archives; main G6.9-R2 CURRENT/Decision Register; implementation/contracts README | Authority is unreconciled. Two local G7.6 Step 2 archives differ: the lightweight duplicate labels ADR-068 Proposed, while the 27,773-byte detailed archive (Authority v1.7.1; TECH_STACK_FREEZE dated 2026-10-03) labels ADR-068/071–076 Accepted, including React/TS/Vite, Node 24/Fastify 5 modular monolith, Go Edge, Python, PostgreSQL 18 initial store, NATS/JetStream, contract-first design and no direct cloud control. Local G7.8 Step 3 separately labels its ADR freeze complete and records React/TS, Node LTS/Fastify, Go Edge, Python and OpenAPI + JSON Schema. Local Deep Research (6) recommends provisional C+ (Go core, Bun/Hono BFF, Temporal Go); later Deep Research (7), dated 2026-10-02, recommends React/TS + Node/NestJS modular monolith + Go ingest/Edge + Python. Report (7) mentions Next.js only as optional public/customer portal/server-feature technology; owner decision #16 separately asks whether to add it to a future backend candidate experiment. Current main says G6.9-R2 Step 3D is pending, C+ provisional, A/B candidates; Node/NestJS is Candidate B implementation evidence, not a winner. Next.js is not in the current bake-off. The G7.8 Step 3 archive is local and is not explicitly cited/superseded in current main. | Record an explicit authority decision on whether G7.8 remains binding, is superseded by G6.9 evidence gates, or requires re-evaluation. Reconcile its OpenAPI + JSON Schema choice with D-065 and the PR #8 catalog. Then complete the applicable pinned comparison/Step 4 rule and owner-review the architecture ADR. Until then, do not call the production stack “unselected” without disclosing the earlier recorded freeze. |
| Contracts and data authority | V1 telemetry schema/TS/Go consumers; CostResult/ReplayManifest proposal; contract-format comparison | Noncanonical and incomplete. Static comparison found consumer differences; source-event identity, deduplication, replay canonicalization/storage unresolved. | Choose contract authority/generation after domain semantics; use the same versioned contract in actual runtimes; prove equivalent fixtures, evolution and semantic replay identity; record compatibility policy. |
| Capability detailed designs | VS-001, identity/tenant, telemetry, Energy Graph, Tariff & Settlement, Cost/Evidence Replay, Forecasting/Optimization, Recommendation/Review, Deployment/Recovery, traceability | Substantial stack-neutral drafts exist; the telemetry design now distinguishes durable capture/publication/consumer states, acknowledgement semantics and crash recovery, but no approved contracts, runtime topology or Gate acceptance exists | Cross-review with approved product scope and evidence; resolve data, identity, time/money, replay, retention, failure, security and operations decisions; approve each implementation-slice design. |
| Security and safety | G6 evidence/checklist, tenant authorization, command-boundary proposals, stack-neutral STRIDE threat model v0.1, and command arbitration / Edge Safety Kernel detailed design v0.1 | G6 OPEN; U-022 and U-024 open. Threat scenarios/invariants and a future controlled-mode lifecycle are drafted, including cloud/human/site authority separation, local physical veto, separate settlement guard, offline/manual behavior, durable command intent, unknown-outcome reconciliation, key lifecycle, and G6-01–G6-10 traceability. These are review designs only: controls are not verified, the inspected tree lacks an executable Safety Kernel/command runtime, and no field command is authorized. | Owner/security risk review; deployment-specific mitigations; tenant-isolation/revocation evidence; Edge key lifecycle; site-local veto/limits, manual/offline behavior, signed/idempotent commands, audit and recovery before field writes. A candidate ASVS 5.0.0 control-to-evidence map is drafted and linked from G6-08/G6-09, but target scope/level and all runtime evidence remain open. |
| Implementation | Phase B/C scaffold and static source/tree audit | Partial scaffold, not accepted product. UI, durable migrations/storage, live adapters and executable Safety Kernel are absent or incomplete as recorded in traceability/CURRENT. | Implement approved vertical slices; prove functional, negative, isolation, security, recovery, data-quality and operational acceptance in target environment. |
| Pilot and outcomes | G7 Gate and vertical-slice plan | Not complete; G7.2 live R0 baseline/no-op and U-017 open; no Macau customer result claimed. | Named site/customer authorization; accepted baseline, access, measures and operating owners; fresh no-op and applicable M&V evidence; separate simulation from field results; owner/customer expand/remediate/stop decision. |

## 3. Designed versus not yet complete

### Product design

A coherent product direction is now explicit from the user: economic scheduling of commercial-site electricity sources and flexible loads, supported by data/contract qualification, site topology, evidence, SHADOW review and replay. This direction is reflected in the PRD and product-design drafts but is not yet an owner-approved/frozen product scope. The first evidence-qualified outcome, lead role/site and commercial value remain unvalidated. The dispatch-first PRD and IA describe source/load scheduling, role hypotheses, task flows, result categories, unknown states and safety boundaries. Prototype v0.11 is the broader nine-destination synthetic core-flow study; PR #10 v0.4 is the separate six-stage dispatch workflow study, currently on an open Draft PR. The latter received a bounded rendered-browser review at 1265×712 CSS px and prior width checks at 1440/1024/768/375; these establish only the recorded layout/visible-source observations, not complete interaction coverage, user validation, accessibility conformance or approval. No canonical dispatch contract, solver, site evidence or executable dispatch workflow is established.

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


## Follow-up: operability and tenant-authorization cross-design review — 2026-10-04

**Method:** Static cross-reading of Deployment, Operability and Recovery §§3–9, Security Threat Model §§1–6C, and VS-001 Identity and Tenant Authorization §§4–8. This review checks design handoffs only; it does not validate implementation or approve an identity/deployment policy.

- **Consistent trust boundary:** all three designs derive tenant/site scope from authenticated principals and server-owned entitlements; request payload IDs remain selectors, and scope is carried through synchronous APIs, workers, persistence, caches, evidence/replay and support paths. Default-deny and explicit cross-boundary reauthorization are consistent.
- **Consistent operating boundary:** liveness/readiness and source freshness remain separate; health projection does not rewrite evidence status. Economic correctness is not inferred from uptime. Tenant-safe observability, site-level degradation, restoration validation and release manifests are aligned.
- **Consistent recovery and safety boundary:** backups/restores must preserve tenant scope, historical evidence and authorized deletion state; retries/replay must not widen access or duplicate a future physical effect. Device writes remain disabled unless separate G6/G7 evidence and site/customer authorization exist.
- **Gap found and corrected in the identity draft:** the deployment design requires sensitive-evidence access logging, while identity §6 explicitly named privileged changes and denied cross-scope attempts but did not state successful sensitive reads, exports, support access, restore or break-glass events. Identity §6 now requires auditable events for data classified as sensitive and these privileged paths, while leaving the exact read classes to data classification and leaving retention/access policy open.
- **Still unresolved:** validated user roles/site grants; identity provider and workload identity; deployment/isolation mode; data classification and Macau-specific privacy/legal review; log/audit retention; revocation bounds; numeric SLO/RPO/RTO; support/on-call ownership; and executable negative, restore and failure-recovery evidence. The design checklists are not test results and do not close G6-08/09/10.

No other direct semantic contradiction was found in this bounded review. Product/security/operations owner review and runtime verification remain required; this review does not authorize customer-data processing or field control.


## Follow-up: cost-result and request-state cross-design review — 2026-10-04

**Method:** Static cross-reading of Cost Analysis and Evidence Replay §§3–9, the VS-001 CostResult/ReplayManifest proposal, the MVP Application and Event Contract Catalog §§5.1–5.2/6, the Recommendation and Operator Review design, and D-026. This checks state semantics in drafts; it does not approve or implement a canonical wire contract.

- **Mismatch found:** the cost-analysis design listed `failed` as a calculation-result status, while the application catalog places `failed` in request lifecycle. The result proposal omitted `FAILED` but included `SCENARIO` in `resultStatus`, even though it already defined `evidenceStatus` and `settlementReadiness` for assumption/scenario basis.
- **Drafts reconciled:** economic-result status is now `COMPLETE | PARTIAL | BLOCKED` when a CostResult exists. Request execution failure is `FAILED` in request lifecycle and emits no CostResult or amount. Scenario basis uses `PROJECT_ASSUMPTION` evidence and `SCENARIO_ONLY` settlement readiness; its completed calculation may be COMPLETE or PARTIAL, but is not bill-grade eligible. Cost design, contract proposal and application catalog now state this consistently.
- **Semantics preserved:** BLOCKED remains a usable result explaining missing/conflicting required evidence and emits no authoritative amount; PARTIAL is explicitly bounded; COMPLETE describes computation completeness, not bill correctness. RecommendationV1 `estimatedValue` remains non-authoritative under D-026; review acknowledgement remains separate from measured outcome and command execution.
- **Still open:** canonical contract owner/version, monetary display meaning, decimal grammar/scale/rounding, evidence and replay identity/canonicalization, applicability of G1 rules, and product validation. The proposal remains noncanonical; generated bindings and runtime changes are not authorized by this review.

No direct contradiction remains across the reviewed state handoffs. Static documentation review only; no application tests, generated contract validation, customer validation, bill acceptance, Gate closure or production readiness is claimed.

## Follow-up: G4/G5 economic handoff and tariff status mapping — 2026-10-04

**Method:** Static cross-reading of G4/G5 Gate criteria; Forecasting and Optimization §§2–9; Tariff & Settlement §§4–7; Cost Analysis/Evidence Replay; CostResult/ReplayManifest; Application/Event Status Catalog; and D-002/D-018/D-028/D-033/D-040/D-050/D-059–D-061/D-074.

- **Forecast/time boundary is consistent:** day-ahead/intraday grids are evaluation choices, not CEM demand-window definitions or universal command cadence. U-001 remains the authority for the unresolved Pu measurement window.
- **Economic evaluation boundary is consistent:** total economic cost/value (D-002), same tariff-rule package for solver representation and exact re-evaluation (D-018/D-028), and paired modeled dispatch value versus absolute site bill (D-050/SitePowerComposer) are preserved. BOPTEST KPIs remain engineering diagnostics, and G1/G2/G3/G4/G5/G6/G7 evidence boundaries are not collapsed.
- **Safety/recommendation boundary is consistent:** hard constraints and Demand Guard can veto; optimization has no privileged command path; only eligible outputs become SHADOW proposals; review, modeled delta and measured outcome remain distinct.
- **Interface gap found and corrected:** Tariff & Settlement previously exposed BILL_GRADE, PROJECT_ASSUMPTION and FAILED in one overall-status field, while the CostResult proposal separates result status, evidence status, settlement readiness, request lifecycle and replay state. Its resolver states (UNKNOWN/CONFLICT) also lacked explicit projection rules. Tariff design §4/§7 now maps COMPLETE/PARTIAL/BLOCKED results, BILL_GRADE_ELIGIBLE/SCENARIO_ONLY, PROJECT_ASSUMPTION, FAILED requests and INCOMPLETE_REPLAY independently; it preserves component/resolver reasons and emits no amount on request failure. Forecasting and the application catalog now point to the shared mapping.
- **Still open:** G1 bill/demand/tax/rounding evidence; G2 site capability/response/recovery; G3 graph and metering; G4/G5 measured model/solver evidence; G6 controls; G7 live baseline/M&V; canonical D-065 contract generation and product meaning. This static review closes no Gate and authorizes no production implementation or field control.

No other direct semantic contradiction was found in this bounded review. No application/runtime tests, simulator experiment or Macau-site validation were performed.

## Follow-up — G3 mapping identity and freshness boundary (2026-10-04)

- Cross-reviewed Energy Graph, Telemetry Ingestion/Data Quality, the logical application/event catalog and the prepared G3 site evidence packet.
- Found two interface ambiguities: Energy Graph required an immutable source event identity even though telemetry V1 has no producer event ID; and graph `STALE` conflated expired mapping validity with measurement freshness. The capture identity is now the durable platform raw-capture record reference, while producer/source event identity is optional when an authenticated integration supplies it. Graph mapping results now use `EXPIRED_MAPPING`; telemetry freshness/quality remains a separate dimension.
- Aligned APP-04 and the G3 packet's machine vocabulary (`CONFLICT`, `EXPIRED_MAPPING`) and recorded measurement quality separately.
- This is a static design correction only. No site evidence, runtime contract, source-ID stability, resolver behavior, tests, Gate closure or production schema was validated. G3 remains OPEN; U-027/secure intake and site authorization remain prerequisites.

## Follow-up — PRD, user-flow and vertical-slice alignment for G3 states (2026-10-04)

- Compared PR-02/PR-03 acceptance, Flow A/S-03/S-04, PRD-to-architecture traceability, and VS-003/VS-004 acceptance with the revised Energy Graph/Telemetry status boundary.
- Found the design semantics were separated in the architecture documents, but the product flow and slice acceptance still used the ambiguous phrase “stale mapping.” Updated PR-02, Flow A, S-03/S-04, the traceability matrix and VS-003/VS-004: mapping resolution (including `EXPIRED_MAPPING`) and measurement freshness/quality must be displayed and accepted separately.
- This closes a terminology/traceability gap across product and architecture drafts. It does not establish that users understand these states; WP-4 study evidence, site source behavior, implementation and G3 remain open.

## Nine PRD requirement closure review (2026-10-04)

**Method:** Re-read the current PRD, four user flows/nine screen responsibilities, the requirement-to-architecture/evidence matrix, MVP vertical-slice plan, latest handoff and the implementation status recorded on PR #8. This is a document/source audit; it is not a product acceptance test, user study or full runtime audit.

| PRD | Product/design coverage | Architecture / implementation evidence | Remaining proof before acceptance |
|---|---|---|---|
| PR-01 Tenant/site scope | Roles, site access and screen responsibilities are drafted; role/action matrix is unapproved. | Identity, persistence, security and deployment designs exist; inspected HTTP path has no auth guard. | Owner-approved role/site entitlements; implemented auth and scoped API/jobs/storage; negative isolation and revocation evidence; user validation. |
| PR-02 Data quality/provenance | PRD and Flow A/S-03 now distinguish mapping status from measurement freshness/quality. | Ingestion, persistence and event lifecycle are logical drafts; V1 Schema/TypeScript/Go parity and durable capture/recovery are unproven. | Select contract authority/identity policy; verify real connector behavior, schema parity, durable capture, quality handling and operator comprehension. |
| PR-03 Energy Graph | Flow A/B and S-04 describe separate physical/electrical and settlement/economic views. | Stack-neutral graph design exists; current adapter is unresolved/synthetic; G3 has no validated site graph. | Authorized site topology/point/meter/contract evidence; reviewed mappings, time history, reconciliation and deterministic resolver proof. |
| PR-04 Tariff/bill analysis | Economics flow separates bill reconstruction and scenario/interval views. | Tariff design exists, but G1 remains open and no applicable Golden Bill acceptance is recorded. | Resolve applicable G1 unknowns and Golden Bill evidence; prove effective-date and bill-grade acceptance for declared scope. |
| PR-05 Cost/demand explanation | Component traceability and distinct result kinds are described; monetary presentation remains unsettled. | Cost design is draft; implementation returns synthetic amount/reference only. | Owner decision on monetary view/components; decimal/rounding/aggregation rules; evidence-backed result and user comprehension. |
| PR-06 SHADOW recommendation | Flow C and S-07 keep review separate from execution and measured outcome. | Forecast/optimization and review designs exist; optimizer implementation/evidence is absent, `estimatedValue` is non-authoritative. | G2/G4/G5/G7 evidence, product value semantics, real constraints/baseline and proven SHADOW isolation. |
| PR-07 Evidence/audit/replay | Flow D/S-08 requires pinned versions and visible replay limits. | Replay design exists; inspected evidence persistence is in-memory and replay fixtures are synthetic. | Canonical identity/digest and retention decisions; durable tenant-scoped evidence; replay, correction and backup/restore verification. |
| PR-08 Operator review/authority | Flow C and prototype distinguish review annotation from command authority. | SHADOW lifecycle is designed; controlled-mode/Safety Kernel is review-only and G6 remains open. | Authorized operator usability evidence; attributable durable review; no executable path in MVP; separate G6 proof before any later control scope. |
| PR-09 Integration/run health | PRD and screens show source delay/failure/quality and downstream impact. | Health/recovery designs exist; no site connector, Edge buffering/reconnect or production health projection is evidenced; SLO/support ownership open. | Site connector tests and degraded recovery; approved thresholds, runbooks, ownership, tenant-scoped operations and restore/rollback evidence. |

**Cross-cutting:** QLR-01 localization is a proposed quality requirement with a stack-neutral design. Macau language candidates are not an approved launch set; no target-user language/terminology evidence or locale formatting tests exist. The prototypes are synthetic study stimuli, not accepted UI. Product scope, role priorities, information architecture and visual direction remain owner/customer-validation decisions. The latest core-flow prototype is v0.11; v0.10 is its predecessor, and v0.9 is a separate IA comparison.

**Conclusion:** No PRD requirement is accepted as complete. The product and detailed-design coverage is substantial but remains partial; implementation evidence is a scaffold, not an MVP. The next dependency-ready work is (1) owner review of the product promise, lead role/site hypothesis, monetary semantics and first-release boundary; (2) authorized WP-4 user evaluation; (3) independent domain-Gate and Step 3D/4 evidence; then (4) complete slice-level design approval and implementation. Owner/site authorizations are prerequisites where noted; no customer contact or data intake is implied.
