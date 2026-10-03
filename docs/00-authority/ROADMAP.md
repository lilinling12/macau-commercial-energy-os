# Research-to-Delivery Roadmap

**Authority baseline:** Original G0–G7 Research Gates, Library Research Authority v1.6.2, G6.9-R2 bake-off authority, and current repository handoff.  
**Status date:** 2026-10-04  
**Purpose:** Turn the research framework into a traceable sequence of evidence, decisions, product design, architecture, engineering, MVP, and pilot work. This roadmap organizes existing authority; it does not close a Gate or select a technology stack.

## Project objective

Deliver a Macau commercial-building Energy OS that connects metering, building systems, assets, site topology, customer contracts, and tariff/settlement rules. It should explain economic energy performance, produce safe optimization recommendations, and preserve evidence for replay and measurement and verification.

The first product validates an intelligence loop in shadow/advisory mode. It is not a BMS replacement, a generic dashboard, or an autonomous controller.

## Current verified position

- **G0 — Thesis & Market Rationale:** substantially complete in the original gate register; customer and willingness-to-pay evidence remains a product validation activity.
- **G1 — Macau Tariff & Settlement Foundation:** OPEN. G1.1/G1.2 are complete, but blocking Macau billing and settlement questions remain, including U-001, U-009, U-010, U-011, U-025, and U-026.
- **G2 — Commercial Load Flexibility:** OPEN; public context is documented, but no site-level flexibility envelope, response/rebound or operating boundary is validated.
- **G3 — Energy Digital Twin / Energy Graph:** OPEN; logical design is drafted, but no pilot-site topology, point mapping or settlement mapping has been validated.
- **G4 — Forecasting:** OPEN; no eligible Macau site dataset, leakage-safe baseline/candidate evaluation or decision-usefulness evidence is recorded.
- **G5 — Optimization:** OPEN; the optimizer is a data model and no reproducible site/reference candidate-vs-baseline evidence closes the Gate.
- **G6 — Safety & Control:** OPEN / not demonstrated closed. The exit criteria require site-local safety veto/limits, offline fallback, manual override, authenticated and idempotent command handling, audit and replay. U-022 remains OPEN for production command signing and Edge key lifecycle. Step-3C semantic evidence is not production security proof.
- **G6.9-R2 — Technology Stack Bake-off:** Steps 3A–3C complete; pinned framework-native Step 3D pending. C+ is a provisional default, not a measured winner. Step 4 selection follows comparable candidate evidence.
- **G7 — Reference Simulator & Pilot Validation:** ACTIVE / INCOMPLETE. G7.2 live R0 baseline/no-op remains pending and U-017 response/rebound remains open. U-013 cites a v0.9.0 preflight artifact that is absent from the audited repository tree; fixture counts/hashes are not independently reviewable here.
- **Repository structure:** the numbered documentation structure is in place. Existing Node/NestJS code is Candidate B implementation evidence only; it does not close the bake-off.

See `docs/00-authority/handoff/CURRENT.md` and the individual Gate records for the authoritative status.

## Gate plan

Gate exit criteria below are execution checks derived from the research objectives. Where Library authority already supplies a numeric or hard criterion, that criterion remains controlling. A gate may only be marked complete when its evidence and decision are recorded in the Authority registers and CURRENT snapshot.

| Gate | Research question and required result | Dependency / status |
|---|---|---|
| **G0 Thesis & Market Rationale** | Confirm the Macau commercial-energy problem, target buyer, economic pain, and why an Energy OS is needed. Preserve assumptions separately from customer evidence. | Substantially complete; continue customer discovery alongside G1. |
| **G1 Tariff & Settlement** | Resolve applicable tariff/contract/measurement rules; obtain at least two real Golden Bill cases; reconstruct bills to the Authority target of ≤0.5% with zero unexplained adjustment; register contract-specific exceptions. | OPEN and economically blocking. Complete before claiming bill-grade savings or closing settlement semantics. |
| **G2 Commercial Load Flexibility** | For each in-scope asset, document response speed, duration, operating constraints, comfort/SLA effects, rebound, controllability, and the economic mechanism, with source or site evidence. | Evidence needed before assigning realizable flexibility value. |
| **G3 Energy Digital Twin / Energy Graph** | Demonstrate linked Physical, Electrical Topology, Settlement, and Economic Twins with stable identity, provenance, effective dating, tenant/site boundaries, and explicit mappings between measured and settled quantities. | Depends on asset and settlement evidence from G1/G2; schema may evolve while unknowns remain explicit. |
| **G4 Forecasting** | Define load/cooling/PV/occupancy/EV/Pu-risk forecasts only where data supports them; evaluate errors by economic impact and decision usefulness, not generic ML scores alone. | Requires G1 tariff semantics and G2/G3 data definitions. |
| **G5 Optimization** | Define day-ahead (24–48 h), intraday (5–15 min receding horizon), and local fast-limit responsibilities; compare recommendations against a reproducible baseline and account for uncertainty and constraints. | Requires G1–G4 outputs; begin in simulation/shadow mode. |
| **G6 Safety & Control** | Verify policy evaluation, Safety Kernel veto, site-local limits, offline fallback, manual override, authenticated/idempotent commands, audit, and replay. AI/optimizer may propose but cannot bypass safety authority. | Required before any controlled deployment; autonomous control is not authorized by the MVP. |
| **G7 Simulator & Pilot Validation** | Validate reference cases and attribution; distinguish simulation evidence from Macau-site evidence. For live R0, complete the required fresh baselines and no-op identity trajectory before interpreting control response. | Parallel workstream. G7.2 remains pending; U-017 must be resolved for SAT/CHWS response and rebound claims. |
| **G6.9-R2 Technology Bake-off** | Execute pinned, framework-native Candidate A/B/C+ integrations on common contracts and shared services; inject workflow/worker, broker, database, and Edge failures; gather comparable reliability, performance, and controlled AI-engineering-task evidence. Apply hard safety gates before the published decision rule. | Parallel technical workstream. Step 3D pending; Step 4 decision only after comparable results. |

