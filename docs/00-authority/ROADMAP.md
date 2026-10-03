# Research-to-Delivery Roadmap

**Authority baseline:** Original G0–G7 Research Gates, Library Research Authority v1.6.2, G6.9-R2 bake-off authority, and current repository handoff.  
**Status date:** 2026-10-03  
**Purpose:** Turn the research framework into a traceable sequence of evidence, decisions, product design, architecture, engineering, MVP, and pilot work. This roadmap organizes existing authority; it does not close a Gate or select a technology stack.

## Project objective

Deliver a Macau commercial-building Energy OS that connects metering, building systems, assets, site topology, customer contracts, and tariff/settlement rules. It should explain economic energy performance, produce safe optimization recommendations, and preserve evidence for replay and measurement and verification.

The first product validates an intelligence loop in shadow/advisory mode. It is not a BMS replacement, a generic dashboard, or an autonomous controller.

## Current verified position

- **G0 — Thesis & Market Rationale:** substantially complete in the original gate register; customer and willingness-to-pay evidence remains a product validation activity.
- **G1 — Macau Tariff & Settlement Foundation:** OPEN. G1.1/G1.2 are complete, but blocking Macau billing and settlement questions remain, including U-001, U-009, U-010, U-011, U-025, and U-026.
- **G2–G6:** defined as research gates. The current handoff does not claim that each gate has passed; their evidence and closure records must be checked before dependent production claims.
- **G6.9-R2 — Technology Stack Bake-off:** Steps 3A–3C complete; pinned framework-native Step 3D pending. C+ is a provisional default, not a measured winner. Step 4 selection follows comparable candidate evidence.
- **G7 — Reference Simulator & Pilot Validation:** active in parallel. G7.2 live baseline/no-op remains pending; U-017 live response and rebound remains open.
- **Repository structure:** the numbered documentation structure is in place. Existing Node/NestJS code is Candidate B implementation evidence only; it does not close the bake-off.

See `docs/00-authority/handoff/CURRENT.md` and the individual Gate records for the authoritative status.

## Gate plan

Gate exit criteria below are execution checks derived from the research objectives. Where Library authority already supplies a numeric or hard criterion, that criterion remains controlling. A gate may only be marked complete when its evidence and decision are recorded in the Authority registers and CURRENT snapshot.

| Gate | Research question and required result | Dependency / status |
|---|---|---|
| **G0 Thesis & Market Rationale** | Confirm the Macau commercial-energy problem, target buyer, economic pain, and why an Energy OS is needed. Preserve assumptions separately from customer evidence. | Substantially complete; continue customer discovery alongside G1. |
| **G1 Tariff & Settlement** | Resolve applicable tariff/contract/measurement rules; obtain at least two real Golden Bill cases; reconstruct bills to the Authority target of ≤0.5% with zero unexplained adjustment; register contract-specific exceptions. | OPEN and economically blocking. Complete before claiming bill-grade savings or closing settlement semantics. |
| **G2 Commercial Load Flexibility** | For each in-scope asset, document response speed, duration, operating constraints, comfort/SLA effects, rebound, controllability, and the economic mechanism, with source or site evidence. | Evidence needed before assigning realizable flexibility value. |
| **G3 Energy Digital Twin / Energy Graph** | Demonstrate linked Physical, Electrical Topology, Settlement, and Economic Twins with stable identity, provenance, effective dating, tenant/site boundaries, and explicit mappings between measured and settled quantities. | Depends on asset and settlement evidence from G1/G2; schema may evolve while unknowns remain explicit. |
| **G4 Forecasting** | Define load/cooling/PV/occupancy/EV/Pu-risk forecasts only where data supports them; evaluate errors by economic impact and decision usefulness, not generic ML scores alone. | Requires G1 tariff semantics and G2/G3 data definitions. |
| **G5 Optimization** | Define day-ahead (24–48 h), intraday (5–15 min receding horizon), and local fast-limit responsibilities; compare recommendations against a reproducible baseline and account for uncertainty and constraints. | Requires G1–G4 outputs; begin in simulation/shadow mode. |
| **G6 Safety & Control** | Verify policy evaluation, Safety Kernel veto, site-local limits, offline fallback, manual override, authenticated/idempotent commands, audit, and replay. AI/optimizer may propose but cannot bypass safety authority. | Required before any controlled deployment; autonomous control is not authorized by the MVP. |
| **G7 Simulator & Pilot Validation** | Validate reference cases and attribution; distinguish simulation evidence from Macau-site evidence. For live R0, complete the required fresh baselines and no-op identity trajectory before interpreting control response. | Parallel workstream. G7.2 remains pending; U-017 must be resolved for SAT/CHWS response and rebound claims. |
| **G6.9-R2 Technology Bake-off** | Execute pinned, framework-native Candidate A/B/C+ integrations on common contracts and shared services; inject workflow/worker, broker, database, and Edge failures; gather comparable reliability, performance, and controlled AI-engineering-task evidence. Apply hard safety gates before the published decision rule. | Parallel technical workstream. Step 3D pending; Step 4 decision only after comparable results. |

