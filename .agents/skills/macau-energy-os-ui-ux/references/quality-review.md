# UI Quality Review and Iteration

Use this review at concept, prototype, and implementation stages. A checklist pass is evidence of review, not proof of usability or production accessibility.

## 1. Composition and craft

- Does the first viewport establish site/context, operational state, and the next useful decision?
- Is there one clear hierarchy with intentional typography, alignment, rhythm, and negative space?
- Does each element earn its space? Reduce repeated cards, generic KPI strips, pills, gradients, glass layers, decorative chart junk, and redundant labels unless they serve a task.
- Are color, shape, type, iconography, and imagery coherent and recognizable as this product rather than a copied template?
- Does the design remain polished with real labels, long text, errors, empty states, and dense data?

## 2. Energy semantics and trust

- Are measured, predicted, estimated, scenario, synthetic, stale, and incomplete states distinguishable in both text and visuals?
- Are source, time window, units, freshness, uncertainty and relevant constraints visible where users interpret the result?
- Do energy flows balance only where verified? Are unsupported export, savings, control, or tariff assumptions blocked or marked unknown?
- Can users trace a recommendation back to its evidence and understand its review/execution state?

## 3. Layout and responsive behavior

Review at representative desktop (1440px), laptop (1024px), tablet (768px), and mobile (375px) widths, plus zoom/text enlargement where available.

- Does hierarchy adapt instead of merely shrinking columns?
- Do charts gain a compact or tabular alternative when labels/legends would become unusable?
- Can users reach filters, site context, evidence, and key actions without horizontal scrolling or hidden hover-only controls?
- Do Traditional Chinese, Portuguese, and English text lengths reflow without overlap, clipping, or ambiguous truncation?

## 4. Accessibility and interaction

Use WCAG 2.2 AA as a minimum target, and check the interaction against platform guidance where applicable.

- Text contrast meets applicable thresholds; non-text controls and focus indicators are visible.
- Status and chart meaning do not depend on color alone.
- All actions work with keyboard; focus order, names, roles, selected/disabled states, and error feedback are understandable.
- Targets and spacing are usable on touch; fields have persistent labels and clear validation/recovery.
- Motion is meaningful, brief, interruptible, and respects `prefers-reduced-motion`.

## 5. Visual benchmark and originality

Treat Apple HIG and Google Material as sources for interaction, accessibility, adaptive layout, tokens, state and motion principles. Treat Awwwards/Webby/FWA winners as references for originality, narrative, composition, craft and interaction quality. Do not inherit a platform system wholesale or copy an award site's look. Award recognition is an aspiration, not a measurable guarantee; for an operational console, trust, task success, clarity and sustained usability remain equal requirements.

Useful primary references:

- Apple Human Interface Guidelines — [Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Motion](https://developer.apple.com/design/human-interface-guidelines/motion), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- Google — [Material 3 foundations](https://m3.material.io/foundations/), [Material 3](https://m3.material.io/).
- W3C — [WCAG 2.2](https://www.w3.org/TR/WCAG22/).
- Webby — [2026/2027 judging criteria](https://www.webbyawards.com/judging-criteria/) and [Best User Interface](https://winners.webbyawards.com/winners/websites-and-mobile-sites/features-design/best-user-interface).
- Awwwards — [Site of the Day example and scoring dimensions](https://www.awwwards.com/sites/designed-by-women) (Design, Usability, Creativity, Content; developer criteria include responsive design/accessibility/performance).
- FWA — [25th-anniversary overview](https://thefwa.com/FWA25/25.html) describing its focus on digital innovation, creativity, originality, and technical excellence.

## 6. Iteration and sign-off

Record findings by severity:

- **Blocker:** misleading energy/cost meaning, unsafe implied action, inaccessible essential path, or broken task completion.
- **High:** major hierarchy, evidence, responsive, keyboard, localization, or interaction failure.
- **Polish:** non-blocking refinement to type, spacing, animation, transitions, or visual consistency.

Fix Blockers and High findings before calling a screen ready. Iterate visual details until no obvious material improvement remains for the defined task and constraints. Do not keep polishing subjective micro-details after gains become marginal; record trade-offs and ask the product owner to approve unresolved product decisions.

For handoff, record the viewport/state reviewed, contrast/accessibility checks performed, language/sample strings used, interaction path, issues fixed, and remaining risks. Do not claim user validation unless actual representative users tested the design.

