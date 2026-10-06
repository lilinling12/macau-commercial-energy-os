# Source/load dispatch result projection — v2.8

**Status:** review prototype; not an approved product design or production UI.  
**Source:** PR #14 exact head `d5180703df3730779f1f180a89d07c620e7e349d`; exact optimizer and assessor source were previously blob-verified in the task workspace.  
**Data:** `dispatch-projection-fixture.json`, regenerated from the pinned PR #14 source; every input is `PROJECT_ASSUMPTION`.  
**Purpose:** replace the v2.7 fixed presentation schedule with an inspectable projection of one actual bounded PR #14 generated result.

## What the page demonstrates

- Baseline and generated candidate grid-import profiles over six one-hour Macau-time intervals.
- On-site PV used, ESS charging/discharging and state of charge, and aggregate HVAC/EV/hot-water task energy placement.
- Scenario-period totals and peak shown as a trade-off: 44 kWh import in both schedules; peak import changes from 10 kW to 11 kW. The peak is explicitly not a billing-period demand/Pu result.
- Economic result shown as **not calculated**. The supplied rates are assumptions, so no charge, full bill, savings or export compensation is displayed.
- Claim eligibility and scope remain distinct. Scenario-only physical outputs stay qualified; comfort/service, controllability, cross-site credit and device-control claims remain withheld.
- Assumptions, search resolution, search-state count and omitted models are available by progressive disclosure.
- The primary result view states that the search minimizes the supplied interval import-energy rates, and that these unverified assumed rates do not establish a Macau-contract economic optimum.
- Physical result scope is explicitly shown as synthetic scenario only, separately from the uncalculated/blocked economic result.
- Review choices update page-local text only and disappear on reload. No API, persistence, approval record, optimizer invocation, customer/site evidence or device command is connected.

## Source result summary

| Local interval | Baseline / candidate grid import | PV generation · baseline→candidate self-use | Candidate ESS | Baseline → candidate flexible tasks |
|---|---:|---:|---:|---|---|
| 09:00–10:00 | 8 / 9 kW | 0 · 0→0 kW | charge 1 kW; SOC 5→6 kWh | — → — |
| 10:00–11:00 | 8 / 9 kW | 0 · 0→0 kW | charge 1 kW; SOC 6→7 kWh | — → — |
| 11:00–12:00 | 6 / 11 kW | 2 · 2→2 kW | charge 1 kW; SOC 7→8 kWh | — → HVAC 2, EV 1, hot water 1 kW |
| 12:00–13:00 | 4 / 3 kW | 4 · 4→4 kW | discharge 1 kW; SOC 8→7 kWh | — → — |
| 13:00–14:00 | 8 / 5 kW | 2 · 2→2 kW | discharge 1 kW; SOC 7→6 kWh | HVAC 1 + hot water 1 kW → — |
| 14:00–15:00 | 10 / 7 kW | 0 · 0→0 kW | discharge 1 kW; SOC 6→5 kWh | HVAC 1 + EV 1 kW → — |

The optimizer searches exactly only within the declared discrete action grid and bounded horizon (5,706 transitions). It preserves the supplied aggregate service-energy quantities and terminal SOC. The example does not model thermal response/rebound, an EV departure requirement, hot-water temperature/service, equipment safety interlocks, forecast uncertainty, or billing-period demand charges. “Feasible” must therefore never be generalized beyond the supplied scenario constraints.

## UI/UX method and quality bar

The `ui-ux-pro-max` skill was applied. Its design-system search for a commercial energy dispatch workspace returned an Organic Biophilic / Trust & Authority conversion pattern, wide futuristic typography and marketing calls to action. Those results fit an acquisition site, not a sustained operator comparison, so they were rejected rather than copied. The targeted chart search supports time-series comparison with a visible table fallback, direct series labels/styles and no hue-only encoding. The UX search supports visible keyboard focus and keeping focused elements visible around persistent content.

