# G3 Site Evidence Acquisition Packet v0.1

**Gate:** G3 — Energy Digital Twin / Energy Graph  
**Status:** Prepared, not sent. No pilot site is selected; no external contact or site-data collection is authorized or claimed.  
**Purpose:** Define the minimum authorized evidence bundle needed to model one representative Macau site's physical/electrical topology and its separately evidenced settlement relationships.

## 1. Scope and authority

This packet operationalizes the evidence requirements in `docs/01-research/gates/G3-energy-graph.md`. It is site-neutral: it does not select a customer, building segment, supplier, data format, database, graph service or production deployment.

Use it only after the project owner selects a site/discovery scope, the customer/site authority approves the purpose and permitted records, a restricted intake location and retention policy are agreed, and the responsible privacy/legal reviewer completes any dataset-specific review required by U-027. No personal data, credentials, access tokens, private bills or raw customer telemetry should be sent to a public issue, this repository, ordinary chat or an unapproved AI/model service.

Keep this packet coordinated with:
- G1's tariff and Golden Bill request rules: `docs/01-research/gates/G1-EVIDENCE-ACQUISITION-PACKET-v0.1.md`;
- G2's site measurement and flexibility protocol: `docs/01-research/evidence/G2-MACAU-COMMERCIAL-LOAD-FLEXIBILITY-EVIDENCE-2026-10.md`;
- G3 Gate criteria: `docs/01-research/gates/G3-energy-graph.md`;
- Macau data governance boundary: `docs/01-research/evidence/MACAU-PERSONAL-DATA-AND-CROSS-BORDER-FLOW-REVIEW-2026-10.md`.

## 2. Preconditions before any request or intake

1. Record site owner/authorized representative, site scope, purpose, permitted evidence classes, users, retention/deletion, onward sharing and a named approval record. No request is sent until the project owner explicitly authorizes it.
2. Inventory fields and flows before receiving data. Ask for the least detailed evidence that can answer the G3 question. Do not request room-level occupancy, named staff/customer activity, credentials, security-sensitive network details or identifiable logs unless necessary, explicitly authorized and privacy-reviewed.
3. Verify the restricted intake location, encryption, role access, transfer method, backup/deletion behavior and access logging with the data owner. Keep re-identification keys outside the analysis bundle.
4. Assign a random evidence-case ID. Keep the identity/site lookup separately under the data owner's control. Store no names, account numbers, exact addresses, contact details, credentials, or unredacted customer documents in the public repo.
5. Record unavailable, refused, disputed or out-of-scope items as limitations. Do not infer an edge, meter/account relationship or right from a missing document, label, drawing or operator statement.

## 3. Request bundles

Request only bundles needed for the approved scope. G1 tariff/bill semantics and G2 controllable-capacity measurement remain owned by their respective Gates; this packet links to them instead of duplicating their acceptance rules.

| Bundle | Minimum evidence to request (if authorized) | G3 question answered | Classification / limit |
|---|---|---|---|
| A — Scope, authority and site boundary | Site/building scope diagram; permitted areas and supplies; evidence owner; document dates/versions; named role approvals stored in the restricted manifest | What physical site and evidence boundary is in scope, and who may propose/review mappings? | Site/contract material may be confidential or personal. A descriptive name is not an identifier or permission. |
| B — Electrical topology and metering | Current single-line diagram; supply/transformer and switchboard hierarchy; meter/register schedule; import/export direction; CT/PT ratios and multipliers; meter IDs or consistently pseudonymized source IDs; commissioning/change records | Which electrical nodes and meter boundaries exist, and how do measured directions/quantities relate? | Drawings/registers are documentary evidence; require version/date and reconciliation against meter/commissioning evidence. |
| C — Assets and source points | Equipment/asset schedule; BMS/EMS point list with vendor namespace, point ID, description, unit, direction, scan/sample cadence and read/write capability; mapping/version history; connector/credential owner (no credentials) | Which assets, devices and source points exist, and how stable are source identities? | A point name or operator label is a candidate mapping, not proof of physical or settlement relation. |
| D — Authorized measurement sample | Minimal time-bounded, read-only sample with source timestamps, receive/export timestamps if available, time zone/offset, raw unit/value, quality/status, meter/point identity and known gaps; matching clock/source metadata | Can the proposed topology and measurement directions be reconciled to observed data and quality? | Request aggregated/minimized records. Do not infer accuracy or settlement integration from sampling cadence. G1 owns demand-window truth. |
| E — Settlement boundary references | Pseudonymized supply-point/account/contract references, meter-to-account diagrams or schedules, applicable import/export contract excerpts and matching periods; for bills/meter evidence follow the G1 packet | Which physical meters are contractually linked to which import/export account or producer relationship? | Documentary evidence supports only the scope and effective dates it actually covers. No remote bill credit or cross-parcel allocation is presumed (U-025). |
| F — Operating constraints relevant to graph scope | Site-approved asset availability, zones served, operating schedule, criticality and maintenance/isolation notes; boundaries for any G2 measurement, with personal occupancy details omitted unless expressly necessary/reviewed | Which topology/use relationships are operationally relevant, and which evidence is excluded? | Operator explanation is tagged separately from records/measurement. G2 controls flexibility claims and active-test authorization. |
| G — PV / ESS / EV (only if in scope) | Installation location/site-use right, system owner/operator, approved connection/capacity basis, import/export meter diagram, producer/export agreement, asset/commissioning details and any explicit allocation/settlement instrument | Are generation/storage/charging physical flows and producer/consumer settlement paths separately evidenced? | Site connection or feed-in purchase alone does not establish another building/account's bill credit; preserve U-025 limits. |
| H — Reconciliation and review | Evidence-owner explanation of known conflicts; site engineer/metering reviewer; corrections, dates, superseded drawings and sign-off for each proposed high-impact relationship | Which assertions are agreed, disputed, stale or unresolved, and by whom? | Sign-off validates only the reviewed scope; it does not close G1/G2/G6/G7 or authorize control. |

