# Source/load dispatch workflow completeness trace v0.1

**Review date:** 2026-10-07  
**Status:** Source-pinned product/workflow gap trace for owner and domain review. It is not product approval, a final PRD, Gate closure, architecture selection, site validation, or control authorization.  
**Purpose:** Make the current product-design answer auditable: identify what is designed, what is represented in prototypes, what exists as code, what is integrated into `main`, and what evidence is still missing.

## 1. Exact repository snapshot

This review compared the same `main` base against the three relevant open proposals:

| Ref | Exact state checked | Meaning |
|---|---|---|
| `main` | PR base `a897bf0b1e7e6ceea3862d7d87fa288ecca08203` | Current target branch for the three PRs below. |
| PR #8 `docs/product-architecture-roadmap` | `9e3dec0bccf5acb5122f94c688814e7f4e026a1b`, open, non-draft, unmerged | Broad product design, PRD, IA, visual principles, research/usability plan, detailed-design proposals, UI/UX skill draft and platform prototypes. |
| PR #10 `product/source-load-economic-dispatch` | `e1ce7486d9ea752e2421249d044748fefa078773`, open, Draft, unmerged | Dispatch-specific product proposal, research traces, six-stage workflow prototypes, locale and layout studies, and result-projection reviews. |
| PR #14 `poc/shadow-dispatch-assessment` | `9b80adca9243a0ae9a7bd666f0efee1acfc6309a`, open, Draft, unmerged | Bounded Python SHADOW assessment/search experiment; not an integrated product service. |

The current main branch therefore does **not** contain these complete proposed product/design artifacts as one adopted, end-to-end dispatch product. A green branch check does not change that state or constitute owner approval.

### Source anchors checked

- PR #8 `docs/02-product/PRODUCT-DESIGN.md` — blob `4726a5bb7b74711054cee5eda056f2bd51c3da33a`.
- PR #8 `docs/02-product/PRD-v0.1.md` — blob `22b129baf1a7c3d0cf11069d9f23fb414908d1d7`.
- PR #8 `docs/02-product/USER-FLOWS-AND-IA-v0.1.md` — blob `41082c28d41386303fc991ba1217b3f7ba9f0e08`.
- PR #10 `docs/02-product/PRODUCT-DESIGN-RECONCILIATION-v0.4.md` — blob `8c16124704a44118f0cad5c6d3ba6b3a05e0f993`.
- PR #10 `docs/02-product/SOURCE-AND-LOAD-DISPATCH-DESIGN-v0.1.md` — blob `b34860f487d1b83b2cc9d6b6e99cbd27ebe93ef8`.
- PR #10 `docs/02-product/G7.3-G7.9-RESEARCH-AND-REPOSITORY-TRACE-v0.1.md` — blob `3c2a18a7dc4cead6b74d267afdd2cc11972d2122`.
- PR #10 full-workflow prototype v1.9 review — `docs/02-product/prototype/source-load-dispatch/v1.9/REVIEW.md`, blob `61c802008079a1b44de5fa7c8929e881a41f5219`.
- PR #10 result/claim prototype v2.9 review — `docs/02-product/prototype/source-load-dispatch/v2.9/REVIEW.md`, blob `3d5b545485a532b4784582f2fff1c4d7d48b9894`; HTML blob `a19472d11fcbdf39afde64fcc8d0d9bf2f1c4457`; fixture blob `fec75272470155c531a1747ddf00db91ec00c583`.
- PR #10 matched-palette layout comparison v0.2.3 review — `docs/02-product/prototype/source-load-dispatch/directions/v0.2.3/REVIEW.md`, blob `9c61627197195faebb15144f59defb72eaeae66c`.
- PR #10 `docs/03-architecture/detailed-design/APP11-V2.8-PR14-RESULT-PROJECTION-REVIEW-2026-10-07.md` — blob `d84e0c36aa37c5d8875c16bdb830eacfd750775f`.

The referenced original ChatGPT share page was also attempted on this review date and returned a cache miss. This trace is therefore grounded in the accessible repository sources above, not a claim that the full original conversation was re-read. The full local research archive semantic review is a separate, incomplete audit scope.

## 2. Status vocabulary

