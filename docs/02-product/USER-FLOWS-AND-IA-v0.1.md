# Product Interaction Design v0.1 — Information Architecture and User Flows

**Status:** Research-derived product design draft; target-user interviews and usability validation have not been demonstrated.  
**Purpose:** Translate PRD v0.1 into reviewable navigation, role/task hypotheses, screen responsibilities, and interaction states.  
**Scope:** First Energy OS increment in SHADOW/advisory mode. This is not final visual design, approved scope, or authorization to control equipment.  
**Authority:** PRODUCT-DESIGN.md, PRD-v0.1.md, G0–G7 Authority, G6-safety-control Gate record and VS-001.

## 1. Design intent

The interface's primary job is to help an authorized site user prepare and review evidence-bounded source/load schedules. The task order is:

1. Which site, horizon and evidence snapshot are in scope?
2. Which grid/PV/ESS/load resources and operating constraints are supported for that period?
3. How does the candidate schedule compare with a same-horizon baseline, interval by interval and across the full horizon?
4. Which physical, economic and contractual conclusions are supported, and what is blocked or uncertain?
5. How can a person record a SHADOW review and later compare replay with measured outcomes?

Evidence status must be visible where users interpret a number or recommendation. Distinguish telemetry recency from settlement truth, predicted from measured outcomes, and project assumptions from verified customer evidence.

## 2. User and authority hypotheses

These roles are proposed from current research and must be validated with Macau operators, finance/asset stakeholders and integration partners.

| Candidate role | Primary tasks | Likely access | Must validate |
|---|---|---|---|
| Energy/facilities manager | Review site health, cost drivers, demand exposure and recommendations | Overview, data health, cost analysis, recommendation detail, evidence | Task frequency, decision responsibility, accepted cost/savings evidence |
| Building operator/control room | Check integrations, inspect constraints and review advisory proposals | Site/data status, graph context, recommendation review and annotations | Shift workflow, alert/escalation channels and operational language |
| Finance/asset owner | Review bill-linked economics, contract/tariff evidence and M&V | Cost analysis, tariff/contract provenance and evidence exports | Reconciliation method, required bill components and decision threshold |
| Energy-service/integration partner | Configure devices, point mappings and site context | Integration setup and graph configuration, scoped by authorization | Delegated access, approval controls and integration effort |
| Organization administrator | Manage memberships, site access and audit | Organization/site administration | Identity provider, deployment mode and tenant ownership |

No role is assumed to have device-execution permission in the MVP. Reviewing a recommendation is not approval to change plant operation.

## 3. Proposed information architecture

    Organization / Portfolio
    ├── Sites
    │   └── Site workspace
    │       ├── Dispatch workspace (primary task)
    │       ├── Site readiness overview (supporting)
    │       ├── Data health and integrations
    │       ├── Site model: physical/electrical topology / settlement relationships
    │       ├── Economics: cost assessment / tariff and contract evidence
    │       ├── SHADOW assessment review
    │       └── Monitoring, evidence and replay
    ├── Portfolio overview (supporting; not the primary task destination)
    └── Organization access & audit

Keep organization and site visible in titles and breadcrumbs. Give sites stable deep links. Put unresolved issues near affected results. Do not label a feed “Live” without current source data; show last observed and received times. Avoid global green health badges that hide a failed source or blocked calculation. Link recommendations and evidence by stable IDs.

## 4. Primary task flows

### Flow A — Connect and qualify a site

Select/create site → connect an approved telemetry source → inspect points and timestamps → map point to site/device/asset/metric/unit → resolve unmapped, ambiguous, conflicting or expired mappings separately from stale/invalid measurement quality → confirm meter/contract relationships separately → review readiness and remaining blockers.

**Outcome:** the operator understands what is measured and what is missing.  
**Behavior:** never infer asset, unit, contract or tariff from point names alone. Mapping changes are versioned, attributed and effective-dated. Unresolved or cross-site mappings cannot feed authoritative economic results.

### Flow B — Build and compare a source/load schedule (primary task)

Choose site and horizon → pin the data/evidence snapshot → confirm physical meter/source/load mappings separately from settlement links → identify eligible grid import, on-site PV, ESS and site-qualified flexible loads → compare baseline and candidate schedules on the same intervals → inspect source/load balance, storage trajectory where supported, technical/comfort constraints and horizon-wide effects such as rebound → review cost only if applicable contract/tariff/demand evidence resolves → mark the assessment SHADOW and record a review disposition.

