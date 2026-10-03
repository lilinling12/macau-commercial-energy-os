# G7 Reference Simulator & Pilot Validation

**Status:** ACTIVE / INCOMPLETE. The repository records G7.2 live R0 baseline/no-op as pending and U-017 as open. No authorized Macau customer pilot or measured customer outcome is evidenced here.
**Purpose:** Establish reproducible reference-simulator behavior, safe progression to an authorized Macau site, and credible measurement and verification without mixing fixture, simulation and customer evidence.
**Authority:** Original G0–G7 research framework; G7 definitions and cross-Gate dependencies in `docs/00-authority/ROADMAP.md`; U-012, U-013, U-015–U-017; G1/G2/G3/G6 records; G7.2-R0 harness authority where its source artifact is available.
**Boundary:** Simulator success is engineering evidence, not Macau customer or tariff evidence. No field command, customer savings claim, or pilot readiness follows from this Gate without separate G6, site authorization and acceptance evidence.

## Evidence classes

Record each run and claim as one of:

1. **Contract/fixture evidence:** pinned schemas, API regression fixtures, point metadata and deterministic contract tests.
2. **Reference simulation:** a versioned simulator, testcase/build, configuration, initial state, seed, exogenous inputs and replayable run artifacts.
3. **Authorized live-site baseline/no-op:** site-approved read-only or identity/no-op runs with verified point bindings, timestamps, quality, coverage and run manifest.
4. **Authorized intervention/response:** a site-approved test under G6 controls, with pre-agreed operating boundaries, operator veto and rollback.
5. **Measured pilot outcome:** customer-agreed baseline and M&V method, matched operating period, verified meter/contract/tariff context, confounder handling and customer review.

Never relabel an earlier class as a later one. Synthetic fixtures, BOPTEST results, public aggregate statistics, and vendor demonstrations are not Macau customer performance evidence.

## Research and validation questions

1. Does the pinned reference runtime expose the intended R0 points and metadata consistently, and can runs be reproduced from an immutable manifest?
2. Does a fresh baseline/no-op identity trajectory preserve expected behavior under the approved R0 configuration, timestamps and point bindings?
3. Which signal-quality, coverage, clock, initialization, stale-data and simulator-health conditions invalidate a run?
4. How should candidate response be paired against a compatible baseline, including pre-event, event and recovery periods, weather/occupancy/schedule changes and missing observations?
5. Which outcomes can be attributed to the tested action, and which remain confounded or outside the measurement boundary?
6. What site permissions, safety controls, operator roles, stop conditions and rollback evidence are mandatory before a live intervention?
7. What user, service, comfort/SLA, economic and operational outcomes will the customer accept for a pilot decision?
8. Which findings are reference-simulator only, site-specific, contract-specific or suitable for a broader claim?

## Current evidence boundary

- U-013 currently reports that v0.9.0 API regression fixtures define 182 inputs, 204 measurements and 134 forecast points, and cites exact fixture SHAs in `G7.2-R0-HARNESS-PREFLIGHT.md`. No dedicated preflight path was found in an audit of all seven current GitHub branch trees; the originating conversation read on 2026-10-04 had no attached files. Counts and hashes therefore cannot be independently audited from available repository/conversation artifacts. Treat them as a recorded external assertion until the artifact is restored or linked to a stable accessible authority.
- G7.2 live R0 baseline/no-op remains pending. A fresh live deployment must reproduce the authoritative metadata/hashes and complete the required baseline and no-op identity trajectory before response/control interpretation.
- U-017 remains open for live SAT/CHWS response and rebound interpretation. Do not claim site-wide power reduction from those perturbations until the measurement boundary, paired baseline, total-power response and recovery are resolved.
- U-012 Macau reference-building calibration and U-015 weather-source validation remain open. BOPTEST is an engineering harness, not a calibrated Macau hotel/commercial-building ground truth.
- No selected customer/site authorization, pilot protocol, customer-accepted baseline, production integration, or measured Macau commercial outcome is recorded by this Gate document.

## Historical sub-gate status report requiring source recovery

A prior assistant message in the originating ChatGPT conversation stated that G7.1, G7.3 and G7.4 research had been completed while G7.2 live execution remained pending. This is a historical conversation statement, not a Gate decision or source artifact. The conversation read on 2026-10-04 had no attached files, and the current repository branches contain no dedicated G7.1/G7.3/G7.4 evidence packet or G7.2 preflight path by filename. Therefore those sub-gate completion claims remain **REPORTED / UNVERIFIED** and are not promoted to current status.

**Resolution:** recover the referenced original Library/research artifacts or immutable links; map each claimed sub-gate to its question, evidence, exit criteria, decision/approver and residual unknowns; then update this Gate, Evidence Register and CURRENT from the recovered sources. Until then, report only the independently reviewable current state: G7.2 live R0 baseline/no-op pending, U-017 open, and no authorized Macau pilot outcome evidenced in this repo.

