# Source/load dispatch v1.9 — locale coverage baseline

**Status:** Review inventory only. The prototype remains `zh-Hant` only; Portuguese and English are untranslated, and the release locale set remains an owner decision.

## Source and extraction

- Current source: PR #10, `docs/02-product/prototype/source-load-dispatch/v1.9/index.html`.
- Exact GitHub blob: `b2ebcaf4cfd59d0825fb105ed0d320808776b902`.
- The v1.8 standard-library HTML/script-literal extractor was adapted to v1.9 identifiers and run against the fetched source. Its source-blob check passed.
- Candidate locales: `zh-Hant`, `pt`, `en`; this is a discovery set, not an approved release-language commitment.

## Extracted v1.9 source surface

| Inventory measure | Count |
|---|---:|
| Static text nodes (hidden stages included) | 429 |
| Unique text values | 368 |
| Unique text values containing Chinese characters | 292 |
| Non-empty `aria-label`, `title`, `placeholder`, and `alt` values | 23 |
| Unique Chinese values in those attributes | 21 |
| Chinese inline-script string-literal candidate values | 21 |
| Candidate catalog units with stage/channel context | 337 |

The 337 units are not 337 distinct phrases: keys preserve stage and content channel. Script-literal extraction can include sentence fragments and may miss values assembled from variables. Runtime-generated stage navigation is represented through source literals, not rendered-node counts. Manual review is required before translation.

## Implications for the next prototype increment

- Translation scope includes all six workflow stages, planning context, chart legends/labels, table headers, modal content, warnings, accessible names, dynamic review feedback and stage navigation.
- Translate whole contextual messages, not isolated fragments. Keep site IDs, source evidence, raw readings, MOP and SI quantities independent of display locale.
- Preserve `Asia/Macau` time semantics when UI language changes. Select and validate the regional Portuguese/English formatting policy separately.
- The language selector must preserve site, horizon, comparison, stage, scroll/task context and review state without changing inputs or recalculating a different schedule.
- Test natural text wrapping and reflow at 320, 375, 768, 1024 and 1440 CSS px, plus enlarged text. Essential warnings and actions must never be clipped or reduced to unexplained ellipses.
- Report missing translations as incomplete locale coverage; do not show a few translated controls as multilingual support.

## Design guidance applied

The project UI/UX skill requires locale-aware terminology, dates, numbers and units, full critical-path coverage, and responsive review in Traditional Chinese, Portuguese and English once confirmed. The `ui-ux-pro-max` search first returned mostly unrelated results; a narrower retry surfaced directly relevant high-severity guidance: content-driven text reflow, complete access to essential action/error/safety text, and wrapping rather than clipping content collections. These are used as review criteria, not as proof of conformance.

## Limits and next evidence

This is source inventory, not translation, runtime locale switching, linguistic review, rendered text-expansion testing, WCAG evaluation, operator research or owner approval. The next prototype increment should implement one complete locale switch over the real workflow using reviewed messages, then expand and verify all six stages and meaningful states in each owner-approved locale. Macau-local energy, tariff, settlement, safety and comfort terminology needs qualified human review.

## Progress update — single-screen study and coverage checker

The next increment now includes a [separate one-screen locale study](localization-study-v0.1/REVIEW.md) for the dispatch-comparison task. It renders Traditional Chinese, English, and Portuguese draft copy, and records browser checks at 320, 375, 768, 1024, and 1440 CSS px. It covers interval selection and the accessible data-table disclosure; it does not localize this six-stage v1.9 source or fulfill the full-workflow requirement above. The companion review explicitly records that the translations need local technical review.

A standard-library [catalog validator](localization/tools/validate_locale_catalog.py) now verifies the catalog's Git blob against the source, checks key/unit uniqueness and placeholder preservation, reports translation coverage by stage, and can enforce completeness with `--require-complete`. Run it from the repository root:

```sh
python docs/02-product/prototype/source-load-dispatch/v1.9/localization/tools/validate_locale_catalog.py docs/02-product/prototype/source-load-dispatch/v1.9/localization/locale-catalog-candidate.json docs/02-product/prototype/source-load-dispatch/v1.9/index.html
```

Against source blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902`, catalog integrity passes for 337 units across the six workflow stages plus shell and interaction messages. The original `locale-catalog-candidate.json` remains an untranslated baseline at **0/337**. The earlier [shell/evidence draft v0.1](localization/TRANSLATION-DRAFT-SHELL-EVIDENCE-v0.1.md) contains 108 units (32.0%). The expanded [core-workflow draft v0.2](localization/TRANSLATION-DRAFT-CORE-v0.2.md) covers shared shell (65), evidence review (43), site model (35), and dispatch comparison (99): **242/337 per language (71.8%)** in `locale-catalog-draft-core-v0.2.json`. Reproduce v0.2 with `localization/tools/build_locale_draft_batch_v0_2.py`. Constraint analysis (48), SHADOW review (10), outcome replay (16), and dynamic interaction messages (21) remain untranslated, so strict all-catalog coverage correctly reports `FAIL`. All draft translations require Macau energy-domain and Portuguese-variant review; they are not wired into the prototype, do not establish runtime localization, and do not approve a release-language set. The checker does not judge translation accuracy, rendered source parity, screen-reader behavior, or owner approval.
