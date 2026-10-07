# G7.9 cross-review — Python SHADOW dispatch experiment

**Status:** implementation review; proposal remains unapproved.  
**Evidence branch:** PR #14 `poc/shadow-dispatch-assessment`, exact head `f443dd21fed30386937510a69d0b4c8dabb1b6f3`.  
**Design branch:** PR #10 `product/source-load-economic-dispatch`.

## Verified improvement

The current G7.9 time-boundary design retains UTC instants and the named site-local timezone. PR #14 originally required every timestamp's wall-clock fields to match the site zone, so an equivalent UTC-encoded Macau interval was rejected. The prototype was changed to accept timezone-aware instants in UTC/explicit offsets while still validating the IANA site timezone. Elapsed duration now uses the UTC instants.

A regression test constructs baseline/candidate intervals in UTC for the same Asia/Macau hour and asserts the physical result and 10 kWh integration. On exact PR #14 head `f443dd21fed30386937510a69d0b4c8dabb1b6f3`, Runtime Bootstrap passed all four jobs; Optimizer ran 19 tests successfully, including this new case: [Runtime Bootstrap #37248083253](https://github.com/lilinling12/macau-commercial-energy-os/actions/runs/37248083253).

## Current gaps against T1 semantics

1. The request-level physical evidence tuple is all-or-nothing: any UNKNOWN/STALE item causes the whole physical assessment to return BLOCKED. It cannot yet scope a missing point/mapping to only dependent intervals/assets or retain independent claims.
2. The economic evaluator requires verified account/meter mapping, contract, tariff and an exact rate for every schedule interval. It returns one grid-import energy component or withholds all monetary output; it does not return independent partial economic claims or split rates across effective tariff boundaries.
3. Evidence references are caller-supplied. The experiment neither resolves nor authenticates evidence, tenant/site authority, or point-to-meter mappings.
4. Comfort/service bounds for HVAC, EV and hot water, tariff demand/Pu windows, export compensation, full bill reconstruction, safety interlocks, uncertainty and realized savings remain outside the PoC. Its draft description states those limits.

These are disclosed experiment limits, not proof that PR #14 is a production optimizer. The new PR #10 T1 claim-readiness matrix is a review target for later service/corpus work; it does not retroactively turn this PoC into an implementation of that matrix.

## Exact-head check boundaries

- Runtime Bootstrap: all four jobs passed at PR #14 head above.
- [Authority Validation #37248083394](https://github.com/lilinling12/macau-commercial-energy-os/actions/runs/37248083394) failed because the required authority file path was missing.
- [Repository Hygiene #37248083213](https://github.com/lilinling12/macau-commercial-energy-os/actions/runs/37248083213) failed because its check still expects the legacy `docs/handoff/CURRENT.md` and `CONTINUE-PROMPT.md` paths. This is a repository authority/handoff alignment issue and must be evaluated separately from the passing runtime workflow.

## Next engineering evidence

- Decide how evidence scope is represented (request-, asset-, interval- or claim-level) after T1 product/domain review; do not silently make caller markers authoritative.
- Add cases for one stale independent point, unresolved site mapping, PV export without payee, missing ESS state, missing flexible-load service bounds, absent Pu interval, and tariff boundary split/withholding.
- Keep monetary components separate and make withheld reason/scope explicit. Only connect the acceptance corpus to the implementation after the applicable contract and authority profile are approved.
- Keep read-only acquisition and SHADOW review separate from any device-command authorization path.

## T1 service-boundary cross-check — 2026-10-07

### Evidence inspected

- PR #14 is still open, Draft, and unmerged at exact head `deed7683a8b0ce3a811966ab8fc3b030695debad`.
- The current prototype assessment defines separate `DISPATCH_FEASIBILITY` and `COMFORT_SERVICE` claims. Its readiness logic can return `DISPATCH_FEASIBILITY=ALLOWED` when the physical profile and declared schedule constraints qualify, while always returning `COMFORT_SERVICE=WITHHELD` with reason “Thermal comfort and other service constraints are not modeled.”
- A regression test named `test_electrical_feasibility_does_not_assert_comfort_service` explicitly expects that combination. The optimizer's `_check_baseline_service` checks each flexible task's aggregate energy, availability mask, and electrical power envelope; it does not evaluate thermal comfort, EV departure target, or hot-water delivery/service.
- The PR #10 service-boundary design already states that an electrical schedule is not a service outcome, and that without a qualified service trajectory an HVAC result is an electrical scenario, not operational feasibility.

### Finding

The implementation does withhold the service claim correctly, but its positive `DISPATCH_FEASIBILITY` claim uses the unqualified reason “All applicable schedule constraints are evidenced within this bounded prototype.” The `ALLOWED` state is therefore broader in ordinary product language than the evidence: HVAC/EV/hot-water service has not been assessed. This is a claim-label/copy ambiguity, not evidence that the prototype asserts comfort service—the separate withheld claim and test show the opposite.

### Proposed resolution for review

Keep the two claim dimensions independent, but qualify the positive claim wherever it appears as **bounded electrical schedule feasibility** (or the eventual canonical equivalent), with an explicit service state alongside it. When any changed resource has no service evaluator, the UI/API must not present a generic “dispatch feasible”, “operationally feasible”, “optimized”, or “ready” headline. The result may still expose the balanced electrical profile and the bounded electrical constraints it checked. A known evidenced hard service-bound violation must invalidate that resource's candidate; missing service evidence remains UNKNOWN/NOT_ASSESSED and must not be described as either safe or violated.

| Electrical schedule assessment | Resource service assessment | Permitted interpretation | Prohibited summary |
|---|---|---|---|
| ALLOWED within declared electrical envelope | NOT_ASSESSED / UNKNOWN | Bounded electrical schedule only; service is unresolved | Dispatch/operational feasibility, safe, service satisfied |
| ALLOWED within declared electrical envelope | WITHIN_DECLARED_PROFILE for every changed resource | Service is supported only within named profiles/models and evidence scope | Site-safe, field executable, guaranteed savings |
| Any known hard electrical or service bound is breached | VIOLATION / INFEASIBLE | Candidate rejected for the affected scope | Feasible/ready |
| Incomplete evidence | PARTIAL / UNKNOWN | Show independent qualified portions and withheld scope | Treat missing values as zero or infer service success |

### Acceptance gap and next action

The current regression only checks that COMFORT_SERVICE is withheld; it does not assert the user-facing interpretation of an ALLOWED `DISPATCH_FEASIBILITY` result. Add a claim-vocabulary/copy assertion when the cross-runtime claim contract and owner-facing terminology are reviewed. Until then, this is a design conformance issue for PR #10's map and UI projection—not a reason to pretend service models exist or to change the production stack. No schema/API is selected by this review.

