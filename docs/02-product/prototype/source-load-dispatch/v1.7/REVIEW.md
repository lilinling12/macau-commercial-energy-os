# Source/load dispatch workflow prototype v1.7 — review

**Status:** Unapproved mobile-density variant; v1.6 remains unchanged.  
**Date:** 2026-10-05  
**Parent:** v1.6, source blob `f16a80df67ae4504751d0a46473f181aa86cdcbb`; proposal branch `product/source-load-economic-dispatch`.  
**Task:** Surface the source/load schedule comparison sooner on narrow screens while preserving time window, Shadow status, synthetic-data warning, and access to full planning conditions.

## Change

At widths up to 680 CSS px, the four-cell planning context collapses behind a native disclosure row: “規劃條件 · 12:00–18:00 · Shadow”. The site header continues to show that this is synthetic, non-field data. Expanding the row reveals the full planning period, input snapshot, Shadow state, and unverified billing-rule status. Desktop keeps the planning strip expanded and hides the disclosure label.

The change is presentation only. It does not alter schedule values, chart semantics, cost claims, accessibility names for existing controls, product scope, or the SHADOW/no-device-control boundary.

## Browser review

I fetched the exact v1.6 file from PR #10, created v1.7 on that branch, fetched the created branch file back to the local preview server, then reviewed the rendered page and DOM accessibility state.

| Viewport | Document scroll width | Planning context | Dispatch section top |
|---|---:|---|---:|
| 320 × 844 | 305 px / 320 px viewport | Collapsed by default; expanded state shows all four cells | 620 px |
| 375 × 844 | 360 px / 375 px viewport | Collapsed by default | 596 px |
| 1440 × 1000 | 1425 px / 1440 px viewport | Expanded strip remains visible; disclosure label hidden | 475 px |

At 375 px, the dispatch section begins 56 px earlier than v1.6 (652 px → 596 px). At 320 px, the heading, planning controls, compact context, stage summary, dispatch heading, and synthetic-data caveat begin within the first viewport. The actual time-series plot still requires scrolling at this width; this change improves entry into the task but does not put the full comparison above the fold.

At 320 px, clicking the summary opened the 2 × 2 context cells without increasing document width. Keyboard Enter opened and closed the same native disclosure; focus remained on the summary control. At desktop the full status strip remained present. The top-level source remains Traditional Chinese; the existing site-context, schedule, constraints, and no-control copy are unchanged. No Portuguese or English behavior was reviewed.

## Findings and limits

- **Improved:** redundant planning metadata consumes less initial vertical space on mobile while the time window and Shadow status remain visible.
- **Still open:** the core plot itself remains below the 320 px first viewport; the site header, title and planning controls still consume considerable height. Further exploration should compare a denser mobile header/control treatment before choosing a baseline.
- **No horizontal overflow** was observed at these three widths. This is a bounded layout check, not complete breakpoint or WCAG conformance.
- No screen-reader session, full keyboard path, text enlargement, measured contrast, loading/empty/error state review, complete locale review, representative operator evaluation, live-site data, tariff validation, optimizer validity, dispatch feasibility, savings, or device control was tested or established.
- All values remain synthetic. v1.7 is not an approved visual direction, product decision, or production UI.

## Source and preview

- Proposed file: `index.html`
- Rendered local preview: `http://127.0.0.1:8773/dispatch-v17-study.html`
- UI/UX references and the project skill remain evaluation inputs; this variant does not adopt an award site's composition or choose a palette.
