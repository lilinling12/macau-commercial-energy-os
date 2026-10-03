# Recommendation & Operator Review Detailed Design v0.1

**Status:** Stack-neutral design draft; product scope and user roles remain unvalidated.  
**Scope:** Generation, publication, explanation, human review and evidence lifecycle for SHADOW-mode recommendations.  
**Authority:** PR-06/PR-08, D-002/D-003/D-006–D-009, D-019/D-026/D-028, D-041/D-046/D-049/D-061, G2/G4/G5/G6 and current recommendation/result contracts.  
**Production status:** Not an approved production workflow, optimizer contract, control API or authority to change plant operation.

## 1. Product and safety boundary

A recommendation is an advisory proposal derived from a pinned set of measurements, site/asset mappings, forecasts, constraints and economic assessments. It explains what the optimizer proposes, why it proposes it, what evidence and assumptions it used, and how a human may record a review outcome.

The first product increment is SHADOW/advisory. A human review action records product feedback or operational disposition only; it does not authorize a device write. The MVP has no “Apply”, “Send command” or control-enable workflow. G6 remains OPEN, and no recommendation state or user-interface action may bypass the Edge/Safety Kernel path required by D-008.

The recommendation lifecycle and any future command lifecycle are separate domains:

- Recommendation: proposed → reviewed/annotated → expired/superseded and later evaluated against observed outcomes.
- Command: a separately authorized, signed, scoped, expiring, idempotent object that may be considered only after the relevant G6/G6.9 gates, Decision Records, site approvals and implementation proof.
- Outcome: measured effect and M&V assessment, distinct from predicted effect, user acceptance or command acknowledgement.

## 2. Inputs, readiness and generation

### Required logical inputs

A generated recommendation references:

- authorized tenant/site identity and a pinned Energy Graph snapshot;
- canonical, quality-qualified measurements and source/freshness coverage;
- applicable rule/tariff result or an explicit reason why monetary evaluation is unavailable;
- forecast/optimizer request, horizon, objective, baseline and model/build identity;
- asset operating constraints, comfort/SLA limits, policy version and unavailable/disabled action boundaries;
- evaluation status, unresolved questions, assumptions and immutable Evidence Record references;
- created time, valid-from/until and clock/boundary policy.

The concrete request/result schemas remain open under D-065 and contract authoring review. This design defines semantics, not a finalized schema.

### Generation eligibility

| Condition | Recommendation behavior |
|---|---|
| Required site/tenant authorization fails | Reject generation; audit stable denial reason |
| Required point/asset mapping is missing, ambiguous or cross-scope | Do not generate an actionable asset proposal; create blocked evidence |
| Inputs are stale, invalid, BAD or insufficient for the objective | Suppress or mark blocked; show the affected interval and source coverage |
| Economic/tariff inputs are unresolved | Do not emit authoritative monetary value or rank as verified savings; if an explicitly allowed engineering scenario is useful, label it PROJECT_ASSUMPTION and keep it separate from customer bill economics |
| Forecast, constraints or baseline version missing | Block or return a non-economic informational analysis; do not imply a complete recommendation |
| Inputs and policy are resolved for the declared objective | Generate a SHADOW proposal with complete provenance, validity horizon and constraints |
| A safety/control capability is absent or G6 is open | Keep all actions advisory; no command object or execution endpoint is produced |

Generation must be deterministic for the same pinned input set and versions, except for explicitly versioned stochastic models whose seed/configuration and reproducibility envelope are recorded. An LLM may explain a deterministic result only as a non-authoritative narrative and may not invent input values, override reason codes, clear blockers or create commands (D-007).

## 3. Recommendation record and semantics

RecommendationV1 is the current wire contract. It includes tenant/site, mode, timestamps, objective, actions, evidence references and safetyReviewRequired. It permits modes SHADOW, HUMAN_APPROVAL and CONTROLLED_EXECUTION and an untyped numeric estimatedValue. This design restricts the product's current behavior to SHADOW; presence of other enum values does not authorize those paths.

A future versioned recommendation record should logically carry:

- immutable recommendation ID, schema version, tenant/site scope and created/valid interval;
- mode fixed to SHADOW for this product stage;
- objective identity and a reference to the cost/assessment result rather than treating a float as money;
- baseline identity, comparison period, source coverage and model/optimizer build;
- proposed actions with canonical asset, action type, typed parameters/unit and constraint references;
- expected effect range and uncertainty only when its mathematical semantics are defined;
- evidence status, assumptions, unresolved reason codes and links to graph/rule/forecast snapshots;
- reviewer interaction as separate append-only events, not a mutation to the original optimizer output;
- semantic digest/canonicalization only after D-065 replay identity policy is approved.

The stored proposal is immutable. A correction in source data, mappings, constraints or model creates a new recommendation linked through supersedes/recomputed-from references. It does not edit the old evidence.

