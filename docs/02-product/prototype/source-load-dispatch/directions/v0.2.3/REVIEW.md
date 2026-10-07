# Dispatch visual directions v0.2.3 — matched-palette layout comparison

**Status:** Exploratory UI study. A/B, palette, product scope and visual identity remain unapproved. This is not a full workflow sign-off, WCAG conformance, operator test, Macau-site result, production UI, or award claim.

**Source:** PR #10 branch `product/source-load-economic-dispatch`, v0.2.3 HTML blob `2f20f55469a6c683eb15e23d39c81028c5ab7690` (branch commit `b8579216c42fcaa2ca3aab233d5ff97e3dd959a4`). It derives from v0.2.2 and preserves its single six-hour synthetic dispatch scenario. v0.2.2 remains unchanged.

## Comparison

Both directions use the same six intervals, measured-example-shaped but synthetic quantities, claims and semantic color tokens. The update removes B's dark variables and status overrides so palette does not vary with layout.

- **A — timeline-first:** shared baseline/candidate interval chart with evidence/readiness beside it.
- **B — interval-first:** selected-hour supply/load explanation and constraint/review panel, with a six-interval selector.
- Both keep the peak comparison and blocked settlement visible; neither displays bill cost, savings, export credit or a device-control action.

The source tables use slightly different spacing and unit suffixes. A numeric-token comparison of every row found the same six interval values in A and B; it is not a claim that every display string is identical.

## Browser review

Rendered the exact fetched v0.2.3 HTML in Microsoft Edge through Playwright. The browser check covered both A and B at 1440, 1024, 900, 768, 640, 375, 360, 340 and 320 CSS px.

- In all 18 layout/viewport combinations, document and body widths matched the viewport.
- At compact widths, chart/table content remains inside its own scroll regions. At 320px, A's chart region is 260px wide around 570px content; table regions are 290px/760px in A and 266px/760px in B. No page-level horizontal overflow was observed.
- Computed palette tokens matched between A and B at every width: paper `#f5f5ef`, surface `#fff`, ink `#152c3a`, teal `#007f78`, orange `#b7502c`.
- Six table rows were checked between layouts; their numeric tokens match.
- Pointer selection of 17:00–18:00 showed grid import 480 → 510 kW. Keyboard Enter on the 16:00–17:00 slot updated the selected interval to 485 → 509.691 kW and left one slot selected; Enter opened the table disclosure.
- The three SHADOW review buttons measured at least 44px high at 320px and 375px after the v0.2.3 correction. This is a targeted check, not a complete touch audit.
- A DOM leaf-text foreground/background scan of B at 1440px found no sampled pair below WCAG normal/large-text thresholds. SVG text, all states, focus contrast and every component were not covered. This does not establish WCAG conformance.
- No browser page errors occurred during the recorded interactions.

Saved review images in the local task workspace:
- [Direction A at 1440px](/C:/Users/admin/Documents/Codex/2026-10-03/chatgpt-conversation-6abf4f5c-b2d4-83ea-b189/work/dispatch-direction-v023-A-1440.png)
- [Direction B at 1440px](/C:/Users/admin/Documents/Codex/2026-10-03/chatgpt-conversation-6abf4f5c-b2d4-83ea-b189/work/dispatch-direction-v023-B-1440.png)
- [Direction B at 320px](/C:/Users/admin/Documents/Codex/2026-10-03/chatgpt-conversation-6abf4f5c-b2d4-83ea-b189/work/dispatch-direction-v023-B-320.png)

## Findings and limits

The shared palette makes the information-hierarchy comparison cleaner. A exposes the whole horizon first; B gives a selected interval and constraints more prominence. This browser check establishes neither operator preference nor the best primary workflow. The composition is still a prototype study with small secondary labels, a synthetic six-hour example, Traditional Chinese only, no authenticated evidence, no comfort/service evaluator, no runtime localization and no backend binding. B's table is horizontally scrollable; the table disclosure is not a substitute for a full mobile table usability review.

No A/B direction is selected. Next design review should compare task completion and error detection with representative operators, and should carry the chosen composition through the six-stage workflow, localized content, full keyboard/assistive-technology review, and current browser render tests before design approval.
