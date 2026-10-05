# Dispatch workflow prototype v1.6 — UI/UX review

**Status:** Review artifact; visual and interaction direction remains unapproved.  
**Date:** 2026-10-05  
**Prototype:** [v1.6/index.html](index.html)  
**Baseline:** v1.5 source blob `b9417aa9db49c261e1d5d70fec733982aaead821`; v1.6 changes navigation and narrow-screen site context only.  
**Task represented:** Let a commercial-energy operator compare source/load arrangements over the same time window, inspect the evidence boundary, and move through a six-stage SHADOW review. All displayed energy and site values remain synthetic.

## What changed in v1.6

- Replaced four ambiguous Unicode navigation glyphs with a consistent set of inline SVG icons for overview, dispatch, model and evidence.
- Kept explicit Traditional Chinese accessible names and the current-page marker on dispatch. Desktop retains the compact rail; keyboard focus reveals the short label.
- On screens at or below 760 CSS px, the 64 px top rail displays each icon with a visible 11 px Chinese label. Each target measures 50 × 50 px.
- Localized the context breadcrumb to Traditional Chinese.
- At widths at or below 390 px, moved “澳門情境” to its own aligned line beneath the site name, removing the orphaned final character and separator.
- Preserved the v1.5 schedule data, source/load balance, synthetic evidence boundary, six-stage workflow, SHADOW-only disposition, and no-control state.

## UI/UX Pro Max and project skill use

The required UI/UX Pro Max design-system query was run for a commercial energy dispatch operator console. Its top result combined a conversion-focused marketing-page structure with an “Organic Biophilic” style, green call-to-action colors, and Syncopate/Space Mono typography. That result does not fit a persistent operator workspace, so none of those style or type choices were applied.

A focused UX search returned general guidance about responsive tables, redundant color encoding, heading order, and repeated form entry. The table guidance is already represented by v1.5's card layout at narrow widths. For v1.6, the project skill's energy-operations and quality-review guidance drove the specific change: keep navigation visually understandable at small widths, preserve the task's synthetic/evidence boundary, and do not turn the operator workflow into a promotional landing page.

The project skill's product rules remain in force: energy-flow graphics require evidence, physical energy and financial settlement stay separate, measured/forecast/scenario/synthetic states are named, and SHADOW review never implies execution.

## Reference principles consulted

These references were used as quality criteria, not copied as templates:

- [Apple Human Interface Guidelines — Layout](https://developer.apple.com/design/human-interface-guidelines/layout) and [Motion](https://developer.apple.com/design/human-interface-guidelines/motion): adapt layout to context and keep motion purposeful and responsive to accessibility settings.
- [Google Material 3 — Canonical layout examples](https://m3.material.io/foundations/layout/canonical-examples/overview): adapt navigation and panes to the available screen, preserving a clear hierarchy.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/), including [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) and [Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum): check narrow reflow and usable targets. Passing the limited checks below is not a conformance result.
- [Awwwards — Proof SOTD review](https://www.awwwards.com/sites/proof-1): the public score shows separate design, usability, creativity and content dimensions, and a separate development score. That supports evaluating operational clarity and responsive craft alongside originality.
- [Webby Awards — Judging Criteria](https://www.webbyawards.com/judging-criteria/) and [Best User Interface winners](https://winners.webbyawards.com/winners/websites-and-mobile-sites/features-design/best-user-interface): consider experience quality and interface craft, not visual novelty alone.
- [FWA 25th Anniversary](https://thefwa.com/FWA25/25.html): its stated digital-work themes include creativity, originality and technical excellence.

Award references set an aspiration for original, well-crafted work. They do not establish that this prototype is award-ready, and marketing-site spectacle is not a substitute for reliable energy operations.

## Checks performed

Edge/Playwright rendered the local v1.6 HTML at:

| Viewport | Document width | Navigation |
|---|---:|---|
| 1440 × 1000 | 1440 px | Icon rail; 44 px high targets |
| 1024 × 900 | 1024 px | Icon rail; 44 px high targets |
| 768 × 900 | 768 px | Icon rail; 44 px high targets |
| 680 × 900 | 680 px | Labeled top rail; 50 × 50 px targets |
| 375 × 844 | 375 px | Labeled top rail; 50 × 50 px targets |
| 320 × 844 | 320 px | Labeled top rail; 50 × 50 px targets |

At each viewport, document width equaled viewport width, and navigation stayed inside the viewport. The review checked the six navigation accessible names, `aria-current="page"` on dispatch, mobile label visibility, and minimum target dimensions. A keyboard path reached the skip link first, then the overview button with a visible focus outline. The page-error listener recorded no JavaScript errors. Desktop and mobile screenshots were visually inspected after the render.

## Limits and open work

- Traditional Chinese is the only fully represented locale in this prototype. This does not demonstrate complete Portuguese or English localization, translation quality, localized dates/currency, or locale-specific number formatting.
- No screen-reader session, touch-device session, text enlargement, page-wide contrast audit, or complete keyboard walkthrough was performed. No WCAG conformance is claimed.
- The responsive checks cover layout and navigation at six widths; they do not establish usability with operators, field/site validity, economic correctness, a working optimizer, dispatch feasibility, production UI readiness, or equipment-control authority.
- The site, loads, PV, storage and values remain synthetic. The prototype does not claim savings, export settlement, controllability, or live execution.
- Product scope, locale scope, palette, visual system and production architecture remain subject to owner review.
