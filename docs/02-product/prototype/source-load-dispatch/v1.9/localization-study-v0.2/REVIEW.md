# Full-workflow locale preview v0.1 — review record

**Status:** Exploratory static-prototype translation study. English and Portuguese remain unapproved machine-assisted drafts. No launch locale policy or visual direction is approved.

## Source and build

- Source prototype: PR #10 source/load dispatch v1.9, pinned Git blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902`.
- Catalog: 337 contextual translation units, covering all six workflow stages and eight catalog groups.
- Preview builder: `docs/02-product/prototype/source-load-dispatch/v1.9/localization-study-v0.2/tools/build_localized_preview.py`.
- Output: `docs/02-product/prototype/source-load-dispatch/v1.9/localization-study-v0.2/index.html`.
- Builder fails if the source HTML blob differs from the catalog's pinned source.
- The preview is generated separately; it does not alter v1.9 or the current v2.7 proposal.

## Browser check performed (2026-10-06)

Opened the generated page in Codex In-app Browser at the `dispatchComparison` stage, separately loading `zh-Hant`, `en`, and `pt` via URL query parameter. Reviewed each initial page's accessibility tree. Checked the workflow/navigation labels, date and time selectors, synthetic-data and evidence boundaries, dispatch schedule, HVAC rebound, ESS/SOC explanation, unknown billing-period Pu, chart title/description, stage number, and prototype boundary.

- All three initial loads displayed the same stage-3 dispatch scenario. English and Portuguese primary stage-3 content and chart descriptions rendered in the selected language. The stage pager read “Stage 03 of 06” and “Etapa 03 de 06”.
- The English and Portuguese locale menus retain native-language names for the other choices; this is intentional.
- No obvious Traditional Chinese leakage appeared in the primary English or Portuguese stage-3 content. Brand, version, engineering abbreviations, units, and native locale names remain as designed.
- The page continued to identify the data as synthetic, describe tariff/billing evidence as unverified, leave Pu unknown, and state that no export, savings, or control execution is asserted.
- The browser check exposed no obvious translation-runtime error in the accessibility tree. It did not exercise a language change using the selector.

## Scope and limits

This checks browser-rendered accessibility-tree text for one workflow stage at three initial locales. It is not a visual inspection: CSS viewport size and screenshots were not captured. It does not verify responsive wrapping, all six stages, dialogs or review states, keyboard behavior, screen-reader language announcements, contrast, enlarged text, date/number formatting across locales, translation quality, Macau terminology, or operator comprehension. Query-loading locales does not prove that switching language preserves page or review state.

The catalog's 100% figure means that all extracted contextual units have draft strings; it does not mean the prototype is fully localized, the translation is correct, or multilingual support is approved. The separate v0.1 localization interaction study has stronger documented viewport/state checks for its single dispatch-comparison screen; this full-workflow preview extends the draft copy into the wider v1.9 workflow but has not repeated those interaction and viewport tests.

## Next evidence required

1. Review all English and Portuguese strings in context with qualified Macau energy-domain and language reviewers; decide the Portuguese regional variant and release locale policy.
2. Review every workflow stage and important partial, blocked, review, and replay state in each approved locale.
3. Capture rendered evidence at narrow mobile, tablet, and desktop widths; inspect wrapping, clipping, focus, zoom/text enlargement, contrast, and screen-reader announcements.
4. Test selector-driven locale switching and whether stage, selected interval, scenario, and review state are preserved or intentionally reset.
5. Evaluate with Macau commercial-building operators before claiming usability or pilot readiness.
