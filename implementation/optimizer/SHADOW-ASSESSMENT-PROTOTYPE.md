# SHADOW dispatch assessment prototype

This is a bounded assessment slice for schedules supplied by another component. It does not generate or optimize schedules and has no device-control interface.

## What it checks

- Baseline and candidate use the same contiguous, site-timezone intervals.
- PV generation reconciles to on-site use, export, or curtailment.
- Each interval's AC power balance reconciles.
- Flexible-load power stays inside the supplied asset envelope.
- ESS power, SOC transitions, efficiency, and interval continuity stay inside the supplied limits.
- An optional candidate grid-import guard is respected.
- Economic output is limited to a precisely interval-matched grid-import energy charge and is withheld unless account/meter, contract, tariff, and rate references are marked verified. ESS comparisons also require matching SOC at the schedule-window boundaries.

## What it does not prove

The assessment trusts the caller's `EvidenceRef.state`; it does not retrieve, authenticate, or independently verify the referenced evidence. A `VERIFIED` state in a synthetic input is not proof of a Macau site fact. It does not establish contractual export rights, cross-building settlement, customer tariff applicability, load comfort/service feasibility, demand charges, taxes, export credits, full-bill settlement, forecast quality, optimizer quality, or realized savings. Those remain gated on evidence models, approved contract semantics, and site validation.

This is therefore a code-level SHADOW boundary experiment, not an approved API, production algorithm, G7.9 Step 3 closure, or pilot-readiness claim. Product and production-architecture choices remain subject to owner review.

## Local check

From `implementation/optimizer`, run `PYTHONPATH=src python -m unittest discover -s tests -v`. Project `pyproject.toml` currently requires Python `>=3.14,<3.15`; results on another interpreter are useful development evidence, not target-runtime proof.

