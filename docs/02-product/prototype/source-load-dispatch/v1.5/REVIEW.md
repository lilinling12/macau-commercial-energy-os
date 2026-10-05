# Source/load dispatch prototype v1.5 review

**Review date:** 2026-10-05  
**Status:** Responsive cost/evidence-table refinement; not production UX approval.  
**Base:** v1.4 EV physical/economic boundary.

## Change

- At widths up to 680 CSS px, the cost/constraint matrix becomes a set of labeled cards. Long values wrap, and the table remains available as rows and cells in the accessibility tree.
- At wider widths, the same four-column matrix uses fixed proportional column widths and wrapping so the evidence column remains visible without horizontal scrolling.
- The EV settlement row and its boundary are unchanged: do not presume building-tariff inheritance or cost allocation; require the charger-serving meter, account, effective contract/tariff and corresponding bill.

## Rendered review

**Desktop:** Microsoft Edge, available browser viewport 1265×712 CSS px, cost/constraint stage. The four columns, including the complete EV required-evidence cell, fit inside the table container; the table no longer needs horizontal scrolling. The two-column constraint explanation remains alongside it.

**Narrow viewport:** Microsoft Edge, exact v1.5 source inside a same-origin 375×680 CSS-pixel iframe viewport. The parent review harness measured:

- Embedded viewport: **375×680px**.
- Embedded document client width / scroll width: **360/360px**; no page-level horizontal overflow.
- Cost-table container client width / scroll width: **332/332px**; no table-level horizontal scrolling.
- EV settlement row is present, with visible status, impact and evidence labels in the accessibility tree.
- The table remains exposed as a table with rows/cells in the browser accessibility tree after the responsive presentation change.

The narrow-height render checks wrapping and width; it does not prove full phone task completion, touch ergonomics or all scroll states. The cost/constraint stage remains vertically long.

## Limits

Only the Traditional Chinese synthetic cost/constraint state was reviewed. No customer/site usability, tariff applicability, bill reconstruction, EV schedule, optimizer result or equipment control is validated. Keyboard and screen-reader walkthrough, touch-device review, text scaling, measured contrast, complete Portuguese/English localization, WCAG conformance and customer/site validation remain open. Product scope, visual direction, locale scope and production architecture remain unapproved.
