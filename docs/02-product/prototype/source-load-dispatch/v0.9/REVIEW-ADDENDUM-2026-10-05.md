# Source/load dispatch v0.9 — visual review addendum

**Review date:** 2026-10-05  
**Scope:** Rendered PR #10 v0.9 screenshots at 1440px and 375px; targeted `ui-ux-pro-max` chart and UX search. This supplements the existing exact-source interaction review. It is not a user study or conformance certification.

## Design guidance checked

Used the installed `ui-ux-pro-max` skill and its local search data with three focused queries:

- `commercial energy operations chart direct labels` (`chart`): time-series advice supports direct labels, distinctions beyond hue, and a visible data-table/summary fallback.
- `mobile chart scroll keyboard responsive accessibility` (`ux`): general responsive guidance discourages horizontal overflow and recommends mobile-first layouts; keyboard operation and a clear alternative are part of chart accessibility.
- `accessible color states keyboard focus` (`ux`): keep focus visible, expose selected state semantically, and do not convey status through color alone.

These are skill recommendations to apply with context. A dense time-series plot may retain an internal horizontal viewport when its full interval detail cannot fit; that exception should remain visible, keyboard accessible, and paired with an equivalent alternative.

## Screenshot observations

### 1440px

- The dispatch task is the visual focus: a clear source/load heading, explicit synthetic-data warning, interval schedule chart and evidence/readiness comparison.
- The chart distinguishes baseline and candidate and calls out HVAC shift/rebound, PV, ESS action and the full-window peak. The later peak increase is visible, avoiding a misleading “lower demand” claim based only on the shifted interval.
- Readiness and economics constraints remain separate from the physical schedule. Unknown billing-period Pu is explicitly not converted into a bill amount.
- The page uses a restrained neutral base with teal, lime, purple and orange for domain series/status. The screenshot supports visual coherence; it does not establish that this is the approved brand palette.

### 375px

- Workflow steps, controls, evidence panels and review choices stack into a single readable column; no new document-level horizontal overflow was observed in the rendered screenshot. Prior exact-source browser measurements remain recorded in `SOURCE-LOAD-DISPATCH-PROTOTYPE-REVIEW-v0.9.md` for 1440/1024/768/375px.
- The schedule SVG is intentionally 640px wide inside a roughly 345px viewport. The page shows a scroll hint, provides a “view data table” alternative, and the prior browser review recorded keyboard arrow scrolling. The screenshot alone cannot establish touch discoverability, screen-reader equivalence, or that users will notice the hint.
- The mobile page remains long (the exact-source review measured 3,081px at the 375×844 viewport). This is documented as a hierarchy/usability question, not as a defect proven by screenshot review.

## Disposition and next design evidence

The current version is a defensible responsive prototype for review, not a completed mobile UX. Keep the full temporal chart and interval table available. Before approving the visual direction, compare a mobile-specific compact representation (for example, a six-interval summary with an explicit “open full chart/table” action) against the current scrollable chart using the same evidence and schedule values. Validate touch scrolling, keyboard focus/scroll, and screen-reader announcement on the chosen version; record the tested states and locale separately.

Do not remove series or interval information solely to shorten the page. Preserve the distinction between grid import, site PV, ESS charge/discharge, total load, and HVAC rebound. Avoid presenting prototype screenshot review as WCAG conformance, full localization, award-level quality, or representative-operator validation.

## Source links and limits

- Prototype: PR #10, `docs/02-product/prototype/source-load-dispatch/v0.9/index.html` (the branch is open and Draft).
- Existing exact-source interaction/responsive review: `docs/02-product/prototype/source-load-dispatch/v0.9/REVIEW.md`.
- This addendum records screenshot inspection and skill guidance only. No code, accessibility-tree, touch-device, Portuguese, English, or representative-user validation was performed in this pass.


