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
- PR #10, branch `product/source-load-economic-dispatch`, head `754e7ca8da57096af27ff1458a491220c4289475`: open, Draft, unmerged. The v1.0 HTML is present on this branch. The combined-status lookup returned no status records; this is unavailable status evidence, not a pass.
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
