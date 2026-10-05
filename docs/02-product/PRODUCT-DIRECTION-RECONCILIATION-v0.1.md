# Product Direction Reconciliation v0.1

**Date:** 2026-10-05  
**Status:** Evidence-based reconciliation for owner review. This document does not approve or freeze product scope, navigation, visual direction, locale scope, or production architecture.

## Finding

The product direction did not first become dispatch-first in the later prototype. PR #8's research-derived product baseline already defines **economic source/load dispatch** as the primary task, with portfolio and site overview as supporting areas. Its PRD, product design, and information architecture say so directly.

The early v0.10 prototype and palette study do not communicate that hierarchy clearly: both center a portfolio/evidence overview. They are incomplete UI expressions of the product proposal, not evidence that the product thesis itself was a generic dashboard. PR #10's source/load workflow prototype addresses this mismatch by making qualification, site model, schedule comparison, economics/evidence, SHADOW review, and monitoring/replay the visible workflow.

This is an alignment assessment, not a claim that the product design is approved or validated with customers.

## Source-to-artifact trace

| Artifact | Branch / exact file | Evidence | What it establishes |
|---|---|---|---|
| PRD v0.1 | PR #8, `docs/02-product/PRD-v0.1.md`, blob `22b129baf1a7c3d0cf11069d9f23fb414908d1d7` | Sections 1, 3 and PR-10 explicitly describe evidence-bounded economic source/load dispatch across grid imports, on-site PV, ESS and site-qualified flexible loads. | Dispatch is already the intended primary product task in the written proposal. |
| Product design baseline | PR #8, `docs/02-product/PRODUCT-DESIGN.md`, blob `4726a5bb7b74711054cee5eda056f2bd51c3da33` | “Primary product task: economic source/load dispatch”; portfolio/site overview is listed as supporting. | The written product design distinguishes the primary workspace from supporting overview pages. |
| IA and user flows | PR #8, `docs/02-product/USER-FLOWS-AND-IA-v0.1.md`, blob `41082c28d41386303fc991ba1217b3f7ba9f0e08` | Flow B and S-10 are the primary source/load scheduling workflow; S-01 portfolio overview is supporting. | The information architecture already places dispatch at the center of the intended operator workflow. |
| Prototype v0.10 | PR #8, `docs/02-product/prototype/v0.10/index.html`, blob `5d148b4990e353c7a400b7401216066f35ed68cf` | The first page is “Portfolio overview”; visible navigation emphasizes portfolio, sites, data health and recommendations. | The rendered concept starts from portfolio readiness and does not make the dispatch task the dominant entry point. |
| Visual direction study v0.1 | PR #8, `docs/02-product/prototype/visual-directions/v0.1/index.html`, blob `986f7f6bd1f7c01506ac6cc41a3b3430d9d8309c` | Harbor Teal, Mineral Blue and Night Graphite are compared on a synthetic portfolio-overview task; the file says no direction is selected or user-tested. | This is a palette comparison stimulus, not an approved dispatch visual system or a product-direction decision. |
| Product/architecture review packet | PR #8, `docs/02-product/PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md`, blob `8fb6da1d40cfb88f48d6b4238ef7d9dd4def9f5e` | Calls dispatch-first the current user-directed proposal; explicitly says scope, stack, visual direction and production architecture remain unapproved. | It records the distinction between user direction and owner-approved baselines. |
| Project UI/UX skill draft | PR #8, `.agents/skills/macau-energy-os-ui-ux/SKILL.md`, blob `3b61a9fa66dae0681c0fc6af6a834256685cfdb0` | The skill draft is present on PR #8. | The project-specific guidance is proposed on an open branch; it is not part of main until merged. |
| Dispatch workflow v1.0 | PR #10, `docs/02-product/prototype/source-load-dispatch/v1.0/index.html`, blob `d896378094cc1c26fd762829cd5dbe5247b7e94f` | Six-stage source/load workflow; synthetic data, unverified billing rules, and SHADOW-only review are visible. | This prototype makes the written primary task visible. It does not establish product approval, site feasibility, measured savings, or control capability. |
| v1.0 review | PR #10, `docs/02-product/prototype/source-load-dispatch/v1.0/REVIEW.md`, blob `1885868badeb1a76de641a134434101c215585fb` | Records 1440, 1024, 768 and 375 CSS-pixel renders, mobile interval-summary/table checks, and remaining page-length, locale, assistive-tech and operator-validation gaps. | The claimed review is bounded to the documented synthetic prototype and checks. |

## Current GitHub state checked 2026-10-05

