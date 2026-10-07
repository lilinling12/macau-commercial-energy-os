# Macau Dispatch Localization Requirements v0.1

**Status:** Product and UX review proposal; no launch locale or translation is owner-approved.  
**Date:** 2026-10-05  
**Applies to:** PR #10 source/load dispatch flow; read with PR #8's [Localization and Internationalization Design v0.1](https://github.com/lilinling12/macau-commercial-energy-os/blob/docs/product-architecture-roadmap/docs/03-architecture/detailed-design/LOCALIZATION-AND-I18N-DESIGN-v0.1.md) and product PRD QLR-01.  
**Prototype evidence:** PR #10 v1.7, v1.8 and v1.9 are Traditional-Chinese-only; their labels do not establish multilingual support. The v1.9 [`locale surface inventory`](prototype/source-load-dispatch/v1.9/LOCALE-COVERAGE.md) fingerprints current source blob `b2ebcaf4cfd59d0825fb105ed0d320808776b902` and records 429 static text nodes, 292 Chinese text values, 23 non-empty text attributes, 21 dynamic Chinese string candidates and 337 context/channel-aware candidate catalog units.

## 1. Macau language evidence and product inference

- The Macao Government Tourism Office states that Chinese and Portuguese are official languages, Cantonese is most widely spoken, and English is generally used in trade, tourism and commerce. This supports validating all three written UI locales for a local commercial product.
- The official source does not prove that every energy buyer, facilities operator, finance user, or integrator prefers the same interface language. It does not by itself impose a three-language requirement on this private product.
- **Product recommendation for owner review:** design and evaluate the pilot's complete critical task flow in Traditional Chinese, Portuguese and English. Do not ship only translated navigation labels while leaving warnings, constraints, chart semantics or recovery states untranslated.
- Interview users by role and task before approving the release locale set. Record spoken language, written/UI preference, source-document language and terminology preference separately. Cantonese is a spoken-language context; do not present it as a written UI locale.
- Follow the project i18n proposal's neutral tags `zh-Hant`, `pt`, and `en` during discovery. Validate whether a regional Portuguese tag and Macau-specific terminology are needed before product freeze.

**Primary sources:**

