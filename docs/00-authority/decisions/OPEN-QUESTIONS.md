# Open Questions / Blocking Unknowns

## U-001 — CEM Pu averaging/integration interval
**Status:** UNKNOWN / G1 BLOCKER  
**Verified public boundary (2026-10-04):** Administrative Regulation 25/2022 defines Group B Pu in Article 10 as the highest periodically measured average active power; Group C applies Article 10 through Article 17, and Article 24 states the corresponding rule for Group D. Article 14 prescribes loss-compensation calculations for low-voltage Group B. Current CEM B/C/D tariff pages describe Pu as the highest measured demand during a billing period. The reviewed sources do not state the numeric interval, fixed/block versus rolling semantics, boundary/clock convention, or meter/register configuration.  
**Unknown:** Exact averaging/integration window used for settlement (e.g. 15 min, 30 min or another period), including class/topology-specific differences.  
**Resolution path:** obtain the CEM demand-register/configuration specification and matched B/C/D bill plus interval/load-profile data; written CEM confirmation if the meter profile does not expose the settlement interval.  
**Production behavior:** never hard-code 15 minutes.  
**Evidence:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`.

## U-002 — Commercial PV settlement topology
**Status:** CONTRACT-SPECIFIC  
**Question:** gross production FIT, surplus export, self-consumption, zero export or another structure for a given project?  
**Resolution path:** customer PV purchase agreement, meter diagram and CEM interconnection documents.

## U-003 — Third-party high-frequency CEM AMI access
**Status:** UNKNOWN  
**Verified public boundary (2026-10-04):** CEM reports full AMI coverage, utility-side smart-meter data retrieval and customer-facing daily consumption history for the past 30 days. Its 2024 Sustainability Report also describes CEM-side customer-substation telemetry pilots. These sources do not establish that customer or third-party systems can access those feeds, nor an external API, interval, export format, latency/backfill, retention, authorization or commercial terms.  
**Question:** Can an authorized commercial customer or its named third-party service provider obtain a supported high-frequency interval feed from CEM, by API or another documented channel, and under what data, security and commercial conditions?  
**Resolution path:** Obtain current written CEM technical/commercial confirmation tied to the commercial use case and account-authorized access; require a sanitized sample/schema and protocol/interval specification before selecting a connector. No request has been sent.  
**Design implication:** keep local meter/BMS or another authorized data path viable until access is evidenced.

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
**Known (public-source boundary):** CEM's Chinese B-group page calls the line “政府稅” and describes it as payable for monthly use of the electrical installation; its Portuguese current B/C/D pages use “Taxa de Exploração” and describe a monthly installation-use charge. Those are CEM billing labels, not conclusive legal classification. The reviewed Administrative Regulation 25/2022 (Arts. 3, 8, 36) and Executive Order 105/2022 tariff annex define tariff components, group formulas/parameters and periods, but no separate B/C/D formula for this line was found in those instruments. That bounded review does not exclude another current legal, concession or contractual basis. A historical CEM Group A leaflet described government remittance and an installation-type-dependent formula under the former regime; it does not establish the present basis or B/C/D rule. Current A/EV examples do not establish a B/C/D formula.  
**Unknown:** current legal/contractual characterization and authority for the separate line; authoritative B/C/D formula, classes, exceptions, effective dates and relationship to the current tariff-system instruments.  
**Resolution path:** current consolidated legislation/Executive Order 105/2022 annex review; CEM billing tariff specification; anonymized B/C/D bill examples and written CEM clarification.  
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
**Status:** PARTIALLY RESOLVED / CITED PREFLIGHT ARTIFACT NOT IN REPOSITORY / LIVE HASH RECHECK REQUIRED  
**Recorded authority assertion:** The prior record says official v0.9.0 API regression fixtures establish 182 inputs, 204 measurements and 134 forecast points, with exact fixture SHAs in `G7.2-R0-HARNESS-PREFLIGHT.md`. A recursive audit of all seven current GitHub branch trees (including `main`, PR #8, and the other current branches) found no dedicated path matching `G7.2-R0-HARNESS-PREFLIGHT`, G7.2, R0 or PREFLIGHT. The originating conversation read on 2026-10-04 also had no attached files. The counts and hashes are therefore not independently auditable from available repository/conversation artifacts; retain them as reported, not verified.
**Resolution path:** Restore the referenced preflight artifact to the canonical research/MVP location or link its immutable source and provenance; reconcile point counts and hashes against the pinned v0.9.0 API fixtures. Then re-run metadata hash/count checks on the approved live deployment and preserve the exact run manifest and outputs.
**Remaining runtime check:** A live v0.9.0 deployment must reproduce the authoritative metadata hashes/counts before a run is accepted. Do not mark U-013 fully resolved until both the preflight evidence and live recheck are reviewable.

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
**Known (updated 2026-10):** The standard low/medium-voltage supply conditions republished under Law 26/2024 make ordinary supplied electricity specific to the contracted location and prohibit its resale/transfer; own generation in parallel with the public grid requires the applicable written approval, subject to the separately regulated PV route. The extended/amended CEM public electricity-supply concession contract, published in Official Gazette Series II 49/2025 and effective 2026-01-01, further states that distribution of electricity self-generated through private installations is outside the public concession only within the same concession/private land parcel as the installation and subject to prior written SAR authorization. The concession requires CEM to purchase renewable output under government-set tariff/price arrangements using bidirectional metering and applicable purchase contracts. Annex VIII allows SAR-owned public renewable generation to offset public lighting or other consumption designated by the SAR; this is not a private customer's virtual-netting entitlement. Administrative Regulation 20/2014 and DSPA/CEM describe the PV-to-grid producer feed-in route (with purchase terms up to 20 years); CEM's application procedure requires legal right to use the installation site and documents a behind-the-meter configuration where anti-backflow may be required. Third-party rooftop ownership/PPA and host-supply treatment remain unsettled. Separately, Administrative Regulation 20/2014, Technical Regulation Article 12(4), caps a PV system's total installed capacity at 50% of the public-grid supply capacity to the installation or 50% of the upstream supply capacity to its transformer. This is project-specific interconnection feasibility evidence, not a cross-site settlement rule; the regulation's “or” wording must follow project-specific regulatory/CEM interpretation. CEM/CSGI's announced cross-border GEC procurement model concerns environmental attributes and is not evidence of physical remote-PV delivery or CEM bill netting.
**Unknown:** Whether any specific CEM/SAR approval, contract, or settlement arrangement authorizes distribution across separate land parcels, remote account credits, virtual allocation, wheeling, third-party PPA supply, or host-building self-consumption by a separate system owner; how such a structure would be metered, priced and billed. The concession contract narrows the general same-parcel private distribution exception but does not resolve these project-specific arrangements.  
**Resolution path:** Obtain current CEM PV application/interconnection and purchase contract forms; request written CEM/DSPA/DSSCU clarification on host self-consumption, generator ownership/roof lease or third-party PPA, and any remote account allocation; inspect anonymized contracts, meter diagrams and bills for any actual approved arrangement.  
**Design implication:** keep PV producer feed-in revenue separate from another site's consumption settlement unless a verified arrangement explicitly links them. Do not model off-site PV as a direct customer bill credit by default.


## U-026 — Official Macau grid-connected PV count reconciliation
**Status:** PARTIALLY RESOLVED / CAPACITY AND SCOPE RECONCILIATION OPEN
**Question:** Do CEM's connected-system count and DSPA's connected-and-selling count use identical reference dates, operational status and capacity/energy definitions?
**Known:** CEM's PV introduction page reports 12 connected systems, 4,193 kWp and more than 6 million kWh generated as of January 2026. CEM's 2026-06-08 announcement reports 12 grid-connected systems and more than 6 million kWh cumulatively, without a capacity update. DSPA's page last revised 2026-09-01 reports that by 2026-08-31, 12 systems had proceeded to grid interconnection and electricity sales from 39 consultation cases. The current reported count is consistent at 12, but time cutoffs and the status/category wording differ. The previously recorded CEM figure of 18 systems / 4,762 kWp as of June 2026 is unsupported by the primary CEM pages reviewed and is withdrawn.
**Resolution path:** Confirm the common reference date, whether CEM's figure counts all connected systems versus systems already selling, and updated capacity/cumulative generation scope with CEM/DSPA before constructing a time series.
**Design implication:** Current evidence supports existence and reported scale of grid-connected PV, but do not infer capacity growth, project/site count equivalence or generation trend from the mismatched cutoffs.


## U-027 — Personal data classification and cross-border processing
**Status:** OPEN / DATA-GOVERNANCE BLOCKER BEFORE CUSTOMER-DATA INTAKE OR EXTERNAL PROCESSING  
**Verified public boundary (2026-10-04):** Law 8/2005 defines personal data by relation to an identified or identifiable natural person (Art. 4(1)(1)); Articles 19/20 govern transfers outside Macau, while Article 21(1) is a separate automated-processing notification provision. GPDP guidance says the applicable transfer route depends on the facts; the reviewed guidance page reports no published adequacy list. These sources do not classify Energy OS telemetry as a category.  
**Unknown:** Which project datasets/flows identify or can be linked to people; controller/processor roles, purposes/notices and retention; actual storage, backup, support, subprocessor and AI-service locations; and which legal conditions, notices, notifications or authorizations apply.  
**Resolution path:** inventory each dataset and end-to-end flow, including logs/support; verify vendor and subprocessor regions/access; obtain case-specific review by the responsible Macau privacy/legal owner before customer-data intake or external processing.  
**Design implication:** keep data location and access boundaries explicit; minimize data and access; do not assume Macau-only hosting is required or sufficient, and do not assume building telemetry is categorically personal or non-personal.  
**Evidence:** `docs/01-research/evidence/MACAU-PERSONAL-DATA-AND-CROSS-BORDER-FLOW-REVIEW-2026-10.md`.