### Economic meaning

RecommendationV1’s objective.estimatedValue is a JSON number with no proven scale, comparison meaning or authoritative settlement relationship. It cannot be interpreted as absolute cost or savings. Under D-026, monetary truth must be decimal-safe and supported by a CostEvaluationResult.

Until product review chooses the meaning and a versioned contract records it:

- do not display V1 estimatedValue as a monetary claim;
- do not label optimizer objective change as customer savings;
- show monetary result only from a referenced cost assessment with its evidence/settlement status;
- separate absolute projected cost, change versus baseline, producer PV revenue and any site-economic scenario;
- do not rank proposals by unverified or assumed economics as if they were comparable.

## 4. Review lifecycle

Recommendation business status is distinct from recommendation mode. For the MVP, use an append-only review timeline with a derived current state:

| Derived state | Meaning | Allowed transition |
|---|---|---|
| GENERATED | Immutable proposal and evidence were created | → AVAILABLE, BLOCKED, or EXPIRED |
| BLOCKED | A required input/policy is missing or conflicting | New evidence may trigger a new recommendation; never silently mutate this one |
| AVAILABLE | Proposal is in its validity interval and ready for advisory review | → REVIEWED, DISMISSED, NEEDS_EVIDENCE, EXPIRED, SUPERSEDED |
| REVIEWED | A named authorized user inspected the proposal and recorded acknowledgement/comment | May later be superseded/expired; does not mean accepted for execution |
| DISMISSED | A reviewer chose not to pursue the advisory proposal and optionally recorded a reason | Terminal for this recommendation; a changed situation creates a new recommendation |
| NEEDS_EVIDENCE | Reviewer requested additional data/context | New data may produce a new assessment/recommendation; original remains immutable |
| EXPIRED | Validity window ended without current relevance | Terminal; generation under current inputs creates a new identity |
| SUPERSEDED | A new assessment/recommendation replaces it or invalidates the earlier context | Link to the superseding record and reason |

No MVP state named APPROVED_FOR_EXECUTION, ACCEPTED, or CONTROLLED is defined. If a later gated release needs operator approval for a control request, that is a distinct command authorization state machine with independent G6 authority and contracts.

### Review event

A review event logically records review-event ID, recommendation ID/revision, actor identity from authenticated session, actor’s authorized tenant/site role, event time, event type, optional controlled reason code/comment, referenced evidence reviewed and UI/client version. Event types for MVP are OPENED/ACKNOWLEDGED, DISMISSED, NEEDS_EVIDENCE and COMMENTED. Free-text content is access-controlled and treated as user data; it cannot modify calculation facts.

Do not infer that a proposal was read from a page impression alone; opening can be telemetry, while explicit acknowledgement is a human review event. Do not equate dismissal with unsafe status or reviewed with endorsement.

## 5. Operator workflow and interface requirements

1. **Queue:** filter by site, validity window, evidence readiness, objective and review state. Default ordering explains its rationale; do not sort by monetary impact when monetary semantics are blocked.
2. **Summary card:** show SHADOW, status, created/valid time, site/asset, objective, evidence coverage, uncertainty and blockers. Use text and icon/state labels in addition to color.
3. **Detail:** compare actual baseline context with proposal; show forecast period, proposed change, operating constraints, affected assets, expected effect semantics, input freshness and supporting evidence links.
4. **Evidence:** inspect telemetry source and times, mapping snapshot, tariff/contract/rule references, baseline, model/optimizer version and reason codes. Indicate synthetic vs site data and project assumptions.
5. **Review:** record acknowledgement, dismiss, needs-evidence or comment. Display a clear statement that the action records review only and cannot execute plant control.
6. **Expiry/supersession:** identify why it is stale or replaced and link the new assessment; never show it as currently actionable after expiry.
7. **Outcome:** show forecast separately from measured outcome and M&V result. Use a named baseline, measurement window and attribution status; no savings claim without G1/G7 evidence.

Accessibility and usability: preserve keyboard access/focus, announce state changes to assistive technology, provide chart/table alternatives, show full timestamps/timezone, support localization and maintain readable layouts at validated screen sizes. The role hierarchy, terminology, responsive behavior and visual direction remain subject to the planned Macau user research and UI/UX Pro Max workflow.

## 6. Authorization and audit

- Derive tenant/site scope and actor identity from authenticated context; never trust the recommendation’s payload tenant/site as authority.
- Read access is scoped to authorized portfolio/site membership. Review-event creation requires an explicit review capability; configuration and mapping powers are separate.
- A comment cannot change a tariff package, measurement policy, action bound or safety rule.
- Review events are append-only and attributable; correction uses a superseding event with reason, not history rewrite.
- Enforce access controls at API, query, export and background-job boundaries; the current inspected controller path has no auth guard and is not production-ready.
- Minimize sensitive operating details in notification/email previews; never leak another tenant’s site identity or recommendation data.
- Retention/export/deletion policy, role taxonomy, partner delegation and identity provider remain open for owner/product/deployment review.

