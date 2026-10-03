# ARCH-INGEST-RELIABILITY-001 — Durable telemetry receipt and recovery

## Identity

- **Task ID / title:** ARCH-INGEST-RELIABILITY-001 — Durable telemetry receipt and recovery
- **Type:** Architecture
- **Gate / workstream:** PR-02 / PR-09; G3/G6.9-R2 integration design; G6 identity boundary
- **Status:** Review
- **Owner / reviewer:** Product owner; architecture/engineering and security review required before implementation
- **Created / updated:** 2026-10-04

## Outcome

- **Question or problem to resolve:** What does an ingestion acknowledgement mean, and how must a source record move through durable capture, event publication, normalization and downstream processing when processes or dependencies fail?
- **User/business outcome:** Operators and source integrations can distinguish durable receipt from valid/usable measurements and from completed downstream analysis. Data loss, duplicate business effects and false healthy status are visible and bounded.
- **Concrete deliverable:** A reviewable, stack-neutral receipt/publication state model; crash/retry rules; owner decision #12; PR-02/PR-09 traceability; and VS-003 acceptance criteria.
- **Why this is the next dependency-ready task:** VS-003 cannot be implemented or accepted safely until receipt acknowledgement, recoverable publication, redelivery, durable consumer effects and operator-visible progress have explicit semantics. These semantics must not be inferred from a broker or application framework.

## Authority and context

- **Current handoff / snapshot:** `docs/00-authority/handoff/CURRENT.md`; PR #8, branch `docs/product-architecture-roadmap` (open/unmerged).
- **Relevant Decision IDs:** D-065 (versioned contract authority/generation); D-073 (correlation metadata does not affect semantic identity); D-075 applies to future field-write replay protection and is not closed by this task.
- **Relevant Open Question IDs:** U-003 (source/API access, where applicable); U-021 (full-stack execution environment); U-022 (production Edge key lifecycle); U-024 (zero duplicate field writes under real failures — command/control hard gate, not telemetry exactly-once evidence).
- **Relevant Gate and exit criteria:** G3 source identity and data-quality dependencies; G6.9-R2 Step 3D/4 runtime evidence; G6 remains open for identity/control proof.
- **Evidence sources / contracts / architecture records:**
  - `docs/03-architecture/ARCHITECTURE-DESIGN.md` — logical runtime view and durable capture before downstream publication.
  - `docs/03-architecture/detailed-design/TELEMETRY-INGESTION-AND-DATA-QUALITY-DETAILED-DESIGN-v0.1.md` §§3, 6.5, 9–11.
  - `docs/03-architecture/detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md` — PR-02 mapping.
  - `docs/05-mvp/vertical-slices/MVP-VERTICAL-SLICE-PLAN-v0.1.md` — VS-003 acceptance.
  - `docs/02-product/OWNER-DECISION-SUMMARY-v0.1.md` decision #12 and `PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md`.
  - `docs/01-research/G6.9-technology-research/STEP-3D-READINESS-AND-EXECUTION-PLAN-v0.1.md`.
- **Known status distinctions:** The state model is a stack-neutral proposal. It is not an approved connector/API contract, schema, storage design or runtime implementation. Candidate technologies remain candidates. No source/site connector was validated and no application behavior was tested.

## Scope

### In scope

- Separate authenticated/authorized request, raw-durable capture, quarantine, pending publication, published, normalized-durable and blocked/replayable progress.
- Specify that a receipt acknowledgement may occur only after authorized raw payload and receipt metadata are durable; it does not imply validation or economic eligibility.
- Specify crash recovery between capture and publication and acknowledgement after consumer-side durable effects.
- Preserve at-least-once/redelivery reality; use stable internal capture references for internal replay; do not deduplicate distinct source publications by payload hash, timestamp or value.
- Distinguish telemetry event processing from U-024's future physical field-write/idempotency proof.
- Carry the design into VS-003 acceptance and PR-02 traceability.

### Out of scope

- Selecting an outbox product, database, broker, MQTT QoS, API status code, schema/contract format, event-ID field or retention period.
- Claiming exactly-once delivery or authorizing field commands.
- Choosing production technology/deployment architecture, closing G3/G6/G6.9-R2, contacting CEM/customers, or collecting live data.
- Implementing the runtime or running application tests in this documentation task.

### Assumptions to validate

- Connector-specific protocol acknowledgements can represent durable capture separately from downstream processing, or a documented per-connector contract is needed.
- The selected topology can recover pending raw captures after process restart without relying on an in-memory queue.
- Data governance/security review permits the required raw payload and metadata capture under defined access, retention and deletion rules.
- The source event identity inventory determines when producer identity exists and when platform capture references are the only safe internal retry key.

