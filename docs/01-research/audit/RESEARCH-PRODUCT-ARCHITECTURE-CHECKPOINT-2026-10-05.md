# Macau Commercial Energy OS — Research and Design Checkpoint

**Review date:** 2026-10-05  
**Status:** evidence checkpoint; not a replacement Authority, Gate closure, owner approval, product freeze or production architecture decision.

## 1. What the evidence currently supports

| Area | Verified state | What that means |
|---|---|---|
| Product thesis | Main-branch D-001–D-009 position an energy orchestrator; optimize total economic cost/value; prioritize HVAC/chiller first; ESS is optional and site-economics dependent; PV rules come from the customer's verified settlement terms; Demand Guard can veto; AI/cloud do not directly control equipment; the MVP foundation includes tariff/contract and meter/settlement twins, Energy Graph, HVAC model, Shadow mode and M&V. | Economic source/load coordination is consistent with the accepted product/engineering boundaries. The current main product README still describes visibility, tariff intelligence and recommendations, so the dispatch-first commercial promise is not yet an approved main-branch product requirement. |
| Dispatch product proposal | Open Draft PR #10 contains a source/load economic-dispatch product design and a six-stage v0.4 workflow: evidence readiness → physical site model → aligned schedule comparison → cost/constraint/evidence explanation → Shadow review → monitoring/replay. | This is the most complete dispatch-first proposal located. It is still a draft; it does not establish tariff truth, site capability, user validation or owner approval. |
| G7.9 | The supplied G7.9 Step 2 package calls its domain/data/contract design complete and explicitly names **G7.9 Step 3 — Service Boundary and Implementation Design** as next. It says that package contains no business implementation code. PR #10 has a stack-neutral dispatch contract and implementation map proposal. | G7.9 Step 2 is complete as a package declaration. Step 3 is not closed: the new map is a proposal and still lists decisions, contract sources, interfaces, migrations and executable acceptance evidence to resolve. This does not prove a dispatch MVP exists. |
| Current implementation | Main contains a bounded telemetry → Energy Graph → tariff/cost → Shadow recommendation/evidence path, initial JSON Schemas and VS-001 code/tests. Main's own docs retain G1 and G7.2 live evidence as open. | This is a useful implementation foundation, not an integrated source/load dispatch workflow or pilot-ready energy model. Synthetic tests do not establish Macau site, bill or savings validation. |
| UI/UX | Main has no selected visual system. PR #8 carries a project UI/UX skill draft and portfolio/readiness prototypes; PR #10 carries a dispatch-first prototype and its review record. The local palette study presents Harbor teal, Mineral blue and Night graphite without selecting one. | Design work exists in review branches and workspace files, not as an approved main-branch experience. The older v0.10 home is Recommendations/portfolio-oriented; it labels synthetic values and no-control limits, but dispatch is not the dominant task. The dispatch v0.4 proposal better represents the requested task and explicitly accounts for HVAC rebound. |
| Macau languages | Current UI studies are not complete multilingual products: the v0.10 review surface is English and PR #10 v0.4 is Traditional Chinese only. | Traditional Chinese, Portuguese and English are a strong release-scope candidate for Macau, but no source reviewed here proves complete localization or an owner-approved locale list. Terminology, currency/time formatting, accessibility names and long-string reflow still need design and user review. |

## 2. Research authority and technology decision matrix

Statuses describe what each source actually says. A later package assertion is not treated as a measured experiment or a silent supersession.

| Technology / decision | Evidence-backed status | Source reconciliation |
|---|---|---|
| React + TypeScript frontend | Stable project direction / confirmed in Authority v2.0; also repeated in the current main G6.9 register. | This does not select the backend framework or mean the production stack is fully frozen. |
| TypeScript vs Go application core | Unresolved in current main: TypeScript/Go responsibility split remains under evaluation; C+ Go core is the provisional hypothesis. | Deep Research (6) recommends C+; Deep Research (7) recommends Node/NestJS. G7.6's larger Step 2 archive and G7.8 Step 3 archive record a TypeScript backend with Node LTS/Fastify, creating a status conflict with the still-open G6.9 Step 3D checkpoint. |
| Node/NestJS | Existing implementation path and report (7) recommendation; not a measured G6.9 winner. | Current main contains NestJS code. This proves the code path exists, not that Step 3D selected NestJS. |
| Node/Fastify | Explicitly accepted in the detailed G7.6 Step 2 archive and G7.8 Step 3 ADR package; not reconciled as current controlling authority. | A separate same-named, seven-entry G7.6 ZIP labels ADR-068 Proposed, while the 39-entry variant marks ADR-068/071–076 Accepted. PR #11 records both hashes/statuses and the conflict. |
| Bun/Hono/Effect | Candidate/challenger in G6.9 A; Bun also allowed as evaluation/development tooling in later packages. | Not approved as the production runtime. Report (6) recommends it only as the C+ thin product/BFF option/challenger; the benchmark evidence remains incomplete. |
| Next.js | Not selected as the backend or core operator UI. | Deep Research (7) favors React/TypeScript SPA for the operator console and describes Next.js conditionally for a public/customer portal or valuable server-side UI composition. Report (6) mentions Next.js documentation for coding agents, not a project stack choice. It is outside the named A/B/C+ G6.9 candidates. |
| Temporal | Candidate; runtime/persistence integration evidence remains part of the G6.9 Step 3D gap. | No pinned, comparative end-to-end result was located that closes the bake-off. |
| PostgreSQL / Timescale | PostgreSQL is the system-of-record baseline; PostgreSQL + Timescale is the G6.9/report baseline. | Detailed G7.6 Step 2 says PostgreSQL 18 as initial store/telemetry with a separate time-series database deferred. The accepted archive wording and current G6.9 README need an owner-approved reconciliation before a freeze. |
| NATS / MQTT | NATS JetStream is a G6.9 candidate and appears in accepted G7.6 package decisions; MQTT is relevant to the Edge/cloud boundary in research. | Do not infer a final transport topology or broker choice from one archive. The G7.9 Step 2 package lists domain events but does not select NATS, Kafka, MQTT or delivery guarantees. |
| Python / Go Edge | Strong architectural directions: Python for forecasting/optimization/simulation; Go for Edge and local safety boundary. | Both reports and Authority/Gate materials support these roles. Exact deployment, optimizer and safety-runtime closure still needs implementation evidence. |
| Wasm/WASI | Future plugin-isolation direction. | Not an MVP implementation commitment. |
| Java | Not selected for this MVP. | It appears in technology landscape research, not as an accepted project runtime. Report (7) argues against adding a fourth production language during the pilot. |

