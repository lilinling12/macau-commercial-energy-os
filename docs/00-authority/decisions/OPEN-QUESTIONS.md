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
**Verified public boundary (2026-10-04):** CEM reports full smart-meter coverage and customer-facing daily consumption history. The reviewed official material does not establish an external third-party API, high-frequency interval, export format, retention or commercial access terms.  
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

## U-009 — Exact B/C/D government tax / installation-use charge formula
**Status:** UNKNOWN / G1 BLOCKER  
**Known:** CEM Chinese bill material labels it “政府稅”; the Portuguese bill guide calls the corresponding line “Taxa de Exploração”. Both describe a monthly charge for use of the electrical installation. Current B/C/D public tariff pages show the monthly item but no calculation formula. Administrative Regulation 25/2022's reviewed tariff formulas do not establish the formula for this separate line. A-group/EV examples show `0.75 × √subscribed demand`, but do not prove the B/C/D rule.  
**Unknown:** legal/contractual characterization and authoritative B/C/D formula, classes, exceptions and effective dates.  
**Resolution path:** applicable legislation and Executive Decree 105/2022 annex review; CEM billing tariff specification; anonymized B/C/D bill examples and written CEM clarification.  
**Design implication:** keep the monthly charge as an explicit unknown/contract-versioned tariff component; never reuse the A/EV formula for B/C/D without evidence.  
**Evidence:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`.

## U-010 — Golden Bill Test cases
**Status:** NOT ACQUIRED / G1 BLOCKER  
**Need:** at least one real B/C customer bill + interval/load-profile evidence and a second case from a different tariff class.  
**Gate:** Tariff Engine cannot be marked production-ready until reconstruction error is <=0.5% with zero unexplained balancing adjustment.

## U-011 — Commercial bill rounding / odd-amount carry-forward semantics
**Status:** PARTIALLY RESOLVED / GOLDEN-BILL VALIDATION REQUIRED  
**Verified public boundary (2026-10-04):** CEM's bill explanation for A and B/C/D says an odd amount is automatically carried to the next bill and the amount payable is rounded down to the nearest ten.  
**Unknown:** Exact denomination semantics, calculation order across charges/tax/credits, ledger representation/direction, negative adjustment treatment, and whether/how component values are rounded; interaction with reconstruction tolerance remains unverified. No commercial Golden Bill has been reconciled.  
**Resolution path:** real B/C/D bills + matching meter/load-profile evidence and CEM billing explanation/contract confirmation.  
**Design implication:** treat the public statement as an invoice-payable-level behavior only; do not infer component rounding or round each interval. Keep settlement policy explicit.

**Evidence:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`.

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


## U-018 — Candidate A production Temporal topology
**Status:** OPEN / G6.9-R2
**Question:** Does a Bun/Hono/Effect API plus Node-backed Temporal TypeScript Worker produce enough engineering advantage to justify the extra runtime topology compared with C+?  
**Resolution path:** common vertical slice + AI engineering trials + chaos/soak.


## U-019 — Effect 4 agent-maintainability advantage
**Status:** OPEN / G6.9-R2
**Question:** Do Effect 4 typed failure/dependency/resource semantics reduce hidden defects and review burden for current coding agents, or increase compiler/context repair cost?  
**Resolution path:** controlled T01–T10 trials and reviewer scoring.


## U-020 — Go-core product-iteration cost
**Status:** OPEN / G6.9-R2
**Question:** Does generated contract sharing keep Go core + TS product iteration within 10–20% of all-TS engineering cost while materially simplifying command/Edge reliability?  
**Resolution path:** candidate C+ trial metrics.


## U-021 — Live full-stack bake-off execution environment
**Status:** OPEN / EXECUTION BLOCKER
**Question:** Establish a pinned Linux x86-64 environment containing Bun 1.4.2, Node 24 LTS, Go 1.27.x, Python, Docker/Compose and common Postgres/Timescale/Temporal/NATS/MQTT/OTel services.  
**Current environment:** lacks Bun, Deno, pnpm and Docker, so Step 3A can build the pack but cannot produce comparable full-stack runtime results.

## U-022 — Production command signing and Edge key lifecycle
**Status:** OPEN / G6 SECURITY
**Question:** Select production command signing algorithm/device identity model, provisioning, rotation, revocation and optional hardware-backed key storage.  
**Constraint:** must preserve D-070 canonical payload semantics and deterministic replay/audit behavior; Step-3B HMAC is not production authority.



## U-023 — Framework-native Step-3D execution
**Status:** OPEN / G6.9-R2
**Question:** Under pinned Bun 1.4.2, Node 24 LTS and Go 1.27, do Candidate A/B/C+ preserve the Step-3C semantic invariants when Hono/Effect, NestJS/Fastify and Temporal are actually introduced?  
**Resolution path:** pinned Linux x86-64 integration runner with common Postgres/Timescale, NATS, MQTT and OTel services.


## U-024 — Durable exactly-once-effect behavior under real workflow/broker failures
**Status:** OPEN / G6.9-R2 HARD GATE
**Question:** Does the production workflow topology maintain zero duplicate field writes through worker kill, ACK loss, broker partition, DB restart and retry storms?  
**Known:** the local Step-3C persisted-state crash-after-field-write scenario passes for Node and Go semantic shells.  
**Resolution path:** Temporal-backed 100 kill/recover trials plus MQTT partition/reconciliation tests in Step 3D/4.

## U-025 — Cross-site PV procurement and settlement rights
**Status:** UNKNOWN / G1 BLOCKER FOR OFF-SITE PV CUSTOMER ECONOMICS  
**Known:** The current republication of Decree-Law 43/91/M under Law 26/2024 (including the 53/98/M amendment) restricts ordinary supplied electricity to the contracted location and bars its resale/transfer. It also requires written concessionaire approval for a consumer's own generation to operate in parallel with the public grid, except the separately regulated PV route. Administrative Regulation 20/2014 and DSPA/CEM describe a specific approved PV interconnection and producer-to-CEM feed-in purchase route (up to 20 years).  
**Unknown:** Whether host-building self-consumption can be structured under current CEM contract terms and how that differs from sale of injected surplus; whether a remote customer can obtain bill credits, netting, wheeling, virtual allocation or another recognized settlement benefit. Public sources found so far do not establish those customer entitlements.  
**Resolution path:** Obtain current CEM PV application/interconnection and purchase contract forms; request written CEM/DSPA/DSSCU clarification on host self-consumption, generator ownership/roof lease or third-party PPA, and any remote account allocation; inspect anonymized contracts, meter diagrams and bills for any actual approved arrangement.  
**Design implication:** keep PV producer feed-in revenue separate from another site's consumption settlement unless a verified arrangement explicitly links them. Do not model off-site PV as a direct customer bill credit by default.


## U-026 — Official Macau grid-connected PV count reconciliation
**Status:** OPEN / G1 EVIDENCE QUALITY
**Question:** Why does CEM's current PV page report 18 connected PV systems as of June 2026 (4,762 kWp), while DSPA's page last revised 2026-09-01 reports 12 grid-connected-and-selling cases as of August 31, 2026?
**Known:** The sources use different units ("systems" and "cases") and may use different scopes or update cycles.
**Resolution path:** Confirm the system/case definitions, reporting cutoffs and treatment of connected-but-not-selling or multi-installation projects with CEM and DSPA.
**Design implication:** Do not combine these figures or use them as a time trend until reconciled.
