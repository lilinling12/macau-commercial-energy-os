# Product and Architecture Review Packet v0.1

**Status:** Review draft; no owner decisions recorded.
**Prepared:** 2026-10-03
**Related work:** PR #8 product/architecture drafts, G6.9-R2 bake-off, G1/G6/G7 research gates.
**Purpose:** Put the current product and architecture assumptions in one reviewable place before they become baselines. This packet requests review; it does not record approval.

## 1. Decision status

The repository contains useful research-derived product and architecture drafts. Their existence does not mean the product scope, interaction design, technology stack, detailed design, or production architecture has been approved.

- Product roles and workflows are hypotheses pending customer/user validation.
- React + TypeScript is a provisional frontend proposal, not an approved framework choice.
- TypeScript/Go hybrid, Temporal, PostgreSQL + Timescale, NATS JetStream, Python, Go Edge, and Wasm/WASI remain the stated candidate directions with the exact status recorded in the G6.9-R2 and related authority.
- Existing Node/NestJS implementation is Candidate B evidence, not a technology decision.
- Next.js is not an approved choice.
- G6 remains OPEN; the detailed designs do not authorize device control or close security/safety evidence.

## 2. Product proposition for review

### Research-derived proposal

Macau Commercial Energy OS is proposed as an energy-intelligence and orchestration product for commercial buildings and sites. It joins metering and building-system data with site/asset topology, customer contracts, tariffs, and settlement evidence. Its initial value proposition is traceable cost intelligence and explainable, shadow-mode recommendations, with evidence that can be replayed and compared.

This proposal excludes autonomous control, unsupported bill-grade claims, and treating remote PV as another building's bill credit without settlement evidence. These boundaries follow the current research authority and remain subject to product-owner review.

### Users and workflow hypotheses

The draft assumes facilities/energy managers, finance or asset owners, site operators, and integration/service partners. The primary loop is: connect a site → understand data and topology → resolve tariff/cost → review exposure and uncertainty → inspect a shadow recommendation → preserve evidence and replay.

These are not yet validated role rankings or final navigation. Discovery must confirm who buys, who uses, which job occurs most often, and which evidence is trusted.

### Product decisions requested

1. Is the proposed initial product promise (traceable cost intelligence + shadow-mode recommendation + replayable evidence) the right first product?
2. Which user and site type should lead the first workflow and pilot discovery? Current roles/sites are hypotheses; please name a preferred lead role/site or request more evidence before choosing.
3. Are there product capabilities or exclusions that should change before detailed design proceeds?

## 3. UI/UX Pro Max search evidence and interpretation

The installed Pro Max skill was used with:

- Design-system query: enterprise energy management dashboard.
- UX query: dense operational data dashboard status hierarchy.
- Chart query: energy cost demand time-series dashboard.

The design-system query “enterprise energy operations dashboard dense analytical workspace” returned a **Real-Time / Operations Landing** pattern and **Glassmorphism** style, a dark/neutral palette with semantic status colors, and Fira Code/Fira Sans. UX Pro Max query results reinforce visible focus, semantic controls, loading/empty/disabled feedback, and clear action states. Its time-series chart guidance calls for solid actual versus dashed forecast lines, direct labels, named uncertainty, and visible table/narrative alternatives. These are candidate heuristics; no palette, font or framework is approved.

These are search results, not user evidence. The landing-page pattern is not automatically appropriate for the signed-in operations workspace. The frosted/blurred glass style may reduce clarity or contrast in sustained, information-dense energy analysis; it should not be applied without prototyping and accessibility checks. Font-family and palette suggestions also require fit review. No stack-specific search was run because the frontend framework is unapproved.

### Visual directions for owner review

| Direction | Description | Strengths to evaluate | Risks/questions |
|---|---|---|---|
| **A. Clear operational workspace** | Light-first neutral surfaces; restrained brand accents; clear typography; strong hierarchy for cost, freshness, uncertainty, and exceptions; optional dark mode later. | Long-session readability, dense tables/charts, clear evidence provenance, lower dependence on decorative effects. | Does it feel sufficiently distinctive and suited to an Energy OS? |
| **B. Dark operations console** | Dark neutral canvas with restrained semantic status colors; high-contrast data panels; clear separation between live, stale, and synthetic evidence. Avoid heavy blur by default. | May suit control-room environments and reduce glare in some settings; aligns partly with Pro Max's dark operations suggestion. | Validate contrast, daylight use, print/export, and role preferences; dark mode must not hide data quality. |
| **C. Expressive layered interface** | Selective depth/translucency for navigation or overlays, with opaque reading surfaces for charts, tables, and evidence. | Could provide modern brand character while limiting blur to low-risk surfaces. | Requires performance and contrast checks; easy to overuse and make the interface dated or decorative. |

