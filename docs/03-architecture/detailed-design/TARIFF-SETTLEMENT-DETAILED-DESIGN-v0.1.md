# Tariff & Settlement Detailed Design v0.1

**Status:** Stack-neutral design draft; owner review and G1 evidence remain pending.  
**Scope:** Macau commercial retail-bill reconstruction and forward cost evaluation, including the rule-resolution and evidence path.  
**Authority:** D-012, D-015–D-029, D-039–D-040, D-065, current G1 gate and U-001/U-009/U-010/U-011/U-025/U-026.  
**Production status:** Not approved for bill-grade use. This document does not select a runtime, framework, database, or deployment topology.

## 1. Purpose and boundary

Define a deterministic, auditable Tariff & Settlement capability used by historic bill reconstruction and future economic evaluation. It resolves the applicable meter, customer contract, tariff and settlement policy for an evaluation period, calculates only from adequate evidence, and retains a replayable trace.

The Tariff Engine is a domain capability, not a commitment to a standalone microservice. Runtime placement follows the G6.9-R2 decision. Exact settlement rules come from effective-dated, source-backed rule packages. Unknown legal, contract or meter semantics must produce a blocked/partial result; they are never filled by defaults.

The engine handles the customer account's retail settlement stream. Producer-side PV feed-in revenue and any independently approved export arrangement are separate streams. The 2025 concession amendment effective 2026-01-01 limits private self-generated electricity distribution to the same concession/private land parcel with prior written SAR authorization; any such physical flow still requires explicit contract and meter treatment. Do not net off-site PV into another account without verified rights and meter/contract evidence (D-021, D-077, U-025).

### In scope

- Resolve contract, tariff class/subclass, tariff package and applicable policies for a site/account and time range.
- Evaluate bill components from settled/quality-qualified quantities, including demand, active and reactive energy, tariff-clause adjustment, monthly installation-use charge, bill rounding/carry-forward and supported adjustments.
- Reconstruct an issued invoice, explain differences, and keep source evidence and calculation trace.
- Evaluate a forward scenario with the same rule definitions and explicit forecast/assumption mode (D-018).
- Return proposed contract/demand state transitions without mutating customer state (D-025).
- Distinguish verified tariff output from partial analysis, project assumptions and unknowns.

### Out of scope

- Authoritative determination of unresolved Macau legal or CEM rules.
- Inventing a Pu interval, B/C/D installation-use charge formula, component rounding order, or remote PV credit.
- Invoice issuance, payment collection, utility account updates, or production customer ledger posting.
- Arbitrary scripts or customer-authored executable tariff rules (D-022).
- Direct device commands or optimizer execution.

## 2. Authority and evidence rules

Rule packages are immutable once published (D-012). A correction or amendment creates a new package revision and preserves both the effective time and when the system learned the fact (bitemporal identity, D-024). Rates and legal/economic constants are data parameters; formula/mechanism changes version the evaluator separately (D-023).

Every parameter and formula must point to evidence: issuing authority, document/contract identity, article/table/line, source URL or controlled source reference, publication and effective dates, capture date, reviewer, and evidence status. A CEM explanation page may explain a bill field but must not silently override a regulation, tariff dispatch, or customer contract. Conflicts are explicit and block exact settlement until resolved.

Known current constraints:

- Pu/demand integration policy is first-class and distinct from telemetry sample cadence, optimizer step and control cadence (D-027, D-040). U-001 is unresolved; never assume 15 minutes.
- The monthly “政府稅” / “Taxa de Exploração” line is visible in CEM materials; its B/C/D formula and legal/contractual characterization remain unresolved (U-009). A-group/EV examples are not B/C/D authority.
- Invoice amount rounding / odd-amount carry-forward is partially clarified by CEM's published explanation; exact B/C/D calculation order, ledger behavior and adjustments remain unverified (U-011).
- Real Golden Bill cases are unavailable (U-010). A bill-grade release requires at least two real cases, matched settlement/meter evidence, <=0.5% reconstruction error and zero unexplained balancing adjustment.
- Off-site PV account allocation is not established (U-025); CEM/DSPA PV count scope discrepancy remains open (U-026).

## 3. Logical components

These are module boundaries independent of language/framework:

| Component | Responsibility | Invariant |
|---|---|---|
| **Evidence/Rule Catalog** | Store source-backed immutable tariff packages, parameters, formula versions, contract clauses and applicability | No active rule without provenance, review state and effective interval |
| **Settlement Context Resolver** | Resolve account → supply contract → settlement meter → tariff class and site topology for the requested valid time | Exactly one applicable context, or explicit unresolved/conflict result |
| **Quantity Settlement Adapter** | Convert canonical validated measurements and utility-provided settled values into typed tariff quantities | Never equate raw sample cadence to billing window; preserve original and derived quantities |
| **Tariff Evaluator** | Pure deterministic functions for approved tariff mechanics, using decimal money and typed physical units | No I/O, hidden clock, mutable account state, network calls or executable user scripts |
| **Bill Reconciliation** | Compare calculated components and payable total with an issued invoice; classify variances | Never add an unexplained plug/balancing item to force agreement |
| **Trace & Replay Builder** | Pin all inputs, rule/context versions, evidence and intermediate outputs | A replay cannot resolve against “latest” rules or data |
| **Projection Adapter** | Produce candidate optimizer-cost curves from the same rule package | Exact evaluator remains the final economic authority; optimization approximation cannot replace settlement (D-028) |

