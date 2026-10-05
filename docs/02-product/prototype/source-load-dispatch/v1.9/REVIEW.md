# Source/load dispatch prototype v1.9 — narrow-screen hierarchy review

**Status:** unapproved responsive refinement; v1.8 remains unchanged.  
**Parent source:** PR #10 `docs/02-product/prototype/source-load-dispatch/v1.8/index.html`, source blob `ea0d3087815f52764ac9e7ac227ef64a2631c155`.  
**Scope:** CSS-only narrow-screen compaction plus version text. Energy values, stage flow, controls, claims, evidence labels, locale, visual palette and SHADOW/no-control boundary are unchanged.

## Finding and change

At compact widths the site and planning context, heading and controls consumed substantial vertical space before the schedule comparison. The dispatch task was therefore visually late in the page even though the page had no horizontal overflow.

v1.9 shortens the compact navigation, removes a redundant breadcrumb, tightens top/title spacing, keeps the planning summary available, and increases small compact labels to 12–14px where the prior source used 10–11px. It preserves target sizes and all control semantics. No content or interaction has been removed. The existing color palette and composition are not selected or approved by this refinement.

## Browser comparison

Compared the exact local v1.8 and v1.9 HTML using Microsoft Edge through Playwright at 320, 375 and 768 CSS px. Both variants were opened at document top, set to the same `dispatchComparison` stage, then measured at the same 844px viewport height. `documentElement.scrollWidth` equaled the viewport at each width.

| Viewport | v1.8 schedule heading top | v1.9 schedule heading top | Shift earlier | Page overflow |
|---:|---:|---:|---:|---|
| 320 × 844 | 654px | 540px | 114px | None |
| 375 × 844 | 637px | 516px | 121px | None |
| 768 × 844 | 690px | 690px | 0px | None |

The unchanged 768px result is expected: this refinement only changes compact layouts. A 320px render was visually inspected; the stage, schedule title, evidence warning and first interval cards remain visible in the viewport. The complete six-hour summary extends below the fold and is scrollable. A 375px and 768px DOM/layout sweep was recorded, but their screenshots were not separately inspected in this pass.

All six workflow stages (`evidence-check`, `site-model`, `dispatchComparison`, `constraint-analysis`, `shadow-review`, `outcome-replay`) became active and rendered at their target widths without document overflow. The schedule data-table control expanded and exposed the table. The accessibility tree in the in-app browser still identifies the schedule title, synthetic-data warning, six hourly values, readiness blockers, baseline/candidate controls, and page-only review/no-control boundary.

## Limits

This is a narrow hierarchy/layout check, not a full UX or accessibility audit. It does not establish full keyboard-flow or screen-reader behavior, WCAG conformance, touch or text-scaling behavior, contrast compliance, Portuguese/English layout, complete localization, operator usability, Macau site/tariff validity, schedule feasibility, savings, or equipment control. The prototype remains Traditional Chinese, synthetic, and SHADOW-only. Product scope, visual direction, palette and production architecture remain unapproved.
