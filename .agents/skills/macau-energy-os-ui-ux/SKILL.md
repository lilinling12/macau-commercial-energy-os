---
name: macau-energy-os-ui-ux
description: Design, prototype, review, and refine user interfaces for Macau Commercial Energy OS. Use for operator workflows, energy sourcing and dispatch, evidence review, dashboards, product visual systems, responsive behavior, and UI quality audits. Combine project-specific energy semantics with current platform guidance; do not apply a fixed legacy EMS or admin-dashboard template.
---

# Macau Energy OS UI/UX

Create a distinctive, trustworthy, contemporary energy operations experience. Design from the operator's decisions and the site's energy behavior, not from a generic dashboard template. Use `ui-ux-pro-max` for searchable design guidance and this skill for project context; neither overrides verified domain rules or owner decisions.

## Product truth

- The central product problem is coordinating **where electricity comes from and when it is used**: grid import, on-site PV, storage charge/discharge, and flexible loads, including HVAC, EV charging, and hot water when applicable.
- Present cost, carbon or energy objectives only with their evidence and constraints. Do not imply PV export, settlement credit, storage economics, controllability, savings, or live status without verified site/contract data.
- Separate measured, forecast, estimated, scenario, and synthetic values in wording and visual encoding. Surface source, period, freshness, uncertainty, and unresolved assumptions at the point of decision.
- Recommendations in MVP are advisory/Shadow. Review is not command approval. Do not design an interaction that implies device execution unless the current approved product scope explicitly includes it.
- Read the active project authority, current prototype, and relevant decision records before changing a settled domain label or workflow. Treat the three palette studies as unselected alternatives until an owner decision exists.

For dispatch-specific screen guidance, read [energy-operations-ux.md](references/energy-operations-ux.md).
For visual review and iteration, use [quality-review.md](references/quality-review.md). It links to sourced [visual reference case studies](references/visual-reference-case-studies.md) with product-specific transfer boundaries.

## Design workflow

1. **Name the user and decision.** Identify role, context, task frequency, risk, device, information needed, and what a correct next action means. Distinguish executive portfolio review from operator/site investigation and engineering commissioning.
2. **Inspect current authority and product surface.** Reuse valid contracts, terminology, user research and interaction behavior. Record unknowns rather than filling gaps with familiar SaaS conventions.
3. **Explore a visual idea before styling components.** For an unresolved direction, compare a small number of meaningfully different concepts using the same real task and information hierarchy. Explain each direction's strengths and trade-offs. Avoid a palette-only exercise when the deeper issue is layout, task flow, or information hierarchy.
4. **Use references as evidence, not templates.** Consult current Apple Human Interface Guidelines, Google Material guidance, W3C WCAG, and selected Awwwards, Webby and FWA work. Extract the principle or craft technique that helps this product; do not copy another site's composition, assets, brand language, or interaction wholesale. Distinguish marketing-site spectacle from a persistent B2B operations console.
5. **Create a coherent responsive system.** Define semantic color and type tokens, spacing, grid, density, chart conventions, component states and motion rules before styling many pages. Allow branded expression without reducing legibility or hiding operational state.
6. **Prototype meaningful states.** Include representative populated, empty, loading, stale, partial, error, uncertain, disabled, reviewed and narrow-screen states as relevant. Make actions, feedback, undo/recovery, and evidence paths inspectable.
7. **Review and refine.** Run the checklist in `references/quality-review.md`. Fix high-impact issues first and repeat visual and interaction review until no material issue remains. Report remaining trade-offs honestly; never claim literal perfection or an award outcome.

### Match searchable guidance to the product surface

Treat `ui-ux-pro-max` matches as hypotheses, not instructions. Search separately for a persistent operator console, a customer/account portal, or a public marketing site; their goals and visual structures differ. For an operator-console query, verify that the returned pattern, use case, conversion focus, typography and palette actually support the named energy-operations task before applying any of them.

If results emphasize landing-page conversion, hero/testimonial/CTA sections, or an aesthetic unrelated to evidence-heavy operations, do not transfer those patterns into the console. Retry once with a narrower query naming the operator task and surface. If the retry is still off-target, record that no applicable match was found and use verified project guidance, domain evidence and platform/accessibility standards as the fallback. Do not persist an unverified search result as the project visual system, and do not invent a fixed palette or style merely because the search did not fit. Evaluate marketing pages in a separate design study.

## Non-negotiable UX qualities

- Visual hierarchy makes the primary energy decision obvious without turning every metric into a card.
- Whitespace and density are deliberate: dense where comparison is needed, spacious where explanation or a consequential decision needs focus.
- Color is semantic, tokenized, contrast-checked, and never the only carrier of status. Do not default to green-as-good / red-as-bad for complex or uncertain energy conditions without labels and context.
- Typography, chart annotation, units, dates, times, currency, and numeric precision remain readable and locale-aware.
- Motion is short, purposeful, interruptible, and honors reduced-motion preferences. Use it to explain change, hierarchy, or feedback, not as decoration that delays work.
- Interactions provide visible focus, keyboard support, clear affordance, immediate feedback, and recoverable errors. Do not rely on hover alone.
- Test the real experience at wide desktop, laptop/tablet, and narrow mobile widths. No clipped controls, hidden decision context, or horizontal overflow.
- Support the project's required locales once confirmed. Layouts and content must tolerate Traditional Chinese, Portuguese, and English text lengths and locale-specific formatting; do not claim complete localization from a few translated labels.
- Preserve product originality. A reference is a quality bar or design lesson, not permission to imitate.

## Delivery notes

For each design/review, state: user/task; assumptions; design direction and why; key interaction/data semantics; responsive/localization/accessibility coverage; what was actually checked; and open decisions. Keep proposed visual directions explicitly unapproved until the owner chooses them.

