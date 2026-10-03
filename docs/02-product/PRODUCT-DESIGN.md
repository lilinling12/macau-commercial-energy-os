# Product Design Baseline

**Status:** Research-derived product baseline; user workflows and commercial assumptions require validation.  
**Authority:** Original G0–G7 research framework, current G1/G7 evidence status, and current handoff.  
**Purpose:** Define what the first product should help a Macau commercial-site team do, and keep the MVP inside what current evidence can support.

## Product statement

Macau Commercial Energy OS is an enterprise energy-intelligence and orchestration product for commercial buildings and sites. It joins meter and building-system data with physical assets, contracts, tariffs, and settlement rules so teams can understand energy cost, evaluate safe actions, and verify outcomes.

The product is not a generic consumption dashboard, a replacement BMS, or an autonomous controller. Its initial promise is trustworthy cost intelligence and evidence-backed recommendations.

## Customer and user hypotheses

These are research hypotheses, not validated segment rankings:

- **Initial site types:** integrated resorts, hotels, shopping malls, office towers, public buildings, and later EV-heavy parking or refrigeration/cold-chain sites.
- **Energy/facilities manager:** needs to understand site demand, equipment context, constraints, and operational recommendations.
- **Finance/asset owner:** needs traceable bill reconciliation, cost exposure, and credible savings evidence.
- **Building operator / control-room staff:** needs safe, explainable recommendations that respect comfort, SLA, and manual authority.
- **Energy service or integration partner:** may configure meters, BMS connections, site assets, and customer-approved operating policies.

Validate roles, buying authority, willingness to pay, and workflow frequency through interviews and pilot observation before fixing segment priority or commercial packaging.

## User outcome and first workflow

The MVP validates this sequence:

1. **Connect a site:** register organization/site boundaries, meters, relevant BMS/asset feeds, and source quality.
2. **Understand the site:** resolve telemetry to the Energy Graph; show what is measured, inferred, missing, stale, or rejected.
3. **Reconcile economics:** associate meter → customer contract → applicable tariff version; calculate cost only when required inputs resolve, otherwise fail closed and show the missing evidence.
4. **Review cost and risk:** explain consumption, tariff drivers, demand exposure, and uncertainty with traceable source data.
5. **Evaluate a recommendation:** run optimization in shadow mode; show baseline, proposed action, predicted effect, constraints, and assumptions.
6. **Verify and learn:** create an Evidence Record that can be replayed and compared against actual outcomes.

## Conceptual product areas

These are information areas for product design, not a finalized screen specification:

- **Portfolio and site overview:** site status, data freshness, major cost/demand signals, and open evidence gaps.
- **Data health and integrations:** meter/BMS feeds, mapping status, quality, and connector health.
- **Site and Energy Graph:** assets, meters, electrical relationships, contracts, settlement relationships, and provenance.
- **Tariff and bill intelligence:** versioned tariff resolution, bill reconstruction, Golden Bill comparisons, and explicit unresolved items.
- **Cost and demand analysis:** consumption/cost breakdown, demand exposure, and confidence/coverage.
- **Recommendations (shadow):** prioritized, explainable proposals; baseline comparison; constraints; expected effect; no direct control in MVP.
- **Evidence and replay:** input snapshot, model/rule versions, calculation path, decision trace, and M&V result.

Usability, information hierarchy, and role-specific permissions must be validated with pilot users.

## MVP boundary

### Included

- Telemetry ingestion and data-quality visibility.
- Energy Graph resolution for meters, assets, sites, contracts, and tariff references.
- Fail-closed tariff resolution and bill/cost analysis where evidence is adequate.
- Forecast/optimization interfaces behind versioned contracts; shadow recommendations only.
- Evidence records, deterministic replay, and measurement/verification support.
- Tenant/site isolation, audit, and safe Edge command boundaries even when commands are disabled.

### Excluded until separate evidence and authorization gates pass

- Autonomous safety-critical control.
- Claims of Macau customer savings based only on synthetic fixtures or reference simulations.
- Unverified demand interval, tax, rounding, PV/ESS settlement, or cross-building netting assumptions.
- Replacing BMS, tariff/settlement systems of record, or customer operational approval.
- Treating an LLM recommendation as an executable command.

## Product acceptance evidence

A product increment is ready for a pilot only when its target user can complete the intended task using traceable inputs and the system makes missing/uncertain evidence visible. Before claiming commercial value, require a real customer baseline and bill-linked measurement agreed with the customer. Before any controlled action, require G6 safety evidence, G7 live evidence, and explicit customer authorization.

## Open product decisions

- Which Macau segment and buyer is the first paid pilot? (Validate under G0/product discovery.)
- Which data access path and site integration burden is acceptable?
- Which cost/savings metric will a customer accept as contractual evidence?
- What are the user-specific approval and escalation workflows?
- How should deployment packaging and pricing vary by Shared, Dedicated, or Private delivery?

Record answers as evidence-backed decisions; keep hypotheses visibly provisional.
