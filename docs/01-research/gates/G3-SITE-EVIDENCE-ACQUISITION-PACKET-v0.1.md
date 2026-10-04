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
| Resolution | RESOLVED / UNMAPPED / AMBIGUOUS / CONFLICTING / STALE / OUT_OF_SCOPE |
| Consequence | Which product calculation or workflow is blocked, scenario-only or eligible |
| Disposition | Validated in scope / excluded / unresolved-deferred, with reason and approver |

A mapping is not resolved until supporting evidence agrees on identity, scope, direction and effective time. Preserve conflicting assertions; do not silently overwrite history. Ineligible or unresolved mappings must fail closed for settlement-grade attribution and recommendations that depend on them. Keep tariff-rule interpretation with G1 and flexibility/response claims with G2.

## 6. Execution sequence and exit record

1. Obtain owner/site authorization and privacy/security intake approval; otherwise stop before requesting or accepting evidence.
2. Choose the smallest representative scope and bundles; document omitted asset classes and boundaries.
3. Inventory and hash authorized source items in the restricted manifest; validate provenance and temporal scope.
4. Draft physical/electrical topology separately from settlement/economic mappings; reconcile against measurements and site review.
5. Update relevant U-items, Evidence Register and Energy Graph design with sanitized findings; preserve disputes and gaps.
6. Submit the reviewed evidence packet to the G3 Gate approver. Record what is validated, excluded and unresolved, the approver, date and downstream consequences.

This preparation packet does not itself pass G3, approve production schemas or graph technology, authorize customer contact/data intake, close G1/G2/G6/G7, or permit field control. Until the site-specific evidence and review exist, G3 remains OPEN.
