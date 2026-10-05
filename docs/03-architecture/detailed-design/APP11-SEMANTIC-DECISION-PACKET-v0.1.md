# APP-11 Semantic Decision Packet — Review Candidate v0.1

**Date:** 2026-10-06  
**Status:** Prepared for product/domain/security/architecture review; no decision approved.  
**Branch:** PR #10 product/source-load-economic-dispatch, baseline before this packet 1f30ed40fb94020d929058c5ff11b4c39b01618a.  
**Purpose:** Make the remaining semantic choices concrete before a canonical fixture, API contract, schema or implementation is produced.

## Authority and evidence boundary

Inputs reviewed on PR #10:
- G7.9-STEP3-DISPATCH-CONTRACT-IMPLEMENTATION-MAP-v0.1.md blob 9cc5acec84d13e8cb255f9eb4381c32b9a98829b
- DISPATCH-CLAIM-STATE-PRESENTATION-CONTRACT-v0.1.md blob 3d621c51c8eb34c0642eb56dada938fd0903fb47
- APP11-ASSESSMENT-RESULT-VIEW-MODEL-PROPOSAL-v0.1.md blob c465899ea4bf14001a9efad56696d80c99ed8008
- APP11-RESULT-PROJECTION-CROSSWALK-REVIEW-v0.1.md blob 7558c0090af148be7376f7a8a219a03988ddf9f9
- PR #14 bounded experiment, exact reviewed revision referenced by the APP-11 proposal.

All four design files are unmerged proposals. PR #14 is a bounded prototype. Existing main authority and owner decisions continue to control. The recommendations below are review positions, not approvals.

## Decision table

| ID | Decision to resolve | Option A | Option B | Evidence-based recommendation | Consequence if deferred |
|---|---|---|---|---|---|
| S-01 | Separate lifecycle from domain results? | One overall status combines queued/running/failed and physical/economic state. | Application lifecycle, physical assessment, each economic evaluation, each claim, and each service outcome are independent dimensions. | **B.** The G7.9 map and claim UI contract both separate these concerns; APP-11 proposal also distinguishes queued/running from result state. A transport/runtime failure must not look like physical infeasibility. | UI/API may show a false green/red composite and cannot preserve partial independent results. |
| S-02 | How map PR #14 statuses to future app vocabulary? | Rename prototype statuses directly into application enums. | Preserve raw experiment status in the adapter input; define a reviewed, versioned mapping at the application boundary with explicit non-mappable/error cases. | **B.** PR #14's VALIDATED_WITHIN_SCOPE is narrower than application COMPLETE; SCENARIO_ONLY is a qualification; BLOCKED, INFEASIBLE, and failed execution have different causes. Never infer a winner from spelling. | Canonical examples and views can silently exaggerate scope or collapse operating error into domain outcome. |
| S-03 | What is the unit of economic result? | One economic context on the parent assessment. | Zero or more economic children, each tied to one independently authorized settlement-scope revision and its own immutable inputs. | **B.** The G7.9 map's 2026-10-05 addendum requires 0..N children and per-account authorization; physical energy flows are not copied into multiple accounts. | The current PR #14 single-scope shape can be mistaken for multi-account product support or totals can be duplicated. |
| S-04 | Can child results be rolled into one dispatch objective/summary? | Sum/evaluate all available account costs implicitly. | Show per-scope results; aggregate or optimize across scopes only under an explicit authorized/versioned objective and rule for missing scopes/components. | **B.** The map says per-scope evaluation alone does not define cross-account optimization or portfolio savings. | “Site-wide cheapest” and combined savings may be invalid where account applicability, missing tariffs, or overlapping meters differ. |
| S-05 | What does evidence state VERIFIED mean? | Trust a caller-provided reference/state field. | Resolve identity, authorization, source, effective period and immutable source snapshot in an application evidence service; prototype caller labels remain untrusted input. | **B.** The APP-11 source review confirms PR #14 does not authenticate or pin evidence. | Claims can be upgraded by a caller assertion; audit/replay cannot establish which source supported a result. |
| S-06 | How represent resource service requirements? | Treat electrical feasibility as sufficient. | Keep service outcome per resource (NOT_ASSESSED/PASS/VIOLATION/UNKNOWN) separate from electrical feasibility; PASS requires qualified site evidence, synthetic PASS remains example-only. | **B.** The product/claim contract and PR #14 trace both separate power balance from HVAC comfort, EV departure energy and hot-water delivery. | A physically balanced schedule can be presented as operationally acceptable without service proof. |
| S-07 | What is a claim's state? | Add PARTIAL as a third claim disposition. | Keep disposition ALLOWED/WITHHELD; represent scope/qualification separately, with reasons and evidence references. | **B.** The claim contract's PR #14 reconciliation explicitly rejects PARTIAL as a third decision. | UI logic and API clients may disagree about whether a partial claim is allowed. |
| S-08 | How represent failed work? | Emit an assessment with BLOCKED/INFEASIBLE even when the worker failed before evaluating inputs. | Keep request/worker lifecycle failure and typed operational error separate; produce an assessment status only when a domain assessment exists. | **B.** G7.9 map prohibits treating request acceptance as completion and requires no partial numeric result without defined scope. Typed error taxonomy still needs design. | Retry/incident states become confused with missing data or actual constraint infeasibility. |
| S-09 | What identity/replay unit is immutable? | Recompute “latest” site/tariff/mapping inputs when a user reopens a result. | Pin parent physical manifest, each child settlement manifest, policy/build and result revision; changed semantics create a new revision; review is append-only. | **B.** Existing G7.9 map already proposes manifest-pinned replay and immutable review targets. | Result history cannot be reproduced; replay may silently use changed tariffs or mappings. |
| S-10 | What can SHADOW review authorize? | Accept/review can trigger an execution pathway later or imply readiness. | Review is a human disposition against a specific immutable result/scope set; execution authority remains unavailable in MVP, with no command affordance/path. | **B.** Product and architecture proposals explicitly prohibit device writes and state review is not execution authority. | Users can mistake review for control authorization; scope of what was reviewed is ambiguous. |
| S-11 | Is APP-11 a catalog capability or a composed workflow? | Add APP-11 as a new independently deployed service/catalog operation. | Keep APP-11 a logical orchestration capability over existing assessment/cost/review operations unless an owner-approved catalog and deployment decision says otherwise. | **B for now.** G7.9 map says APP-11 is not automatically a new deployment/service boundary; final catalog ownership needs owner review. | Premature service boundaries or catalog duplication. |
| S-12 | When create a canonical cross-language fixture/schema? | Now, using proposed view-model names and current PR #14 enums. | After S-01–S-11 semantics and D-065/G7.8 contract-authority conflict are reviewed; then version schema/fixtures and compatibility rules. | **B.** This avoids encoding unresolved authority and semantic conflicts as a de facto freeze. | Current proposals remain non-executable for contract conformance; implementation cannot safely claim cross-language compatibility. |

