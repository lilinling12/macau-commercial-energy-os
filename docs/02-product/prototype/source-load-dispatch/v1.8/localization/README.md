# v1.8 locale catalog candidate

**Status:** review aid only; not a production localization catalog. The release locale set is not approved.

## Source and output

- Source: `index.html`, v1.8, `zh-Hant`, Git blob `ea0d3087815f52764ac9e7ac227ef64a2631c155`.
- Candidate locales for review: `zh-Hant` (source), Portuguese (`pt`) and English (`en`). Macau-specific Portuguese locale selection is still open.
- The generated JSON contains 337 candidate message units. Every row has a stable candidate key, source text, source location line(s), and `pt`/`en` translation slots set to `null`.
- The extractor verifies the exact source Git blob before producing output. Run it only against the reviewed v1.8 source; update the pinned blob deliberately when the source changes.

## Human review required

The generator uses Python's standard-library HTML parser and a heuristic scan of inline-script string literals. It is a starting inventory, not a complete localization extractor. Review each key and context, especially dynamic fragments, duplicate wording, concatenated messages, values built outside literals, chart labels, accessible names, keyboard instructions and runtime-generated pager copy. Add missing strings and states manually. Do not translate fragments independently where that would break grammar or interpolation.

Translations are intentionally absent. Qualified Macau-local reviewers should validate energy, tariff, settlement, safety and comfort terminology. Product owners must approve the release locale set. Localized layouts, number/currency/date/time formatting, keyboard and assistive-technology behavior must be reviewed in each approved locale before claiming multilingual support.

## Reproduce and validate

From the v1.8 directory, use Python 3.10 or later and run:

```sh
python localization/tools/extract_locale_catalog.py index.html localization/locale-catalog-candidate.json --source-blob ea0d3087815f52764ac9e7ac227ef64a2631c155
```

The candidate JSON is for translation review and coverage tracking. It is not wired into the prototype, not a runtime locale bundle, and does not establish complete translation, user acceptance, or launch readiness.
