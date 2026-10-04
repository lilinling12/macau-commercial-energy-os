# Implementation

This tree contains executable product code and machine-readable contracts.

It is downstream of repository Authority. Implementation must not redefine research, tariff semantics, safety boundaries, or evidence status.

**Maturity and architecture boundary:** This tree currently contains scaffolds and limited vertical-slice artifacts; it is not an accepted MVP. Module languages and frameworks describe existing candidate code or proposed responsibilities, not an approved production architecture. The project-layer proposal and G6.9-R2 A/B/C+ topologies remain provisional; Step 3D is not executed and Step 4 is pending. See `docs/03-architecture/technology-authority/G6.9-technology-selection/README.md` and the owner review packet before treating any stack as selected.

## Modules

- `contracts/` — versioned cross-module contracts and schemas.
- `platform-api/` — control plane and enterprise application boundary.
- `edge-runtime/` — site/edge data-plane boundary.
- `optimizer/` — forecasting, simulation, and optimization shadow-mode boundary.
- `simulator/` — reference-system, replay, and regression boundary.

## First vertical slice

Telemetry
→ Energy Graph
→ Tariff Resolution
→ Cost Analysis
→ Optimization Recommendation
→ Evidence Record

See `docs/05-mvp/vertical-slices/VS-001-energy-intelligence-loop.md`.

## Non-negotiable constraints

- G1 remains open; unknown Macau settlement semantics must fail closed.
- G7.2 live R0 execution remains pending.
- No safety-critical autonomous control in the first slice.
- Optimizer output is advisory unless it passes the governed command path.
- PROJECT_ASSUMPTION must never be represented as VERIFIED evidence.
