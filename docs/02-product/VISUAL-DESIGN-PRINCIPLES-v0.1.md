# Visual Design Principles and Evaluation Plan v0.1

**Status:** Owner design constraint and research plan; no visual direction, palette, typography, theme, or component system is approved.  
**Prepared:** 2026-10-04  
**Applies to:** Product discovery, interaction prototypes, visual exploration, and eventual production UI.

## Purpose

The product should feel contemporary and carefully designed without copying a particular large platform or mistaking novelty for usability. Mature design systems are reference material for principles and evidence, not templates to reproduce. Visual choices must support Macau commercial-energy work: long sessions, dense readings, comparisons, alerts, uncertain data, evidence trails, and multilingual labels.

## Owner-stated quality bar

- Reference mature internet-product practice, current design research, and established accessibility standards.
- Avoid freezing the product into familiar but dated navigation, page, table, card, or dashboard patterns. Reconsider each pattern against the user's task; do not use novelty for its own sake.
- Develop a modern, intentional palette and typography system. “Modern” does not imply dark mode, neon accents, glassmorphism, gradients, or fashionable decoration.
- Prioritize legibility, information hierarchy, efficient scanning, trust, and calm sustained use. The interface should make data quality, evidence, uncertainty, and action state easy to tell apart.
- Use color consistently through semantic design tokens. Status and chart meaning must not depend on color alone; check contrast in every supported theme.
- Keep density adjustable to role and task where evidence supports it; preserve readable type and spacing on small screens and for long labels.
- Prefer purposeful motion and clear interaction feedback. Respect reduced-motion settings and provide visible keyboard focus.
- Avoid copying the visual identity or information architecture of Google, Apple, IBM, or another product. Compare their documented principles, then validate a distinct solution for this product and its users.

## Reference methods

Use the following as complementary evidence, not as a prescribed look:

1. **UI/UX Pro Max skill:** Run product-specific design-system and targeted UX/chart searches. Record query, result, and fit critique. Search output is a candidate heuristic; the skill's result must not override user evidence or accessibility review.
2. **Material Design 3 foundations:** Use its published framing around accessibility, content and information design, reusable design tokens, interaction states, and layout as a reference for design-system completeness. Do not copy Material's visual language by default. <https://m3.material.io/foundations/>
3. **IBM Design Language data visualization:** Use its guidance to make chart encodings and legends interpretable, and to consider accessibility and cultural context. Do not assume an IBM chart style is the right product style. <https://www.ibm.com/design/language/data-visualization/design/basics/>
4. **W3C WCAG 2.2:** Treat conformance criteria as a floor for accessibility; verify text contrast and non-text contrast, keyboard access, focus visibility, reflow, and other applicable criteria in rendered states. <https://www.w3.org/WAI/standards-guidelines/wcag/>
5. **Target-user evidence:** Observe actual tasks and terminology with Macau facilities/energy, finance, and site-operations users. Test translated layouts and domain wording with people who use each supported language.

## UI/UX Pro Max evidence and fit review

The installed skill has been used in the research/design review. The repository packet records the earlier enterprise-energy design-system, operational-dashboard UX, and time-series-chart queries. A further design-system query on 2026-10-04 ("enterprise energy operations dashboard modern calm high density") returned a dark/neutral operations pattern, a glassmorphism style, Fira Code/Fira Sans, and a green accent palette. A targeted UX query surfaced readable mobile text, contrast, heading hierarchy, accessible naming, and contextual status feedback.

These results are not a design decision. The dark/glass recommendation may be a poor fit for dense, long-duration analysis or multilingual data labels; verify it against a light-first and neutral alternative instead of adopting it. No stack-specific search is appropriate until the frontend stack is selected. A palette/font/style should not be persisted as the product design system until the owner reviews rendered alternatives and evidence.

## Evaluation before visual approval

