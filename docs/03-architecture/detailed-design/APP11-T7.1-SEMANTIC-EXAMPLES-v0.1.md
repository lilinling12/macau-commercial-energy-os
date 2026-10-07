# G7.9 T7.1 — Schema-Neutral Semantic Examples v0.1

**Status:** Study-only review corpus. Not a wire contract, JSON Schema, API response, accepted domain vocabulary, optimizer output, or Gate exit.  
**Date:** 2026-10-07  
**Purpose:** Make the T7.1 semantic boundaries executable without inventing a canonical serialized model.

## Source pins

- PR #10 at dd411a83b9c41ffbf7b8c17ff2a80b7c4229f35e: APP11 semantic decision packet; assessment/result view-model proposal; G7.9 T1 scoped evidence matrix; APP11 claim-to-UI mapping; flexible-load service boundary proposal.
- PR #14 at ccbfa7011f66f86d0a2d541776b02c80eea3df7a: bounded Python assessor/optimizer and generated synthetic projection fixture.
- Exact paths and pins are also embedded in semantic-examples.v0.1.json.

These PRs are open Drafts. The semantic decision packet's S-01…S-12 remain review positions, not owner approvals. Existing G7.8/G6.9 authority conflicts remain unresolved as recorded elsewhere.

## How to read this corpus

The JSON shape is only a convenient test-vector container. Its keys and sample status strings are not proposed APP-11 field names or enums. Each case says whether it describes current source behavior, a presentation example, or a semantic review proposal. Do not deserialize it as an application response.

1. **T71-01** pins the synthetic fixture plus v3.5 static UI projection boundary. Physical output is scenario-only; economics is blocked; the UI-derived service row is not emitted by PR #14.
2. **T71-02** reproduces the separate T1 presentation example: four covered intervals out of six, an in-scope component disposition, and no calculated amount. The intervals are illustrative and do not establish verified rates.
3. **T71-03** combines PR #14's resource-scoped partial behavior with the proposed service vocabulary. Stale required ESS evidence may withhold the affected claim; UNKNOWN service is proposed semantics and stale evidence alone is not a violation.
4. **T71-04** reflects current PR #14 behavior for request-wide unknown core evidence: the physical assessment is blocked and metrics are absent. BLOCKED does not mean a known constraint breach.
5. **T71-05** is a proposed lifecycle boundary. An operational failure has no physical/economic assessment result; it must not be relabeled as blocked or infeasible.
6. **T71-06** is a positive semantic comparator: a violation is meaningful only when the applicable hard bound and breach are known. It is a proposal, not behavior implemented by PR #14.

## Executable acceptance boundaries

Run python3 validate_semantic_examples.py. It verifies the six case classes and rejects:
- PARTIAL used as a claim disposition;
- a partial component whose scope differs from the exact covered interval set;
- invented amount/currency in this presentation corpus or a broadened bill/savings/demand/export claim;
- stale/unknown evidence mapped to a service violation without an evidenced hard-bound breach;
- unknown core evidence treated as infeasible or given invented metrics;
- operational failure populated with physical/economic results;
- any claim that device control is authorized or the artifact is canonical.

This verifier checks only this study corpus's internal semantic invariants. It does not validate a production contract, evaluator, evidence service, UI/API integration, real tariff, Macau site, accessibility, or user comprehension.

## Review status and next step

This closes only the missing executable example/verifier sub-scope of T7.1 on this branch. T7.1 remains open until product/domain/owner review accepts the terminology and source hierarchy, and until unresolved authority decisions (including APP ownership, D-065/G7.8 contract authority and G6.9 selection status) are reconciled. It does not authorize implementation freeze.

T7.2 remains unstarted: add a read-only local server/client seam only after reviewing this adapter boundary, with request/response provenance and browser assertions. No authentication, persistence, evidence resolution, durable lifecycle, replay, or device-command path is introduced here.
