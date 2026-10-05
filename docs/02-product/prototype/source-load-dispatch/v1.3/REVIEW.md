# Source/load dispatch prototype v1.3 review

**Review date:** 2026-10-05  
**Status:** Responsive anchor correction review; not production UX approval.  
**Base:** v1.2 six-stage workflow.  
**Base HTML blob:** aa36108ad4781d8906afe00d41d2a3308e15f94f

## Change

At widths up to 760 CSS px, the dispatch comparison anchor now uses a 64px scroll margin. The previous target scrolled to the top of the viewport beneath the sticky 58px navigation rail, hiding the stage heading. At 375px after the change, the section begins at y=63.6px while the rail ends at y=58px. Desktop and tablet anchor behavior is unchanged.

## Rendered review

Rendered this v1.3 source in Microsoft Edge via Playwright with `prefers-reduced-motion: reduce`. The measurements below are from the dispatch-comparison state unless noted.

| Viewport | Document width | Document height | Observation |
|---|---:|---:|---|
| 1440×1000 | 1440px | 1512px | No page-level horizontal overflow; desktop comparison and constraint columns remain side by side. |
| 1024×900 | 1024px | 1719px | No page-level horizontal overflow. |
| 768×1024 | 768px | 1906px | No page-level horizontal overflow. |
| 375×844 | 375px | 2975px | No page-level horizontal overflow; interval summaries replace the wide chart for mobile. The stage heading is now visible below sticky navigation. |

At 375×844, separate stage renders measured 2,328px for evidence readiness, 2,321px for cost/constraints and 1,836px for monitoring/replay. The mobile document remains long and still requires substantial scrolling. The stage 4 table remains locally scrollable for its full columns rather than widening the page.

The page emitted no Playwright page-error events during these renders. Screenshots were captured for dispatch comparison at each listed viewport and for the evidence, constraints and replay states at 375×844.

## Remaining review limits

This is synthetic product/UI review only. It does not validate Macau site data, tariffs, equipment feasibility, optimization quality, savings, device control, customer/operator usability or production readiness. Traditional Chinese is the only complete interface language in this prototype. Keyboard walkthrough, screen-reader assessment, touch-device review, text scaling, measured contrast and WCAG conformance remain open. Product scope, visual system and production architecture remain unapproved.
