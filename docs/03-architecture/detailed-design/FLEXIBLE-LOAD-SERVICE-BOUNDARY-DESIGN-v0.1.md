# Flexible-Load Service Boundary Design v0.1

**Status:** Stack-neutral design proposal for G7.9 T1/T6 review. It does not approve an asset as controllable, define a canonical API/schema, select a solver, authorize an equipment write, or close G2/G4/G5/G6/G7.9.  
**Date:** 2026-10-05  
**Purpose:** Specify how source/load dispatch represents HVAC/chiller, EV charging and hot-water flexibility without mistaking an electrical schedule for delivered service.

## 1. Authority and evidence basis

This proposal operationalizes existing research; it does not replace it.

- Main D-002 sets the objective as total economic cost/value rather than minimum kWh.
- D-003 prioritizes HVAC/chiller as the first pilot controllable-asset hypothesis. It does not prove access, response, safe controls, comfort limits or transferable Macau capability.
- D-004 keeps ESS optional and site-economics dependent. D-060 requires explicit recovery/rebound treatment. D-061 does not give MPC a privileged safety or command path.
- D-046/D-049/D-057 constrain the R0 simulator actuator surface and activation semantics. They are evidence for the bounded R0 experiment, not generic authority to actuate commercial HVAC, EV or hot-water systems.
- G2 remains OPEN until the selected site's asset inventory, measured response, duration, operating boundary, recovery and economic mapping are evidenced. Its required outputs distinguish measured flexibility from aggregate public data, simulation and reported practice.
- PRD PR-10 requires same-horizon source/load comparison, evidence-backed capability, service/comfort constraints and no-control SHADOW behavior. The Forecasting and Optimization design requires hard safety/site-policy constraints, rebound/recovery and a replaceable optimizer.
- The current PR #14 Python optimizer is a bounded electrical schedule experiment. It always withholds COMFORT_SERVICE, appropriately, because it has no thermal, mobility or hot-water service evaluator.

Relevant sources: main `docs/00-authority/decisions/DECISIONS.md`; PR #8 `docs/01-research/gates/G2-load-flexibility.md`, `docs/02-product/PRD-v0.1.md` PR-10 and `docs/03-architecture/detailed-design/FORECASTING-AND-OPTIMIZATION-DETAILED-DESIGN-v0.1.md`; PR #10 `G7.9-STEP3-DISPATCH-CONTRACT-IMPLEMENTATION-MAP-v0.1.md`; PR #14 `implementation/optimizer/SHADOW-ASSESSMENT-PROTOTYPE.md`.

## 2. Core domain separation

A schedule states electrical power over a declared interval. It does not by itself say whether the building remains comfortable, a vehicle leaves with sufficient energy, or hot water is delivered at the required service level. Keep three independent assessments:

1. **Electrical profile:** interval-aligned grid import, PV use/export/curtailment, ESS charge/discharge, fixed and flexible load, losses and power balance for a named physical boundary.
2. **Service outcome:** asset-specific satisfaction/violation/unknown against a versioned service profile and applicable observations/forecasts.
3. **Economic evaluation:** separately authorized meter/account/contract/tariff scope and effective-time rules. Physical balance or a service result does not establish a bill component.

The product may show a qualified electrical profile while service or economics is partial/blocked. An unassessed service outcome must never become “feasible”, “optimized”, “ready” or a positive savings claim.

## 3. Proposed logical resource model

Names are conceptual; this is not a table layout or wire schema.

