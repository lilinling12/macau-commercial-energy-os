# APP-11 Result Projection Crosswalk Review v0.1

**Date:** 2026-10-06  
**Status:** Review note; no contract, product, architecture, or Gate approval.  
**Branch baseline:** `product/source-load-economic-dispatch`, PR #10 exact head `6e2b06ab3d3a0be1f7b493de78f1be6d04ca1491`.  
**Purpose:** Check whether the new adapter/view-model proposal duplicates or conflicts with the existing G7.9 Step 3 map and claim-state presentation proposal.

## Sources read at the pinned branch

| Artifact | Blob |
|---|---|
| `G7.9-STEP3-DISPATCH-CONTRACT-IMPLEMENTATION-MAP-v0.1.md` | `9cc5acec84d13e8cb255f9eb4381c32b9a98829b` |
| `DISPATCH-CLAIM-STATE-PRESENTATION-CONTRACT-v0.1.md` | `3d621c51c8eb34c0642eb56dada938fd0903fb47` |
| `APP11-ASSESSMENT-RESULT-VIEW-MODEL-PROPOSAL-v0.1.md` | `c465899ea4bf14001a9efad56696d80c99ed8008` |

These are branch proposals and an isolated prototype mapping. This review does not promote them to controlling main authority.

## Crosswalk findings

| Concern | Existing G7.9 map / UI claim contract | New APP-11 projection proposal | Review |
|---|---|---|---|
| Physical vs economic scope | Separate physical assessment from per-scope economic evaluation; economic children may be 0..N; component and scope qualification required. UI contract likewise makes economics per settlement scope/component. | Keeps physical schedule and economic evaluations as separate children; explicitly calls out PR #14's current single-scope limit. | Aligned. New note maps actual prototype outputs and missing fields; it does not supersede the richer domain model. |
| Claim semantics | ALLOWED/WITHHELD are claim dispositions; qualification/status is a separate dimension. | Preserves this rule and maps prototype `claim_readiness` plus scope/reasons without inventing a third claim state. | Aligned. |
| Status vocabularies | G7.9 candidate application vocabulary includes COMPLETE/PARTIAL/BLOCKED/INFEASIBLE/FAILED and NOT_CALCULATED; these remain proposals. | Retains PR #14's raw `VALIDATED_WITHIN_SCOPE` / `SCENARIO_ONLY` / `PARTIAL` / `BLOCKED` / `INFEASIBLE` values and treats UI orchestration `NOT_CALCULATED` as distinct. | Deliberately not normalized yet. A future owner-approved semantic mapping must reconcile vocabulary and operational failures before any canonical fixture/schema. |
| Evidence | Map requires trusted authorization, source/effective scope, stable reason semantics and immutable input manifests. UI contract requires evidence readiness and affected scope. | Explicitly says PR #14 refs and VERIFIED labels are caller supplied and unauthenticated; lists evidence service and pinned snapshot as absent. | Aligned; projection is more explicit about the implementation gap. |
| Service feasibility | Map/product acceptance keeps electrical feasibility separate from comfort/service; service outcome may be unknown/not assessed. | Adds per-resource service child but records that PR #14 does not compute it. | Aligned; do not infer service PASS from balanced electrical flow. |
| Review, persistence and replay | G7.9 map already proposes durable assessment identity, append-only review and replay bound to immutable versions. | Repeats those as application-owned projection requirements absent from PR #14. | Complementary but overlapping. Keep the map as the broader domain/contract proposal and this note as a source-to-view adapter trace until consolidation is reviewed. |
| Execution | Both existing proposals prohibit device writes in the MVP. | Marks control authority unavailable and forbids an execution action/path. | Aligned. |

## Corrections to interpretation

1. The new APP-11 view-model proposal is **not** the first place where multi-scope settlement, durable identity, review or replay were designed. The G7.9 Step 3 map already describes those requirements. The new artifact's contribution is a concrete mapping from the current PR #14 experiment into a future UI-facing projection and an inventory of fields that experiment lacks.
2. The proposal's placeholder fields and illustrative names must not be copied into an API, database, UI fixture or generated client as if approved.
3. Candidate application statuses in the G7.9 map cannot be inferred by renaming PR #14's experiment-local statuses. In particular, transport/runtime failure, physical INFEASIBLE, input BLOCKED and economic NOT_CALCULATED require separate semantics.
4. UI claim decisions remain only ALLOWED/WITHHELD. PARTIAL is qualification/assessment scope, never a third claim disposition.
5. The map, claim contract and adapter proposal all remain review material on an unmerged draft PR; none closes G7.9 Step 3 or authorizes production use.

## Next design action

Use the existing map as the single broader G7.9 domain/contract proposal. Before canonical fixtures or schemas are made, have product/domain/security owners review one small semantic table that reconciles:
- application lifecycle vs physical assessment vs economic component vs per-claim disposition/scope vs per-resource service outcome;
- PR #14 experiment status/error mapping to the candidate application vocabulary;
- which missing evidence blocks a claim, which allows an independent partial result, and which is only a transport/operational failure;
- application identity, immutable input snapshot and independently authorized settlement scope ownership.

After that review, fold accepted mappings into the appropriate authoritative design artifact rather than letting parallel proposal files drift. Until then, keep all names illustrative and G7.9 Step 3 OPEN.