### Cross-gate execution order

1. Keep G0 customer validation active while closing **G1** billing and settlement blockers.
2. Collect **G2** asset-flexibility evidence and refine **G3** Energy Graph semantics; do not encode unsupported Macau assumptions as defaults.
3. Use stable G1–G3 contracts/data to complete **G4** forecasting and **G5** shadow optimization.
4. Complete **G6** safety proof before enabling any field command path.
5. Run **G7** reference simulation and live pilot evidence in parallel where prerequisites permit; keep simulated and live evidence separate.
6. Run **G6.9-R2 Step 3D/4** in parallel with domain research. A stack decision may change implementation boundaries, not domain semantics.
7. Convert only passed and approved Gate outputs into product scope, architecture decisions, engineering tasks, and implementation.

## Product and architecture design deliverables

- Product definition: `docs/02-product/PRODUCT-DESIGN.md`
- Logical system architecture and technology decision states: `docs/03-architecture/ARCHITECTURE-DESIGN.md`
- Gate-specific evidence and outcomes: `docs/01-research/gates/`
- Single current handoff and next task: `docs/00-authority/handoff/CURRENT.md`

The product and architecture documents distinguish confirmed research from hypotheses and provisional technology candidates. They do not claim the UI has been usability-tested or that a production stack has been selected.

## Next work packets

### WP-1 — Close G1 evidence blockers
Obtain authoritative tariff and meter-window answers, anonymized real bills with matching meter data, tax/rounding rules, and written clarification for cross-site PV settlement and the official PV-count discrepancy. Update U-items, evidence register, tariff rules, and Golden Bill fixtures. Do not recognize remote PV generation as a customer's bill credit without contractual and settlement evidence.

### WP-2 — Execute G6.9-R2 Step 3D and Step 4
Build the pinned Linux x86-64 environment and run Candidate A/B/C+ with the same contracts and workload. Record exact versions, commands, raw results, failures, retries, and reviewer judgments. Do not call a winner until all hard gates pass and the authority decision rule is met.

### WP-3 — Advance G7.2 live R0 safely
Complete the required fresh live baseline runs and live no-op identity trajectory with approved point bindings, run manifest, telemetry quality, and site authorization. Keep SAT/CHWS response and rebound claims open until U-017 is resolved.

### WP-4 — Complete domain and product validation
Use G2/G3 evidence to refine in-scope assets and customer workflows. Validate the proposed primary user tasks with Macau building operators and finance/energy stakeholders before treating navigation or segment priority as final.

### WP-5 — Authorize implementation by Gate
Only after relevant research and architecture decisions pass, create implementation work packets tied to an approved Decision Record, contracts, acceptance evidence, rollback behavior, and explicit scope. Keep the existing Node/NestJS path replaceable until the bake-off decision.

## Gate reporting standard

Every Gate update must state: (1) question researched, (2) evidence and provenance, (3) changed conclusions, (4) decision and approver, (5) unresolved questions, (6) product/model/architecture impact, (7) Authority files updated, and (8) next dependency-ready Gate or work packet.
