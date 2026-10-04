# Forecasting and Optimization — Detailed Design v0.1

**Status:** Stack-neutral research-derived draft; G4/G5 remain open. No model, solver, production runtime, or control deployment is approved here.  
**Scope:** PR-06 forecasting/optimization pipeline and its handoff to SHADOW recommendations. Simulation and Macau-site evidence remain distinct.  
**Authority:** G2–G7 gate definitions; D-002–D-009, D-018, D-028, D-032/D-033, D-037, D-040, D-042, D-044, D-046/D-048/D-050, D-056/D-057, D-059–D-061, D-068 and D-073/D-074; current G6/G7 and G6.9-R2 status; VS-001.

## 1. Purpose and system boundary

Forecasting estimates future site conditions with an explicit horizon and uncertainty. Optimization searches candidate operating schedules under economic, physical, comfort, equipment and site-policy constraints. The exact settlement evaluator rechecks each candidate trajectory. A recommendation builder packages an eligible candidate as a versioned SHADOW proposal.

Keep these evidence products separate:

- **Forecast:** conditional estimate from versioned observations, features and model.
- **Optimization candidate:** modeled schedule feasible under supplied constraints.
- **Economic assessment:** tariff-engine evaluation of baseline and candidate under an explicit scope and rule version.
- **Recommendation:** operator-readable SHADOW proposal, not authorization or proof of a realized outcome.
- **Observed outcome:** separately measured using an approved measurement-and-verification method.

Cloud forecast/optimization has no device-write interface. G6 remains OPEN. Any later command must use the site Edge policy and Safety Kernel path; an optimizer or MPC cannot bypass it (D-006/D-008/D-061).

## 2. Inputs and readiness

Each run is scoped to authenticated tenant/site context, a declared horizon, a clock/boundary policy and a run identifier separate from business identity. Pin immutable or versioned references to:

- quality-qualified telemetry, source and point-mapping provenance (PR-02);
- effective-dated assets, meters, topology and operational relationships (PR-03);
- tariff/contract/rule context and solver-friendly tariff representation compiled from the same rule package as the exact evaluator (D-018/D-028);
- validated asset capabilities and response/constraint evidence from G2;
- model, feature transform, training data lineage and forecast artifact from G4;
- baseline, exogenous assumptions, solver/controller, constraints and schedules;
- simulator/testcase, seed, clock, step and configuration when a reference harness is used.

Reject unauthorized scope. Check stream coverage, mappings, units, time policy, quality/freshness, required tariff inputs, and constraint versions. Missing required evidence returns blocked/partial status with reasons. Do not guess a site limit, tariff parameter or equipment response.

Do not infer the CEM Pu settlement window from telemetry interval, optimizer resolution, controller communication step, simulator timestep, or rolling-peak diagnostic. These are independent time scales (D-040/D-059/D-074); G1 U-001 remains open.

## 3. Forecast subsystem

### 3.1 Candidate targets

Candidate targets include site/building import load, HVAC/cooling demand, PV generation/export, occupancy-driven load and flexible-load availability. Include a target in pilot evaluation only when the site has sufficient source coverage, identity/mapping, timestamps, quality policy, and outcome evidence. The architecture having a forecast slot does not prove every target is supported.

Preserve scope: producer export remains distinct from consumer import unless an explicit, authorized site-economic scenario combines them.

### 3.2 Horizon and time contract

The roadmap's current evaluation horizons are day-ahead (24–48 hours) and intraday receding updates (5–15-minute grid). These are forecast/optimization grids, not Macau demand-settlement rules or universal device command cadence. Site lead times, resolution, scheduling deadline, timezone boundaries and output expiry require G2/G3/G7 evidence.

Each forecast identifies issue time, valid-time range, interval boundaries, timezone/clock policy, target, unit, model/build and feature versions, input coverage, status, estimate and uncertainty representation. Exact wire fields remain subject to D-065/G6.9-R2 contract selection.

### 3.3 Uncertainty and status

Use a validated uncertainty representation such as calibrated quantiles or prediction intervals. Record calibration period, horizon, target population and coverage evidence; an uncalibrated confidence label is not evidence. Carry uncertainty into optimization through explicit scenarios or robust constraints only when the data and model support them. Do not collapse uncertainty into a precise savings number.

Forecast states distinguish ready, partial, blocked and failed, with reasons for stale inputs, insufficient coverage, out-of-distribution conditions, model unavailability or invalid output. A forecast can be useful as operator context while ineligible for economic ranking.

### 3.4 G4 evaluation evidence

Compare candidates with simple documented baselines using chronological/rolling-origin evaluation and leakage controls. Report error by target, horizon, site/asset and operating regime, plus uncertainty calibration/coverage and missing-data behavior. Evaluate whether forecast errors change downstream decisions or economic assessments; generic MAE/RMSE alone does not establish usefulness. Preserve benchmark inputs, outputs, metrics code, model/data versions and reviewer interpretation.

