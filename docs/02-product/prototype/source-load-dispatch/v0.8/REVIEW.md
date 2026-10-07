# Prototype v0.8 browser review

**Review date:** 2026-10-05  
**Purpose:** Check the dispatch-window versus billing-period Pu distinction, responsive layout, core prototype interactions, and obvious visual issues. This is source/render review evidence, not product approval.

## Exact source

- Repository: `lilinling12/macau-commercial-energy-os`
- Branch: `product/source-load-economic-dispatch`
- Reviewed commit: `f65fb2a68f7608bb1680837fa999e52954bc1fe8`
- File: `docs/02-product/prototype/source-load-dispatch/v0.8/index.html`
- GitHub Contents API blob SHA: `4e87ff38e69f429ca158e0959fc8ec0b428874d4`
- The fetched branch file was saved locally and rendered as a file URL in Microsoft Edge using Playwright.

## Scope and observed results

| Viewport (CSS px) | Document width | Resource-card layout | Result |
|---|---:|---|---|
| 1440 × 1000 | 1440 | 3 columns | No page-level horizontal overflow |
| 1024 × 900 | 1024 | 3 columns | No page-level horizontal overflow |
| 768 × 1024 | 768 | 2 columns | No page-level horizontal overflow |
| 375 × 844 | 375 | 1 column | No page-level horizontal overflow |

At these widths the four dispatch inspection metrics render in 4, 2, 2 and 1 columns respectively. The source uses separate horizontally scrollable table regions for wide interval data.

Verified wording and state boundaries:

- The former “全時段” wording is absent. The 485 → 510 kW maximum is named as the maximum within the **display window**.
- The CEM current-billing-period Pu is explicitly unknown; the Pu averaging/measurement window is also unknown.
- The page says that the synthetic display-window maximum is not billing-period Pu and makes no bill, demand-charge, saving, export-credit, or cross-site-netting claim.
- EV and hot-water loads are marked ineligible for this synthetic candidate because their evidence is missing.
- The page states that there is no site connection, persisted approval, command authorization, equipment execution, or measured outcome.

Exercised interactions:

- Workflow navigation updates the current-step state after selecting “Site model”.
- Candidate selection updates `aria-pressed` and the chart emphasis; it is page-local.
- The interval data table opens and exposes `aria-expanded=true`.
- REVIEWED, REQUEST_EVIDENCE and DISMISSED are mutually exclusive; reloading resets the demonstration state.
- A tested action has a visible 3 px focus outline.
- No page JavaScript errors were observed.

## Visual review findings

The core domain distinction is materially clearer than in v0.7, and the workflow contains source/load balance, PV, ESS charge/discharge, HVAC shift/rebound, evidence blockers, SHADOW review and outcome/replay boundaries.

The current page is still a **long-form single-page workflow prototype**, not a settled operator-console information architecture:

- The full-page render is about 4,419 CSS px high at 1440 px width and 7,555 px high at 375 px width. It requires substantial scrolling through six stages even though jump links exist.
- At desktop width, the tall right-side review stack leaves a large unused area beneath the dispatch chart before the next workflow section.
- Several secondary/mobile labels and explanatory text are 10–12 px. They are legible in the rendered file at the tested scale but need a readable-text pass, zoom/text-enlargement review, and localization-length checks.
- The rail uses typographic glyphs as icons; replace or validate these against a consistent labeled icon system in a later visual iteration.
- The current palette and card treatment remain prototype styling; no visual direction is selected.
- The screen includes a synthetic schedule comparison, not a forecast model or a production optimizer. The product design must surface forecast availability/quality and withhold optimizer claims when the required forecast is missing.

These findings suggest the next prototype iteration should test progressive disclosure or a focused stage workspace, reduce the desktop dead zone, improve mobile reading density, and explicitly show forecast readiness. That is a design hypothesis for review, not an approved production direction.

## Design guidance used

- UI/UX Pro Max responsive guidance: contain wide tables within an overflow region; preserve readable text and touch controls on narrow screens.
- UI/UX Pro Max time-series chart guidance: use direct labels and non-color encodings and provide a visible tabular alternative.
- Project skill draft `.agents/skills/macau-energy-os-ui-ux/`: keep scenario/synthetic states distinct, put time/source/unknown evidence near the decision, distinguish operator-console needs from marketing patterns, and record locale and validation limits.
- Apple HIG layout guidance emphasizes hierarchy, deliberate grouping, progressive disclosure and adaptable layouts. This review identifies the long page and desktop dead zone as iteration areas; it does not claim compliance with Apple platform guidance.
- References reviewed: [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/), and project-skill references to [Material 3](https://m3.material.io/foundations/), [Awwwards judging](https://www.awwwards.com/), [Webby judging criteria](https://www.webbyawards.com/judging-criteria/), and [FWA](https://thefwa.com/). No award-site case study was used as a design template in this review.

## Limits

This review covers Traditional Chinese only and four viewport sizes. It does not establish WCAG 2.2 conformance, measured contrast, full keyboard coverage, screen-reader behavior, language completeness, representative-user/operator usability, real-site or tariff correctness, dispatch feasibility, optimizer quality, savings, or production readiness. No customer site or live system was accessed.
