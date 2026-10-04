# Product Design Baseline

**Status:** Research-derived product baseline; user workflows and commercial assumptions require validation.  
**Authority:** Original G0–G7 research framework, current G1/G7 evidence status, and current handoff.  
**Purpose:** Define what the first product should help a Macau commercial-site team do, and keep the MVP inside what current evidence can support.

## Product statement

Macau Commercial Energy OS is an enterprise energy-intelligence and orchestration product for commercial buildings and sites. It joins meter and building-system data with physical assets, contracts, tariffs, and settlement rules so teams can understand energy cost, evaluate safe actions, and verify outcomes.

The product is not a generic consumption dashboard, a replacement BMS, or an autonomous controller. Its primary job is evidence-bounded economic source/load dispatch: compare how grid imports, on-site generation, storage and eligible flexible loads can be scheduled over a shared horizon, explain the constraints and economics that the evidence supports, and retain a replayable review record. Portfolio status, cost intelligence and evidence management support this task; they do not replace it.

## Primary product task: economic source/load dispatch

For an authorized commercial-site user, the core task is to prepare and review a same-horizon baseline/candidate schedule. The model may include grid import, on-site PV, ESS charge/discharge, and site-qualified flexible loads such as HVAC, EV charging or hot water. A source or load is eligible only when its site mapping, measurement/provenance, technical capability, operating limits and applicable authority are supported for the requested period.

The workflow is: qualify data and contracts → resolve the site's physical energy model and separate settlement relationships → compare interval-aligned schedules → inspect energy balance, constraints and evidence → calculate economic effects only when the applicable tariff/contract inputs are verified → record a SHADOW review → monitor and replay against later measurements.

Physical energy flow and financial settlement are distinct views. Unknown capability, SOC, comfort limits, meter mapping, demand window or settlement rights are blockers, not zero or unlimited values. When economics are blocked, the interface may present an explicitly labelled physical scenario comparison, but must suppress bill-grade cost, savings, export credit and ROI claims. MVP review remains advisory and has no device-write path.

## Customer and user hypotheses

These are research hypotheses, not validated segment rankings:

- **Initial site types:** integrated resorts, hotels, shopping malls, office towers, public buildings, and later EV-heavy parking or refrigeration/cold-chain sites.
- **Energy/facilities manager:** needs to understand site demand, equipment context, constraints, and operational recommendations.
- **Finance/asset owner:** needs traceable bill reconciliation, cost exposure, and credible savings evidence.
- **Building operator / control-room staff:** needs safe, explainable recommendations that respect comfort, SLA, and manual authority.
- **Energy service or integration partner:** may configure meters, BMS connections, site assets, and customer-approved operating policies.

Validate roles, buying authority, willingness to pay, and workflow frequency through interviews and pilot observation before fixing segment priority or commercial packaging.

## User outcome and first workflow

The MVP validates this dispatch-first sequence:

1. **Qualify inputs:** identify the site, time horizon, source snapshot, telemetry quality, meter/contract links and unresolved evidence.
2. **Resolve the site model:** map grid import, on-site PV, ESS and eligible flexible loads to verified physical/electrical relationships; keep settlement/economic mappings separate.
3. **Compare schedules:** inspect a baseline and candidate on the same horizon and interval grid, including source contribution, load, storage state where known, and whole-horizon effects such as rebound.
4. **Explain feasibility and value:** expose each applicable technical, comfort, contractual and safety constraint. Calculate cost only when G1 inputs are sufficient; otherwise show which economic result is blocked.
5. **Review in SHADOW:** record an advisory disposition and rationale without authorizing or executing equipment changes.
6. **Monitor and replay:** link later measured outcomes to the original inputs, rules, model version, schedule and review record.

## Conceptual product areas

These are information areas for product design, not a finalized screen specification:

- **Dispatch workspace (primary):** shared-horizon baseline/candidate source/load schedules, interval balance, qualified resource scope, constraints, evidence status and SHADOW review.
- **Site and Energy Graph:** physical/electrical source-load topology kept distinct from settlement relationships, contract links and provenance.
- **Economics and tariff evidence:** cost/demand interpretation and bill reconstruction only when applicable meter, contract, tariff and settlement evidence supports the result.
- **Data health and integrations:** source freshness, point mapping, quality, connector health and downstream impact on dispatch/economics.
- **Portfolio and site overview (supporting):** site readiness, open evidence gaps and links into the active site's dispatch task.
- **Assessment history, monitoring and replay:** pinned input snapshots, model/rule versions, review disposition and later measured outcomes.

Usability, information hierarchy, and role-specific permissions must be validated with pilot users.

## MVP boundary

### Included

- Telemetry ingestion and data-quality visibility.
- Energy Graph resolution for meters, assets, sites, contracts, and tariff references.
- Fail-closed tariff resolution and bill/cost analysis where evidence is adequate.
- Evidence-bounded source/load schedule assessment for in-scope grid import, on-site PV, ESS and site-qualified flexible loads; same-horizon comparisons, explicit constraints and SHADOW-only review. Monetary effects remain blocked when applicable G1 evidence is unresolved.
- Forecast/optimization interfaces behind versioned contracts; proposals only, with no equipment command path.
- Evidence records, deterministic replay, and measurement/verification support.
- Tenant/site isolation, audit, and safe Edge command boundaries even when commands are disabled.

### Excluded until separate evidence and authorization gates pass

- Autonomous safety-critical control.
- Claims of Macau customer savings based only on synthetic fixtures or reference simulations.
- Unverified demand interval, tax, rounding, PV/ESS settlement, or cross-building netting assumptions.
- Replacing BMS, tariff/settlement systems of record, or customer operational approval.
- Treating an LLM recommendation as an executable command.

## Product acceptance evidence

A dispatch increment is ready for a pilot only when a target user can inspect an interval-aligned baseline/candidate schedule for a named site using traceable, freshness-qualified inputs; understand which sources/loads are eligible and why; see unresolved constraints and horizon-wide rebound; and distinguish physical balance from any supported economic calculation. Unknown economics must block monetary output. Before claiming realized commercial value, require a customer-agreed baseline and bill-linked measurement/M&V. Before any controlled action, require G6 safety evidence, G7 live evidence, and explicit customer authorization.

## Open product decisions

- Which Macau segment and buyer is the first paid pilot? (Validate under G0/product discovery.)
- Which data access path and site integration burden is acceptable?
- Which cost/savings metric will a customer accept as contractual evidence?
- What are the user-specific approval and escalation workflows?
- How should deployment packaging and pricing vary by Shared, Dedicated, or Private delivery?

Record answers as evidence-backed decisions; keep hypotheses visibly provisional.
