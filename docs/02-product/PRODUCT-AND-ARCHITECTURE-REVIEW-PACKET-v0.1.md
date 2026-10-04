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

This proposal excludes autonomous control, unsupported bill-grade claims, and treating remote PV as another building's bill credit without settlement evidence. The amended electricity concession contract effective 2026-01-01 contemplates private self-generated distribution only within the same land parcel and with prior written SAR authorization; this does not establish cross-parcel customer bill credits. These boundaries follow the current research authority and remain subject to product-owner review.

### Users and workflow hypotheses

The draft assumes facilities/energy managers, finance or asset owners, site operators, and integration/service partners. The primary loop is: connect a site → understand data and topology → resolve tariff/cost → review exposure and uncertainty → inspect a shadow recommendation → preserve evidence and replay.

These are not yet validated role rankings or final navigation. Discovery must confirm who buys, who uses, which job occurs most often, and which evidence is trusted.

### Product decisions requested

1. Is the proposed initial product promise (traceable cost intelligence + shadow-mode recommendation + replayable evidence) the right first product?
2. Which user and site type should lead the first workflow and pilot discovery? Current roles/sites are hypotheses; please name a preferred lead role/site or request more evidence before choosing.
3. Are there product capabilities or exclusions that should change before detailed design proceeds?
5. D-003 currently prioritizes HVAC/chiller as the first controllable asset, but the G2 Gate and Macau evidence review classify this as a pilot-priority hypothesis; public evidence does not establish any site's flexible capacity, control access, service/comfort limits or rebound. Should the product retain HVAC/chiller as a working hypothesis until a named site's G2 evidence exists, compare it with ESS/other loads during discovery, or revisit the priority after site selection? Until validated, do not describe it as a confirmed pilot asset or claim dispatchable capacity/savings.
4. How should SHADOW recommendations express economic effect? Current RecommendationV1 `estimatedValue` is not monetary truth. Review three options: (A) modeled absolute expected cost over a named horizon; (B) modeled change against an explicitly comparable baseline; or (C) defer a currency amount until an eligible immutable cost assessment exists. **Interim recommendation:** use C for the recommendation card, while allowing a separately evidenced cost assessment to be opened and explained. Any modeled effect must remain distinct from realized savings. The selected meaning must name its assessment scope, horizon, baseline, uncertainty and provenance before Recommendation/CostResult contracts or UI labels are frozen.

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

Prototype v0.2 lets reviewers switch among bill reconstruction, interval assessment, and baseline comparison; the bill view states why it is blocked without Golden Bill/G1 evidence, the comparison view withholds any delta without a validated baseline, and the interval amount remains synthetic. Recommendation review adds a dismissed disposition and separates review from measured outcome. Prototype v0.3 corrects the data-health review count, synchronizes the breadcrumb with the active view, and adds a text summary plus an expandable sample table for the synthetic trend chart. Prototype v0.4 replaces mixed Unicode navigation glyphs with one decorative SVG icon style, removes a one-option nonfunctional site selector, and preserves the synthetic trend's explanatory summary/table when phone-sized chart labels are hidden. These iterations improve design reviewability only; they are not customer-tested product behavior, and v0.4 has not undergone WCAG conformance testing. No visual direction or frontend framework is approved.

**Prototype v0.4 static review:** CSS foreground/background pairs were sampled from the source: body text 15.86:1; muted text 5.48:1; chart axis text 4.87:1; focus outline on white 4.72:1; semantic status labels 5.77:1–7.68:1; demo/alert text 7.47:1–9.00:1. This supports the selected sampled combinations against the 4.5:1 normal-text threshold; it does not cover every rendered component/state, transparency/composited colors, browser zoom, keyboard/screen-reader behavior, or all responsive layouts. v0.4 has not received rendered browser, assistive-technology, real-device, or WCAG-conformance testing.

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

The current draft separates site Edge and local safety from cloud intelligence, cost/settlement, forecasting/optimization, evidence/replay, and human approval. The new logical runtime view in `docs/03-architecture/ARCHITECTURE-DESIGN.md` makes browser/API, application core, ingress/async processing, persistence, AI jobs and Edge responsibilities reviewable without prescribing process counts or deployment placement. It also makes durable raw capture before downstream event publication an explicit invariant; crash recovery/outbox and redelivery handling remain to be designed. This remains a research-derived proposal. Please review whether these responsibilities and trust boundaries fit the intended product and operating model.

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