- **Resource identity and physical mapping:** site, asset, electrical boundary, metering points, asset kind and effective period.
- **Electrical capability profile:** valid interval, evidence, allowed modes, power direction, min-on/max power, ramp/response, on/off dwell, availability, cycle limits and boundary conditions. Zero/off is explicit; an absent interval record is not automatically proof the resource was off.
- **Service profile:** resource-specific outcome, hard/soft boundary, measured/forecast state, validity, uncertainty and evidence. Missing inputs yield NOT_ASSESSED/UNKNOWN, not relaxed constraints.
- **Recovery profile:** post-shift recovery/rebound horizon, limits and evidence. Evaluate recovery as part of the comparison; without it, full-horizon benefit/service remains unresolved.
- **Schedule trajectory:** timezone-aware instants, half-open intervals, units/signs, and baseline/candidate under the same horizon and exogenous assumptions.
- **Service assessment:** separate result per resource and claim, linked to schedule/profile/model/input versions and affected intervals; distinct from electrical feasibility and SHADOW review.

Proposed service states for discussion: `NOT_ASSESSED`, `WITHIN_DECLARED_PROFILE`, `VIOLATION`, `PARTIAL`, and `UNKNOWN`. Exact names remain open. `VIOLATION` requires a known applicable hard bound and a measured/modelled value outside it. Missing evidence is `UNKNOWN`/`PARTIAL`, not a violation or proof of safety.

## 4. Resource-specific service contracts

| Resource | Electrical schedule needs | Service state and hard constraints to evidence | Missing-evidence behavior |
|---|---|---|---|
| HVAC / chiller | Power/load trajectory, mode, response/ramp, dwell, availability, plant/zone mapping, fixed versus flexible components. | Relevant zone/return/supply temperatures and humidity; occupied/critical zones; comfort bands; weather/occupancy assumptions; plant limits; response delay, thermal state and recovery/rebound. Points/models/authority are site-specific. | Without a qualified thermal/service trajectory, show an electrical scenario only; comfort/service remains unassessed and the result is not operationally feasible. A known hard-bound breach is infeasible for that profile. |
| EV charging | Charger power, connection/availability windows, charger limits and efficiency assumptions; vehicle/charger identity and electrical boundary. | Initial SOC or required delivered energy; departure time and target energy/SOC; efficiency and user/vehicle/charger constraints; site import/phase limits where applicable. Availability and targets must be effective-dated and authorized. | Without a verified target/window, mobility service is unassessed. Total kWh alone cannot establish departure readiness. Do not assume V2G, export or cross-account credit; those require separate equipment, interconnection and settlement evidence. |
| Hot-water service | Heater/heat-pump electrical trajectory, mode, response/ramp, thermal storage mapping and recovery window. | Tank/loop state and calibrated model if used; draw profile; delivery temperature/volume; reserve/recovery; equipment and hygiene-cycle requirements where applicable. Electricity use does not establish these. | Without draw/service or thermal-state evidence, service remains unassessed. Shifted/stored kWh does not prove delivery temperature, volume, reserve or cycle completion. A known approved hard-bound breach is infeasible. |
| ESS (cross-cutting) | Charge/discharge power/direction, interval energy, losses/efficiency and explicit SOC trajectory. | Current SOC evidence, usable capacity, min/max SOC, reserve, ratings, degradation/cycle policy, mode and terminal/recovery boundary. | Preserve only independent electrical profile; withhold ESS feasibility when SOC/capability evidence is missing or stale. Never assume zero initial energy or unlimited power/capacity. |

These are evidence categories, not a universal commissioning checklist. Pilot engineering/security review must identify exact points, sampling, quality, access, calibration and customer/site authority.

## 5. Claim and optimization rules

- Compare total eligible cost/value (D-002) only over explicitly named, compatible settlement scopes and approved components. Label electrical-only objectives accordingly.
- Preserve hard limits as constraints. Do not trade safety, comfort, process, mobility, hot-water service, equipment protection or customer policy against lower modeled cost.
- Keep service outcomes resource-specific. One site-wide COMFORT_SERVICE badge cannot summarize EV departure readiness or hot-water service.
- A changed resource needs a current capability profile over every affected interval. Unknown availability, power envelope or state limits withhold that dispatch claim while preserving independent profile/economic claims.
- Quantify recovery/rebound over the full evaluation horizon, including shifted peaks. A target-window reduction alone is not a benefit.
- Share exogenous assumptions between baseline and candidate; disclose weather, occupancy, production, vehicle arrival/departure, hot-water draw, uncertainty and coverage.
- Distinguish measured, derived, modelled, scenario-assumed and unknown values with provenance, valid/recorded time and version. Replay uses pinned inputs/models/policies.
- Keep the product SHADOW-only. A review disposition is not control authorization. R0's simulator actuator surface cannot be generalized to a site or another asset category.

