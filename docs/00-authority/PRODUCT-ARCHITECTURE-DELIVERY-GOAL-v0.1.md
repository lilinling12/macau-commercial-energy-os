# Product, Architecture and Delivery Goal Charter v0.1

**Status:** Active lifecycle goal; owner confirmed continuation on 2026-10-04. Product scope, UX baseline, and production architecture still require separate owner decisions.
**Prepared:** 2026-10-04
**Authority:** Original G0–G7 research framework, G6.9-R2 technology authority, current Decision Records, product/architecture review packet, and delivery governance.
**Purpose:** Define the project end state and evidence required to call the product-design-to-pilot lifecycle complete. The owner has instructed that work continue under this full lifecycle goal. This confirms the goal and its tracking boundary; it does not approve product scope, close a Gate, select a production stack, or authorize implementation/deployment decisions that have separate approval boundaries.

## Goal

Complete a Macau commercial-energy product that has a validated product definition and user experience, an owner-approved evidence-backed technical architecture and detailed designs, an implemented and verified MVP, and a site-authorized pilot with measured results and an operational handoff.

The current first-release hypothesis is an explainable, evidence-traceable energy-intelligence workflow operating in SHADOW/advisory mode. The product promise, lead user/site, MVP boundary, user experience, and production architecture remain subject to owner review and customer/site evidence. No autonomous device control is implied.

## Completion evidence

The goal is complete only when all applicable items below have reviewable, current evidence linked from the Authority records.

1. **Problem and customer validation**
   - Named target users, buyer, high-value job, site context, operating constraints and integration burden are supported by Macau customer/site evidence.
   - Willingness-to-pay or an explicitly approved alternative commercial validation outcome is recorded.
   - Hypotheses, sample limits and unresolved questions remain visible.

2. **Approved product design**
   - The owner approves product promise, MVP scope/non-goals, lead workflow, user roles/permissions, primary navigation and decision semantics.
   - PRD requirements have observable acceptance criteria and trace to user evidence, screens/flows, detailed designs, implementation slices and validation.
   - UI/UX Pro Max findings are evaluated against actual users, mature product practice, responsive behavior and accessibility; the chosen design is not treated as approved until owner review.
   - Representative users complete the critical workflows with recorded usability findings and unresolved problems.

3. **Evidence-backed architecture**
   - G1–G7 and G6.9-R2 evidence is either passed for the declared product scope or explicitly bounded with owner-approved limitations and safe fallbacks.
   - G6.9-R2 Step 3D/4 produces comparable evidence and a recorded technology decision before production stack selection.
   - The owner approves the logical/physical architecture, trust and tenant boundaries, deployment model and consequential technology decisions through linked ADRs/Decision Records.
   - Provisional candidates—including React + TypeScript, TypeScript/Go responsibilities, Temporal, PostgreSQL + Timescale, NATS JetStream, Python, Go Edge and Wasm/WASI—remain proposals until that decision; Next.js is not selected by this charter.

4. **Complete detailed design**
   - Every approved MVP user journey has component-level design for APIs/events/data ownership, identity/authorization, persistence/migrations, state transitions, errors, retries/recovery, security, observability, deployment, backup/restore, release/rollback and operations.
   - Contracts, threat scenarios and verification evidence are versioned and traceable to approved requirements and architecture decisions.
   - Open Gate evidence and design limitations are reflected in implementation readiness; unsupported bill-grade, savings, PV-credit or control claims fail closed.

5. **Implemented and verified MVP**
   - All approved MVP vertical slices work end-to-end against approved contracts and architecture, with required positive, negative, authorization/isolation, failure and recovery evidence.
   - Product, architecture, security and operational acceptance criteria are met for the declared scope; application checks are recorded against the exact reviewed source revision.
   - The MVP preserves SHADOW/advisory boundaries unless separately authorized control scope passes G6 and receives explicit site/customer approval.

6. **Authorized pilot and handoff**
   - A named Macau site/customer approves scope, data access, measurement, operational roles and support/recovery arrangements.
   - Baseline, data quality, outcome method, confounders, privacy/data-flow review and applicable safety requirements are accepted before pilot execution.
   - Pilot evidence separates simulation from live site results and modeled effects from measured outcomes.
   - Owner/customer records an expand, remediate or stop decision; runbooks, known limits, rollback/recovery and operational ownership are accepted.