The supplied v0.3.0 pack defines A as Bun/Hono/Effect product/API services, B as Node/NestJS/Fastify API/worker, and C+ as Go core plus a thin Bun/Hono/TypeScript product BFF/UI. The canonical flow emits a live UI event; T01 tests a UI contract, T07 tests tenant-filtered live streaming, and the metrics score API/live-stream behavior. None defines browser rendering or a visual/user-task metric. The Step 3D plan therefore recommends equal UI-contract/API/live-stream checks for A/B/C+ while excluding browser rendering and React from the stack score; the scope of C+'s BFF/UI must be clarified. If frontend implementation is to be compared, amend the pack with equivalent browser tasks and separate UI effort metrics. This is an experiment-scope recommendation, not an approved decision; React + TypeScript remains a separate frontend proposal. The production stack still depends on the G6.9-R2 Step 3D/4 evidence and owner-approved Decision Record.

## 5. Detailed-design readiness and gaps

The repository has detailed-design drafts for VS-001, result/replay, identity/tenant authorization, and PRD-to-architecture traceability. They are not production-ready merely because they are detailed.

A stack-neutral proposal for the future command arbitration and Edge Safety Kernel is now available at `docs/03-architecture/detailed-design/COMMAND-ARBITRATION-AND-EDGE-SAFETY-KERNEL-DETAILED-DESIGN-v0.1.md`. It is a review draft; site scope, hazard review, G6 evidence, cryptographic design and owner/security approval remain open. The MVP stays SHADOW/advisory.

Before implementation of a design area is treated as ready, resolve or explicitly scope:

- approved product workflow and acceptance evidence;
- recommendation economics meaning: absolute expected cost versus change against a baseline; the current RecommendationV1 number is not monetary truth under D-026, and any V2 migration must reference an eligible immutable assessment;
- canonical request/event/result/evidence contracts and versioning;
- tenant/site authorization derived from authenticated identity, not caller-supplied body fields;
- storage, retention, replay determinism, idempotency, failure and recovery;
- observability, audit, migration/rollback, and operational ownership;
- which Gate evidence is a prerequisite and what may remain out of scope for shadow mode.

No change here closes G1, G6, G6.9-R2, or G7.2. No device control is authorized.

### Telemetry event identity and duplicate-delivery decision — review draft

The telemetry design now records a transport-independent identity invariant: prefer a producer-stable event ID scoped to an authenticated source; if a connector cannot provide one, assign a platform ingress ID only when raw capture is first durable and preserve it for internal retry/replay. Without stable source evidence, retain distinct later publications rather than collapsing equal value/time/device records. MQTT Packet Identifiers are reusable transport-flow identifiers and are not event identity. This follows the event identity boundaries described in the telemetry detailed-design references; it does not require CloudEvents, define the canonical envelope, or promise exactly-once processing.

**Owner choice still open:** after inventorying the actual pilot meter/BMS/source connectors, decide whether the ingress-ID fallback is acceptable for any connector or whether a particular in-scope source must provide a stable event ID/sequence. Record source-specific exceptions and their duplicate/recovery limits before freezing the V2 telemetry contract or claiming safe deduplication.

### Macau data classification and transfer review — owner/legal dependency

