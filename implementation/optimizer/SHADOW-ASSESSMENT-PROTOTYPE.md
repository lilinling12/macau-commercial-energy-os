# SHADOW dispatch assessment prototype

The assessment module validates a schedule supplied by another component. The adjacent `dispatch_optimizer.py` adds an experimental bounded schedule generator over a declared discrete action space. Neither module has a device-control interface.

## What it checks

- Each interval comparison exposes separate baseline and candidate grid import, fixed load, per-asset flexible loads, total load, PV generation/on-site use/export/curtailment, losses, ESS charge/discharge, and ESS boundary SOC when supplied. This is an auditable scenario trace, not evidence that a device is controllable or that the schedule will execute.
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


## PV curtailment evidence gate — 2026-10-05

Candidate-side non-zero PV curtailment now requires an explicit site/inverter capability evidence reference in the bounded assessment request. Missing, unknown or stale evidence marks the physical assessment partial and withholds both the PV-curtailment and overall dispatch-feasibility claims; verified evidence permits only a bounded claim within the supplied assessment. Project-assumption evidence produces a scenario-only result. A candidate with zero declared curtailment does not require this capability evidence. This does not authorize or model a remote curtailment command, prove that a real site can curtail PV, or replace source/evidence authentication. Regression cases cover missing, unknown and stale capability evidence; project-assumption and verified evidence; and the zero-curtailment path. Evidence remains a caller-provided reference/state in this prototype.


## ESS SOC evidence gate — 2026-10-05

Active ESS schedules now also require an explicit evidence reference for the SOC inputs used by the bounded assessment. Missing, UNKNOWN or STALE SOC evidence downgrades the physical result to PARTIAL and withholds ESS-dispatch and overall feasibility claims; PROJECT_ASSUMPTION yields a scenario-only result; VERIFIED supports only the supplied bounded calculation. This evidence reference is distinct from the ESS operating-envelope reference in `EssLimits`. It remains caller-provided and is not authenticated or resolved against a meter/BMS source; per-interval SOC provenance and immutable input snapshot semantics remain open for the production contract.

## Macau B1/C1 interval-rate mapping (bounded addition)

The new `macau_energy_optimizer.macau_tariff_periods` module maps effective-dated, caller-supplied active-energy rate cards into the existing SHADOW optimizer's per-interval rate input. It recognizes the published Macau B1 busy/off-peak windows and C1 low/high-season windows in Asia/Macau time, adds the separately supplied effective-dated tariff-clause adjustment (TCA), and preserves the supplied evidence reference. It refuses naive timestamps, unsupported tariff subclasses, out-of-window intervals, and intervals that straddle midnight or tariff boundaries; callers must split at boundaries first.

This is deliberately limited to B1/C1 interval active-energy pricing. It does not validate that the customer is entitled to the supplied tariff, authenticate rate or TCA evidence, reproduce demand/Pu/Pc charges, B2/B3/C2 transformer losses, reactive energy, tax, PV export/FIT, or a full bill. It does not upgrade the result from the existing `GRID_IMPORT_ENERGY_ONLY` component, and does not imply Macau site truth or equipment control. The test rate cards are synthetic `PROJECT_ASSUMPTION` fixtures.

## Historical Macau B1/C1 bill-component replay

The additional `macau_energy_optimizer.macau_bill_replay` module replays a historical, already-periodized B1/C1 meter-register subtotal: demand charge using the supplied bill-period Pu/Pc and supplied demand weight/rate; active-energy charge by tariff period; reactive charge using the B1/C1 statutory thresholds and direction; and a separate caller-supplied TCA by register block. It preserves evidence references for tariff, contract, demand and register inputs/outputs. It blocks a Pc/Pu contradiction, missing tariff-period buckets, mismatched reactive direction, unsupported tariff variant, an uncovered rate-card billing period, and nonzero C1 seasonal buckets outside that season.

This is a historical subtotal arithmetic function, not candidate-dispatch settlement or a complete bill. Input register values are already classified according to the tariff and read period; the function does not derive them from the source/load schedule or raw meter intervals. Caller-supplied rate values and evidence references are not independently authenticated. Government tax, PV FIT/export settlement, full-bill adjustments/rounding, B2/B3/C2 transformer corrections and real bill reconciliation remain out of scope. Synthetic tests exercise the statutory formulas but do not prove any customer bill. Production remains SHADOW-only.

The formulas are grounded in Articles 8, 9, 13, 15, 16 and 20 of Macau Administrative Regulation 25/2022 and the corresponding parameters in Executive Dispatch 105/2022. Effective legal/customer records must be verified for any real replay:
- [Administrative Regulation 25/2022](https://bo.dsaj.gov.mo/bo/i/2022/26/regadm25_cn.asp)
- [Executive Dispatch 105/2022](https://bo.dsaj.gov.mo/isapi/go.asp?d=despce-105-2022cn)



## Overall versus electrical feasibility

The claim ledger keeps the physical profile and resource electrical-envelope results separate from overall dispatch feasibility. When any flexible-load schedule changes, this prototype has no HVAC comfort/recovery, EV departure-energy, or hot-water service evaluator; therefore `DISPATCH_FEASIBILITY` is WITHHELD with an explicit reason, while an independently qualified electrical profile and per-load envelope claim may remain visible. This matches the PR #10 draft presentation example. It does not implement resource service models or make the product contract canonical.
