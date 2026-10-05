# v1.9 Full-Workflow Localization Draft — Coverage Report v0.3

**Status:** Complete-coverage AI-assisted translation draft; not approved Macau Portuguese, not runtime localization, and not evidence of user comprehension.

## Source and scope

- Source HTML: PR #10 v1.9 source, Git blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902`.
- Source locale: Traditional Chinese (`zh-Hant`). Candidate draft locales: English (`en`) and Portuguese (`pt`). The Portuguese regional variant remains undecided.
- Catalog: `locale-catalog-draft-full-workflow-v0.3.json` (337 contextual units).
- Builder: `complete_translation_draft_v0_3.py`; the original v0.2 catalog remains unchanged.
- Scope includes shell, evidence qualification, site model, dispatch comparison, cost/constraint analysis, SHADOW review, outcome replay, and dynamic interaction strings.

## Coverage and structural validation

| Locale | Drafted units | Coverage | Missing units | Structural/placeholder errors |
|---|---:|---:|---:|---:|
| English | 337 / 337 | 100% | 0 | 0 |
| Portuguese | 337 / 337 | 100% | 0 | 0 |

Validated with the repository's `validate_locale_catalog.py` against the pinned v1.9 HTML using strict complete-catalog mode. The validator reported six workflow stages and all eight catalog groups. No source code or prototype runtime was changed by this draft.

## Quality safeguards preserved in drafted text

- Physical schedule and financial settlement remain separate.
- Unknown or unverified Pu, account/tariff mapping, ESS capability, HVAC comfort, export revenue, and savings remain explicitly unknown or withheld.
- The display-window peak/rebound is not relabeled as billing-period demand.
- SHADOW review states, illustrative requests, and replay remain page-only/unimplemented; no translation implies authorization or equipment control.
- Dynamic HTML placeholder `<strong>` and source numeric/SI content are retained for the catalog validator.

## Limits and required review

- All 95 newly added units per language are machine-assisted drafts. The prior 242 units per language are also unapproved drafts.
- Portuguese wording is neutral research Portuguese. Macau-specific electricity, billing, and operator terminology needs a qualified local language/domain review; the appropriate Portuguese regional variant is undecided.
- English wording has not received professional product or energy-domain review.
- Coverage is catalog coverage only. No language switch, translated prototype render, state-preservation test, viewport comparison, screen-reader check, or operator evaluation was performed.
- This v1.9 catalog is not the latest prototype's runtime resource set. The current v2.7 proposal remains Traditional Chinese-only and would need its own source-pinned catalog and rendered language/state review.
- Do not claim product-level multilingual support or release readiness from this artifact.

## Suggested review sequence

1. Confirm intended first-release locale set and Portuguese regional style.
2. Have a Macau energy-domain reviewer and qualified translators review the complete strings in stage context, resolving glossary choices and sentence fragments.
3. After approval, wire reviewed resources into a separate prototype increment; do not mutate v1.9's source stimulus.
4. Render all six stages and critical blocked/partial/review/replay states in each approved locale at desktop, tablet, and narrow mobile widths; record line wrapping, focus, screen-reader language/announcements, and numerical/date formatting.
5. Re-run the strict catalog checker and add locale/state/browser evidence before any claim of complete support.