The security threat model now records a dataset-specific review boundary based on Macau Law 8/2005 and GPDP guidance. The law's personal-data definition concerns information relating to identified or identifiable natural persons; building-energy telemetry is not classified wholesale here. Before customer-data intake or production/pilot deployment, identify the actual fields, identities/linkage, purposes, controller/processor roles, storage, sub-processors/support access, retention/deletion and backup/export paths. If in-scope personal data may be transferred outside the MSAR, the responsible privacy/legal owner must assess Articles 19/20 and applicable GPDP conditions for that specific flow. This does not decide a provider, require Macau-only hosting, or provide a legal opinion.

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
| **Recommendation monetary semantics** | Directional review now; finalize before labels/contracts, subject to evidence eligibility | (A) modeled absolute expected cost over a named horizon; (B) modeled change against a comparable named baseline; (C) no currency amount on the recommendation until it references an eligible immutable assessment (interim recommendation). Modeled effect is never realized savings. | Clarifies UI/Recommendation/CostResult semantics; does not make ineligible evidence bill-grade or close G1/G2/G4/G5. |
| **Telemetry event identity and duplicate policy** | After in-scope connector inventory; before telemetry V2/deduplication freeze | Confirm source-scoped, transport-independent identity: prefer a producer event ID; if unavailable, assign platform ID at first durable raw capture; do not merge separate source publications by value/time heuristics. Adjust only when connector evidence supports a source-specific rule. | Authorizes the telemetry identity/deduplication contract for known connectors; does not claim exactly-once delivery or require CloudEvents. |
| **Initial PV scope** | Directional review now; validate specific contracts before any economic claim | (A) include PV host-site generation and producer-side CEM feed-in settlement as distinct, evidence-backed site/economic records, with no credit to another customer by default; (B) keep PV producer/export capability outside the first product increment until a specific host/producer case is validated; (C) identify a specific authorized PPA/allocation case to research. | Sets product discovery and Energy Graph scope; it does not approve cross-site transfer, bill netting, PV savings or any legal arrangement. |
| **D-003 first controllable asset scope** | After a named pilot site and G2 evidence; before claiming controllability or freezing pilot scope | (A) keep HVAC/chiller as a discovery hypothesis; (B) compare it with ESS/other loads during discovery; (C) revisit after site evidence. | Resolves the product/design hypothesis only; no option establishes flexibility, dispatch rights or savings without site measurements and authorization. |
| **Macau data governance and transfer boundary** | Before customer-data intake, external AI processing, or production/pilot deployment | Review actual datasets and flows, identifiability, purpose, controller/processor roles, hosting, support/subprocessor access, retention/deletion, backups and any transfer outside MSAR with the responsible privacy/legal owner. | Authorizes an evidenced data-handling boundary only after case-specific review; this packet is not a legal conclusion or hosting mandate. |
| **Step 3D browser UI scope** | Before runner freeze | (A) follow the current pack’s UI contract/API/live-stream evidence and exclude browser rendering from stack scoring, clarifying C+ BFF/UI scope (recommended); (B) amend the pack to require equivalent browser workflows for all candidates and measure UI effort separately. | Locks bake-off scope only; it does not select React or the production frontend. |
| **Step 3D Temporal persistence service** | Must be resolved before freezing the common runner | (A) approve adding one shared PostgreSQL 16 service for Temporal persistence while candidate app services use PostgreSQL 18 + TimescaleDB; (B) defer Step 3D until another Temporal-supported topology is researched and pinned; (C) request a specific alternative. | Authorizes only the bake-off runner configuration. It does not select production database or application architecture. |
| **Step 3D execution host and trust boundary** | Before runner freeze | (A) use a manually controlled isolated Linux x86_64 VM/harness for the reviewed commit, with fixed resources and Docker; (B) use an owner-restricted clean/ephemeral one-shot Actions runner after proving public-repository and artifact controls; (C) nominate another controlled host. The pack requires a 24-hour mixed-load soak on the same Linux x86-64 runner. Standard hosted jobs cap at 6 hours and each job provisions a new VM, so multi-job orchestration must preserve the same external host and soak state; a persistent self-hosted runner must never execute arbitrary PR code. | Authorizes only the experiment host and execution boundary; does not choose production hosting or deployment topology. Owner for provisioning, cost/resource approval and raw-result retention must be named.
| **Architecture boundaries** | Review now, finalize with evidence | Review the logical runtime view and confirm or revise cloud intelligence vs site-local Edge/Safety Kernel, human approval boundary, evidence/replay as a core product capability, and which responsibilities belong in the product boundary. This confirms logical responsibilities only, not microservice count, hosting, provider or runtime topology. Edge machine-identity lifecycle requirements are drafted, but production signing/key model remains U-022 OPEN. | Sets logical responsibilities for detailed design. Technology frameworks and production key mechanisms remain unselected. |
| **Transport acknowledgement vs platform capture receipt** | Review the logical invariant now; finalize mapping per connector before contract/implementation approval | Distinguish protocol/broker acknowledgement, application capture receipt, and later processing. Issue the application receipt only after the designated raw system of record can recover the record. MQTT PUBACK/PUBREC may acknowledge broker custody before onward delivery; treat it as platform capture only if that broker is deliberately the raw system of record and durability/recovery are proven. HTTP 202 means accepted for processing, not completed. Options: (A) separate capture receipt/status after raw commit (recommended logical behavior); (B) designate a broker as raw system of record after persistence/failover/replay evidence; (C) define connector-specific mapping. | Sets user-visible integration status and VS-003 behavior. It does not claim end-to-end exactly-once effects or authorize heuristic deduplication.
| **Visual direction and interaction system** | After target-user tasks are recruited and prototype is tested | Keep A (clear operational workspace) as a prototype baseline; compare A/B/C through usability and accessibility evidence; or request another direction. | Guides the next prototype iteration only; does not establish final visual identity. |
| **Production stack and deployment model** | Defer until G6.9-R2 Step 3D/4 and product/operations evidence | No winner selected. Review measured candidate results, product requirements and operating costs before Decision Record. | A later, explicit owner-approved technology and deployment baseline. |
| **Security verification baseline** | Review now as an engineering-governance choice | (A) use the candidate tailored OWASP ASVS 5.0.0 control-to-evidence mapping in the Security Threat Model, without claiming a conformance level; (B) nominate another security baseline; or (C) defer until a security reviewer is engaged. | Sets later security-verification scope only. It does not claim controls are implemented or close G6. |

