# Product Interaction Design v0.1 — Information Architecture and User Flows

**Status:** Research-derived product design draft; target-user interviews and usability validation have not been demonstrated.  
**Purpose:** Translate PRD v0.1 into reviewable navigation, role/task hypotheses, screen responsibilities, and interaction states.  
**Scope:** First Energy OS increment in SHADOW/advisory mode. This is not final visual design, approved scope, or authorization to control equipment.  
**Authority:** PRODUCT-DESIGN.md, PRD-v0.1.md, G0–G7 Authority, G6-safety-control Gate record and VS-001.

## 1. Design intent

The interface should help a commercial-site team answer, in order:

1. Is the site data current and trustworthy?
2. Which measurements, mappings, contracts and tariff versions support this result?
3. What economic conclusion is supported, and what remains unknown?
4. What does the system recommend in shadow mode, against which baseline and constraints?
5. Can the result be reproduced and reviewed later?

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
    ├── Portfolio overview
    ├── Sites
    │   └── Site workspace
    │       ├── Overview
    │       ├── Data health
    │       ├── Site model: Assets & points / Settlement relationships
    │       ├── Economics: Cost analysis / Tariff & contract evidence
    │       ├── Recommendations (SHADOW)
    │       └── Evidence & replay
    ├── Integrations (site-scoped)
    └── Organization access & audit

Keep organization and site visible in titles and breadcrumbs. Give sites stable deep links. Put unresolved issues near affected results. Do not label a feed “Live” without current source data; show last observed and received times. Avoid global green health badges that hide a failed source or blocked calculation. Link recommendations and evidence by stable IDs.

## 4. Primary task flows

### Flow A — Connect and qualify a site

Select/create site → connect an approved telemetry source → inspect points and timestamps → map point to site/device/asset/metric/unit → resolve unknown, conflicting or stale mappings → confirm meter/contract relationships separately → review readiness and remaining blockers.

**Outcome:** the operator understands what is measured and what is missing.  
**Behavior:** never infer asset, unit, contract or tariff from point names alone. Mapping changes are versioned, attributed and effective-dated. Unresolved or cross-site mappings cannot feed authoritative economic results.

### Flow B — Explain a cost or demand result

Choose site and period → inspect coverage and quality → choose meter/settlement view → inspect contract, tariff version and demand policy → view component results and source measurements → inspect uncertainty/excluded inputs → save/share evidence-linked result.

**Behavior:** unknown tariff or measurement rules produce “Not calculated” or a clearly labelled scenario, never a verified bill total or savings value. Never use sampling interval as Pu settlement window without verification. Show site consumption and PV producer feed-in/export separately; off-site PV is not a customer bill credit without verified entitlement.

### Flow C — Review a shadow recommendation

Open recommendation queue → filter by site, period, state and evidence coverage → inspect proposal → compare baseline and current operation → review action, horizon, constraints and assumptions → record reviewed/dismissed/needs-data/comment → revisit later measured outcomes.

**Behavior:** prominently show SHADOW, safetyReviewRequired, validity interval, model/build version, baseline, forecast uncertainty, operating constraints and input coverage. Review actions only annotate the proposal. No “Apply”, “Send” or execution affordance exists in this MVP. Predicted effects remain separate from measured outcomes.

### Flow D — Reproduce and assess evidence

Open evidence → inspect status and source references → inspect input/mapping/tariff/model versions → start replay if all inputs retained → compare replay and stored result → record outcome and limitations.

Incomplete inputs produce “Replay unavailable/incomplete” with missing references; never silently substitute current data, mappings or tariff rules. Trace IDs are diagnostic metadata, not business identity.

## 5. Screen-level requirements

### S-01 Portfolio overview
Show registered sites, source freshness, required-data coverage, unresolved blockers, and latest evidence-backed cost/recommendation timestamps. Mark synthetic/demo sites. Aggregate only compatible verified site bases; otherwise show separate results and a coverage warning.

### S-02 Site overview
Show site identity, local timezone, integration health, data freshness, evidence status, and links to Economics, Recommendations and Evidence. Never show an unqualified savings tile. Display observedAt and receivedAt separately. For offline sources, retain last known result but mark it stale and show its timestamp. Explain each unknown and affected downstream function.

### S-03 Data health
Filterable/searchable points table: source/device/point, canonical asset/metric, unit, quality, last observed, last received, mapping version/status and downstream impact. Support keyboard use, visible focus, text status plus color, and responsive cards or contained horizontal scrolling. Mapping edits show before/after, effective time, actor, validation and confirmation.

### S-04 Site model
Show physical/electrical relationships separately from settlement/economic relationships. Each link displays provenance, valid time, review state and related meters/contracts. Make ambiguous, orphaned or overlapping links inspectable; provide a table/list alternative to graph visualization.

### S-05 Economics
Header states site, period/timezone, result status, meter, contract, tariff version, included/excluded components, coverage and blockers. Show a component breakdown only when the evaluator supplies it. Until a component-result contract exists, show an amount and references as an engineering result, not a complete bill. Charts label axes, units, currency, period boundaries, missing-data gaps and quality filters.

### S-06 Tariff and contract evidence
Show version, effective period, source/evidence links, unresolved parameters and calculation rules. Distinguish regulation, customer contract, project assumption and site configuration. Changes create a new version and audit entry; historical results retain original versions.

### S-07 Recommendation queue/detail
Queue filters by site, validity, evidence coverage, objective and review annotation. Do not show “savings” urgency without a validated rule. Detail sections: SHADOW state and validity; proposed action and affected asset; baseline/horizon; predicted effect/units/uncertainty; comfort/safety constraints; data and tariff status; rationale/model version; review annotations only. Unknown tariff or insufficient data blocks authoritative monetary claims. No action button implies field execution.

### S-08 Evidence and replay
Show evidence ID, status, subject, recorded time, source links, derivation, notes and related results. Replay compares original and replayed output plus pinned versions. If the persistence model lacks a replay manifest, show that limitation instead of a decorative replay control.

### S-09 Integration and site access
Disclose required permissions before credentials are entered. Separate connector authentication from data quality. Show role and site scope; never reveal stored secrets. Identity/delegation UX remains provisional until security architecture is decided.

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
- Built-in UI/UX search matched a real-time operations pattern emphasizing freshness timestamps, stale states and scannable data. Its Glassmorphism style suggestion is not adopted as a design decision: contrast and dense operational readability need user validation before selecting visual styling.

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