## Architecture packet

- **Affected modules/files:** architecture design; telemetry detailed design; owner review packet and decision summary; PRD traceability; VS-003 plan; CURRENT handoff.
- **Approved interfaces/contracts:** None for this task. Existing V1 is noncanonical and has no stable producer event ID.
- **Architecture and safety constraints:** authenticate and authorize before data is eligible for downstream use; durable capture precedes publication/acceptance; tenant/site scope follows verified identity; remain fail-closed; no control authority; no exactly-once assertion.
- **Failure, retry, idempotency, tenant, audit, and rollback behavior:** see telemetry detailed design §9. Any selected implementation must recover PUBLISH_PENDING, tolerate redelivery, avoid duplicate durable consumer effects, preserve raw-to-normalized lineage and expose backpressure/backlog. Source retries without stable source identity may create distinct records and must not be heuristically collapsed.
- **Required checks and exact acceptance criteria:**
  1. Owner reviews or explicitly defers decision #12 without treating silence as approval.
  2. Each in-scope connector's receipt acknowledgement is mapped to the state model and protocol behavior.
  3. A fault matrix covers failure before raw commit, after raw commit/before publish, after broker publish/before publication-state update, and after consumer durable write/before acknowledgement.
  4. Later runtime acceptance demonstrates pending-publication recovery, at-least-once redelivery, consumer idempotency, backpressure, quarantine, correction/replay, tenant isolation and observable state transitions under selected topology.
  5. No result is called exactly-once; U-024 physical field-write trials remain separate.
- **Evidence to preserve:** source/protocol inventory; owner decision/deferral; frozen design version; runner manifest and dependency pins; raw and normalized lineage references; fault-injection manifests/logs; state transition/backlog metrics; data-governance approval; exact commands and results when runtime work is authorized.

## Current implementation baseline recheck

- PR #8 base and current `main` both resolve to `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`; PR #8 is documentation/governance-only at the latest inspected head and does not modify application source.
- Source files rechecked at that main snapshot:
  - `implementation/platform-api/src/vs001/vs001.controller.ts` blob `de93bc59354890f1e8be6274123ecf51f24fb3ca`: the VS-001 route has no visible authentication/authorization guard.
  - `implementation/platform-api/src/app.module.ts` blob `df2e93719b1209633597045142d3c5688751f47e`: wires fail-closed Energy Graph/Tariff adapters, a fail-closed optimizer and an in-memory evidence repository.
  - `implementation/platform-api/src/vs001/adapters.ts` blob `d4b0872fd9a52dedf8745cc45bdcbcd2fb3e83d6`: confirms unresolved graph/tariff behavior and in-memory evidence storage.
  - `implementation/edge-runtime/cmd/edge/main.go` blob `ee671a01e41f9325658bb2a98243936bc31825f4`: logs bootstrap only; no ingestion transport or durable capture path is present in this entrypoint.
- This is a static source inspection, not a runtime verification. These findings mean there is no safe production VS-003 implementation to begin in the present scaffold without first resolving identity, storage, contract and architecture authority. They do not mean that the existing code cannot be retained as Candidate B evidence.

## Completion record

- **Changes/deliverables:** durable telemetry lifecycle and crash/retry design added; architecture/runtime view aligned; owner decision #12 added; PR-02 and VS-003 criteria updated.
- **Sources or files updated:** architecture design; telemetry detailed design; owner decision summary; product/architecture review packet; readiness audit; PRD traceability; vertical-slice plan; CURRENT.
- **Checks run and results:** The preceding exact PR head `5464e0e` passed Authority Validation and Repository Hygiene before this task packet/handoff was added. The task-packet commit requires those same repository-governance checks on its exact resulting PR head. These workflows validate repository governance only; no application tests or runtime fault experiments were run.
- **New evidence / decisions / unknowns:** design proposal is reviewable; outbox/physical persistence, connector ack semantics, producer event identity, SLO/retention and topology remain open. U-024 is not resolved.
- **PR/branch and review state:** `https://github.com/lilinling12/macau-commercial-energy-os/pull/8`, `docs/product-architecture-roadmap`, open/unmerged.
- **Gate or task status after work:** Review; no Gate closed.
- **Next task and dependencies:** review owner decision #12; inventory the first authorized connector(s); then revise connector contract and implementation packet to the selected protocol/topology and complete the fault-injection plan. Do not begin production connector implementation until product/data/security and runtime authority are recorded.
