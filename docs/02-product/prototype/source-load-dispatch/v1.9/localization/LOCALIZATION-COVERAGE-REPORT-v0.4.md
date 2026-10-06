# v1.9 Full-Workflow Localization Draft — Coverage Report v0.4

**Status:** Complete-coverage AI-assisted translation draft with static SVG chart text included. Not approved Macau Portuguese, not production runtime localization, and not evidence of user comprehension or an approved language policy.  
**Source:** PR #10 branch `product/source-load-economic-dispatch`, `v1.9/index.html`, Git blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902`.  
**Locale approval:** Unresolved. Portuguese regional variant and first-release language scope require owner/product review.

## Coverage

Catalog `locale-catalog-draft-full-workflow-v0.4.json` contains 346 contextual units across six workflow stages and shell/interaction groups. Strict complete-catalog validation was run against the exact pinned HTML source with `--require-complete`.

| Locale | Drafted units | Coverage | Missing | Validation errors |
|---|---:|---:|---:|---:|
| English (`en`) | 346 / 346 | 100% | 0 | 0 |
| Portuguese (`pt`) | 346 / 346 | 100% | 0 | 0 |

The validator reported `coverageGate: PASS`, `localeApproval: UNRESOLVED`, and the expected pinned source blob. The result establishes structural/catalog completeness only. The Traditional Chinese source remains the display source for `zh-Hant` in the preview.

## v0.4 correction: chart SVG text

The previous v0.3 catalog had 337 units and did not represent visible SVG plot annotations as independently translated strings. A browser screenshot review found Chinese plot labels still visible in English and Portuguese. The previous accessibility-tree text review had therefore overstated its coverage of visible chart text.

For v0.4, the preview builder identifies SVG `text`/`tspan` separately from ordinary page text and uses `svg-text` channel units. Nine contextual chart units were added, including the 18:00 boundary and ESS charge/discharge/SOC annotations. This avoids using full-length narrative translations for short plot labels and lets the translation draft fit the plot intentionally.

## Render and viewport evidence

See `localization-study-v0.3/REVIEW.md` and its `evidence/` folder. A browser matrix covered 90 combinations: 3 locales × 6 stages × 5 viewports (320×800, 375×812, 768×900, 1024×900, 1440×900). Recorded results: no page/active-section horizontal overflow, no width mismatch, no page errors, and no queried CJK SVG text in English/Portuguese. Thirteen samples contained a horizontally scrollable table/region within its own container. Eighteen stage screenshots were captured (dispatch comparison: 4 widths per locale; constraint analysis: 2 narrow widths per locale). Screenshot inspection was sampled and does not constitute user or assistive-technology validation.

At widths up to 900 CSS pixels, the preview hides direct plot annotations to address collisions while leaving the axes/series, legend, and data alternatives. Wider Portuguese chart density remains a review item. This breakpoint behavior is an evidence-driven prototype adjustment, not a finalized responsive specification.

## Scope and interpretation limits

- `346/346` means all catalog units have en/pt draft strings; it does not mean the product supports those locales end-to-end.
- Strings remain AI-assisted and unapproved. Qualified Macau Portuguese and energy-domain review, glossary approval, and English product terminology review are still required.
- The preview uses a locale query parameter; selector interaction, persisted user preference, state preservation, formatting, screen-reader language, and complete dynamic/error-state localization were not established by the matrix.
- No screen-reader review, full keyboard test, contrast audit, enlarged-text/zoom test, WCAG conformance review, or operator task evaluation is claimed.
- This study is for the six-stage v1.9 source/load-dispatch operational flow; it does not define a marketing website or a product-wide localization system.
- Locale set and Portuguese variant remain owner decisions. Do not describe this catalog as launch-ready or complete multilingual product support.

## Suggested next gate

After the owner confirms candidate launch locales and Portuguese variant, commission contextual linguistic/domain review; resolve a glossary; implement reviewed resources in the selected product runtime; test switching/state preservation and numerical/date formats; then repeat the six-stage, dynamic-state, keyboard, screen-reader and responsive review with recorded evidence.