- **Draft design:** a written requirement or proposed behavior exists; it is not approved.
- **Synthetic prototype:** a user interface demonstrates selected states using fixture values; it does not prove service behavior, site facts or product acceptance.
- **Code experiment:** executable code exists within a bounded test scope; it is not integrated into the user workflow.
- **Implemented on main:** the actual default branch contains the behavior, contract and necessary persistence/integration.
- **Site/user validated:** authorized Macau site evidence and representative-user results support the behavior.

A stage can have a draft design and synthetic prototype while remaining unimplemented on main.

## 3. Product-design finding

**The product direction is coherent and has substantial draft design, but the product design is not complete or approved, and the six-stage dispatch task is not implemented end-to-end on main.**

The product proposal is centered on a commercial operator comparing time-aligned schedules for grid import, evidenced on-site PV, optional ESS charging/discharging, and only site-qualified flexible loads such as HVAC/chillers, EV charging or hot water. It is not merely an energy KPI dashboard. It keeps physical energy flow separate from account/meter/contract/tariff settlement and makes the result advisory.

PR #8 contains the broad product workspace, PRD, IA, visual principles and discovery/usability proposals. PR #10 makes source/load economic dispatch the first-class task and adds the six-stage workflow and successive interaction studies. These are complementary draft lines; neither is an approved baseline and neither is merged. PR #14 supplies a bounded optimizer experiment but does not integrate it into the PRD, UI, API, evidence service, durable review or monitoring flow.

## 4. Six-stage requirement-to-evidence trace

| Stage | Draft design evidence | Prototype / code evidence | Main-branch and validation status | Gap and acceptance evidence still required |
|---|---|---|---|---|
| **1. Data and contract evidence** | Dispatch design and product reconciliation require site/horizon context, telemetry quality, physical mapping, separate account/meter/contract/tariff applicability and independent readiness states. | v1.9 starts at an evidence-check stage using synthetic readiness. v2.9 deliberately withholds bill-grade money when applicability is unverified. PR #14 uses caller-supplied evidence markers. | **Not an integrated main workflow.** No product-level authenticated evidence intake, effective-dated source registry or user repair path is established by the cited prototypes/experiment. No customer documents/data have been validated here. | Demonstrate source identity, authorization, version/effective dates, freshness and lineage for meter mapping, interval data, account, contract and tariff. Missing evidence must withhold only dependent claims and show an actionable next step. |
| **2. Physical site model** | Design separates physical topology (grid, meters, PV, ESS, loads) from settlement/account mapping; unknown links must remain explicit. | v1.9 presents a synthetic site-model stage. v2.9 shows a synthetic source/load schedule but is not a topology editor. | **Not implemented as an integrated site model on main; not site-validated.** PR #14 supports one supplied site/account-meter scope and does not establish an energy graph. | Review an authorized site's one-line/topology, meter boundaries, point mappings, assets and effective periods. Prove separate physical and economic mappings, including ambiguity/overlap handling, before stating cross-building supply or credits. |
| **3. Schedule comparison** | Product requirement is a same-site, same-horizon comparison with aligned baseline/candidate intervals, sources, loads, ESS trajectory and explicit flexible-load shifts/rebound. | v1.9 represents this stage in its six-step synthetic flow. v2.9 presents a six-interval fixture. PR #14 can search a supplied finite set of discrete actions in a bounded horizon; its exactness is limited to that search space. | **No integrated dispatch API-to-product UI path on main is evidenced.** PR #14 is code experiment, not a production service or schedule-generation UI. Neither prototype proves a real feasible schedule. | Pin same immutable inputs, timezone, horizon, interval grid and model/rule versions. Show baseline and at least two alternatives with per-resource changes, rebound, ESS SOC, import/export and binding constraints. Validate against site-approved capability envelopes. |
| **4. Cost, constraints and evidence** | Design requires independent physical, service/comfort and economic claim states; values must be withheld when their own evidence is missing. | v2.9 shows synthetic rates and scenario search rationale, but withholds bill cost, full-bill amounts, savings, export compensation, comfort/controllability, cross-site credits and control. APP-11 projection review documents this UI/result boundary. PR #14's monetary scope is limited to qualifying interval grid-import energy rates; it does not implement full tariff settlement. | **No bill-grade dispatch result on main or validated against a Macau customer's bill.** Neither the fixture's six interval rates nor the prototype's 44 kWh comparison establish tariff applicability, billing demand/Pu or savings. | Independently reconstruct representative bills (“Golden Bill” cases) using verified account, meter, contract, effective tariff, billing intervals and settlement rules. Model demand windows, export and other components only when source evidence supports them; compare outputs against approved reference calculations and explicit tolerances. |
| **5. SHADOW review** | Design proposes advisory recommendation review with identity, authorization, immutable result reference and an append-only disposition; review is not execution. | v1.9 and v2.9 controls are page-local and reset on reload. PR #14 contains no device-control path, but does not supply durable review service semantics. | **No durable dispatch review flow on main is established here.** A click in a prototype is not an audited decision. | Persist reviewer, role, time, result version, disposition, reason and evidence reference; enforce authorization and idempotency. Demonstrate that no review action can reach a device command endpoint. |
| **6. Monitoring and replay** | Design requires measured post-period results, declared M&V basis, immutable input/rule/model/build manifest and replay differences. | v1.9 includes a monitoring/replay stage as a conceptual/synthetic screen. The cited v2.9 prototype focuses result disclosure and has no durable replay. PR #14 repeatability is bounded code evidence, not an integrated replay service. | **No live Macau monitoring, M&V, durable dispatch replay or verified savings is demonstrated on main by these artifacts.** A synthetic/reference simulator baseline is not a site baseline. | Capture consented, quality-qualified measurements and a pre-agreed baseline/M&V method. Replay the pinned request deterministically; surface unavailable or changed evidence and explain any difference. Validate reporting with site/operator and finance owner. |

