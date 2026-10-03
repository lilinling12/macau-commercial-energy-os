# G2 Evidence Note — Macau Commercial Load and Flexibility Evidence (2026-10)

**Reviewed:** 2026-10-04  
**Gate:** G2 — Commercial Load Flexibility  
**Status:** PUBLIC CONTEXT VERIFIED; asset-level flexibility NOT VERIFIED; G2 remains OPEN.

## Research question

What can public Macau evidence establish about commercial electricity use and controllable building operation, and what site evidence is still required before assigning flexible kW/kWh or savings value?

## Findings supported by Macau primary sources

### 1. Official statistics establish commercial-sector scale and rising seasonal demand, not site flexibility

The newest located official quarterly source is DSPA's 2026 Q2 Energy and Services synthesis (page updated 2026-09-25). It reports CEM-supplied total electricity consumption of 1,710 GWh (+3% year on year), CEM sales of 1,669 GWh (+3%), and a system maximum load of 1,130 MW, a record. Its electricity sales table breaks the total down by customer group:

| Q2 2026 CEM electricity sales | GWh | Year-on-year |
|---|---:|---:|
| Commercial | 1,059 | +3% |
| Residential | 362 | +3% |
| Government institutions | 207 | +5% |
| Industrial | 42 | 0% |
| Total | 1,669 | +3% |

Using the published rounded values, commercial customers account for approximately 63.5% of Q2 sales (1,059 / 1,669); H1 2026 commercial sales are 1,887 GWh, approximately 64.6% of the 2,920 GWh H1 total. These are utility customer-group aggregates, not a hotel/retail/site count, an addressable market estimate, or a building load profile. The report attributes the quarter's higher total electricity consumption partly to above-average temperatures. Its total-consumption definition excludes the waste-incineration centre's own-use and private-facility self-generation. DSEC's 2025 Q3 Energy Statistics separately reports 1,200 million kWh for its broader "establishments" category (+1.7% year on year), alongside households (437 million kWh, +3.3%) and government (232 million kWh, +6.4%). These are distinct statistical series and must not be merged or treated as like-for-like without category reconciliation. Neither source publishes named-building interval profiles, HVAC end-use shares, building coincident peaks, controllable capacity, or response/rebound measurements.

**Implication:** use the newer DSPA/CEM series for commercial-customer quarterly sales and system-level seasonal context, and retain DSEC's establishments series as a separate category. Neither series supports building load-shape inference or available demand response.

### 2. Macau hotel evidence shows that energy monitoring and scheduling actions exist

DSPA's 2023 Green Hotel Award record for Galaxy says the hotel used a Central Monitoring and Control Center to monitor and control electricity consumption and switched off 50% of escalators and lifts during non-peak periods. This establishes reported operational measures at that named hotel. The public award record gives no metered kW reduction, event duration, comfort/service impact, rebound, or causal baseline.

CEM's 2026 hotel/resort energy-saving activity groups each hotel/resort complex as one participant even when it has multiple supply points or contracts; segments participants at subscribed demand of 1,600 kVA; and compares four billing months (July–October) year over year using actual boundary meter reads. It is a seasonal energy-saving comparison and does not test dispatch response, demand-charge impact, intra-month peaks, causal attribution, or control latency.

**Implication:** these sources support hotel customer segmentation and the existence of energy-management practices. They do not validate a Macau hotel flexibility model.

### 3. Existing simulation is engineering evidence only

D-032/D-033/D-037 and the G7 reference-building authority define BOPTEST R0 as a controller/harness case, not Macau hotel ground truth. A simulated controller response may validate software behavior and experiment reproducibility; it cannot supply Macau site capability, comfort limits, equipment availability, or representative savings without site calibration.

## Evidence status by claim

| Claim | Status | Supported conclusion | Evidence limit |
|---|---|---|---|
| Macau commercial establishments are a large, measurable electricity-use category | VERIFIED, aggregate | DSEC publishes establishment-level sector totals | No building interval data or end-use composition |
| Some Macau hotels report centralized electricity monitoring and scheduled equipment shutdown | VERIFIED, named practice | DSPA records the Galaxy 2023 award measures | No measured response magnitude, service impact, or causal savings |
| Macau hotel complexes are compared across billing months and supply points for energy-saving activity | VERIFIED, program rule | CEM defines grouping, subscribed-demand segments and comparison period | Not a flexibility dispatch test or tariff-demand settlement proof |
| HVAC/chiller is the best first flexible asset for a target pilot | PROJECT DECISION / HYPOTHESIS | D-003 prioritizes it for the initial pilot | Must be confirmed against the actual site's BMS, plant and service constraints |
| Any Macau site has a quantified flexible kW/kWh envelope | UNKNOWN / SITE-SPECIFIC | None from reviewed public evidence | Requires site data and approved measurement |
| Simulated R0 values represent a Macau hotel | NOT ESTABLISHED | No such inference is allowed | R1/R2 calibration and site evidence required |