## 6. Acceptance examples for domain review

1. **HVAC shift with no thermal model:** show a balanced electrical scenario when its inputs qualify; service is NOT_ASSESSED/UNKNOWN; withhold operational feasibility and comfort-preserving savings.
2. **HVAC trajectory breaches a verified comfort bound:** mark the affected resource/service profile infeasible; retain unrelated results only where their inputs are independent.
3. **EV energy arrives after departure:** with a verified authorized target/window, mark service infeasible; do not average a miss away across site assets.
4. **EV target or availability absent:** withhold mobility and flexible-dispatch claims; do not assume arbitrary shift windows.
5. **Hot-water kWh matches baseline but temperature/draw evidence is absent:** report electrical energy only; service is unassessed.
6. **Hot-water schedule violates evidenced reserve or hygiene cycle:** reject as service-infeasible even if grid-import cost improves.
7. **ESS power balance qualifies but SOC evidence is missing/stale:** retain independent electrical profile; withhold ESS and overall dispatch-feasibility claims.
8. **Resource inactive/off in an interval:** represent zero explicitly in the candidate. A missing interval record is incomplete data unless the declared schedule boundary says otherwise.
9. **Recovery window is shorter than the evidenced response:** withhold full-horizon benefit/service claims and disclose the unobserved remainder.
10. **One resource's service limits are unknown, another's are qualified:** return per-resource states so missing evidence does not erase independent results or falsely qualify the site.

These are proposed semantic acceptance cases. The prototype/UI/API must eventually share a versioned claim vocabulary; PR #14 does not bind an authenticated site resource registry or service evaluator.

## 7. T1/T6 trace and remaining proof

| Requirement | Existing evidence | Remaining proof |
|---|---|---|
| Economic rather than kWh-only objective | D-002; Forecasting/Optimization design §4 | Account-specific settlement and eligible objective components under open G1. |
| HVAC/chiller first pilot hypothesis | D-003; R0 and G2 | Real-site points, constraints, access, response, comfort effects and rebound. |
| ESS optional/site-economics dependent | D-004; bounded PR #14 power/SOC checks | Real BMS/PCS capability, SOC quality, reserve, losses, degradation and economics. |
| EV and hot-water service requirements | PRD PR-10 when evidence exists; this proposal's typed requirements | Customer/asset model, meter, service constraints and site evidence. No V2G assumption. |
| Electrical profile vs service/economics | PR #10 map; PR #14 withholds COMFORT_SERVICE | Canonical cross-runtime contract, typed service results, UI state binding and service validation. |
| Site flexibility | G2 remains OPEN | Site-authorized repeatable baseline/response/recovery measurement. Public aggregates and BOPTEST are insufficient. |
| Edge/control limit | D-046/049/057/061 and read-only Edge proposal | Read-only acquisition/identity and safety evidence; actuation remains separately gated. |

## 8. Decisions intentionally left open

- Which assets the first paid-pilot scope includes; D-003 makes HVAC/chiller the first hypothesis, not universal inclusion.
- Which site service model/points are available and authorized.
- Which evidence levels qualify physical profile, service, economic ranking and savings claims.
- How forecast and service uncertainty appear in the canonical contract.
- Whether future controlled assets use the R0 simulator surface or another site-approved interface. This proposal adds no controller.
- Schema authoring, runtime, solver and deployment choices remain governed by G6.9/G7.8/D-065 and the owner decision packet.

