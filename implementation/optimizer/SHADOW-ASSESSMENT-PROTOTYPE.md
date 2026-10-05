# SHADOW dispatch assessment prototype

The assessment module validates a schedule supplied by another component. The adjacent `dispatch_optimizer.py` adds an experimental bounded schedule generator over a declared discrete action space. Neither module has a device-control interface.

## What it checks

- Baseline and candidate use the same contiguous, site-timezone intervals.
- PV generation reconciles to on-site use, export, or curtailment.
- Each interval's AC power balance reconciles.
- Flexible-load power stays inside the supplied asset envelope.
- ESS power, SOC transitions, efficiency, and interval continuity stay inside the supplied limits.
- An optional candidate grid-import guard is respected.
- Economic output is limited to a precisely interval-matched grid-import energy charge and is withheld unless account/meter, contract, tariff, and rate references are marked verified. ESS comparisons also require matching SOC at the schedule-window boundaries.

The search prototype uses dynamic programming over discrete task power and ESS charge/discharge steps. It preserves aggregate required energy for each flexible task, uses the supplied import-rate series as its objective, applies an optional per-interval import guard, starts at the baseline SOC and ends at the baseline terminal SOC. It is exact only within that finite declared action space and short-horizon search budget, not over a continuous production model. Assumption-tagged inputs may guide a scenario candidate, but the result is explicitly marked scenario-only and bill-grade monetary output stays subject to the separate evidence gate.

## What it does not prove

The assessment trusts the caller's `EvidenceRef.state`; it does not retrieve, authenticate, or independently verify the referenced evidence. A `VERIFIED` state in a synthetic input is not proof of a Macau site fact. It does not establish contractual export rights, cross-building settlement, customer tariff applicability, load comfort/service feasibility, demand charges, taxes, export credits, full-bill settlement, forecast quality, optimizer quality, or realized savings. Those remain gated on evidence models, approved contract semantics, and site validation.

The search does not model demand charges, tariff demand windows, export revenue, battery degradation, reserve requirements, equipment ramp/minimum-on dynamics, thermal comfort, EV departure deadlines beyond a simple availability mask, hot-water service constraints, forecast uncertainty, or site-specific safety interlocks. It does not authenticate evidence, establish contractual export rights, cross-building settlement, customer tariff applicability, or realized savings. The current `VERIFIED` marker is a trusted caller assertion until the approved evidence service/contract is integrated.

These are code-level SHADOW boundary experiments, not an approved API, production optimizer, G7.9 Step 3 closure, or pilot-readiness claim. Product and production-architecture choices remain subject to owner review.

## Local check

From `implementation/optimizer`, run `PYTHONPATH=src python -m unittest discover -s tests -v`. Project `pyproject.toml` currently requires Python `>=3.14,<3.15`; results on another interpreter are useful development evidence, not target-runtime proof.



## Claim-specific readiness follow-up (T1 experiment)

The assessment now distinguishes its overall physical status from a fixed claim-readiness ledger. If core site/meter/topology evidence is absent, unknown or stale, the physical assessment remains BLOCKED. If that core evidence qualifies but only a resource-specific constraint is unresolved, the implementation can retain the balanced grid-import profile while returning PHYSICAL PARTIAL and withholding the affected dispatch-feasibility claim:

- Missing or unknown ESS operating evidence with an active ESS schedule withholds ESS and overall dispatch-feasibility claims; it does not erase a profile whose core physical inputs and power balance qualify.
- Missing or unknown/stale flexible-load envelope evidence withholds the claim for a changed load. An unchanged load is treated as part of the supplied profile, not as a claim that the product can control it.
- Missing or unknown/stale grid-import-guard evidence withholds guard compliance, while preserving an otherwise supported profile.
- A verified import-energy component may still be calculated against exact intervals when these physical resource constraints are unresolved, but its economic status is SCENARIO_ONLY. It is not savings, a full bill, or proof that the candidate schedule is feasible.

The result includes per-claim ALLOWED/WITHHELD status and a bounded scope. Demand charges, export compensation, full-bill totals, savings, controllability, comfort/service, cross-site credits and device control remain explicitly WITHHELD. Three focused tests cover unknown ESS evidence, a stale flexible-load envelope with scenario-only economic output, and an unknown grid guard.

This is a prototype-level T1 advance, not the complete T1 acceptance matrix. Claim types and reason text are not canonical contracts; caller-provided evidence references are not retrieved or authenticated; the fixed ledger does not yet represent multiple independent meter/account scopes or evidence provenance at each interval; and real site topology, tariff applicability and operational feasibility remain unvalidated. Production schema/API changes require the separate authority and owner decisions.


## Partial rate coverage and interval-boundary withholding

The assessment now reports the exact schedule intervals whose import-energy rates have one unique, valid, VERIFIED exact-interval match. It calculates baseline and candidate energy charges only over those common covered intervals, returns their timestamp pairs and the total number of schedule intervals, and labels incomplete coverage `PARTIAL`. Uncovered, unverified, invalid or duplicate-rate intervals are disclosed in the reasons and are never treated as zero. If no interval qualifies, the energy component is BLOCKED.

A rate window that splits a schedule interval does not exactly match it. Because this prototype has only an interval-average grid-import quantity and no finer-grained measured/forecast load profile to allocate kWh across the rate boundary, it withholds that schedule interval rather than applying either rate to the whole interval. Exact sub-interval allocation requires finer-grained source data and an approved tariff interval policy. This prototype result is still only the import-energy component, not demand charges, full bill, savings or settlement validation.


## Per-interval economic component trace

For each eligible schedule interval, the result now carries a prototype-local economic component record: start/end instant, caller-supplied rate evidence reference, MOP/kWh rate, baseline and candidate import kWh, and each corresponding import-energy amount. Aggregate baseline/candidate/delta fields equal the sum of these records. The record improves review and replay diagnostics but does not authenticate the evidence reference or establish a canonical API/schema.

For partial coverage, only returned interval records are included in the totals; the covered interval set and planned interval count remain explicit, with withheld intervals in reasons. Consumers must display the component as scoped to that coverage and must not call the delta savings or a full-period bill result.
