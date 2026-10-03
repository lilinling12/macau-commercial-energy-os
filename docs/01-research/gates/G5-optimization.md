# G5 Optimization

**Status:** OPEN; no G5 closure record is present.  
**Purpose:** Validate that constrained, tariff-aware candidate schedules are feasible, explainable and better than an explicit baseline under reproducible evidence.  
**Authority:** Research-to-Delivery Roadmap, G5 exit definition, G1–G4/G6/G7 dependencies, D-002–D-009, D-018/D-028, D-032/D-033/D-040/D-042, D-046/D-050/D-056/D-059–D-061, and Forecasting and Optimization Detailed Design v0.1.

## Research questions

1. Which assets have site-validated operating capability, response, comfort/SLA and recovery constraints?
2. Which economic objectives and tariff components are authoritative for each customer/site?
3. What is the explicit baseline, evaluation horizon and comparator?
4. Can a candidate meet hard safety/site constraints under forecast uncertainty and model limits?
5. Does the modeled benefit survive exact tariff-engine re-evaluation, full-period accounting, rebound and recovery?
6. What solver/controller quality, runtime, reproducibility and maintenance evidence is required?
7. Which outputs are suitable for a SHADOW recommendation, and which must be blocked?

## Scope and boundaries

Optimize total economic energy cost/value, not minimum kWh (D-002). Exact settlement and solver-friendly cost models are separate representations generated from the same tariff rule package; re-evaluate proposed schedules with the exact evaluator (D-018/D-028). Unknown tariff semantics or incompatible baselines block authoritative monetary ranking.

Hard Demand Guard and site safety limits are constraints/vetoes, not objective penalties. The optimizer cannot command equipment. G6 remains OPEN; no G5 evidence authorizes controlled execution. The site Edge and Safety Kernel retain the command boundary.

For the initial R0 simulator sequence, D-056 requires a deterministic tariff-aware supervisory state machine before promotion of MPC. This is a scoped research sequence, not a universal production algorithm decision. BOPTEST provides reference engineering behavior, not Macau commercial-building ground truth or CEM settlement economics (D-032/D-033/D-042).

## Evaluation protocol

- Pin initial state, time grid, objective, hard/soft constraints, baseline, exogenous assumptions, tariff and rule versions, solver/controller build, simulator/testcase, seed and output manifest.
- Compare candidate and baseline under the same exogenous trajectory, horizon and compatible scope.
- Re-evaluate candidate and baseline through the exact tariff/settlement evaluator. Keep paired dispatch value distinct from absolute site bill as required by D-050.
- Report feasibility, active constraints/margins, solver status/optimality gap/runtime, forecast uncertainty/scenarios and any relaxation.
- Include pre-event, event and recovery windows. Evaluate rebound, new peaks, comfort/SLA and equipment/degradation impacts; event-window peak clipping alone is not success (D-060).
- Use only evidence-backed asset limits. For R0, respect the authorized four-point supervisory surface, activation semantics and explicit exclusions (D-046/D-049/D-057).
- Preserve raw simulator artifacts and distinguish synthetic fixtures, reference simulation and live Macau-site evidence.
- Produce operator explanations, blocked states and explicit modeled-versus-measured outcome distinctions.

## Dependencies

- **G1:** tariff/settlement and economic objective evidence.
- **G2:** asset flexibility, response, comfort, rebound and operating limits.
- **G3:** Energy Graph identity and aggregation.
- **G4:** eligible forecasts, uncertainty and data-failure states.
- **G6:** independent safety proof before any command path; G5 cannot substitute for G6.
- **G7:** reproducible reference runs and authorized live baseline/no-op/response evidence.
- **G6.9-R2:** runtime choice follows its separate pinned bake-off and does not determine optimization semantics.

## Exit criteria

G5 may close only when the evidence packet contains:

1. explicit objective, baseline, time policy, compatible scope and hard/soft constraint register;
2. validated asset capability and forecast inputs for the evaluated site/regime;
3. reproducible candidate-vs-baseline runs with exact economic re-evaluation;
4. feasibility, solver quality/runtime, uncertainty, rebound/recovery, comfort/SLA and equipment-impact analysis;
5. evidence-class separation and documented limits for simulation versus live site;
6. reviewed recommendation eligibility/withholding rules, updated evidence register and a Gate decision recording residual unknowns.

No G5 closure or field-control authorization is asserted. See docs/03-architecture/detailed-design/FORECASTING-AND-OPTIMIZATION-DETAILED-DESIGN-v0.1.md.