- Macao Government Tourism Office, [Language — English](https://www.macaotourism.gov.mo/en/article/about-macao/language) and [Language — Traditional Chinese](https://www.macaotourism.gov.mo/zh-hant/travelessential/about-macao/language), accessed 2026-10-05.
- Macao SAR Government Portal, [Laws](https://www.gov.mo/en/laws/): its English law pages identify English as a reference translation from Chinese originals and direct readers to Traditional Chinese or Portuguese when an English version is absent. Preserve legal/customer source material in its original language; do not make an English UI translation authoritative.

## Primary-source legal-scope recheck — 2026-10-07

The current primary text of Article 9 of the Macao Basic Law, published by the Legislative Assembly in Traditional Chinese and Portuguese, says that the MSAR executive, legislative and judicial organs may use Portuguese in addition to Chinese, and that Portuguese is also an official language. This confirms Chinese and Portuguese as official languages in the stated governmental context. The Macao Government Tourism Office separately describes Cantonese as most widely spoken and English as generally used in trade, tourism and commerce.

Product implication: retain `zh-Hant`, `pt` and `en` as discovery candidates for the commercial-operations workflow, but do not infer from Article 9 that a private energy-software product has a statutory three-language UI obligation, or that English is an official language. The law establishes context; launch locale scope must still be validated with pilot customers and role-based users. This is a product-research note, not legal advice.

Primary references checked 2026-10-07:

- Macao SAR Basic Law, Article 9 — [Legislative Assembly, Traditional Chinese](https://al.gov.mo/zh/basic-law) and [Portuguese](https://www.al.gov.mo/pt/basic-law).
- Macao Government Tourism Office, [Language (English)](https://www.macaotourism.gov.mo/en/travelessential/about-macao/language) and [語言 (Traditional Chinese)](https://www.macaotourism.gov.mo/zh-hant/travelessential/about-macao/language).

## 2. Locale behavior proposal

- Provide one complete UI locale at a time, selected explicitly by the user. Do not put three languages on every control or table row by default.
- Offer a persistent, text-labeled language selector with native names: 繁體中文, Português, English. Do not use flags as language identifiers.
- Changing locale preserves the current site, date/horizon, selected comparison, disclosure state where practical, and scroll/task context. It must not silently submit, recalculate with different semantics, reset review state, or change source evidence.
- Keep locale preference, site timezone, customer-document language and translated-display language distinct. Macau timezone display is `Asia/Macau`; changing UI language must not change the time basis.
- If a translation is unavailable, expose a clear incomplete-locale state and return to the selected language's documented fallback. Do not mix arbitrary English labels into a screen that appears fully localized.
- Customer bills, contracts, tariff notices, equipment labels and external source records remain in their source form/language. Any translation shown alongside them must be identified, versioned and marked as human-reviewed or machine-generated. A machine translation is never the source of settlement/legal truth.

## 3. Required critical-path coverage by workflow stage

The six stages in the dispatch workflow must be translated consistently in all selected locales. Include controls and non-happy-path states in the same coverage review.

| Stage | Content that must be localized | Required states / semantics |
|---|---|---|
| 1. Data and contract verification | Site/source labels, meter and contract relationships, source snapshot, coverage, freshness, effective dates, document language and evidence links | Ready, missing, unmapped, ambiguous, stale, expired, conflicting, partial; explain which claims are blocked |
| 2. Site energy model | Grid import, on-site PV, ESS, meters, HVAC and other site-qualified loads; physical graph vs settlement/account relationship | Verified, proposed mapping, unknown, excluded, not applicable; never imply that physical connection establishes a billing credit |
| 3. Forecast and schedule comparison | Baseline/candidate, forecast/scenario label, interval, timezone, chart legends/axes/units/tooltips and accessible table equivalent | Synthetic, forecast, measured, stale, unavailable; expose whole-horizon rebound and peak differences |
| 4. Cost, constraints and evidence | Tariff period, contract applicability, demand/Pu policy, import/export claim eligibility, MOP values, constraint reasons | Calculated, scenario only, partial, blocked, not calculated, infeasible; distinguish evidence unknown from known infeasibility |
| 5. SHADOW review | Recommendation summary, assumption and evidence links, reviewed / request evidence / dismiss actions | Review is a human disposition only; no approval or command wording; preserve no-control boundary |
| 6. Monitoring and replay | Observed vs predicted outcome, original input snapshot, model/rule versions, replay lineage, evidence export | Pending measurement, measured, replay complete, incomplete, unavailable, changed input; never silently substitute current data |

The shared application frame is also in scope: site and organization context, navigation, language selector, breadcrumbs, forms, dialog names, help, validation, keyboard instructions, table summaries, notifications, loading/empty/error/disabled states, confirmation copy, export names and screen-reader announcements.

## 4. Controlled terminology for bilingual/domain review

The table gives **draft translation candidates**, not approved Macau energy terminology. Validate them with a Macau Chinese/Portuguese reviewer and representative energy users. Preserve the English term in parentheses only where a pilot user study shows it reduces ambiguity; do not make mixed-language UI the default.

| Concept | 繁體中文 draft | Português draft | English |
|---|---|---|---|
| Grid import | 電網購電 | Importação da rede | Grid import |
| On-site PV | 現場光伏 | Fotovoltaico no local | On-site solar PV |
| Storage charge / discharge | 儲能充電／放電 | Carregamento / descarregamento do armazenamento | Storage charge / discharge |
| Flexible load | 可調負荷 | Carga flexível | Flexible load |
| Baseline | 基線 | Referência de base | Baseline |
| Candidate schedule | 候選時序方案 | Plano horário candidato | Candidate schedule |
| Missing-evidence result | 因證據不足而未計算 | Não calculado por falta de evidência | Not calculated: evidence missing |
| SHADOW mode | Shadow 模式（只作建議） | Modo Shadow (apenas recomendação) | Shadow mode (advisory only) |
| No device command | 不會下發設備控制指令 | Não são enviados comandos aos equipamentos | No device commands are sent |
| Measured outcome | 實測結果 | Resultado medido | Measured outcome |
| Modeled estimate | 模型估算 | Estimativa do modelo | Model estimate |

Do not localize canonical status codes, JSON keys, contract IDs, device IDs, evidence IDs or protocol values. Display localized human-readable labels while preserving stable identifiers for APIs, exports and replay.

## 5. Macau number, money, time and measurement rules

- Use locale-aware number/date/time rendering; formatting must not alter stored numeric values, energy balance, tariff calculation, rounding order or replay identity.
- Display the currency code **MOP** wherever money could be confused with another dollar currency. Use locale-aware placement and separators; do not hard-code a naked `$` or parse formatted text as a canonical amount.
- Keep `kW` and `kWh` explicit. Translate accessible unit descriptions while preserving SI symbols; show whether a value is average power, interval energy, import, export, charge or discharge.
- Persist source instants and site-time semantics according to the approved event-time policy; display schedule intervals in `Asia/Macau` with an explicit timezone context. A locale switch cannot change the underlying intervals.
- Proposed interface default is a 24-hour schedule clock because the dispatch task compares time intervals; validate this choice with target users. Test midnight crossings, daylight/timezone labels, month/year boundaries, decimal/group separators, negative values, zero, large demand values, and long Portuguese text.
- Keep source precision and underlying values available to accessible names/table alternatives. Do not round a chart label so it disagrees with the detailed table or evidence export.

## 6. Acceptance and review evidence before calling a locale supported

For every locale that the owner selects for pilot, record evidence for all of the following:

1. All six workflow stages and shared frame have complete reviewed strings, including empty/loading/stale/blocked/partial/error/replay states, dialogs, tooltips, accessible names, and help.
2. The same synthetic fixture and result are shown in each locale; only presentation changes. No missing-key or fallback mixture appears in a critical path.
3. A language switch during stages 1–6 preserves task context and does not change numeric values, scenario identity, review semantics or source-language evidence.
4. MOP, `kW`, `kWh`, numbers, dates and Asia/Macau time are checked for representative regular, boundary and long-value cases.
5. The complete task is rendered at 320, 375, 768, 1024 and 1440 CSS px with long translated labels, tables, chart alternatives, warnings and controls. Record page/region overflow, clipping, truncation and fixes per locale.
6. Keyboard users can change language, reach every control and retain visible focus. Screen-reader language, reading order, chart/table equivalence and status announcements are checked; no color-only status exists.
7. A qualified reviewer signs off Chinese, Portuguese and English domain terminology; WP-4 sessions test comprehension with target roles. Translation completeness is not user validation.

A prototype with a few translated navigation labels, a selector without translated content, or locale formatting alone is **not** multilingual support.

## 7. Current state and open decision

- PR #8 contains a stack-neutral i18n architecture proposal with language candidates, evidence/source-language rules, locale-neutral contracts, MOP/timezone formatting constraints and WP-4 probes. Its first-release locale set remains explicitly unselected.
- PR #10 v1.7 renders only Traditional Chinese and has no locale selector or complete translation catalogs. Its mobile responsiveness checks do not test multilingual reflow.
- This document recommends complete `zh-Hant`, `pt`, `en` critical-flow capability for a Macau pilot, subject to owner decision and user research. It does not claim a legal requirement or approved launch scope.
- Before product freeze, decide: (A) require all three locales for pilot, (B) select one/two initial locales but enforce translation-ready architecture, or (C) defer non-selected locales to a defined later release. Evidence and scope trade-offs are recorded above; implementation planning can continue with the locale-neutral content and acceptance rules.

## 8. Related design artifacts

- PR #8: [Localization and Internationalization Design v0.1](https://github.com/lilinling12/macau-commercial-energy-os/blob/docs/product-architecture-roadmap/docs/03-architecture/detailed-design/LOCALIZATION-AND-I18N-DESIGN-v0.1.md).
- PR #8: [Product Requirements Draft v0.1](https://github.com/lilinling12/macau-commercial-energy-os/blob/docs/product-architecture-roadmap/docs/02-product/PRD-v0.1.md).
- PR #10: [Source/load dispatch workflow v1.7](https://github.com/lilinling12/macau-commercial-energy-os/blob/product/source-load-economic-dispatch/docs/02-product/prototype/source-load-dispatch/v1.7/index.html).


## v2.3 exact-source locale inventory — 2026-10-05

The [v2.3 locale inventory](prototype/source-load-dispatch/v2.3/LOCALE-COVERAGE.md) was generated from exact branch blob `6f199ddaee1f2a416b9925ce310a073b0455b054` using a v2.3-adapted version of the source-pinned extractor. It found 520 static text nodes, 445 unique text values, 27 non-empty text attributes, 94 dynamic Chinese string candidates, and 489 contextual catalog units. v2.3 remains `zh-Hant` only; Portuguese and English have zero translated v2.3 units. English status enums are technical codes, not evidence of English UI coverage. This does not approve a locale set or claim runtime multilingual support.


## 9. Reconciliation of the v1.9 full-flow and v2.3 claim-state localization studies — 2026-10-07

The two prototype lines answer different questions and must not be combined into a claim of complete product localization:

- **v1.9 six-stage flow:** source HTML blob b2ebcaf4cfd59d0825fb105ed0d320808776b902; its v0.4 draft catalog contains 346 contextual units in each of English and Portuguese, with zero catalog validation errors. The paired browser study records 90 geometry/render samples (3 candidate locales × 6 stages × 5 viewport sizes), 0 measured page or active-stage overflow, 0 page errors, 13 contained horizontal-scroll regions and 18 sampled screenshots. At widths up to 900 CSS px, plot annotations are hidden while axes, series, legend and data alternatives remain. The report explicitly labels the translations AI-assisted and unapproved.
- **v2.3 claim-state page:** the existing inventory remains tied to v2.3 source blob 6f199ddaee1f2a416b9925ce310a073b0455b054: 489 contextual source units, zh-Hant only, and zero Portuguese/English translations for that version. English status codes are not translated UI. Do not transfer v1.9's catalog counts or rendered matrix to v2.3.
- **v2.9 result-projection page:** a separate review records 15 viewport/locale renders and page-width containment for one synthetic result panel. Its candidate-language content on that page is not proof of a shared runtime localization system, translated full workflow, persistence, or approved Macau Portuguese.

### Evidence interpretation

The v1.9 study materially improves evidence over the earlier 337-unit catalog by adding nine contextual SVG chart-text units after screenshots exposed untranslated annotations. Its 346/346 English and Portuguese counts establish catalog coverage for that pinned six-stage source only. The render matrix establishes limited geometry and browser-error observations for that generated preview. It does not establish translation accuracy, operator comprehension, complete dynamic/error-state coverage, language-switch behavior, date/number formatting, screen-reader language or WCAG conformance.

The updated evidence therefore supports this status:

| Scope | Evidence-backed status |
|---|---|
| v1.9 static six-stage source catalog | en/pt draft catalog coverage recorded as 346/346 each; human/domain review pending |
| v1.9 generated preview | 90-case render/geometry smoke evidence recorded; selector, persistence, formatting, assistive technology and user validation not established |
| v2.3 claim-state prototype | zh-Hant source only according to its pinned inventory; no en/pt translations for that version |
| v2.9 result-projection prototype | one-page three-locale rendering evidence only; not end-to-end localization |
| Product launch locale policy | unresolved; zh-Hant, Portuguese variant and en remain owner/product decisions |
| Production application localization | not demonstrated by these static prototypes |

### Source records

- prototype/source-load-dispatch/v1.9/localization/LOCALIZATION-COVERAGE-REPORT-v0.4.md, blob 65466ed26e3a81f00ba7730848ef8cc391cc60fc.
- prototype/source-load-dispatch/v1.9/localization-study-v0.3/REVIEW.md, blob 09be29f9dc3a5d7062290d5b1c15d45b9c40ee55.
- prototype/source-load-dispatch/v2.3/LOCALE-COVERAGE.md, blob b11a75524c5867b36a726db0997f9899d4273a4d (verify against current branch before reusing this fingerprint).
- prototype/source-load-dispatch/v2.9/REVIEW.md, blob 3d5b545485a532b4784582f2fff1c4d7d48b9894.

### Next localization work

Keep the existing locale-neutral requirements and test plan. Before calling any locale supported, choose the pilot locale set and Portuguese variant; commission qualified terminology review; connect reviewed resources to the actual product runtime; exercise locale switching with state preservation and Macau number/time formatting; and review all dynamic states with keyboard and assistive technology. Repeat responsive review on the integrated workflow, including chart alternatives and long translated content. Until then, describe these artifacts as separate localization studies, not product multilingual support.
