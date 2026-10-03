# Implementation

This tree contains executable product code and machine-readable contracts.

It is downstream of repository Authority. Implementation must not redefine research, tariff semantics, safety boundaries, or evidence status.

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
