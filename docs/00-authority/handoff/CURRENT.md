# CURRENT — Macau Commercial Energy OS

**Snapshot:** 2026-10-04  
**Authority mode:** research-first / evidence-governed  
**Research authority:** Library Research Authority v1.6.2 + G6.9-R2 Step 3C bake-off evidence + Macau PV follow-up D-077/U-025/U-026  
**Repository:** lilinling12/macau-commercial-energy-os

## Project mission

Build a commercial multi-energy orchestration system for Macau commercial buildings and sites. It connects meters, BMS, HVAC/chiller plants, PV, ESS, EV and other flexible loads to physical topology, customer contracts and tariff/settlement rules. It evaluates total economic energy cost/value, recommends safe actions, and preserves evidence for replay and measurement & verification.

This is not a generic energy dashboard, chatbot, BMS replacement, or kWh-only optimizer. Cloud recommendations do not directly control devices; site Edge and the Safety Kernel own command validation and execution. Initial operation remains SHADOW/advisory until evidence and authorization gates are met.

## End-to-end product and delivery objective

The project objective is to complete and validate the product design, complete the evidence-backed technical architecture and detailed designs, implement and verify the MVP, and reach an authorized Macau pilot with measured outcomes and an operational handoff. This is one lifecycle objective, not a claim that planning documents alone constitute completion.

Definition of done spans: customer/problem validation; product requirements and tested workflows; passed domain/safety/technology gates or explicitly bounded pilot limitations; approved architecture and detailed designs; implementation mapped to requirements; security/reliability/acceptance evidence; site authorization; pilot measurement; and an expand/remediate/stop decision.

**Current active delivery record:** PR #8, branch `docs/product-architecture-roadmap` (open, not merged). It contains the research-derived product baseline, PRD draft, logical architecture, research/coding continuity, roadmap, product interaction design draft and clickable prototype, VS-001 detailed-design draft, PRD-to-architecture traceability matrix, expanded G6 evidence/closure checklist, proposed product/engineering governance, an owner review packet with provisional visual directions, and a machine-readable Step 3D runner manifest draft. All remain drafts pending review where applicable. These documents remain drafts; customer validation, complete detailed design, production stack selection, implementation completion, and pilot evidence are outstanding. Changes on this branch are not yet on `main`.

## Research state

- **G1 — Macau Tariff & Settlement Foundation:** OPEN. G1.1/G1.2 completed. CEM's public bill guide partially clarifies amount-due rounding/odd-amount carry-forward (U-011), while Golden Bill validation remains required. Pu interval (U-001), B/C/D tax formula (U-009), real bills (U-010), and cross-site PV rights (U-025) remain open; U-026 tracks an official PV-count discrepancy. CEM reports smart-meter coverage and customer-facing daily history, but third-party high-frequency API access remains unknown (U-003). Evidence: `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`.
- **G6 — Safety & Control:** OPEN / no formal closure evidence recorded. The itemized status and closure checklist is `docs/01-research/gates/G6-safety-control.md`. Required proof includes site-local veto/limits, offline fallback, manual override, authenticated/idempotent commands, audit and replay. U-022 remains OPEN for production signing and Edge key lifecycle; Step-3C semantics do not close this security gate.
- **G6.9-R2 — Technology Stack Bake-off:** Step 3A, 3B and 3C complete; **Step 3D pinned framework-native integration pending**. The v0.3.0 archive contains Step 3C evidence only. Readiness findings and execution requirements are in `docs/01-research/G6.9-technology-research/STEP-3D-READINESS-AND-EXECUTION-PLAN-v0.1.md`; the machine-readable draft `docs/01-research/G6.9-technology-research/STEP-3D-RUNNER-MANIFEST-v0.1.json` is not an executable runner and retains explicit freeze blockers.
- **G7 — Reference Simulator & Pilot Validation:** active in parallel; G7.2 live baseline/no-op still pending; U-017 live response/rebound remains open.
- Research Authority v1.6.2 contains D-001..D-076 and U-001..U-024. Repository follow-up records add D-077 and U-025..U-026; the synced registers now cover D-001..D-077 and U-001..U-026. See the architecture technology-authority, decision, and research evidence documents.
- Official CEM PV material confirms an approved grid-interconnection and feed-in-tariff route. It does **not** establish cross-building virtual netting or a customer's right to claim another building's PV generation; U-025 tracks that question.

## Repository implementation state

