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

The current prototype v0.10 is a synthetic workflow study, not a final visual system. Its bounded viewport observations do not establish accessibility conformance, localization readiness, or user preference.

## Source links

- Material Design 3, Foundations: <https://m3.material.io/foundations/>
- IBM Design Language, Data visualization basics: <https://www.ibm.com/design/language/data-visualization/design/basics/>
- W3C, Web Content Accessibility Guidelines (WCAG): <https://www.w3.org/WAI/standards-guidelines/wcag/>
- W3C, WCAG 2.2 contrast minimum: <https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html>