## 7. Staleness, concurrency and replay

At read time, compare recommendation valid interval, input freshness, graph snapshot validity and relevant rule/policy versions with the current time/pinned assessment. A stale proposal becomes visibly EXPIRED or SUPERSEDED; do not extend validity automatically. If site conditions changed materially, require new evaluation.

Review events are append-only and concurrent events preserve actor/time order; a derived display state is recalculated by a versioned lifecycle policy. Conflicting reviewer actions do not rewrite earlier events. Define ordering and conflict display before production implementation.

Replay pins the original event set, data-quality policy, graph snapshot, tariff/settlement result, baseline, forecasts, model/build, optimizer configuration and clock policy. A replay with missing input is INCOMPLETE; never substitute the latest graph/model/tariff. Trace IDs are diagnostic only, not recommendation identity.

The measured outcome is a separate M&V assessment that references the original recommendation and an approved baseline/measurement window. It records actual telemetry coverage, confounding changes, effect estimate and uncertainty. User acknowledgement, dismissal, command acknowledgement and measured effect are separate facts.

## 8. Failure behavior

| Failure or ambiguity | Behavior |
|---|---|
| Recommendation inputs cannot be authorized or scoped | Reject; audit without exposing unauthorized site data |
| Input quality/freshness insufficient | BLOCKED or non-actionable informational result; show affected inputs and period |
| Tariff/settlement unknown | Remove authoritative monetary claim/ranking; if a scenario remains useful, mark PROJECT_ASSUMPTION with excluded components |
| Evidence reference unavailable | Mark evidence incomplete; do not publish as fully reviewable |
| Recommendation expired | Disable review-as-current and surface expiry; require reevaluation for current conditions |
| Reviewer role revoked before save | Reject the review event; retain no unauthorized action |
| Duplicate review request retry | Use review-event idempotency once an event identity contract is approved; do not duplicate comments or silently discard distinct actions |
| Replay dependency missing | INCOMPLETE_REPLAY with exact missing references |
| Optimizer/LLM returns malformed or unsupported action | Reject/quarantine proposal; no automatic repair that changes intent |
| User attempts execution through API/UI | No execution endpoint in MVP; reject and audit. This is not a substitute for G6 command security in a future release |

## 9. Acceptance evidence

Before PR-06/PR-08 can be accepted for the first product increment:

1. Validate recommendation tasks, roles, terminology and review dispositions with target Macau users; no response or clickthrough metric alone proves usability.
2. Approve recommendation lifecycle and product meaning of expected economic value (absolute cost, baseline-relative change, or withheld until eligible evidence exists).
3. Verify all recommendation fields link to versioned input, graph, settlement, model and evidence references.
4. Show missing/stale/uncertain inputs as visible blocked/partial states and prove there is no supported control write path in the MVP.
5. Review tenant/site authorization and reviewer permissions with product/identity owners; verify audit and revocation behavior before production.
6. Keep recommendation lifecycle state independent from future command/approval state; any command surface requires G6 closure evidence, G6.9 runtime evidence, site authorization and a new owner-approved decision.
7. Validate keyboard/accessibility, chart/table alternatives, responsive layouts and localization with the intended user and device context.
8. Prove that displayed measured outcome is an independent M&V assessment, not inferred from reviewer acknowledgement or predicted value.

This is a design proposal, not customer-validated interaction design, production authorization or runtime evidence.

## 10. Unresolved product and technical decisions

- Lead user/site and main review task are not selected or customer-validated.
- Recommendation priority and queue ordering when economic evidence is incomplete.
- Expected value semantics and when it is safe to show money.
- Reviewer role and audit policy; identity provider and delegated partner access.
- Forecast/model/optimizer contract, uncertainty representation and reproducibility.
- Validity-window policy and stale-condition triggers by asset type.
- Review-event schema and idempotency contract.
- M&V baseline and attribution method by use case.
- Visual direction and responsive control-room/desktop/mobile priorities.
- G6 command lifecycle is outside this document and remains OPEN.

## References

- Product workflow hypotheses: docs/02-product/PRD-v0.1.md and docs/02-product/USER-FLOWS-AND-IA-v0.1.md.
- Recommendation contract: implementation/contracts/recommendation.v1.schema.json.
- Cost/replay contract proposal: docs/03-architecture/detailed-design/VS-001-RESULT-AND-REPLAY-CONTRACT-PROPOSAL-v0.1.md.
- Safety authority: docs/01-research/gates/G6-safety-control.md and D-006/D-007/D-008.
- Current architecture and implementation gaps: docs/03-architecture/ARCHITECTURE-DESIGN.md; docs/03-architecture/detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md.
