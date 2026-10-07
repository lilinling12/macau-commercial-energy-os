# v1.9 Localization Study v0.3 — Browser and Viewport Review

**Reviewed:** 2026-10-07  
**Status:** Localized prototype evidence for review; not approved translations, a product locale decision, WCAG conformance, user validation, or production readiness.  
**Pinned source:** PR #10 branch `product/source-load-economic-dispatch`, `v1.9/index.html`, Git blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902`.  
**Preview:** `index.html`, generated from that source by the adjacent localization builder and draft catalog v0.4.

## Scope and method

The browser script opens the generated local preview for each locale (`zh-Hant`, `en`, `pt`), each of the six workflow stages, and each CSS viewport size (320×800, 375×812, 768×900, 1024×900, 1440×900). It records document/active-section overflow, page errors, horizontal-scroll regions, current stage, and untranslated CJK text still visible in SVG for English and Portuguese. This is a rendering and geometry smoke check for one static prototype file, not a full browser/device, assistive-technology, or product-runtime test.

The resulting matrix contains 90 samples (3 locales × 6 stages × 5 viewports). The checked measurements report:

| Check | Result |
|---|---:|
| Samples | 90 |
| Page horizontal overflow | 0 |
| Active-section horizontal overflow | 0 |
| Browser JavaScript errors | 0 |
| Document width different from viewport | 0 |
| English/Portuguese SVG containing CJK text | 0 |
| Samples with contained horizontal table/region scrolling | 13 |
| Captured screenshots | 18 |

The measurement JSON contains every sample and is retained at `evidence/measurements.json`. `tools/inspect_localized_viewports.mjs` reproduces the matrix against the preview. `tools/build_localized_preview.py` builds the preview from the pinned Traditional Chinese source and catalog.

## Screenshot coverage

- Dispatch comparison: all three locales at 320×800, 375×812, 768×900 and 1440×900 (12 captures).
- Constraint analysis: all three locales at 320×800 and 375×812 (6 captures).
- 1024×900 is included in the 90-sample measurement matrix but not in the screenshot subset.

Screenshots are viewport captures of the active stage, not full-page captures. The captured images were spot-checked at 320, 375, 768 and 1440 widths across the available locales/stages. The 90-row browser measurements are the exhaustive part of this pass; screenshot review is a sampled visual inspection, not a manual review of every pixel in every image.

## Findings and changes made

1. **Visible SVG text was missing from translation coverage.** The earlier accessibility-tree review did not catch Chinese chart annotations in English and Portuguese screenshots. The builder now extracts SVG `text`/`tspan` as separate `svg-text` contextual units. Catalog v0.4 adds nine chart-text units, including the previously missed end-boundary and ESS charge/discharge labels. The rerun found no CJK text in the English/Portuguese SVG elements it queried.
2. **Dense chart annotations collided at narrow and medium widths.** At CSS widths up to 900px the preview hides plot annotations while retaining the chart axes/series, legend, and the interval table/summary alternative. This is a prototype presentation rule, not a chosen product breakpoint. On wider Portuguese screenshots the chart remains information-dense and warrants further design review.
3. **Narrow layouts remain contained.** No document or active-stage horizontal overflow was measured. Some tabular/region content uses its own horizontal scroll container; 13 samples exposed such a contained region. This is recorded rather than counted as page overflow.

## What this evidence does not establish

- The en/pt strings are complete-coverage AI-assisted drafts. Macau Portuguese terminology, regional variant, English product/energy terminology, tone, and translation accuracy have not received qualified human review.
- The locale selector was not exercised; language switching, state preservation, URL/history behavior, and locale-specific date/number formatting are untested.
- A query-parameter preview and translated static strings are not production runtime localization or an adopted launch language policy. Traditional Chinese, Portuguese and English remain candidate locales only.
- The 90 samples do not cover every dynamic state, browser engine, zoom/text scaling, keyboard path, screen reader, contrast pair, reduced-motion interaction, or mobile device. No WCAG 2.2 conformance claim is made.
- No Macau operator, customer, or domain expert completed a comprehension or task test. No live site, tariff, PV export right, controllability, savings, or dispatch feasibility is demonstrated.
- The preview is a single operational-console study. It does not establish the design of a marketing homepage, a production design system, or an approved visual direction.

## Design review lenses

This pass treats Apple HIG layout/accessibility/motion guidance and Material 3 adaptive-layout/state guidance as principles to test, not as a visual skin. WCAG 2.2 is a future measurable accessibility baseline; these geometry/text checks are not a conformance audit. Awwwards, Webby and FWA are craft/originality references only; no award scoring or award-level claim is made. The workflow remains an evidence-led operator task, so clarity, safe state communication, responsiveness and non-color cues take priority over decorative motion.

- [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Apple HIG — Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Material 3 — Foundations](https://m3.material.io/foundations/)
- [Material 3 — Adaptive canonical layouts](https://m3.material.io/foundations/layout/canonical-examples/overview)
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Awwwards — judging criteria example](https://www.awwwards.com/sites/peden-munk)
- [The Webby Awards — judging criteria](https://www.webbyawards.com/judging-criteria/)
- [FWA — archive](https://thefwa.com/archive/)

## Next validation steps

1. Decide whether these locales are actually in the first-release scope; if Portuguese is retained, decide the regional variant.
2. Have qualified Macau Portuguese and energy-domain reviewers review the complete strings in workflow context and establish an approved glossary.
3. Exercise language switching and state preservation, then test keyboard-only navigation, focus order, screen-reader language/announcements, zoom and reduced-motion behavior.
4. Review dense chart information with representative energy operators; test alternative annotation/legend/table compositions rather than treating the 900px rule as frozen.
5. Rerun the visual and accessibility review after an approved locale set and product design direction exist.