## G2 measurement protocol required for site evidence

For every asset included in a pilot, retain a site-approved asset/point map and collect aligned evidence sufficient to evaluate:

- baseline interval power and data quality at the settlement meter and relevant submeters;
- asset state, command/setpoint, measured response, and timestamp/clock quality;
- available direction (increase/reduce/shift), kW envelope, ramp/response delay, minimum/maximum duration, availability window and recovery trajectory;
- relevant operating constraints: occupancy/operating schedule, comfort and humidity bands, critical zones, equipment limits, maintenance state, override behavior, and non-energy service requirements;
- weather and other major exogenous conditions needed to compare baseline and response;
- tariff/contract/meter mapping and explicit uncertainty for any Pu/demand window or settlement rule still unresolved under G1;
- test authorization, safety vetoes, operator overrides, event log, baseline method, comparison period and attribution assumptions.

Use a controlled, site-approved test protocol with paired baseline and response periods. Start with passive observation and SHADOW replay. Any active setpoint/dispatch test requires explicit site authorization and applicable G6 controls. Report measured response and rebound separately; do not convert simulated response, annual energy comparisons, nameplate ratings or unverified tariff assumptions into dispatchable value.

## Asset coverage to resolve for the chosen pilot

Do not force every asset type into the MVP. For each asset actually present and in scope, document evidence and exclusions:

- **HVAC/chiller and thermal mass:** plant topology, BMS read/write points, operating envelope, zones served, weather/occupancy sensitivity, comfort/humidity risk, response and rebound.
- **Lighting, lifts/escalators and other scheduled loads:** controllable circuits, service/egress constraints, schedule, measured reduction and restoration behavior.
- **PV:** forecast/measurement, curtailment capability and the specific producer/consumer settlement contract. Keep export revenue distinct unless an approved arrangement links it.
- **ESS:** usable power/energy, SOC/temperature/protection limits, round-trip losses, warranty/degradation, and verified export/settlement rights; U-004 remains open.
- **EV charging:** charger control/telemetry, vehicle connection and departure/SOC requirements, user override, and metering/contract boundary.
- **Thermal hot water, kitchen, laundry, refrigeration and other process loads:** only include when a site owner confirms safe scheduling bounds and measurement access.

This is a characterization list, not a claim that each asset is flexible or available in Macau pilot sites.

## G2 exit evidence and decision

G2 may close only when the selected pilot's in-scope assets have a versioned, source-backed flexibility envelope and constraints; at least one repeatable site-approved observation/response protocol has measured response, duration and recovery/rebound where active response is allowed; comfort/service/safety impacts are bounded; the economic mechanism maps to verified meter, contract and tariff inputs; and unsupported asset classes are explicitly excluded.

Until those conditions are met, G2 remains OPEN, no site-level dispatchable capacity is claimed, and D-003 remains a pilot-priority hypothesis to validate rather than a measured generalization.

## Sources

- DSEC, **Energy Statistics, 3rd Quarter 2025** (published 2025-11): https://www.dsec.gov.mo/getAttachment/f7256b86-0c0a-4d1f-b35a-c37369890410/E_ENE_FR_2025_Q3.aspx
- DSPA, **Energy and Services Comprehensive Data, 2nd Quarter 2026** (page last modified 2026-09-25; report includes CEM-supplied electricity demand/sales, customer-group sales, and system peak): https://www.dspa.gov.mo/energyfigures/tc/en-chn_q226.pdf
- DSPA, **2023 Macao Green Hotel Awardees — Gold Award — Galaxy** (last modified 2024-04-25): https://www.dspa.gov.mo/h_award_detail.aspx?a_id=1710484470
- CEM, **Macao Energy Saving Activity 2026 Hotel / Resort Group**: https://www.cem-macau.com/en/event/75/
- Project authority: `docs/00-authority/decisions/DECISIONS.md` (D-003, D-032, D-033, D-037), `docs/00-authority/decisions/OPEN-QUESTIONS.md` (U-004, U-006–U-008, U-012, U-014–U-017), and `docs/01-research/evidence/G1-PV-GRID-INTERCONNECTION-2026-10.md`.
