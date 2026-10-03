# Cost Analysis and Evidence Replay — Detailed Design v0.1

**Status:** Stack-neutral review draft; not an approved contract, bill-grade tariff implementation, or customer savings claim.  
**Scope:** PR-05 cost/demand explanation and PR-07 evidence/replay for shadow/advisory operation.  
**Authority:** G1 tariff/settlement research, D-021/D-026/D-065/D-073/D-074/D-077, Tariff & Settlement detailed design, VS-001 CostResult/ReplayManifest proposal, and current product review packet.

## 1. Purpose and boundary

This design separates three kinds of economic result that must not be presented as interchangeable:

1. **Bill reconstruction:** a billing-period result intended to explain an actual bill against applicable contract, tariff, meter, and invoice evidence. It can be called bill-grade only after the applicable Golden Bill and G1 acceptance criteria pass.
2. **Interval assessment:** an estimate for a defined time interval or scenario using resolved tariff rules and qualified measurements. It is an estimate unless reconciled to the bill and all required evidence is present.
3. **Baseline comparison:** a counterfactual comparison between two explicitly versioned scenarios or trajectories. A positive difference is not “savings realized”; realized savings require an agreed measurement-and-verification method and observed outcome evidence.

The output is SHADOW/advisory. This design does not authorize device commands, claim customer savings, or decide whether cost analysis or recommendations lead the MVP. It keeps retail-consumer settlement, PV producer export/feed-in settlement, and optional site-economic roll-up as distinct scopes. Remote PV must not become another customer's bill credit without the required legal, contractual, topology, and settlement evidence.

## 2. Inputs and trust conditions

A calculation request identifies tenant, site, subject meter/contract, scope, period, requested calculation kind, and optional baseline/scenario references. Tenant and site authorization must come from authenticated context, not request-body identifiers alone.

The evaluator consumes immutable or versioned references to:

- telemetry or settlement quantities with source, observed/received time, units, quality, coverage, and correction lineage;
- Energy Graph resolution for meter, site, contract, tariff applicability, and effective-dated relationships;
- tariff/rule set and clock/boundary policy;
- invoice/bill evidence for reconstruction;
- baseline/scenario definition for comparison;
- evaluator build/configuration and calculation request.

Missing identity, ambiguous meter-to-contract mapping, unknown tariff rule, unsupported time boundary, invalid unit, insufficient coverage, or cross-scope aggregation without an explicit policy must prevent a definitive monetary result. The system may return a blocked/partial assessment with reasons and evidence references.

## 3. Calculation flow

1. **Authorize scope.** Resolve authenticated principal to tenant/site permissions; reject caller-selected scope that exceeds them.
2. **Resolve subject.** Bind meter/contract/tariff and time interval against effective-dated Energy Graph context. Preserve the resolution version and ambiguity status.
3. **Resolve source quantities.** Select eligible measured/settled quantities under explicit quality, freshness, unit, correction, and clock policies. Keep received time distinct from event/settlement time.
4. **Resolve rules.** Select the applicable tariff and contract version by effective period. Unknown demand window, tax/installation-use formula, rounding order, or other required G1 rule blocks bill-grade calculation; do not insert a guessed default.
5. **Calculate components.** Produce deterministic, typed components with quantity basis, tariff/rule reference, calculation trace, currency, period and status. Keep demand charges, energy charges, adjustments, taxes/fees and export remuneration distinguishable where evidence supports them. Component catalogue and class-specific applicability remain policy/data, not hard-coded assumptions in this document.
6. **Assess coverage and confidence.** Record expected/observed interval coverage, excluded or estimated inputs, unresolved rules and status. Confidence is not a substitute for missing mandatory evidence.
7. **Compare only when requested.** Evaluate baseline and candidate with the same compatible scope, tariff/rule versions, boundary policy, and evaluator version. If comparability conditions fail, return no delta. Label modeled difference as counterfactual estimate; keep measured outcome separate.
8. **Persist result and replay manifest.** Store immutable references and canonical semantic inputs sufficient to re-run the calculation. A hash alone is not a replay record.
9. **Reconcile when bill evidence exists.** Compare component and total amounts with the invoice under documented rounding/carry-forward behavior; report unexplained variance. Passing a synthetic fixture is not a Golden Bill pass.
10. **Present state and provenance.** Return status, scope, period, result kind, amounts/components when permitted, assumptions, exclusions, data coverage, rule versions, evidence links, and replay identity.

## 4. Result and status semantics

The existing CostResult/ReplayManifest file remains a proposal. Before canonical schema generation, the owner and domain evidence must settle result meaning, field names, decimal grammar/scale, component catalogue, status roll-up, and digest canonicalization.

The result envelope should distinguish:

- result kind: bill reconstruction, interval assessment, or baseline comparison;
- scope: consumer import/settlement, producer export/feed-in, or an explicitly named site scenario;
- status: at minimum complete, partial, blocked, or failed, with stable reason codes;
- period plus named clock/boundary policy;
- amount and currency only where eligible;
- component breakdown and trace references;
- source coverage and evidence references;
- tariff/contract/graph/evaluator versions;
- optional compatible baseline/candidate references and modeled delta;
- replay-manifest reference and immutable semantic digest.

