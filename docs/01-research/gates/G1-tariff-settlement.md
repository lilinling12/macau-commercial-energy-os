# G1 Macau Tariff & Settlement Foundation

**Status:** OPEN / economically blocking. G1.1 and G1.2 are recorded complete in the current handoff; applicable bill, demand, tax, settlement and real-customer evidence remains incomplete.
**Purpose:** Establish versioned, effective-dated, source-traceable Macau commercial tariff and settlement semantics so the product can distinguish consumer import cost, producer export revenue and other economic scenarios without inventing bill rules or unsupported credits.
**Authority:** Original G0–G7 research framework; D-001–D-009, D-018, D-020–D-021, D-026–D-028, D-050, D-065, D-073–D-077; current U-001, U-002, U-009–U-011, U-025–U-026 and related contract/site unknowns.
**Boundary:** G1 defines economic semantics and evidence. It does not select a software stack. A verified grid-interconnection/feed-in route does not prove cross-site retail netting; a simulator or synthetic bill does not prove a customer's settlement.

## Research questions

1. Which customer classes, tariff schedules, contracts and regulatory provisions apply to each supply/account/meter topology, and over which effective dates?
2. Which meter/register is authoritative for billed energy and demand; what are units, direction, multipliers, interval boundaries, timezone and missing/correction behavior?
3. What is the exact Pu demand averaging/integration window for applicable customer classes and meter configurations (U-001)?
4. How are energy periods, demand charges, fixed/monthly charges, taxes/installation-use charges, credits, rounding, carry-forward and adjustments calculated and ordered?
5. What real Golden Bill and matching interval/load-profile evidence is available for each representative tariff class, and can the full invoice be reconstructed without unexplained balancing adjustments (U-010)?
6. Which PV/ESS import, self-consumption, export and producer payments are permitted for a specific site, concession/land parcel, contract and account? What project-specific interconnection/approved-capacity constraints apply, what settlement follows, and what remains unknown about cross-site rights (U-002/U-025)?
7. What does the public mismatch in PV installation counts describe—date, installed vs connected/selling system, capacity vs unit count, and reporting scope (U-026)?
8. What meter/AMI data is available to third parties and under what sampling, export, retention, security and commercial terms (U-003)?
9. Which claims are bill-reconstruction results, interval assessments, baseline comparisons, producer export revenue or scenario-only economics, and what evidence is required for each?

## Evidence rules

- Prefer Macau legislation, concession/contract text, official CEM tariffs/bill explanations, utility meter/configuration records, customer contracts and anonymized real bills with matched measurement data.
- Record issuing body, source title/identifier, URL or controlled file reference, publication/effective/retrieval dates, applicable class/topology, exact clause/table/field and claim supported.
- Keep rule validity time distinct from when the platform learned/approved the rule; preserve prior revisions for replay.
- Separate CEM billing-month reads, tariff energy-price periods, meter sample cadence and Pu demand integration interval. Do not substitute one time scale for another.
- Separate consumer import settlement from PV/ESS producer export settlement and site economic roll-up. No implicit import/export netting, remote PV credit, wheeling or third-party PPA treatment.
- Treat unexplained discrepancies as blockers; do not tune a balancing line or rounding behavior to force a match.
- Label public-source statements, derived interpretation, contract-specific facts, customer evidence, simulation and assumptions separately.
- Preserve unresolved semantics as UNKNOWN with fail-closed product behavior; public silence is not proof that a right or rule does not exist.

## Required outputs

1. A tariff/contract applicability matrix by class, account/meter topology, effective date and source.
2. A source-backed rule inventory for units, energy periods, demand, fixed charges, tax/installation-use charges, credits, carry-forward, rounding and adjustments; each rule has provenance, validity and uncertainty.
3. A meter/register semantics record covering boundary, direction, multipliers, cadence, timezone, Pu window, missingness and correction behavior.
4. Distinct versioned calculation definitions for consumer import, PV/ESS producer export and explicitly approved site-economic aggregation; no unsupported cross-site credit.
5. At least two real Golden Bill cases from different tariff classes with matching meter/load-profile evidence, reproducible inputs, expected components and discrepancy analysis.
6. A deterministic bill-reconstruction acceptance report meeting the authority target of no more than 0.5% error and zero unexplained adjustment, with all class-specific exceptions stated.
7. An explicit unresolved-items and fail-closed register, including U-001/U-009/U-010/U-011/U-025/U-026 and any newly found contradictions.
8. Evidence Register, Decision/Open Questions, Tariff & Settlement design and CURRENT updates, plus an owner-reviewed Gate decision.

## Exit criteria

G1 remains OPEN until all applicable criteria are evidenced and reviewed:

- tariff and contract rules are source-backed, applicable to a stated customer class/topology and effective interval;
- the CEM demand window and required meter/register interpretation are evidenced for any claim depending on Pu; no unverified 15-minute default is encoded;
- B/C/D monthly government-tax/installation-use formula is authoritative or explicitly remains unsupported and excluded from bill-grade calculation;
- at least two real Golden Bill cases from different tariff classes are linked to matched measurement evidence and reproduce to ≤0.5% error with zero unexplained adjustment, or the project owner explicitly narrows the G1 scope under a documented decision without claiming broader coverage;
- invoice-level carry-forward/rounding behavior and component calculation order are verified from real evidence where they affect the acceptance result;
- PV/ESS flows and any allocation/credit are supported by the applicable contract, meter and regulatory evidence; otherwise they remain separate/unknown and excluded from customer bill credits;
- source-data access and limitations are explicit for the target pilot; no high-frequency third-party API is presumed from smart-meter deployment or customer app history;
- residual unknowns, exceptions and class exclusions are recorded, and the owner reviews the Gate decision.

A partially scoped pass must name the included customer classes, calculation types and exclusions. It cannot be represented as general Macau commercial tariff closure. G1 research closure is separate from production Tariff Engine acceptance, security review and site pilot validation.

## Current evidence status

- G1.1/G1.2 are recorded complete; this does not close G1 overall.
- Public CEM material partially clarifies amount-due rounding/odd-amount carry-forward (U-011), but calculation order, component rounding, negative adjustments and Golden Bill behavior remain open.
- Public sources reviewed do not specify the CEM Pu integration window (U-001), authoritative B/C/D installation-use/tax formula (U-009), or third-party high-frequency AMI API terms (U-003).
- No real commercial Golden Bill set with matched interval/load-profile evidence is recorded (U-010).
- PV-to-grid interconnection and producer feed-in purchase are documented. The 2025 concession amendment effective 2026-01-01 constrains the private self-generation distribution exception to the same concession/private land parcel with prior written SAR authorization; it does not establish ordinary cross-parcel private bill credits or virtual netting (U-025 remains open).
- CEM and DSPA both report 12 PV systems in the reviewed public sources, but reference dates, installed/connected/selling status, capacity and generation scope remain unreconciled (U-026 partially resolved).

## Related records

- Roadmap WP-1: `docs/00-authority/ROADMAP.md`
- Open Questions and Decisions: `docs/00-authority/decisions/OPEN-QUESTIONS.md`, `docs/00-authority/decisions/DECISIONS.md`
- G1 public billing and demand review: `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`
- G1 PV interconnection and settlement: `docs/01-research/evidence/G1-PV-GRID-INTERCONNECTION-2026-10.md`
- Tariff and settlement detailed design: `docs/03-architecture/detailed-design/TARIFF-SETTLEMENT-DETAILED-DESIGN-v0.1.md`
- Golden Bill criteria: U-010 in `docs/00-authority/decisions/OPEN-QUESTIONS.md`
