# Source/load dispatch prototype v1.5 review

**Review date:** 2026-10-05  
**Status:** Narrow-screen cost/evidence-table refinement; not production UX approval.  
**Base:** v1.4 EV physical/economic boundary.  
**Base HTML blob:** 54bb68a37c40a44480c40a63ae2edb473c663a50

## Change

The cost/constraint stage retains its full four-column semantic table on wider screens. At widths up to 680 CSS px, each row is presented as a card with visible field labels for status, impact and required evidence. The table headers remain in the accessibility tree. Cell text wraps; the cost table no longer requires horizontal scrolling on narrow screens. The EV settlement-attribution row and its “do not presume the building tariff or allocation rule” boundary are unchanged.

## Narrow-screen render

Rendered the exact v1.5 source in Microsoft Edge inside a same-origin 375 CSS-pixel iframe review viewport at 375×680. The parent harness reads the embedded document's actual viewport and layout dimensions.

- Embedded viewport: **375×680**.
- Embedded document client width / scroll width: **360/360px**; no page-level horizontal overflow.
- Cost-table container client width / scroll width: **332/332px**; no table-level horizontal scrolling.
- The EV settlement row remains present. Its status, impact and required-evidence labels are visible in the accessibility tree.
- The table remains exposed with rows and cells in the browser accessibility tree after the mobile presentation change.

The browser viewport was shorter than a common phone height, so this checks width/wrapping and internal scroll behavior rather than full-device task completion or touch ergonomics. The stage remains vertically long.

## Limits

The review covers only the Traditional Chinese synthetic cost/constraint state. It does not establish tariff applicability, bill reconstruction, an EV schedule, real site/operator usability, or equipment control. Portuguese/English coverage, keyboard and screen-reader walkthrough, touch-device validation, text scaling, measured contrast, WCAG conformance, and customer/site validation remain open. Wider desktop rendering relies on the unchanged v1.4 table styles; a separate v1.5 desktop visual pass remains to be recorded.