Completed on main:
- Authority / handoff / evidence foundation;
- detailed decisions D-001..D-055 and unknowns U-001..U-017;
- Commit 004 Phase A contracts-first foundation;
- Phase B Node/NestJS, Go Edge and Python Optimizer bootstrap;
- Phase C VS-001 domain path, merged via PR #4.

The Phase B Node/NestJS code is an existing implementation path corresponding to Candidate B. It is not evidence that Candidate B won the open G6.9-R2 bake-off. Treat it as provisional until Step 3D evidence and an explicit Decision Record select or revise the production stack.

## Current authority for technical architecture

Product and technology design documents on PR #8 are review drafts. User confirmation is required before product scope, major interaction design, frontend stack, or production architecture is baselined.

The earlier layer summary below is a research-derived provisional proposal, not an owner-approved product or production architecture:
- Frontend: React + TypeScript candidate.
- Application: TypeScript/Go hybrid responsibilities under evaluation.
- Workflow: Temporal candidate.
- Data: PostgreSQL + Timescale evaluation baseline.
- Event: NATS JetStream candidate.
- AI / Optimization: Python responsibility candidate.
- Edge: Go responsibility candidate.
- Future plugin isolation: Wasm/WASI direction candidate.

Each layer and its boundaries require product-owner review before becoming an approved architecture baseline. This summary does not replace the bake-off's topology candidates. C+ (Go authoritative Energy Core + Temporal Go workers + Go Edge/Safety, thin Bun/Hono/TypeScript product surface, Python intelligence) remains a **provisional default**, not a measured winner. A and B remain candidates until the common Step 3D/Step 4 decision rule is satisfied and the resulting decision is reviewed. See D-062..D-076.

## Research sequence and next work

The research-to-delivery chain is:
**Research → Evidence → Decision → Architecture → Engineering → Implementation.**

Immediate work:
1. Continue G1 with authoritative Macau tariff/billing evidence, including U-025 cross-site PV rights and settlement.
2. Execute G6.9-R2 Step 3D in the pinned environment; do not infer a framework winner from Step 3C.
3. Execute G7.2 live baseline/no-op when the pinned BOPTEST runtime is available.
4. Review product scope, user workflows, visual direction, and the technology decision packet with the product owner before treating drafts or candidates as approved baselines; continue user validation in parallel.
5. Extend component-level detailed design beyond VS-001 after product workflows and dependent Gate inputs are validated; close contract gaps and retain unresolved items explicitly.
6. Only then revise technology decisions and authorize dependent production implementation.

### Active design progress on PR #8

- `docs/02-product/USER-FLOWS-AND-IA-v0.1.md` translates PRD PR-01..PR-09 into role hypotheses, information architecture, four primary task flows, nine screen responsibilities, error/unknown/freshness behavior and user-validation criteria. It is explicitly unvalidated; no customer workflow is claimed as confirmed.
- `docs/02-product/CUSTOMER-DISCOVERY-AND-USABILITY-RESEARCH-PLAN-v0.1.md` operationalizes roadmap WP-4 with role/site sampling, a behavior-first interview guide, synthetic-prototype usability tasks, evidence handling and synthesis rules. It is a protocol only: no interviews, artifact reviews or usability sessions have been conducted.
- `docs/02-product/prototype/v0.1/index.html` is a no-framework clickable demo of portfolio/site/data/model/economics/recommendations/evidence views with synthetic data, responsive layout, keyboard-focus support and demo-only local annotations/replay state. It has no runtime/API connection and is not usability-validated.

