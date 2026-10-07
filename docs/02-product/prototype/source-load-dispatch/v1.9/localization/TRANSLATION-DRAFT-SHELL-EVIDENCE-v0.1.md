# v1.9 locale draft batch — shared shell and evidence review

**Status:** AI-assisted translation draft for specialist review. Not wired into the prototype, not approved for production, and not evidence of complete multilingual support.

## Source and scope

- Source: PR #10 v1.9 prototype at Git blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902`.
- Source locale: Traditional Chinese (`zh-Hant`).
- Draft targets: English (`en`) and Portuguese (`pt`). The Portuguese regional variant remains undecided.
- Included groups: shared application shell (65 contextual units) and evidence/contract qualification (43 units).
- Excluded groups still untranslated: site model (35), dispatch comparison (99), constraint analysis (48), SHADOW review (10), outcome replay (16), and dynamic interaction strings (21).
- Coverage in this partial catalog: 108/337 units per target locale, or 32.0%. The untranslated baseline inventory remains unchanged.

## Translation approach and terminology

The drafts preserve source evidence, status labels, product boundaries, and all numeric/SI content. They keep physical model readiness separate from economic readiness, and preserve the distinction between site authorization and account access. Repeated values reuse one translated phrase while retaining the source catalog's stage/channel-specific keys.

The provisional glossary uses “dispatch” / “despacho” for 調度, “site” / “local” for 站點, “settlement” or billing context for 結算, “grid import” / “entrada da rede” for 電網進線, and keeps ESS, HVAC/AVAC, SOC, Pu, SHADOW, DEMO-04, and SI units recognizable. These are translation choices for review, not an approved Macau product glossary. Tariff, demand, Pu, injection/export, and account/settlement terms need local energy-domain review.

Some catalog units are sentence fragments extracted from the source DOM. The builder marks each translated unit `DRAFT_NEEDS_MACAU_ENERGY_DOMAIN_REVIEW`; fluent whole-screen copy still requires reading each phrase in context.

## Validation evidence

The deterministic builder checks the exact Git blob and expected unit counts before creating the draft JSON. The coverage validator then checked the draft against the same HTML source:

| Check | Result |
|---|---|
| Pinned source blob | Match |
| Target groups | 65 shared-shell + 43 evidence-review units |
| English draft coverage | 108/337 (32.0%) |
| Portuguese draft coverage | 108/337 (32.0%) |
| Duplicate catalog key/unit or missing placeholder errors | None |
| Remaining Chinese characters in translated values | None detected |
| Strict all-catalog coverage mode | FAIL, as expected |

## Limits and next step

This batch does not change `index.html`, provide runtime language switching, or show the translated content rendered. Responsive reflow, enlarged text, keyboard and screen-reader behavior, translation accuracy, and operator comprehension remain unverified for these strings. Do not copy these drafts into a live operator UI before Macau Portuguese and energy-domain review.

Next translation batch: site model (35 units) and dispatch comparison (99 units), with special review of physical balance, ESS charging/discharging, interval selection, bill settlement, full-horizon peak/rebound, and the existing SHADOW boundary. Expand to the remaining stages and interaction strings before claiming full-workflow locale coverage.

