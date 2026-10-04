# Macau Commercial Energy OS — UI/UX Direction & Review v0.1

**Date:** 2026-10-04  
**Status:** Evidence-based design direction and static prototype review. Not an owner-approved visual system, localization sign-off, WCAG conformance claim, or user validation.  
**Reviewed surface:** standalone source/load dispatch prototype v0.3; project UI/UX skill draft; `ui-ux-pro-max` skill guidance; repository product decisions D-001..D-010 and D-055/D-077 as recorded in the current-state trace.

## 1. User, task and product context

The reviewed screen is for an energy/facilities operator comparing source and flexible-load schedules for a commercial site. Its central task is to understand a common-horizon baseline and candidate, identify the constraints and evidence behind them, and decide what to review. It is a sustained B2B operations workspace, not a marketing homepage and not a control-room command console.

Repository decisions constrain the design: total economic cost/value is the product objective (D-002); HVAC/chiller is first-priority asset hypothesis (D-003); ESS is optional and site-economics dependent (D-004); PV treatment comes from verified settlement terms (D-005); Demand Guard can veto (D-006); recommendations are advisory with strict LLM/cloud control boundaries (D-007/008); R0 economic truth is limited under D-055; and D-077/U-025 keep PV feed-in/cross-site rights evidence-bound. The prototype remains synthetic and non-controlling.

## 2. UI/UX skill use, search evidence and fit

The project-specific `macau-energy-os-ui-ux` skill draft was read and applied as domain guidance: design around the energy operator's decision, evidence quality, source/load semantics, and SHADOW boundary; compare compositions using the same task; keep locales and responsive behavior explicit. It is a local proposal, not yet an installed or repository-approved project skill.

A fresh, reproducible `ui-ux-pro-max` search was run on 2026-10-04:

| Search | Returned result | Fit and use |
|---|---|---|
| `commercial energy operations dispatch planning modern analytical workspace --design-system` | Hero + Testimonials + CTA, Soft UI Evolution, romantic pink/gold palette and wedding/editorial fonts | Misrouted marketing pattern and typography. Rejected; none of these are adopted. |
| Retry: `energy management software operations console dispatch planning --design-system` | Same marketing/testimonials pattern and off-domain wedding typography | Retry remained unsuitable. This is recorded as a search limitation, not as project design evidence. |
| `energy operations interface analytical chart --domain product` | Sustainable Energy / Climate Tech; primary Organic Biophilic + E-Ink/Paper; alternatives Data-Dense Dashboard and Swiss Modernism; Earth Green + Sky Blue + Solar Yellow | Relevant product category and palette family only. It is a taxonomy suggestion, not an endorsed style or palette. We use it to ensure the visual study includes energy-specific alternatives, while preserving chart and evidence legibility. |
| `professional energy software interface --domain style` | Generic Adobe Spectrum, Minimalism & Swiss Style, and Soft UI Evolution matches | General craft references only; no framework or component system is selected. |
| `accessible energy chart data table keyboard focus --domain ux` | Native button semantics and selected state, visible focus, and unobscured focus guidance | Applied as concrete review criteria for interactive choices and evidence controls. The result identifies the enhanced AAA focus-obscuration rule separately; this review does not misstate it as an AA requirement. |
| `energy management operator color palette trustworthy --domain color` | Fitness/gym, CRM, and inventory palettes | Off-domain results. Rejected rather than used as a color specification. |

The design-system aggregate and the targeted domain searches return mixed-quality results. Therefore, we accept only traceable, task-relevant principles and explicitly reject off-domain templates and palettes. The existing three-theme study (Harbor teal, Mineral blue, Night) remains an unselected project study; it is not represented as a direct output of the searches above.

The project skill draft correctly places verified energy semantics and current product authority above generic trend references. The working design direction remains an original schedule-comparison canvas with contextual evidence and readiness, subject to rendered comparison and owner/user review. Search output does not approve a layout, palette, brand or technology stack.

## 3. Visual direction proposal (not frozen)

### Dispatch operations workspace

