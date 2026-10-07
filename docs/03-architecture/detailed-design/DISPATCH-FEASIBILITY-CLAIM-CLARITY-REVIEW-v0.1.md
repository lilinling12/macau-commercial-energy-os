# Dispatch-feasibility claim clarity review v0.1

**Status:** Review finding and proposed wording boundary; not an approved contract or product decision.  
**Reviewed:** 2026-10-07  
**Design branch:** PR #10 `product/source-load-economic-dispatch`  
**Experiment branch:** PR #14 `poc/shadow-dispatch-assessment`, exact head `deed7683a8b0ce3a811966ab8fc3b030695debad`

## Evidence reviewed

- PR #14 is open, Draft, and unmerged at the exact head above.
- Its assessment defines separate `DISPATCH_FEASIBILITY` and `COMFORT_SERVICE` claims.
- When a supplied HVAC electrical schedule is inside its declared envelope, the code can return `DISPATCH_FEASIBILITY=ALLOWED` while returning `COMFORT_SERVICE=WITHHELD`, reason: “Thermal comfort and other service constraints are not modeled.”
- Test `test_electrical_feasibility_does_not_assert_comfort_service` explicitly expects that combination.
- The optimizer's `_check_baseline_service` checks flexible tasks' aggregate energy, availability mask and electrical power envelope. It does not evaluate HVAC thermal comfort, an EV departure-energy target, or hot-water delivery/service.
- PR #10's flexible-load service-boundary design already says an electrical schedule does not establish delivered service; absent a qualified service trajectory, the result is electrical-only and not operationally feasible.

## Finding

The implementation withholds the service claim correctly. However, the positive feasibility claim uses the unqualified reason “All applicable schedule constraints are evidenced within this bounded prototype.” In product language, `DISPATCH_FEASIBILITY=ALLOWED` could be read as overall dispatch or service feasibility even though service is not assessed.

This is a claim-label and presentation ambiguity. The code and test do **not** claim comfort/service is satisfied.

## Proposed boundary for review

Keep electrical and service outcomes independent, but qualify any positive result as **bounded electrical schedule feasibility** (or a future canonical equivalent) and show the service state beside it. If a changed resource has no service evaluator, do not present an overall “dispatch feasible”, “operationally feasible”, “safe”, “optimized” or “ready” headline. The interface may show the balanced electrical profile and the specific electrical constraints checked.

| Electrical assessment | Service assessment | Permitted interpretation | Do not claim |
|---|---|---|---|
| ALLOWED within declared electrical envelope | NOT_ASSESSED / UNKNOWN | Bounded electrical schedule only; service unresolved | Overall dispatch/operational feasibility, safety, service satisfied |
| ALLOWED within declared electrical envelope | WITHIN_DECLARED_PROFILE for every changed resource | Supported only within named profiles, models and evidence scope | Site-safe, field-executable, guaranteed savings |
| Known hard electrical or service bound breached | VIOLATION / INFEASIBLE | Reject candidate for affected scope | Feasible or ready |
| Evidence incomplete | PARTIAL / UNKNOWN | Show independent qualified portions and withheld scope | Treat missing values as zero or infer service success |

Missing service evidence is not proof of either safety or violation. A known, applicable hard-bound breach is a violation for the affected candidate/resource.

## Acceptance gap and next step

The current regression verifies that `COMFORT_SERVICE` is withheld; it does not assert the user-facing meaning of an ALLOWED `DISPATCH_FEASIBILITY` result. Add a claim-vocabulary and UI-copy assertion when the cross-runtime claim contract and owner-facing terminology are reviewed.

This is a design conformance issue for the G7.9 implementation map and UI projection. It does not establish that service models exist and does not select a schema, API, runtime, solver or production stack.
