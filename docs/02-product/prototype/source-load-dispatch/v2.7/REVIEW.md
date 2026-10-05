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

The first visual pass exposed an inherited 850px table minimum that clipped claim text in the side panel. It was corrected with a zero-minimum, fixed-layout claim table and text wrapping; the final 1440px and 375px screenshots were visually rechecked.

## Remaining validation

- Traditional Chinese only; Portuguese and English are not implemented or reviewed.
- No screen-reader review, complete keyboard audit, measured contrast report, operator usability session, or WCAG conformance claim.
- Values and evidence states are synthetic; no tariff, settlement, site, asset capability, forecast, optimizer result, savings, or pilot evidence is established.
- The fixed schedule is a presentation fixture and does not change with the selected case. The state selector gates what may be shown; it does not simulate a real assessment or generate a dispatch plan.

