# ARCH-PERSISTENCE-BOUNDARY-001 — Logical persistence and schema evolution

## Identity

- **Task ID / title:** ARCH-PERSISTENCE-BOUNDARY-001 — Logical persistence and schema evolution
- **Type:** Architecture
- **Gate / workstream:** WP-5; PR-01/PR-02/PR-03/PR-04/PR-05/PR-07/PR-08/PR-09; G3/G6.9-R2; G6 identity and audit boundary
- **Status:** Review
- **Owner / reviewer:** Product owner; architecture/engineering, data and security review required before implementation
- **Created / updated:** 2026-10-04

## Outcome

- **Question or problem to resolve:** How should the product preserve tenant-scoped operational state, raw and normalized telemetry, tariff/graph versions, evaluation evidence, replay inputs and operator-review events across failures and schema changes?
- **User/business outcome:** An operator or reviewer can see which source facts and versioned rules support a result, distinguish accepted from processed data, and recover or replay safely without silently changing prior evidence.
- **Concrete deliverable:** A stack-neutral logical data authority and persistence design covering data domains, lifecycle, transaction boundaries, tenant scope, correction/replay, retention questions and migration/rollback rules; traceable PR-01/02/03/04/05/07/08/09 requirements and VS-001/VS-003 acceptance evidence.
- **Why this is the next dependency-ready task:** Existing detailed designs define the responsibilities and evidence semantics, but persistence, transaction and schema-evolution commitments remain distributed. The bake-off cannot be compared or a vertical slice safely implemented without knowing the required persistence behavior, even though the database, time-series extension, object store and event/workflow products remain unselected.

## Authority and context

- **Current handoff / snapshot:** docs/00-authority/handoff/CURRENT.md; PR #8, branch docs/product-architecture-roadmap (open/unmerged).
- **Relevant Decision IDs:** D-013/D-014 (graph and relationships); D-022–D-029 (economic evaluation and traceability); D-065 (contract authority/versioning); D-073 (correlation metadata is not semantic identity); D-074 (aggregation boundary before quality filter); D-075 (field-write replay protection remains separate).
- **Relevant Open Question IDs:** U-001/U-009/U-010/U-011 (settlement inputs); U-021 (runtime environment); U-022 (Edge key lifecycle); U-024 (physical field-write duplicate proof); U-027 (data classification/privacy/cross-border flow); owner decisions #8, #11, #12 and #14.
- **Relevant Gate and exit criteria:** G1 evidence governs bill-grade data; G3 validates source/site identity and mapping; G6.9-R2 Step 3D/4 freezes candidate runtime evidence; G6 authorizes security boundary evidence. None is closed by this task.
- **Evidence sources / contracts / architecture records:** Logical Architecture Design; VS-001 Detailed Design; Telemetry Ingestion and Data Quality; Energy Graph; Tariff and Settlement; Cost Analysis and Evidence Replay; Deployment, Operability and Recovery; Identity and Tenant Authorization; PRD-to-Architecture Traceability; current telemetry/result/replay contracts; MVP Vertical Slice Plan.
- **Known status distinctions:** This design is a logical proposal. PostgreSQL + Timescale remains an evaluation baseline, and Temporal/NATS/object storage remain candidates or unspecified. No canonical physical schema, migration, retention, provider, or runtime behavior is approved or tested.

## Scope

### In scope

- Identify logical data domains and their authorities, ownership scope, mutability, versioning and lineage.
- State durability/acknowledgement boundaries for raw capture, publication, consumer effects and derived evidence.
- Define correction, replay, audit and deletion/retention behavior as far as current authority allows; mark owner/legal decisions explicitly.
- Define tenant/site scope requirements across records, transactions, asynchronous work, caches and exports.
- Define technology-neutral migration, compatibility, backfill, rollback and backup/restore expectations.
- Link acceptance evidence to vertical slices and unresolved research/owner decisions.

### Out of scope

