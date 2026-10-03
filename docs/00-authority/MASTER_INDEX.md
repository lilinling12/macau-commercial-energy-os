# Macau Commercial Energy OS Authority Master Index

## Purpose

This is the entry point for project knowledge. The repository's numbered documentation structure follows the original research-to-delivery framework:

Research → Decision → Architecture → Engineering → Implementation.

## Canonical directory structure

- `docs/00-authority/`: project state, roadmap, decisions, open questions and handoff instructions.
- `docs/01-research/`: domain and technology research, research gates, evidence register and source-backed evidence notes.
- `docs/02-product/`: product thesis, customer segments, commercial model, product requirements, MVP definition and pilot design.
- `docs/03-architecture/`: system boundaries and architecture records, including technology selection authority.
- `docs/04-engineering/`: development workflow, module boundaries, AI coding governance and CI/CD.
- `docs/05-mvp/`: executable MVP plans and vertical slices.

## Core planning and continuity documents

- Research-to-delivery Gate sequence and work packets: `docs/00-authority/ROADMAP.md`
- Cross-conversation research/coding continuity: `docs/00-authority/handoff/CONTINUATION-PROTOCOL.md`
- New-conversation entry prompt: `docs/00-authority/handoff/CONTINUE-PROMPT.md`
- Reusable research and coding task packet: `docs/04-engineering/ai-coding-governance/TASK-PACKET-TEMPLATE.md`
- Product design approval and engineering delivery governance (proposed): `docs/04-engineering/PRODUCT-DESIGN-AND-DELIVERY-GOVERNANCE-v0.1.md`
- Research-derived product scope and user workflow: `docs/02-product/PRODUCT-DESIGN.md`
- Product and architecture owner review packet (unapproved; choices and Pro Max synthesis): `docs/02-product/PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md`
- G6.9-R2 Step 3D readiness audit and execution packet (not execution results): `docs/01-research/G6.9-technology-research/STEP-3D-READINESS-AND-EXECUTION-PLAN-v0.1.md`
- G6.9-R2 Step 3D machine-readable runner manifest (draft; pins and freeze blockers, not a runnable Compose environment): `docs/01-research/G6.9-technology-research/STEP-3D-RUNNER-MANIFEST-v0.1.json`
- Research-derived product requirements draft (not customer-approved): `docs/02-product/PRD-v0.1.md`
- Customer discovery and formative usability research protocol (proposed; no sessions conducted): `docs/02-product/CUSTOMER-DISCOVERY-AND-USABILITY-RESEARCH-PLAN-v0.1.md`
- Product information architecture, user flows and screen requirements (draft): `docs/02-product/USER-FLOWS-AND-IA-v0.1.md`
- Clickable HTML product prototype v0.2 (synthetic data; distinct economic result views and review/outcome states, no live control): `docs/02-product/prototype/v0.2/index.html`
- Prior clickable prototype v0.1 (preserved for design history): `docs/02-product/prototype/v0.1/index.html`
- Logical system architecture and technology decision states: `docs/03-architecture/ARCHITECTURE-DESIGN.md`
- VS-001 component-level detailed design draft (shadow-mode; not production authorization): `docs/03-architecture/detailed-design/VS-001-DETAILED-DESIGN-v0.1.md`
- Tariff & Settlement Engine detailed design v0.1 (stack-neutral; G1 blocked; not bill-grade approved): `docs/03-architecture/detailed-design/TARIFF-SETTLEMENT-DETAILED-DESIGN-v0.1.md`
- Energy Graph detailed design v0.1 (stack-neutral; G3/site validation pending): `docs/03-architecture/detailed-design/ENERGY-GRAPH-DETAILED-DESIGN-v0.1.md`
- Telemetry Ingestion & Data Quality detailed design v0.1 (stack-neutral; contract parity and site policies pending): `docs/03-architecture/detailed-design/TELEMETRY-INGESTION-AND-DATA-QUALITY-DETAILED-DESIGN-v0.1.md`
- Recommendation and Operator Review detailed design v0.1 (SHADOW-only lifecycle; no execution authorization): `docs/03-architecture/detailed-design/RECOMMENDATION-AND-OPERATOR-REVIEW-DETAILED-DESIGN-v0.1.md`
- Cost Analysis and Evidence Replay detailed design v0.1 (stack-neutral; G1 and replay acceptance pending): `docs/03-architecture/detailed-design/COST-ANALYSIS-AND-EVIDENCE-REPLAY-DETAILED-DESIGN-v0.1.md`
- Forecasting and Optimization detailed design v0.1 (stack-neutral; G4/G5 open; no model/solver/control decision): `docs/03-architecture/detailed-design/FORECASTING-AND-OPTIMIZATION-DETAILED-DESIGN-v0.1.md`
- Deployment, Operability and Recovery detailed design v0.1 (stack-neutral; deployment mode, SLOs and recovery objectives remain open): `docs/03-architecture/detailed-design/DEPLOYMENT-OPERABILITY-AND-RECOVERY-DETAILED-DESIGN-v0.1.md`
- VS-001 cost-result and replay-manifest contract proposal (not canonical): docs/03-architecture/detailed-design/VS-001-RESULT-AND-REPLAY-CONTRACT-PROPOSAL-v0.1.md
- VS-001 identity and tenant authorization design (draft; provider/roles not selected): docs/03-architecture/detailed-design/VS-001-IDENTITY-AND-TENANT-AUTHORIZATION-DESIGN-v0.1.md
- PRD-to-architecture traceability and design-gap matrix (draft): `docs/03-architecture/detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md`
- Current status and next authorized work: `docs/00-authority/handoff/CURRENT.md`
- G1 CEM billing, demand-window and smart-meter unknown review (2026-10; partial public evidence): `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`
- G2 Macau commercial-load flexibility evidence (public context only; site validation pending): `docs/01-research/evidence/G2-MACAU-COMMERCIAL-LOAD-FLEXIBILITY-EVIDENCE-2026-10.md`

All authoritative project documentation belongs under these six numbered directories. Do not create parallel unnumbered documentation roots under `docs/`. Keep implementation source code in the repository's `implementation/` directory.

## Authority chain

Research → Evidence → Decision → Product / Architecture → Engineering → Implementation → Validation → Handoff.

Every implementation decision must trace to an approved decision and supporting evidence. Research conclusions, assumptions, and unresolved questions must retain their status.

## Rule

When adding or moving documentation, update this index and every affected internal link in the same change.