### G6.9 status

The main-branch handoff and G6.9 register say Steps 3A, 3B and 3C are complete and **Step 3D pinned framework-native integration remains pending**; no measured production-stack winner is recorded there. Later Authorities consolidate the broader G6.9 research as complete, while other Authority snapshots still name framework evidence or G6.9-R2 3G.2 as next. The exact answer is therefore: broad research/consolidation was declared complete in later snapshots, but the specific Step 3D comparative integration evidence and the 3G.2 adoption proof are not established by the current main record. “All of G6 is complete” is not supported.

## 3. Shared conversation and source-access boundary

On 2026-10-05, the shared ChatGPT URL displayed the conversation title but a login wall and no message body. The conversation archive lookup returned four recent turns with no older cursor (`hasMore=false`), not the full historical transcript. The full share-page conversation and all linked generated outputs therefore remain unverified; this review does not claim to have read every original turn. The two supplied Deep Research reports, local Authority/Gate packages and GitHub files were independently inspectable.

The package inventory and the detailed Gate readouts are in PR #12's `ARCHIVE-INVENTORY-v0.1.md`, `G7.1-7.5-RESEARCH-READOUT-v0.1.md`, `G7.6-7.9-DELIVERY-TRACE-v0.1.md` and `G6.9-3G.1-3G.2-AND-G7.9-STEP3-STATUS-v0.1.md`. The archive inventory is not a claim that every historical Authority artifact received a complete semantic review.

## 4. UI/UX evidence and practical quality bar

- `ui-ux-pro-max` was applied. Its two attempted energy-console design-system searches returned a generic marketing/Trust-and-Authority layout and an off-domain organic/dashboard recipe. Those matches were rejected; no resulting palette, font or layout is adopted.
- The project `macau-energy-os-ui-ux` skill draft is in PR #8, not main. It correctly makes source/load semantics, evidence labels, Shadow-only operation, accessibility, responsiveness, language reflow and originality product-specific review criteria.
- [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) and [Material 3 foundations](https://m3.material.io/foundations/) are used for adaptable layout, visual hierarchy, tokens, interaction states and accessibility guidance. [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/) is the minimum accessibility target, not a claim of conformance.
- An [Awwwards scored site example](https://www.awwwards.com/sites/proof-1) breaks down design, usability, creativity and content; the [Webby 2026/27 criteria](https://www.webbyawards.com/judging-criteria/) cover content, structure/navigation, visual design, functionality, interactivity, innovation and overall experience; [FWA's own anniversary overview](https://thefwa.com/FWA25/25.html) describes its references in terms of digital creativity, originality and technical excellence. These are inspiration/quality lenses, not a guarantee of awards or a substitute for validating an operations task.
- Existing v0.4 branch review records a browser render and layout inspection at 1440, 1024, 768 and 375 CSS px; it does not claim user validation, complete localization, bill truth, field readiness or full runtime interaction verification. This checkpoint did not re-render that branch version.

## 5. Current GitHub delivery state

Main is `a897bf0b1e7e6ceea3862d7d87fa288ecca08203` (`docs: sync current authority register counts`). On the checked snapshot, PRs #8 and #9 are open and ready for review; PRs #10–#13 are open Drafts. Product, dispatch, technology reconciliation and archive-audit work remain review proposals and have not been merged into main. Passing structural CI does not close research gates or validate a site.

## 6. Next work that does not require an owner freeze

1. Complete a source-to-main/GitHub trace for each required Authority, G6.9 and G7.1–G7.9 deliverable; keep package-declared completion distinct from executable proof and user/site validation.
2. Reconcile G6.9 Step 3D, G7.6 duplicate ADR packages and G7.8 ADR status with dated authority precedence; do not silently select a stack.
3. Advance the PR #10 dispatch proposal against main D-001–D-009, current PR #8 APP-01…APP-10, G1/G2/G3/G6/G7 evidence, and the G7.9 Step 3 boundary. Keep APP-11 as a proposal until catalog ownership is reviewed.
4. Review the dispatch v0.4 visual and interaction design against the project skill at representative widths and all proposed locales; choose a visual direction only after the same operator task is compared and reviewed. Separate the operator console from marketing-site concepts.
5. Specify and then implement a verified read-only dispatch path: common-horizon baseline/candidate; source/load physical balance; constraints and rebound; independently qualified economic evaluation; withheld claims when tariff/contract data are missing; immutable evidence/replay; Shadow-only review.
6. Keep G1, live baseline/no-op, customer/operator validation, M&V, tariff evidence and pilot-readiness gates open until their required evidence exists.

