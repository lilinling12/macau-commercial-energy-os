# Full-workflow locale preview v0.2 — review record

**Status:** Exploratory static-prototype translation study. English and Portuguese remain unapproved machine-assisted drafts. No launch locale policy or visual direction is approved.

## Source and build

- Source prototype: PR #10 source/load dispatch v1.9, pinned Git blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902`.
- Catalog: 337 contextual translation units, covering all six workflow stages and eight catalog groups.
- Preview builder: `docs/02-product/prototype/source-load-dispatch/v1.9/localization-study-v0.2/tools/build_localized_preview.py`.
- Output: `docs/02-product/prototype/source-load-dispatch/v1.9/localization-study-v0.2/index.html`.
- Builder fails if the source HTML blob differs from the catalog's pinned source.
- The preview is generated separately; it does not alter v1.9 or the current v2.7 proposal.

From the `localization-study-v0.2` directory, reproduce the page with:

```powershell
python tools/build_localized_preview.py --source ../index.html --catalog ../localization/locale-catalog-draft-full-workflow-v0.3.json --output index.html
```

## Browser check performed (2026-10-06)

Opened the generated page in Codex In-app Browser at each of the six workflow anchors for English (`en`) and Portuguese (`pt`), using locale query parameters. Also opened Traditional Chinese (`zh-Hant`) at the dispatch-comparison stage as the source-language reference. Reviewed the accessibility tree for the active stage in each locale. The reviewed stages were data/contracts, site energy model, timeline/schedule comparison, costs/constraints, SHADOW review, and monitoring/replay.

- English and Portuguese showed the matching stage number, localized stage navigation, titles, tables/statuses, descriptions, controls, and stage-specific evidence boundaries for all six stages. The stage-3 chart title and accessible description appeared in the selected language.
- The stage-2 review confirmed that physical flows (grid import, PV, ESS and load) remained distinct from tariff/account settlement; EV charging and hot-water load remained explicitly excluded for insufficient evidence in both target locales.
- The stage-4 review found a punctuation seam in the partial-tariff example (`tariffs ;` / `verificadas ;`). The translation draft was corrected to carry the semicolon with the emphasized phrase; a fresh browser load showed `tariffs; 2 other intervals…` and `verificadas; 2 outros intervalos…`.
- In stage 5, reviewed the localized illustrative review actions and disabled equipment-control state. In stage 6, reviewed the localized no-measurement/no-execution states and replay evidence requirements.
- The English and Portuguese locale menus retain native-language names for the other choices; this is intentional.
- No obvious Traditional Chinese leakage appeared in the primary English or Portuguese stage content reviewed. Brand, version, engineering abbreviations, units, and native locale names remain as designed.
- The page continued to identify the data as synthetic, describe tariff/billing evidence as unverified, leave Pu unknown, and state that no export, savings, or control execution is asserted.
- The browser check exposed no obvious translation-runtime error in the reviewed accessibility trees. It did not exercise a language change using the selector.

## Scope and limits

This checks browser-rendered accessibility-tree text for all six stages in two draft locales, plus the source language at stage 3. It is not a visual inspection: CSS viewport size and screenshots were not captured. It does not verify responsive wrapping, selector-driven language switching, stage/state preservation, dialog states, keyboard behavior, screen-reader language announcements, contrast, enlarged text, date/number formatting across locales, translation quality, Macau terminology, or operator comprehension. Loading each locale by URL does not prove that switching language preserves page or review state.

The catalog's 100% figure means that all extracted contextual units have draft strings; it does not mean the prototype is fully localized, the translation is correct, or multilingual support is approved. The separate v0.1 localization interaction study has stronger documented viewport/state checks for its single dispatch-comparison screen; this full-workflow preview extends the draft copy into the wider v1.9 workflow but has not repeated those interaction and viewport tests.

## Next evidence required

1. Review all English and Portuguese strings in context with qualified Macau energy-domain and language reviewers; decide the Portuguese regional variant and release locale policy.
2. Review every workflow stage and important partial, blocked, review, and replay state in each approved locale.
3. Capture rendered evidence at narrow mobile, tablet, and desktop widths; inspect wrapping, clipping, focus, zoom/text enlargement, contrast, and screen-reader announcements.
4. Test selector-driven locale switching and whether stage, selected interval, scenario, and review state are preserved or intentionally reset.
5. Evaluate with Macau commercial-building operators before claiming usability or pilot readiness.