- **Composition:** one dominant schedule canvas with a compact, contextual readiness/evidence panel; preserve the comparison task above decorative KPI cards. Allow the right-side evidence region to become a contextual drawer or stacked section on narrow screens.
- **Visual character:** calm, precise, contemporary and recognizably energy-focused. Use a restrained neutral foundation with distinct semantic series colors, not generic “green means good” dashboards or a permanent dark glass aesthetic. The existing off-white canvas/navy structure is a plausible study, not the selected brand palette.
- **Data grammar:** keep grid import, PV, storage charge/discharge, base/flexible load, and baseline/candidate visibly distinct with direct labels, units and textual state. Use line style, shape, labels and tables as well as color. Separate physical energy paths from bill settlement and scenario economics.
- **Typography:** prioritize high legibility for dense numeric comparisons and Chinese/Portuguese/English line wrapping. Use a neutral UI sans family plus a tabular-numeric style for measurement values if font coverage and rendering are verified. Keep brand/editorial display type out of operator data tables.
- **Motion:** short, interruptible feedback for scenario switching, evidence expansion and saved review state. No ambient movement or animated data that suggests live telemetry in synthetic mode. Honor reduced motion.
- **Marketing home:** should tell the product story, establish credibility and invite a demo using verified claims. Do not transplant landing-page hero, awards-site motion or conversion patterns into the persistent operator workspace.

### Reference principles

