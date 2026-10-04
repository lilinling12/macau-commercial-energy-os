# ARCH-APP-CONTRACT-CATALOG-001 — MVP application and event boundary catalog

## Identity

- **Task ID / title:** ARCH-APP-CONTRACT-CATALOG-001 — MVP application and event boundary catalog
- **Type:** Architecture
- **Gate / workstream:** WP-5; PR-01 through PR-09; G6.9-R2 contract-authority and framework-native evaluation; D-065
- **Status:** Review
- **Owner / reviewer:** Product owner; architecture, API/integration, data and security review required before contract freeze
- **Created / updated:** 2026-10-04

## Outcome

- **Question or problem to resolve:** What logical read, command, acknowledgement and event boundaries must the MVP expose across its user tasks and asynchronous processing, independent of its final API protocol or schema format?
- **User/business outcome:** Users receive explicit, safe status for site access, source health, cost assessments, recommendations, review and replay; systems can evolve contracts without confusing durable capture, processing completion, economic eligibility or control authority.
- **Concrete deliverable:** A reviewable logical application/API/event catalog that maps PRD workflows and vertical slices to data ownership, authorization and status semantics, while linking the existing result/replay contract proposal and leaving endpoint shapes/wire format unselected.
- **Why this is the next dependency-ready task:** The current repository has V1 telemetry/recommendation/evidence schemas and a VS-001 cost/replay proposal, but no cross-workflow catalog tying user tasks to application boundaries, authorization, asynchronous states and compatibility. A logical catalog can identify blockers before Step 3D compares candidate frameworks.

## Authority and context

- **Current handoff / snapshot:** docs/00-authority/handoff/CURRENT.md; PR #8, branch docs/product-architecture-roadmap (open/unmerged).
- **Relevant Decision IDs:** D-065 (cross-language contract authority/generation); D-073 (correlation metadata is not semantic identity); D-074 (aggregation window before quality filtering); D-069 (Java Phase D implementation deferred); D-062–D-076 technology-authority records.
- **Relevant Open Questions / owner decisions:** U-003 (site source/API access); U-021 (execution environment); U-022/U-024 (separate Edge identity and physical command proof); U-027 (customer-data governance); owner decisions #1/#8/#12/#14; G1/G3/G6/G6.9-R2 dependencies.
- **Evidence sources / contracts / architecture records:** PRD and USER-FLOWS-AND-IA; VS-001 Detailed Design; VS-001 Cost Result and Replay Manifest proposal; Data Persistence and Schema Evolution design; Identity and Tenant Authorization design; Telemetry Ingestion and Data Quality design; Recommendation and Operator Review design; MVP Vertical Slice Plan; implementation/contracts V1 inventory; D-065 contract-authoring comparison.
- **Known status distinctions:** Logical operations and state transitions are draft review input. Existing schemas are not automatically canonical contracts. No REST/GraphQL/RPC protocol, OpenAPI/JSON Schema/Protobuf authoring format, URL, endpoint, generated binding or production API is approved.

## Scope

### In scope

- Catalogue logical user/application operations and producer/consumer/event responsibilities for the research-derived MVP workflows.
- Map each operation to authorization scope, owning capability, durable evidence, status semantics and relevant vertical-slice acceptance.
- Separate synchronous request completion, asynchronous accepted/pending state, durable receipt, downstream processing, economic eligibility and human review.
- Reuse existing domain-specific proposals instead of redefining monetary or replay semantics.
- State compatibility, retry, failure, tenant isolation and observability requirements at the logical boundary.
- Record owner/Gate dependencies that must be resolved before freezing wire contracts or implementing production APIs.

### Out of scope

- Selecting an API style, transport, endpoint path, wire schema format, version encoding, authentication provider or code generator.
- Replacing existing result/replay or telemetry contract proposals, or promoting current V1 implementation schemas to final authority.
- Defining customer-validated user roles, monetary semantics, tariff details, connector-specific ACK codes or source event IDs.
- Implementing endpoints, modifying runtime contracts, starting external integrations, processing customer data or authorizing commands.

## Architecture packet

- **Affected modules/files:** new logical contract catalog; new task packet; architecture index; PRD-to-architecture traceability; MVP vertical-slice handoff; contract README; CURRENT, roadmap and HISTORY.
- **Approved interfaces/contracts:** No final interface or wire contract is approved by this task. D-065 remains the contract governance authority.
- **Architecture and safety constraints:** server-derived principal and explicit resource/action scope; durable raw capture before platform receipt; fail closed on ambiguous scope or evidence; SHADOW only; no API, event, annotation, approval or replay path may imply device execution authority.
- **Failure, retry, idempotency, tenant, audit, and rollback behavior:** asynchronous operations expose stable progress and blocked reasons; repeated delivery is expected; consumer effects require a selected durable idempotency boundary; no deduplication without identity evidence; error responses do not disclose foreign resources; contract changes preserve compatible consumers and pinned replay lineage.
- **Required checks and exact acceptance criteria:**
  1. Each logical operation maps to a PRD user task, capability owner, vertical slice, authorization action/resource scope, status semantics and required evidence.
  2. User-facing API status never equates request acceptance, raw durability, consumer completion, economic eligibility, recommendation review, measured outcome or execution.
  3. Unresolved owner decisions and G1/G3/G6/G6.9 dependencies are explicit; no endpoint or schema format is implicitly approved.
  4. Event and retry descriptions do not invent producer IDs, exactly-once delivery, ordering, or transport guarantees absent a selected protocol.
  5. Catalog is linked from PRD/architecture traceability and slices; existing V1 schemas and result/replay proposal remain separately identified with their limitations.
  6. Exact-head Authority Validation, Repository Hygiene and Runtime Bootstrap are inspected; no application tests are claimed for documentation-only design.
- **Evidence to preserve:** operation/state catalog; traceability links; referenced contract versions and limitations; decision dependencies; exact revision and CI outcomes.

## Completion record

- **Changes/deliverables:** To be recorded after catalog drafting and cross-reference updates.
- **Sources or files updated:** This packet and linked architecture/authority files.
- **Checks run and results:** To be recorded at the exact resulting PR head. No runtime contract, endpoint or application test is authorized by this task.
- **New evidence / decisions / unknowns:** To be recorded after catalog review.
- **PR/branch and review state:** PR #8, docs/product-architecture-roadmap, open/unmerged.
- **Gate or task status after work:** Review; no Gate closed.
- **Next task and dependencies:** owner review of user operations/status vocabulary and decisions #8/#12/#14; G6.9-R2 Step 3D/4 for protocol/framework/contract tooling evidence; then freeze canonical wire contracts and implement them through a separate approved task packet.