### Cross-gate execution order

1. Keep G0 customer validation active while closing **G1** billing and settlement blockers.
2. Collect **G2** asset-flexibility evidence and refine **G3** Energy Graph semantics; do not encode unsupported Macau assumptions as defaults.
3. Use stable G1–G3 contracts/data to complete **G4** forecasting and **G5** shadow optimization.
4. Complete **G6** safety proof before enabling any field command path.
5. Run **G7** reference simulation and live pilot evidence in parallel where prerequisites permit; keep simulated and live evidence separate.
6. Run **G6.9-R2 Step 3D/4** in parallel with domain research. A stack decision may change implementation boundaries, not domain semantics.
7. Convert only passed and approved Gate outputs into product scope, architecture decisions, engineering tasks, and implementation.

## Product and architecture design deliverables

- Product definition: `docs/02-product/PRODUCT-DESIGN.md`
- Owner decision summary: `docs/02-product/OWNER-DECISION-SUMMARY-v0.1.md` (**review aid; no product or technology choice approved**)
- Product requirements: `docs/02-product/PRD-v0.1.md` (**research-derived draft; customer validation and approval remain pending**)
- Product information architecture, primary flows and screen requirements: `docs/02-product/USER-FLOWS-AND-IA-v0.1.md` (**draft; target-user validation remains pending**)
- Clickable product interaction prototype v0.4: `docs/02-product/prototype/v0.4/index.html` (**synthetic demo; coherent SVG navigation icons, truthful read-only site context, and phone-sized trend presentation backed by text/table; not customer/usability validated or WCAG-conformance tested**)
- Prior prototype v0.3, retained for comparison: `docs/02-product/prototype/v0.3/index.html` (**synthetic demo; corrects data-health count, synchronizes breadcrumb, and adds chart text/table alternative; not customer/usability validated**)
- Prior prototype v0.2, retained for comparison: `docs/02-product/prototype/v0.2/index.html` (**synthetic demo; separates cost-result types and review/outcome states; not customer/usability validated**)
- Prior prototype v0.1, retained for comparison: `docs/02-product/prototype/v0.1/index.html` (**synthetic demo; not customer/usability validated**)
- Logical system architecture and technology decision states: `docs/03-architecture/ARCHITECTURE-DESIGN.md`
- VS-001 detailed design draft, explicitly SHADOW-only and non-authorizing: `docs/03-architecture/detailed-design/VS-001-DETAILED-DESIGN-v0.1.md`
- Candidate MVP vertical-slice sequence and acceptance evidence: `docs/05-mvp/vertical-slices/MVP-VERTICAL-SLICE-PLAN-v0.1.md` (**draft; VS-001 remains incomplete, product scope and technology approval pending**)
- Tariff & Settlement Engine detailed design v0.1 (stack-neutral proposal; blocked from bill-grade implementation by G1 unknowns): `docs/03-architecture/detailed-design/TARIFF-SETTLEMENT-DETAILED-DESIGN-v0.1.md`
- Energy Graph detailed design v0.1 (stack-neutral proposal; site topology and G3 acceptance evidence pending): `docs/03-architecture/detailed-design/ENERGY-GRAPH-DETAILED-DESIGN-v0.1.md`
- Telemetry Ingestion & Data Quality detailed design v0.1 (stack-neutral proposal; contract parity, identity and site-policy evidence pending): `docs/03-architecture/detailed-design/TELEMETRY-INGESTION-AND-DATA-QUALITY-DETAILED-DESIGN-v0.1.md`
- Recommendation and Operator Review detailed design v0.1 (stack-neutral SHADOW lifecycle proposal; product semantics and G6 authorization remain open): `docs/03-architecture/detailed-design/RECOMMENDATION-AND-OPERATOR-REVIEW-DETAILED-DESIGN-v0.1.md`
- Cost Analysis and Evidence Replay detailed design v0.1 (stack-neutral; bill-grade G1 evidence and canonical replay contract remain open): `docs/03-architecture/detailed-design/COST-ANALYSIS-AND-EVIDENCE-REPLAY-DETAILED-DESIGN-v0.1.md`
- Forecasting and Optimization detailed design v0.1 (stack-neutral; G4/G5 evidence and decisions remain open): `docs/03-architecture/detailed-design/FORECASTING-AND-OPTIMIZATION-DETAILED-DESIGN-v0.1.md`
- Deployment, Operability and Recovery detailed design v0.1 (stack-neutral; deployment mode, SLOs and recovery objectives remain open): `docs/03-architecture/detailed-design/DEPLOYMENT-OPERABILITY-AND-RECOVERY-DETAILED-DESIGN-v0.1.md`
- PRD-to-architecture requirement traceability, design-gap matrix, and G0–G7/G6.9 Gate-to-delivery map: `docs/03-architecture/detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md` (draft; no Gate closure, approval or implementation completion implied)
- VS-001 cost-result and replay-manifest contract proposal: docs/03-architecture/detailed-design/VS-001-RESULT-AND-REPLAY-CONTRACT-PROPOSAL-v0.1.md (draft; no schema or stack decision implied)
- VS-001 identity and tenant authorization detailed design: docs/03-architecture/detailed-design/VS-001-IDENTITY-AND-TENANT-AUTHORIZATION-DESIGN-v0.1.md (draft; identity provider, roles and implementation remain open)
- Gate-specific evidence and outcomes: `docs/01-research/gates/`
- Single current handoff and next task: `docs/00-authority/handoff/CURRENT.md`

