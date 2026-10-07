# v1.9 core-workflow translation draft v0.2

**Status:** AI-assisted draft, awaiting Macau energy-domain and language review. The JSON remains a non-runtime review artifact; no production locale or Portuguese regional variant is approved.

## Scope and source

- Pinned source: PR #10 v1.9 HTML, Git blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902`.
- Source locale: Traditional Chinese (`zh-Hant`); draft targets: English (`en`) and Portuguese (`pt`).
- Drafted groups: shared shell (65), data/contract evidence check (43), site energy model (35), and dispatch comparison (99): **242 of 337 contextual units (71.8%) per language**.
- Still untranslated: constraint analysis (48), SHADOW review (10), outcome replay (16), and dynamic interaction messages (21): **95 units**.
- Draft catalog: `localization/locale-catalog-draft-core-v0.2.json`; generator: `localization/tools/build_locale_draft_batch_v0_2.py`.

The catalog retains separate context keys for static text, accessible names, and stages. Every included value is tagged `DRAFT_NEEDS_MACAU_ENERGY_DOMAIN_REVIEW`. The separate v0.1 shell/evidence batch remains as the earlier review snapshot; this v0.2 batch expands it with both core dispatch stages.

## Product meaning preserved in the drafts

The copy keeps physical energy flow separate from billing and settlement. It distinguishes a displayed-window peak from billing-period Pu, keeps the example's 485 → 510 kW peak rebound visible, and states that tariff, contract, account mapping, meter window, and real-site capability are unverified. Solar export, cross-building sharing or credits, savings, EV cost allocation, and dispatch authority are not asserted. It labels the values as synthetic and states that the MVP prototype sends no equipment commands.

The draft glossary uses “dispatch” / “despacho,” “grid import” / “importação da rede,” “site” / “local,” and keeps ESS, HVAC/AVAC, SOC, Pu, SHADOW, and SI units recognizable. Portuguese wording is a neutral research draft; Macau terminology and regional choice need expert review. Some catalog entries are sentence fragments; review must consider surrounding UI context.

## Verification

The reproducible builder checks the source Git blob and expected unit counts before producing the draft JSON. The locale validator reports:

| Check | Result |
|---|---|
| Source blob | Exact match |
| Drafted units | 242/337 in each target locale (71.8%) |
| Remaining units | 95 in each target locale |
| Duplicate keys/context units | None |
| Placeholder mismatches | None |
| CJK characters left in translated values | None detected |
| Strict complete-catalog coverage | FAIL, as expected |

## Limits and next step

This is not wired into the v1.9 prototype, so it does not establish runtime language switching or preserve stage, interval, scroll, and review state. None of these 242 translations have had qualified human linguistic/domain review. Their rendered text expansion, enlarged-text behavior, contrast, keyboard access, screen-reader announcements, and operator comprehension have not been checked.

Next, draft and review constraint analysis, SHADOW review, outcome replay, and all 21 dynamic interaction messages. Then wire only fully reviewed contextual messages into a separate prototype increment; keep candidate locales visibly incomplete until the strict coverage report passes and the locale scope is decided.