- PR #8, branch `docs/product-architecture-roadmap`, head `ce362b1d10bfe97b743261ca9507be591af1cddf`: open, ready for review, unmerged. Its PRD, detailed design, prototype sequence and project UI/UX skill therefore remain proposals outside main.
- PR #10, branch `product/source-load-economic-dispatch`, current head `0925aad35f2a8bd5cfaf73581c78a66ed67af56f`: open, Draft, unmerged. The v1.0 HTML and this reconciliation are present on the branch. Exact-head Authority Validation [run #37251804768](https://github.com/lilinling12/macau-commercial-energy-os/actions/runs/37251804768) and Repository Hygiene [run #37251804725](https://github.com/lilinling12/macau-commercial-energy-os/actions/runs/37251804725) both passed. These checks establish authority-path and repository-hygiene results, not product approval, visual quality, full feature validation, or pilot readiness.
- Exact text comparison of the local v1.0 output and the GitHub v1.0 source normalized for line endings and trailing newlines: equal. The v1.0 review claims refer to that prototype content.
- Original shared ChatGPT dialogue remains unavailable in full in this task. This reconciliation uses the cited repository artifacts and does not claim to reconstruct unseen conversation turns.

## Product-design assessment

### What is aligned

1. The written proposal treats dispatch as the core operator job: qualify inputs, establish the physical site model, compare a same-horizon baseline and candidate, show constraints and evidence, calculate economics only where eligible, record a non-executable SHADOW review, then monitor/replay.
2. Grid import, on-site PV, ESS and site-qualified flexible loads appear in the dispatch proposal, with physical flow kept distinct from tariff/account settlement.
3. The v1.0 prototype carries the dispatch comparison into a visible workflow and avoids requiring mobile users to pan a wide chart to read all six interval summaries.

### What is not yet complete or approved

1. The v0.10 and palette study remain portfolio-first stimuli. Do not present them as proof of a completed dispatch-centered UI or a selected color system.
2. v1.0 is a single synthetic workflow prototype, not a complete production product design. It does not prove representative-user task success, complete localization, WCAG conformance, touch behavior, or pilot readiness.
3. The v1.0 review documents a 3,125px mobile page at 375px width; replacing the chart with interval summaries improves access to interval values but does not resolve the full page-length question.
4. The project UI/UX skill, product requirements, and design documents are on PR #8, which is still unmerged. The proposed design has not become the repository's main-branch operating standard.
5. Owner decisions and site evidence still govern the first supported outcome, pilot resource eligibility, language scope, selected visual direction, and production architecture.

## Recommended next product-design work

1. Keep the dispatch-first proposal as the working design direction because it is present in the research-derived PRD and current user direction. Mark it **proposed / awaiting owner review**, not approved.
2. Rework the primary navigation and page composition around the dispatch task. Keep portfolio/site readiness as a supporting overview and evidence entry point.
3. Continue from v1.0 with a staged operator workflow: improve progressive disclosure and page length; keep physical and settlement evidence in separate, explicit sections; preserve a table alternative and show affected-claim limits beside each result.
4. Produce rendered, comparable visual options for the dispatch task itself before selecting colors, typography or a component system. Do not select a palette from the portfolio-only palette study.
5. Validate full Traditional Chinese, Portuguese and English task flows only after locale scope is confirmed, including units, dates, decimal/currency formatting, terminology and missing/blocked states.
6. Test the task with representative operators and domain reviewers before claiming workflow validation. Keep all schedules synthetic until site, contract, equipment and measurement evidence qualifies a real site.

## Decision boundary

This review concludes that the written research-derived product direction and the dispatch-first proposal are aligned; the earlier v0.10 presentation is behind that written direction. It does **not** conclude that the overall product design is complete or approved. The owner must review the first pilot outcome, user/role assumptions, initial site/resource scope, locale priorities and visual direction before those become baselines.


## Current-state correction — 2026-10-05 (v1.6 and live PR heads)

The sections above retain the v1.0 checkpoint and its contemporaneous evidence. Rechecking current branch contents shows that v1.0 is no longer the latest dispatch prototype.

### Current research-derived product direction

At PR #8 head `98e510700cf65be94a729ed01e81d9e8754d6c82`, `PRD-v0.1.md` (blob `22b129baf1a7c3d0cf11069d9f23fb414908d1d7`), `PRODUCT-DESIGN.md` (blob `4726a5bb7b74711054cee5eda056f2bd51c3da33`) and `USER-FLOWS-AND-IA-v0.1.md` (blob `41082c28d41386303fc991ba1217b3f7ba9f0e08`) already make economic source/load dispatch the primary operator task; portfolio/site overview is supporting. PRD PR-10 calls for shared-horizon source/load schedule comparison across grid imports, on-site PV, ESS and site-qualified flexible loads, while withholding bill-grade totals and savings when tariff, demand-window, contract or settlement evidence is unresolved. The user-flow draft explicitly separates physical topology from settlement links and keeps review non-executable SHADOW. PR #8 remains open, Ready for Review, and unmerged, so this is a research-derived proposal on a branch, not an approved/frozen product baseline.

### Current dispatch prototype and evidence

At PR #10 head `3ae590b0823f70802f4fe8a53020c018aaf41a21`, the latest prototype is v1.6: HTML blob `f16a80df67ae4504751d0a46473f181aa86cdcbb`, review blob `91cfacbe6e17e8f79a5baf670d4555c9c24d1b80`. It preserves the six-stage flow—data/contract qualification, physical site model, same-horizon schedule comparison, economics/constraints/evidence, SHADOW review, and monitoring/replay—while improving navigation and narrow-screen site context. Scenario values remain synthetic. It does not implement real onboarding, a production Energy Graph, forecasting, schedule generation, persisted review, monitoring or replay.