No site, customer access, service model, comfort result, savings or field control is claimed by this design.

## 9. Proposed service-outcome semantics and acceptance matrix

This section makes the review examples testable without selecting serialized enum names, a canonical API, or a production service model. Product/domain review remains open.

### 9.1 Keep four result dimensions independent

1. **Electrical profile and balance** — the supplied or generated interval trajectory at a declared physical boundary.
2. **Asset operating envelope** — resource availability, electrical ratings, modes, ramp/dwell limits, SOC/reserve, protection and recovery limits. ESS SOC belongs here; SOC alone is not a customer-service outcome.
3. **User/process service outcome** — HVAC comfort, EV departure-energy target, hot-water delivery, or another declared service obligation for the affected resource and horizon.
4. **Economic evaluation** — separately scoped meter/account/contract/tariff calculations and their eligibility.

A pass in one dimension cannot imply a pass in another. In particular, a balanced electrical schedule is not proof of service, an ESS SOC trajectory is not proof of comfort, and a lower modeled objective is not proof of an eligible bill saving.

### 9.2 Proposed outcome meanings

These are domain meanings for review, not approved wire values.

| Proposed outcome | Exact meaning | Required disclosure |
|---|---|---|
| `NOT_ASSESSED` | No applicable service obligation was requested for this resource, or no service evaluator was invoked. This is not a pass. | State whether the service was out of scope or the evaluator/model was unavailable; identify any resulting claim withheld. |
| `UNKNOWN` | Evaluation was requested, but none of the required service scope can be evaluated because required evidence is absent, invalid, stale, conflicting, unauthorized, or uncertainty prevents a pass/fail determination. | Name affected resource, horizon/intervals, evidence gaps and the next evidence needed. |
| `PARTIAL` | At least one required interval is evaluable and at least one is not; no known hard-bound violation has been established. | List covered and uncovered intervals, count or duration coverage, and the reason for each gap. Never label the covered subset as a full-horizon pass. |
| `WITHIN_DECLARED_PROFILE` | Every required interval, including the declared recovery horizon, is evaluable under an accepted site-specific service profile; evidence/model is usable for the stated purpose; no applicable hard bound is breached. | Identify service-profile/model revision, evidence basis, uncertainty policy, horizon and any soft-bound trade-offs. |
| `VIOLATION` | At least one applicable, evidenced hard bound is known to be breached in the declared scope. This dominates incomplete coverage elsewhere in that same service scope. | Identify the bound, affected interval/resource, observed or modeled value and evidence/model basis. Do not average the breach away. |

Combination rule: a known hard-bound breach yields `VIOLATION`; otherwise full required coverage yields `WITHIN_DECLARED_PROFILE`; partial coverage yields `PARTIAL`; zero evaluable coverage after a requested assessment yields `UNKNOWN`; no requested/invoked assessment yields `NOT_ASSESSED`. If an uncertainty range crosses a hard bound but does not establish a breach or a safe result, use `UNKNOWN` for the affected interval. An accepted model prediction may establish a modeled violation only when the model, uncertainty rule and applicable hard bound are themselves qualified; label it as modeled, not observed.

Evidence basis (`MEASURED`, `MODELLED`, `SCENARIO`, `SYNTHETIC`, or other future vocabulary) and claim disposition (`ALLOWED` / `WITHHELD`) are separate axes. A synthetic fixture may demonstrate a scenario outcome only; it cannot qualify a site service claim. `PARTIAL` describes coverage, not a third claim disposition.

### 9.3 Proposed overall feasibility composition

