# Product Requirements Draft v0.1

**Status:** Research-derived draft; not approved for production scope  
**Authority:** `PRODUCT-DESIGN.md`, G0–G7 research framework, Decision Register, Open Questions, and current handoff  
**Customer validation:** Not yet demonstrated in this repository  
**MVP operating mode:** Shadow/advisory; no autonomous safety-critical control

## 1. Product intent

Macau Commercial Energy OS helps commercial-site teams plan and review evidence-bounded economic source/load dispatch. Its primary workflow compares interval-aligned baseline and candidate schedules for grid imports, on-site PV, ESS and site-qualified flexible loads, then explains technical constraints, supported economics and later measured outcomes. It joins telemetry and the physical energy model to contracts, tariffs and settlement evidence without conflating energy flow with billing rights.

The first release must make evidence gaps visible. It must not present assumed settlement inputs, synthetic reference-building outcomes, or an AI-generated explanation as verified customer economics.

This draft turns existing research into testable product requirements. It does not finalize customer segment, commercial packaging, screen design, technical stack, or field-control authorization.

## 2. Users and jobs to be validated

These are candidate roles from current research, not confirmed buyer research:

- **Energy or facilities manager:** understand site demand, data quality, equipment context, cost drivers, and operational recommendations.
- **Building operator / control-room staff:** review safe, explainable recommendations and retain manual operating authority.
- **Finance / asset owner:** reconcile bill components and assess whether measured value is credible.
- **Energy-service / integration partner:** configure site, meters, BMS mappings, assets, and customer-approved policies.

Before fixing role permissions or navigation, validate who uses each workflow, who approves actions, who pays, how often the task occurs, and what evidence each role accepts.

## 3. MVP outcome and boundary

### Intended outcome

For an in-scope site, an authorized user can:

1. qualify the source snapshot, contract evidence, meter mappings and site-time horizon;
2. resolve which grid, on-site PV, ESS and flexible-load resources are supported for that site and interval;
3. compare a baseline and candidate source/load schedule over the same intervals, including constraints and whole-horizon effects;
4. inspect cost only when applicable tariff, demand and settlement evidence supports it, otherwise see an explicit blocked state;
5. record a SHADOW review that does not authorize or execute a device action; and
6. preserve and replay inputs, versions, schedule and review state against later measurements.

### Included in the first product increment

- Organization/site context and tenant/site-scoped access.
- Telemetry ingestion and visible data quality/provenance.
- Energy Graph resolution for the in-scope site, meters, assets, contracts, and tariff references.
- Effective-dated tariff resolution and cost/bill analysis only when required inputs are supported.
- Source/load dispatch assessment and schedule comparison over a shared horizon, with verified eligibility and limits for each included resource; unknown parameters block feasibility/economic claims.
- Forecast and optimizer integration through versioned contracts, operating in shadow/advisory mode.
- Recommendation explanation with baseline, constraints, assumptions, uncertainty, and expected effect.
- Evidence Record, audit trail, and deterministic replay.
- Site integration and run health visible to the responsible operator.

### Excluded until separate evidence and authorization gates pass

- Autonomous safety-critical device control.
- Treating a recommendation or LLM output as an executable command.
- Bill-grade claims for unresolved tariff/measurement rules.
- Macau customer ROI claims based only on synthetic fixtures or reference simulation.
- Cross-site PV allocation/netting without verified regulatory, contract, meter, and CEM settlement evidence.
- Replacing the BMS or the customer’s settlement system of record.

## 4. Product requirements

### PR-01 — Site and tenant scope

Every user-visible result and stored record must resolve to an authorized organization and site. Requests or events crossing tenant/site boundaries must be rejected and auditable.

**Acceptance:** A record scoped to another tenant cannot appear in the current user’s view, affect its calculations, or produce a recommendation.

### PR-02 — Data quality and provenance

For each relevant telemetry series, the product must expose source, event time, ingestion time, unit, measurement quality/freshness, and Energy Graph mapping status/version. Mapping resolution and measurement freshness/quality are separate dimensions: a stale measurement does not invalidate a mapping, and a valid mapping does not make old or invalid data usable. Missing, stale, uncertain, rejected, or unmapped inputs must remain visible.

**Acceptance:** When required inputs are stale, unmapped, or invalid, the product identifies the affected result and does not silently substitute a plausible value. Graph mapping outcomes (`UNMAPPED`, `AMBIGUOUS`, `CONFLICT`, `EXPIRED_MAPPING`) remain distinct from telemetry freshness and quality states.

### PR-03 — Energy Graph context