This page uses an original calm analytical treatment: restrained ink/canvas surfaces, explicit scenario warnings, source labels, a solid candidate versus dashed baseline, exact interval rows and a persistent distinction between physical status and economic qualification. It avoids a generic landing-page hero/CTA and avoids representing a blocked monetary claim as zero. The palette is exploratory; no product-wide design system or final color direction is frozen.

## Local interaction and responsive review

- Language: Traditional Chinese only. This is a single-language prototype, not complete Chinese/Portuguese/English localization.
- Layout intent: two-column desktop comparison and evidence rail; one-column tablet/mobile flow; contained chart/table scrolling rather than page-wide overflow.
- Keyboard: skip link, visible focus, labelled scroll regions, native disclosure control, and button-based review choices. No drag/hover-only actions.
- Motion: no meaning-bearing animation; reduced-motion preferences are respected for any browser/user-agent transition.
- Chart: source series differ in line style and point marker as well as color; the visible table carries exact values.
- External evidence/contract state: all synthetic; no user or operator validation has occurred.

### Browser observations — 2026-10-07

- Opened the saved page in the Codex in-app browser with the local fixture. Its narrow embedded screenshot exposed a wrapped brand/header; the header now stacks the brand and scenario labels below the narrow breakpoint.
- The first interval-table screenshot showed header text squeezed into very narrow columns. The table now keeps a readable minimum width inside its own horizontal-scroll region; the page content remains within the captured viewport, with horizontal scrolling contained to chart/data regions.
- A direct raw-source read of the PR #10 v2.7 HTML returned 1,676 Unicode replacement characters, affecting the Chinese interface copy. v2.8 was authored as a new version in UTF-8 rather than carrying the damaged strings forward; v2.7 remains an immutable historical study until the owner chooses how to treat it.
- Opened the assumptions disclosure and verified the exact six rate assumptions, task quantities, time zone and 5,706 transition count in the accessibility tree.
- After reviewing the exact PR #14 optimizer source, a source-backed search-objective caveat was promoted into the primary result summary. A fresh browser/AX review confirmed the visible objective, `物理結果 · 僅限合成情景`, 44→44 kWh, 10→11 kW, and separate `未計算` economic state.
- Selected “需要現場／合同證據” and verified the local-only review message. Reload returned the control and message to their initial state, confirming there is no persistence.
- Keyboard sequence verified through the focused controls: skip link → chart scroll region → interval-table scroll region → disclosure → review choices. Space expands the disclosure and records the local review message; the chart focus outline was visibly rendered.
- The embedded browser exposed a narrow raster preview but not a trustworthy CSS viewport measurement. This is not evidence for exact 320/375 CSS-pixel breakpoints or desktop widths. The full responsive matrix remains open.

Selected token contrast calculations using WCAG relative luminance: ink on white 14.36:1, muted on white 5.86:1, quiet on canvas 4.72:1, teal on white 5.01:1, amber status text/background 6.92:1, red status text/background 6.29:1. These are selected token pairs, not an exhaustive rendered-state contrast audit. The page does not claim WCAG conformance or award-level quality.

## Acceptance checks for this projection

1. JSON source head equals the pinned PR #14 source commit, with six aligned baseline/candidate intervals.
2. Rendered totals match JSON: 44 kWh and 44 kWh; peak 10 kW and 11 kW.
3. No numeric MOP amount, savings, full-bill, demand-charge, export-remuneration or cross-site-credit result is shown.
4. All economics and service/control unknowns remain visibly withheld or unassessed.
5. The page has no equipment-control or persistent-review action.
6. Current browser review is intentionally bounded: local fixture projection, disclosure content, local-only feedback/reset, and one narrow embedded rendering have been observed. Full keyboard traversal, an exact 320/375/768/1024/1440 CSS-pixel matrix, programmatic document-overflow checks, browser-console review, screen-reader testing, locale review and user testing remain open.

