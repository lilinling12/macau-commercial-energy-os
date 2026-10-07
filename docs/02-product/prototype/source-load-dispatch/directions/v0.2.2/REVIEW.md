# Dispatch visual directions v0.2.2 — keyboard scrolling follow-up

**Status:** exploratory; A/B and their palettes remain unapproved. v0.2 and v0.2.1 remain unchanged.  
**Parent source:** PR #10 v0.2.1 source blob `258806c072353c6a33fef2a902662e0725eef3b5`.  
**Scope:** make the already focusable horizontal chart/table regions respond to arrow keys, and update the chart's accessible name to say so. No schedule values, layout, direction, color, or product claim changed.

## Finding and change

Keyboard review of v0.2.1 found that its chart and data-table regions had a `tabindex` and labels indicating horizontal scrolling, but pressing ArrowRight while focused left `scrollLeft` at zero. v0.2.2 adds a bounded 160px ArrowLeft/ArrowRight step to the chart and table regions. It clamps at the region's scroll limits and prevents the key from moving the document horizontally.

## Keyboard interaction checks at 320 × 844 CSS px

| Direction / region | Scrollable distance | ArrowRight | ArrowLeft |
|---|---:|---:|---:|
| A chart | 310px | 0 → 160px | 160 → 0px |
| A six-interval table | 470px | 0 → 160px | 160 → 0px |
| B six-interval table | 494px | 0 → 160px | 160 → 0px |

Also opened both table disclosures by focusing the summary and pressing Enter. Switched A↔B with Enter. In B, selected the last interval by keyboard and confirmed 17:00–18:00 and 480 → 510 kW. These are targeted browser interactions, not full keyboard-flow or screen-reader validation.

v0.2.1's 18-combination viewport sweep remains the responsive baseline for this JavaScript-only follow-up: both directions at 1440, 1024, 900, 768, 640, 375, 360, 340 and 320px. At 320px chart/table overflow remains inside the focusable named regions; the document itself fits the viewport. No text, chart, or table content was removed.

## Limits

This update does not establish WCAG conformance, screen-reader behavior, focus-order completeness, text enlargement, touch usability, full-state color contrast, complete Chinese/Portuguese/English localization, operator preference, Macau site/tariff validity, schedule feasibility, savings, or device control. A/B and visual direction remain unselected; the interaction remains page-only and SHADOW-only.
