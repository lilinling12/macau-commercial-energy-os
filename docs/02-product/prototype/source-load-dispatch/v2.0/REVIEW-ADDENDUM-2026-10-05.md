# v2.0 Review Addendum — Service readiness disclosure

**Status:** Source-level product review; not a new visual direction or owner-approved design.  
**Date:** 2026-10-05  
**Reviewed source:** v2.0 `index.html`, Git blob `44f1c23fe0d86d7029f8370796a446ed22cff651`. The existing v2.0 `REVIEW.md` remains the responsive chart-legibility review; this addendum does not extend its browser-test claims.

## Finding

The prototype already contains visible, static safeguards for missing comfort/service evidence:

- In source qualification, the HVAC row asks for point mapping, comfort/service bounds, authorization and response evidence.
- The resource summary says HVAC shifting/rebound is synthetic and does not prove comfort/service bounds or controllability.
- The readiness checklist says the HVAC comfort model is not established.
- The constraint table labels HVAC comfort/service bounds as illustrative and candidate feasibility as unverified.
- The page says the schedule remains a scenario comparison and is not executable; no device operation is authorized or performed.

This corrects the broad reading that the prototype has no service-readiness disclosure. Those disclosures are present in the reviewed HTML source.

## What remains unverified

The source is a static synthetic workflow. It does not bind its displayed service state to the optimizer's `COMFORT_SERVICE` claim, nor test how a runtime API result with `DISPATCH_FEASIBILITY=ALLOWED` and `COMFORT_SERVICE=WITHHELD` is rendered. The existing v2.0 browser review rendered one Traditional-Chinese synthetic `dispatchComparison` state for chart/layout legibility; it did not report a focused service-readiness interaction or API-state mapping review.

## Proposed acceptance invariant

Keep electrical balance/equipment-envelope readiness, economic eligibility and comfort/service outcome as separate states. If service/comfort evaluation is unavailable, display “未评估 / Not assessed” alongside the candidate schedule; never translate bounded electrical feasibility into “可执行 / ready to execute.” Preserve the explicit SHADOW/no-command boundary. Add paired UI/API examples for service evidence missing, current, stale and infeasible before claiming dynamic readiness behavior.

This addendum records static evidence and a remaining integration gap. It does not imply user validation, full localization, WCAG conformance, a production contract or G7.9 Step 3 completion.
