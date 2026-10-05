# v2.1 mixed readiness state study — review record

Status: review draft; synthetic interaction study only. It does not replace the v2.0 source or make a production product/architecture decision.

## Purpose

Make four independent claims visible together in the cost/constraints stage: (1) electrical balance can be reconciled in the supplied synthetic example, (2) comfort/service evidence may be unassessed, stale, failed, or synthetically passing, (3) bill economics remains unavailable without verified tariff/contract/window evidence, and (4) equipment control remains unavailable in SHADOW.

## Interaction

Four native radio states change the service label, explanation, and polite live announcement. All displayed values and statuses are mock UI state. No API, persistence, site evidence, command path, or equipment control is connected.

## Source checks completed

- Started from PR #10 v2.0 source at blob `44f1c23fe0d86d7029f8370796a446ed22cff651`, fetched at branch head `f83e4963cf36fe6a108e2782b227a7e61a9cb854`.
- Inline JavaScript syntax checked with `node --check`.
- Source inspection confirms four native radio options, `role=status` / `aria-live=polite`, and the explicit SHADOW/no-control notice.
- Responsive CSS defines 4-column, 2-column, and narrow single-column breakpoints at 900px, 560px, and 360px.

## Not verified in this iteration

The browser preview action was denied by automatic review while the review service was at capacity. No workaround was attempted. Therefore visual rendering, state-switch behavior in a browser, keyboard traversal, responsive overflow, contrast, assistive-technology output, and localization are unverified. This record does not claim WCAG conformance, operator validation, or award-level quality.

Before treating the UI direction as reviewed, render this exact v2.1 file and inspect all four states at wide, tablet, mobile, and narrow-mobile widths. Then record actual findings and update the design based on those findings.