The product must distinguish physical/electrical relationships from settlement/economic relationships and link measured meters to applicable contracts and tariff references through explicit, time-aware mappings.

**Acceptance:** An operator can inspect the provenance path from a displayed measure to its site, asset/meter mapping, contract, and tariff version. Ambiguous mappings are flagged instead of guessed.

### PR-04 — Tariff and bill analysis

The product must resolve tariff and contract rules by effective time and retain the version and inputs used. Unresolved settlement rules must fail closed for bill-grade outputs; scenario-only results must be visibly labelled with their assumptions.

**Acceptance:** A result crossing an effective-date boundary uses the applicable versions for each interval. If a required rule is unknown, the product shows the missing evidence and withholds a bill-grade result.

**Authority constraint:** Where a Golden Bill gate applies, reconstruction must meet the Authority target of error ≤0.5% with zero unexplained balancing adjustment before the tariff capability is called production-ready.

### PR-05 — Cost and demand explanation

The product must present cost/demand results with component-level traceability, input coverage, unresolved evidence, and the calculation/rule version. It must distinguish energy quantities and settlement quantities, and keep bill reconstruction, interval assessment, and baseline comparison as separate result kinds. A modeled baseline difference is not realized savings.

**Acceptance:** A user can navigate from a reported cost component to the contributing measurements, tariff/contract version, calculation trace, and evidence status. The user can distinguish a bill result (or why it is blocked), an interval estimate, and a counterfactual comparison without conflating their values or evidence.

### PR-06 — Shadow recommendation

The optimizer may produce a recommendation, but the MVP must not directly execute it. Each recommendation must identify its time horizon, baseline, proposed action, constraints, model/version, expected effect, uncertainty, and assumptions.

**Acceptance:** A user can distinguish predicted from measured outcomes; a proposal cannot enter a device-write path while the MVP remains in shadow mode.

### PR-07 — Evidence, audit, and replay

For each material cost result or recommendation, the product must preserve enough versioned input and execution context to explain and replay the result, including relevant source/mapping/rule/model versions and timestamps.

**Acceptance:** Replaying an unchanged evidence snapshot with unchanged versions reproduces the same business result and stable semantic identity. Operational trace identifiers must not change the business result. Corrected inputs create a new assessment lineage; unavailable or changed replay inputs are disclosed rather than silently replaced.

### PR-08 — Operator review and authority

The interface must keep recommendation, review/approval, authorization, command, acknowledgement, and observed physical effect as separate states. Manual override and rejection remain visible and auditable.

**Acceptance:** An unapproved recommendation remains non-executable; a rejected or expired proposal cannot be represented as applied. Reviewed/dismissed/needs-evidence dispositions remain separate from command authorization, measured physical effect, and outcome evidence.

### PR-09 — Integration and run health

The responsible user must be able to identify whether source integrations are connected, delayed, failing, or producing rejected/unmapped data, and understand which product results are affected.

**Acceptance:** A failed or stale source is surfaced with its effect on coverage and downstream calculations rather than hidden behind a green aggregate status.

### PR-10 — Economic source/load dispatch

The product must let an authorized user inspect and compare a baseline and candidate energy schedule for the same site, horizon, timezone and interval grid. The candidate may include grid import, on-site PV, ESS charge/discharge, and in-scope flexible loads such as HVAC, EV charging or hot water only when the source, mapping, capability, contract/site authority and applicable operating limits are evidenced for that period.

Each interval must make source contribution and load demand inspectable, preserve energy-balance semantics and expose applicable technical/comfort constraints, storage state/efficiency/reserve where supported, and full-horizon effects such as rebound. Physical energy flow must remain separate from customer settlement and bill calculation. Unknown constraints must not be treated as zero, unlimited or permissive. If applicable tariff, demand-window, contract or settlement inputs are unresolved, the system may present a clearly labelled physical scenario comparison but must block monetary totals, savings, export credits and ROI.

The first product increment is SHADOW/advisory. A schedule review records a human disposition only; it does not create a command, authorize a device write or prove an outcome.

**Acceptance:** For synthetic fixtures, an operator can inspect the same-horizon baseline/candidate schedule in both chart and data-table form, trace each included resource to its evidence/status, see a blocked reason for unresolved capability/economic inputs, and identify whole-horizon rebound or peak changes. The interface labels all synthetic values, exposes no device-execution affordance, and does not state realized savings. These checks do not prove a Macau site, optimizer or tariff result.

## 5. Product-level quality requirements