## 4. Restricted evidence manifest

For each received item, retain the manifest in the approved restricted store, not this public repository:

- random evidence ID; evidence bundle and question(s) addressed;
- source/issuer/owner role, exact artifact ID, issue/effective date, received date and version;
- site scope and relation/time interval asserted; validity time and knowledge/receipt time kept distinct;
- permitted purpose, access/transfer authorization, sensitivity classification and reviewer;
- original-file digest, redaction/minimization status and restricted storage reference;
- extracted assertions, conflicting sources, confidence and explicit limitations;
- retention/deletion date, backup expiry and reprocessing/replay dependencies.

Only sanitized claim summaries and non-identifying source references may be promoted into the Authority Evidence Register. Preserve the source original only in the authorized restricted store and only for the approved duration.

## 5. Mapping output and acceptance

The analyst produces a versioned draft inventory; a site-authorized technical reviewer checks it before any mapping is marked resolved.

| Field | Required content |
|---|---|
| Entity / relation | Canonical entity or typed relation; physical/electrical or settlement/economic layer |
| Source identity | Source namespace and source ID, pseudonymized where permitted; no identity inferred from label alone |
| Measurement | Metric, unit, direction, multiplier, sampling/time quality and boundary |
| Validity | Effective interval, observed/knowledge time, evidence version and correction link |
| Evidence | Restricted evidence ID, source class, owner role, reviewer and permission status |
| Mapping resolution | `RESOLVED` / `UNMAPPED` / `AMBIGUOUS` / `CONFLICT` / `EXPIRED_MAPPING` / `OUT_OF_SCOPE`; use the Energy Graph machine vocabulary |
| Measurement quality | Freshness, coverage and source-clock/quality state reported separately from mapping resolution; use the Telemetry Ingestion vocabulary |
| Consequence | Which product calculation or workflow is blocked, scenario-only or eligible |
| Disposition | Validated in scope / excluded / unresolved-deferred, with reason and approver |

A mapping is not resolved until supporting evidence agrees on identity, scope, direction and effective time. An expired or absent mapping is distinct from a mapped observation whose source measurement is stale; record both dimensions when applicable. Preserve conflicting assertions; do not silently overwrite history. Ineligible or unresolved mappings must fail closed for settlement-grade attribution and recommendations that depend on them. Keep tariff-rule interpretation with G1 and flexibility/response claims with G2.

## 6. Execution sequence and exit record

1. Obtain owner/site authorization and privacy/security intake approval; otherwise stop before requesting or accepting evidence.
2. Choose the smallest representative scope and bundles; document omitted asset classes and boundaries.
3. Inventory and hash authorized source items in the restricted manifest; validate provenance and temporal scope.
4. Draft physical/electrical topology separately from settlement/economic mappings; reconcile against measurements and site review.
5. Update relevant U-items, Evidence Register and Energy Graph design with sanitized findings; preserve disputes and gaps.
6. Submit the reviewed evidence packet to the G3 Gate approver. Record what is validated, excluded and unresolved, the approver, date and downstream consequences.

This preparation packet does not itself pass G3, approve production schemas or graph technology, authorize customer contact/data intake, close G1/G2/G6/G7, or permit field control. Until the site-specific evidence and review exist, G3 remains OPEN.


## Dispatch-workflow evidence overlay (optional; G1/G2/G3 boundaries preserved)

Use this overlay only if the owner later authorizes source/load scheduling research for a selected site. It is a prepared checklist, not a data request, site approval, customer contact, or evidence that a pilot is ready. Select only bundles that answer an approved question; record excluded assets and boundaries.

### Dispatch-specific evidence prompts

