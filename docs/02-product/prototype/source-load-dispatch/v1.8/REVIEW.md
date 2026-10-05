# Source/load dispatch prototype v1.8 — narrow-table keyboard access review

**Status:** Unapproved accessibility follow-up; v1.7 is preserved unchanged.  
**Parent:** exact PR #10 v1.7 source blob `c6a3886749baf291ae36e10420c276cbcf59a4f8`.  
**Scope:** one bounded interaction change to the evidence-readiness source table. Schedule values, product claims, locale, visual direction and SHADOW boundary are unchanged.

## Finding and change

At 320 CSS px the evidence-check source table is 763 px wide inside a 275 px viewport. Its wrapper scrolled horizontally but was not keyboard-focusable and had no accessible name. This left keyboard users without a reliable way to reach the full table.

v1.8 gives that wrapper a named `region`, `tabindex="0"`, visible keyboard focus styling, and left/right arrow-key scrolling. It does not replace native table semantics. The separate 320 px cost/constraint table is rendered as stacked rows and does not need horizontal scrolling. The schedule chart remains a separate horizontal-scroll region.

## Browser verification

Reviewed all six workflow stages (`evidence-check`, `site-model`, `dispatchComparison`, `constraint-analysis`, `shadow-review`, and `outcome-replay`) at these viewport widths:

| Viewport | Document width | Active stage width | Result |
|---:|---:|---:|---|
| 320 × 844 | 305 px | 277 px | No document-level horizontal overflow in any stage |
| 375 × 844 | 360 px | 332 px | No document-level horizontal overflow in any stage |
| 768 × 844 | 753 px | 615 px | No document-level horizontal overflow in any stage |
| 1440 × 844 | 1425 px | 1234 px | No document-level horizontal overflow in any stage |

At 320 px, the source table region measured 275 px wide with 763 px of scrollable content. It exposed the accessible name “合成來源清單；水平捲動查看所有欄位” and `tabindex=0`. Focusing it and pressing ArrowRight moved `scrollLeft` from 0 to 160 px; ArrowLeft returned it to 0. The focus outline was visible in the rendered screenshot. At the 320 px cost/constraint stage, the table is transformed into stacked rows and fits the 277 px stage width.

## Limits and next review

The review covers rendered layout and this one keyboard interaction only. It does not establish screen-reader behavior, full keyboard-flow conformance, touch behavior, text enlargement, WCAG conformance, Portuguese or English localization, representative operator usability, Macau tariff/site validity, dispatch feasibility, savings, or control capability. The prototype remains Traditional Chinese, synthetic and SHADOW-only. Full locale coverage remains a separate planned review; this change does not count as multilingual support.



## Locale surface inventory

The source remains Traditional Chinese. A DOM and inline-interaction scan found 296 unique Chinese DOM text values, 23 Chinese accessibility-attribute values (22 unique), and 21 distinct Chinese inline-script literals; counts overlap and are not a deduplicated translation-unit total. See [`LOCALE-COVERAGE.md`](LOCALE-COVERAGE.md) for stage distribution, dynamic UI categories and completion criteria. This inventory is not translation or multilingual support.
