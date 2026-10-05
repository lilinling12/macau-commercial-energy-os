# Source/Load Dispatch Prototype v2.6 — Separate Status and Schedule Studies

**Status:** Unapproved, UI-only synthetic study. No production product scope, visual direction, API, architecture, feasibility, or control behavior is approved by this prototype.  
**Base:** PR #10 v2.5, HTML blob `07e309c69f6eb4487d955d095eca124945c63d8c`.  
**Purpose:** Make the separation between the four synthetic evidence/status examples and the independent fixed source/load schedule example unmistakable at both control groups.

## Change

The four-button selector updates only the physical, HVAC, ESS, economic, and claim presentation examples. It does not change the schedule curve or interval table. The v2.5 copy already disclosed that these were separate studies; v2.6 strengthens the boundary by renaming the selector and adding a direct note beside the schedule title. No case data, schedule values, claim semantics, palette, or workflow stage was changed.

This is a clarity improvement, not integration: the displayed schedule remains one fixed synthetic schedule illustration, not the output of any of the four status cases, an optimizer, or a site assessment.

## Design review basis

- Followed the project-specific `macau-energy-os-ui-ux` skill draft and its energy-operations/quality-review references from PR #8 head `9e3dec0bccf5acb5122f94c688814e7f4e026a1b`. PR #8 is still unmerged, so this is a review basis rather than active main-branch authority.
- Ran `ui-ux-pro-max` chart search for “energy dispatch operator scenario consistency”: 0 matches. Retried “scenario operational”; the single result was an anomaly-monitoring chart pattern and did not fit this task, so it was not applied.
- The UX search for “scenario selection live result feedback” returned contextual live-status guidance. The existing case summary already uses `role=status`, `aria-live=polite`, and `aria-atomic=true`; the updated control keeps native buttons and `aria-pressed`.

## Browser review — 2026-10-06

Reviewed the local v2.6 copy in Microsoft Edge / Playwright at **1440×900, 1024×900, 768×900, 375×812, and 320×800 CSS px**.

- Selected all four evidence/status cases at every viewport (20 case/viewport combinations).
- Each selection updated its status summary and claim rows; exactly one case button remained `aria-pressed=true`.
- The schedule SVG paths, mobile schedule summary, and interval table remained byte-for-byte equivalent in the DOM across the four status examples. This confirms the documented independence; it does not claim that the studies are integrated.
- Document width equalled viewport width at all five viewports; no document-level horizontal overflow was observed.
- Keyboard Space activated the no-tariff case and updated its summary. No JavaScript page errors were recorded.
- Fixture metadata remains `apiConnected=false` and `deviceControlEnabled=false`.

## Limits and remaining work

This remains a Traditional Chinese-only synthetic interface study. Portuguese and English localization were not tested; language selection and locale-specific units/currency/date formatting are not implemented. No screen-reader session, full WCAG 2.2 AA audit, contrast measurement, operator interview, or task-based usability study was performed.

The chart still contains a fixed candidate example while the no-tariff status example says that its case does not generate a candidate. v2.6 now labels these as independent examples at the selection and chart points, but it does not provide a unified result object. The next product-design step is to define and approve the canonical assessment/result view model and fixture-to-screen mapping before connecting UI to an optimizer/API. PR #14 remains a bounded experimental evaluator; it is not a canonical contract or integrated product.

This prototype does not establish a real Macau site, tariff, PV settlement right, savings, equipment controllability, dispatch feasibility, or device-command path.