| Evidence prompt | Minimum sanitized or restricted evidence | Readiness purpose and limit |
|---|---|---|
| Common site-time and measurement grid | Representative read-only intervals from the grid connection meter and only the in-scope source/load meters; IANA site timezone/clock and daylight/clock policy; interval start/end convention; observed vs received timestamp, multiplier/unit/direction, quality, gaps and commissioning changes. | Determine whether observed series can support a common physical comparison horizon. Sampling cadence is not the tariff demand window; G1/D-027/U-001 owns Pu policy. |
| Physical source/load linkage | Versioned single-line/topology plus point-to-asset-to-meter/feeder mappings for grid import/export, PV generation/self-use/export (if present), ESS charge/discharge/SOC, HVAC/chiller, EV charging, hot water or other explicitly in-scope loads. | Establish what can be reconciled at a common electrical boundary. Do not double-count a feeder and its child submeters; unknown flows remain unmapped. Physical linkage does not establish account settlement. |
| Asset capability and service envelope | For assets proposed for a physical scenario, site-reviewed operating ranges, direction, max/min power, ramp/delay, duration, availability, recovery/rebound, SOC/efficiency/protection limits, zones/service dependencies, comfort/humidity/service bounds and override/maintenance states. Link each value to G2 measurement/document/operator evidence and effective period. | Establish whether a bounded schedule scenario can be formed. Nameplate ratings, generic equipment assumptions or operator labels alone do not prove dispatchable capacity. G2 owns measured flexibility/response and active-test approval. |
| Forecast and exogenous input provenance | Existing load/PV/weather/occupancy-operating-calendar inputs only where approved and minimized; issue/recorded time, valid interval, model/source version, uncertainty, quality and missing periods. Prefer aggregated operating schedules; no room-level or person-identifiable activity by default. | Expose data coverage and forecast limits. Do not silently substitute synthetic values for a site forecast; scenario-only inputs must be labeled. |
| Economic-boundary linkage | G1-approved account/contract/bill evidence references; installation/service point, applicable tariff group/class, billed meter(s), effective period, import vs producer/export stream, and explicit physical meter-to-account association. Restricted raw bills remain outside GitHub. | Determine whether an independent economic evaluation is even eligible. G1 owns tariff interpretation, Golden Bill reconciliation, CEM demand window, PV payment/payee and cross-site rights. No physical graph edge becomes a bill credit. |
| SHADOW review and operating authorization | Named human review role and site entitlement, permitted read scope, escalation/override path, evidence review responsibility and audit/retention conditions; confirm that this research phase is read-only. | Support a human-reviewed recommendation flow only. A review or site agreement in this packet does not authorize setpoint writes or active tests; those require separate explicit G6/site approval. |

### Claim/readiness ladder for site intake

| Evidence result | Permitted next claim | Still withheld |
|---|---|---|
| Authorized topology records and reviewed mappings only | Sanitized site topology inventory; missing/conflicting relationships surfaced. | Schedule feasibility, controllability, economics, savings or control. |
| Aligned, quality-qualified physical meter/asset series plus complete in-scope hard constraints | A bounded physical scenario can be assessed for the stated horizon, subject to explicit omitted terms and solver evidence. | Tariff cost, bill-grade demand/savings, equipment response, comfort or service guarantee without their own evidence. |
| G1-matched contract/account/meter rules, required demand/energy inputs and eligible exact evaluator | Scoped economic result for the covered components/horizon; Golden Bill and applicable M&V gates still apply. | Uncovered tariff components, export compensation, cross-site allocation, realized savings. |
| G2-approved paired baseline/response evidence and explicit site test authorization | Measured response/recovery for the named site/asset/test conditions. | Generalized site capacity, untested assets, cloud/device actuation authority. |

### Intake completeness checklist before a dispatch shadow study

- Every included interval series resolves to a site, timezone, physical point, asset and measurement boundary with unit/sign/quality provenance.
- The physical flow equation reconciles at the selected grid boundary; child metering is not added twice, and unknown/loss terms are called out.
- Each proposed load/source has either a reviewed capability/operating envelope or is marked non-dispatchable/out of scope; safety, comfort and recovery limits cannot default to unlimited.
- Any settlement scope is separately evidenced for the same effective period and linked to the actual billed meter/account. Pu uses the verified D-027 measurement policy; dispatch intervals are never substituted.
- PV export is modeled as a physical quantity first; any money/credit requires the producer-side contract, approved interconnection, export meter, effective tariff and payee/account evidence under G1/U-025.
- The output can remain physical-only/SHADOW when economics are blocked; no site-specific cost/saving is displayed from synthetic or incomplete settlement inputs.
- Authorization, privacy classification, restricted storage, minimized export, retention/deletion and named reviewer are approved before any actual collection. No production write/control capability is included.

This overlay connects the current product workflow to the existing G1/G2/G3 evidence boundaries. It does not close any Gate, select a pilot site, authorize collection/contact, prove customer settlement or approve device control.