- `docs/03-architecture/detailed-design/VS-001-DETAILED-DESIGN-v0.1.md` covers the shadow-mode energy intelligence loop, its component boundaries, data/time semantics, failures, evidence/replay, security boundaries, and current contract gaps.
- `docs/03-architecture/detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md` maps all nine PRD requirements to current logical designs/contracts and records a preliminary static source audit of the VS-001/Edge/optimizer scaffold. It identifies gaps and does not claim product implementation completion.
- docs/03-architecture/detailed-design/VS-001-RESULT-AND-REPLAY-CONTRACT-PROPOSAL-v0.1.md proposes technology-neutral cost-result and replay-manifest shapes; it is a reviewable proposal only, not an accepted canonical contract.
- docs/03-architecture/detailed-design/VS-001-IDENTITY-AND-TENANT-AUTHORIZATION-DESIGN-v0.1.md defines a stack-neutral PR-01/G6-09 identity and scope model. It exposes auth guard, service identity, scoped persistence/cache/job and revocation gaps; roles/provider remain undecided.
- The recursive repository tree contains no frontend source/package, database model/migration, command implementation or Safety Kernel runtime package. The platform HTTP controller path has no auth guard wired in AppModule; the health endpoint returns UP without dependency/readiness checks; Edge main only logs bootstrap start. Command arbitration and Safety Kernel currently have principles in README files, not executable modules.
- The real Energy Graph and tariff adapters fail closed, replay uses hard-coded synthetic fixtures, evidence persistence is in-memory, and the Python optimizer is only a data model. VS-001 service tests use static/in-memory fakes; Edge test checks serialization. No tests were run during this static audit.
- These findings show the product implementation is still a scaffold; they do not close G6 or authorize field commands.
- The Step 3D runner manifest records candidate service/runtime pins, five verified Linux/AMD64 registry digest observations, and explicit freeze blockers; remaining unresolved digests stay null, and all captured digests require re-resolution on the frozen runner. It also records the unresolved authority question for adding a shared PG16 Temporal persistence service while preserving the specified PG18 + TimescaleDB application database. `executionReady` remains false. No Compose runner, package lock set, BOPTEST frozen build, Step 3D execution, or comparative results exist yet.
- Authority Validation and Repository Hygiene run on PR updates. Verify both against the exact live PR head before merge; earlier successful runs do not validate later commits.
- Contract authoring/code generation has a new research comparison in the owner review packet: OpenAPI 3.1, JSON Schema 2020-12, and Protobuf remain experiment candidates, not a selected canonical format. The proposed proof is a pinned TypeScript/Go dual-runtime slice covering presence/null, decimal money, formats, evolution, transport mapping, and semantic replay digest; no generator bake-off has run.
- The static PRD-to-architecture audit now records telemetry-consumer parity gaps against D-065: the V1 JSON Schema, hand-maintained TypeScript parser/model and Go Event struct differ in optional fields, unit validation and date-time/unknown-field behavior. This identifies a design gap only; no contract or runtime code was changed and no parity tests were run. Shared fixtures and generated bindings remain Step 3D work after the contract-authority decision.
- The VS-001 CostResult/ReplayManifest proposal has been refined against D-021, D-026, D-065, D-073/D-074 and D-077: consumer settlement and PV producer-export streams are kept distinct, any site-economic roll-up requires an explicit versioned aggregation policy, and result time provenance pins the clock/boundary policy. It remains noncanonical. It also records that RecommendationV1's numeric `estimatedValue` is not authoritative money under D-026 and proposes a non-breaking V2 assessment-reference path, pending owner confirmation of the product meaning (absolute cost versus baseline-relative effect). Source-event identity, decimal grammar/scale/rounding, status roll-up semantics, immutable digest/canonicalization/storage/retention, and contract ownership/code generation remain unresolved.
- Next: review and resolve those remaining contract decisions before creating canonical schemas. Review the tenant authorization design with validated user roles and deployment context before selecting an identity provider or role policy. In parallel, continue G1, G6.9-R2 Step 3D, G7.2 and target-user validation where required inputs are available. Do not implement production adapters until product scope and technology authority are reviewed.

## Suspended implementation gate

The previous “Phase D — Java 25 tariff-core bootstrap” is **SUSPENDED** by D-069 while G6.9-R2 remains open. D-030's tariff semantic architecture remains active, but its Java/Spring implementation choice is not current production authority. Do not start or describe Java Phase D as the next implementation gate absent a completed bake-off or a separately justified, approved decision.

## Non-negotiable open evidence

Do not claim:
- G1 is closed;
- CEM Pu averaging interval is verified;
- cross-site/virtual PV netting is authorized;
- G7.2 live baseline is complete;
- synthetic reference-building results are Macau customer evidence;
- autonomous control is authorized;
- SAT/CHWS perturbations reduce total site power until U-017 is resolved.

## Start here in a new conversation

Read:
1. `AGENTS.md`
2. `docs/00-authority/handoff/README.md`
3. `docs/00-authority/handoff/CURRENT.md`
4. `docs/00-authority/decisions/DECISIONS.md`
5. `docs/00-authority/decisions/OPEN-QUESTIONS.md`
6. `docs/03-architecture/technology-authority/G6.9-technology-selection/README.md`
7. `docs/01-research/evidence/G1-PV-GRID-INTERCONNECTION-2026-10.md`
8. Authority files referenced by the current task.

GitHub live state, exact-head CI, verified evidence, and Decision Records take precedence over chat memory.
