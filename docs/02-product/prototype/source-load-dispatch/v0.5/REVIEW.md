# Macau Energy OS dispatch workflow prototype v0.5 — review record

**Status:** synthetic interaction/design study; no owner approval, site validation, tariff evaluation, user validation, or production UI claim.
**Locale:** Traditional Chinese only.
**Prototype:** [index.html](index.html)
**Fixture:** [fixtures/synthetic-dispatch.json](fixtures/synthetic-dispatch.json)
**Design guidance used:** project `macau-energy-os-ui-ux` skill and the local `ui-ux-pro-max` skill. The skill's design-system search leaned toward a marketing/conversion site and a generic organic palette, which does not match a persistent energy-operations workspace. A targeted product search did return a data-dense comparative analytics pattern; only that broad comparative principle was relevant. The page uses an experimental neutral/teal skin for this study; it is not an owner-selected palette or final visual system. No palette or architecture choice is frozen here.

## Change from v0.4

The previous workflow carried an ESS discharge example without a charge path, SOC continuity, or conversion efficiency. v0.5 updates the synthetic candidate to discharge 20 kW AC in 15:00–16:00 and recharge at 24.691358 kW AC in 16:00–17:00, using separate 90% discharge and charge efficiencies. SOC moves from 40 kWh to 17.777778 kWh and returns to 40 kWh. The candidate grid import in the recharge interval is 509.691358 kW. The HVAC 30 kW shift and equal 30 kW rebound remain explicit; the 17:00–18:00 interval remains the candidate horizon peak at 510 kW, above the 485 kW baseline peak.

The screen now presents the battery's discharge, recharge and SOC path in its annotation and interval table; the source list, site-model explanation, constraint table, candidate copy, and SHADOW summary state where the new quantities are synthetic. The scenario still makes no bill, savings, export-credit, field capability, thermal-comfort, or equipment-control claim. HVAC comfort dynamics, ESS degradation, forecast uncertainty and tariff settlement remain unmodelled.

## Arithmetic and source alignment

The fixture and static verifier cover:

- six continuous one-hour Macau (+08:00) intervals and load-component sums;
- per-interval physical balance `grid import + PV used + ESS discharge = site load + ESS charge`;
- HVAC shift/rebound neutrality across the synthetic horizon;
- ESS charge/discharge ratings, SOC continuity and bounds, and SOC integration using the declared separate efficiencies;
- restoration of the illustrative initial SOC, with charging losses visible in the AC charge quantity;
- consistency between all interval fixture values and the prototype table;
- withholding tariff cost, savings, PV export credit, cross-site netting and device control; and
- retention of the six-stage workflow and SHADOW/no-control boundary.

This check verifies only internal synthetic arithmetic and source-to-screen alignment. It does not establish that the dispatch is optimal, safe, thermally comfortable, economically beneficial, or feasible at any Macau building.

The contrast calculation follows the WCAG relative-luminance ratio for the listed foreground/background CSS pairs; those ratios do not imply whole-page WCAG 2.2 conformance. The chart has a title/summary and a tabular alternative, consistent with Apple's chart accessibility guidance, but assistive-technology behavior was not exercised. References: [WCAG 2.2, Contrast Minimum](https://www.w3.org/TR/WCAG22/#contrast-minimum) and [Apple HIG, Charts](https://developer.apple.com/design/human-interface-guidelines/charts/).

## UI/UX review coverage

| Area | Observed | Still open |
|---|---|---|
| Product flow | The browser tab available in the current review session resolves to a v0.4 page: its document title and left-rail badge say v0.4. This observation cannot validate the v0.5 source. The v0.5 source is present in this PR, but an exact-source browser render has not been reproduced in this session. | Operator task validation and role/site scope. |
| Energy semantics | The currently visible v0.4 page says ESS has no SOC trajectory and omits the recharge interval from its visible model/table. It is therefore stale relative to v0.5 and must not be used as evidence for v0.5 energy semantics. The v0.5 source and fixture carry the stated charge/SOC values; this session did not confirm them in a rendered v0.5 page. | Confirm terminology with Macau operators and finance users. The interval table remained collapsed in this browser observation. |
| ESS/HVAC | Candidate now exposes an explicit charge/discharge and SOC trajectory; HVAC shift/rebound is unchanged and fully interval-labelled. | Site-specific battery limits, thermal comfort/service model, response and safety constraints. |
| Interaction/accessibility | Source includes native scenario buttons, labels, focus styling, a skip link, page-only review, a data-table alternative, reduced-motion handling and a keyboard-contained evidence dialog. The current browser accessibility tree belongs to the stale v0.4 preview, not this v0.5 source. Limited CSS-pair contrast calculations: body/paper 13.35:1; muted/card 4.93:1; teal/card 4.92:1; chart-axis/card 6.03:1; table-heading/background 5.81:1; footer/paper 5.39:1. Chart-axis, table-heading and footer tokens were darkened after the first pass. | These are static checks for selected token pairs, not all text, focus, states, borders or chart marks. Keyboard interaction, screen-reader behavior and WCAG conformance remain unverified. |
| Responsive | The v0.5 source declares 1050/760/390 px layout breakpoints and a horizontally scrollable data table. The current browser tab reports a 1280×720 viewport and 1265 px document width for v0.4 only; those dimensions cannot establish v0.5 responsive behavior. | No v0.5 pixel screenshot or viewport/no-overflow measurement was captured. Review at 1440, 1024, 768 and 375 CSS px, text enlargement and v0.5 table containment remain open. |
| Localization | Traditional Chinese was visible in the stale v0.4 browser tree; v0.5 locale rendering was not independently confirmed. | Portuguese and English complete flow, terminology, locale metadata, date/time/currency and long-string reflow. No multilingual support is claimed. |
| Originality/visual direction | The composition puts the six-stage source/load decision ahead of generic portfolio metrics. Project skill calls for comparing complete task compositions and treating award sites as craft references, not templates. | Compare substantially different compositions and palettes on the same operator task; no owner selection or user validation yet. |

