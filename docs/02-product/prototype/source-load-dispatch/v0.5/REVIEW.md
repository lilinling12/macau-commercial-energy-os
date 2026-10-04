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
| Product flow | The current v0.5 in-app browser accessibility tree exposes all six stages: evidence readiness, physical model, aligned schedule, constraints/economics, SHADOW review, and outcome/replay. It also confirms the version rail says v0.5. | Operator task validation and role/site scope. |
| Energy semantics | The v0.5 browser tree exposes the 15:00–16:00 discharge, 16:00–17:00 charge, 40→17.778→40 kWh SOC path, 509.691 kW recharge-period import, synthetic assumptions, and no-control state. It retains the separation from tariff settlement. | Confirm terminology with Macau operators and finance users. The interval table remained collapsed in this browser observation. |
| ESS/HVAC | Candidate now exposes an explicit charge/discharge and SOC trajectory; HVAC shift/rebound is unchanged and fully interval-labelled. | Site-specific battery limits, thermal comfort/service model, response and safety constraints. |
| Interaction/accessibility | Source includes native scenario buttons, labels, focus styling, a skip link, page-only review, a data-table alternative, reduced-motion handling and a keyboard-contained evidence dialog. Browser accessibility-tree content was observed at the local preview. Limited CSS-pair contrast calculations: body/paper 13.35:1; muted/card 4.93:1; teal/card 4.92:1; chart-axis/card 6.03:1; table-heading/background 5.81:1; footer/paper 5.39:1. Chart-axis, table-heading and footer tokens were darkened after the first pass. | These are static checks for selected token pairs, not all text, focus, states, borders or chart marks. Keyboard interaction, screen-reader behavior and WCAG conformance remain unverified. |
| Responsive | Source retains 1050/760/390 px layout breakpoints and a horizontally scrollable data table. | This turn did not capture pixel screenshots or measure the active viewport; render inspection at 1440, 1024, 768 and 375 CSS px, text enlargement and no-overflow checks remain open. |
| Localization | Traditional Chinese is visible in the current browser tree. | Portuguese and English complete flow, terminology, locale metadata, date/time/currency and long-string reflow. No multilingual support is claimed. |
| Originality/visual direction | The composition puts the six-stage source/load decision ahead of generic portfolio metrics. Project skill calls for comparing complete task compositions and treating award sites as craft references, not templates. | Compare substantially different compositions and palettes on the same operator task; no owner selection or user validation yet. |

## Current stage and next evidence

The G7.9 Step 3 service-boundary and implementation-design gate remains open; this local prototype improves one product/interaction input only. It does not reconcile APP-01…APP-11, define production contracts or persistence, close G6.9 framework evidence, or authorize field control. The next design pass should render the exact review file at the four target widths, walk all controls by keyboard, measure text/non-text contrast, and review complete English/Portuguese/Traditional Chinese flows. In parallel, domain review must replace synthetic battery/load/tariff assumptions with a customer-approved site fixture before any optimizer or economics acceptance criterion can use this example.