### Approval boundary

The next design work can advance on directional product scope and logical trust/module boundaries. The candidate ASVS mapping still needs scope/reviewer approval before becoming the project's verification checklist. A production architecture decision requires both the bake-off decision rule and owner review. G1 bill-grade functionality, G6 command execution, G7 field claims, customer/site selection, and deployment authorization each retain their own evidence and approval gates.

## 7. Proposed review sequence

1. Confirm a directional product promise, lead-user/site discovery hypothesis, product exclusions and logical cloud/Edge authority boundaries; record every choice as a hypothesis until validated where required.
2. Review monetary labels, initial PV scope and the existing synthetic workflows; preserve G1/G2 evidence gates and revise the PRD/prototype only after the owner response.
3. Resolve Step 3D's UI-comparison boundary and Temporal test-persistence topology before runner freeze; these choices authorize the experiment only.
4. Continue connector inventory, user research, data-governance review and G1/G2/G3/G6 evidence acquisition. Resolve telemetry identity after source inventory, D-003 after site/G2 evidence, and data-flow handling before customer-data intake or external processing.
5. Review detailed designs against confirmed product direction. Keep identity provider, production signing/key handling, security verification scope and deployment model open until the required security/deployment context and G6.9 evidence exist.
6. Update PRD, user flows, prototype, logical architecture, decision register and linked designs from recorded owner decisions; then approve a vertical slice and its acceptance evidence before implementation.

## 8. Owner response record

### Confirmed process and quality constraints

The owner has confirmed these review constraints in the conversation:

- Product scope, interaction design, technical architecture and detailed design must be presented for owner review before they become approved baselines.
- Use the specified UI/UX Pro Max skill when designing or reviewing the interface.
- Ground interface decisions in mature product-design practices and current research; do not keep dated interaction or visual patterns simply because they exist in an earlier prototype.
- Apply engineering governance and the necessary development/review/validation workflow.

These confirmations govern how decisions are researched and reviewed. They do **not** approve the product promise, target role/site, MVP scope, visual direction, frontend framework, production architecture, deployment model, or any G6.9-R2 candidate. No such substantive product or architecture approval is recorded here.

### Decisions still awaiting owner review

- Product promise:
- Lead user/site:
- Visual direction:
- Product changes/exclusions:
- Architecture boundaries:
- Technology decisions deferred to bake-off:
- Recommendation economic display (absolute expected cost / baseline-relative change / omit until evidence):
- Step 3D shared Temporal persistence service (approve PG16 addition / request supported alternative / defer):
- Detailed-design slice to prioritize:
- Security verification baseline (tailored ASVS checklist / other / defer):
- Date / reviewer:


## Follow-up: Pro Max and prototype v0.4 static UX review (2026-10-04)

**Scope:** Static source review of `docs/02-product/prototype/v0.4/index.html` against the product IA and the installed UI/UX Pro Max skill. This is a design review, not a browser/device assistive-technology audit or user test.

### Search evidence