Implementations may co-locate these modules. Persistence, API, workflow and runtime are deliberately unspecified.

## 4. Input and result contracts (logical)

### Evaluation request

An evaluation request must identify:

- tenant and authorized account/site scope from authenticated context;
- settlement account/contract and meter reference, or enough graph keys to resolve them;
- billing/scenario start and end instants, explicit timezone and boundary policy;
- valid-time mode and system/knowledge-time cutoff (current reconstruction vs decision-time replay);
- source quantity references and provenance, or source event set with immutable IDs;
- evaluation mode: `RECONSTRUCTION`, `HISTORICAL_REPLAY`, or `FORWARD_SCENARIO`;
- optional issued bill reference for comparison; never treat it as rule authority by itself.

Physical values include explicit unit, interval boundaries, source, quality, mapping/version and measurement/receipt time. Money is decimal text plus currency; floating-point values are not accepted as final monetary truth (D-026).

### Resolved context

Resolution returns pinned identifiers and versions for account, contract, meter/topology, tariff class/subclass, tariff package, parameter set, demand policy, tax/installation-use policy, rounding/carry-forward policy, time-zone/boundary policy and source evidence.

Each resolved field carries status and valid/system intervals. Resolution returns `RESOLVED`, `PARTIAL`, `UNKNOWN`, or `CONFLICT`; only `RESOLVED` permits exact calculation.

### Evaluation result

Return:

- overall status: `BILL_GRADE`, `PARTIAL`, `PROJECT_ASSUMPTION`, `BLOCKED`, or `FAILED`;
- component results with formula/rule version, quantity, unit, rate/parameter, decimal amount and provenance;
- demand/energy quantities before and after each approved adjustment;
- invoice total, amount payable and carry-forward only if their semantics are resolved;
- coverage and exclusions, uncertainty, unresolved question IDs and stable reason codes;
- differences to issued bill by named component, with no unexplained balancing adjustment;
- proposed Pc/contract state transition as data only (D-025);
- replay manifest identity and content references.

A numeric total without resolved context and component trace is not a valid settlement result.

## 5. Resolution and evaluation flow

1. **Authorize scope.** Bind tenant/account/site from authenticated identity and access policy. A request-body tenant ID is a selector, not proof of authority. Deny and audit cross-tenant references.
2. **Pin time.** Normalize the requested half-open evaluation interval under an explicit Macau timezone and boundary policy. Preserve the source timezone/offset and the exact boundary policy ID. Do not infer tariff time buckets from server-local time.
3. **Resolve bitemporal context.** Resolve supply contract, settlement meter, tariff class/subclass and graph relationship valid at each point in the evaluation interval, as known at the requested system-time cutoff. Split the evaluation at every effective-date boundary.
4. **Resolve immutable rules.** Select tariff, parameter, formula, TCA, demand, tax/installation-use, loss-adjustment, reactive-energy and rounding policies with evidence. Missing, overlapping, expired or contradictory rules block the affected component.
5. **Settle quantities.** Preserve raw meter/BMS inputs. Apply only explicitly authorized mapping, quality, conversion and topology rules. For billing-grade demand, require either a CEM-provided settled Pu with provenance or a verified meter policy and sufficient interval data. Do not derive Pu from arbitrary samples.
6. **Evaluate components.** Execute typed deterministic evaluators. Every intermediate is traceable. An unresolved component remains unresolved; do not substitute zero unless an authoritative rule explicitly establishes zero.
7. **Apply invoice-level policy.** Apply carry-forward, credits, late fees or final payable rounding only in the order/semantics established by authoritative evidence. Until U-011 is resolved, invoice-payable reconciliation is not bill-grade.
8. **Reconcile or project.** In reconstruction mode compare each named bill component and payable amount. In forward mode use the same rules but mark forecast quantities and results as projections. Do not treat a forecast as settled truth.
9. **Persist evidence.** Store immutable input/rule/context references, trace, result and any rejected/blocked reason. Evaluation itself has no side effect on contract state or device state.
10. **Publish only supported claims.** The operator view names missing evidence and separates measured/settled, derived, assumed and unknown values. Bill-grade status requires the G1 acceptance gate, not merely successful arithmetic.

## 6. Tariff package and rule safety

A package is a signed/reviewed declarative document containing applicability selectors, effective intervals, parameter references, references to an allowlisted typed evaluator, required input set, evidence records, revision and lifecycle state. Package loading validates schema, units, parameter completeness, overlap/ambiguity, dates and evidence. Production packages cannot contain arbitrary code, network retrieval, reflection or dynamic evaluation (D-022).

Evaluator implementations are reviewed source code with stable version IDs. A rule-package revision may change parameters without changing formula code; a formula change requires a new evaluator version. Historical runs retain both IDs. A general-purpose DMN/rule engine may support bounded eligibility or explainability only, not authoritative monetary arithmetic (D-031).