- Apple HIG emphasizes purposeful, recoverable interactions; layouts that adapt to display context; accessibility from the start; and optional, meaningful motion. Apply these as interaction guidance, not as a visual skin: [Apple Design Principles](https://developer.apple.com/design/human-interface-guidelines/design-principles), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), [Motion](https://developer.apple.com/design/human-interface-guidelines/motion).
- WCAG 2.2 AA is the proposed baseline for web content; for ordinary text, the minimum contrast ratio is 4.5:1 (large text 3:1). Charts also need non-color cues and non-text contrast review. See [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [Understanding Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- Material 3 can inform adaptive layout, state and component behavior; its foundations describe accessibility, content design, layout and interaction states, and its canonical layouts consider compact/medium/expanded breakpoints. Use these as adaptable references rather than applying components wholesale: [Material 3 foundations](https://m3.material.io/foundations/), [canonical layout examples](https://m3.material.io/foundations/layout/canonical-examples/overview).
- Awwwards, Webby and FWA are craft/creativity references, not usability proof for this operational product. Awwwards' public examples score design, usability, creativity and content; the [Peden+Munk scoring example](https://www.awwwards.com/sites/peden-munk) supports checking those dimensions separately. The current [Webby 2026/2027 website criteria](https://www.webbyawards.com/judging-criteria/) cover content, structure/navigation, visual design, functionality, interactivity, innovation and overall experience. FWA is used here as an award-winning work reference, not as a published design rubric; see the [FWA of the Day archive](https://thefwa.com/rss/) for dated examples. Borrow no visual identity or motion treatment. For this dispatch console, task clarity, evidence integrity, access and responsive legibility remain the quality floor; original craft is evaluated only after those are satisfied. No award-level claim is made.

## 4. Static and browser-semantic review findings

| Severity | Finding | Disposition |
|---|---|---|
| High | The synthetic baseline was labeled “forecast demand”, conflating a made-up reference with a modeled forecast. | Changed to “synthetic reference” and explicitly says it is not a forecast. |
| High | The example used a real-looking named site and the current date, which could be mistaken for site/live context despite the demo badge. | Replaced with “example commercial site”, “example date” and an explicit Macau scenario label. |
| High | Source/meter readiness used a positive check while saying it was only illustrative and not connected to the site. | Changed the source/meter state to an unverified warning. |
| Medium | Candidate copy did not make HVAC-first and ESS-optional authority clear. | Candidate now names HVAC load shifting as the focus and states ESS is optional and site controllability is unverified. |
| High | Candidate total load was labeled without a plotted line, and the shifted HVAC demand had no later rebound interval. | v0.3 adds the orange candidate-load line, a 17:00 rebound and a matching grid-import/table example. |
| Medium | The selector and chart said 15-minute data although the plotted marks were hourly. | v0.3 labels this as a one-hour synthetic example and says the CEM billing interval is unverified. |
| High | The hourly averages were drawn as interpolated lines, 18:00 read like another interval point, and three ESS bars did not match the described one-hour discharge. | v0.3 now uses six interval-aligned step series, labels 18:00 as the end boundary, and marks only the 15:00–16:00 20 kW ESS example in a separate annotation lane. A fixture verifier checks that the full six-row table matches the synthetic inputs. |
| Good | Screen gives baseline and candidate on a shared horizon, direct units, a table alternative, a synthetic-data notice, tariff-unverified state, and no-device-control boundary. | Preserved. It currently displays no bill cost, export credit, cross-site allocation or saving claim. |

Changes are limited to local output prototype v0.3. They do not alter the repository's v0.11 prototype or claim product approval.

## 5. Current review coverage and remaining gaps

The source was statically inspected for semantic labels, synthetic/demo boundary, responsive breakpoint declarations (1050/760/390 px), reduced-motion behavior declarations, table alternative and interaction copy. A current source pass found that the scenario choices were implemented as `div[role=button]`; the PR branch prototype has since been changed to native buttons with `aria-pressed`, visible focus styling, and no hand-written key emulation. The table control now exposes `aria-controls`/`aria-expanded`; evidence dialogs identify their trigger and contain source-level Tab/Escape/focus-return handling. The page's reduced-motion mode now also selects non-animated programmatic scrolling. These are source changes only: scenario switching, focus order, dialog focus behavior and table toggle have not been exercised in a browser or with assistive technology.

That browser snapshot predates the current keyboard-semantics source edits. A fresh visual/browser review of the updated file was not possible in this pass: the browser tool rejected the local-file URL under its security policy, and no workaround was attempted. The current source therefore has not been rendered or interacted with in this review. The updated v0.3 HTML was opened in the in-app browser and its accessibility tree inspected at the browser's default viewport. The tree confirms the step-chart description, six one-hour intervals, 18:00 end boundary, unverified tariff and disabled device control; the viewport CSS-pixel size was not captured and this did not provide a pixel-level visual review. A local static fixture checker passed arithmetic and table-alignment assertions, which does not constitute site, optimizer or usability evidence. There is no recorded rendered verification of the current source at 1440, 1024, 768 or 375 px, no measured contrast audit, no screen-reader walkthrough, no zoom/reflow check, and no browser/device compatibility evidence. Traditional Chinese is the only locale present in this prototype; Portuguese and English are not implemented. Locale requirements remain unconfirmed, and no user research was run. The screen is not ready for usability or accessibility sign-off.

### Next review actions

1. Render the updated artifact at 1440, 1024, 768 and 375 px, inspect long labels and chart/table behavior, and record issues before changing visual direction.
2. Measure foreground, status, focus and chart contrast; verify keyboard focus and dialog focus entry/return with assistive technology.
3. Add Portuguese and English only after owner/user locale scope is confirmed; then test reflow and Macau terminology across all required locales.
4. Compare two compositions of the same task (schedule-first canvas vs contextual evidence-first layout) using the same fixture; decide with task observation, not palette preference alone.
5. Obtain domain review of the synthetic balance fixture and D-055 economics boundary before expanding any result metric; separately review actual interval, SOC, loss, comfort and rebound constraints before claiming physical feasibility.

## 6. Owner decisions still open

- Approve the first user/site workflow and required locales.
- Choose between the studied composition alternatives and confirm a brand direction/palette.
- Confirm whether the web operator workspace is desktop-first with responsive mobile review, or whether mobile operations is also a primary task.
- Approve visual design tokens only after rendered comparison and accessibility review.

Until then, this is a documented proposal and quality checkpoint, not a frozen design system.


## 7. Current design-reference check (2026-10-04)

Reviewed the official design/accessibility sources and award materials again while assessing the review criteria:

- Apple HIG [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) was updated on 2026-09-09. It emphasizes visual hierarchy, grouping/progressive disclosure, adaptable layouts and testing across sizes, localizations and text sizes. [Motion](https://developer.apple.com/design/human-interface-guidelines/motion) says custom motion should be purposeful, brief, optional, and cancellable where practical.
- Google [Material 3 Foundations](https://m3.material.io/foundations/) organizes guidance around accessibility, content design, tokens, interaction states and layout. Its [canonical adaptive layouts](https://m3.material.io/foundations/layout/canonical-examples/overview) show feed, list-detail and supporting-pane patterns across compact/medium/expanded breakpoints. These are adaptable references, not templates to adopt wholesale.
- W3C [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and its [focus appearance explanation](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance) provide verifiable keyboard, contrast, focus and reflow requirements. Source attributes alone cannot demonstrate conformance; rendered and keyboard testing is still absent.
- The Webby Awards' [2026/2027 criteria](https://www.webbyawards.com/judging-criteria/) assess content, structure/navigation, visual design, functionality, interactivity, innovation and overall experience; its 2026 [Best User Interface winners page](https://winners.webbyawards.com/winners/websites-and-mobile-sites/features-design/best-user-interface) defines excellence around a seamless end-user experience. These criteria support evaluating the console as an operating tool, not only as a visually striking first screen.
- An [Awwwards Site of the Day example](https://www.awwwards.com/sites/self-aware) displays design/usability/creativity/content scores and separate developer dimensions such as accessibility and responsive design. This is an example of its judging surface, not a universal acceptance rubric for this B2B product.
- The FWA's [25th-anniversary overview](https://thefwa.com/FWA25/25.html) describes its focus on digital innovation, creativity, originality and technical excellence; no detailed, project-applicable scoring rubric was established in this check.

**Application to this product:** the schedule canvas should make the site's current context, source/load comparison, units, claim eligibility, constraints and next review action legible before decorative treatment. Motion can explain a schedule transition or provide concise feedback, but it must not obscure interval data or delay a frequent operator task. Responsive layout must preserve comparison and evidence access; at compact widths it may change the composition or switch to a table rather than shrink a desktop chart. The marketing-site aspiration for expressive storytelling remains separate from the persistent operations console.

At the time of this reference review, the updated v0.3 product-flow prototype had not been rendered at named viewport sizes. A subsequent review of the separate v0.1 layout-direction study is recorded below; it does not retroactively validate v0.3. Measured contrast, screen-reader review, full keyboard coverage, complete localization and user validation remain unperformed. No award-level, WCAG-conformance or user-validation claim is made.

## 2026-10-04 targeted design-system fit and dispatch-flow revision

Applied the project skill and UI/UX Pro Max. The first broad design-system result routed this operator console to a “Trust & Authority + Conversion” marketing pattern with organic/biophilic styling. The one allowed narrower retry routed it to “Real-Time / Operations Landing” with glassmorphism and Fira Code/Fira Sans. Both are rejected as poor fit: they describe a promotional landing/conversion page or default dashboard styling, not this evidence-led, sustained-use energy operations workspace. No palette or type decision is inferred from those outputs.

Targeted UI/UX Pro Max results were useful for native selection semantics, accessible names, visible keyboard focus, logical tab order, skip navigation, and direct chart labels plus a table fallback. The project skill's 44×44 px touch target and responsive review guidance are now reflected in the source. The prototype updates selection by emphasizing, not hiding, baseline/candidate series and provides a page-only review-state interaction with truthful non-persistence copy.

The source review also uncovered and corrected the misleading 430 kW “peak” label. The entire synthetic horizon has a baseline peak of 485 kW and candidate peak of 510 kW at the HVAC rebound interval. This changes the interpretation of the candidate: a 15:00 interval reduction does not prove a lower peak or economic benefit. The view now puts the whole-horizon effect first and keeps cost/settlement claims blocked pending applicable evidence.

For the v0.3 product-flow prototype, verification remains source-level plus the static synthetic fixture check. It has not received a rendered viewport review, measured contrast audit, complete Portuguese/English localization, full keyboard/screen-reader review or operator usability evaluation. Separately, the v0.1 layout-direction study has been rendered at 1440×900, 1024×900, 768×900 and 375×812 CSS pixels in Traditional Chinese, with its A/B/C and page-only SHADOW interactions checked; those results and limits are in `directions/v0.1/REVIEW.md`.

## Cross-prototype task coverage check — PR #8 source review

Fetched the current PR #8 prototype source at:
- v0.10 core workflow: blob SHA 5d148b4990e353c7a400b7401216066f35ed68cf.
- Visual direction study v0.1: blob SHA 986f7f6bd1f7c01506ac6cc41a3b3430d9d8309c.

The v0.10 initial view is Portfolio overview. Its navigation covers Portfolio, Site overview, Data health, Site model, Economics, Tariff & contract evidence, Integrations & site access, Recommendations, and Evidence & replay. Its source truthfully labels synthetic data and advisory/no-control boundaries, but the initial task is evidence/readiness scanning; it does not make source/load economic dispatch the dominant task. The visual direction study applies three palettes to portfolio readiness and demand review. Its Traditional Chinese and Portuguese content is a sample freshness label, not full page localization or validated terminology.

The PR #10 v0.3 dispatch study is therefore a complementary, focused task prototype rather than a replacement for v0.10's broader workflow. It makes grid import, site PV, ESS discharge, HVAC shift/rebound, whole-horizon comparison, tariff evidence and SHADOW review visible together. It remains a single Traditional Chinese synthetic screen and does not provide the full path from contract/data verification through replay/M&V. These are coverage limits to resolve in the integrated PRD and user-flow review.

The broad UI Pro Max patterns returned a marketing/conversion or operations landing page; neither should replace the operator workflow. The palette study remains unselected. At the time of this cross-source review, no rendered UI or user test had been performed. The later v0.1 layout-study rendering is a limited responsive/interactions check, not a user test.


## Macau localization scope and evidence review — 2026-10-04

### What the public evidence supports

- The Macao Government Tourism Office states that Chinese and Portuguese are the official languages, Cantonese is most widely spoken, official languages are used for government documents/communications, and English is generally used in trade, tourism and commerce ([official language guidance](https://www.macaotourism.gov.mo/en/article/about-macao/language)).
- The Macao Government Information Bureau's overview reports 2021 Census language figures: more than 81% speak Cantonese, 2.3% Portuguese, 45% Putonghua and 22.7% English ([Macao Government fact sheet](https://www.gcs.gov.mo/news/factSheet/en)). These are general population figures, not evidence about commercial-building energy operators, their procurement requirements or their preferred interface language.
- These sources establish strong Macao context for Chinese/Portuguese and a credible commercial use case for English. They do not, by themselves, establish that a private commercial energy SaaS must provide a particular number of UI locales. Public-sector, concession, procurement or customer-contract obligations need separate review.

### Product recommendation — proposed, not owner-approved

Design the product for complete **Traditional Chinese, Portuguese and English** locale support. Make these selectable per user, with a tenant/site default only as an onboarding convenience; never let UI language change a calculation, tariff rule, evidence state, stored identifier or unit. Before committing the first pilot's launch languages, validate the actual operator, finance and facilities roles and any CEM/procurement/customer-document requirements. A few translated labels in the existing v0.10 prototype do not count as localization.

Localize the entire critical dispatch task, not only navigation: evidence onboarding, meter/site-model terms, forecasts, baseline/candidate schedules, blocked/partial/infeasible explanations, tariff/settlement claims, SHADOW review, review history, alerts, empty/error/loading states, keyboard/accessibility labels, chart descriptions and any customer-facing export included in scope. Establish a human-reviewed energy/settlement glossary for Macao terminology; do not rely on machine translation for tariff, safety, comfort or financial explanations.

### Locale implementation and acceptance proposal

- Keep source content in locale catalogs with typed keys and a completeness check. Missing critical strings should fail release validation instead of silently mixing languages in the operator workflow; development may expose missing-key markers.
- Format dates, times, decimal/group separators and MOP display using locale-aware presentation. Store instants, quantities, units, evidence and tariff semantics independently of locale; preserve the configured site timezone and do not infer settlement intervals from display format.
- Check CJK and Latin font coverage, line wrapping, table density, chart labels, numeric alignment, focus/error states, and text enlargement separately in each locale. Every chart needs direct labels plus an equivalent accessible description/table.
- Pilot acceptance should show complete reviewed translations for all in-scope states in each selected locale, consistent technical terminology, no clipped/overlapping strings at compact/medium/desktop sizes, correct date/number/currency presentation, keyboard and screen-reader name coverage, and zero missing critical keys. Localization review is separate from WCAG conformance and operator validation.

### Actual prototype coverage at this date

The v0.1 layout-direction study was rendered only in Traditional Chinese at 1440×900, 1024×900, 768×900 and 375×812 CSS pixels; A/B/C switching, the page-only SHADOW state, skip-link focus and first direction-button focus were exercised. No Portuguese or English rendering, translation expansion test or locale-specific terminology review was performed. The v0.3 six-stage product-flow prototype remains unrendered in this review. Therefore multilingual support remains **proposed and unverified**, not implemented.

### Owner questions retained for the product decision review

1. Must the first pilot provide full workflows and exports in all three languages, or can a named pilot cohort validate a staged launch?
2. Which roles need Portuguese and English, and which customer/legal/procurement materials require bilingual or trilingual delivery?
3. Should locale preference be per user only, or should a site default also be configurable for shared control-room workstations?

No language scope is frozen by this review.
