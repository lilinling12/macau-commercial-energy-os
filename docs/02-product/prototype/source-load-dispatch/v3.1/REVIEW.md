# Localized dispatch workflow v3.1 — review record

**Review date:** 2026-10-07  
**Status:** Three-locale design-study prototype on PR #10; language scope, translations and product design remain unapproved.  
**Branch:** `product/source-load-economic-dispatch`  
**Scenario:** Same fixed six-hour synthetic schedule used in v3.0; not forecast, optimization output, Macau site data or bill calculation.

## What changed

v3.1 adds a full six-stage localized workflow prototype in candidate Traditional Chinese, Portuguese and English:

1. Data, meter/account, tariff/contract, asset and forecast evidence;
2. Physical energy-flow model separated from account settlement;
3. Baseline/candidate import comparison and interval schedule;
4. Energy, full-bill and service/safety claims shown separately;
5. Page-local Shadow research review;
6. Measurement, pinned-input and replay prerequisites.

All three language versions use the same synthetic data: baseline imports 8, 8, 6, 4, 8, 10 kW; candidate imports 9, 9, 11, 3, 5, 7 kW. Both total 44 kWh for the six intervals; the maximum interval rises from 10 to 11 kW. The UI states that this is not billed demand or a Macau Pu calculation. No forecast, PV profile, ESS profile, bill savings, export credit, service feasibility, controllability or equipment command is presented as verified.

The locale identifiers `zh-Hant-MO`, `pt-MO` and `en` are implementation-study candidates only. Their selection does not establish audience preference, legal obligation or finalized locale policy.

## Validation performed

- Parsed the inline JavaScript with Node.js `v22.20.0` using `node --check`; the final source passed.
- Loaded a fresh local browser tab after the final code edits; it rendered and had zero console errors on that clean load.
- Inspected all 6 stages in each candidate locale at viewport widths 320, 375, 768, 1024 and 1440 CSS px (90 combinations). The final responsive CSS had no document/body horizontal overflow, blank stage headings or HTML-language mismatch.
- The 320 px first-pass review exposed a page-width overflow caused by the stage rail’s min-content width. Added `min-width: 0` to the rail and repeated the matrix successfully. The stage strip itself scrolls horizontally by design at compact widths.
- After the matrix, separately checked the final keyboard change: ArrowRight from stage 1 activates and focuses stage 2. Checked the final localized accessible labels and document title.
- Selected “Request scenario changes” in English, switched to Portuguese, and verified the selected state persisted with Portuguese status text.
- A prior intermediate, syntactically invalid local draft produced a console error before correction. A fresh post-correction tab loaded without console errors; the retained older tab may still show that historical console entry.
- Screenshots were inspected during the pass at narrow mobile and 1440 px desktop. The compact rail and content fit within the viewport after correction.

These checks cover prototype behavior and layout only. They are not full keyboard/screen-reader testing, WCAG conformance, translation QA, native-speaker review or user research.

## Remaining design and localization work

- Portuguese wording and `pt-MO` must be reviewed by a Macau Portuguese language professional; do not assume this is the correct locale tag or spelling policy.
- Traditional Chinese technical terminology and written style need review by local energy operators; this prototype is not Cantonese-language copy.
- Confirm whether all three languages are required, for which roles and artifacts, and whether user, organization or browser preference should select the initial language.
- Review MOP/number/date formatting, site timezone, long table labels, 200% text zoom, narrow-screen chart/table use, complete keyboard interaction, screen-reader announcements and color/non-color status cues.
- Review whether product-generated exports and audit narratives need each locale or should preserve source-language evidence alongside translated interface labels.
- Conduct role-based task review with building/energy operations, facilities engineering and finance/billing reviewers before calling the design validated.
- The current draft has not re-run the full 90-case matrix after the final navigation aria-label and keyboard-focus changes; these were separately checked for behavior and do not alter geometry. Repeat the matrix if the stage rail or language copy changes.

## Traceability

- Locale evidence and scope boundary: [LOCALIZATION-STRATEGY-v0.1.md](../../LOCALIZATION-STRATEGY-v0.1.md).
- v3.0 Chinese workflow and previous UX review: [v3.0 review](../v3.0/REVIEW.md).
- Locale background: Macao Government Tourism Office [Language](https://www.macaotourism.gov.mo/en/travelessential/about-macao/language); Macao Legal Affairs Bureau [Decree-Law 101/99/M](https://bo.dsaj.gov.mo/bo/ba/i/99/50/declei101.asp). These describe official language context, not a private-product language mandate.
- Accessibility basis: W3C [WCAG 2.2](https://www.w3.org/TR/WCAG22/), especially 3.1.1 and 3.1.2 for page and passage language.

No Gate, product scope, visual system, architecture, locale scope or control authority is approved by this prototype. G7.9 Step 3 remains open.