The product and architecture documents distinguish confirmed research from hypotheses and provisional technology candidates. They do not claim the UI has been usability-tested or that a production stack has been selected. PRD-v0.1 formalizes traceable requirements, but does not replace customer discovery, interaction design, detailed architecture, or approval of product scope.

## Next work packets

### WP-0 — Owner review and decision baseline
Use `docs/02-product/OWNER-DECISION-SUMMARY-v0.1.md` as the immediate review entry point. The owner may approve, revise, or defer each proposed choice; record only choices explicitly confirmed by the owner. Review the initial product promise, lead user/site, visual direction, and initial PV boundary for product discovery/design. Separately resolve the Step 3D comparison boundary and test-only Temporal persistence configuration before freezing its runner. These experiment choices do not select the frontend or production stack.

**Exit evidence:** owner responses are recorded in the relevant PRD/decision record and reflected in the Step 3D readiness plan/manifest; deferrals remain explicit blockers rather than inferred approval. Product discovery and evidence gathering that do not depend on a decision may continue in parallel.

### WP-1 — Close G1 evidence blockers
Obtain authoritative tariff and meter-window answers, anonymized real bills with matching meter data, tax/rounding rules, and written clarification for cross-site PV settlement and the official PV-count discrepancy. Update U-items, evidence register, tariff rules, and Golden Bill fixtures. Do not recognize remote PV generation as a customer's bill credit without contractual and settlement evidence.

### WP-2 — Execute G6.9-R2 Step 3D and Step 4
Build the pinned Linux x86-64 environment and run Candidate A/B/C+ with the same contracts and workload. Record exact versions, commands, raw results, failures, retries, and reviewer judgments. Do not call a winner until all hard gates pass and the authority decision rule is met.

### WP-3 — Advance G7.2 live R0 safely
Complete the required fresh live baseline runs and live no-op identity trajectory with approved point bindings, run manifest, telemetry quality, and site authorization. Keep SAT/CHWS response and rebound claims open until U-017 is resolved.

### WP-4 — Validate and complete product design
Use G0/G2/G3 evidence to refine in-scope assets and customer workflows. PRD-v0.1 and USER-FLOWS-AND-IA-v0.1 are research-derived drafts, not customer-approved scope. Validate target users, buying authority, willingness to pay, integration burden, task frequency, and acceptable bill/savings evidence with Macau building operators and finance/energy stakeholders. Validate the role/task hypotheses, six-step product workflow, information architecture, permission/approval flows, and screen-state requirements in USER-FLOWS-AND-IA-v0.1; produce interview/evidence records and reviewable screen prototypes with accessibility and responsive behavior. Update PRD and PRODUCT-DESIGN from evidence rather than filling gaps with assumptions.

**Exit evidence:** named user/customer evidence; decisions or explicitly retained hypotheses for segment, buyer, workflow, and commercial value; usability feedback on primary tasks; versioned product requirements with acceptance criteria and unresolved dependencies.

