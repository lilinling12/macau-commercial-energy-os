# v2.1 mixed readiness state study — review record

Status: review draft; synthetic interaction study only. It does not replace the v2.0 source or make a production product/architecture decision.

## Purpose

Make four independent claims visible together in the cost/constraints stage: (1) electrical balance can be reconciled in the supplied synthetic example, (2) comfort/service evidence may be unassessed, stale, failed, or synthetically passing, (3) bill economics remains unavailable without verified tariff/contract/window evidence, and (4) equipment control remains unavailable in SHADOW.

## Interaction

Four native radio states change the service label, explanation, and polite live announcement. All displayed values and statuses are mock UI state. No API, persistence, site evidence, command path, or equipment control is connected.

## Source checks completed

- Started from PR #10 v2.0 source at blob `44f1c23fe0d86d7029f8370796a446ed22cff651`, fetched at branch head `f83e4963cf36fe6a108e2782b227a7e61a9cb854`.
- The exact v2.1 inline JavaScript passed `node --check` at source blob `846c966f78413f36da1d14b4a3f84bc8dc400099`; the subsequent version-label-only correction is at the current file revision.
- Browser render inspected at 1265 × 712 screenshot pixels. The mixed-readiness card and all four status columns fit within the visible page width in the default desktop state. No conclusion is made for other viewport sizes.
- All four radio states were selected in the browser. The visible state text and accessibility tree updated for unassessed, stale, unmet and synthetic-pass states; the live announcement explained each boundary.
- Keyboard Right from the first radio moved selection to the stale-evidence option and updated the live announcement.
- The initial render exposed stale v2.0 labels in the browser title, side rail and footer. These were corrected to v2.1; a reload confirmed all three labels.
- Source inspection confirms four native radio options, `role=status` / `aria-live=polite`, and the explicit SHADOW/no-control notice. CSS defines 4-column, 2-column and narrow single-column breakpoints at 900px, 560px and 360px, but those breakpoints were not browser-tested in this review.

## Not verified in this iteration

Exact 900px/560px/360px viewport behavior, narrow-screen overflow, measured contrast, full keyboard coverage, screen-reader output, full localization, operator validation and API binding remain unverified. The prototype is Traditional Chinese only; it is not evidence of complete Portuguese/English support. This review does not claim WCAG conformance or award-level quality.