- The design-system query `commercial energy operations analytics dashboard` returned a Real-Time / Operations Landing pattern and conditional Glassmorphism direction. The product's signed-in, sustained analysis workspace is not a marketing landing page; these results are reference material only. No palette, font or visual style is approved from them.
- The first UX query (`data uncertainty decision review dashboard`) returned unrelated bulk-edit and autoplay guidance, so it was not applied. The required narrower retry (`keyboard focus navigation state`) returned directly relevant guidance on keyboard reachability, focus, active state, deep links and skip links.
- The chart query (`time series accessible chart uncertainty`) returned relevant time-series guidance: use more than hue to distinguish series and provide a visible table or narrative alternative. v0.4 already has a labeled SVG, line-style distinction, explanatory summary and sampled-value table for its synthetic trend.
- No framework-specific guidance was run: the frontend framework remains unapproved and this prototype is standalone HTML.

### What the static source supports

- Skip-to-main link, semantic main/navigation regions, visible focus styling, 44px minimum navigation/button/filter targets, keyboard-operable native controls and focus transfer to the active view heading are present.
- Workspace views update the hash and support browser back/forward navigation. Chart context remains explicitly synthetic; the text summary and table remain available when small-screen chart axis labels are hidden.
- The economics selector distinguishes bill reconstruction, interval assessment and baseline comparison. Recommendation disposition and replay controls explicitly state that their local demo actions do not authorize execution or run a real replay.

These findings establish source-level presence only. They do not establish that contrast and focus remain correct in every state, that the page has no rendered overflow at target viewports, or that a keyboard/screen-reader user can complete tasks.

### Follow-up items before visual/product baseline

1. **Typography:** addressed in prototype v0.4: the root body size is now 16px, matching the skill's baseline recommendation. A rendered browser preview after the change loaded the primary navigation, main view, and chart explanation. This was a single available preview viewport, not the required responsive/200%-zoom review; dense-table fit and the final product-wide type scale remain open.
2. **Macau language and formats:** the prototype is English-only. Validate Traditional Chinese, Portuguese and English needs, terminology, number/currency formatting, and timezone expectations with the lead user/site hypothesis before fixing locale defaults.
3. **Responsive navigation and dense data:** verify the seven-item narrow-screen navigation, table behavior, focus visibility and page-level overflow at 375, 768, 1024 and 1440 CSS px in a rendered browser. The source uses a horizontally scrollable nav/table region at narrow widths; this static review cannot confirm its usability.
4. **Evidence and chart comprehension:** ask target users to explain source, freshness, synthetic status, threshold, and what the sampled chart table does not contain. Keep the current non-bill-grade and not-measured language unless validated evidence supports a stronger claim.
5. **Prototype boundary:** review-state and replay buttons are local demonstrations with no persistence or runtime replay. Preserve their explicit labels; implementation must not carry these demo semantics into production unnoticed.

### Screen and task-flow coverage audit (static source comparison)

The IA defines nine screen responsibilities (S-01–S-09) and four primary flows. The v0.4 prototype exposes seven top-level views: portfolio, site, data health, site model, economics, recommendations, and evidence/replay. Tariff and contract evidence (S-06) appears as a summary/status reference but has no dedicated inspection flow. Integration and site access (S-09) appears as site/integration status, but no connection setup, permission, credential, retry, or recovery task is represented. Flow A therefore cannot be completed end to end in this prototype; Flow B's tariff evidence and Flow D's replay are explanatory/local demonstrations rather than operational workflows.

This is a deliberate prototype-coverage limit, not evidence that the product should have nine permanent navigation items. Before calling the product interaction design complete or using it to validate those tasks, either extend the prototype with representative S-06/S-09 task paths and honest states, or explicitly narrow the validation task set and record what remains unvalidated. Keep the navigation structure open for user research; do not promote the IA screen count directly into final navigation.

**Disposition:** v0.4 is a useful review prototype for the existing research-derived task hypotheses. No urgent source-level implementation blocker was found in this limited pass; the IA-to-prototype coverage gap above is a product-validation blocker for claims about complete Flow A, tariff-evidence inspection, or integration onboarding. Product scope, lead role/site, language, final visual system, accessibility conformance, and frontend framework remain open; no customer validation or WCAG conformance is claimed. The next product-design evidence step is an owner-selected lead role/site hypothesis followed by authorized discovery and formative usability sessions using these tasks.

## Follow-up: v0.5 screen-flow coverage draft (2026-10-04)

**Status:** Synthetic, no-framework review prototype; exploratory only. It does not approve a product workflow, final navigation, visual system or frontend framework.