### WP-5 — Complete architecture and detailed design
Translate approved product requirements and passed Gate outputs into component-level designs. The first bounded draft now covers VS-001 in `docs/03-architecture/detailed-design/VS-001-DETAILED-DESIGN-v0.1.md`; it is not yet approved or production-authoritative. Extend detailed design across all validated MVP journeys and specify module boundaries, API/event/data contracts, persistence and migrations, workflow state machines, security/threat and key-lifecycle design, tenant isolation, failure/recovery semantics, deployment topology, SLO/observability, operations and rollback. Keep provisional stack choices replaceable until G6.9-R2 Step 4 records a formal decision.

**Progress evidence:** VS-001 has an initial component-level draft. Stack-neutral detailed-design drafts now cover Telemetry Ingestion/Data Quality, Energy Graph, Tariff & Settlement, Cost Analysis/Evidence Replay, Forecasting/Optimization, Recommendation/Operator Review, and Deployment/Operability/Recovery. They specify domain/data flows, evidence states, forecast uncertainty, optimization feasibility, replay, tenant/security boundaries, health/readiness semantics, failure recovery and release/restore evidence. Deployment mode, SLO/RPO/RTO, provider and operations ownership remain undecided; the design does not claim G6-08/09/10 closure. G1/G3/G4/G5 evidence and product semantics remain open; recommendations remain SHADOW-only. The PRD has a requirement-to-architecture gap matrix and preliminary static source/tree audit. These are reviewable drafts; runtime, full-module, security and pilot audits remain outstanding.

**Exit evidence:** approved architecture decisions linked to bake-off and Gate evidence; detailed design covers every validated MVP path and failure mode; contracts and acceptance tests are traceable; G6 security unknowns and operational authorization are explicit.

### WP-6 — Authorize and implement MVP by vertical slice
Only after relevant research and architecture decisions pass, create implementation work packets tied to an approved Decision Record, contracts, acceptance evidence, rollback behavior, and explicit scope. Use the candidate, technology-neutral increment sequence in `docs/05-mvp/vertical-slices/MVP-VERTICAL-SLICE-PLAN-v0.1.md` to order tenant/site access, source health/ingestion, Energy Graph, evidence/replay, tariff/cost, SHADOW recommendation/review, and pilot M&V. VS-001 is the integration-level target, not an accepted implementation: the current source audit records scaffold gaps. Retain the existing Node/NestJS path as Candidate B implementation evidence unless Step 4 selects it. No technology-specific production slice is ready until G6.9-R2 Step 4 and the required owner/product decisions are recorded.

**Exit evidence:** every approved MVP requirement maps to merged implementation and successful acceptance evidence; operator-facing flows work end-to-end; required positive, negative, authorization/isolation, failure and recovery cases are evidenced; unresolved research blocks bill-grade claims or device commands; customer/site and owner sign-off plus operational handoff are recorded.

### WP-7 — Verify, pilot, and make deployment decision
Complete product, integration, security, reliability, performance and G7 validation at the level required for the pilot. Deploy only under site authorization; preserve run manifests and evidence; train operators; measure agreed user, safety, service, and economic outcomes.

**Exit evidence:** customer-approved pilot protocol and baseline; successful deployment and operational handoff; reproducible results against agreed acceptance criteria; documented expand/remediate/stop decision.

## Gate reporting standard

Every Gate update must state: (1) question researched, (2) evidence and provenance, (3) changed conclusions, (4) decision and approver, (5) unresolved questions, (6) product/model/architecture impact, (7) Authority files updated, and (8) next dependency-ready Gate or work packet.

## Cross-cutting capability: continuous AI research and AI Coding

This capability applies across G0–G7 and G6.9-R2; it is not a new domain Gate and does not replace the original research sequence. The goal is for a new conversation or AI agent to continue from durable project state without requiring the prior chat.

- **Continuity authority:** `docs/00-authority/handoff/CONTINUATION-PROTOCOL.md`, `CURRENT.md`, `CONTINUE-PROMPT.md`, and the task packet.
- **Research process:** question and Gate → primary evidence with provenance → synthesis and uncertainty → Decision/Open Question update → product/architecture impact → next dependency-ready packet.
- **Coding process:** approved Authority → explicit task packet → bounded change → required validation and evidence → human review → updated handoff.
- **Persistent memory:** write conclusions, assumptions, rejected hypotheses, source provenance, decisions, and next steps into versioned repository files. Do not rely on conversation history as the only record.
- **Governance boundary:** AI may research, draft, implement, and validate within scope; a person reviews Authority changes, architecture decisions, and operational authorization.

This workstream is now documented by the cross-conversation protocol and reusable task packet template. Its effectiveness should be checked by using them at the start and end of each subsequent research or coding task.