**Behavior:** eligibility and limits are evidence-qualified for the requested period. Unknown capacity, SOC, efficiency, comfort limit, control authority or settlement term is a blocker, never zero, unlimited or permissive. Physical flow and settlement remain separate. When economics are incomplete, allow only an explicitly labelled physical scenario comparison; suppress bill-grade totals, savings, export credits and ROI. A SHADOW review never sends a command.

### Flow C — Explain an economic result when supported

Choose site and period → inspect coverage and quality → choose meter/settlement view → inspect contract, tariff version and demand policy → view supported cost components and source measurements → inspect uncertainty/excluded inputs → save or replay the evidence-linked result.

**Behavior:** unknown tariff or measurement rules produce “Not calculated” or a clearly labelled scenario, never a verified bill total or savings value. Never use sampling interval as Pu settlement window without verification. Show site consumption and PV producer feed-in/export separately; off-site PV is not a customer bill credit without verified entitlement.

### Flow D — Review a SHADOW assessment

Open an assessment → inspect its schedule, source snapshot, baseline, validity horizon, constraints, economic eligibility and uncertainty → record reviewed/needs-data/rejected/comment → revisit later measured outcomes.

**Behavior:** prominently show SHADOW, model/build version, baseline, schedule horizon, forecast uncertainty, operating constraints and input coverage. Review actions only annotate the assessment. No “Apply”, “Send” or execution affordance exists in this MVP. Predicted effects remain separate from measured outcomes.

### Flow E — Reproduce and assess evidence

Open evidence → inspect status and source references → inspect input/mapping/tariff/model versions → start replay if all inputs retained → compare replay and stored result → record outcome and limitations.

Incomplete inputs produce “Replay unavailable/incomplete” with missing references; never silently substitute current data, mappings or tariff rules. Trace IDs are diagnostic metadata, not business identity.

## 5. Screen-level requirements

### S-01 Portfolio overview
Show registered sites, source freshness, required-data coverage, unresolved blockers, and latest evidence-backed cost/recommendation timestamps. Mark synthetic/demo sites. Aggregate only compatible verified site bases; otherwise show separate results and a coverage warning.

### S-02 Site overview
Show site identity, local timezone, integration health, data freshness, evidence status, and links to Economics, Recommendations and Evidence. Never show an unqualified savings tile. Display observedAt and receivedAt separately. For offline sources, retain last known result but mark it stale and show its timestamp. Explain each unknown and affected downstream function.

### S-03 Data health
Filterable/searchable points table: source/device/point, canonical asset/metric, unit, measurement quality/freshness, last observed, last received, Energy Graph mapping version/status and downstream impact as separate fields. Show `EXPIRED_MAPPING` distinctly from stale measurement quality. Support keyboard use, visible focus, text status plus color, and responsive cards or contained horizontal scrolling. Mapping edits show before/after, effective time, actor, validation and confirmation.

### S-04 Site model
Show physical/electrical relationships separately from settlement/economic relationships. Each link displays provenance, valid time, review state and related meters/contracts. Make ambiguous, orphaned, overlapping or expired links inspectable; provide a table/list alternative to graph visualization. Do not fold telemetry freshness into the relationship's mapping status.

### S-05 Economics
Make the selected result kind explicit and keep three separate views: (1) bill reconstruction, with invoice reconciliation and a blocked state until applicable G1/Golden Bill evidence passes; (2) interval assessment, labelled as an estimate with period and tariff assumptions; and (3) baseline comparison, labelled as a modeled counterfactual rather than realized savings. Do not show one result as interchangeable with another. Each view states site, period/timezone, meter/contract/tariff version, included/excluded components, coverage, provenance, unresolved rules and blockers. Show components only when the evaluator supplies them. Charts label axes, units, currency, period boundaries, missing-data gaps and quality filters; any forecast uses a different line style and an accessible table/narrative summary.

### S-06 Tariff and contract evidence
Show version, effective period, source/evidence links, unresolved parameters and calculation rules. Distinguish regulation, customer contract, project assumption and site configuration. Changes create a new version and audit entry; historical results retain original versions.

