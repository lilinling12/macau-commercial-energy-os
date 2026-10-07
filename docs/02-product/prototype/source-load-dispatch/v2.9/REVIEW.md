# Source/load dispatch prototype v2.9 — review record

**Review date:** 2026-10-07  
**Scope:** Browser and interaction review of the v2.9 design prototype on PR #10. This is design evidence for a synthetic SHADOW scenario, not a product acceptance or site-validation record.

## Reviewed source

- PR: [#10 — Source/load economic dispatch proposal](https://github.com/lilinling12/macau-commercial-energy-os/pull/10), branch `product/source-load-economic-dispatch`.
- Prototype: `docs/02-product/prototype/source-load-dispatch/v2.9/index.html`, blob `a19472d11fcbdf39afde64fcc8d0d9bf2f1c4457` at the reviewed prototype commit `1a577680e7ac1e11069d812df9afe85e8e06f90c`.
- Fixture: `docs/02-product/prototype/source-load-dispatch/v2.9/dispatch-projection-fixture.json`, blob `fec75272470155c531a1747ddf00db91ec00c583`. It is the same synthetic fixture blob used by v2.8; values are project assumptions, not Macau site evidence.
- Locale candidates shown: Traditional Chinese (`zh-Hant`), English (`en`), and Portuguese (`pt`). The document language tags use neutral language identifiers; the Portuguese option is visibly marked as a draft. This does not establish a Macau Portuguese regional variant, product locale approval, or complete localization.

## What was reviewed

The scenario puts grid import, on-site PV generation/self-use, ESS charge/discharge and SOC, and HVAC/EV/hot-water task schedules in one six-interval view. The table explicitly separates PV generation/self-use from export/settlement. The scenario reports 44 → 44 kWh horizon import and 10 → 11 kW horizon import peak; the period peak is not described as billing demand or Pu. Assumed hourly import rates inform a bounded search objective, but bill assessment is withheld because the account, contract, and tariff applicability are unverified.

Export compensation, full-bill amounts, realized savings, equipment controllability, service/comfort feasibility, cross-site credits, and device control are withheld. The review controls are page-local only, have no service submission or field-action path, and reset on reload.

## Rendered viewport matrix

Reviewed in the in-app browser at CSS viewport sizes **320×800, 375×812, 768×900, 1024×900 and 1440×900** for each of the three locale candidates (**15 locale/viewport combinations**).

- In all 15 combinations, document and body scroll widths stayed within the viewport; no page-level horizontal overflow was observed.
- The 900 px-wide interval table scrolls horizontally inside its labelled data region at narrower sizes (for example, region client widths of 271 px at 320 px viewport and 326 px at 375 px viewport). It does not widen the page. The chart uses its own horizontal scroll region when its 550 px minimum content width exceeds the available width.
- At 1024 px the main view retains the two-column chart/evidence layout; at 768 px and below the evidence column stacks under the chart. At 620 px and below the header and summary cards stack.
- Each candidate language rendered its translated heading, scenario content, claims, review text and footer. This is a coverage check of this single page only, not a translation-quality or end-to-end locale audit.

## Interaction and accessibility observations

- Replaced three mutually exclusive `aria-pressed` buttons (which the browser accessibility snapshot exposed as checkboxes) with a native fieldset and radio group. The group legend is translated with the selected language.
- In the rendered page, the accessibility tree exposed three radio buttons under the localized group label. Space selected an option; Arrow Down moved the exclusive selection to the next option. The live status text updated. Switching to Portuguese retained the in-page selection and translated its status; reloading restored the empty state.
- Visible focus styling, a skip link, descriptive chart text plus the precise interval table, line style and point shape in addition to color, and a reduced-motion CSS rule are present in source. These checks do not establish WCAG conformance or a complete screen-reader experience.
- Spot-checked foreground/background contrast from the source tokens using the WCAG relative-luminance ratio calculation: primary text `#142d3a` on white **14.32:1**; muted text `#526873` on white **5.86:1**; teal `#087d73` on white **5.01:1**; warning text `#634a1c` on `#fff5df` **7.67:1**; review-state text `#315f57` on white **7.23:1** and `#785518` on white **6.75:1**; focus ring `#126e93` on white **5.71:1**. The grey-blue `#647b86` is used for chart strokes/markers, not small text; it measures **4.45:1** on white and should not be reused for normal-sized text on white without adjustment. This is a sampled source-token check, not a complete contrast audit across every state and background.

## Remaining validation

- Macau energy-domain and Portuguese terminology review; locale selection and regional Portuguese variant remain owner/domain decisions.
- Full translation review for every product screen, keyboard coverage beyond the tested radio group, assistive-technology testing, zoom/reflow testing, and an end-to-end reduced-motion review.
- Real site, meter topology, contract, applicable tariff, PV settlement, equipment service limits, forecast quality, optimizer feasibility and operator validation.
- The prototype remains synthetic and SHADOW-only. No optimizer/API integration, persistence, user testing, field control, savings claim, Gate closure, or production readiness is established.


## Current source regeneration and fixture lineage — 2026-10-07

The projection JSON was regenerated by PR #14's pinned source tool, [generate_dispatch_projection_fixture.py](https://github.com/lilinling12/macau-commercial-energy-os/blob/poc/shadow-dispatch-assessment/implementation/optimizer/tools/generate_dispatch_projection_fixture.py), and synced from its committed output fixture. The generator checks the exact optimizer and assessment Git blob fingerprints before constructing the scenario; PR #14 adds an automated test that compares deterministic generation with the committed fixture.

- Engine source commit: 9b80adca9243a0ae9a7bd666f0efee1acfc6309a.
- Optimizer source blob: 2d3256801f0ddce6b849c648c160f5a32fd90a27.
- Current assessment source blob: 534ae269a7949601bd4504271e0076369807a68f.
- PR #14 generated fixture blob: 0e746cbe54532e58221529f38c7a2583d1787c4b.
- Synced v2.9 UI fixture blob: 0e746cbe54532e58221529f38c7a2583d1787c4b.

A normalized comparison confirmed the generated and prior v2.9 fixture had identical inputs, schedules, statuses, claims and metrics; only the source commit/assessment fingerprint had changed. The v2.9 display values therefore did not change. PR #14's exact head deed7683a8b0ce3a811966ab8fc3b030695debad passed its Optimizer job, including the new reproducibility test, plus Contract Fixtures, Platform API, Edge Runtime, Repository hygiene and Validate authority structure. The local exploratory run used Python 3.11.9, below the project's declared Python 3.14 requirement, and lacked a complete IANA timezone database; it is not used as target-runtime evidence.

This closes the previously recorded **source-lineage mismatch** for this pinned synthetic fixture only. The browser page still loads a static JSON file and is not connected to an APP-11/API service, durable review, authenticated evidence or site data. No optimizer-to-UI runtime integration, Macau economics, service feasibility, user acceptance, savings or pilot readiness is established.