- A dispatch-feasibility claim may be `ALLOWED` only when the declared electrical profile is qualified, every changed resource's applicable operating envelope is qualified over the affected intervals and recovery horizon, and every required service outcome for changed flexible loads is `WITHIN_DECLARED_PROFILE`.
- If any required changed-load service outcome is `NOT_ASSESSED`, `UNKNOWN` or `PARTIAL`, withhold the overall dispatch-feasibility claim while preserving independent electrical-profile, resource and economic results that remain qualified.
- A known operating-envelope or required-service hard-bound violation makes the candidate infeasible for the affected resource/scope. Do not imply the unaffected site scope also failed unless its dependencies require that conclusion.
- When no user-service obligation applies to the changed resources (for example, a source-only scenario), do not invent a service failure; label service as not applicable/out of scope and assess the separately declared electrical operating envelope.
- Economic `BLOCKED`/`WITHHELD` remains independent: it cannot turn a physical/service pass into a failure or turn an unqualified service result into a pass. An economic objective may not be ranked as bill savings without eligible settlement evidence.
- This proposal is consistent with PR #14's current narrower rule: changed flexible loads without an evaluator keep their electrical profile, while `DISPATCH_FEASIBILITY` and `COMFORT_SERVICE` are withheld. It does not claim PR #14 implements these per-resource outcomes.

### 9.4 Review acceptance matrix

| Case | Expected resource/service outcome | Dispatch-feasibility and retained result |
|---|---|---|
| HVAC schedule changes; no service evaluator/profile exists | `NOT_ASSESSED` | Keep qualified electrical profile; withhold overall dispatch feasibility and comfort/service claims. |
| HVAC profile covers all required zones and recovery; all hard bounds hold | `WITHIN_DECLARED_PROFILE` | Service may support feasibility only if electrical and operating-envelope gates also pass. |
| HVAC measured/modelled trajectory breaches an evidenced hard comfort bound | `VIOLATION` | Candidate infeasible for the affected HVAC scope; retain independent qualified outputs. |
| HVAC evidence is stale/conflicting for every required interval, or uncertainty crosses a hard bound | `UNKNOWN` | Withhold affected service and overall feasibility; disclose the missing/uncertain evidence. |
| EV service was not requested for a changed charging resource | `NOT_ASSESSED` | Do not call it departure-ready; withhold feasibility if that service obligation is required by the declared task. |
| EV target/window is requested but unavailable evidence prevents evaluation in all intervals | `UNKNOWN` | Withhold mobility and overall dispatch-feasibility claims. |
| EV target is evaluated and projected delivered energy misses the evidenced departure target | `VIOLATION` | Candidate infeasible for the EV service scope, regardless of site-average cost. |
| Hot-water draw or delivery evidence is missing for all required intervals | `UNKNOWN` when assessment requested; otherwise `NOT_ASSESSED` | Electrical energy may remain visible; do not claim delivered service. |
| Hot-water reserve/hygiene bound is known to fail in an interval | `VIOLATION` | Reject the affected candidate scope even if modeled import cost improves. |
| ESS SOC evidence is missing/stale but no customer-service evaluator is relevant | Service outcome is not the applicable result; ESS operating envelope is unqualified | Preserve only independent qualified profile; withhold ESS and overall dispatch feasibility when ESS is required by the candidate. |
| Some HVAC/EV/hot-water intervals evaluate while others lack evidence; no known violation | `PARTIAL` | Report exact coverage and gaps; do not present the schedule as full-horizon service-feasible. |
| Candidate explicitly records zero/off for an interval versus omitting the interval record | Explicit zero is a value subject to the profile; omission is incomplete scope unless schedule bounds define it | Never coerce omission to zero or treat it as proof of inactivity. |
| Recovery horizon ends before the required/evidenced response is covered | `PARTIAL` if some required scope is covered, otherwise `UNKNOWN` | Withhold full-horizon feasibility/benefit; show the uncovered recovery interval. |

These cases become contract and code acceptance tests only after product/domain owners accept the meanings and the authority chooses a contract profile. Until then, they are reviewable design criteria, not canonical API behavior or a Gate exit.