For an initial source-level comparison, see [Visual Direction Study v0.1](prototype/visual-directions/v0.1/index.html). The local browser preview confirmed the content and stacked narrow-screen composition. Explicit 320px/1440px captures were clipped/scaled in the in-app browser, so exact overflow and full desktop readability remain unverified; it is not target-user or accessibility validation. Continue to rendered alternatives using identical workflow and data. Review:

- Light and dark surfaces (when both solve a demonstrated need), color roles, type scale, density, chart palette, borders, focus, and status states.
- Actual, forecast, estimated, missing, stale, blocked, and verified states, including print/export and chart/table alternatives.
- Contrast for text and interactive/data marks, grayscale/color-vision robustness, keyboard focus, reduced motion, 200% zoom, narrow reflow, and long Traditional Chinese, Portuguese, and English strings.
- Long-session readability and task completion with target users. Separate preference reactions from observed comprehension, error recovery, and task performance.
- All choices as versioned design tokens, with the reasons, trade-offs, unresolved risks, and explicit owner decision recorded.

## Prototype v0.11 source-level interaction review

The current prototype v0.11 remains a synthetic workflow study, not a final visual system. A targeted UI/UX Pro Max review searched the UX guidance for disabled-state clarity and action feedback, then inspected the actual prototype source and a fresh browser accessibility tree.

- **Finding:** v0.10 changed recommendation-card state in the page DOM and disabled the card's follow-up controls, but its confirmation said “saved locally”. Source inspection found no browser storage, persistence API or server request for these annotations. That wording could imply a durable record.
- **Change:** v0.11 preserves v0.10 and clarifies that the reviewed/dismissed/needs-data demo state appears only on this page, resets on reload, and is not persisted, executed or a measured outcome. The WP-4 protocol now points new task sessions to v0.11.
- **Positive source signals:** action buttons have a 44px minimum height; disabled controls reduce emphasis and use a not-allowed cursor; the review message is in a polite live region; status badges carry text as well as semantic color. These are source observations, not conformance findings.
- **Browser observation:** a fresh tab opened the Recommendations view with both synthetic items unreviewed and their demo controls available. The already-open tab showed a post-action “Reviewed (demo)” state with those controls disabled. The page's source initializes items as unreviewed and contains no persistence path; a reload-reset behavior is inferred from that source and was not separately tested by refreshing.
- **Limits:** no full keyboard path, screen-reader session, contrast calculation, language review, user session or WCAG-conformance test was performed for v0.11. The page remains English-only, synthetic and unapproved. The existing Harbor Teal, Mineral Blue and Night Graphite options remain alternatives; no palette, typography or design system is selected.

## UI/UX Pro Max targeted visual follow-up — 2026-10-04

A fresh Pro Max run used the product-specific design-system query `commercial energy analytics workspace dense data evidence` (balanced-modern variance, subtle motion, dense-dashboard setting), followed by targeted style, color and chart searches.

- **Pattern fit:** the aggregate search returned **Enterprise Gateway**, a public marketing/site-selection pattern; this is not appropriate evidence for the signed-in product workspace. Its separate **Data-Dense Dashboard** style is relevant as an information-density reference for analytics, but its compact 12–14px suggestion is not a default body-text rule. Density must be balanced with sustained reading and long localized labels.
- **Palette fit:** targeted color results returned generic **Analytics Dashboard** blue/amber and **Sustainable Energy / Climate Tech** green palettes. They are comparison inputs only, not Macau brand or product decisions. Blue/amber must be checked against chart/status semantics; green must not imply positive performance or savings when it is only a brand accent. Each foreground/background and non-text pair requires contrast evaluation in rendered states.
- **Chart fit:** the time-series result supports solid actual versus dashed forecast, a named uncertainty range, and a visible table/summary alternative. These align with current product principles; they do not choose a chart library or color values.
- **Decision boundary:** no palette, theme, font, frontend framework or component system is selected. No stack-specific search was run because the production UI stack remains unapproved. The existing Harbor Teal, Mineral Blue and Night Graphite study remains a set of hypotheses to compare on the same task, with target-user and accessibility evidence still required.

## Source links