- **Correctness:** monetary truth uses decimal arithmetic and explicit units; effective-dated decisions are reproducible.
- **Safety:** AI and optimization may propose but cannot bypass the Safety Kernel or site-local authority.
- **Isolation:** tenant/site boundaries apply to APIs, events, workflows, storage, evidence, and Edge identity.
- **Auditability:** material configuration, calculation, review, and command-state changes have attributable records.
- **Resilience:** duplicate or retried telemetry/commands do not create duplicate business effects; outage behavior is explicit.
- **Transparency:** users can distinguish verified, derived, hypothesis, project assumption, and unknown information.
- **QLR-01 Localization readiness (proposed):** externalize user-visible text and keep domain contracts locale-neutral so the validated pilot language set can be supported without changing domain calculations. Candidate locales for WP-4 are Traditional Chinese (`zh-Hant`), Portuguese (`pt`, regional preference to be confirmed), and English (`en`); no locale is selected. Date/number/currency formatting, fallback, translation provenance, accessibility metadata and language preference precedence are specified in a separate design proposal and require user/owner review.
- **Accessibility, response time, availability, retention, and support targets:** to be set after user discovery and architecture/SLO design; this draft does not invent numeric targets.

## 6. Pilot acceptance and success measures

Pilot success measures must be agreed with the pilot customer before the measurement period. Candidate measures include:

- coverage and freshness of required meter/BMS data;
- successful mapping of in-scope meters and assets;
- tariff/bill reconstruction error and unexplained adjustment count;
- operator task completion and recommendation review behavior;
- recommendation performance against a reproducible baseline;
- comfort, equipment, site-limit, and rebound impacts where live control experiments are authorized;
- measured economic value against a customer-approved baseline and bill method.

Do not publish a savings or ROI result until the customer baseline, applicable tariff/contract semantics, measured inputs, and M&V method are agreed and traceable.

## 7. Release gates

- **Product definition:** user roles, primary jobs, first paid-pilot segment, data access, and customer value measures validated or explicitly retained as hypotheses.
- **Bill-grade economics:** G1 evidence and Golden Bill acceptance conditions satisfied for the relevant tariff/contract.
- **Controlled field action:** G6 safety evidence, G7 live evidence, production command identity/signing decisions, and explicit customer authorization are all required. G6.9-R2 stack status is tracked separately.
- **Pilot claims:** simulated and live evidence are reported separately; claims match the evidence level.

## 8. Open product decisions

1. Which Macau segment and buyer is the first paid pilot?
2. Which users own configuration, review, approval, and escalation?
3. What meter/BMS data access is available at an acceptable integration cost?
4. Which bill/cost/savings evidence will the customer accept contractually?
5. Which deployment mode (Shared, Dedicated, Private) and pricing approach fit the first pilot?
6. Which pilot roles need which written interface, notification, report and support languages? Investigate Traditional Chinese, Portuguese and English as candidates, but confirm language per role/site and terminology in WP-4; official-language status and business use are discovery context, not proof that all locales belong in MVP.
7. Which service-level, retention, and support commitments are required?

Resolve these through interviews, site observation, sample artifacts, and pilot evidence. Record findings in the relevant Gate/evidence and Decision registers before treating them as settled.

## 9. Source traceability

Primary project constraints represented here include:

- D-001/D-002/D-009: product category, economic objective, and MVP foundation.
- D-006/D-007/D-008/D-041/D-046/D-049: safety, AI, demand-guard, and initial control boundaries.
- D-012/D-015/D-017/D-019/D-024/D-026/D-027/D-028/D-029: tariff identity, effective dating, evidence, unknown handling, monetary precision, and Golden Bill validation.
- D-032/D-037/D-043/D-044/D-047/D-048/D-055: simulation vs Macau evidence boundaries and R0 limitations.
- D-070/D-073/D-074/D-075: canonical command identity, observability separation, fixed aggregation windows, and replay protection.
- D-077/U-025: PV export and cross-site settlement boundary.
- Proposed QLR-01 and `docs/03-architecture/detailed-design/LOCALIZATION-AND-I18N-DESIGN-v0.1.md`: locale-ready UI/content separation, source-language provenance, and WP-4 validation; launch languages remain undecided.
- U-001/U-006/U-007/U-008/U-009/U-010/U-011/U-012/U-014/U-016/U-017/U-022: unresolved billing, site data, comfort, calibration, command security, and live response questions.

See `docs/02-product/PRODUCT-DESIGN.md`, `docs/00-authority/decisions/DECISIONS.md`, `docs/00-authority/decisions/OPEN-QUESTIONS.md`, and the G1/G7 evidence records. Update this draft when evidence changes; do not silently convert an assumption into a requirement.