### Cross-cutting product states

The interface and future contracts must not collapse these into one “ready” badge:

1. request lifecycle;
2. physical input/result readiness;
3. service, comfort and safety constraint status;
4. economic applicability and component coverage;
5. recommendation and review state;
6. monitoring/replay state.

A physical profile may remain inspectable while tariff economics are withheld, but whether an optimized physical-only candidate is allowed with no applicable contract remains an **owner/domain decision**. Prototype v2.9's no-tariff withholding behavior is a study policy, not a final product rule.

## 5. UI/UX evidence and limits

- The six-stage v1.9 review reports six stage states at 320, 375, 768 and 1440 CSS px (24 combinations), with no document-level horizontal overflow in the reviewed synthetic prototype. This is layout evidence, not user validation.
- The v1.9 localization study is split into separate review versions. The existing reconciliation reports a 337-unit contextual translation draft and limited accessibility-tree review; its status must not be generalized into full, human-reviewed multilingual support.
- The v2.9 review checks the single claim/results page in Traditional Chinese, English and Portuguese at 320×800, 375×812, 768×900, 1024×900 and 1440×900 (15 combinations). It reports no page-level overflow and translated page content; it explicitly does not establish translation quality or launch locale approval.
- Layout directions v0.2.3 compare timeline-first and interval-first compositions on a matched palette across nine widths. The palette, layout, product visual identity and direction remain unapproved. The recorded checks are targeted; they are not a complete WCAG audit or conformance claim.
- No cited source establishes moderated operator usability, a winning-site reference transfer study, full screen-reader/keyboard coverage, complete locale QA, or production UI.

Keep three separate design jobs: dispatch operations console, customer/account setup and evidence maintenance, and any future marketing homepage. Award-winning consumer/marketing patterns are inspiration and quality-review references, not a substitute for operational task evidence or an excuse to copy a visual style.

## 6. Proposed MVP acceptance bar

Before calling the dispatch workflow an MVP, an integrated review build should prove all of the following:

1. An authorized user can identify site, local-time horizon, interval, source snapshot and measured/forecast/scenario/synthetic status.
2. Physical topology and settlement/account applicability are separate, inspectable mappings.
3. Baseline and candidate share pinned inputs and aligned intervals; each changed resource, SOC trajectory, rebound and constraint is visible.
4. Unknown/missing/stale evidence is never silently replaced with zero, unlimited capability, export rights, comfort, controllability or verified economics.
5. Physical, service, economic, recommendation and replay states remain independent and have explicit blocked/partial explanations.
6. No bill-grade amount, savings, export compensation or demand-charge claim appears until the matching site/contract/meter/tariff evidence passes a validated rule.
7. SHADOW dispositions persist with actor, authorization, result version and audit history; there is no device write path in MVP.
8. A completed assessment can be replayed from immutable input and version references; divergence and missing evidence are visible.
9. The same critical tasks work at approved viewport/locale combinations with keyboard use, accessible names, non-color status cues and human-reviewed terminology.
10. Representative operator and finance users complete agreed tasks against an authorized pilot evidence packet; comprehension/errors and acceptance thresholds are recorded.