The v1.6 review records renders at 1440×1000, 1024×900, 768×900, 680×900, 375×844 and 320×844 CSS px. Document width matched the viewport; mobile navigation labels and 50×50 px targets were checked; desktop targets are recorded as 44 px high. It checked accessible navigation names, current-page state, skip-link-first keyboard focus, visible focus outline and JavaScript page errors, and visually inspected desktop/mobile screenshots. These are bounded checks, not full keyboard, touch, screen-reader, contrast, text-scaling, WCAG-conformance, usability or production validation.

Traditional Chinese is the only fully represented prototype locale. Portuguese and English remain unimplemented in this workflow; full three-language terminology, dates, number/currency, error and blocked-state coverage needs localization review. UI/UX Pro Max and the project skill informed the review, but its generic marketing-style recommendation was rejected for this operator workflow. Apple HIG, Material 3, WCAG 2.2, Awwwards, Webby and FWA are documented as principles/quality references; no award-level quality, user validation or final visual direction is claimed. The earlier v0.10 and palette study remain portfolio-first stimuli and do not select the dispatch product's palette.

### Live repository state and next alignment work

PR #10 is still open, Draft and unmerged; exact head above. Its latest added G7.9 map crosswalk is in commit `3ae590b0823f70802f4fe8a53020c018aaf41a21`; exact-head Authority Validation and Repository Hygiene both passed (runs `37271169821` and `37271169744`). These checks do not approve the product or prototype. PR #8 remains open and unmerged; PR #10 is an additive focused proposal, not a replacement for the PR #8 PRD/IA.

The original shared page was opened in the browser and exposed some Phase B/Phase C outputs, but portions showed “Failed to fetch template.” Treat the source as partially accessible only; no claim is made that every turn, attachment or generated file was read.

Next product-design work is to reconcile the full dispatch workflow into the complete operator shell, preserve evidence/status and physical-versus-settlement boundaries across every state, and validate language coverage and workflow with representative domain users. Keep product scope, first-pilot resource eligibility, visual system, locale priority and technical architecture proposed until reviewed. Do not infer operational scheduling capability from the synthetic prototype or the separate PR #14 optimizer experiment.


## Current prototype correction — v2.3 exact source (2026-10-05)

The earlier current-state section above records v1.6 as the latest at its review time. That statement is historical and is no longer current. PR #10 now contains v2.3 HTML blob `6f199ddaee1f2a416b9925ce310a073b0455b054`, with a separate exact-source review `e93643559a9261ad340f7c2d0b998276252283c1`.

v2.3 advances the **presentation of mixed readiness**: four synthetic supplied-schedule cases can independently show physical, HVAC/service, ESS, economic and claim states. The user can inspect why a claim is allowed, partial or withheld. In the no-tariff case the prototype says no optimized candidate is generated; in the partial-rate case, only independently covered energy components may be represented. The claim decision and claim scope are separate dimensions. Static fixture parity and source-level JavaScript checks are recorded in the v2.3 review.

This is a refinement of the six-stage dispatch-first product proposal, not completion of the end-to-end operating workflow. The v2.3 case selector is disconnected from PR #14, a server/API, site/contract registry, authenticated evidence, forecasts, optimizer execution, persisted SHADOW decisions, monitoring and replay. It evaluates supplied synthetic schedules for the demonstration; it does not generate a live or site-qualified dispatch plan. Therefore the prototype does not yet prove the product can coordinate grid imports, PV, ESS, HVAC, EV and hot-water loads under a Macau site's verified commercial objective and operating constraints.

The exact v2.3 review still records **no browser rendering or interaction session** for this version. It does not establish viewport behavior, keyboard transitions, screen-reader output, full-page contrast, WCAG conformance, operator usability or site validity. Earlier prototype-version renders and checks are not evidence for this exact v2.3 HTML.

The checked-in v2.3 localization candidate contains 489 source/context units. Its source-pinned integrity validator reports no catalog/source errors, while Portuguese and English coverage remain 0/489 each. This is an extraction inventory only: no complete translations, runtime locale switching, localized date/number/currency formatting or multilingual rendered review is established. Locale scope is unapproved.

### Product and implementation conclusion

- The dispatch-first product direction remains a **research-derived proposal consistent with user direction**, not an owner-approved product baseline.
- v2.3 improves claim explanation and truthful mixed-state presentation; it does not resolve the gap between synthetic UI, the separate bounded Python optimizer, and an integrated durable product workflow.
- Keep the visible user workflow as qualification → site/energy model → comparable schedules → separate physical/economic constraints and evidence → SHADOW review → monitor/replay. Each transition needs an explicit state and recoverable reason. The prototype currently demonstrates only a small synthetic slice of the result-explanation step.
- Next product evidence should first connect one immutable assessment fixture to a typed result adapter and verify that the UI renders the same result/claim states. That integration must remain synthetic and SHADOW-only until G7.9 ownership/contracts, security review and site evidence are approved. In parallel, complete v2.3 browser/keyboard review against the exact source; do not describe those checks as user validation.