- Material Design 3, Foundations: <https://m3.material.io/foundations/>
- IBM Design Language, Data visualization basics: <https://www.ibm.com/design/language/data-visualization/design/basics/>
- W3C, Web Content Accessibility Guidelines (WCAG): <https://www.w3.org/WAI/standards-guidelines/wcag/>
- W3C, WCAG 2.2 contrast minimum: <https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html>


## Direct source and skill review — v0.10, palette study, 2026-10-05

### Evidence read

- Project skill [`.agents/skills/macau-energy-os-ui-ux/SKILL.md`](../../.agents/skills/macau-energy-os-ui-ux/SKILL.md), blob `133aa421796ad314a1e4678f3d3a65051f532178`, and its energy-operations, quality-review, and visual-reference case-study references were read directly from PR #8.
- v0.10 source, blob `5d148b4990e353c7a400b7401216066f35ed68cf`, begins on **Portfolio overview**: a four-metric row (sites, point coverage, economic-result status, recommendations) followed by site readiness, evidence items and a synthetic trend. It does carry strong truth boundaries: synthetic data, incomplete evidence, no bill-grade claim, no remote-PV credit, SHADOW-only recommendations and no command path. Economics, tariff/contract evidence and a site/source model are secondary destinations; the opening hierarchy does not make the source/load economic dispatch the primary task.
- The navigation exposes nine destinations on desktop and a single select on narrow screens. This is source inspection, not a current browser, keyboard, screen-reader or reflow result.
- Visual-direction study v0.1, blob `986f7f6bd1f7c01506ac6cc41a3b3430d9d8309c`, compares Harbor Teal, Mineral Blue and Night Graphite on the **same synthetic portfolio-overview** task. It provides an actual/forecast line distinction, uncertainty band, labels and a locale label sample. It is a palette stimulus, not a dispatch-task comparison; it does not select a palette, theme, typography or product design system. The sample has one short localized label, so it cannot establish full Traditional Chinese/Portuguese/English layout fit.
- This turn did not render either exact source in a browser. Prior review notes for earlier versions are not re-labeled as current-version rendered checks.

### UI/UX Pro Max run and fit

The required product-specific run used:

`commercial energy operations dispatch evidence dense data`  
`--design-system --variance 7 --motion 3 --density 7`

The aggregate result routed to **Trust & Authority + Conversion** and **Organic Biophilic**, with a generic green sustainability palette, Fira type and marketing conversion elements. That is an explicit poor fit for a persistent commercial-energy operator console: conversion sections, logo carousel and nature/organic styling do not solve the dispatch review task. **None of this generated palette, typography or pattern is adopted or persisted.**

Two narrow searches returned relevant, product-fit guidance:

- UX query `contextual status evidence claim explanation` returned the rule to announce one meaningful contextual status through a single appropriate atomic live region without moving focus. This fits mixed readiness/claim feedback when it is implemented and checked in the actual interface.
- Chart query `time series actual forecast uncertainty accessible table` returned direct labels, solid actual vs dashed forecast, a named uncertainty range, plus a visible data-table and concise-summary alternative. Those are useful conventions, not a library, color, or final chart design decision.

### Directional conclusion

The current sources establish a **product-hierarchy gap**, not a palette defect: v0.10 and the palette study explain readiness/evidence, but they place portfolio scan ahead of dispatch. Continue the approved-by-user *directional intent*—dispatch first, portfolio/readiness as supporting context—while keeping the product baseline and visual system pending owner review. Compare new visual options on the same dispatch decision task and same evidence states, including blocked/partial/economic-unavailable and SHADOW review. Preserve provenance, time range, units and uncertainty at the decision point; do not fill missing physical or settlement links for a more complete-looking graphic.

**Coverage not established:** exact-source rendering, complete responsive interaction, full keyboard and assistive-technology review, 200% zoom, full-page contrast, complete locale strings/formatting, target-user comprehension or WCAG 2.2 AA conformance. The project quality-review checklist remains the acceptance method for those later checks.
