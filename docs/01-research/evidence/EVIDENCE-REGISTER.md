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