A green CI run, prototype, research memo, architecture draft, bake-off manifest, simulator result or passing isolated slice is evidence only for the claims it directly validates. None alone satisfies the complete goal.

## Delivery stages and decision boundaries

| Stage | Work and exit evidence | Owner decision boundary |
|---|---|---|
| 0. Authority and goal baseline | Reconcile original research authority, current repository state, open Gates/questions, and this completion checklist. The owner confirmed continuation under the lifecycle goal on 2026-10-04. | Amend the full goal or add scope constraints if needed; this does not approve downstream product or architecture decisions. |
| 1. Research and discovery | Progress G0–G7 evidence, customer discovery, site evidence preparation and technology research in parallel when dependencies permit. | Authorize contacts, customer/site data intake and site-specific measurement where required. |
| 2. Product definition and UX | Validate roles/jobs; review PRD, workflows, visual direction and prototype; record usability evidence and product acceptance criteria. | Approve product promise, MVP boundary, roles/flows and major interaction/visual decisions. |
| 3. Architecture and technology | Complete G6.9-R2 Step 3D/4; compare evidence; resolve cross-cutting boundaries and record ADRs. | Approve the production architecture and consequential technology choices after evidence review. |
| 4. Detailed design and readiness | Complete designs for each approved MVP path; close contract, security, data-governance and operational readiness gaps. | Approve designs that establish user-visible, security, data or operational policy. |
| 5. Implementation and verification | Deliver governed, traceable vertical slices; verify application behavior and update Gate, traceability and handoff evidence. | Review scope-changing or risk-accepting changes; accept release readiness. |
| 6. Pilot and operational handoff | Execute only the authorized pilot scope, measure outcomes, review incidents/limits and complete handoff. | Authorize deployment/pilot and decide expand, remediate or stop. |

A decision may be explicitly deferred with its evidence dependency and safe work boundary. Silence is not approval. Work may proceed in parallel only when it does not depend on an unresolved owner decision or missing Gate evidence.

## Current state and next dependency-ready work

At preparation, the repository contains research-derived product and PRD drafts, prototype v0.6, stack-neutral logical/detailed-design drafts, a vertical-slice plan and an implementation-readiness audit. The owner decision packet remains unanswered; G1–G7 are open/incomplete as recorded in CURRENT; G6.9-R2 Step 3D has not run; no production stack is selected; the codebase is a partial scaffold rather than a complete MVP; and no customer/site pilot evidence is recorded.

Next sequence:
1. Continue refining the PRD and user flows against the current evidence-backed product hypothesis; label assumptions, alternatives and unresolved choices. Keep these as review drafts rather than treating silence as approval.
2. Continue independent domain evidence work and prepare customer research. Obtain explicit authorization before contacting participants or receiving customer/site data.
3. Present the concrete PRD, flows and prototype for owner review, then validate with authorized target users. Record approval before baselining product scope or starting dependent implementation.
4. Freeze and execute Step 3D only after its manifest blockers and runner trust boundary are resolved; review results before any production technology decision.
5. Complete owner-approved detailed designs, then implement only dependency-ready slices through governed task packets.
6. Verify pilot prerequisites and obtain site/customer authorization before any live deployment.

## Current authority links

- Research-to-delivery stages and work packets: `docs/00-authority/ROADMAP.md`
- Current state and next authorized work: `docs/00-authority/handoff/CURRENT.md`
- Lifecycle readiness audit: `docs/00-authority/PRODUCT-ARCHITECTURE-IMPLEMENTATION-READINESS-AUDIT-v0.1.md`
- Owner review and pending choices: `docs/02-product/OWNER-DECISION-SUMMARY-v0.1.md` and `docs/02-product/PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md`
- Product/design and engineering governance: `docs/04-engineering/PRODUCT-DESIGN-AND-DELIVERY-GOVERNANCE-v0.1.md`
- Candidate implementation sequence: `docs/05-mvp/vertical-slices/MVP-VERTICAL-SLICE-PLAN-v0.1.md`
