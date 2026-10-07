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
- PR #10's `DISPATCH-CLAIM-STATE-PRESENTATION-CONTRACT-v0.1.md` says the same more explicitly: for an HVAC shift with no service model/comfort evidence, show an electrical scenario, set HVAC service to “Not assessed,” and withhold **overall dispatch feasibility**. This is a draft presentation proposal, not approved canonical behavior.

## Finding

The implementation withholds the service claim correctly. However, the positive feasibility claim uses the unqualified reason “All applicable schedule constraints are evidenced within this bounded prototype.” In product language, `DISPATCH_FEASIBILITY=ALLOWED` could be read as overall dispatch or service feasibility even though service is not assessed.

This is a claim-label and presentation ambiguity. The code and test do **not** claim comfort/service is satisfied.

## Proposed boundary for review

Keep electrical and service outcomes independent. When a changed resource has no qualified service evaluator, the candidate may show its balanced electrical profile and a separately named **electrical-constraints assessment**, but overall `DISPATCH_FEASIBILITY` must be withheld under the existing PR #10 presentation proposal. Show the resource service state as NOT_ASSESSED/UNKNOWN beside it. Do not present an overall “dispatch feasible”, “operationally feasible”, “safe”, “optimized” or “ready” headline. A future contract may define an independently allowed claim named specifically for electrical schedule feasibility; do not repurpose the current overall claim without reconciling that contract.

| Electrical assessment | Service assessment | Permitted interpretation | Do not claim |
|---|---|---|---|
| Electrical limits qualify; service evaluator absent for a changed resource | NOT_ASSESSED / UNKNOWN | Electrical profile/constraint assessment may be shown; overall feasibility WITHHELD | Overall dispatch/operational feasibility, safety, service satisfied |
| Electrical limits and all applicable changed-resource service profiles qualify | WITHIN_DECLARED_PROFILE for every changed resource | Feasibility only within named profiles, models and evidence scope | Site-safe, field-executable, guaranteed savings |
| Known hard electrical or service bound breached | VIOLATION / INFEASIBLE | Reject candidate for affected scope | Feasible or ready |
| Evidence incomplete | PARTIAL / UNKNOWN | Show independent qualified portions and withheld scope | Treat missing values as zero or infer service success |

Missing service evidence is not proof of either safety or violation. A known, applicable hard-bound breach is a violation for the affected candidate/resource.

## Acceptance gap and next step

The current regression verifies that `COMFORT_SERVICE` is withheld while `DISPATCH_FEASIBILITY` is ALLOWED. That directly conflicts with the PR #10 presentation-contract acceptance example for an HVAC shift without service evidence, which requires overall dispatch feasibility to be withheld. Reconcile the semantics before canonicalizing the contract: either withhold overall feasibility as the existing proposal requires, or introduce a distinct electrical-constraints claim and reserve `DISPATCH_FEASIBILITY` for the broader conclusion. Add a regression assertion for the selected semantics and UI copy after owner/domain review.

This is a design conformance issue for the G7.9 implementation map and UI projection. It does not establish that service models exist and does not select a schema, API, runtime, solver or production stack.

