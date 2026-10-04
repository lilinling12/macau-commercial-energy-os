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

