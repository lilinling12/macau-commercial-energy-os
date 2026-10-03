# G1 Evidence Acquisition Packet v0.1

**Status:** Prepared request/collection plan; not sent to CEM or a customer.  
**Gate:** G1 — Macau Tariff & Settlement Foundation  
**Purpose:** Turn the outstanding demand-window, monthly-charge and Golden Bill unknowns into bounded, auditable evidence requests. This packet does not assert that evidence is available and does not close G1.

## Handling rules

- Obtain the site/customer's authorization before requesting or receiving account-level bills, meter records, contracts or operational data.
- Do not put unredacted bills, account numbers, customer names, addresses, contact details, meter serial numbers, credentials or raw interval data in this public repository.
- Use a random evidence-case identifier. Keep any re-identification key separately under the data owner's access controls.
- Redact only after preserving the authorized source in an approved restricted store. Record source filename, owner, received date, effective period, redaction status and SHA-256 digest in the private evidence manifest; store no identifying metadata here.
- Keep the original and normalized/derived records separate. Document every transformation, unit conversion, timezone interpretation and correction. Never adjust a balancing line to force a bill match.
- If a source is unavailable, refused or incomplete, record that as a limitation. Do not infer a tariff rule from silence.

## Request bundle A — Pu demand measurement (U-001)

Request one matching B/C/D customer-period sample that includes:

1. Tariff group and subgroup (B1/B2/B3, C1/C2 or D), supply voltage, billing-period start/end, and effective tariff version.
2. Meter model/register type and the relevant demand-register configuration; account for any CT/PT multiplier and engineering-unit conversion.
3. The measured-demand averaging duration, fixed/block versus rolling window, interval boundary/clock convention, and the rule for selecting the billing-period maximum.
4. Register timestamp/timezone, reset or billing-period boundary behavior, missing/invalid interval handling, and any corrected or estimated readings.
5. The billed Pu value and its timestamp, if shown or available; a matched interval/load profile covering the complete billed period.
6. CEM written confirmation or an authoritative meter/configuration record that ties the stated interval to the applicable tariff class and meter/register.

**Sufficient to resolve U-001 for a scope:** an authoritative interval definition tied to a stated class and meter/register, plus matched data that can reproduce the billed maximum within documented precision. A generic meter sampling cadence, monthly bill period, tariff clock band, app daily summary, or assumed 15-minute interval is insufficient.

## Request bundle B — monthly installation-use charge (U-009)

Request for each included B/C/D class:

1. Exact invoice line label(s), billed amount and applicable billing period from an anonymized bill.
2. The current legal, concession, supply-contract or CEM tariff-specification basis, including exact instrument/clause, version and effective date.
3. The complete calculation rule: input fields, class/installation type, formula, unit, tiers/caps/floors, proration, rounding, exceptions and treatment of account/topology changes.
4. At least one worked example whose source inputs and resulting line amount can be independently recalculated.
5. Confirmation whether the Chinese “政府稅” and Portuguese “Taxa de Exploração” refer to the same charge for the sampled class and period.

**Sufficient to resolve U-009 for a scope:** an authoritative current instrument or written CEM billing specification establishing both the basis and full formula, reconciled against an anonymized bill. The historical A-group formula, an A/EV example, a label translation, or an unexplained bill amount is insufficient. If no basis/formula is provided, leave the line UNKNOWN and exclude it from bill-grade totals.

## Request bundle C — Golden Bill cases (U-010/U-011)

For at least two different tariff classes, request one complete anonymized bill and its matching measurement evidence for the same account and billing period:

- Full bill pages, all component lines, tariff/subgroup, billing dates, meter readings, billed Pu/Pc, active/reactive energy and time-of-use buckets where applicable.
- Effective unit rates, tariff-adjustment clause value, monthly installation-use line, subsidy/credit, carry-forward, rounding and amount due.
- Matched meter/load-profile data and register metadata sufficient to reproduce the billed energy and demand components.
- Contract or CEM records needed to explain topology-dependent multipliers/loss factors or special terms.
- A source explanation for corrections, estimated readings, credits/refunds, negative adjustments or unusual carry-forward balances.

**Acceptance procedure:** pin the evidence case and tariff version; parse inputs without changing source values; independently calculate each supported component; reconcile line by line and invoice total; report both absolute and percentage error, precision/rounding policy and every residual. G1's current target is ≤0.5% invoice reconstruction error with zero unexplained balancing adjustment. A case lacking matching measurements is contextual evidence, not a Golden Bill.

## Evidence register record

For each artifact, capture privately:

- Evidence ID; question(s) addressed; source/issuer and exact document or register identifier.
- Owner authorization and permitted use; restricted storage reference; redaction status and digest.
- Customer class, meter/topology scope and effective/billing period.
- Received date, original timezone/units, transformations and reviewer.
- Claim supported, confidence/limitations, and whether the evidence is public, contractual, customer-provided, measured or derived.

Only sanitized claim summaries and non-identifying source references belong in the public Evidence Register.

## Execution sequence and decisions

1. Product owner authorizes whether to pursue CEM clarification and/or a consenting pilot customer; this packet itself sends no request.
2. Confirm the approved secure intake location and retention/access rules before accepting private evidence.
3. Request bundles A and B first because U-001/U-009 block tariff semantics; collect bundle C only with matching records and permission.
4. Review the records with the tariff owner, update U-001/U-009/U-010/U-011, the evidence note and Tariff & Settlement detailed design.
5. Keep G1 OPEN until its exit criteria are met and the owner records a Gate decision.

## Current known boundary

Public CEM B/C/D tariff pages describe Pu as the highest measured demand within the billing period but do not state the numeric integration window. CEM identifies the monthly installation-use line but does not publish its B/C/D formula. These public-source findings do not replace the request bundles or establish bill-grade reconstruction. See `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`, `docs/00-authority/decisions/OPEN-QUESTIONS.md`, and `docs/01-research/gates/G1-tariff-settlement.md`.
