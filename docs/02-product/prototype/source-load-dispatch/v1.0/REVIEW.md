# Source/load dispatch prototype v1.0 review

**Review date:** 2026-10-05  
**Status:** Mobile layout proposal for product/design review; not approved production UX.  
**Base:** PR #10 v0.9 at HTML blob `415761b3b11fd21961a0fd67d3d57b48bdb123b0`, verified byte-for-byte against the local v0.9 working copy before iteration.

## Iteration

The v0.9 mobile view showed a 640px schedule chart inside a 345px viewport, with a horizontal-scroll hint and a complete data-table alternative. For v1.0, the desktop/tablet chart remains unchanged. At widths of 680px and below, the large curve and redundant legend are replaced by six compact interval summaries. Each interval shows the planning time, baseline-to-candidate grid import, total load, site PV, ESS charge/discharge and SOC, and HVAC movement/rebound. The complete data table remains available from the same control. A short closing note keeps the full-window peak increase and unknown billing-period Pu visible; the four repeated metric cells are hidden on mobile.

This applies the project's energy-operations skill: preserve source/load semantics and evidence labels, keep physical scheduling separate from billing, and adapt content to the viewport instead of shrinking a dense desktop chart. `ui-ux-pro-max` chart guidance also supports direct values, non-color distinctions and an accessible tabular alternative.

## Verification performed

Rendered the exact local HTML in Microsoft Edge through Playwright at the following CSS viewports:

| Viewport | Document width | Document height | Mobile summary | Schedule chart | Result |
|---|---:|---:|---|---|---|
| 1440 × 1000 | 1440 | 1512 | Hidden | Visible | Desktop view preserved |
| 1024 × 900 | 1024 | 1719 | Hidden | Visible | Laptop layout preserved |
| 768 × 1024 | 768 | 1906 | Hidden | Visible | Tablet layout preserved |
| 375 × 844 | 375 | 3125 | Visible | Hidden | No document-level horizontal overflow |

At 375×844, v1.0 is 44px taller than v0.9's recorded 3081px. The mobile schedule itself is fully readable without horizontally scrolling the plot; the small total page-height increase remains a trade-off. The six mobile intervals were compared to the underlying detailed table: time, baseline/candidate grid values, baseline/candidate load, PV, ESS/SOC, and HVAC values match (three-decimal display tolerance). Table expansion still sets `aria-expanded=true` and displays the full table. The workflow link still navigates to the SHADOW review stage. No browser JavaScript errors were observed.

## Limitations and next review

- This is synthetic-data-only and Traditional-Chinese-only. Decimal values in the compact view round to three places; the expanded table retains the source precision.
- The detailed table can still scroll horizontally when expanded. Screen-reader equivalence, touch-device behavior, text zoom, other locales, and representative-operator task success were not validated.
- The same overall page remains long on mobile. This iteration removes chart pan as a prerequisite for reading interval values but does not solve the entire page-length question.
- No palette or product direction is selected. Screenshot review does not establish WCAG conformance, user validation, pilot readiness, or award-level quality.

Artifacts: `outputs/macau-energy-os-dispatch-workflow-prototype-v1.0.html`, screenshots `work/dispatch-v10-{1440,1024,768,375}.png`, and the rendered v0.9 baseline screenshot `work/dispatch-v09-375.png`.


