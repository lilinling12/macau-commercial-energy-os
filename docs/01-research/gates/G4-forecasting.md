# G4 Forecasting

**Status:** OPEN; no G4 closure record is present.  
**Purpose:** Determine which forecasts are justified by the available site data and improve decisions under explicit uncertainty.  
**Authority:** Research-to-Delivery Roadmap, G4 exit definition, G2/G3 dependencies, D-018/D-040/D-074, and Forecasting and Optimization Detailed Design v0.1.

## Research questions

1. Which targets (site import, HVAC/cooling, PV generation/export, occupancy-driven load, flexible-load availability) have authorized, mapped, sufficiently complete observations?
2. Which horizons and resolutions serve a validated task? Current evaluation candidates are day-ahead 24–48 hours and intraday 5–15-minute receding updates; these are not CEM demand-settlement intervals or device command cadence.
3. Which simple baseline is appropriate for each target and operating regime?
4. How do error and uncertainty vary by horizon, site/asset, season and operating regime?
5. Does the forecast change an economic or operational decision enough to justify its complexity?
6. What should happen under missing/stale inputs, unusual conditions, model drift or out-of-distribution data?

## Scope and boundaries

Evaluate only targets with adequate source identity, unit, timestamp, quality, freshness and coverage evidence. Distinguish consumer import from PV producer export. Keep forecast issue time, valid time, bucket policy and site timezone explicit. The optimizer time grid, telemetry cadence, Edge communication interval, simulator step and tariff demand window are separate time scales; U-001 remains authoritative for unresolved Macau demand-window semantics.

G4 evaluates forecast suitability and interface semantics; it does not choose a model vendor or production runtime, pass G5 optimization, authorize device control, or establish Macau customer economics from simulated data.

## Evaluation protocol

- Preserve raw inputs, source/mapping versions, feature transforms, training cutoff, model/build/configuration and evaluation code.
- Use chronological or rolling-origin held-out evaluation; prevent future leakage through features, normalization and site aggregation.
- Compare to a documented naïve/seasonal baseline before comparing complex models.
- Report errors by target, horizon, site/asset and meaningful operating regime. Include error distributions and missing-data behavior, not only pooled averages.
- Evaluate uncertainty calibration/coverage over the stated horizon and population. Explain uncertainty to downstream optimization and operators.
- Test degradation, stale inputs, outages, extreme but in-scope periods and out-of-distribution states.
- Quantify downstream impact: whether forecast error changes candidate feasibility, dispatch ranking, economic result or operator decision. Forecast accuracy alone is not proof of utility.
- Keep synthetic, BOPTEST/reference, and live Macau-site results separately labeled.

## Dependencies

- **G2:** asset response/flexibility where forecasts inform controllable loads.
- **G3:** stable identity, mapping, aggregation and site topology.
- **G1:** tariff semantics when evaluating forecast usefulness by economic impact.
- **G7:** reference simulator and authorized live site evidence for validation context.
- **G6.9-R2:** implementation runtime remains open; contract and runtime selection does not define forecast semantics.

## Exit criteria

G4 may close only when the evidence packet contains:

1. approved forecast target definitions and eligible source/readiness policies;
2. pinned datasets and leakage-safe baseline/candidate evaluation by target and horizon;
3. uncertainty calibration/coverage evidence and explicit known limitations;
4. failure, missingness, drift and out-of-distribution behavior;
5. downstream decision-usefulness analysis, including when a forecast must be withheld;
6. evidence register updates, reproducible artifacts and a reviewed Gate decision with residual unknowns.

No such closure evidence is asserted by this document. See the component design at docs/03-architecture/detailed-design/FORECASTING-AND-OPTIMIZATION-DETAILED-DESIGN-v0.1.md.