**Working recommendation for review, not approval:** prototype A as the baseline and use C only as a limited visual accent if it improves orientation. Keep B available as a testable alternative for control-room users. Validate with actual target users before freezing a design system.

### Prototype iteration evidence

Prototype v0.2 lets reviewers switch among bill reconstruction, interval assessment, and baseline comparison; the bill view states why it is blocked without Golden Bill/G1 evidence, the comparison view withholds any delta without a validated baseline, and the interval amount remains synthetic. Recommendation review adds a dismissed disposition and separates review from measured outcome. Prototype v0.3 corrects the data-health review count, synchronizes the breadcrumb with the active view, and adds a text summary plus an expandable sample table for the synthetic trend chart. These iterations improve design reviewability only; they are not customer-tested product behavior, and they do not approve a visual direction or frontend framework.

### Interaction principles to evaluate

- Make data provenance visible: measurement/source, time range, freshness, coverage, and uncertainty.
- Use explicit system states and recovery: loading, empty, partial, stale, failed, permission denied, and retry.
- Distinguish actual, forecast, recommendation, and executed outcome in labels and chart treatment, not color alone.
- Keep serious actions under human approval; make shadow/advisory state unmistakable.
- Fit navigation and layout to validated tasks and device context. Do not copy old dashboard conventions or force a mobile-first shape.
- Review keyboard navigation, focus visibility, contrast, chart alternatives, reduced motion, and responsive behavior. WCAG 2.2 AA is a proposed evaluation target pending owner review.