**G4 exit evidence:** validated target definitions and data readiness; baseline and candidate results on held-out periods; horizon-specific calibration/error analysis; missingness, drift and out-of-distribution handling; decision-usefulness analysis; evidence-register updates; explicit gate decision and remaining restrictions. This draft does not claim G4 closure or Macau model performance.

## 4. Optimization subsystem

### 4.1 Inputs, objective and constraints

Pin an initial state, eligible forecasts, time grid, candidate assets, feasible operating region, tariff/cost model, objective priorities and baseline. The governing objective is total economic energy cost/value, not minimum kWh (D-002). State the included streams and components. Unknown tariff or unsupported economic inputs block definitive economic ranking.

Hard safety and site-policy constraints are not soft objective penalties. Comfort, SLA, equipment protection, site capacity, ramps, minimum up/down time, cycling/degradation, reserve and recovery constraints enter only when defined and validated for that site and equipment. Demand Guard may veto a schedule; lower cost cannot compensate for violating a hard limit.

### 4.2 Candidate generation and evaluation

1. Validate scope, evidence readiness and pinned versions.
2. Build search inputs from eligible forecasts, initial state, equipment capabilities and versioned constraints.
3. Generate candidate schedules with a replaceable solver/controller module.
4. Reject hard-constraint violations; record infeasible or partially constrained runs.
5. Re-evaluate baseline and candidates through the exact tariff/settlement evaluator, using the solver-friendly model compiled from the same tariff package (D-028). Preserve resolver/component findings and project them to the shared CostResult vocabulary in Tariff & Settlement §4; failed requests and incomplete replay cannot produce an economic amount.
6. Compare only compatible scopes and shared exogenous assumptions; distinguish paired dispatch value from absolute site bill.
7. Record objective decomposition, active constraints/margins, uncertainty/scenarios, solver status/gap, rationale and evidence lineage.
8. Run simulation/replay where authorized and produce a SHADOW recommendation only if eligibility rules pass.
9. Persist immutable run/result manifests; changed input or configuration creates a new lineage.

BOPTEST native electricity-price or cost KPIs are not Macau settlement authority (D-033/D-042). Under D-050, paired baseline/candidate dispatch value may use the changed modeled electric trajectory only under its explicit shared-exogenous-load assumptions; absolute site cost requires SitePowerComposer. Scenario capacity guards, rolling peaks and CEM Pu remain distinct (D-059).

### 4.3 Controller progression and pilot limits

For R0, authority orders a deterministic tariff-aware supervisory state machine (TariffShaper v0) before MPC (D-056). This sequence is a simulator experiment, not a universal production solver decision. R0 actuation remains limited to its approved four-point supervisory surface and activation semantics (D-046/D-049/D-057); zone/low-level overrides remain out of scope. MPC has no privileged safety or command path (D-061).

HVAC/chiller is the first priority controllable asset in the initial pilot hypothesis (D-003). ESS remains optional and site-economics dependent (D-004). Neither decision proves that a Macau site exposes these assets, supports their control, or has approved constraints.

### 4.4 Rebound and recovery

Include post-event recovery where shifting/cooling actions can rebound, create a new peak, violate comfort, or erase modeled benefit. Recovery behavior is explicit (D-060). Report pre-event, event, recovery and full evaluation-period energy/cost plus demand diagnostics. A peak clipped during the target window alone does not prove site savings or acceptable operation.

## 5. Recommendation interface

The optimizer returns a typed run result, not a UI command. The recommendation builder may emit a SHADOW recommendation only when evidence references resolve and status, uncertainty and constraints are representable. It discloses:

- site/asset scope, objective and validity period;
- baseline, forecast/model and solver/controller versions;
- proposed trajectory at approved abstraction level;
- modeled effect with unit, currency and scope only where eligible;
- uncertainty, coverage, active constraints and feasibility status;
- tariff/cost-rule versions and unresolved assumptions;
- simulation versus live-site evidence classification;
- run/replay manifest and review lifecycle reference.

Infeasible, stale, unsupported or constraint-violating candidates are blocked or diagnostic-only. A model output, LLM explanation, review disposition or positive modeled delta cannot mark a recommendation executed or realized. Actual effect remains separate and requires approved M&V evidence.

## 6. Determinism and replay

A run manifest pins semantic inputs, model/feature artifacts, solver/controller version, configuration, tariff compilation, baseline, time policies, random seeds, simulator/testcase identity and output digest. Correlation/trace IDs remain diagnostic metadata and cannot affect proposal identity or business results (D-073). Establish fixed time buckets before quality filtering (D-074).

