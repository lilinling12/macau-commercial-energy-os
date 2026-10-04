# Localization and Internationalization Design v0.1

**Status:** Stack-neutral design proposal; user languages, launch locale set, fallbacks and translation ownership are unresolved. No locale or production architecture is approved.  
**Prepared:** 2026-10-04  
**Authority:** Product/architecture review drafts, WP-4 discovery protocol, Macau government-language context, and current D-001..D-077/U-001..U-026 authority.

## 1. Macau context and evidence boundary

The Macao Government Tourism Office states that Chinese and Portuguese are the official languages, Cantonese is most widely spoken, and English is generally used in trade, tourism and commerce ([official language overview](https://www.macaotourism.gov.mo/en/article/about-macao/language)). This supports investigating Traditional Chinese, Portuguese and English with target users. It does **not** prove that every commercial-energy buyer/operator needs all three UI locales, or establish terminology preference for a specific role, site or customer.

Treat spoken language, written script, UI locale, customer terminology, and source-document language as separate research fields. Cantonese is not a written UI locale. Traditional Chinese is a product hypothesis to validate, not an assumed implementation decision. Portuguese regional terminology and English technical vocabulary also require review by users.

## 2. Product proposal for review

**Design constraint:** prepare the product for localization from the first implementation increment so that adding a validated language does not require rewriting screens, domain calculations, or data contracts.

**Locale candidates for discovery:** Traditional Chinese (candidate tag `zh-Hant`), Portuguese (use generic `pt` until a regional preference is confirmed), and English (`en`). No initial or required release subset is selected. Validate which language each role uses for operations, finance, procurement, integrations, reports, and support; allow role/site differences rather than assuming one language for all Macau businesses.

**Owner decision:** approve the language-readiness constraint, then choose the first-release locale set after WP-4 evidence. A person may defer language breadth while preserving the architectural readiness requirement.

## 3. User experience and content rules

- User-facing interface messages, validation, chart labels, help, navigation and empty/error/recovery states must be externalizable into locale-specific catalogs; do not concatenate sentence fragments or embed visible copy in business logic.
- Evaluate locale-aware dates, times, numbers, percentages and MOP currency while retaining the calculation's source precision, timezone, unit and effective period. Formatting must not change money rounding, tariff semantics, energy values, event identity or replay digests.
- Keep technical units such as kW/kWh explicit and stable. Localized digit/decimal rendering may vary, but data entry and conversion rules must be validated and normalized at the boundary.
- Preserve original customer bills, tariffs, contracts, meter/BMS labels and source records. Display the source language and any reviewed translation's status/provenance. Never silently machine-translate source evidence or imply a translation is legally authoritative.
- Use long Traditional Chinese, Portuguese and English labels to test wrapping, menus, tables, forms, charts, alerts, notifications, exports and responsive behavior. Do not shrink essential text to fit a fixed layout.
- Mark language changes in the accessibility tree for screen readers; maintain correct reading order, accessible names, keyboard operation and visible focus across language changes.
- Decide after discovery whether users need one UI locale at a time, parallel bilingual labels, translated exports, or role-specific language preferences. Do not assume each product screen should display three languages simultaneously.

## 4. Technology-neutral architecture constraints

1. Keep canonical domain values and contracts locale-neutral: typed numeric values, canonical timestamps/offset policy, explicit units, stable status codes, immutable source values and language-neutral identifiers. Localize only presentation unless the domain explicitly models linguistic content.
2. Externalize human-authored product copy and define a message-catalog workflow with locale tags, plural/context support, completeness checks and review ownership. Select the framework/library only after stack approval.
3. Keep user preference, tenant/site default and source-content language distinct. Define precedence, fallback, profile storage and export behavior in a future approved ADR; do not bake a product-wide language choice into domain tables or protocol enums.
4. Store/report timestamps according to the approved event-time policy; render using explicit user/site timezone context (Macau `Asia/Macau` is a candidate display default, not a replacement for source offsets or UTC instants).
5. Format currency and quantity at the UI/export boundary using the selected locale. Monetary calculations continue to follow approved decimal precision, tariff rounding and settlement rules; never parse localized display strings as the canonical amount.
6. Keep evidence language/provenance attached to source documents and translations. Translation service, data residency, privacy, retention and external AI processing require separate data-governance review and customer authorization.
7. Use BCP 47 language tags at presentation/content boundaries as a candidate standard. The exact schema, fallback catalog and framework implementation remain stack-selection decisions.

## 5. WP-4 research probes

Ask behavior-first questions and record participant's preferred language per task, role and artifact. Validate:

- language used to read bills/contracts/tariffs, operate BMS/site screens, explain cost to finance, and approve a recommendation;
- terms users use for demand, maximum demand, tariff period, freshness/staleness, uncertainty, blocked result, recommendation and actual savings;
- whether a bilingual handoff is needed between site operations, finance, owner, and external integration partner;
- acceptable language for notifications, support, reports, exports, onboarding and administration;
- translation trust: which source must remain authoritative, what status/provenance a translated document needs, and whether local review is required;
- mixed-script search/sorting, names, meter labels and customer-provided text behavior.

Recruit across roles/site contexts before assigning locale priority. Report sample size, participant language, task performance and unresolved terminology; preference alone is not proof that users understand tariff or evidence semantics.

## 6. Verification criteria before approving locale scope

For every selected locale, later implementation evidence should show:

- critical task copy has an approved translation owner and completeness process;
- long labels reflow without clipping or hiding warnings/actions at supported viewport widths and 200% zoom;
- screen-reader language and pronunciation metadata are correct where needed;
- dates, times, MOP, decimal values, percentages and units render correctly without changing the underlying result or replay identity;
- untranslated/unsupported locale fallback is explicit and never fabricates translated legal/customer evidence;
- native UI and exports identify their locale and preserve authoritative source language/provenance.

These are design criteria, not present prototype validation. WCAG 2.2 and UI/UX Pro Max form part of the later rendered evaluation; neither selects the product's language set.

## 7. Decisions deliberately left open

- First-release and pilot locale subset; who owns translations and terminology sign-off.
- Whether Macau Chinese UI should use Traditional Chinese for the validated target users and which Cantonese/domain terms should appear in writing.
- Portuguese regional wording and whether `pt` or a regional BCP 47 tag is appropriate.
- User, organization, site and export language preference precedence.
- Bilingual evidence/export requirements and translation provenance model.
- Framework/i18n library, message-catalog format, automated completeness/visual tests, and font stack.
- Translation vendor/service, any AI use, hosting/transfer, customer-data access and retention; all remain subject to U-027 data-governance review.

## References

- Macao Government Tourism Office, [Language](https://www.macaotourism.gov.mo/en/article/about-macao/language) (accessed 2026-10-04).
- Macao SAR Government Portal, [Laws](https://www.gov.mo/en/laws/) (Chinese/Portuguese source-language authority note and English reference-translation limitation).
- [UI/UX Pro Max skill fit review](../../02-product/VISUAL-DESIGN-PRINCIPLES-v0.1.md).
- [Customer discovery and usability research plan](../../02-product/CUSTOMER-DISCOVERY-AND-USABILITY-RESEARCH-PLAN-v0.1.md).
- [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/).