- Preserved v0.4 and added two context-reachable views: S-06 tariff and contract evidence from Economics, and S-09 integrations and site access from Site overview. They are child flows; v0.5 does not add two permanent primary-navigation destinations.
- S-06 separates regulation/published tariff, customer contract, site configuration and project assumptions. Its evidence table now has an explicit caption for assistive-technology context; this is a source-level semantic improvement, not proof of screen-reader behavior. Pu interval, customer-class monthly-charge formula and effective rules stay unresolved; the screen shows no calculated bill.
- S-09 previews the read-only permission purpose and site scope, makes role/credential ownership explicitly undecided, separates connection state from data freshness, and describes denial/revocation recovery. The prototype collects no credentials, connects no source and has no live authorization.
- The review task set can now inspect both evidence classes and onboarding/access expectations. This improves prototype coverage for the corresponding IA questions; it does not show that a real connector or complete operational onboarding workflow is designed.
- Existing visual treatment is carried forward from v0.4 for comparison, not selected as the final design. Final placement, grouping, wording and role-specific access details require owner and user review.

**Static interaction follow-up (2026-10-04):** Source review found that the keyboard-operable `<summary>` disclosures were missing the prototype's explicit shared focus-visible rule. The prototype now includes `summary:focus-visible` in that rule. This confirms a source-level fix only. **Verification boundary:** v0.5 still has no rendered-browser, viewport, keyboard, assistive-technology or user-session review. All data and organizations remain synthetic. No customer validation, WCAG conformance or product approval is claimed.

## Follow-up: v0.5 responsive and accessibility source audit (2026-10-04)

**Method:** Narrow source-level audit of the static HTML/CSS prototype, guided by UI/UX Pro Max searches for keyboard focus visibility and small-viewport table handling. No frontend framework is selected or assumed.

- Confirmed a viewport meta tag, one primary `main` landmark, a navigation landmark, and responsive breakpoints at 1100px, 760px and 480px.
- At narrow widths the KPI cards reflow, two/three-column content becomes one column, chart labels are hidden below 480px, and tabular records sit in `overflow-x:auto` wrappers. Four tables have captions and column headers.
- All 26 source buttons contain text or an accessible name. The two select controls have accessible names, including a visible `<label>` for the point filter. Explicit `:focus-visible` styling covers buttons, selects, links and disclosure summaries.
- The mobile primary navigation becomes a horizontally scrollable strip at 760px and below; discoverability and keyboard/gesture behavior require rendered testing.

**Boundary:** This audit only confirms source constructs. It does not establish computed contrast, actual viewport fit, browser rendering, keyboard traversal, screen-reader announcements, touch usability, WCAG conformance or user validation. No visual direction or interaction design is approved by this review.


## Follow-up: v0.5 Pro Max fit, contrast and mobile-navigation review (2026-10-04)

**Method:** Re-read the v0.5 source and applied the UI/UX Pro Max workflow. The first and narrowed design-system searches both returned the same “Real-Time / Operations Landing” + conditional Glassmorphism direction. That is a poor fit for a signed-in, sustained analytical workspace and is rejected as a visual prescription; no palette, font, stack or style is approved from these results. Targeted UX/chart searches were then checked for fit against the actual prototype.

- **Evidence and positive source checks:** the prototype uses a 16px root font, visible focus styling, named controls, reduced-motion rules, 44px primary controls, semantic status text, an SVG trend chart with a textual legend, and a visible expandable sample-value table. Static contrast calculations for the sampled text pairs in v0.5 meet the 4.5:1 normal-text threshold: primary text 14.75:1; muted text 5.10–5.48:1; table/chart labels 4.87–5.59:1; semantic status labels 5.77–7.68:1. This is a source-color calculation, not rendered/WCAG conformance evidence.
- **Chart issue to resolve:** the dashed scenario-threshold line uses #d68a16 on white, approximately **2.80:1**. W3C WCAG 2.2 SC 1.4.11 sets a 3:1 threshold for meaningful graphical objects. The chart also provides a dashed line style, text legend and sampled values table, so this static result alone does not establish an overall conformance failure; darken the line in the next prototype and verify its adjacent colors, or demonstrate an equivalent accessible explanation in the rendered interface. Reference: https://www.w3.org/WAI/WCAG22/understanding/non-text-contrast.html
- **Mobile-navigation issue to resolve:** at widths ≤760px, the seven-item primary navigation becomes a horizontal scrolling strip. The narrow-view discoverability, keyboard focus/scroll behavior, gesture discoverability and page-level overflow have not been rendered or user-tested. The Pro Max responsive search flags horizontal overflow as a risk; evaluate a compact, discoverable navigation pattern while keeping all product destinations reachable.
- **Visual/product boundary:** retain the neutral, evidence-first analytical workspace as an exploration baseline only. Do not switch the sustained workspace to a marketing landing layout or apply glass blur as a default. The previous A/B/C visual directions remain unapproved; target-user tasks are needed before finalizing navigation or visual system.

