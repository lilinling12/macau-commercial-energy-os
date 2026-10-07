# G2 Commercial Load Flexibility

**Status:** OPEN — public context is documented; site-level flexibility is not validated.

## Purpose

Establish a source-backed, site-specific model of which commercial loads can safely and repeatably change power use, for how long, under which operating conditions, and with what economic value and recovery effects.

## Research questions

For each asset in the selected pilot scope:

- What measured baseline load, controllable range, direction and availability window exist?
- What response delay/ramp and sustainable duration are demonstrated?
- What comfort, humidity, safety, process, equipment, warranty and operator constraints apply?
- What recovery/rebound or shifted peak occurs after an action?
- Which meter, customer contract and tariff rule determine economic value? Are any settlement rules still unknown under G1?
- Is telemetry/control access technically and contractually available, authorized and auditable?

## Evidence rule

Distinguish public aggregate statistics, reported operating practices, engineering simulation, and site-measured evidence. DSEC sector totals and annual bill-month energy comparisons do not establish interval load shape or dispatchable capacity. BOPTEST/R0 validates controller and experiment behavior, not Macau site capability. D-003 prioritizes HVAC/chiller for the initial pilot as a hypothesis to validate, not a measured general rule.

Detailed evidence and protocol: `docs/01-research/evidence/G2-MACAU-COMMERCIAL-LOAD-FLEXIBILITY-EVIDENCE-2026-10.md`.

Relevant unknowns: U-004, U-006, U-007, U-008, U-012, U-014, U-016 and U-017.

## Required outputs

1. A versioned site/asset/point inventory for each in-scope resource, including source, units, timestamps, quality, access and authorization.
2. A measured flexibility envelope per resource: kW up/down, response/ramp, minimum and maximum duration, availability, recovery/rebound and confidence/validity conditions.
3. Explicit operating boundaries: occupancy/schedule, comfort and humidity, critical rooms/services, plant/equipment constraints, operator overrides, safety limits and maintenance state.
4. A reproducible paired baseline/response protocol with weather, schedule and other exogenous conditions; results and uncertainty preserved for replay.
5. An economic mapping to the relevant meter, contract, tariff version and settlement rules. Unknown Pu windows, export permissions or contract semantics remain UNKNOWN and cannot produce bill-grade value.
6. A scope decision for each asset class: included with evidence, excluded, or deferred pending access/data.

## Exit criteria

G2 may close only when:

- each asset in the approved pilot scope has the required data and constraints documented;
- at least one repeatable, site-approved measurement protocol quantifies response and duration, and recovery/rebound where response is tested;
- comfort, service, safety and equipment impacts are bounded, with no unresolved safety bypass;
- the economic mechanism uses verified meter/contract/tariff inputs or is explicitly labeled scenario-only;
- evidence provenance, baseline method, validity window and limitations are recorded; and
- unsupported or unmeasured asset classes are excluded from dispatchable-capacity and savings claims.

No minimum savings threshold is inferred from public aggregate statistics or contest criteria. Pilot/GTM may set a commercial threshold after site calibration. Active control tests require site authorization and applicable G6 controls; SHADOW/simulation cannot authorize field commands.

## Current evidence summary

- DSEC reports aggregate establishment electricity consumption but no public building interval profiles or measured flexibility.
- DSPA records specific hotel energy-management practices, but the public examples do not report response magnitude, rebound or causal savings.
- CEM's hotel energy-saving activity compares billing-month consumption year over year, not dispatch response or demand settlement.
- Macau site capability, comfort/SLA and BMS/control access remain site-specific UNKNOWN.

See the G2 evidence note and U-006–U-008 for current boundaries.