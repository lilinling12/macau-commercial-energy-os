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

## Browser rendering review (2026-10-06)

Opened the generated preview in the in-app browser at all six workflow anchors in English (`en`) and Portuguese (`pt`), plus the Traditional Chinese (`zh-Hant`) source at stage 3. Reviewed the active-stage browser accessibility tree for each locale load. This checks rendered labels, stage content, controls, chart descriptions, navigation, and evidence/claim boundaries; it is not a visual screenshot or a full interaction test.

The detailed check record, generated page, and reproducible builder are delivered under `v1.9/localization-study-v0.2/` in the repository.

- English and Portuguese rendered all six stages, including data/contracts, physical site model, source/load schedule, economics and constraints, SHADOW review, and monitoring/replay. Stage-2 rendering kept physical flows separate from account/tariff settlement and preserved the exclusion of evidence-deficient EV and hot-water loads.
- Stage 4 exposed a punctuation seam across adjacent rich-text nodes (`tariffs ;` / `verificadas ;`). The translations were adjusted, the generated page rebuilt, and a fresh browser load showed the punctuation joined to the emphasized phrase.
- Stage 4 also exposed untranslated Traditional Chinese in the responsive table's `data-label` attributes. The preview builder now translates `data-label` using the existing contextual labels; a fresh English/Portuguese browser load no longer exposed the Chinese labels in the accessibility tree.
- The stage-3 dispatch comparison retained synthetic-data boundaries, HVAC rebound, ESS/SOC narrative, unknown billing-period Pu, localized chart title/description, and stage position in both draft locales. Traditional Chinese at stage 3 retained the source wording.
- The stage-5 view showed page-only review actions and disabled equipment control in both locales. Stage 6 showed no site measurements or execution and the localized replay evidence requirements.
- The locale menu keeps native language names, so `繁體中文` appears in the Portuguese and English menus by design. No obvious Traditional Chinese leakage appeared in the primary English or Portuguese content reviewed; brand/version strings and engineering abbreviations remain.
- Locales were loaded by URL parameters. The selector was present, but switching it and preserving stage/review state were not tested.
- This remains an accessibility-tree text review. No CSS viewport size, screenshot, responsive visual layout, or text wrapping was checked, and it is not proof that every interaction/state or translation is correct.
- The page's own boundary copy continued to mark values as synthetic and denied claims of grid export, cross-building credits, savings, or executed equipment control.

Viewport dimensions and screenshots were not captured. No mobile/tablet layout, all-stage render, keyboard-only flow, screen-reader announcement behavior, contrast, translation quality, or operator comprehension was tested. Browser tree evidence alone cannot establish visual quality, accessibility conformance, or localization approval.

## Limits and required review

- All 95 newly added units per language are machine-assisted drafts. The prior 242 units per language are also unapproved drafts.
- Portuguese wording is neutral research Portuguese. Macau-specific electricity, billing, and operator terminology needs a qualified local language/domain review; the appropriate Portuguese regional variant is undecided.
- English wording has not received professional product or energy-domain review.
- Catalog coverage is complete, and English/Portuguese browser text was reviewed at all six stages; Traditional Chinese was reviewed at stage 3. No language-switch interaction, state-preservation test, viewport comparison, full screen-reader check, or operator evaluation was performed.
- This v1.9 catalog is not the latest prototype's runtime resource set. The current v2.7 proposal remains Traditional Chinese-only and would need its own source-pinned catalog and rendered language/state review.
- Do not claim product-level multilingual support or release readiness from this artifact.

## Suggested review sequence

1. Confirm intended first-release locale set and Portuguese regional style.
2. Have a Macau energy-domain reviewer and qualified translators review the complete strings in stage context, resolving glossary choices and sentence fragments.
3. After approval, wire reviewed resources into a separate prototype increment; do not mutate v1.9's source stimulus.
4. Render all six stages and critical blocked/partial/review/replay states in each approved locale at desktop, tablet, and narrow mobile widths; record line wrapping, focus, screen-reader language/announcements, and numerical/date formatting.
5. Re-run the strict catalog checker and add locale/state/browser evidence before any claim of complete support.
