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

The design-system search returned a **Real-Time / Operations Landing** pattern and **Glassmorphism** style, a dark/neutral palette with semantic status colors, and Fira Code/Fira Sans. The matching UX search returned useful guidance for submission feedback, hierarchy, nested-site breadcrumbs, font scale, and contextual status announcements. The chart search recommended time-series lines for continuous trends, direct labels/line styles, accessible tabular summaries, and explicit actual-versus-forecast distinction.

These are search results, not user evidence. The landing-page pattern is not automatically appropriate for the signed-in operations workspace. The frosted/blurred glass style may reduce clarity or contrast in sustained, information-dense energy analysis; it should not be applied without prototyping and accessibility checks. Font-family and palette suggestions also require fit review. No stack-specific search was run because the frontend framework is unapproved.

### Visual directions for owner review

| Direction | Description | Strengths to evaluate | Risks/questions |
|---|---|---|---|
| **A. Clear operational workspace** | Light-first neutral surfaces; restrained brand accents; clear typography; strong hierarchy for cost, freshness, uncertainty, and exceptions; optional dark mode later. | Long-session readability, dense tables/charts, clear evidence provenance, lower dependence on decorative effects. | Does it feel sufficiently distinctive and suited to an Energy OS? |
| **B. Dark operations console** | Dark neutral canvas with restrained semantic status colors; high-contrast data panels; clear separation between live, stale, and synthetic evidence. Avoid heavy blur by default. | May suit control-room environments and reduce glare in some settings; aligns partly with Pro Max's dark operations suggestion. | Validate contrast, daylight use, print/export, and role preferences; dark mode must not hide data quality. |
| **C. Expressive layered interface** | Selective depth/translucency for navigation or overlays, with opaque reading surfaces for charts, tables, and evidence. | Could provide modern brand character while limiting blur to low-risk surfaces. | Requires performance and contrast checks; easy to overuse and make the interface dated or decorative. |

**Working recommendation for review, not approval:** prototype A as the baseline and use C only as a limited visual accent if it improves orientation. Keep B available as a testable alternative for control-room users. Validate with actual target users before freezing a design system.

### Interaction principles to evaluate

- Make data provenance visible: measurement/source, time range, freshness, coverage, and uncertainty.
- Use explicit system states and recovery: loading, empty, partial, stale, failed, permission denied, and retry.
- Distinguish actual, forecast, recommendation, and executed outcome in labels and chart treatment, not color alone.
- Keep serious actions under human approval; make shadow/advisory state unmistakable.
- Fit navigation and layout to validated tasks and device context. Do not copy old dashboard conventions or force a mobile-first shape.
- Review keyboard navigation, focus visibility, contrast, chart alternatives, reduced motion, and responsive behavior. WCAG 2.2 AA is a proposed evaluation target pending owner review.

Reference material: Pro Max skill; W3C WCAG 2.2; Material Design 3 foundations; Nielsen Norman Group usability heuristics. They are reference points, not visual templates.

## 4. Architecture decision status for review

### Logical boundaries

The current draft separates site Edge and local safety from cloud intelligence, cost/settlement, forecasting/optimization, evidence/replay, and human approval. This is a research-derived boundary proposal. Please review whether these responsibilities and trust boundaries fit the intended product and operating model.

### Technology choices

| Concern | Current recorded state | Review status |
|---|---|---|
| Frontend | React + TypeScript was proposed in provisional architecture notes. | Not approved; confirm framework only after product surfaces and bake-off implications are clear. |
| Cloud-core topology | Candidates A, B, C+ under G6.9-R2. C+ is a provisional default; Node/NestJS is existing Candidate B implementation evidence. | Do not call a winner before Step 3D/4 evidence and Decision Record. |
| Workflow | Temporal candidate. | Candidate, not final selection. |
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
- canonical request/event/result/evidence contracts and versioning;
- tenant/site authorization derived from authenticated identity, not caller-supplied body fields;
- storage, retention, replay determinism, idempotency, failure and recovery;
- observability, audit, migration/rollback, and operational ownership;
- which Gate evidence is a prerequisite and what may remain out of scope for shadow mode.

No change here closes G1, G6, G6.9-R2, or G7.2. No device control is authorized.

## 6. Proposed review sequence

1. Review the product promise, first user/site hypothesis, and exclusions.
2. Review visual direction A/B/C and interaction principles. Treat prototypes as synthetic until user-tested.
3. Confirm product boundaries and the architecture questions to carry into G6.9-R2; do not prematurely select the stack.
4. After those reviews, revise the PRD, user flows, prototype, logical architecture, and relevant ADRs to record accepted decisions and remaining unknowns.
5. Confirm the first detailed-design slice and its acceptance evidence; then implement against that approved packet.

## 7. Owner response record

No response or approval is recorded in this draft.

- Product promise:
- Lead user/site:
- Visual direction:
- Product changes/exclusions:
- Architecture boundaries:
- Technology decisions deferred to bake-off:
- Detailed-design slice to prioritize:
- Date / reviewer:
