# Evidence Register

All important claims and decisions must track evidence status.

Statuses:

- VERIFIED
- DERIVED
- HYPOTHESIS
- PROJECT_ASSUMPTION
- UNKNOWN
- CONTRACT_VERIFIED

Evidence discipline applies to research, architecture and implementation decisions.


## G1 — Macau PV grid interconnection and settlement boundary

- **Claim:** Macau has an approved PV-to-public-grid interconnection and producer-to-CEM feed-in purchase route; the amended electricity concession contract effective 2026-01-01 also recognizes private self-generation distribution only within the same concession/private land parcel with prior written SAR authorization.
- **Status:** VERIFIED for the published regulatory/contract boundary and feed-in mechanism; **UNKNOWN** for cross-parcel private PV allocation, retail bill credits, wheeling, third-party PPA treatment and specific account-linked exceptions.
- **Evidence:** `docs/01-research/evidence/G1-PV-GRID-INTERCONNECTION-2026-10.md`; Official Gazette Series II 49/2025 concession amendment, effective 2026-01-01.
- **Limit:** CEM feed-in revenue belongs to the producer-side export settlement. The concession's SAR-designated offset for public renewable installations is a government/public-infrastructure arrangement; neither establishes a private customer's right to credit another building's PV against its CEM bill. U-025 remains OPEN.

## G2 — Macau commercial load flexibility

- **Claim:** DSEC publishes aggregate establishment electricity use; DSPA documents reported hotel energy-management practices; CEM runs hotel/resort billing-month energy-saving comparisons.
- **Status:** VERIFIED for the cited public context; **UNKNOWN** for site-level flexible kW/kWh, response, duration, comfort/service effects and rebound.
- **Evidence:** `docs/01-research/evidence/G2-MACAU-COMMERCIAL-LOAD-FLEXIBILITY-EVIDENCE-2026-10.md`.
- **Limit:** sector totals, reported measures, annual/billing-month energy comparisons and BOPTEST/R0 do not prove dispatchable Macau site capacity or bill savings. G2 remains OPEN pending site-approved measurement.


## G3 — Energy Digital Twin / Energy Graph

- **Claim:** A logical Energy Graph design can keep physical/electrical topology separate from settlement/economic context, with explicit, versioned links, provenance, temporal validity and fail-closed resolution.
- **Status:** DERIVED as a stack-neutral design proposal from project decisions D-013, D-014, D-020, D-024, D-038–D-040, D-065 and D-077; **not an approved canonical schema or site-validated model**.
- **Evidence:** `docs/03-architecture/detailed-design/ENERGY-GRAPH-DETAILED-DESIGN-v0.1.md`; research scope and closure criteria: `docs/01-research/gates/G3-energy-graph.md`.
- **Unknown:** No Macau pilot site's physical/electrical topology, source-point mapping, meter hierarchy, settlement mapping, or cross-site PV allocation has been validated. U-005/U-016 remain site-evidence dependent; U-025 remains open for cross-site PV rights.
- **Limit:** Existing VS-001 graph adapters are fail-closed/synthetic scaffolding. Public aggregate context, drawings not yet supplied for a selected site, simulation, and the logical design cannot establish a real site's authoritative meter/contract links. Do not claim G3 closure or bill-grade attribution.


## G7 — Reference Simulator & Pilot Validation

- **Claim:** U-013 records a v0.9.0 R0 fixture point set of 182 inputs, 204 measurements and 134 forecast points, with exact fixture hashes said to be in `G7.2-R0-HARNESS-PREFLIGHT.md`.
- **Status:** REPORTED in the Open Questions register; **not independently auditable from the current repository snapshot** because the cited artifact is absent from the PR #8 branch tree. Do not treat the counts/hashes as verified by this repository review.
- **Evidence:** `docs/00-authority/decisions/OPEN-QUESTIONS.md` (U-013) records the assertion; G7 closure requirements: `docs/01-research/gates/G7-pilot-validation.md`.
- **Limit:** G7.2 live baseline/no-op remains pending; U-017 response/rebound, U-012 Macau calibration and U-015 weather validation remain open. No Macau customer pilot or measured customer result is established by the cited fixture assertion. A prior assistant message in the originating conversation also reported G7.1/G7.3/G7.4 research complete, but no underlying sub-gate artifacts were attached or found in the repository; those statuses remain REPORTED / UNVERIFIED pending source recovery.


## G0 — Macau customer/problem and commercial validation

- **Claim:** The current roadmap records the original G0 thesis/market rationale as substantially complete, while direct target-customer, buyer-authority, willingness-to-pay and workflow validation remains outstanding.
- **Status:** REPORTED for prior research rationale; **UNKNOWN / HYPOTHESIS** for validated target-segment demand, buying authority, recurring job, accessible data and commercial commitment.
- **Evidence:** `docs/00-authority/ROADMAP.md`; research-derived product baseline and customer discovery protocol in `docs/02-product/PRODUCT-DESIGN.md` and `docs/02-product/CUSTOMER-DISCOVERY-AND-USABILITY-RESEARCH-PLAN-v0.1.md`.
- **Limit:** Public aggregate energy statistics and concept/prototype reactions do not establish customer pain, purchase intent or willingness to pay. G0's current “substantially complete” label does not mean the product thesis is customer validated.

## G1 — CEM billing and demand-rule evidence

- **Claim:** Public CEM material partially documents payable-amount rounding/odd-amount carry-forward and defines high-level tariff/billing descriptions; reviewed public material does not settle Pu's numeric integration window or the B/C/D monthly installation-use charge formula.
- **Status:** PARTIALLY VERIFIED for the public statements recorded in the G1 evidence note; **UNKNOWN** for calculation order, real Golden Bill behavior, U-001, U-009 and third-party high-frequency data access (U-003).
- **Evidence:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`; corresponding Open Questions U-001/U-003/U-009/U-010/U-011.
- **Limit:** No matched real Golden Bill + interval/load-profile set is recorded. G1 remains OPEN; do not claim bill-grade reconstruction or hard-code a demand interval/tax formula.


## G6.9-R2 — Technology stack bake-off

- **Claim:** Steps 3A–3C are recorded complete; Step 3C contains semantic vertical-slice evidence but did not run the candidate frameworks with the common shared-service environment or produce comparable performance/AI-engineering results.
- **Status:** REPORTED by the G6.9 authority and reviewed archives; Step 3D is **NOT EXECUTED**, Step 4 is **PENDING**, and no measured production-stack winner exists.
- **Evidence:** `docs/03-architecture/technology-authority/G6.9-technology-selection/README.md`; `docs/01-research/G6.9-technology-research/STEP-3D-READINESS-AND-EXECUTION-PLAN-v0.1.md`; draft runner blockers in `STEP-3D-RUNNER-MANIFEST-v0.1.json`; user-provided v0.2.0/v0.3.0 archive audit recorded in the readiness plan.
- **Limit:** Included archive validators check selected pack structure/JSON/hash outputs; they do not execute the applications. Step 3C is not Step 3D, a performance bake-off, a safety certification or production approval. C+ remains provisional; Node/NestJS remains an existing candidate implementation path; Java implementation is suspended by D-069.
