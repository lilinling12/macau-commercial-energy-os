# Source/load dispatch localization study v0.1

**Status:** Exploratory, one-screen interaction study. Locale release scope, visual direction, and terminology remain unapproved. This is not a claim of complete product localization or Macau operator validation.

## Purpose and scope

The study puts the same source/load dispatch comparison screen in Traditional Chinese (`zh-Hant`), English (`en`), and Portuguese (`pt`). It checks how longer localized labels and safety/evidence messages behave in a compact operator workflow. The language selector changes presentation and locale-aware date/number formatting while preserving the selected interval, scenario values, and `Asia/Macau` timezone.

This is one complete screen, not all six workflow stages. Strings are preliminary translations and require Macau energy-domain review. It does not establish that Portuguese should use a particular regional variant, or that all three languages are required for launch.

## Scenario and claims boundary

The source values are from the synthetic six-interval dispatch example already under review in PR #10. They are not site data, forecasts, or optimizer output. At 15:00–16:00, the displayed balance is 430 kW grid import + 110 kW on-site PV + 20 kW ESS discharge = 560 kW site load + 0 kW ESS charging. At 16:00–17:00, the example charges the ESS by 24.7 kW; proposed grid import is 509.7 kW and the full-horizon import peak rises from 485 to 510 kW.

The interface separates physical energy flow from bill settlement. It says cost and savings are not calculated because applicable tariff, meter/account mapping, Pu measurement window, and billing-period evidence are missing. PV export credit, tariff savings, device capability, comfort compliance, and site feasibility are not asserted. SHADOW is illustrative and issues no equipment commands.

## UX changes in this increment

- Replaced the five-cell inline equation with grouped supply and destination sections, making the conservation relationship explicit and easier to scan at narrow widths.
- Made all six workflow stages visible on compact screens using a two-column grid at 680px and below and a three-column grid through 900px. The desktop workflow remains a single row.
- Allowed the SHADOW/no-command boundary text to wrap, fixing a 2px Portuguese overflow at 320px.
- Constrained the single-column content track so the accessible full-width data table scrolls inside its named region instead of widening the page.
- Preserved clear synthetic-scenario, unverified-input, and not-calculated states across all three displayed locales.

No design direction or palette is selected by this study. It remains an operator-console study, not a marketing page. UI/UX Pro Max and the project UI/UX skill are review inputs; their generic suggestions do not override the domain workflow or owner decisions.

## Browser review evidence

Reviewed the local study page in Microsoft Edge with Playwright at these CSS viewport widths and all three locales. The document width matched the viewport in every combination.

| CSS viewport | zh-Hant | en | pt | Workflow presentation |
|---:|---|---|---|---|
| 320 | no page overflow | no page overflow | no page overflow | two columns |
| 375 | no page overflow | no page overflow | no page overflow | two columns |
| 768 | no page overflow | no page overflow | no page overflow | three columns |
| 1024 | no page overflow | no page overflow | no page overflow | single row |
| 1440 | no page overflow | no page overflow | no page overflow | single row |

At 320px in Portuguese, opened the data-table disclosure: the document remained 320px wide; the table's 391px content width stayed inside its 266px scroll region. Selected 16:00–17:00 and observed the 509.7 kW grid import, 24.7 kW ESS charging, and full-horizon peak rebound explanation. Switched to English and confirmed the selected interval and underlying values remained the same while labels and decimal formatting changed. No page-level JavaScript errors were observed.

A local 320px screenshot is retained at `outputs/dispatch-localization-study-v0.1-mobile.png`; it is review evidence, not a repository asset.

## Limits and next evidence

- Only the comparison screen and its interval-selection/table states are covered; locale switching across all six stages, modals, review feedback, and replay is not demonstrated.
- The translations are draft copy, not professionally reviewed Macau Portuguese, English, or energy terminology.
- This pass does not measure WCAG contrast, validate screen-reader announcements, test enlarged text, establish full keyboard coverage, or substitute for operator research.
- The earlier v1.9 inventory found 429 static text nodes, 23 non-empty accessibility/text attributes, and dynamic script literals across the six-stage source. This single-screen study does not discharge that whole-source localization backlog.
- Next: decide the pilot locale policy and Portuguese variant; obtain local terminology review; extend locale handling to all six stages and meaningful states; repeat rendered checks with real user content and text enlargement; then review the resulting prototype with Macau building-energy operators.