## Required artifacts for each accepted run

1. **Run manifest:** unique run ID; evidence class; owner/approver; repository and artifact revisions; simulator/API/runtime versions; testcase/build and image digests where applicable; configuration; seed; initial state; time zone and time grid; input/output point-set identity; exact command and environment.
2. **Source and mapping snapshot:** site/tenant scope; source IDs; point mappings and revisions; units, direction, multipliers, timestamps, quality/freshness and coverage policy; simulator/site binding status.
3. **Baseline/no-op record:** baseline selection and period; no-op identity expectations; preconditions; observed trajectory; tolerances and any deviations with disposition.
4. **Raw evidence:** original inputs, outputs, logs, telemetry, simulator artifacts and relevant metadata hashes, retained with integrity identifiers and access controls.
5. **Analysis:** paired comparator; pre-event/event/recovery windows; weather, occupancy, schedule and operating changes; missingness; uncertainty; confounders; comfort/service/equipment impacts; cost result and exact tariff authority where applicable.
6. **Decision record:** what the evidence supports; what it does not support; reviewer/customer disposition; residual unknowns; next authorized step or stop condition.

A manifest records evidence; it does not prove the run passed. Acceptance criteria and observed results must be separately recorded.

## Required outputs

- A reproducible, version-pinned reference run set for the in-scope simulator cases, separated from live-site results.
- An auditable R0 point/metadata preflight with exact artifact locations, hashes, counts, permitted changes and live recheck procedure.
- Fresh, approved G7.2 baseline and no-op identity evidence, with quality and invalidation rules.
- A paired response and recovery protocol that resolves or explicitly bounds U-017 before interpreting response.
- A pilot M&V plan agreed with the customer, including meter/account/contract scope, baseline, comparison window, adjustments/confounders, outcome metrics and acceptance decision.
- Site authorization, operating/safety boundaries, named roles, stop conditions, rollback and incident ownership for any live intervention.
- Evidence-register, Gate, Open Questions and CURRENT updates that preserve evidence class and residual uncertainty.

## Exit criteria

G7 may close only when its applicable sub-gates and the evidence packet demonstrate:

1. Reference cases are reproducible from pinned artifacts and manifests, with fixture/preflight assertions independently auditable.
2. G7.2 live baseline/no-op requirements are completed on an authorized live R0 deployment, including the required identity trajectory, point/mapping/hash recheck, telemetry quality and explicit deviations.
3. Any response claim has a compatible paired baseline, defined measurement boundary and time windows, complete pre-event/event/recovery analysis, uncertainty and confounder treatment; U-017 is resolved or the claim is explicitly excluded.
4. Macau-specific calibration/weather claims are supported by appropriate evidence, or the pilot's use is explicitly limited so no unsupported generalization is made.
5. Any intervention is separately authorized and passes applicable G6 site-local safety, veto, manual override, offline/failure and audit controls. G7 does not waive G6.
6. Customer outcome claims use a customer-agreed, bill/contract/meter-linked M&V method, separate modeled estimates from measured outcomes and document discrepancies/limitations.
7. The customer/site reviewer and project owner record a proceed, remediate or stop decision with residual risks, operational handoff and rollback/incident ownership.

If only a reference-simulator objective is in scope, report that sub-result explicitly; do not mark the full pilot Gate closed. Pilot readiness may be declared only for a named site, scope, configuration and authorization window.

## Dependencies

- **G1:** verified meter boundary, tariff/contract rules and Golden Bill evidence for any bill-grade economic claim.
- **G2:** measured asset flexibility, operating constraints, response and rebound before assigning realizable value.
- **G3:** validated topology, point mappings and settlement links for the measured site.
- **G4/G5:** forecast/optimization evidence is evaluated against this Gate's reproducible baselines; simulation cannot close live validation requirements.
- **G6:** independent safety and site authorization before controlled action.
- **G6.9-R2:** runtime choice does not determine simulator truth or customer acceptance; preserve pinned environment details for reproducibility.

## Related records

- Roadmap and WP-3: `docs/00-authority/ROADMAP.md`
- Current handoff: `docs/00-authority/handoff/CURRENT.md`
- Open Questions U-012/U-013/U-015/U-016/U-017: `docs/00-authority/decisions/OPEN-QUESTIONS.md`
- G6 safety controls: `docs/01-research/gates/G6-safety-control.md`
- Energy Graph design and G3 Gate: `docs/03-architecture/detailed-design/ENERGY-GRAPH-DETAILED-DESIGN-v0.1.md`, `docs/01-research/gates/G3-energy-graph.md`
