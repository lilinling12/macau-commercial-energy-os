# Dispatch Prototype v2.0 — Tablet Chart Legibility Review

**Status:** unapproved responsive candidate; v1.9 remains preserved.  
**Parent:** PR #10 branch `product/source-load-economic-dispatch`, v1.9 source blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902` at reviewed PR head `b4d12b7eb07b088c97504f6767c3aac56bca8bef`.  
**Scope:** tablet breakpoint and chart/readiness typography only. Energy values, workflows, controls, claims, locale, palette, and SHADOW/no-control boundary are unchanged.

## Finding and change

The v1.9 review measured 768px without document overflow but did not inspect its screenshot. Visual inspection showed the schedule chart compressed beside a fixed-width readiness panel: at 768px, the chart SVG was only 289px wide and the legend text was 11px. This weakened interval and rebound reading in the primary dispatch task.

v2.0 stacks the dispatch chart and readiness/plan panels through 900px, and raises chart legend/labels and readiness text to 12–13px in that range. Below 681px the existing compact interval-card presentation remains in place; at 1024px and above the existing two-column composition remains unchanged. No palette or final visual direction is selected.

The `ui-ux-pro-max` review search returned the Sustainable Energy / Climate Tech pattern as the closest product match, with Data-Dense Dashboard and Swiss Modernism 2.0 as secondary patterns. A focused chart search recommended direct labels, distinct line styles, and a visible table fallback. The v2.0 change is limited to chart legibility; it does not adopt the search's style or color recommendation as a project decision.

## Browser review

Rendered the same Traditional Chinese synthetic `dispatchComparison` state in Microsoft Edge via Playwright at 320, 375, 768, 900, 1024, and 1440 CSS px. The review inspected the 375, 768, and 900 screenshots and compared layout measurements at all six widths.

| Width | v1.9 chart width | v2.0 chart width | v2.0 layout | Document overflow |
|---:|---:|---:|---|---|
| 320 | compact cards | compact cards | single column | none |
| 375 | compact cards | compact cards | single column | none |
| 768 | 289px | 597px | stacked | none |
| 900 | 410px | 718px | stacked | none |
| 1024 | 524px | 524px | two columns | none |
| 1440 | 867px | 867px | two columns | none |

At 768px the chart viewport more than doubles in width, and the readiness panel follows the chart rather than competing for horizontal space. At 375px the interval cards remain the primary representation; the chart remains hidden at this compact breakpoint as in v1.9.

## Limits

This is a focused visual/layout review of one workflow state and one locale. It does not establish full keyboard or screen-reader quality, measured WCAG contrast, text scaling, complete localization, operator usability, tariff/site truth, schedule feasibility, savings, or production readiness. A full interaction and accessibility review remains open.
