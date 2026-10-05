# v2.3 Locale Coverage Inventory

**Status:** Source inventory only. No launch locale or translation is approved; v2.3 remains a Traditional-Chinese-only research prototype.  
**Source:** `docs/02-product/prototype/source-load-dispatch/v2.3/index.html`, Git blob `6f199ddaee1f2a416b9925ce310a073b0455b054`.  
**Extraction:** Adapted the existing v1.9 standard-library HTML/script-literal inventory tool to v2.3 and ran it against the exact fetched source with the required blob check.  
**Tool:** [`extract_locale_catalog.py`](localization/tools/extract_locale_catalog.py). The generated [`locale-catalog-candidate.json`](localization/locale-catalog-candidate.json) is checked in for review; it is not connected to the UI runtime. Catalog SHA-256: `632f909641948641945c863dbe1f538f901447c225424b7d9ac9fe5f4f8e3c46`.

## Current coverage evidence

| Measure | v1.9 baseline | v2.3 exact source |
|---|---:|---:|
| Static text nodes (all six stages) | 429 | 520 |
| Unique static text values | 368 | 445 |
| Unique values containing Chinese | 292 | 365 |
| Non-empty text attributes | 23 | 27 |
| Unique Chinese attribute values | 21 | 25 |
| Dynamic Chinese script-literal candidates | 21 | 94 |
| Context/channel catalog units | 337 | 489 |

Counts are not translation-unit guarantees: repeated strings may have separate context keys; JavaScript literal scanning is heuristic and may yield fragments or miss assembled text.

## Locale status

- **Traditional Chinese (`zh-Hant`):** current source language; the UI declares `lang="zh-Hant"`. The 489-unit inventory has not been through a complete terminology/editorial review.
- **Portuguese (`pt`):** zero translated v2.3 units and no linguistic/energy-domain review.
- **English (`en`):** zero translated v2.3 units. English enum labels such as `PARTIAL`, `ALLOWED`, and `WITHHELD` are technical status codes, not complete English localization.
- The three locales remain a research/coverage set, not an owner-approved release commitment. Locale-specific date, number, currency, energy terminology, legal copy, and Macau Portuguese variant still require policy and qualified review.

## Added v2.3 language surface

The new inventory includes the four mixed-state selector labels, per-case summary announcements, physical/HVAC/ESS/economic dimension details, claim labels/reasons, and synthetic/no-control boundaries. Dynamic text and JSON-embedded strings are included in extraction candidates; a reviewer must consolidate fragments and check each state in context.

The v1.9 catalog remains pinned to its v1.9 source blob and must not be reused as though it covered v2.3. A generic source-pinned validation run against the v2.3 catalog and exact source passed catalog-integrity checks with no errors: 489 units, `pt` 0/489 (0.0%), `en` 0/489 (0.0%), coverage incomplete. This verifies catalog/source integrity and reports missing translation; it does not approve locale scope or establish i18n runtime support. No catalog/runtime binding, language selector, persistence behavior, localized data formatting, screen-reader review, or text-expansion browser review is claimed.

## Next localization evidence

1. Review the 489 source units in stage/channel context and resolve duplicated/fractured candidates.
2. Approve the actual release locale set and Portuguese/English regional formatting policy.
3. Draft complete translations for all critical paths and states; have Macau energy-domain reviewers validate terminology and source-preserving claims.
4. Bind a complete locale catalog only after translation review; verify parity for six stages, four v2.3 claim-state cases, accessible names, errors, empty/loading/blocked states, and SHADOW review.
5. Inspect rendering and text expansion at 320, 375, 768, 1024 and 1440 CSS px in each approved locale. This v2.3 source has not been browser-rendered or localization-tested.

This inventory does not count English state tokens as translated copy, and does not establish multilingual product support.