- Selecting a database, table layout, ORM, time-series extension, event broker, workflow engine, object-storage service or cloud provider.
- Approving exact retention, data residency, legal-hold or deletion periods.
- Inventing producer event IDs, tariff rules, settlement intervals, user roles or customer-data semantics.
- Implementing persistence/migrations, processing live data, claiming replay equivalence or closing a Gate.

## Architecture packet

- **Affected modules/files:** logical architecture; new persistence detailed design; owner review summary if a decision is introduced; PRD traceability; architecture index; roadmap; CURRENT and HISTORY.
- **Approved interfaces/contracts:** None for the physical persistence layer. Existing V1 contracts are not promoted to canonical authority by this task.
- **Architecture and safety constraints:** preserve source facts and versions; use explicit tenant/site authorization scope; fail closed for untrusted or unresolved lineage; SHADOW only; never let persistence/replay become a field-command authorization path.
- **Failure, retry, idempotency, tenant, audit, and rollback behavior:** the design must describe crash points at raw payload/metadata storage, outbox/publication, consumer durable effect and evidence write; any internal retry identity must not collapse distinct source publications without source identity evidence; every read/write and replay remains in its original authorized tenant/site scope; migrations preserve old-reader compatibility until old versions are retired.
- **Required checks and exact acceptance criteria:**
  1. Each logical data domain has a system-of-record responsibility, ownership scope, version/correction policy and unresolved physical-placement decisions.
  2. The design states what must be durable before acknowledging receipt, publication, consumer processing or completed evidence.
  3. Cross-store partial failure/reconciliation is explicit; the design does not assume a distributed transaction.
  4. Schema and contract evolution has an additive rollout, data backfill, compatibility, rollback and destructive-change retirement policy.
  5. Tenant isolation, bitemporal replay lineage, retention/deletion, backup/restore and exact rerun evidence have acceptance criteria with owners/open questions.
  6. PR-01/02/03/04/05/07/08/09 and VS-001/VS-003 traceability is updated without marking product requirements, Gates or owner decisions complete.
  7. Exact-head Authority Validation, Repository Hygiene and Runtime Bootstrap are inspected; no application tests are claimed for documentation-only changes.
- **Evidence to preserve:** design revision; authority links; owner decision dependencies; data-domain/lifecycle matrix; transaction/failure matrix; schema migration and rollback policy; exact CI revision/results and limits.

## Completion record

- **Changes/deliverables:** Added the stack-neutral logical persistence/domain-authority matrix, durability and transaction-boundary proposal, failure/recovery matrix, tenant-scope invariants, temporal/version/replay rules and additive migration/backfill/rollback policy.
- **Sources or files updated:** This packet; DATA-PERSISTENCE-AND-SCHEMA-EVOLUTION-DETAILED-DESIGN-v0.1.md; ARCHITECTURE-DESIGN.md; architecture README; Master Index; PRD-to-architecture traceability; VS-003/VS-005 handoff; roadmap; CURRENT; append-only HISTORY and PR #8 description.
- **Checks run and results:** Exact resulting PR-head Authority Validation, Repository Hygiene and Runtime Bootstrap results are to be recorded after the cross-file synchronization. No application code, migration or runtime test was added or run.
- **New evidence / decisions / unknowns:** The design makes persistence requirements reviewable without selecting physical technologies. Owner decisions #8/#12/#14, U-027, product/Gate evidence, physical data model, retention/deletion, RPO/RTO and G6.9-R2 Step 3D/4 remain open.
- **PR/branch and review state:** PR #8, docs/product-architecture-roadmap, open/unmerged.
- **Gate or task status after work:** Review; draft deliverable prepared, no owner approval or Gate closure.
- **Next task and dependencies:** Owner/customer/security review of data domains and access/retention/replay boundaries; Step 3D/4 evidence for physical persistence capabilities; then a stack-specific data model and migration packet tied to approved product/architecture decisions.