### S-07 Recommendation queue/detail
Queue filters by site, validity, evidence coverage, objective and lifecycle/review state. Detail shows SHADOW state and validity; proposed action and affected asset; baseline/horizon; predicted effect/units/uncertainty; comfort/safety constraints; data and tariff status; rationale/model version; and append-only review events. Keep generated, blocked, available, reviewed, dismissed, needs-evidence, expired and superseded states distinct where their conditions apply. A review event does not authorize execution or prove an outcome. Do not show “savings” urgency without validated rules; unknown tariff or insufficient data blocks authoritative monetary claims. No action button implies field execution.

### S-08 Evidence and replay
Show evidence ID, status, subject, recorded time, source links, derivation, notes and related results. Keep operator review disposition, replay status and measured-outcome status separate; reviewed does not mean implemented or saved energy. Show “not measured” until an outcome is supported by the agreed measurement-and-verification method. Replay compares original and replayed output plus pinned versions. If the persistence model lacks a replay manifest, show that limitation instead of a decorative replay control.

### S-09 Integration and site access
Disclose required permissions before credentials are entered. Separate connector authentication from data quality. Show role and site scope; never reveal stored secrets. Identity/delegation UX remains provisional until security architecture is decided.

### S-10 Dispatch workspace (primary task)

Make the selected site, timezone, planning horizon, interval, evidence snapshot and SHADOW state visible before users interpret a schedule. Show baseline and candidate on the same time axis with source contributions, total load, import, PV and storage series only where present in the evidence. Provide an equivalent interval table and direct labels; line style, labels and shape must supplement color. Mark synthetic, measured, forecast, estimated and unknown values distinctly.

Keep the physical/electrical balance separate from the tariff/settlement view. Expose resource eligibility, data freshness, mapping provenance, applicable technical/comfort limits and blockers beside the intervals they affect. Show full-horizon peak/rebound summaries as well as interval deltas. When tariff/contract/demand evidence is missing, state that monetary impact is blocked and do not display savings or ROI. Review controls record SHADOW disposition only; no equipment-control affordance appears.

## 6. Cross-cutting interaction and visual rules

