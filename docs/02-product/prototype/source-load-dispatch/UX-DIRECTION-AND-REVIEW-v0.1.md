# Macau Commercial Energy OS — UI/UX Direction & Review v0.1

**Date:** 2026-10-04  
**Status:** Evidence-based design direction and static prototype review. Not an owner-approved visual system, localization sign-off, WCAG conformance claim, or user validation.  
**Reviewed surface:** standalone source/load dispatch prototype v0.3; project UI/UX skill draft; `ui-ux-pro-max` skill guidance; repository product decisions D-001..D-010 and D-055/D-077 as recorded in the current-state trace.

## 1. User, task and product context

The reviewed screen is for an energy/facilities operator comparing source and flexible-load schedules for a commercial site. Its central task is to understand a common-horizon baseline and candidate, identify the constraints and evidence behind them, and decide what to review. It is a sustained B2B operations workspace, not a marketing homepage and not a control-room command console.

Repository decisions constrain the design: total economic cost/value is the product objective (D-002); HVAC/chiller is first-priority asset hypothesis (D-003); ESS is optional and site-economics dependent (D-004); PV treatment comes from verified settlement terms (D-005); Demand Guard can veto (D-006); recommendations are advisory with strict LLM/cloud control boundaries (D-007/008); R0 economic truth is limited under D-055; and D-077/U-025 keep PV feed-in/cross-site rights evidence-bound. The prototype remains synthetic and non-controlling.

## 2. Design intelligence search and fit

`ui-ux-pro-max` design-system search was run for this product. The first result (“Trust & Authority + Conversion”, organic biophilic, conversion CTA) was a poor fit: it is a marketing/conversion pattern. Following the skill's retry guidance, a narrower operations query returned “Real-Time / Operations Landing” and “Minimalism & Swiss Style”, with a dark/neutral, scannable data presentation. That result is closer in audience but still names a landing-page pattern, so it is used only for broad qualities (clear status, readable operational data, reduced-motion behavior), not as a literal page structure or palette.

The project-specific skill correctly keeps energy semantics and product authority ahead of generic visual trends. Together, the skills support a custom analytical canvas, direct labels, accessible status, responsive density and purposeful motion. Neither search result was treated as an approved visual system. The generator's typography recommendation included a display/editorial pairing that is not appropriate to adopt without separate multilingual readability evaluation; this review does not adopt it.

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
| Good | Screen gives baseline and candidate on a shared horizon, direct units, a table alternative, a synthetic-data notice, tariff-unverified state, and no-device-control boundary. | Preserved. It currently displays no bill cost, export credit, cross-site allocation or saving claim. |

Changes are limited to local output prototype v0.3. They do not alter the repository's v0.11 prototype or claim product approval.

## 5. Current review coverage and remaining gaps

The source was statically inspected for semantic labels, synthetic/demo boundary, responsive breakpoint declarations (1050/760/390 px), reduced-motion behavior declarations, table alternative and interaction copy. Scenario selection uses keyboard-capable native controls in the source, but switching, focus order, focus return and dialog behavior were not exercised in this review; the prototype review records those interaction checks as outstanding.

The v0.3 HTML was opened in a browser and its accessibility tree was inspected at the browser's current default viewport. This confirms the rendered content and semantic labels at that viewport, but does not provide a pixel-level visual review. There is no recorded verification at 1440, 1024, 768 or 375 px, no measured contrast audit, no screen-reader walkthrough, no zoom/reflow check, and no browser/device compatibility evidence. Traditional Chinese is the only locale present in this prototype; Portuguese and English are not implemented. Locale requirements remain unconfirmed, and no user research was run. The screen is not ready for usability or accessibility sign-off.

### Next review actions

1. Render the updated artifact at 1440, 1024, 768 and 375 px, inspect long labels and chart/table behavior, and record issues before changing visual direction.
2. Measure foreground, status, focus and chart contrast; verify keyboard focus and dialog focus entry/return with assistive technology.
3. Add Portuguese and English only after owner/user locale scope is confirmed; then test reflow and Macau terminology across all required locales.
4. Compare two compositions of the same task (schedule-first canvas vs contextual evidence-first layout) using the same fixture; decide with task observation, not palette preference alone.
5. Obtain domain review of the synthetic balance and D-055 economics boundary before expanding any result metric.

## 6. Owner decisions still open

- Approve the first user/site workflow and required locales.
- Choose between the studied composition alternatives and confirm a brand direction/palette.
- Confirm whether the web operator workspace is desktop-first with responsive mobile review, or whether mobile operations is also a primary task.
- Approve visual design tokens only after rendered comparison and accessibility review.

Until then, this is a documented proposal and quality checkpoint, not a frozen design system.