Status must roll up conservatively: any mandatory unresolved input blocks a definitive result; optional unavailable detail may yield a partial result if clearly shown. A complete computational run does not establish economic truth if the source evidence or tariff rule is unverified.

Do not expose RecommendationV1 objective.estimatedValue as a verified monetary result. A future recommendation may refer to an eligible assessment, but this design does not decide that contract change or imply RecommendationV2 exists.

## 5. Replay, corrections, and audit

A replay record pins the request, principal/scope context (without placing secrets in the manifest), source object identities and content digests, correction lineage, graph/tariff/clock-policy versions, evaluator build and configuration, baseline/scenario definitions, result digest, and creation time.

Replay uses the exact referenced inputs and versions. A corrected source creates a new assessment/replay lineage; it does not mutate the prior result. Retention, legal hold, deletion, redaction, digest algorithm, canonical JSON/decimal encoding, and storage technology require explicit policy decisions. If any dependency is unavailable or changed, report replay as non-reproducible with the missing/version mismatch reason rather than silently substituting “latest”.

## 6. Product presentation requirements

- Label actual bill evidence, reconstructed amount, interval estimate, forecast, counterfactual delta, and measured outcome with distinct terms and visual treatment; never rely on color alone.
- Show currency, period, subject meter/site, tariff basis, data coverage, freshness, exclusions, and unresolved rules alongside the headline.
- Do not render a green “savings” state from a modeled positive delta alone.
- Provide component expansion, source evidence, calculation trace, and replay status.
- Explain blocked/partial results in operator language, including the data or decision needed to proceed.
- Keep consumer import costs and PV export remuneration separate; any combined view must name the aggregation policy and label it as a site-economic scenario.
- Support keyboard navigation, accessible table equivalents for charts, and visible actual-versus-estimated distinctions under the project's proposed WCAG 2.2 AA review target.

## 7. Failure and recovery behavior

| Condition | Required behavior |
|---|---|
| Missing or unauthorized tenant/site scope | Reject request; do not reveal cross-scope existence |
| Ambiguous meter, contract, or tariff mapping | Block definitive amount; return resolution reason and evidence needed |
| Unknown mandatory G1 tariff parameter | Block bill-grade claim; preserve partial non-authoritative analysis only if its limits are explicit |
| Insufficient or stale telemetry | Mark partial/blocked; list affected intervals and source-health references |
| Duplicate/corrected source data | Preserve source identity and correction lineage; produce a new immutable assessment |
| Incompatible baseline/candidate versions | Refuse delta; show comparison incompatibility reason |
| Replay input unavailable or digest mismatch | Mark non-reproducible; do not substitute latest data |
| Evaluator timeout or dependency failure | Return failed/pending state without partial amount unless partial semantics are explicitly supported and disclosed |
| Invoice mismatch | Show component-level variance and unexplained residual; do not adjust silently to force a match |

## 8. Acceptance evidence

This design area is not accepted until evidence covers:

- at least two real, appropriately redacted Golden Bill cases with matched meter/source evidence and the G1 target of ≤0.5% reconstruction with zero unexplained adjustment, or a formally recorded revised criterion;
- class/contract-specific demand-window, tax/fee, rounding and settlement rules, including unresolved exceptions;
- deterministic replay of a pinned assessment and explicit behavior when a source/rule version is unavailable;
- cross-scope isolation and negative tests for tenant/site authorization;
- complete, partial, blocked, failed, stale, correction and invoice-variance states;
- compatible and incompatible baseline comparison cases, with modeled delta separated from measured outcome;
- accessible product review of terminology and states with target users;
- owner approval of canonical result and replay contracts before generated bindings or production persistence are baselined.

No such evidence is asserted by this draft.

## 9. Open decisions and dependencies

- G1 U-001 demand-window interval, U-009 class-specific fee formula, U-010 real bills, U-011 detailed invoice behavior, U-025 cross-site PV rights, and U-026 official PV-count discrepancy remain governed by their source registers.
- Product owner decision: should the initial workflow prioritize bill reconciliation/cost intelligence, or deliver it alongside shadow recommendations?
- Product owner decision: which primary monetary view, if any, should be shown first (reconstructed bill amount, interval estimate, baseline-relative modeled effect)? Retain explicit separate result kinds regardless.
- Domain owner: decimal representation/scale/rounding, component catalogue, status roll-up, semantic digest and retention/correction policy.
- G6.9-R2: contract-authoring and runtime/persistence choices remain candidates pending Step 3D/4 and Decision Record.
- User/site validation: verify that operators understand evidence coverage, uncertainty, modeled delta and blocked states.

## 10. References

- docs/03-architecture/detailed-design/TARIFF-SETTLEMENT-DETAILED-DESIGN-v0.1.md
- docs/03-architecture/detailed-design/VS-001-RESULT-AND-REPLAY-CONTRACT-PROPOSAL-v0.1.md
- docs/03-architecture/detailed-design/RECOMMENDATION-AND-OPERATOR-REVIEW-DETAILED-DESIGN-v0.1.md
- docs/03-architecture/detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md
- docs/01-research/gates/G1-tariff-settlement.md
- docs/00-authority/decisions/DECISIONS.md and OPEN-QUESTIONS.md
