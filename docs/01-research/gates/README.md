# Research Gates

## Domain and delivery research sequence

The original domain research framework is G0–G7. Each Gate requires evidence provenance, explicit unknowns, a reviewed decision, and a handoff. Gate status is controlled by its individual record and the current authority snapshot.

| Gate | Current state | Gate record |
|---|---|---|
| G0 Thesis & Market Rationale | Substantially complete for the original research rationale; customer/problem and commercial validation remain open. | [G0](G0-thesis.md) |
| G1 Tariff & Settlement Foundation | OPEN; Golden Bills and material tariff/settlement unknowns remain. | [G1](G1-tariff-settlement.md) |

G1 evidence acquisition packet (prepared only; unsent): [U-001/U-009/U-010/U-011 request and sufficiency plan](G1-EVIDENCE-ACQUISITION-PACKET-v0.1.md).
| G2 Commercial Load Flexibility | OPEN; public context exists, site-level flexibility is not validated. | [G2](G2-load-flexibility.md) |
| G3 Energy Digital Twin / Energy Graph | OPEN; logical design exists, pilot-site graph is not validated. | [G3](G3-energy-graph.md) |
| G4 Forecasting | OPEN; no eligible Macau dataset and Gate evaluation is recorded. | [G4](G4-forecasting.md) |
| G5 Optimization | OPEN; no reproducible Gate-closing candidate-vs-baseline evidence. | [G5](G5-optimization.md) |
| G6 Safety & Control | OPEN; production safety, command signing and Edge key lifecycle remain unproven. | [G6](G6-safety-control.md) |
| G7 Reference Simulator & Pilot Validation | ACTIVE / INCOMPLETE; live R0 baseline/no-op pending; U-013 preflight artifact gap and U-017 response/rebound open. | [G7](G7-pilot-validation.md) |

## Cross-cutting technology research: G6.9-R2

G6.9-R2 is a parallel technology bake-off that constrains production runtime selection; it does not replace or reorder domain Gates G0–G7 and does not decide product semantics.

- **Step 3A–3C:** recorded complete in the technology authority; Step 3C provides semantic-slice evidence only.
- **Step 3D:** pinned framework-native integration and shared-service failure testing are pending; the current readiness plan records runner and authority blockers.
- **Step 4:** comparative evaluation and production technology decision remain pending. There is no measured winner; C+ is only the provisional default hypothesis.
- Authoritative status and candidates: [G6.9 technology-selection authority](../../03-architecture/technology-authority/G6.9-technology-selection/README.md).
- Step 3D readiness and execution packet: [readiness plan](../G6.9-technology-research/STEP-3D-READINESS-AND-EXECUTION-PLAN-v0.1.md) and [draft runner manifest](../G6.9-technology-research/STEP-3D-RUNNER-MANIFEST-v0.1.json).

A green documentation workflow, a pack-only archive validator, or Step 3C semantic result does not close G6.9-R2 Step 3D/4 or select the production stack.

## Reporting rule

For each Gate update, record: the question, evidence/provenance and class, finding, decision/approver, unresolved items, product/architecture impact, files updated, and next dependency-ready work. Do not mark a Gate complete because a design, plan or test harness exists; require its stated exit evidence.
