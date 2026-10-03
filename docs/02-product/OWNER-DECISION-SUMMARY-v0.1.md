# Owner Decision Summary v0.1

**Status:** Review aid only; no owner decisions are recorded by this document.  
**Prepared:** 2026-10-04  
**Purpose:** Make the next product and architecture review actionable. Research findings and proposals remain in their source documents.

## Confirmed process constraints

The product, interaction design, technical architecture, and detailed designs must be reviewed with the product owner before they become approved baselines. Use UI/UX Pro Max as a design reference, alongside mature product and accessibility practice; validate the resulting workflows with target users. Engineering must follow governed, traceable delivery. These process constraints do not approve a product scope, framework, or production stack.

## Decisions to review

| Decision | Current recommendation / question | What the decision unlocks |
|---|---|---|
| **1. Initial product promise** | **Starting hypothesis:** traceable energy-cost intelligence, explainable SHADOW recommendations, and replayable evidence. Alternatives: begin with cost/bill analysis only; or continue discovery before fixing a promise. | Focused PRD, workflow validation, and MVP acceptance criteria. |
| **2. Lead user and pilot site** | Which role should lead discovery (facilities/energy manager, finance/asset owner, site operator, or another role), and which site type should anchor the first workflow? Public context: Q2 2026 CEM commercial sales were 1,059 GWh (~63.5% of sales); DSEC reports 147 lodging establishments, ~45,000 rooms and 89.4% occupancy for 2025; CEM's hotel/resort energy-saving program uses a 1,600 kVA segmentation threshold. These are aggregate scale/program figures, not building energy or flexibility evidence; segment rankings remain unvalidated. See G2 evidence note. | Recruitment criteria and prototype usability tasks. |
| **3. Visual direction** | **Working recommendation:** prototype A (clear operational workspace) as the baseline; use C (expressive layering) only where it improves orientation, and keep B (dark operations console) as a user-testable alternative. This is not a frozen visual system. | Focused design iteration and usability comparison; final direction follows owner review and target-user evidence. |
| **4. Initial PV boundary** | **Evidence-safe starting scope:** one site, with documented site-use rights, interconnection/export arrangement, and separate producer/export and consumer/import settlement records. Should this be the initial scope, or should PV be excluded until a specific site's rights and settlement evidence are available? Do not assume another building's generation credits a consumer account. | Energy Graph and Tariff & Settlement acceptance scope. U-025 remains open for broader cross-site rights. |
| **5. Step 3D UI comparison boundary** | **Recommendation:** run equal UI-contract, API, and live-stream checks across candidates; exclude browser rendering/React from the stack score and clarify C+'s BFF/UI scope. Alternative: amend the bake-off pack to add equivalent browser workflows and score UI effort separately. | Freeze the comparative experiment's scope. This is an experiment decision, not a frontend or production-stack selection. |
| **6. Step 3D Temporal test persistence** | Approve one shared **test-only PostgreSQL 16** service for Temporal across candidates, alongside the pack's PostgreSQL 18 + TimescaleDB application service; or require another Temporal persistence configuration to be validated before runner freeze. | Freeze the runner's service topology. This does not decide production database architecture. |

## Recommendation versus approval

The recommendations above are research-based proposals to make review concrete. They do **not** record approval. In particular:

- React + TypeScript remains provisional; Next.js is not approved.
- TypeScript/Go responsibilities, Temporal, PostgreSQL + Timescale, NATS JetStream, Python, Go Edge, and Wasm/WASI retain the candidate status recorded in the authority documents.
- C+ remains provisional; no G6.9-R2 winner exists. Step 3D has not run.
- The detailed designs are review drafts. G1, G3, G6, G6.9-R2 Step 3D/4, and G7 evidence remains open or incomplete as recorded in `CURRENT.md`.
- Nothing here approves autonomous device control, bill-grade claims, cross-site PV crediting, a deployment mode, visual system, or production implementation.

## After owner review

Record accepted product choices in the PRD and decision register; update the discovery/usability plan and test the chosen workflows with target users. Record the Step 3D scope and runner-service choice in its readiness plan and manifest, clear the remaining environment/lock/build blockers, then execute the bake-off. Review its evidence before recording any technology decision. Complete and approve the dependent detailed designs, map implementation slices to those designs and acceptance evidence, and proceed through safety, site-authorization, pilot-measurement, and operational-handoff gates.

## Source documents

- Product and architecture review packet: `docs/02-product/PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md`
- G2 official commercial-sales, hotel-scale, and site-flexibility evidence (aggregate only; no site profiles): `docs/01-research/evidence/G2-MACAU-COMMERCIAL-LOAD-FLEXIBILITY-EVIDENCE-2026-10.md`
- Product requirements: `docs/02-product/PRD-v0.1.md`
- Discovery and usability protocol: `docs/02-product/CUSTOMER-DISCOVERY-AND-USABILITY-RESEARCH-PLAN-v0.1.md`
- Step 3D readiness and execution plan: `docs/01-research/G6.9-technology-research/STEP-3D-READINESS-AND-EXECUTION-PLAN-v0.1.md`
- Current authority and lifecycle status: `docs/00-authority/handoff/CURRENT.md`
- Full roadmap: `docs/00-authority/ROADMAP.md`