**Next review artifact:** a prototype iteration should correct the threshold contrast and compare a mobile navigation alternative at 375, 768, 1024 and 1440 CSS px, including 200% zoom, keyboard/focus checks and a rendered chart fallback. Follow that with authorized WP-4 formative tasks before treating the interaction design as validated.

**Boundary:** static source/color review only. No browser/device rendering, zoom, keyboard traversal, assistive-technology, participant or WCAG-conformance test was performed. Product scope, user roles, visual direction and frontend framework remain open.


## Follow-up: v0.6 mobile navigation and chart-threshold iteration (2026-10-04)

**Method:** Applied the prior static findings to a new, preserved prototype version using the UI/UX Pro Max workflow and the existing evidence-first workspace direction. No production framework or visual direction is selected.

- Replaced the narrow-screen horizontally scrolling primary navigation with a compact native selector. Its nine options cover all seven primary destinations plus the tariff-evidence and integration/site-access subviews. Selection updates the active view and URL hash; browser back/forward continues to synchronize through the existing hash handler.
- Darkened the chart's dashed scenario-threshold stroke and legend swatch from `#d68a16` to `#875300`. The new foreground color calculates to approximately **6.43:1 against white**. This is a source-color calculation only; adjacent chart/grid colors and rendered contrast have not been evaluated.
- Preserved v0.5 unchanged at `docs/02-product/prototype/v0.5/index.html`; v0.6 is at `docs/02-product/prototype/v0.6/index.html`.

**Verification boundary:** static source inspection confirms all nine destinations are present, selection is synchronized with `showView` and URL hash navigation, and the old threshold hex no longer appears. A limited local in-app-browser render was then inspected through its accessibility tree: one browser context exposed the compact selector, a second exposed the desktop navigation, and a `#tariffs` deep link showed the tariff view and matching breadcrumb. Exact CSS viewport dimensions were not captured and no screenshot-level visual assessment was performed. Review at 320/375/768/1024/1440 CSS px, 200% zoom, keyboard traversal, assistive technology, participant sessions and WCAG conformance remains outstanding. v0.6 remains synthetic and unvalidated; product scope, interaction direction, frontend framework and production architecture remain unapproved.


## Follow-up: limited rendered and keyboard observation for v0.6 (2026-10-04)

**Method:** Opened the existing synthetic prototype in the Codex in-app browser, inspected its rendered narrow-panel view and accessibility tree, then exercised visible controls by keyboard/pointer. This is a bounded exploratory review of one browser surface, not a formal responsive or accessibility test.

- The narrow-screen native view selector exposed all nine destinations. ArrowDown followed by Enter changed Portfolio overview to Site overview; the URL hash changed to `#site`, the selected option updated, and the page heading/content changed. This confirms that this single selector path is keyboard-operable in this browser context.
- In Economics, selecting Baseline comparison changed the result state to “Unavailable” because no validated baseline/candidate pair exists; no modeled delta or realized-savings amount was shown. This supports the draft's conservative result boundary in this one interaction.
- The screenshot showed a compact header/selector, visible synthetic-data notice and vertically flowing content in the narrow preview. This does not establish exact CSS viewport dimensions, no-overflow behavior at specified breakpoints, touch-target sizing, 200% zoom, desktop layout, full keyboard order, screen-reader behavior, or WCAG conformance. A temporary wide viewport override produced a capture whose bounds were not reliable for desktop layout review; repeat desktop review with a measurable browser surface.

**Boundary:** No prototype source was changed in this follow-up. No customer/user session, assistive-technology session, or production-interface acceptance is claimed. Keep visual direction and product scope unapproved pending owner review and authorized WP-4 research.