Reference material: UI/UX Pro Max local search; W3C WCAG 2.2 (https://www.w3.org/TR/WCAG22/); Material Design 3 foundations; Nielsen Norman Group usability heuristics. These are reference points, not visual templates. WCAG 2.2 AA is the proposed accessibility evaluation baseline, not a completed conformance claim.

## 4. Architecture decision status for review

### Logical boundaries

The current draft separates site Edge and local safety from cloud intelligence, cost/settlement, forecasting/optimization, evidence/replay, and human approval. This is a research-derived boundary proposal. Please review whether these responsibilities and trust boundaries fit the intended product and operating model.

### Technology choices

| Concern | Current recorded state | Review status |
|---|---|---|
| Frontend | React + TypeScript was proposed in provisional architecture notes. | Not approved; confirm framework only after product surfaces and bake-off implications are clear. |
| Cloud-core topology | Candidates A, B, C+ under G6.9-R2. C+ is a provisional default; Node/NestJS is existing Candidate B implementation evidence. | Do not call a winner before Step 3D/4 evidence and Decision Record. |
| Workflow | Temporal candidate. | Candidate, not final selection. |
| Temporal persistence for Step 3D | Temporal's actively tested PostgreSQL range is 13–16; the experiment pack requires PostgreSQL 18 + TimescaleDB for common candidate infrastructure but does not specify Temporal persistence backend/version. A separate PostgreSQL 16 service is proposed for all candidates. | Owner decision required before runner freeze: approve this additional shared test-only service, or require a different supported configuration to be validated first. This does not decide the production database architecture. |
| Data | PostgreSQL + Timescale evaluation baseline. | Baseline for evaluation, not yet final operational decision. |
| Eventing | NATS JetStream candidate. | Candidate, not final selection. |
| Optimization/AI | Python responsibility proposal. | Confirm module boundary and workload evidence in architecture review. |
| Site Edge | Go responsibility proposal including local safety boundary. | Confirm through safety, deployment, protocol, and failure evidence; G6 remains open. |
| Plugin isolation | Wasm/WASI future direction. | Future option; outside first MVP absent a validated requirement. |

The C+ candidate names a thin Bun/Hono/TypeScript product BFF/UI, while the layer proposal separately names React + TypeScript as a possible frontend. Clarify whether React is a separate browser UI served through a thin BFF, or whether the candidates intentionally compare different UI approaches. Define the product/API/BFF/browser-UI boundary consistently before the bake-off; the Step 3D readiness plan records this ambiguity. The next stack decision depends on the pinned G6.9-R2 Step 3D/4 process. Product-owner review of intended product boundaries can proceed in parallel, but it must not predetermine bake-off results.

## 5. Detailed-design readiness and gaps

The repository has detailed-design drafts for VS-001, result/replay, identity/tenant authorization, and PRD-to-architecture traceability. They are not production-ready merely because they are detailed.

Before implementation of a design area is treated as ready, resolve or explicitly scope:

- approved product workflow and acceptance evidence;
- recommendation economics meaning: absolute expected cost versus change against a baseline; the current RecommendationV1 number is not monetary truth under D-026, and any V2 migration must reference an eligible immutable assessment;
- canonical request/event/result/evidence contracts and versioning;
- tenant/site authorization derived from authenticated identity, not caller-supplied body fields;
- storage, retention, replay determinism, idempotency, failure and recovery;
- observability, audit, migration/rollback, and operational ownership;
- which Gate evidence is a prerequisite and what may remain out of scope for shadow mode.

No change here closes G1, G6, G6.9-R2, or G7.2. No device control is authorized.

### Contract authoring and generated bindings — research proposal, decision open

D-065 requires contract-driven boundaries and generated OpenAPI / Protobuf / JSON Schema bindings; it does not establish one canonical authoring format or generator toolchain. The current CostResult/ReplayManifest and identity designs remain proposals, and their domain semantics must be settled before schema code generation is treated as canonical.

| Candidate | Best fit in this product | Main constraints to prove |
|---|---|---|
| OpenAPI 3.1 | HTTP API description plus JSON request/response schemas, documentation and API-client generation. Its Schema Object dialect builds on JSON Schema Draft 2020-12 with OAS-specific vocabulary. | Prove the same source can generate maintainable TypeScript and Go clients/models, enforce intended validation identically, and represent non-HTTP event contracts without an awkward API-centric wrapper. |
| JSON Schema Draft 2020-12 | Language-neutral JSON payload validation for events, results, evidence and fixtures; current contract files can seed experiments. | Select and pin separate TypeScript/Go validators and code generators; compare their support for dialects, references, unions, unknown fields and decimal strings. The format keyword is annotation by default unless assertion behavior is explicitly required/configured, so timestamp and other format checks need an explicit cross-runtime rule. |
| Protocol Buffers | Typed service/event contracts with generated bindings and a compact binary wire format; official tooling includes Go output. | Prove the TypeScript generator/runtime and JSON-facing boundary, field presence/default semantics, evolution rules and operational fit. Never hash serialized Protobuf bytes as a replay identity: serialization is not canonical; define a semantic canonicalization layer if stable digests are required. |

**Evidence gate before choosing:** create one representative contract slice from the approved domain semantics and generate/use it in the actual candidate runtimes. Pin compiler, plugin, validator and generator versions. Compare (1) Go and TypeScript type generation, (2) required/optional/null/unknown-field behavior, (3) oneOf/discriminator and enum evolution, (4) money as decimal strings with currency and scale rules, (5) timestamp/timezone and invalid-format rejection, (6) HTTP and event transport representation, (7) deterministic semantic digest behavior, (8) error quality, build friction, dependency footprint and supply-chain maintenance. Run identical positive and negative fixtures through both language paths and retain generated diffs plus results as bake-off evidence.

**Current recommendation for the experiment only:** include JSON Schema Draft 2020-12 and OpenAPI 3.1 as competing JSON-contract paths, and Protobuf as a separate typed-wire path. Do not select a production canonical format from standards coverage alone. A possible layered outcome (OpenAPI for HTTP descriptions, JSON Schema for shared payload validation, Protobuf only for a demonstrated internal transport need) is a hypothesis to test, not the chosen architecture.

Official references: [OpenAPI 3.1.2](https://spec.openapis.org/oas/v3.1), [JSON Schema Draft 2020-12 Core](https://json-schema.org/draft/2020-12/json-schema-core), [JSON Schema Validation](https://json-schema.org/draft/2020-12/json-schema-validation), [Protocol Buffers proto3 guide](https://protobuf.dev/programming-guides/proto3/), [Protobuf field presence](https://protobuf.dev/programming-guides/field_presence/), [Protobuf serialization is not canonical](https://protobuf.dev/programming-guides/serialization-not-canonical/).

## 6. Decision queue — what is needed now and what must wait

This queue separates owner choices that unblock discovery/design from choices that require completed research. A response can select an option, modify it, or explicitly defer it. “Defer” keeps the corresponding baseline provisional and records the dependency; it is not approval by silence.

| Decision | When | Choices to review | What the choice authorizes |
|---|---|---|---|
| **Initial product scope and promise** | Directional review now; validate in WP-4 | (A) traceable tariff/cost intelligence + shadow recommendations + replay evidence; (B) bill reconciliation and cost intelligence first, defer recommendations; (C) revise the promise. | Sets the research focus for PRD and user interviews. It does not validate demand or authorize bill-grade claims. |
| **Lead user and pilot-site hypothesis** | Select a hypothesis for discovery now; validate before baseline | (A) hotel/resort energy or facilities manager; (B) commercial property finance/asset owner; (C) site operations/control-room lead; (D) name another role/site; (E) defer ranking and compare these in discovery. | Sets recruitment and workflow-prototype priorities. It does not commit to a customer or pilot. |
| **Product operating boundary** | Review now | Keep MVP telemetry, economics, explanation, shadow recommendation, and evidence/replay; exclude direct device control and unsupported remote-PV bill credits; or specify changes. | Allows product workflow and acceptance criteria to be refined while G1/G6/G7 remain open. |
| **Step 3D Temporal persistence service** | Must be resolved before freezing the common runner | (A) approve adding one shared PostgreSQL 16 service for Temporal persistence while candidate app services use PostgreSQL 18 + TimescaleDB; (B) defer Step 3D until another Temporal-supported topology is researched and pinned; (C) request a specific alternative. | Authorizes only the bake-off runner configuration. It does not select production database or application architecture. |
| **Architecture boundaries** | Review now, finalize with evidence | Confirm or revise cloud intelligence vs site-local Edge/Safety Kernel, human approval boundary, and evidence/replay as a core product capability. | Sets logical responsibilities for detailed design. Technology frameworks remain unselected. |
| **Visual direction and interaction system** | After target-user tasks are recruited and prototype is tested | Keep A (clear operational workspace) as a prototype baseline; compare A/B/C through usability and accessibility evidence; or request another direction. | Guides the next prototype iteration only; does not establish final visual identity. |
| **Production stack and deployment model** | Defer until G6.9-R2 Step 3D/4 and product/operations evidence | No winner selected. Review measured candidate results, product requirements and operating costs before Decision Record. | A later, explicit owner-approved technology and deployment baseline. |

### Approval boundary

The next design work can advance on directional product scope and logical trust/module boundaries. A production architecture decision requires both the bake-off decision rule and owner review. G1 bill-grade functionality, G6 command execution, G7 field claims, customer/site selection, and deployment authorization each retain their own evidence and approval gates.

## 7. Proposed review sequence

1. Review the product promise, first user/site hypothesis, and exclusions.
2. Review visual direction A/B/C and interaction principles. Treat prototypes as synthetic until user-tested.
3. Confirm product boundaries and the architecture questions to carry into G6.9-R2; do not prematurely select the stack.
4. Decide whether Step 3D may add a shared PostgreSQL 16 Temporal persistence service while keeping PostgreSQL 18 + TimescaleDB as the common candidate application database. The pack specifies the latter and leaves Temporal persistence unspecified; this is a bake-off environment choice, not production approval.
5. After those reviews, revise the PRD, user flows, prototype, logical architecture, and relevant ADRs to record accepted decisions and remaining unknowns.
6. Confirm the first detailed-design slice and its acceptance evidence; then implement against that approved packet.

## 8. Owner response record

No response or approval is recorded in this draft.

- Product promise:
- Lead user/site:
- Visual direction:
- Product changes/exclusions:
- Architecture boundaries:
- Technology decisions deferred to bake-off:
- Recommendation economic display (absolute expected cost / baseline-relative change / omit until evidence):
- Step 3D shared Temporal persistence service (approve PG16 addition / request supported alternative / defer):
- Detailed-design slice to prioritize:
- Date / reviewer:
