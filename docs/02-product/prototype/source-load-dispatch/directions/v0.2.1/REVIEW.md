# Dispatch visual directions v0.2.1 — 320px overflow correction and comparison review

**Status:** exploratory; neither concept is approved. v0.2 is preserved unchanged.  
**Parent:** exact PR #10 v0.2 source blob `77c042a16908ace740454d8773896aa2a474178d`.  
**Scope:** responsive summary-card grid correction and version labels only. Concepts, palette, data, claims, interactions and SHADOW/no-control boundary are otherwise unchanged.

## Finding and correction

The exact v0.2 source had a page-width overflow at 320 CSS px: 323px in direction A and 335px in direction B. The visual summary cards' two-column grid kept intrinsic minimum widths, so the peak/settlement values extended beyond the viewport. The schedule graph/table had wider content too, but those remain intentionally inside their own horizontal-scroll regions.

v0.2.1 changes the summary cards to one column at widths ≤360px and allows the final settlement card to occupy that same single column. This retains all three summary values and labels instead of clipping or hiding them. v0.2 remains intact for comparison.

## Rendered layout sweep

Microsoft Edge/Playwright rendered both concepts at each viewport, with the same schedule and interaction state. Document and body widths matched the viewport in all 18 direction/viewport combinations.

| CSS viewport widths | Direction A page width | Direction B page width | Result |
|---|---:|---:|---|
| 1440, 1024, 900, 768, 640, 375 | equals viewport | equals viewport | no page overflow |
| 360, 340, 320 | equals viewport | equals viewport | no page overflow after one-column summaries |

At 320px, the direction A chart content is 570px inside a 260px chart scroll region; its table is 760px inside a 290px table region. Direction B's table is 760px inside a 266px table region. Those are contained internal scroll areas, not page-level overflow. Full-page 320px screenshots for both concepts were visually inspected; 1440px full-page screenshots for both concepts were also inspected. Other widths in the sweep were checked by rendered DOM measurements; their screenshots were not individually inspected.

## Interaction and content checks

- Switched A↔B and confirmed exactly one direction is active each time.
- In direction B, selected 17:00–18:00; the page showed import 480→510 kW, load 540→570 kW, and the six-hour window peak 485→510 kW, with only that interval selected.
- Expanded the interval table and confirmed all six rows.
- Set SHADOW disposition to “需補證據”; the message explicitly remained page-only, without persistence, audit write or equipment operation.
- No JavaScript page errors were recorded.

## Visual readout — not a winner selection

At the inspected wide composition, A makes the full six-hour timeline and evidence blockers visible together; it is better suited to noticing the rebound across the horizon. B gives the selected interval a stronger typographic focus and keeps the rebound/blocked-economics explanation adjacent; the dark composition carries more visual weight and the interval grid remains available below. At 320px, A reads as a vertically flowing evidence-and-timeline page; B reads as a dark interval-review workspace with explicit interval cards. These are desk-review observations, not measured operator preference.

The task remains intentionally centered on dispatch rather than a general energy dashboard. No awarded website is copied. Existing selected contrast-pair calculations from v0.2 are inherited because colors did not change; they remain limited pair checks, not WCAG conformance. The v0.2 review's Apple HIG, Material, WCAG, Webby/Awwwards/FWA source scope and limitations still apply.

## Still open

This comparison does not establish owner direction selection, full keyboard coverage, screen-reader use, text enlargement, full-state contrast, Portuguese/English localization, operator usability, site/tariff validity, scheduling feasibility, savings, or field-control capability. Both concepts are Traditional Chinese synthetic studies. Product scope, production UI, locale set, palette and architecture remain unapproved.
