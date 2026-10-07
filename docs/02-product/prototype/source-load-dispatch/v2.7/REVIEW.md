# Source/load dispatch prototype v2.7 — review record

**Status:** Unapproved, UI-only synthetic study. It does not select product scope, visual direction, production architecture, wire contract, or equipment-control behavior.  
**Date:** 2026-10-06  
**Design basis:** PR #10 v2.6 synthetic schedule and assessment states; PR #14 bounded SHADOW assessment claim boundaries. The page is not connected to either branch's runtime output.

## Change from v2.6

The assessment case now governs the schedule projection:

- **Partial rate coverage:** the fixed six-interval schedule remains labeled as supplied synthetic input. It shows no monetary amount or savings claim.
- **No applicable tariff/contract:** candidate curves, candidate metrics and candidate table columns are hidden. The page states that no optimized candidate is generated.
- **Missing core meter mapping:** affected curve, numeric KPIs and interval table are hidden; the reason remains visible.
- **HVAC service violation:** the electrical example remains available for explanation with a visible warning; no overall-feasibility, comfort or execution claim is made.

Review actions remain page-local; there is no persistence, API, optimizer, site or equipment connection. Equipment control is absent.

## Browser review

- Browser: Microsoft Edge via Playwright, headless.
- Viewports: 1440×900, 1024×900, 768×900, 375×812 and 320×800 CSS pixels.
- Cases: partial tariff coverage, no applicable tariff, missing meter mapping and HVAC service violation at each viewport (20 case/viewport combinations).
- Results: one active `aria-pressed` case at a time; blocked mapping hides all schedule numerics; no-tariff state hides candidate curve/metrics/table columns; service-violation state keeps the warning visible; document width equals viewport width in every reviewed combination; zero page errors.
- Interactions: Space activates the focused state button; interval table expands and collapses; the local-only review state updates. All passed.
- Narrow chart uses a contained horizontal scroll region, with visible mobile guidance.
- Selected text/background token pairs were measured from the exact CSS values: body ink/canvas 13.35:1, muted/canvas 4.72:1, summary/pale 7.05:1, chart axis/white 4.76:1, teal/white 4.92:1, partial badge/orange pale 4.98:1, warning/red pale 7.62:1, blue status/blue pale 5.82:1. The initial axis label was 4.48:1; darkened from #687a80 to #63767c, then rechecked at 4.76:1.

The first visual pass exposed an inherited 850px table minimum that clipped claim text in the side panel. It was corrected with a zero-minimum, fixed-layout claim table and text wrapping; the final 1440px and 375px screenshots were visually rechecked. Contrast results cover selected token pairs only, not every rendered state or a complete WCAG audit.

## Remaining validation

- Traditional Chinese only; Portuguese and English are not implemented or reviewed.
- No screen-reader review, complete keyboard audit, measured contrast report, operator usability session, or WCAG conformance claim.
- Values and evidence states are synthetic; no tariff, settlement, site, asset capability, forecast, optimizer result, savings, or pilot evidence is established.
- The fixed schedule is a presentation fixture and does not change with the selected case. The state selector gates what may be shown; it does not simulate a real assessment or generate a dispatch plan.



## Additional narrow-window review — 2026-10-06

The existing controlled review matrix covers 320 CSS px and above. In this turn, the exact PR branch v2.7 file was opened in the Codex browser for an additional narrow-window stress review. The captured raster was 304 × 571 px; the CSS viewport dimensions were not directly available, so this observation is not recorded as a 304 CSS px breakpoint test. At that rendered width, the existing `min-width:320px` caused page-level horizontal overflow and wrapped the brand name. The review copy changed the body minimum width to zero and stacks the header metadata below 360 px. A second screenshot showed the page-level horizontal scrollbar gone and the brand on one line; the chart retains its own contained horizontal-scroll region. This is supplemental visual evidence only and does not replace the documented 320/375 CSS viewport matrix, a complete keyboard/screen-reader review, or a WCAG conformance audit.


## Additional state and design-system review — 2026-10-06

At the same narrow embedded-browser render, the four evidence cases were activated one at a time and the accessibility tree re-read after each interaction. No-tariff withheld the candidate curve, economics and ranking; missing core meter mapping hid dependent curves, KPIs and interval data; a service-limit violation retained the synthetic electrical profile while explicitly withholding overall feasibility, comfort and execution; partial coverage remained without monetary totals. The UI stated that review buttons are local-only and that no device-control endpoint exists. This was state inspection in a synthetic prototype, not an API/optimizer integration test.

The installed `ui-ux-pro-max` design-system query was run twice for the dispatch operations product; both returned a marketing/conversion and organic-biophilic style, with wide/futuristic typography. That result is a poor fit for this sustained operational comparison task and was not adopted. The project UI/UX skill's reference-as-evidence approach remains appropriate. Current guidance checked: [Apple HIG layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Apple HIG motion](https://developer.apple.com/design/human-interface-guidelines/motion), [Material 3 canonical layouts](https://m3.material.io/foundations/layout/canonical-examples/overview), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), and [2026/2027 Webby judging criteria](https://www.webbyawards.com/judging-criteria/). These support adaptable hierarchy, accessible states, purposeful/reduced motion and evaluating visual design together with content, navigation, functionality and overall experience. Awwwards' public scoring example separates design, usability, creativity and content; FWA describes its mission around digital innovation, creativity/originality and technical excellence. The award references are self-review lenses only. This turn did not conduct a detailed review of a particular winning site's design or establish any award-level outcome.
