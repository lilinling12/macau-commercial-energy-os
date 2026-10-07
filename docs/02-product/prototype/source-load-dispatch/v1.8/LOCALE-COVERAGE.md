# v1.8 dispatch prototype — locale surface inventory

**Status:** Inventory only. No Portuguese or English translation, launch locale decision, or localization approval is claimed.  
**Source:** PR #10 `docs/02-product/prototype/source-load-dispatch/v1.8/index.html`, source blob `ea0d3087815f52764ac9e7ac227ef64a2631c155`, fetched 2026-10-05.  
**Extraction:** Rendered DOM inspection plus inline-script string-literal scan in the local browser at `http://127.0.0.1:8773/dispatch-v18-study.html`; the page language is `zh-Hant`.

## Surface counts

| Surface | Inventory result |
|---|---:|
| DOM text nodes, including hidden workflow stages and the modal | 433 |
| Unique trimmed DOM text values | 371 |
| Unique DOM text values containing Traditional Chinese characters | 296 |
| `aria-label`, `title`, `placeholder`, and `alt` attributes with values | 24 total; 23 contain Chinese; 22 unique Chinese values |
| Distinct Chinese literals found in inline interaction code | 21 |

These counts are overlapping inventory categories, not a summed translation-unit total. Numbers, units, duplicated labels, and interpolation fragments need key-level normalization before a production catalog can be sized.

## Six-stage text distribution

Counts below are unique DOM text-node values containing Chinese characters inside each stage; each stage includes its currently hidden content in the DOM.

| Stage | Chinese text values |
|---|---:|
| 01 — Data and contract evidence | 42 |
| 02 — Physical site model | 35 |
| 03 — Schedule comparison | 84 |
| 04 — Cost, constraints and evidence | 48 |
| 05 — SHADOW review | 17 |
| 06 — Outcome monitoring and replay | 16 |

The full page also includes navigation, planning controls, compact mobile context, chart/table captions and labels, footer/boundary text, and modal copy. The 21 inline-script literals include table toggle labels, chart-focus announcements, review-state labels/messages/toasts, and stage-pager labels. A localization pass that handles only the visible navigation would leave critical workflow and assistive text untranslated.

## Required localization completion gate

Before calling the product multilingual, create a stable keyed catalog for every static string, accessible name, chart/table label, modal, status, warning, error/empty state, toast and dynamic interaction message. For each approved locale:

- No Chinese UI string remains in Portuguese or English flows, including hidden stages, modal content, assistive names and interaction feedback.
- Preserve locale-neutral numeric/domain values and source provenance. Format currency, dates, numbers and time through explicit locale rules; retain MOP, SI units and `Asia/Macau` semantics where applicable.
- Review long Portuguese strings and Traditional Chinese variants for wrapping, responsive layout, table access and focus visibility.
- Review energy, tariff, settlement and safety terminology with qualified Macau-local reviewers; translation alone cannot resolve legal or contract meaning.
- Exercise every workflow stage, meaningful control state, keyboard path and error/blocked/partial state in each owner-approved locale. Record actual viewports and translation-review evidence.

Macao's official Chinese/Portuguese status and the commercial use of English support testing the three locales; the reviewed sources do not prove that this private product is legally required to ship all three or establish operator preference. See `MACAU-DISPATCH-LOCALIZATION-REQUIREMENTS-v0.1.md`. The release locale set remains an owner decision, followed by WP-4 user research.