Simulation must be repeatable from pinned manifests under an explicit numerical tolerance/semantic comparison policy. Do not promise bit-for-bit solver determinism until runtime behavior is evidenced. Preserve raw outputs and explain tolerance, solver optimality gap and nondeterminism. Model registry, storage, retention and operational SLO are deferred architecture decisions.

## 7. Failure behavior

| Condition | Required behavior |
|---|---|
| Forecast input/target quality insufficient | Mark forecast ineligible; block dependent optimization |
| Unknown tariff or non-comparable baseline | Withhold authoritative monetary ranking; return blocker |
| Missing or contradictory asset limits | Exclude the asset; invent no fallback bounds |
| Hard constraint violation or infeasible solver result | Emit no recommendation; retain diagnostic run and violated-constraint evidence |
| Out-of-distribution state or failed calibration | Mark degraded/blocked under approved policy; do not present nominal output as reliable |
| Simulator/testcase mismatch or unavailable pinned input | Mark non-comparable/non-replayable; never substitute silently |
| Timeout or excessive solver gap | Return limited/failed status; no best-effort actuation |
| Cloud/site outage | No cloud execution; local behavior only if separately authorized by G6 |
| Rebound or comfort violation | Report outcome/constraint evidence; do not declare success from event-window metrics |

## 8. Safety and security boundary

All requests and artifacts are tenant/site scoped. Model artifacts/data remain untrusted until validated and versioned. Optimizer access to actuator credentials and Edge write channels is absent in SHADOW.

Any future controlled operation requires G6 evidence for site-local safety limits/veto, offline fallback, manual override, authenticated/idempotent command lifecycle, replay protection, key lifecycle, audit and independent authorization. This design does not fill those gaps or approve a command path.

## 9. Gate acceptance evidence

### G4 Forecasting

- Authorized site data, target definitions, source quality/freshness and readiness.
- Leakage-safe baselines and chronological evaluation by target/site/horizon/regime.
- Uncertainty calibration, missingness/out-of-distribution behavior and update/drift policy.
- Evidence linking forecast error to downstream decision usefulness.
- Reviewed G4 decision record with limitations and residual unknowns.

### G5 Optimization

- Versioned objective, baseline, hard/soft constraint classification, asset capability evidence and time policy.
- Candidate vs baseline simulation under same exogenous inputs, with pinned manifests and exact economic re-evaluation.
- Feasibility, solver quality/runtime, uncertainty/scenario, rebound/recovery, comfort/SLA and equipment-impact results.
- Explicit distinction among simulation, synthetic fixtures and live Macau-site evidence.
- Reviewed G5 decision record identifying what is validated and what remains advisory/blocked.

### Cross-gate dependencies

- G1 tariff/settlement passes for bill-grade or authoritative economic ranking claims.
- G2 response and operating-limit evidence passes for flexibility claims.
- G3 topology/identity supports the modeled aggregation.
- G6 passes before any command/control path; optimizer evidence cannot substitute for it.
- G7 simulation, no-op identity, live response and M&V evidence remain distinct.
- G6.9-R2 Step 3D/4 authorizes only a technology decision; it does not select domain semantics.

No gate acceptance evidence above is asserted by this draft.

## 10. Open questions

- Which forecast targets have sufficient Macau/site data and decision value?
- Which baselines and windows fit each site and operating regime?
- Which uncertainty representation is useful and understandable to operators?
- Which assets expose validated capability curves, comfort/response constraints and recovery behavior?
- Which economic objective components/priorities are supported by each customer contract?
- Which solver/controller meets quality, runtime, reproducibility and maintenance needs?
- What product states are required when uncertainty, feasibility or replay evidence degrades?
- Which pilot M&V method and counterfactual baseline can separate modeled value from realized effect?

Resolve these through evidence and owner review, not implementation convention.

## 11. References

- docs/01-research/gates/G2-load-flexibility.md
- docs/01-research/gates/G3-energy-graph.md
- docs/01-research/gates/G4-forecasting.md
- docs/01-research/gates/G5-optimization.md
- docs/01-research/gates/G6-safety-control.md
- docs/01-research/gates/G7-pilot-validation.md
- docs/01-research/energy-os-research/Optimization-Research.md
- docs/03-architecture/ARCHITECTURE-DESIGN.md
- docs/03-architecture/detailed-design/VS-001-DETAILED-DESIGN-v0.1.md
- docs/03-architecture/detailed-design/RECOMMENDATION-AND-OPERATOR-REVIEW-DETAILED-DESIGN-v0.1.md
- docs/03-architecture/detailed-design/COST-ANALYSIS-AND-EVIDENCE-REPLAY-DETAILED-DESIGN-v0.1.md
- docs/00-authority/decisions/DECISIONS.md
- docs/00-authority/decisions/OPEN-QUESTIONS.md