These are proposed acceptance criteria. Items 9–10 are not evidenced as passed.

## 7. Open decisions and next concrete work

### Decisions for a single owner review packet

- **No-applicable-tariff behavior:** physical/scenario-only analysis with economics withheld, or no candidate generation. Explain safety, site permission and product-value consequences.
- **First pilot context:** site archetype, accountable operator/finance roles, available evidence and first supported resources. HVAC/chiller is a leading hypothesis, not validated capability; PV/ESS/EV/hot-water participation depends on site evidence and rights.
- **MVP settlement boundary:** exact bill components and qualification threshold; explicitly identify demand-window/Pu, export, netting, cross-site and uncertainty exclusions.
- **Locale policy:** validate Traditional Chinese, Portuguese and English needs, Macau terminology, regional formatting and human-review capacity. Current strings/prototype checks are not approval.
- **Visual/IA direction:** compare same-task dispatch and evidence layouts; approve only after full state/locale checks and user research.
- **Product acceptance:** name participants, tasks, measurable comprehension/error thresholds and domain reviewers.
- **APP-11 and architecture:** reconcile the proposed logical dispatch capability and result/review/replay contracts with G7.9 and architecture authority before creating canonical APIs or production commitments.

### Work that can proceed before these decisions

1. Preserve PR #8 and PR #10 as review proposals and maintain source links; do not describe either as adopted merely because it is detailed.
2. Create a matched dispatch-task study for missing tariff, partial data, HVAC constraint, ESS unknown, PV export and scenario-only candidate states using identical inputs across layout variants.
3. Extend the six-stage review contract matrix so every visible state/claim maps to a domain rule, source evidence, API field and acceptance example; keep proposed semantics separate from canonical schemas.
4. Build an authorized, redacted site-evidence acquisition packet only after an owner selects a participant/site; until then keep prototype fixtures explicitly synthetic.
5. Resolve the source/authority gaps in G7.9 Step 2/3 and technology decision records before freezing service boundaries or production stack.
6. After product decisions, implement one vertical slice on a review branch: pinned evidence snapshot → topology-qualified schedule assessment → independently gated result claims → durable SHADOW review → deterministic replay. Keep device control excluded.

## 8. Conclusion

**Product design exists as a substantial, research-derived proposal and multiple tested synthetic studies. It is not yet a finalized product, an owner-approved PRD/UI, or a complete implemented workflow.** The most advanced product-design evidence is distributed across PR #8 and PR #10; the most advanced schedule-search code is isolated in PR #14. None is merged into the inspected main base, and none proves site/user validation or a production-ready dispatch product.

The correct next product step is a source-linked owner review of the explicit choices above, supported by one integrated workflow/state/contract trace. Continue independent evidence and design work while those choices remain open; do not silently convert prototype behavior, GitHub checks or a code experiment into an approved business or architecture decision.


## Exact main implementation-tree audit — 2026-10-07

A recursive GitHub tree read at `main` commit `a897bf0b1e7e6ceea3862d7d87fa288ecca08203` returned **167 entries, not truncated**. The feature-level files provide stronger implementation evidence than a filename search alone:

| Main artifact | Exact source evidence | What it establishes |
|---|---|---|
| Platform API | [`vs001.controller.ts`](https://github.com/lilinling12/macau-commercial-energy-os/blob/a897bf0b1e7e6ceea3862d7d87fa288ecca08203/implementation/platform-api/src/vs001/vs001.controller.ts), blob `de93bc59354890f1e8be6274123ecf51f24fb3ca`; [`vs001.service.ts`](https://github.com/lilinling12/macau-commercial-energy-os/blob/a897bf0b1e7e6ceea3862d7d87fa288ecca08203/implementation/platform-api/src/vs001/vs001.service.ts), blob `a35cf74b4587fad75415689341de40d88e623ede` | The route is `POST /v1/vs001/evaluate`. It parses one telemetry event, resolves graph/tariff context, saves an evidence record, asks an optimizer port for a SHADOW recommendation, and returns a cost. It is a VS-001 telemetry-to-recommendation slice, not a planning-horizon source/load schedule assessment. |
| Runtime | [`package.json`](https://github.com/lilinling12/macau-commercial-energy-os/blob/a897bf0b1e7e6ceea3862d7d87fa288ecca08203/implementation/platform-api/package.json), blob `c42fcbca6b423c392c920080999b0d3c6022a2cc` | The current platform scaffold declares Node `24.21.x`, NestJS `12.0.3` and `@nestjs/platform-express`. This proves the current scaffold's runtime/framework, not a measured G6.9 winner; it also differs from G7.8's Fastify-based record. |
| Optimizer | [`recommendation.py`](https://github.com/lilinling12/macau-commercial-energy-os/blob/a897bf0b1e7e6ceea3862d7d87fa288ecca08203/implementation/optimizer/src/macau_energy_optimizer/recommendation.py), blob `3190791b958d862d3f29d1420c6a41a626e1860a` | Defines a SHADOW recommendation data object and mode boundary only; the inspected file does not calculate a dispatch schedule. |
| Edge | [`main.go`](https://github.com/lilinling12/macau-commercial-energy-os/blob/a897bf0b1e7e6ceea3862d7d87fa288ecca08203/implementation/edge-runtime/cmd/edge/main.go), blob `ee671a01e41f9325658bb2a98243936bc31825f4`; telemetry type [`event.go`](https://github.com/lilinling12/macau-commercial-energy-os/blob/a897bf0b1e7e6ceea3862d7d87fa288ecca08203/implementation/edge-runtime/internal/telemetry/event.go), blob `4636b773d9637e314a8f11e0cf326affff3e8a09` | The executable currently logs that the Edge runtime started in bootstrap mode; a typed telemetry event exists. This is not a connected site adapter or a running safety/control path. |
| Machine-readable contracts | `implementation/contracts/` contains telemetry-event, recommendation and evidence-record v1 JSON schemas plus fixtures/verifier. | The repository has a contract-first seed for VS-001, but the inspected tree has no dispatch-assessment, schedule, economic-evaluation, durable review or dispatch replay contract. |
| Product UI | The exact main tree has no `apps/web/`, `portal/` or dispatch UI path. PR #8 and PR #10 contain the review prototypes. | The product UI studies remain branch artifacts, not the shipped or main-branch operator console. |

A small VS-001 replay fixture/runner does exist in main; do not confuse replay of that single input example with immutable dispatch assessment replay, persisted review history, measured-outcome monitoring or M&V.

This exact-tree result confirms the prior status labels: **the repository has a narrow platform scaffold and contract/recommendation examples; the complete dispatch product remains design/prototype work plus an isolated PR #14 search experiment.** The tree check is structural and source-level evidence; it is not a runtime integration run or user/site validation.


## Original v0.10 and palette-study artifact trace — 2026-10-07

Two earlier HTML studies in the Codex task workspace were directly read by source structure and hashed. They are workspace artifacts, not files found in the supplied D: project folder. Fingerprints:

- `prototype-v0.10-review.html` — SHA-256 `DF36E3B988631700491490968C823F9AEECE14545280FE00E7BFE6478CD8EC17`.
- `palette-study-v0.1.html` — SHA-256 `8AEE95D1BCADE7116F4408D69704F9479374A0F788CB16A1D630FCE4ABC24FB8`.

The v0.10 prototype's navigation/views are Portfolio, Site, Integrations & site access, Data health, Site model, Economics, Tariffs, Recommendations and Evidence. The portfolio view presents site readiness, open evidence items and a synthetic energy/demand trend; Economics changes among bill/interval/comparison presentation modes. Its site-model copy usefully separates physical/electrical relationships from settlement/economic relationships and explicitly labels synthetic/unverified PV and tariff data. However, there is no first-class source/load schedule-comparison view with baseline/candidate intervals, PV/ESS/flexible-load coordination, schedule constraints or dispatch review. It is a broad evidence/readiness workspace concept, not the dispatch-first product task.

The palette study presents the same synthetic portfolio/readiness/demand-review task in three visual alternatives—Harbor teal, Mineral blue and Night graphite. It supports exploratory color comparison, semantic state contrast samples and solid-vs-dashed actual/forecast encoding. Its own review copy says none is selected or user-tested; selected text contrast pairs are not a page-level WCAG conformance result. This study does not establish the color system for the later dispatch workspace.

These artifacts explain the product-design evolution: retain useful site/evidence/tariff/recommendation capabilities from the earlier broad workspace, but give the economic source/load comparison the primary workflow position specified by PR #10. The dedicated v1.9 six-stage flow and v2.9 mixed-claim result study provide the later synthetic interaction evidence described above; neither converts the early prototype/palette into an approved or implemented product.


## v3.3 exact-head workflow and product-claim update — 2026-10-07

The previous sections' v1.9/v2.7/v2.9 evidence remains valid for those exact artifacts, but is no longer the latest PR #10 prototype state. PR #10 is now open, draft and unmerged at head a7bef59f2cdb2466dd08397dd6ffe880ec66f07d; main remains at the PR base a897bf0b1e7e6ceea3862d7d87fa288ecca08203. The complete v3.3 prototype and review are under docs/02-product/prototype/source-load-dispatch/v3.3/.

| Stage | v3.3 evidence | Remaining product/runtime gap |
|---|---|---|
| 1. Data/contract qualification | Required evidence categories and unresolved states are visible. | No trusted tenant/site authorization, source registry, user data repair or effective-dated evidence intake. |
| 2. Physical model | Physical source/load topology is visually separated from settlement mapping. | Conceptual only; no site-verified topology, meter boundary, overlap/ownership or export evidence. |
| 3. Schedule comparison | Chart and six-row schedule derive from pinned PR #14 fixture; 44→44 kWh and 10→11 kW are fixture-derived. Optimizer assumed-rate objective is now disclosed. | Scenario-only assumptions, no valid Macau tariff or site service model. Does not prove customer-specific economic optimum. |
| 4. Costs/claims | Reads fixture claim states; economic status BLOCKED. UI-only partial coverage explicitly identifies four covered intervals (09:00–13:00) and two uncovered (13:00–15:00), shows no amount and does not treat missing intervals as zero. | Partial view is not produced by the fixture/optimizer; no bill-grade economic evaluator or result API is connected. |
| 5. SHADOW review | Page-local review choices visibly update. | No authenticated or durable review, immutable decision history or command authorization. |
| 6. Monitoring/replay | Lists evidence/version requirements. | Descriptive only; no measurement ingestion, replay, reconciliation or M&V. |

This extends UI evidence beyond static v3.2, but it is not the T7 vertical slice in the implementation backlog. No API, persistence, authorization, service integration or replay is present. The local static validator checks fixture source pins, energy/peak totals, PV and bus balance, withheld claims and UI/fixture boundary. Browser checks covered all six stages, Chinese/English/Portuguese draft text, actual/partial state selection, page-local review, console errors and viewports 320/375/768/1024/1440; the 320px table stays in its scroll container. These checks do not establish operator validation, WCAG conformance, site/tariff truth or production readiness. Exact evidence: v3.3/REVIEW.md and the three successful exact-head workflow runs on a7bef59: Repository Hygiene #1555, Dispatch Projection Validation #47, Authority Validation #1556. Those checks validate repository rules and fixture semantics only.

### Decision-D and T7 implication

PR #14's generated fixture candidate uses assumed sample import rates, while the owner decision packet recommends D1 as the interim MVP boundary: assess supplied schedules and do not generate a product candidate without an approved objective/economic context. v3.3 deliberately displays the experiment but labels its assumptions; it does not choose D3 or supersede D1. A future implementation must keep the fixture isolated as research data until D1/D2/D3 is decided.

**T7 remains not implemented.** The prototype supplies a browser/fixture view only; T7 acceptance still requires contract, domain, security, integration, browser and replay evidence against the same pinned build, durable review, independent reconstruction and aligned API/UI states. T0/T1/T2–T6 dependencies and owner decisions are unchanged. Do not close G7.9 Step 3 from this prototype or passing Actions.