## Recommended semantic model for review

These dimensions should remain independently addressable in result identity and presentation:

1. **Request lifecycle:** accepted/running/finished or operationally failed.
2. **Physical assessment:** what physical boundary, horizon and claims were assessed; distinguish unknown inputs (BLOCKED) from known constraint conflict (INFEASIBLE).
3. **Economic evaluation:** zero or more children; one authorized settlement scope and component coverage per child; NOT_CALCULATED is not zero.
4. **Claim disposition and qualification:** each claim is ALLOWED or WITHHELD, with independent scope, reason and support references.
5. **Resource service outcome:** per HVAC/EV/hot-water requirement; separate from electrical balance.
6. **Human review:** append-only disposition for a named immutable result and only the scope set visible to that reviewer.
7. **Execution authority:** unavailable for MVP; review does not grant it.

This is a semantic review position. Exact enum spellings, reason-code taxonomy, wire format, schema authoring tool, persistence, event model and API endpoints remain open.

## Review order

1. Product/domain owners: S-01–S-04, S-06–S-07.
2. Security/data owners: S-03, S-05, S-09–S-10, especially per-account non-disclosure and replay authorization.
3. Architecture/contract owners: S-08, S-11–S-12, reconciled with active G6.9-R2 D-065/D-068 authority and the G7.8 archive.
4. After decisions are recorded: create semantic fixtures, then canonical cross-language contracts, then one vertical slice. Do not reverse that order.

## State after this packet

No Gate status changes. G7.9 Step 3 remains OPEN. No production architecture, UI vocabulary or wire schema is approved. PR #14 remains an isolated bounded experiment; current prototypes remain disconnected synthetic UI. This packet is not evidence of a working MVP or pilot readiness.
