# Open Questions / Blocking Unknowns

## U-001 — CEM Pu averaging/integration interval
**Status:** UNKNOWN / G1 BLOCKER  
**Known:** CEM/legislation define Pu as the highest measured demand / maximum periodically measured average active power.  
**Unknown:** Exact averaging/integration window used for settlement (e.g. 15 min, 30 min or another period).  
**Resolution path:** real B/C/D meter load-profile + bill, CEM metering configuration or authoritative technical documentation.  
**Production behavior:** never hard-code 15 minutes.

## U-002 — Commercial PV settlement topology
**Status:** CONTRACT-SPECIFIC  
**Question:** gross production FIT, surplus export, self-consumption, zero export or another structure for a given project?  
**Resolution path:** customer PV purchase agreement, meter diagram and CEM interconnection documents.

## U-003 — Third-party high-frequency CEM AMI access
**Status:** UNKNOWN  
**Question:** Is a supported real-time/high-frequency API available to commercial third parties?  
**Resolution path:** CEM technical/commercial confirmation.  
**Design implication:** first pilot must be viable with local metering/BMS data.

## U-004 — Commercial ESS grid export
**Status:** UNKNOWN  
**Question:** Under what conditions can a commercial ESS export into the public grid and how would that be settled?  
**Production default:** `ESS_EXPORT=false` unless verified for a project.

## U-005 — Real C1/C2/B2/B3 transformer compensation evidence
**Status:** PARTIALLY VERIFIED  
**Question:** How do current customer bills express percentage loss compensation versus regulatory/contract-specific physical-loss treatment?  
**Resolution path:** real bills + contract/meter topology.

## U-006 — Real BMS data quality
**Status:** SITE-SPECIFIC UNKNOWN  
**Need:** timestamps, units, stale-point behavior, sensor accuracy, sampling rate, missing values, control-state history.

## U-007 — Real Macau HVAC flexibility
**Status:** HYPOTHESIS  
**Need:** quantify flexible kW/kWh, comfort impact, rebound, weather dependence and plant constraints from pilot data.

## U-008 — Site comfort and humidity SLA
**Status:** SITE-SPECIFIC UNKNOWN  
**Need:** zone categories, allowed temperature/humidity bands, operating hours, critical rooms and override rules.

## U-009 — Exact B/C/D government tax formula
**Status:** UNKNOWN / G1 BLOCKER  
**Known:** CEM B/C/D pages state a monthly government tax applies.  
**Unknown:** authoritative general formula and exceptions for B/C/D.  
**Resolution path:** legislation/CEM bill evidence.

## U-010 — Golden Bill Test cases
**Status:** NOT ACQUIRED / G1 BLOCKER  
**Need:** at least one real B/C customer bill + interval/load-profile evidence and a second case from a different tariff class.  
**Gate:** Tariff Engine cannot be marked production-ready until reconstruction error is <=0.5% with zero unexplained balancing adjustment.

## U-011 — Commercial bill rounding / odd-amount carry-forward semantics
**Status:** OPEN / GOLDEN-BILL VALIDATION REQUIRED  
**Known:** CEM's bill explanation documents an “Odd Amount” carry-forward/rounding concept.  
**Unknown:** Exact component-level versus invoice-level rounding/carry-forward behavior for B/C/D commercial bills and how it interacts with reconstruction tolerance.  
**Resolution path:** real B/C/D bills + CEM billing explanation/contract evidence.  
**Design implication:** rounding remains an explicit settlement policy; do not round each interval by default.

## U-012 — Macau reference-building calibration targets
**Status:** OPEN / G7  
**Question:** Which measured Macau hotel/commercial load, chiller COP, humidity and occupancy distributions should calibrate the R1/R2 reference cases?  
**Resolution path:** pilot data, published Macau building studies, and measured site evidence.  
**Design implication:** BOPTEST base cases are harnesses only; no ROI claim may be labelled Macau-hotel representative until calibrated.


## U-013 — Pinned R0 native point set
**Status:** RESOLVED FOR v0.9.0 PRE-FLIGHT / LIVE HASH RECHECK REQUIRED  
**Resolved:** Official v0.9.0 API regression fixtures establish 182 inputs, 204 measurements and 134 forecast points, with exact fixture SHAs recorded in `G7.2-R0-HARNESS-PREFLIGHT.md`.  
**Remaining runtime check:** A live v0.9.0 deployment must reproduce the same metadata hashes/counts before a run is accepted.

## U-014 — R0 humidity / latent observability
**Status:** PARTIALLY RESOLVED / R1 REQUIREMENT IDENTIFIED  
**Known:** R0 exposes outdoor RH, supply/return AHU RH for three floors, and latent internal-gain forecasts for all 15 zones.  
**Limitation:** No zone-level relative-humidity measurement is exposed in the pinned v0.9.0 measurement fixture.  
**Implication:** R0 cannot validate zone/guestroom humidity SLA; R1/R2 must add/verify zone humidity observation and latent-control behavior.

## U-015 — Macau weather calibration source beyond TMYx
**Status:** OPEN / G7  
**Question:** Which official Macau/onsite measured weather series should validate the TMYx engineering source for R1/R2?  
**Resolution path:** SMG/official data access where appropriate plus pilot-site outdoor sensors and historical BMS/weather records.

## U-016 — Real absolute non-HVAC site-load composition
**Status:** SITE-SPECIFIC UNKNOWN / NOT A BLOCKER FOR ENERGY-ONLY R0 DELTA  
**Known:** R0 can synthesize office lighting/plug settlement load from the pinned BOPTEST model.  
**Unknown:** A Macau pilot site's real non-HVAC categories and profiles (lighting, plug, kitchens, elevators, gaming/retail loads, laundry, data/IT, etc.).  
**Resolution path:** settlement-meter/submeter/BMS data from pilot site.  
**Design implication:** synthetic R0 absolute cost is harness-only; verified customer total bill/demand analysis requires measured site composition.


## U-017 — Actual SAT/CHWS response sign, magnitude and rebound in live R0
**Status:** OPEN / G7.2 BLOCKER FOR CONTROLLER-PERFORMANCE CLAIMS  
**Question:** What are the actual direction, magnitude, nonlinearity and post-peak rebound effects of the approved supervisory SAT/CHWS perturbations on chiller power, fan power and total composed site power?  
**Resolution path:** close G7.2 live baseline/no-op execution, then run the guarded R0 controller experiment matrix with paired baseline/candidate replay.  
**Design implication:** do not assume that raising SAT/CHWS lowers total site power; recovery/new-peak diagnostics remain mandatory.