- Use direct labels: Verified, Derived, Project assumption, Unknown, Stale, Blocked and Shadow recommendation.
- Pair each warning with the affected meter/result/workflow and next action.
- Keep safety-sensitive execution controls absent from shadow-only flows.
- Use persistent form labels, inline validation and concise error summaries; never rely on placeholders alone.
- All controls are keyboard accessible with visible focus. Status uses text/icon as well as color; normal text contrast is at least 4.5:1.
- Asynchronous actions show loading, success and recoverable failure. Use 44px minimum touch targets where touch operation is expected, with at least 8px between adjacent touch controls.
- Navigation states use stable deep links and participate in browser back/forward history. Restoring a prior view also restores its active navigation state and moves keyboard focus to the view heading.
- Respect reduced motion; live updates must not shift focus or reorder rows while a user is interacting.
- Responsive targets: 375, 768, 1024 and 1440 CSS px. Narrow data tables use card views or labeled contained horizontal scroll.
- Show local timezone and units consistently. Asia/Macau and MOP are proposed defaults, not verified universal settings.
- UI/UX Pro Max search matched a Real-Time / Operations Landing pattern and conditionally suggested Glassmorphism; this is a workspace for sustained, dense operational analysis rather than a marketing landing page, so the pattern is not applied wholesale. Use an opaque, restrained workspace baseline and prototype depth/translucency only where it improves orientation without reducing contrast or chart/table legibility. Pro Max chart guidance favors solid actual versus dashed forecast lines, direct labels, named uncertainty, and a visible table/narrative alternative. This is a research-informed prototype hypothesis, not an approved visual identity. Evaluate against WCAG 2.2 AA requirements, including text contrast, visible focus, reflow and target size; see the [W3C WCAG 2.2 standard](https://www.w3.org/TR/WCAG22/).

## 7. PRD traceability

| Requirement | Main flow/screen | User-visible proof |
|---|---|---|
| PR-01 Tenant/site scope | All workspaces, access settings | Active site context and denied access behavior |
| PR-02 Quality/provenance | S-02/S-03 | Source, timestamps, unit, quality, mapping and result impact |
| PR-03 Energy Graph | Flow A, S-04 | Traceable physical and settlement mappings with effective periods |
| PR-04 Tariff/bill analysis | Flow B, S-05/S-06 | Versions, assumptions and fail-closed unknown state |
| PR-05 Cost/demand explanation | Flow B, S-05 | Components and input/rule trace when supported |
| PR-06 Shadow recommendation | Flow C, S-07 | Advisory mode, baseline, constraints, uncertainty, no execution |
| PR-07 Evidence/replay | Flow D, S-08 | Pinned sources and deterministic/incomplete replay status |
| PR-08 Operator review/authority | Flow C, S-07 | Review annotation separated from approval, command and physical effect |
| PR-09 Integration/run health | Flow A, S-02/S-03/S-09 | Connector state, stale/missing points and downstream impact |

## 8. Validation and completion status

No target-user interviews or usability study were found in current repository evidence. These flows and roles remain hypotheses, not customer-validated design.

For each primary flow, recruit representative energy/facilities, operator and finance users when available. Have them complete realistic tasks in a paper or interactive prototype. Record role/context, task, observed errors, completion, time, confidence, accessibility issues and resulting design decision. Anonymize research and obtain authorization before using real bills or BMS data.

**Product-design exit evidence still required:**
- confirm/revise user roles, buying/operating authority and task frequency;
- validate navigation and primary journeys with target Macau users;
- review screen prototype with keyboard, narrow viewport and accessibility checks;
- derive role permissions and approval policy from customer/site practice;
- align cost/recommendation UI with resolved contracts and actual result schemas;
- approve pilot metrics, support expectations and localization.

Until then, this v0.1 is a design hypothesis and basis for prototype validation, not frozen product scope.


## Follow-up: v0.10 core-workflow prototype review — 2026-10-04

The current nine-destination prototype is v0.10. In one local browser context, selecting each destination exposed its corresponding view and synchronized the URL hash; browser Back restored the previous page and selected navigation state. On the narrow selector, ArrowUp and Enter changed the view and moved focus to the destination heading. At 320, 375, 768, 1024 and 1440 CSS px, document scroll width equaled client width. Wide sample tables remain inside their labeled horizontal-scroll wrappers. These observations do not establish task comprehension, a production workflow, 200% zoom behavior, screen-reader support, localization or WCAG conformance. The screen/flow design remains a hypothesis until authorized WP-4 research and Owner approval.


## Localization and language selection hypothesis

The current screens and task flows are English-first research stimuli, not a supported-language decision. Treat locale choice and terminology as a cross-cutting open product requirement. Validate languages per user, task and artifact with WP-4 participants; official-language context alone does not establish that every role needs every locale. Candidate discovery set: Traditional Chinese (`zh-Hant`), Portuguese (`pt`, regional variant unresolved) and English (`en`). Test long labels, mixed scripts, data dates/numbers/currency, chart legends, alerts, screen-reader language and role handoffs. Keep source bills, contracts, tariff notices and user-provided labels distinguishable from any reviewed translation. Acceptance and initial locale set require user evidence and owner review. See `docs/03-architecture/detailed-design/LOCALIZATION-AND-I18N-DESIGN-v0.1.md`.


## Follow-up: v0.11 temporary recommendation feedback — 2026-10-04

The current nine-destination study stimulus is v0.11; v0.10 is retained as its historical predecessor. This is the same synthetic task flow and recommendation-review hypothesis, with the confirmation copy corrected: the demo state changes only on the current page, resets on reload, and is not persisted, sent to a service, or evidence of execution/outcome. Product review semantics and durable production audit behavior remain subject to user and owner validation.


## Dispatch-first alignment — 2026-10-04

The existing v0.11 prototype opens on a synthetic portfolio/readiness overview and is retained as a supporting workflow study. It does not demonstrate the primary dispatch task. The standalone six-stage source/load prototype in PR #10 is the current dispatch-flow stimulus: input/contract qualification → physical site model → same-horizon schedule comparison → constraints/evidence → SHADOW review → monitoring/replay. The two prototypes therefore cover different workflow layers; neither has owner/user approval, and the focused dispatch flow still needs integration into a complete product shell and representative usability review.
