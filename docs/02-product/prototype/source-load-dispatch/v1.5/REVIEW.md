# Source/load dispatch prototype v1.5 review

**Review date:** 2026-10-05  
**Status:** Responsive cost/evidence-table refinement; not production UX approval.  
**Base:** v1.4 EV physical/economic boundary.

## Change

- At widths up to 760 CSS px, the cost/constraint matrix becomes labeled cards. Long values wrap, and the table remains available as rows and cells in the accessibility tree.
- At wider widths, the same four-column matrix uses fixed proportional column widths and wrapped text so the evidence column fits without table-level horizontal scrolling.
- The EV settlement row and its boundary are unchanged: do not presume building-tariff inheritance or cost allocation; require the charger-serving meter, account, effective contract/tariff and corresponding bill.

## Rendered review

**Desktop:** Microsoft Edge, available browser viewport 1265×712 CSS px, cost/constraint stage. The four columns, including the complete EV required-evidence cell, fit inside the table container; the table does not require horizontal scrolling. The two-column constraint explanation remains alongside it.

**Six-stage narrow walkthrough:** Microsoft Edge with the exact v1.5 source inside a same-origin 375 CSS-pixel iframe viewport at 375×680. Walked the six stages by their actual page states: data/contract evidence, site model, schedule comparison, cost/constraints, SHADOW review, and monitoring/replay. For each state the embedded document client width / scroll width was **360/360px**, and the active stage client width / scroll width was **332/332px**; no page-level horizontal overflow was measured.

**Cost-matrix breakpoint sweep:** The parent review harness changed the embedded viewport and measured the rendered document and matrix container:

| Embedded viewport | Document client / scroll | Matrix client / scroll | Result |
|---:|---:|---:|---|
| 375px | 360 / 360px | 332 / 332px | Cards; no horizontal overflow |
| 680px | 665 / 665px | 637 / 637px | Cards; no horizontal overflow |
| 681px | 666 / 666px | 638 / 638px | Cards; no horizontal overflow |
| 768px | 753 / 753px | 614 / 614px | Four-column matrix; no horizontal overflow |
| 1024px | 1009 / 1009px | 849 / 849px | Four-column matrix; no horizontal overflow |

At 1265px, the desktop screenshot showed all columns and the EV evidence cell with no table-level horizontal scrollbar. The 375×680 frame checks responsive width and page state; it does not prove full-phone task completion, touch ergonomics, or every scroll interaction. The cost/constraint stage remains vertically long.

## Limits

Only the Traditional Chinese synthetic dispatch flow was reviewed. No customer/site usability, tariff applicability, bill reconstruction, EV schedule, optimizer result or equipment control is validated. Keyboard and screen-reader walkthrough, touch-device review, text scaling, measured contrast, complete Portuguese/English localization, WCAG conformance and customer/site validation remain open. Product scope, visual direction, locale scope and production architecture remain unapproved.