## Preview-source correction — 2026-10-05

The browser tab available in this session loaded `http://127.0.0.1:8769/?review=final-77a3`, whose title, rail badge and content identify v0.4. Its ESS row says there is no SOC trajectory, and its site-model text omits the recharge/SOC path present in the v0.5 branch source. The accessible tree therefore does not correspond to the file reviewed here. The previous session note that described a v0.5 browser tree could not be reproduced against the current browser state and is treated as unverified until an exact-source render is recorded. The tab's 1280×720 viewport and 1265 px document width apply only to that v0.4 page. No claim of v0.5 visual, responsive, interaction or localization validation is made.

## Current stage and next evidence

The G7.9 Step 3 service-boundary and implementation-design gate remains open; this local prototype improves one product/interaction input only. It does not reconcile APP-01…APP-11, define production contracts or persistence, close G6.9 framework evidence, or authorize field control. Next, render this exact v0.5 branch source through an authorized preview path and record the four target widths, then walk controls by keyboard, measure text/non-text contrast, and review complete English/Portuguese/Traditional Chinese flows. The currently available preview serves v0.4 and is not suitable for those v0.5 checks. In parallel, domain review must replace synthetic battery/load/tariff assumptions with a customer-approved site fixture before any optimizer or economics acceptance criterion can use this example.



## Exact branch render and first-screen refinement — 2026-10-05

**Source verified:** Rendered the HTML content fetched from PR #10 branch product/source-load-economic-dispatch after commit ab61536afbe89707f165cbd47ee14f2a75e07555 (source blob 3c29b5dd121fb4298780fbe165bb1d5fbbc48a9f). This is separate from the similarly named local output file; earlier local-output previews do not prove the branch file's behavior.

**Observed at 1265 × 712 CSS-pixel screenshot:** the six-step dispatch workflow fits across the first viewport, and the source/contract evidence section begins below it. The rendered hero's original subtitle left a single Chinese character (“性。”) on its own line. Shortened it to “比較同一時段的供能與負荷安排，先核實現場證據，再看成本與約束。” The updated exact-branch render keeps the complete sentence on one line at this viewport and gives the date/granularity/evidence controls a single aligned row. The accessible page tree confirms named evidence and schedule controls, six workflow links, the synthetic-data boundary, blocked economics, the no-control state and replay boundary.

**Guidance applied:** the project Macau Energy OS UI/UX skill plus ui-ux-pro-max. The product-wide design-system search returned a marketing/conversion pattern and Organic Biophilic styling, including after a narrower operations query; these results are not a fit for a persistent dispatch workspace and were not adopted. Targeted UX search supported native keyboard-operable controls with visible state/focus; chart guidance supported distinguishing observed/forecast series with line style and providing a table alternative. The existing neutral/teal treatment remains an unapproved study direction.

**Scope of this check:** exact-branch initial-screen visual render and accessibility-tree inspection only. No control was activated and no keyboard-only path, responsive breakpoint other than the observed viewport, Portuguese/English locale, chart/table toggle, modal, contrast sweep, browser zoom, assistive technology, user study, or WCAG conformance was verified. The rendering check does not validate dispatch semantics or synthetic arithmetic.

**Next review:** inspect the same exact branch source at 1440, 1024, 768 and 375 CSS px; exercise all controls by keyboard; inspect chart and table states; check full Traditional Chinese, English and Portuguese sample flows; then record any resulting fixes and remaining product/owner decisions. The locale set and visual direction remain proposals, and the prototype remains synthetic and non-executable.


## Responsive and interaction review — 2026-10-05

**Exact source:** PR #10 branch `product/source-load-economic-dispatch`; interaction/accessibility refinement committed as `ea3e770d1731deb8951476cd7143dac4569517d1` (prototype blob `afd4128995b5ba350d8c56974c2b759492b2a5bc`). The earlier one-viewport review did not reveal that an extra closing parenthesis in the final review-button handler caused a syntax error in the whole inline script. This made the scenario selector, table toggle and SHADOW demo control inert. The handler was corrected before this pass.

**Rendered and inspected:** Microsoft Edge via Playwright at 1440×1000, 1024×900, 768×1024 and 375×844 CSS px. The document had no horizontal page overflow at any width. The six workflow steps lay out in one row at 1440, three columns at 1024/768 and two columns at 375; planning controls wrap at 375. Keyboard Tab traversal showed the skip link, icon navigation, form controls and workflow links with a visible 3 px focus outline. The data table expands and updates `aria-expanded`; at 375 it is 1230 px wide inside a 345 px horizontal-scroll region. A visible narrow-screen scroll hint, focusable named region and ArrowLeft/ArrowRight scrolling were added. Keyboard interaction moved the region's `scrollLeft` by 160 px.

**Interaction evidence:** no page JavaScript errors after the fix; selecting the candidate updates `aria-pressed` and the live comparison message; the review button changes only the page-local example state and explicitly says it is not saved, does not authorize and does not execute equipment. These checks verify this synthetic prototype's interactions only.

**Remaining limits:** only the Traditional Chinese content was rendered. English and Portuguese copy/reflow, full contrast measurement, zoom, screen-reader operation, all modal/keyboard paths, user validation, tariff/bill truth, site capabilities, arithmetic/domain approval and production readiness remain unverified. The prototype remains a design study and an advisory-only UI hypothesis.