## 7. Failure and status behavior

| Condition | Result and operator-visible reason | Bill-grade? |
|---|---|---|
| No/ambiguous contract, meter or tariff mapping | `BLOCKED`; show unresolved entity and valid-time range | No |
| Pu provided without trustworthy provenance, or no verified demand window | Demand component `UNKNOWN`; no demand-charge claim | No |
| B/C/D monthly installation-use formula unresolved | Component `UNKNOWN`; no exact invoice total | No |
| Rates/TCA/contract change inside bill period without an effective-dated split | `BLOCKED`; show boundary and missing version | No |
| Incomplete reactive-energy/time-band quantities | Partial result with omitted component and coverage | No |
| PV export/self-consumption/account rights unclear | Keep producer export separate; block customer-credit allocation | No |
| Invoice rounding/carry-forward semantics unresolved | Show pre-rounding component subtotal only as partial; do not claim amount payable | No |
| Conflicting authoritative sources or post-hoc correction | `CONFLICT`; preserve both sources and require reviewed superseding rule | No |
| Replay lacks any pinned input/rule/build | `FAILED` or `INCOMPLETE_REPLAY`; never substitute current values | No |
| All required rules and quantities resolved and Golden Bill criteria pass | `BILL_GRADE` with component reconciliation and replay manifest | Yes, for exact covered tariff/version/site scope only |

## 8. State, correction and concurrency semantics

Evaluation is pure. Rule/context publication and account state changes are separate commands with explicit reviewer identity, effective time and audit. No evaluation may auto-update Pc, contract demand, account status, carry-forward ledger or customer account. If applicable rules propose a state change, return a typed proposal; a separately authorized operation decides whether it is committed.

Concurrent rule publication must reject overlapping active applicability/effective intervals unless precedence is explicit and reviewed. A later discovered fact creates a new knowledge-time version and preserves the prior result; historical replay can answer both “what is believed now about that bill?” and “what did the system know at the time?”

Idempotency keys are scoped to an evaluation request and its pinned input set. Identical retries return the same semantic result/reference; they do not duplicate ledger writes because evaluation performs none.

## 9. Security, observability and operational requirements

- All reads and writes are tenant/account scoped from authenticated principal context; enforce scope on API, jobs, storage and export paths.
- Rule publication is restricted, reviewed and audited; read-only customer roles cannot activate tariff packages.
- Audit rule changes with actor, reviewer, source evidence, diff, approval time and effective time.
- Logs/metrics contain stable evaluation ID, rule/context IDs, status and reason codes, but avoid exposing customer bills or personal data.
- Track blocked/partial rates by reason, unresolved mapping/tariff counts, reconciliation error by bill component, replay completeness, and rule-publication failures.
- Provide rollback by deactivating a newly published package for future evaluation while preserving historical identities; never rewrite completed evidence.
- SLO, retention, encryption, backup/restore and availability targets remain to be agreed with product/operations after deployment-mode discovery; none are invented here.

## 10. Acceptance evidence and design exit

This design is ready for owner review as a stack-neutral proposal. It is **not** ready for production implementation. Before tariff implementation is authorized:

1. Resolve or explicitly scope U-001, U-009, U-010, U-011 and relevant contract-specific unknowns.
2. Approve product meaning for historical bill reconstruction vs forward cost projection and required user explanations.
3. Define canonical request/result/rule-package/replay schemas consistent with D-065 and the contract-authoring decision.
4. Build versioned Golden Bill fixtures from at least two real tariff-class cases, separately labeled from synthetic fixtures.
5. Meet <=0.5% reconstruction error with zero unexplained adjustment and exact component-level trace for every accepted case.
6. Verify time-boundary, effective-date, decimal, unit, bitemporal, state-transition, correction and replay behavior with acceptance evidence.
7. Complete security/isolation review and operator role/approval model; production tariff writes and device commands are separate authorities.
8. Record the selected implementation runtime only after G6.9-R2 Step 4 and an owner-approved Decision Record.

## 11. Explicit unresolved design decisions

- Exact CEM Pu integration window and whether demand registers differ by class/topology (U-001).
- B/C/D monthly installation-use charge formula, name/legal basis, class applicability and effective dates (U-009).
- Bill component order, amount precision and carry-forward ledger semantics (U-011).
- Source event identity, exact quality/freshness and load-profile normalization contracts (D-065 follow-up).
- Contract/tariff conflict precedence and customer-specific exceptions.
- Which partial economic scenarios are useful to operators without implying bill-grade results.
- Retention/immutability mechanics and replay digest/canonicalization.
- Product rollout, tenant roles, operator review and commercial packaging.

## References

- Macau Administrative Regulation 25/2022 tariff system: https://bo.io.gov.mo/bo/i/2022/26/regadm25.asp
- CEM Tariff Groups B/C/D and bill explanation pages: https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-b/ ; https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-c/ ; https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-d/ ; https://www.cem-macau.com/zh/customer-service/billing-service/understand-my-bill/
- Project G1 unknowns and current evidence: `docs/00-authority/decisions/OPEN-QUESTIONS.md`; `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`.
