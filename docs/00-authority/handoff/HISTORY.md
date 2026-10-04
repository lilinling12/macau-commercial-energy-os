# Handoff History

Append-only record of material changes to the cross-conversation handoff. This file starts on 2026-10-04; it does not reconstruct earlier chat history. Verify each entry against the linked repository state.

## 2026-10-04 — Continuity entry points and task-packet references

- **Change:** Audited AI research/coding continuity files on the open PR #8 branch. The canonical task-packet template is `docs/04-engineering/ai-coding-governance/TASK-PACKET-TEMPLATE.md`. The handoff README's previous reading order named a missing `HISTORY.md` and treated root-level `decisions/`, `evidence/`, and `research-gates/` as handoff subdirectories; these paths are corrected in this update.
- **Status:** Documentation correction on `docs/product-architecture-roadmap`; PR #8 remains open/unmerged. No product, architecture, Gate, or technology decision is made.
- **Validation boundary:** Documentation authority/hygiene checks will be reported against the exact resulting PR head. This entry does not claim application validation or Gate completion.
- **Related records:** `docs/00-authority/handoff/README.md`, `CONTINUATION-PROTOCOL.md`, `CONTINUE-PROMPT.md`, `CURRENT.md`, and `docs/04-engineering/ai-coding-governance/TASK-PACKET-TEMPLATE.md`.


## 2026-10-04 — G1 evidence acquisition plan

- **Change:** Added a prepared evidence acquisition packet for U-001/U-009/U-010/U-011, including demand-register fields, charge-basis/formula fields, matched Golden Bill requirements, privacy-safe handling and evidence sufficiency criteria. Linked it from the G1 Gate, Gate index, Master Index and CURRENT.
- **Status:** Plan only. No request was sent, no customer data was received, no G1 unknown was resolved, and no Gate was closed. Customer/CEM contact requires owner authorization and an approved secure intake path.
- **Validation:** The packet's source commit `36f3038b7d4330c7b3fd45b41d57208b017efdd3` passed Repository Hygiene and Authority Structure checks. The history-only update is subject to exact-head checks.
- **Related records:** `docs/01-research/gates/G1-EVIDENCE-ACQUISITION-PACKET-v0.1.md`, `docs/01-research/gates/G1-tariff-settlement.md`, `docs/00-authority/handoff/CURRENT.md`, and `docs/00-authority/MASTER_INDEX.md`.

## 2026-10-04 — Telemetry durability task packet

- **Change:** Added `docs/04-engineering/ai-coding-governance/task-packets/ARCH-INGEST-RELIABILITY-001.md` as the active packet for durable telemetry receipt/publication design, owner decision #12, PR-02/VS-003 acceptance, and future runtime proof. Linked it from CURRENT.
- **Status:** Review draft on PR #8; no owner decision, connector protocol, persistence/outbox mechanism, Gate closure, or runtime verification is implied.
- **Validation boundary:** Exact-head repository governance checks are required for the commit containing this entry; prior documentation checks do not validate application behavior.
- **Next:** Review decision #12; inventory authorized connector protocol/identity behavior; then create the implementation packet only after connector, data-governance, contract, and runtime authority are settled.

## 2026-10-04 — Telemetry protocol acknowledgement boundary

- **Change:** Reviewed OASIS MQTT 5.0 QoS acknowledgements and RFC 9110 HTTP 202 semantics. Synchronized the telemetry architecture, PR-02 traceability, VS-003 acceptance, implementation readiness audit, task packet and CURRENT handoff to distinguish protocol/broker acknowledgement from an application-level durable-capture receipt. A broker ACK counts as RAW_DURABLE only if that broker is explicitly the authoritative raw store and persistence/failover/recovery are verified.
- **Evidence:** `docs/03-architecture/detailed-design/TELEMETRY-INGESTION-AND-DATA-QUALITY-DETAILED-DESIGN-v0.1.md` §9 and references. This is a logical design correction; connector mapping, runtime behavior and Gate closure remain unverified.

## 2026-10-04 — Step 3D runner hosting constraints

- **Change:** Reviewed official GitHub Actions limits, runner specifications and security guidance. Added execution-host and public-repository trust-boundary requirements to the Step 3D readiness plan and machine-readable runner blockers; added owner review item #13 and synchronized the product/architecture review packet and CURRENT handoff.
- **Evidence:** GitHub-hosted jobs have a six-hour execution cap, below the bake-off's continuous 24-hour soak. Self-hosted jobs allow up to five days and require Linux + Docker for container services, but GitHub warns that public-repository PR code can compromise persistent self-hosted runners. A clean, isolated, fixed-resource execution host with a reviewed/trusted dispatch boundary is therefore still required.
- **Status:** Research and documentation only. No runner was provisioned, no Step 3D experiment was executed, and no production architecture was selected.
- **References:** [Actions limits](https://docs.github.com/en/actions/reference/limits); [hosted runner specifications](https://docs.github.com/en/actions/reference/runners/github-hosted-runners); [self-hosted runner requirements](https://docs.github.com/en/actions/reference/runners/self-hosted-runners); [secure use](https://docs.github.com/en/actions/reference/security/secure-use).

## 2026-10-04 — Step 3D soak requirement wording clarification

- **Change:** Inspected the original user-provided v0.3.0 bake-off archive after recording the runner-host assessment. Corrected decision and readiness wording from “continuous 24-hour soak” to the pack's actual “24h mixed load” requirement and preserved its same Linux x86-64 runner condition. The pack does not explicitly require a single uninterrupted GitHub Actions job; splitting jobs is only acceptable if it preserves the same controlled host and workload state and remains within the pack's authority.
- **Evidence:** `spec/METRICS.md` in `macau-energy-os-stack-bakeoff-v0.3.0.zip` states “Soak | 24h mixed load”; `README.md` step 6 requires runtime/load/chaos/24h soak on the same Linux x86-64 runner.
- **Status:** Documentation clarification only; no Step 3D execution or architecture decision.

## 2026-10-04 — v0.5 UI/UX Pro Max follow-up

- **Change:** Re-reviewed the v0.5 synthetic interaction prototype using UI/UX Pro Max. The repeated design-system result (operations landing page + conditional Glassmorphism) was rejected as a poor match for a signed-in analytical workspace. Recorded source-level text-contrast samples, the 2.80:1 amber chart-threshold line for next-iteration correction/review under WCAG 2.2 SC 1.4.11, and narrow-screen seven-item horizontal navigation as a discoverability/render-validation concern. Synced the product/architecture readiness audit and CURRENT.
- **Status:** Static source and color calculation only. No browser/device, zoom, keyboard, assistive-technology, user-session or WCAG conformance validation; no final visual direction or frontend framework approved.
- **References:** docs/02-product/PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md follow-up section; W3C WCAG 2.2 Understanding SC 1.4.11: https://www.w3.org/WAI/WCAG22/understanding/non-text-contrast.html.


## 2026-10-04 — v0.6 responsive navigation and chart-threshold follow-up

- **Change:** Added the preserved v0.6 synthetic prototype. At narrow widths, a native selector exposes all nine workspace views, including tariff-evidence and integration/site-access subviews; its value follows view and URL-hash navigation. Darkened the dashed chart-threshold stroke and legend swatch to `#875300` (source calculation: approximately 6.43:1 against white). Updated the product index, review packet, roadmap and readiness audit.
- **Status:** Static source review only. No rendered viewport/zoom inspection, keyboard traversal, assistive-technology review, participant session or WCAG conformance claim. No product or production technology decision is implied.
- **Next:** Render and inspect supported viewport sizes and keyboard/focus behavior; then use authorized WP-4 formative sessions to validate task discoverability and comprehension. Keep product direction and architecture pending owner review and required research/bake-off evidence.


## 2026-10-04 — Step 3D host preflight recheck

- **Change:** Rechecked the task host after the latest design review. Node 22.20.0 is the PATH default; Node 24.9.0 is installed separately but does not meet the proposed 24.21.0 pin. Bun, Go, Docker and Docker Compose are absent; the machine is Windows 10 AMD64 and has no installed WSL Linux distribution.
- **Status:** The local task host cannot run Step 3D's pinned Linux x86-64 common-service environment. No software was installed and no application/runtime experiment was run. A clean isolated Linux runner and explicit security/ownership choice remain necessary.

## 2026-10-04 — Limited local browser render check for v0.6

- **Change:** Opened the exact v0.6 HTML through a local preview in the Codex in-app browser after direct access to the raw GitHub URL was blocked by the browser. Accessibility-tree output showed the compact selector in one browser context, desktop navigation in a second, and the `#tariffs` deep link opening the matching tariff view and breadcrumb.
- **Status:** Limited rendered DOM/accessibility-tree evidence only. Exact viewport pixel sizes and screenshot-level visual layout were not captured. No 200% zoom, keyboard traversal, screen-reader, participant or WCAG evaluation is claimed; the planned responsive/accessibility review remains incomplete.

## 2026-10-04 — WP-4 usability protocol aligned with v0.6

- **Change:** Updated the formative usability protocol to use the current synthetic v0.6 prototype. Added a no-coaching, phone-sized task to find tariff and integration/access subviews and return with browser history; defined task-specific success and observation measures for selector discoverability and state synchronization.
- **Status:** Research preparation only. No participant recruitment, user contact or session is authorized or claimed. The mobile selector remains a design hypothesis until rendered review and authorized formative sessions.
- **Next:** Render the prototype at relevant widths and inspect keyboard/focus behavior, then conduct WP-4 only after participant access is authorized.


## 2026-10-04 — Owner decision queue reconciliation

- **Change:** Restored owner decision #12 for durable telemetry-capture receipt semantics in the owner decision summary, matching the existing architecture review packet, task packet and CURRENT handoff. Corrected spelling in the CURRENT heading and readiness-audit title.
- **Status:** Decision #12 is a review proposal, not owner approval. It defines the logical distinction among protocol ACK, recoverable raw-capture receipt and downstream processing; database, broker, schema and production architecture remain undecided.


## 2026-10-04 — D-003 evidence qualification

- **Change:** Added an evidence qualification to D-003 in the Decision Register: HVAC/chiller remains the first-priority design/discovery hypothesis while G2 is OPEN, not a validated dispatchable asset, approved control target or savings claim. Reaffirmation or supersession requires named-site evidence and owner/site review.
- **Status:** The original priority is preserved; no controllability or pilot selection is asserted.


## 2026-10-04 — Macau data-protection and cross-border-flow review

- **Change:** Added an official-source research note on Law 8/2005 and GPDP guidance, registered the evidence, and added U-027 for project dataset/flow classification and case-specific privacy/legal review. Updated the owner review item, master index and CURRENT handoff.
- **Status:** Research only. No dataset was classified, provider region selected, legal advice obtained, transfer authorized or deployment decision made. Customer-data intake/external AI processing remains dependent on actual-flow review.
- **Evidence:** `docs/01-research/evidence/MACAU-PERSONAL-DATA-AND-CROSS-BORDER-FLOW-REVIEW-2026-10.md`; official sources are linked within that note.


## 2026-10-04 — Node 22/24 lifecycle clarification

- **Change:** Rechecked the official Node.js release schedule and Temporal TypeScript SDK support. Clarified that Node 22.16.0 is the historical Step 3C pin; Node 22 remains Maintenance LTS through 2027-04-30; Node 24 is the v0.3.0 Step 3D candidate line and is Active LTS as of this review, with 24.21.0 pinned for repeatability. Node 26 remains Current as of this review and is not substituted into the pack.
- **Status:** The exact Node 24 pin is a Step 3D experiment requirement only, not a production-runtime decision. Recheck compatible patches/support status at runner freeze; a major-line change requires authority update and comparable rerun.
- **References:** Node.js release schedule https://nodejs.org/en/about/previous-releases and https://github.com/nodejs/Release#release-schedule; Node 22.23.3 https://nodejs.org/en/blog/release/v22.23.3; Node 24.21.0 https://nodejs.org/en/blog/release/v24.21.0; Temporal SDK support https://github.com/temporalio/sdk-typescript.


## 2026-10-04 — G2 customer-group classification boundary

- **Change:** Updated CURRENT and owner decision #2 after reviewing the DSEC Q3 2025 statistical note. Electricity users are classified by use declared when applying for supply; the reviewed sources do not provide a one-to-one crosswalk between DSEC Establishments and CEM Commercial. Hotel counts therefore cannot be used to infer a share of CEM commercial-customer sales.
- **Status:** Aggregate sources remain valid for context only. No target segment or first pilot site is selected; G2 remains open pending site-level measurement.
- **Evidence:** `docs/01-research/evidence/G2-MACAU-COMMERCIAL-LOAD-FLEXIBILITY-EVIDENCE-2026-10.md`.


## 2026-10-04 — G3 site evidence acquisition preparation

- **Change:** Added a site-neutral evidence acquisition packet covering scope/permission, electrical topology/meters, assets and source points, authorized telemetry samples, settlement references, site constraints, optional PV/ESS/EV evidence, restricted evidence manifests, and mapping/review outputs. Linked it from G3, the master index, CURRENT, roadmap and owner decision source list.
- **Status:** Prepared, not sent. No pilot site was selected; no contact or data intake occurred or was authorized. U-027 privacy/legal review, secure intake and explicit owner/site permission remain prerequisites. G3 stays OPEN.
- **Boundary:** The packet does not duplicate G1 Golden Bill or G2 flexibility acceptance and does not authorize field control, production schema selection or Gate closure.


## 2026-10-04 — DSEC quarterly Establishments electricity context

- **Change:** Added DSEC Q1/Q2/Q3 2025 Establishments electricity totals (819/1,069/1,200 million kWh) and year-on-year changes (-2.3%/-0.1%/+1.7%) to the G2 evidence note. Recorded the 46.5% Q1-to-Q3 aggregate increase only as an unadjusted comparison; it does not isolate seasonality, weather, business activity, site counts or building load shape. Added Q1/Q2 source links.
- **Status:** Public aggregate context only. DSEC Establishments and DSPA/CEM Commercial have no one-to-one crosswalk in reviewed sources; G2 remains OPEN for site-level flexibility evidence.
- **Related:** G2 evidence note, Evidence Register and CURRENT handoff.


## 2026-10-04 — G2 CEM commercial sales and peak-load update

- **Change:** Added DSPA/CEM 2026 Q1 and Q2 customer-group sales and system-peak evidence to the G2 note. Commercial sales were 828 GWh and 1,059 GWh; maximum system load was 844 MW and 1,130 MW. The sequential changes are explicitly unadjusted; the Q2 source attributes high demand partly to above-average temperatures.
- **Interpretation:** This strengthens current sector/system context only. It does not isolate drivers, provide commercial-building interval profiles, or quantify flexible capacity, response, comfort/service impact or rebound. DSEC Establishments and CEM Commercial remain separate statistical populations; G2 remains OPEN.
- **Evidence:** https://www.dspa.gov.mo/energyfigures/tc/en-chn_q126.pdf ; https://www.dspa.gov.mo/energyfigures/tc/en-chn_q226.pdf


## 2026-10-04 — G1 smart-meter access boundary and U-003 request bundle

- **Change:** Expanded the G1 smart-meter evidence note with CEM's 2024 Sustainability Report: utility-side data retrieval across more than 280,000 meters and customer-substation telemetry pilots over fiber/4G. CEM's public customer-facing history is daily use for the past 30 days.
- **Interpretation:** These sources establish CEM-side AMI/telemetry capability and daily customer summaries, not third-party interval-feed access. U-003 remains UNKNOWN. Added a prepared U-003 request bundle with channel, granularity, latency/backfill, corrections, retention, authorization/security and commercial-term sufficiency criteria.
- **Status:** Prepared only. No inquiry was sent, no customer account data was requested, and no CEM interface/access conclusion was inferred. G1 remains OPEN.
- **Evidence:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`; `docs/01-research/gates/G1-EVIDENCE-ACQUISITION-PACKET-v0.1.md`.


## 2026-10-04 — G1 Pu statutory scope clarification

- **Change:** Clarified that Administrative Regulation 25/2022 defines the maximum periodically measured average active power for Group B (Article 10), applies that rule to Group C through Article 17, and states the corresponding rule for Group D (Article 24); Article 14 adds low-voltage Group B loss-compensation calculations.
- **Status:** Scope clarification only. The numeric demand interval, fixed/block versus rolling semantics, clock/boundary convention, and meter/register configuration remain unresolved. U-001 remains UNKNOWN and G1 remains OPEN; no 15-minute default or Gate closure is introduced.
- **Source:** [Official Chinese text of Administrative Regulation 25/2022](https://bo.dsaj.gov.mo/bo/i/2022/26/regadm25_cn.asp).

## 2026-10-04 — Implementation runtime labels clarified

- **Change:** Audited the executable implementation tree against current G6.9-R2 authority. The module READMEs described Node/NestJS, Go and Python as runtime directions, which could be mistaken for approved production choices. Clarified their candidate status and bounded current implementation maturity; documented that Step 3D is unexecuted and Step 4 is pending.
- **Evidence:** The Platform API is partial Candidate B implementation evidence with a missing route authorization guard, fail-closed graph/tariff adapters and in-memory evidence storage. The Edge entrypoint only logs bootstrap status; a telemetry event struct exists but protocol ingestion/durable capture is absent. The Python optimizer module currently contains a recommendation data model, not a validated forecast/optimizer. Static source inspection only.
- **Status:** Documentation correction only; no runtime code, contract, technology decision, Gate, or production authority changed. No application tests or runtime experiments were run. PR #8 remains open/unmerged.
- **Related records:** `implementation/README.md`, `implementation/platform-api/README.md`, `implementation/edge-runtime/README.md`, `implementation/optimizer/README.md`, and G6.9 technology authority.

## 2026-10-04 — Frontend and API/BFF candidate boundary clarified

- **Change:** Reviewed the 64 changed Markdown/JSON/YAML files in PR #8 for Next.js, Java/Spring and candidate-stack authority. The changed-file set contains no statement selecting Next.js; D-030 is marked superseded in implementation by D-069; React + TypeScript remains a separate, unapproved browser-UI proposal.
- **Finding:** The G6.9-R2 pack's C+ “product BFF/UI” wording and whether browser rendering is included in Step 3D remain an owner decision. This is not resolved by the candidate-stack scan.
- **Update:** Added this boundary to the lifecycle readiness audit and CURRENT handoff. No technology choice, research Gate or production authority changed.
- **Validation:** Exact-head repository checks are pending for the updated docs; this was a documentation-only change, not an application test or bake-off.
- **Related:** docs/00-authority/PRODUCT-ARCHITECTURE-IMPLEMENTATION-READINESS-AUDIT-v0.1.md, docs/00-authority/handoff/CURRENT.md, docs/03-architecture/ARCHITECTURE-DESIGN.md, and owner Step 3D browser-UI-scope decision.

## 2026-10-04 — End-to-end product/architecture delivery goal charter

- **Change:** Added `docs/00-authority/PRODUCT-ARCHITECTURE-DELIVERY-GOAL-v0.1.md` to define the full lifecycle objective, completion evidence, owner decision boundaries, stage exits, and next dependency-ready sequence. Linked it from the Master Index, roadmap and CURRENT handoff.
- **Status:** Proposed charter on PR #8; owner confirmation remains pending. It does not approve product scope, close a research Gate, select a production stack, authorize implementation beyond existing approved scope, or authorize deployment/control.
- **Current-state basis:** Existing roadmap, lifecycle readiness audit, owner decision packet, detailed-design drafts, vertical-slice plan and handoff were inspected. They establish substantial planning/design drafts, while product approval, user validation, G6.9-R2 Step 3D/4, implementation completion and authorized Macau pilot evidence remain outstanding.
- **Next:** Obtain the owner's product-promise decision; continue independent evidence and research work; then follow the charter's product → architecture → detailed design → implementation → pilot completion criteria.

## 2026-10-04 — Product hypothesis work boundary clarified

- **Change:** Refined the delivery-goal charter sequence so PRD and user-flow drafts continue evolving under explicit research hypotheses while owner approval remains the gate for baselining scope and dependent implementation. This avoids treating owner approval as a prerequisite for useful draft research, while preserving the no-silence-as-approval rule.
- **Status:** Documentation clarification on PR #8; no product choice, user validation or production architecture is approved.

## 2026-10-04 — CURRENT handoff aligned with hypothesis-driven design

- **Change:** Updated the CURRENT next-work statement to review existing detailed-design drafts against the current evidence-backed product hypothesis while retaining open choices, and to require owner approval before product baseline and production implementation. This aligns the live handoff with the delivery-goal charter.
- **Status:** Documentation clarification on PR #8; no product direction or technology decision was approved.

## 2026-10-04 — G2 quarterly data release watch

- **Change:** Rechecked official Macau quarterly energy sources. DSPA currently lists Q2 2026 as the latest Energy and Services report; DSEC's official calendar schedules Q3 2026 Energy Statistics for 2026-11-20. Added a release-watch checkpoint to the G2 evidence note and CURRENT.
- **Status:** Public aggregate context only; G2 remains OPEN. No Q3 2026 use data, site load shape or flexibility inference is claimed.
- **Next:** Recheck official releases after 2026-11-20 and update the G2 evidence note if published.
- **Sources:** https://www.dspa.gov.mo/richtext.aspx?a_id=1598253482; https://www.dsec.gov.mo/TimeTables.aspx?lang=en-US

## 2026-10-04 — U-001 public-source recheck

- **Change:** Re-opened current CEM B/C tariff pages, the CEM B leaflet, CEM smart-meter page and Administrative Regulation 25/2022. Added a live-source recheck to the G1 billing/demand evidence note.
- **Finding:** CEM continues to describe Pu as the maximum measured demand in the billing period; the regulation defines the maximum periodically measured average active power. No numeric measurement window, block/rolling method, meter register configuration or clock-boundary rule was found. Public AMI material still does not specify a third-party raw interval interface.
- **Status:** U-001 and U-003 remain OPEN. Do not hard-code 15 minutes; seek CEM register configuration or matched bill + interval/load-profile evidence. No Gate closed and no product/technology decision changed.
- **Source note:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`.


## 2026-10-04 — CEM tariff and TCA public-source snapshot

- **Change:** Added a dated evidence note recording CEM's public A/B/C/D tariff listings and quarterly TCA values, and linked the note from the Evidence Register, Master Index and CURRENT handoff. The Tariff & Settlement detailed design now treats base schedule and quarterly TCA as separate effective-dated inputs.
- **Finding:** CEM's page lists 2026 Q3 TCA as MOP 0.36/kWh effective 2026-07-22. The A-group illustrative example's 0.340 is stale example data, not the current Q3 TCA.
- **Status:** Public-source snapshot only. G1 remains OPEN; customer-specific applicability, Pu interval, B/C/D monthly installation-use formula, real Golden Bills and invoice arithmetic remain unresolved. C2 tariff-table cell attribution requires rendered/controlled-source verification. No bill-grade claim, customer savings claim or Gate closure is implied.
- **Sources:** CEM tariff-group and TCA pages; Administrative Regulation 25/2022; Executive Decree 105/2022. See the evidence note for direct links and limits.
- **Validation boundary:** Documentation-only update. Exact-head repository workflows must be checked; no application test, customer-data intake or runtime tariff implementation was performed.


## 2026-10-04 — Official C1/C2 schedule clarification

- **Change:** Rechecked the C-group merged-cell ambiguity against Article 7(1)–(3) of Executive Decree 105/2022 in the Official Gazette. The tariff order explicitly sets separate C1/C2 demand parameters and a shared C1/C2 seasonal energy-period schedule. Corrected the dated G1 rate snapshot and linked the clarification from the G1 Gate and Evidence Register.
- **Status:** Public tariff schedule interpretation is strengthened. C2 loss adjustments and customer-specific tariff applicability still require account contract and bill evidence. U-001/U-009/U-010/U-011 remain open; G1 remains OPEN. No bill-grade result, customer savings claim or Gate closure is implied.
- **Source:** https://bo.dsaj.gov.mo/bo/i/2022/26/despce_cn.asp?printer=1 (Article 7); CEM C-group page linked in the snapshot.
- **Validation boundary:** Documentation-only update; exact-head governance checks are required. No application tests or tariff runtime implementation were performed.


## 2026-10-04 — Lifecycle goal confirmed for continued execution

- **Change:** Updated the goal charter from a proposed/confirmation-pending draft to an active lifecycle goal after the owner explicitly instructed that work continue using Goal mode and asked that the eventual architecture be brought back for owner confirmation. Updated CURRENT and Master Index accordingly.
- **Confirmed scope:** Complete and validate the product design, evidence-backed technical architecture and detailed designs, verified MVP implementation, authorized Macau pilot, measured outcomes and operational handoff.
- **Decision boundary:** This confirmation activates the lifecycle objective and its tracking criteria. It does not approve product scope, PRD baseline, visual/UI direction, any production framework/database/service choice, G6.9 winner, controlled operation, or site deployment. Those remain separate evidence-backed owner decisions.
- **Status:** Goal active; project Gate and delivery completion criteria remain unchanged. PR #8 remains open/unmerged.

## 2026-10-04 — UI/UX Pro Max fit audit

- **Change:** Added a focused Pro Max fit audit to the owner review packet. A rerun for a commercial energy analytics workspace returned a marketing “Operations Landing” pattern and generic glassmorphism styling; the packet now marks these as poor-fit search suggestions for an authenticated operational workspace, not as design direction.
- **Design-review probes:** Added four WP-4 observation checks for freshness/provenance, cost-result semantics and supporting evidence, actual-versus-forecast/chart alternatives, and comprehension of SHADOW review versus execution and replay versus measured outcome.
- **Accessibility criteria:** Clarified WCAG 2.2 AA reflow at 320 CSS px and minimum target size at 24×24 CSS px subject to exceptions; 44×44 CSS px is the enhanced AAA criterion. Linked the normative W3C sources.
- **Status:** Documentation update only. Visual directions, product navigation, product scope, and frontend framework remain unapproved. The probes are not participant findings; no WP-4 user session or WCAG conformance test was performed.

## 2026-10-04 — Product design review refocused on workflow architecture

- **Finding:** The owner packet's A/B/C directions compared light, dark and translucent styling but did not compare how users navigate and complete the product's core work. Prototype v0.6 is an exploratory mixed flow, not an equal comparison of workspace organization.
- **Change:** Replaced the visual-style-first recommendation with three IA/workflow hypotheses: evidence-first workbench, exception-led site workspace, and guided assessment workflow. Reframed visual styling as an independent, later design-system decision. Withdrew the prior light-first/A recommendation because no user or site evidence supports it.
- **Decision readiness:** Updated owner decision #3 to request selection of an IA direction to validate, or a request for further evidence. WP-4 observation probes remain the proposed evaluation basis.
- **Status:** Design hypotheses only; no direction, visual system, product scope or frontend framework is approved. No participant study or accessibility-conformance review was performed.

## 2026-10-04 — Workspace organization comparison prototype v0.7

- **Change:** Added prototype v0.7 with three unapproved organizations of the same synthetic demand-evidence task: evidence-first workbench, exception-led site workspace and guided assessment. Content and styling are held constant to foreground information architecture. Local controls switch variants; native details disclosures expose the same synthetic evidence requirements.
- **Research protocol:** Added an optional comparative IA method to the WP-4 plan: assign a focal version for unaided task performance, balance variants across participants and role/site context where feasible, rotate optional comparison order, and distinguish observed performance from stated preference. The existing 5–8-person formative target is not sufficient by itself to rank all three options across user/site groups.
- **Links:** Product README, owner review packet, owner decision summary, Master Index, Roadmap and CURRENT handoff updated.
- **Status:** Synthetic design study only. No rendering/accessibility evaluation, participant recruitment/session, customer data, product decision or user finding is claimed. Product and visual direction remain open for owner review.

## 2026-10-04 — v0.7 source contrast review

- **Change:** Added a limited source-color calculation to the product review packet and CURRENT handoff: body text/canvas 14.29:1; muted text/canvas 5.85:1; amber status text/background 7.40:1; selected-mode text/background 11.38:1; focus outline/canvas 5.00:1.
- **Boundary:** Selected source pairs only. They do not establish rendered contrast in every state, non-text contrast, focus appearance conformance, responsive behavior, zoom, forced-colors behavior, screen-reader support or WCAG conformance.
- **Review limitation:** The available in-app browser rejected the local-file preview URL under its URL security policy. No alternate route was used. v0.7 remains without browser-rendered review or user evaluation.

## 2026-10-04 — Logical Edge diagram made stack-neutral

- **Finding:** The opening logical architecture diagram named a “Go Edge” runtime even though the authority table and status clearly keep Go as an unapproved responsibility proposal.
- **Change:** Renamed the diagram boundary to “Site Edge Energy Runtime + Safety Kernel”. The later technology table continues to identify Go as a proposal and preserves the unresolved site/hardware/security decisions.
- **Status:** Documentation consistency correction only; no production technology decision or implementation authority changed.

## 2026-10-04 — Provisional AI and Edge responsibility labels clarified

- **Change:** The logical architecture technology-authority table now describes Python AI/optimization responsibilities and Go Site Edge responsibilities as provisional proposals, and lists workload/deployment/hardware validation still open.
- **Boundary:** The provisional candidate map remains: React + TypeScript UI proposal; TypeScript/Go cloud-core responsibility candidates under G6.9-R2; Temporal and NATS candidates; PostgreSQL + Timescale evaluation baseline; Python AI proposal; Go Edge proposal; Wasm/WASI future option. No item becomes approved by the diagram/table or by this documentation update. Java/Spring and Next.js remain unselected as previously recorded.

## 2026-10-04 — Identity/tenant design mapped to product workflows

- **Finding:** Identity design already specified server-derived action grants, default-deny scope propagation and tenant-isolation checks, but its candidate role mapping did not connect the PRD/IA's organization administrator, finance cross-site access, delegated integrator configuration, recommendation annotation, replay and service-ingestion workflows to explicit scope/evidence questions.
- **Change:** Added a workflow-to-authorization review map to the VS-001 identity design, distinguishing stable enforcement invariants from role-grant decisions. Added verification scenarios for membership administration versus site-data access, partner expiry/revocation and replay's persisted scope. Expanded PR-01 gap traceability.
- **Owner review:** Added decision #14 for role-to-action/site-entitlement policy and linked the identity detailed design. Exact role grants, identity provider, cross-site finance policy, partner delegation, separation of duties and customer deployment context remain unapproved.
- **Status:** Design and traceability only. No authorization roles/grants, customer identities, production identity implementation or security verification are claimed.

## 2026-10-04 — Authorization acceptance evidence synchronized

- **Change:** Propagated the VS-002 workflow-to-authorization review cases into the Security Threat Model SHADOW-MVP verification scenarios and the VS-002 acceptance statement.
- **Covered cases:** Site-data access is not implied by membership administration; partner grants are scoped, attributable, expiring and revocable; replay references remain within the persisted authorized scope. Explicit multi-site grants may be supported after owner/site policy validation.
- **Status:** Acceptance design only. No executable authorization tests, role grants, identity integration, customer access or G6-09 closure are claimed.

## 2026-10-04 — Chinese owner review brief

- **Change:** Added `docs/02-product/OWNER-REVIEW-BRIEF-zh-CN-v0.1.md`, a Chinese-language review entrypoint summarizing the 14 open product, UX, architecture, security and Step 3D decisions, the provisional stack boundaries, and the full research-to-pilot sequence.
- **Status:** Translation/decision aid only; it does not approve a decision or replace the linked English authorities. Silence remains non-approval.

## 2026-10-04 — Canonical contract authority added to Owner decision queue

- **Finding:** The architecture review packet already compared OpenAPI 3.1, JSON Schema 2020-12 and Protobuf and required a pinned TypeScript/Go evidence slice, but the Owner decision summary did not list the eventual canonical contract authoring/versioning/code-generation policy as a separate decision.
- **Change:** Added Owner decision #15 and synchronized the Chinese review brief/current handoff. The decision is explicitly deferred until domain semantics and candidate boundaries are ready; the evidence gate covers cross-runtime generation/validation, evolution, money/time rules, HTTP/event representations, semantic replay identity, errors and toolchain/supply-chain cost.
- **Status:** No format/toolchain selected. Evidence plan only; production contract V2 and code generation remain unapproved.


## Owner decision dependency sequence — 2026-10-04

- **Change:** The English Owner Decision Summary and Chinese owner brief now group the 15 open decisions by the earliest safe decision point and their evidence prerequisites. This distinguishes decisions available for directional review now, Step 3D runner-only choices, pre-customer-data governance/authorization, connector-dependent telemetry semantics, post-domain contract tooling, site-specific PV/asset claims, and later security verification.
- **Status:** Prioritization aid only. No decision was approved, no Gate was closed, and production architecture remains subject to Owner review and evidence.


## G1 concession-fee classification lead — 2026-10-04

- **Change:** Rechecked official CEM and Gazette sources for U-009. Added a bounded note and evidence-register entry on the 2007 concession-contract Article 36 distinction between periodic tariffs for subscribed capacity/energy and fees for concessionaire services, alongside the 2025 extension/amendment effective 2026-01-01 and CEM's current “Taxa de Exploração” description.
- **Finding:** This is a concrete review lead only. It does not establish that the current B/C/D monthly installation-use charge is the contract-defined service fee or reveal its legal basis/formula. U-009 remains UNKNOWN and excluded from bill-grade totals; G1 remains OPEN.
- **Evidence:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`, `docs/01-research/evidence/EVIDENCE-REGISTER.md`, and `docs/00-authority/handoff/CURRENT.md`. Official sources are linked in the evidence note.


## WP-4 readiness pointer aligned with v0.7 protocol — 2026-10-04

- **Change:** Corrected the lifecycle readiness audit's immediate WP-4 instruction, which only named v0.6 after the v0.7 three-way information-architecture protocol had been added. The audit now directs the study owner to select core workflow tasks and/or the comparative IA protocol based on the research question, preserve task parity/counterbalancing, separate observed performance from stated preference, and avoid an unsupported winner claim from a small formative sample.
- **Status:** Preparation guidance only. No recruitment, contact, participant session, product approval or usability finding is claimed or authorized.


## Owner review runtime note — 2026-10-04

- **Change:** Synchronized the English and Chinese Owner review summaries with the Step 3D runtime evidence: Node 22.16.0 is historical Step 3C only; Node 24.21.0 is the v0.3.0 Step 3D test pin for TypeScript candidates/Temporal worker, subject to recheck at runner freeze. The note also clarifies that Next.js is not in the current G6.9-R2 candidate set or evaluated as a backend framework; evaluating it would require an authority update and comparable evidence.
- **Status:** Test-runtime clarification only. No production Node version, Next.js usage or production architecture is approved.


## Next.js backend-candidate scope added to Owner review — 2026-10-04

- **Change:** Added Owner decision #16 in the English and Chinese review summaries and linked it from the logical architecture and CURRENT handoff. The question is whether to add Next.js as a fourth backend/API candidate, replace Candidate B's NestJS/Fastify path, or explicitly defer it while retaining the current A/B/C+ pack. It requires an equivalent workload and explicit boundary for browser rendering, worker behavior, live streaming and deployment.
- **Evidence:** Official Next.js docs support server-side Route Handlers and a backend-for-frontend/API-layer pattern while cautioning that this is not a full backend replacement. See https://nextjs.org/docs/app/guides/backend-for-frontend and https://nextjs.org/docs/app/getting-started/route-handlers.
- **Status:** No choice recorded. Next.js is neither selected nor rejected. The Step 3D pack is unchanged; any inclusion/replacement requires owner decision and an authority/pack amendment before runner freeze.


## Next.js Step 3D feasibility evidence — 2026-10-04

- **Change:** Added an official-documentation-based fit assessment for Owner decision #16 to the Step 3D readiness plan and bilingual owner summaries; added the unresolved scope choice to the runner manifest's freeze blockers.
- **Evidence:** Next.js Route Handlers support an API/BFF role; Next.js 16 requires Node 20.9+, which is below the proposed Node 24.21.0 test pin; self-hosted Node/Docker supports streaming, subject to end-to-end proxy/load-balancer streaming behavior. Serverless constraints are host-dependent. Next.js documentation cautions that its API layer is not a full backend replacement.
- **Status:** Plausible backend/API candidate for controlled evaluation only. No Step 3D pack amendment, candidate inclusion, production decision, or performance evidence exists. A fourth candidate would raise the current 120 controlled AI trial count to 160 if the same per-candidate matrix is retained. Owner decision #16 remains open.

# Handoff History

Append-only record of material changes to the cross-conversation handoff. This file starts on 2026-10-04; it does not reconstruct earlier chat history. Verify each entry against the linked repository state.

## 2026-10-04 — Continuity entry points and task-packet references

- **Change:** Audited AI research/coding continuity files on the open PR #8 branch. The canonical task-packet template is `docs/04-engineering/ai-coding-governance/TASK-PACKET-TEMPLATE.md`. The handoff README's previous reading order named a missing `HISTORY.md` and treated root-level `decisions/`, `evidence/`, and `research-gates/` as handoff subdirectories; these paths are corrected in this update.
- **Status:** Documentation correction on `docs/product-architecture-roadmap`; PR #8 remains open/unmerged. No product, architecture, Gate, or technology decision is made.
- **Validation boundary:** Documentation authority/hygiene checks will be reported against the exact resulting PR head. This entry does not claim application validation or Gate completion.
- **Related records:** `docs/00-authority/handoff/README.md`, `CONTINUATION-PROTOCOL.md`, `CONTINUE-PROMPT.md`, `CURRENT.md`, and `docs/04-engineering/ai-coding-governance/TASK-PACKET-TEMPLATE.md`.


## 2026-10-04 — G1 evidence acquisition plan

- **Change:** Added a prepared evidence acquisition packet for U-001/U-009/U-010/U-011, including demand-register fields, charge-basis/formula fields, matched Golden Bill requirements, privacy-safe handling and evidence sufficiency criteria. Linked it from the G1 Gate, Gate index, Master Index and CURRENT.
- **Status:** Plan only. No request was sent, no customer data was received, no G1 unknown was resolved, and no Gate was closed. Customer/CEM contact requires owner authorization and an approved secure intake path.
- **Validation:** The packet's source commit `36f3038b7d4330c7b3fd45b41d57208b017efdd3` passed Repository Hygiene and Authority Structure checks. The history-only update is subject to exact-head checks.
- **Related records:** `docs/01-research/gates/G1-EVIDENCE-ACQUISITION-PACKET-v0.1.md`, `docs/01-research/gates/G1-tariff-settlement.md`, `docs/00-authority/handoff/CURRENT.md`, and `docs/00-authority/MASTER_INDEX.md`.

## 2026-10-04 — Telemetry durability task packet

- **Change:** Added `docs/04-engineering/ai-coding-governance/task-packets/ARCH-INGEST-RELIABILITY-001.md` as the active packet for durable telemetry receipt/publication design, owner decision #12, PR-02/VS-003 acceptance, and future runtime proof. Linked it from CURRENT.
- **Status:** Review draft on PR #8; no owner decision, connector protocol, persistence/outbox mechanism, Gate closure, or runtime verification is implied.
- **Validation boundary:** Exact-head repository governance checks are required for the commit containing this entry; prior documentation checks do not validate application behavior.
- **Next:** Review decision #12; inventory authorized connector protocol/identity behavior; then create the implementation packet only after connector, data-governance, contract, and runtime authority are settled.

## 2026-10-04 — Telemetry protocol acknowledgement boundary

- **Change:** Reviewed OASIS MQTT 5.0 QoS acknowledgements and RFC 9110 HTTP 202 semantics. Synchronized the telemetry architecture, PR-02 traceability, VS-003 acceptance, implementation readiness audit, task packet and CURRENT handoff to distinguish protocol/broker acknowledgement from an application-level durable-capture receipt. A broker ACK counts as RAW_DURABLE only if that broker is explicitly the authoritative raw store and persistence/failover/recovery are verified.
- **Evidence:** `docs/03-architecture/detailed-design/TELEMETRY-INGESTION-AND-DATA-QUALITY-DETAILED-DESIGN-v0.1.md` §9 and references. This is a logical design correction; connector mapping, runtime behavior and Gate closure remain unverified.

## 2026-10-04 — Step 3D runner hosting constraints

- **Change:** Reviewed official GitHub Actions limits, runner specifications and security guidance. Added execution-host and public-repository trust-boundary requirements to the Step 3D readiness plan and machine-readable runner blockers; added owner review item #13 and synchronized the product/architecture review packet and CURRENT handoff.
- **Evidence:** GitHub-hosted jobs have a six-hour execution cap, below the bake-off's continuous 24-hour soak. Self-hosted jobs allow up to five days and require Linux + Docker for container services, but GitHub warns that public-repository PR code can compromise persistent self-hosted runners. A clean, isolated, fixed-resource execution host with a reviewed/trusted dispatch boundary is therefore still required.
- **Status:** Research and documentation only. No runner was provisioned, no Step 3D experiment was executed, and no production architecture was selected.
- **References:** [Actions limits](https://docs.github.com/en/actions/reference/limits); [hosted runner specifications](https://docs.github.com/en/actions/reference/runners/github-hosted-runners); [self-hosted runner requirements](https://docs.github.com/en/actions/reference/runners/self-hosted-runners); [secure use](https://docs.github.com/en/actions/reference/security/secure-use).

## 2026-10-04 — Step 3D soak requirement wording clarification

- **Change:** Inspected the original user-provided v0.3.0 bake-off archive after recording the runner-host assessment. Corrected decision and readiness wording from “continuous 24-hour soak” to the pack's actual “24h mixed load” requirement and preserved its same Linux x86-64 runner condition. The pack does not explicitly require a single uninterrupted GitHub Actions job; splitting jobs is only acceptable if it preserves the same controlled host and workload state and remains within the pack's authority.
- **Evidence:** `spec/METRICS.md` in `macau-energy-os-stack-bakeoff-v0.3.0.zip` states “Soak | 24h mixed load”; `README.md` step 6 requires runtime/load/chaos/24h soak on the same Linux x86-64 runner.
- **Status:** Documentation clarification only; no Step 3D execution or architecture decision.

## 2026-10-04 — v0.5 UI/UX Pro Max follow-up

- **Change:** Re-reviewed the v0.5 synthetic interaction prototype using UI/UX Pro Max. The repeated design-system result (operations landing page + conditional Glassmorphism) was rejected as a poor match for a signed-in analytical workspace. Recorded source-level text-contrast samples, the 2.80:1 amber chart-threshold line for next-iteration correction/review under WCAG 2.2 SC 1.4.11, and narrow-screen seven-item horizontal navigation as a discoverability/render-validation concern. Synced the product/architecture readiness audit and CURRENT.
- **Status:** Static source and color calculation only. No browser/device, zoom, keyboard, assistive-technology, user-session or WCAG conformance validation; no final visual direction or frontend framework approved.
- **References:** docs/02-product/PRODUCT-AND-ARCHITECTURE-REVIEW-PACKET-v0.1.md follow-up section; W3C WCAG 2.2 Understanding SC 1.4.11: https://www.w3.org/WAI/WCAG22/understanding/non-text-contrast.html.


## 2026-10-04 — v0.6 responsive navigation and chart-threshold follow-up

- **Change:** Added the preserved v0.6 synthetic prototype. At narrow widths, a native selector exposes all nine workspace views, including tariff-evidence and integration/site-access subviews; its value follows view and URL-hash navigation. Darkened the dashed chart-threshold stroke and legend swatch to `#875300` (source calculation: approximately 6.43:1 against white). Updated the product index, review packet, roadmap and readiness audit.
- **Status:** Static source review only. No rendered viewport/zoom inspection, keyboard traversal, assistive-technology review, participant session or WCAG conformance claim. No product or production technology decision is implied.
- **Next:** Render and inspect supported viewport sizes and keyboard/focus behavior; then use authorized WP-4 formative sessions to validate task discoverability and comprehension. Keep product direction and architecture pending owner review and required research/bake-off evidence.


## 2026-10-04 — Step 3D host preflight recheck

- **Change:** Rechecked the task host after the latest design review. Node 22.20.0 is the PATH default; Node 24.9.0 is installed separately but does not meet the proposed 24.21.0 pin. Bun, Go, Docker and Docker Compose are absent; the machine is Windows 10 AMD64 and has no installed WSL Linux distribution.
- **Status:** The local task host cannot run Step 3D's pinned Linux x86-64 common-service environment. No software was installed and no application/runtime experiment was run. A clean isolated Linux runner and explicit security/ownership choice remain necessary.

## 2026-10-04 — Limited local browser render check for v0.6

- **Change:** Opened the exact v0.6 HTML through a local preview in the Codex in-app browser after direct access to the raw GitHub URL was blocked by the browser. Accessibility-tree output showed the compact selector in one browser context, desktop navigation in a second, and the `#tariffs` deep link opening the matching tariff view and breadcrumb.
- **Status:** Limited rendered DOM/accessibility-tree evidence only. Exact viewport pixel sizes and screenshot-level visual layout were not captured. No 200% zoom, keyboard traversal, screen-reader, participant or WCAG evaluation is claimed; the planned responsive/accessibility review remains incomplete.

## 2026-10-04 — WP-4 usability protocol aligned with v0.6

- **Change:** Updated the formative usability protocol to use the current synthetic v0.6 prototype. Added a no-coaching, phone-sized task to find tariff and integration/access subviews and return with browser history; defined task-specific success and observation measures for selector discoverability and state synchronization.
- **Status:** Research preparation only. No participant recruitment, user contact or session is authorized or claimed. The mobile selector remains a design hypothesis until rendered review and authorized formative sessions.
- **Next:** Render the prototype at relevant widths and inspect keyboard/focus behavior, then conduct WP-4 only after participant access is authorized.


## 2026-10-04 — Owner decision queue reconciliation

- **Change:** Restored owner decision #12 for durable telemetry-capture receipt semantics in the owner decision summary, matching the existing architecture review packet, task packet and CURRENT handoff. Corrected spelling in the CURRENT heading and readiness-audit title.
- **Status:** Decision #12 is a review proposal, not owner approval. It defines the logical distinction among protocol ACK, recoverable raw-capture receipt and downstream processing; database, broker, schema and production architecture remain undecided.


## 2026-10-04 — D-003 evidence qualification

- **Change:** Added an evidence qualification to D-003 in the Decision Register: HVAC/chiller remains the first-priority design/discovery hypothesis while G2 is OPEN, not a validated dispatchable asset, approved control target or savings claim. Reaffirmation or supersession requires named-site evidence and owner/site review.
- **Status:** The original priority is preserved; no controllability or pilot selection is asserted.


## 2026-10-04 — Macau data-protection and cross-border-flow review

- **Change:** Added an official-source research note on Law 8/2005 and GPDP guidance, registered the evidence, and added U-027 for project dataset/flow classification and case-specific privacy/legal review. Updated the owner review item, master index and CURRENT handoff.
- **Status:** Research only. No dataset was classified, provider region selected, legal advice obtained, transfer authorized or deployment decision made. Customer-data intake/external AI processing remains dependent on actual-flow review.
- **Evidence:** `docs/01-research/evidence/MACAU-PERSONAL-DATA-AND-CROSS-BORDER-FLOW-REVIEW-2026-10.md`; official sources are linked within that note.


## 2026-10-04 — Node 22/24 lifecycle clarification

- **Change:** Rechecked the official Node.js release schedule and Temporal TypeScript SDK support. Clarified that Node 22.16.0 is the historical Step 3C pin; Node 22 remains Maintenance LTS through 2027-04-30; Node 24 is the v0.3.0 Step 3D candidate line and is Active LTS as of this review, with 24.21.0 pinned for repeatability. Node 26 remains Current as of this review and is not substituted into the pack.
- **Status:** The exact Node 24 pin is a Step 3D experiment requirement only, not a production-runtime decision. Recheck compatible patches/support status at runner freeze; a major-line change requires authority update and comparable rerun.
- **References:** Node.js release schedule https://nodejs.org/en/about/previous-releases and https://github.com/nodejs/Release#release-schedule; Node 22.23.3 https://nodejs.org/en/blog/release/v22.23.3; Node 24.21.0 https://nodejs.org/en/blog/release/v24.21.0; Temporal SDK support https://github.com/temporalio/sdk-typescript.


## 2026-10-04 — G2 customer-group classification boundary

- **Change:** Updated CURRENT and owner decision #2 after reviewing the DSEC Q3 2025 statistical note. Electricity users are classified by use declared when applying for supply; the reviewed sources do not provide a one-to-one crosswalk between DSEC Establishments and CEM Commercial. Hotel counts therefore cannot be used to infer a share of CEM commercial-customer sales.
- **Status:** Aggregate sources remain valid for context only. No target segment or first pilot site is selected; G2 remains open pending site-level measurement.
- **Evidence:** `docs/01-research/evidence/G2-MACAU-COMMERCIAL-LOAD-FLEXIBILITY-EVIDENCE-2026-10.md`.


## 2026-10-04 — G3 site evidence acquisition preparation

- **Change:** Added a site-neutral evidence acquisition packet covering scope/permission, electrical topology/meters, assets and source points, authorized telemetry samples, settlement references, site constraints, optional PV/ESS/EV evidence, restricted evidence manifests, and mapping/review outputs. Linked it from G3, the master index, CURRENT, roadmap and owner decision source list.
- **Status:** Prepared, not sent. No pilot site was selected; no contact or data intake occurred or was authorized. U-027 privacy/legal review, secure intake and explicit owner/site permission remain prerequisites. G3 stays OPEN.
- **Boundary:** The packet does not duplicate G1 Golden Bill or G2 flexibility acceptance and does not authorize field control, production schema selection or Gate closure.


## 2026-10-04 — DSEC quarterly Establishments electricity context

- **Change:** Added DSEC Q1/Q2/Q3 2025 Establishments electricity totals (819/1,069/1,200 million kWh) and year-on-year changes (-2.3%/-0.1%/+1.7%) to the G2 evidence note. Recorded the 46.5% Q1-to-Q3 aggregate increase only as an unadjusted comparison; it does not isolate seasonality, weather, business activity, site counts or building load shape. Added Q1/Q2 source links.
- **Status:** Public aggregate context only. DSEC Establishments and DSPA/CEM Commercial have no one-to-one crosswalk in reviewed sources; G2 remains OPEN for site-level flexibility evidence.
- **Related:** G2 evidence note, Evidence Register and CURRENT handoff.


## 2026-10-04 — G2 CEM commercial sales and peak-load update

- **Change:** Added DSPA/CEM 2026 Q1 and Q2 customer-group sales and system-peak evidence to the G2 note. Commercial sales were 828 GWh and 1,059 GWh; maximum system load was 844 MW and 1,130 MW. The sequential changes are explicitly unadjusted; the Q2 source attributes high demand partly to above-average temperatures.
- **Interpretation:** This strengthens current sector/system context only. It does not isolate drivers, provide commercial-building interval profiles, or quantify flexible capacity, response, comfort/service impact or rebound. DSEC Establishments and CEM Commercial remain separate statistical populations; G2 remains OPEN.
- **Evidence:** https://www.dspa.gov.mo/energyfigures/tc/en-chn_q126.pdf ; https://www.dspa.gov.mo/energyfigures/tc/en-chn_q226.pdf


## 2026-10-04 — G1 smart-meter access boundary and U-003 request bundle

- **Change:** Expanded the G1 smart-meter evidence note with CEM's 2024 Sustainability Report: utility-side data retrieval across more than 280,000 meters and customer-substation telemetry pilots over fiber/4G. CEM's public customer-facing history is daily use for the past 30 days.
- **Interpretation:** These sources establish CEM-side AMI/telemetry capability and daily customer summaries, not third-party interval-feed access. U-003 remains UNKNOWN. Added a prepared U-003 request bundle with channel, granularity, latency/backfill, corrections, retention, authorization/security and commercial-term sufficiency criteria.
- **Status:** Prepared only. No inquiry was sent, no customer account data was requested, and no CEM interface/access conclusion was inferred. G1 remains OPEN.
- **Evidence:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`; `docs/01-research/gates/G1-EVIDENCE-ACQUISITION-PACKET-v0.1.md`.


## 2026-10-04 — G1 Pu statutory scope clarification

- **Change:** Clarified that Administrative Regulation 25/2022 defines the maximum periodically measured average active power for Group B (Article 10), applies that rule to Group C through Article 17, and states the corresponding rule for Group D (Article 24); Article 14 adds low-voltage Group B loss-compensation calculations.
- **Status:** Scope clarification only. The numeric demand interval, fixed/block versus rolling semantics, clock/boundary convention, and meter/register configuration remain unresolved. U-001 remains UNKNOWN and G1 remains OPEN; no 15-minute default or Gate closure is introduced.
- **Source:** [Official Chinese text of Administrative Regulation 25/2022](https://bo.dsaj.gov.mo/bo/i/2022/26/regadm25_cn.asp).

## 2026-10-04 — Implementation runtime labels clarified

- **Change:** Audited the executable implementation tree against current G6.9-R2 authority. The module READMEs described Node/NestJS, Go and Python as runtime directions, which could be mistaken for approved production choices. Clarified their candidate status and bounded current implementation maturity; documented that Step 3D is unexecuted and Step 4 is pending.
- **Evidence:** The Platform API is partial Candidate B implementation evidence with a missing route authorization guard, fail-closed graph/tariff adapters and in-memory evidence storage. The Edge entrypoint only logs bootstrap status; a telemetry event struct exists but protocol ingestion/durable capture is absent. The Python optimizer module currently contains a recommendation data model, not a validated forecast/optimizer. Static source inspection only.
- **Status:** Documentation correction only; no runtime code, contract, technology decision, Gate, or production authority changed. No application tests or runtime experiments were run. PR #8 remains open/unmerged.
- **Related records:** `implementation/README.md`, `implementation/platform-api/README.md`, `implementation/edge-runtime/README.md`, `implementation/optimizer/README.md`, and G6.9 technology authority.

## 2026-10-04 — Frontend and API/BFF candidate boundary clarified

- **Change:** Reviewed the 64 changed Markdown/JSON/YAML files in PR #8 for Next.js, Java/Spring and candidate-stack authority. The changed-file set contains no statement selecting Next.js; D-030 is marked superseded in implementation by D-069; React + TypeScript remains a separate, unapproved browser-UI proposal.
- **Finding:** The G6.9-R2 pack's C+ “product BFF/UI” wording and whether browser rendering is included in Step 3D remain an owner decision. This is not resolved by the candidate-stack scan.
- **Update:** Added this boundary to the lifecycle readiness audit and CURRENT handoff. No technology choice, research Gate or production authority changed.
- **Validation:** Exact-head repository checks are pending for the updated docs; this was a documentation-only change, not an application test or bake-off.
- **Related:** docs/00-authority/PRODUCT-ARCHITECTURE-IMPLEMENTATION-READINESS-AUDIT-v0.1.md, docs/00-authority/handoff/CURRENT.md, docs/03-architecture/ARCHITECTURE-DESIGN.md, and owner Step 3D browser-UI-scope decision.

## 2026-10-04 — End-to-end product/architecture delivery goal charter

- **Change:** Added `docs/00-authority/PRODUCT-ARCHITECTURE-DELIVERY-GOAL-v0.1.md` to define the full lifecycle objective, completion evidence, owner decision boundaries, stage exits, and next dependency-ready sequence. Linked it from the Master Index, roadmap and CURRENT handoff.
- **Status:** Proposed charter on PR #8; owner confirmation remains pending. It does not approve product scope, close a research Gate, select a production stack, authorize implementation beyond existing approved scope, or authorize deployment/control.
- **Current-state basis:** Existing roadmap, lifecycle readiness audit, owner decision packet, detailed-design drafts, vertical-slice plan and handoff were inspected. They establish substantial planning/design drafts, while product approval, user validation, G6.9-R2 Step 3D/4, implementation completion and authorized Macau pilot evidence remain outstanding.
- **Next:** Obtain the owner's product-promise decision; continue independent evidence and research work; then follow the charter's product → architecture → detailed design → implementation → pilot completion criteria.

## 2026-10-04 — Product hypothesis work boundary clarified

- **Change:** Refined the delivery-goal charter sequence so PRD and user-flow drafts continue evolving under explicit research hypotheses while owner approval remains the gate for baselining scope and dependent implementation. This avoids treating owner approval as a prerequisite for useful draft research, while preserving the no-silence-as-approval rule.
- **Status:** Documentation clarification on PR #8; no product choice, user validation or production architecture is approved.

## 2026-10-04 — CURRENT handoff aligned with hypothesis-driven design

- **Change:** Updated the CURRENT next-work statement to review existing detailed-design drafts against the current evidence-backed product hypothesis while retaining open choices, and to require owner approval before product baseline and production implementation. This aligns the live handoff with the delivery-goal charter.
- **Status:** Documentation clarification on PR #8; no product direction or technology decision was approved.

## 2026-10-04 — G2 quarterly data release watch

- **Change:** Rechecked official Macau quarterly energy sources. DSPA currently lists Q2 2026 as the latest Energy and Services report; DSEC's official calendar schedules Q3 2026 Energy Statistics for 2026-11-20. Added a release-watch checkpoint to the G2 evidence note and CURRENT.
- **Status:** Public aggregate context only; G2 remains OPEN. No Q3 2026 use data, site load shape or flexibility inference is claimed.
- **Next:** Recheck official releases after 2026-11-20 and update the G2 evidence note if published.
- **Sources:** https://www.dspa.gov.mo/richtext.aspx?a_id=1598253482; https://www.dsec.gov.mo/TimeTables.aspx?lang=en-US

## 2026-10-04 — U-001 public-source recheck

- **Change:** Re-opened current CEM B/C tariff pages, the CEM B leaflet, CEM smart-meter page and Administrative Regulation 25/2022. Added a live-source recheck to the G1 billing/demand evidence note.
- **Finding:** CEM continues to describe Pu as the maximum measured demand in the billing period; the regulation defines the maximum periodically measured average active power. No numeric measurement window, block/rolling method, meter register configuration or clock-boundary rule was found. Public AMI material still does not specify a third-party raw interval interface.
- **Status:** U-001 and U-003 remain OPEN. Do not hard-code 15 minutes; seek CEM register configuration or matched bill + interval/load-profile evidence. No Gate closed and no product/technology decision changed.
- **Source note:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`.


## 2026-10-04 — CEM tariff and TCA public-source snapshot

- **Change:** Added a dated evidence note recording CEM's public A/B/C/D tariff listings and quarterly TCA values, and linked the note from the Evidence Register, Master Index and CURRENT handoff. The Tariff & Settlement detailed design now treats base schedule and quarterly TCA as separate effective-dated inputs.
- **Finding:** CEM's page lists 2026 Q3 TCA as MOP 0.36/kWh effective 2026-07-22. The A-group illustrative example's 0.340 is stale example data, not the current Q3 TCA.
- **Status:** Public-source snapshot only. G1 remains OPEN; customer-specific applicability, Pu interval, B/C/D monthly installation-use formula, real Golden Bills and invoice arithmetic remain unresolved. C2 tariff-table cell attribution requires rendered/controlled-source verification. No bill-grade claim, customer savings claim or Gate closure is implied.
- **Sources:** CEM tariff-group and TCA pages; Administrative Regulation 25/2022; Executive Decree 105/2022. See the evidence note for direct links and limits.
- **Validation boundary:** Documentation-only update. Exact-head repository workflows must be checked; no application test, customer-data intake or runtime tariff implementation was performed.


## 2026-10-04 — Official C1/C2 schedule clarification

- **Change:** Rechecked the C-group merged-cell ambiguity against Article 7(1)–(3) of Executive Decree 105/2022 in the Official Gazette. The tariff order explicitly sets separate C1/C2 demand parameters and a shared C1/C2 seasonal energy-period schedule. Corrected the dated G1 rate snapshot and linked the clarification from the G1 Gate and Evidence Register.
- **Status:** Public tariff schedule interpretation is strengthened. C2 loss adjustments and customer-specific tariff applicability still require account contract and bill evidence. U-001/U-009/U-010/U-011 remain open; G1 remains OPEN. No bill-grade result, customer savings claim or Gate closure is implied.
- **Source:** https://bo.dsaj.gov.mo/bo/i/2022/26/despce_cn.asp?printer=1 (Article 7); CEM C-group page linked in the snapshot.
- **Validation boundary:** Documentation-only update; exact-head governance checks are required. No application tests or tariff runtime implementation were performed.


## 2026-10-04 — Lifecycle goal confirmed for continued execution

- **Change:** Updated the goal charter from a proposed/confirmation-pending draft to an active lifecycle goal after the owner explicitly instructed that work continue using Goal mode and asked that the eventual architecture be brought back for owner confirmation. Updated CURRENT and Master Index accordingly.
- **Confirmed scope:** Complete and validate the product design, evidence-backed technical architecture and detailed designs, verified MVP implementation, authorized Macau pilot, measured outcomes and operational handoff.
- **Decision boundary:** This confirmation activates the lifecycle objective and its tracking criteria. It does not approve product scope, PRD baseline, visual/UI direction, any production framework/database/service choice, G6.9 winner, controlled operation, or site deployment. Those remain separate evidence-backed owner decisions.
- **Status:** Goal active; project Gate and delivery completion criteria remain unchanged. PR #8 remains open/unmerged.

## 2026-10-04 — UI/UX Pro Max fit audit

- **Change:** Added a focused Pro Max fit audit to the owner review packet. A rerun for a commercial energy analytics workspace returned a marketing “Operations Landing” pattern and generic glassmorphism styling; the packet now marks these as poor-fit search suggestions for an authenticated operational workspace, not as design direction.
- **Design-review probes:** Added four WP-4 observation checks for freshness/provenance, cost-result semantics and supporting evidence, actual-versus-forecast/chart alternatives, and comprehension of SHADOW review versus execution and replay versus measured outcome.
- **Accessibility criteria:** Clarified WCAG 2.2 AA reflow at 320 CSS px and minimum target size at 24×24 CSS px subject to exceptions; 44×44 CSS px is the enhanced AAA criterion. Linked the normative W3C sources.
- **Status:** Documentation update only. Visual directions, product navigation, product scope, and frontend framework remain unapproved. The probes are not participant findings; no WP-4 user session or WCAG conformance test was performed.

## 2026-10-04 — Product design review refocused on workflow architecture

- **Finding:** The owner packet's A/B/C directions compared light, dark and translucent styling but did not compare how users navigate and complete the product's core work. Prototype v0.6 is an exploratory mixed flow, not an equal comparison of workspace organization.
- **Change:** Replaced the visual-style-first recommendation with three IA/workflow hypotheses: evidence-first workbench, exception-led site workspace, and guided assessment workflow. Reframed visual styling as an independent, later design-system decision. Withdrew the prior light-first/A recommendation because no user or site evidence supports it.
- **Decision readiness:** Updated owner decision #3 to request selection of an IA direction to validate, or a request for further evidence. WP-4 observation probes remain the proposed evaluation basis.
- **Status:** Design hypotheses only; no direction, visual system, product scope or frontend framework is approved. No participant study or accessibility-conformance review was performed.

## 2026-10-04 — Workspace organization comparison prototype v0.7

- **Change:** Added prototype v0.7 with three unapproved organizations of the same synthetic demand-evidence task: evidence-first workbench, exception-led site workspace and guided assessment. Content and styling are held constant to foreground information architecture. Local controls switch variants; native details disclosures expose the same synthetic evidence requirements.
- **Research protocol:** Added an optional comparative IA method to the WP-4 plan: assign a focal version for unaided task performance, balance variants across participants and role/site context where feasible, rotate optional comparison order, and distinguish observed performance from stated preference. The existing 5–8-person formative target is not sufficient by itself to rank all three options across user/site groups.
- **Links:** Product README, owner review packet, owner decision summary, Master Index, Roadmap and CURRENT handoff updated.
- **Status:** Synthetic design study only. No rendering/accessibility evaluation, participant recruitment/session, customer data, product decision or user finding is claimed. Product and visual direction remain open for owner review.

## 2026-10-04 — v0.7 source contrast review

- **Change:** Added a limited source-color calculation to the product review packet and CURRENT handoff: body text/canvas 14.29:1; muted text/canvas 5.85:1; amber status text/background 7.40:1; selected-mode text/background 11.38:1; focus outline/canvas 5.00:1.
- **Boundary:** Selected source pairs only. They do not establish rendered contrast in every state, non-text contrast, focus appearance conformance, responsive behavior, zoom, forced-colors behavior, screen-reader support or WCAG conformance.
- **Review limitation:** The available in-app browser rejected the local-file preview URL under its URL security policy. No alternate route was used. v0.7 remains without browser-rendered review or user evaluation.

## 2026-10-04 — Logical Edge diagram made stack-neutral

- **Finding:** The opening logical architecture diagram named a “Go Edge” runtime even though the authority table and status clearly keep Go as an unapproved responsibility proposal.
- **Change:** Renamed the diagram boundary to “Site Edge Energy Runtime + Safety Kernel”. The later technology table continues to identify Go as a proposal and preserves the unresolved site/hardware/security decisions.
- **Status:** Documentation consistency correction only; no production technology decision or implementation authority changed.

## 2026-10-04 — Provisional AI and Edge responsibility labels clarified

- **Change:** The logical architecture technology-authority table now describes Python AI/optimization responsibilities and Go Site Edge responsibilities as provisional proposals, and lists workload/deployment/hardware validation still open.
- **Boundary:** The provisional candidate map remains: React + TypeScript UI proposal; TypeScript/Go cloud-core responsibility candidates under G6.9-R2; Temporal and NATS candidates; PostgreSQL + Timescale evaluation baseline; Python AI proposal; Go Edge proposal; Wasm/WASI future option. No item becomes approved by the diagram/table or by this documentation update. Java/Spring and Next.js remain unselected as previously recorded.

## 2026-10-04 — Identity/tenant design mapped to product workflows

- **Finding:** Identity design already specified server-derived action grants, default-deny scope propagation and tenant-isolation checks, but its candidate role mapping did not connect the PRD/IA's organization administrator, finance cross-site access, delegated integrator configuration, recommendation annotation, replay and service-ingestion workflows to explicit scope/evidence questions.
- **Change:** Added a workflow-to-authorization review map to the VS-001 identity design, distinguishing stable enforcement invariants from role-grant decisions. Added verification scenarios for membership administration versus site-data access, partner expiry/revocation and replay's persisted scope. Expanded PR-01 gap traceability.
- **Owner review:** Added decision #14 for role-to-action/site-entitlement policy and linked the identity detailed design. Exact role grants, identity provider, cross-site finance policy, partner delegation, separation of duties and customer deployment context remain unapproved.
- **Status:** Design and traceability only. No authorization roles/grants, customer identities, production identity implementation or security verification are claimed.

## 2026-10-04 — Authorization acceptance evidence synchronized

- **Change:** Propagated the VS-002 workflow-to-authorization review cases into the Security Threat Model SHADOW-MVP verification scenarios and the VS-002 acceptance statement.
- **Covered cases:** Site-data access is not implied by membership administration; partner grants are scoped, attributable, expiring and revocable; replay references remain within the persisted authorized scope. Explicit multi-site grants may be supported after owner/site policy validation.
- **Status:** Acceptance design only. No executable authorization tests, role grants, identity integration, customer access or G6-09 closure are claimed.

## 2026-10-04 — Chinese owner review brief

- **Change:** Added `docs/02-product/OWNER-REVIEW-BRIEF-zh-CN-v0.1.md`, a Chinese-language review entrypoint summarizing the 14 open product, UX, architecture, security and Step 3D decisions, the provisional stack boundaries, and the full research-to-pilot sequence.
- **Status:** Translation/decision aid only; it does not approve a decision or replace the linked English authorities. Silence remains non-approval.

## 2026-10-04 — Canonical contract authority added to Owner decision queue

- **Finding:** The architecture review packet already compared OpenAPI 3.1, JSON Schema 2020-12 and Protobuf and required a pinned TypeScript/Go evidence slice, but the Owner decision summary did not list the eventual canonical contract authoring/versioning/code-generation policy as a separate decision.
- **Change:** Added Owner decision #15 and synchronized the Chinese review brief/current handoff. The decision is explicitly deferred until domain semantics and candidate boundaries are ready; the evidence gate covers cross-runtime generation/validation, evolution, money/time rules, HTTP/event representations, semantic replay identity, errors and toolchain/supply-chain cost.
- **Status:** No format/toolchain selected. Evidence plan only; production contract V2 and code generation remain unapproved.


## Owner decision dependency sequence — 2026-10-04

- **Change:** The English Owner Decision Summary and Chinese owner brief now group the 15 open decisions by the earliest safe decision point and their evidence prerequisites. This distinguishes decisions available for directional review now, Step 3D runner-only choices, pre-customer-data governance/authorization, connector-dependent telemetry semantics, post-domain contract tooling, site-specific PV/asset claims, and later security verification.
- **Status:** Prioritization aid only. No decision was approved, no Gate was closed, and production architecture remains subject to Owner review and evidence.


## G1 concession-fee classification lead — 2026-10-04

- **Change:** Rechecked official CEM and Gazette sources for U-009. Added a bounded note and evidence-register entry on the 2007 concession-contract Article 36 distinction between periodic tariffs for subscribed capacity/energy and fees for concessionaire services, alongside the 2025 extension/amendment effective 2026-01-01 and CEM's current “Taxa de Exploração” description.
- **Finding:** This is a concrete review lead only. It does not establish that the current B/C/D monthly installation-use charge is the contract-defined service fee or reveal its legal basis/formula. U-009 remains UNKNOWN and excluded from bill-grade totals; G1 remains OPEN.
- **Evidence:** `docs/01-research/evidence/G1-CEM-BILLING-AND-DEMAND-UNKNOWN-REVIEW-2026-10.md`, `docs/01-research/evidence/EVIDENCE-REGISTER.md`, and `docs/00-authority/handoff/CURRENT.md`. Official sources are linked in the evidence note.


## WP-4 readiness pointer aligned with v0.7 protocol — 2026-10-04

- **Change:** Corrected the lifecycle readiness audit's immediate WP-4 instruction, which only named v0.6 after the v0.7 three-way information-architecture protocol had been added. The audit now directs the study owner to select core workflow tasks and/or the comparative IA protocol based on the research question, preserve task parity/counterbalancing, separate observed performance from stated preference, and avoid an unsupported winner claim from a small formative sample.
- **Status:** Preparation guidance only. No recruitment, contact, participant session, product approval or usability finding is claimed or authorized.


## Owner review runtime note — 2026-10-04

- **Change:** Synchronized the English and Chinese Owner review summaries with the Step 3D runtime evidence: Node 22.16.0 is historical Step 3C only; Node 24.21.0 is the v0.3.0 Step 3D test pin for TypeScript candidates/Temporal worker, subject to recheck at runner freeze. The note also clarifies that Next.js is not in the current G6.9-R2 candidate set or evaluated as a backend framework; evaluating it would require an authority update and comparable evidence.
- **Status:** Test-runtime clarification only. No production Node version, Next.js usage or production architecture is approved.


## Next.js backend-candidate scope added to Owner review — 2026-10-04

- **Change:** Added Owner decision #16 in the English and Chinese review summaries and linked it from the logical architecture and CURRENT handoff. The question is whether to add Next.js as a fourth backend/API candidate, replace Candidate B's NestJS/Fastify path, or explicitly defer it while retaining the current A/B/C+ pack. It requires an equivalent workload and explicit boundary for browser rendering, worker behavior, live streaming and deployment.
- **Evidence:** Official Next.js docs support server-side Route Handlers and a backend-for-frontend/API-layer pattern while cautioning that this is not a full backend replacement. See https://nextjs.org/docs/app/guides/backend-for-frontend and https://nextjs.org/docs/app/getting-started/route-handlers.
- **Status:** No choice recorded. Next.js is neither selected nor rejected. The Step 3D pack is unchanged; any inclusion/replacement requires owner decision and an authority/pack amendment before runner freeze.


## Next.js Step 3D feasibility evidence — 2026-10-04

- **Change:** Added an official-documentation-based fit assessment for Owner decision #16 to the Step 3D readiness plan and bilingual owner summaries; added the unresolved scope choice to the runner manifest's freeze blockers.
- **Evidence:** Next.js Route Handlers support an API/BFF role; Next.js 16 requires Node 20.9+, which is below the proposed Node 24.21.0 test pin; self-hosted Node/Docker supports streaming, subject to end-to-end proxy/load-balancer streaming behavior. Serverless constraints are host-dependent. Next.js documentation cautions that its API layer is not a full backend replacement.
- **Status:** Plausible backend/API candidate for controlled evaluation only. No Step 3D pack amendment, candidate inclusion, production decision, or performance evidence exists. A fourth candidate would raise the current 120 controlled AI trial count to 160 if the same per-candidate matrix is retained. Owner decision #16 remains open.


## v0.7 product UX heuristic review — 2026-10-04

- **Change:** Added a source-level UI/UX Pro Max heuristic audit of the v0.7 three-way workspace-organization prototype to the product/architecture review packet and synchronized a Chinese summary and CURRENT handoff.
- **Evidence:** Native named/pressed mode buttons, focus-visible styling, polite mode hint, native evidence disclosures, hidden inactive workspaces, textual blocked/missing states, and 44px minimum mode controls are present in source. At narrow widths the three-option selector uses horizontal scrolling; viewport/keyboard behavior remains to be rendered and reviewed. One synthetic case is used; chart/table/form/loading/action patterns are outside this prototype's scope.
- **Status:** Source-level review only. No code/design direction or A/B/C information architecture was approved; no user, assistive-technology, rendered viewport, WCAG-conformance or production framework validation is claimed.

## v0.7 rendering defect / v0.8 correction — 2026-10-04

- **Finding:** A local browser rendering of v0.7 showed all three workspace variants at once. The CSS author rule `.workspace{display:grid}` overrode the browser's native hidden-state display rule. Variant selection changed the selected button and explanatory hint but did not isolate the content. This invalidated v0.7 as a fair A/B/C comparison stimulus.
- **Change:** Preserved v0.7 and created v0.8 with explicit `.workspace[hidden]{display:none}` and a wrapping narrow-screen variant selector. Updated product README, WP-4 protocol, review packet, Chinese owner brief and CURRENT to identify v0.8 as current and v0.7 as historical/unsuitable for comparative sessions.
- **Evidence:** In one local browser context, initial load exposed only A; clicking B/C and keyboard Shift+Tab/Space changed the accessibility tree to only the selected workspace. A narrow-view screenshot showed all three selector controls wrapped without partial horizontal clipping. Exact CSS viewport size was not captured.
- **Status:** Prototype correction and bounded browser observation only. No A/B/C winner, user validation, complete keyboard/screen-reader review, localization review, WCAG conformance, product/visual/framework approval or architecture decision is claimed.


## v0.8 narrow overflow / v0.9 responsive correction — 2026-10-04

- **Finding:** At 320 CSS px, v0.8's `body{min-width:320px}` exceeded the 305px client width after the vertical scrollbar, creating page-level horizontal overflow even though the selector wrapped.
- **Change:** Preserved v0.8 and created v0.9 without a body minimum width. Updated product README, WP-4 stimulus/version, owner review packet, Chinese owner brief and CURRENT.
- **Evidence:** At 320/375/768/1024/1440 CSS px, document scroll width equaled client width, selector scroll width equaled its client width, and only the selected workspace was visible. Screenshots were inspected at 320 and 1440.
- **Status:** Bounded local browser observation. 200% zoom remains unverified; no full keyboard, screen-reader, localization or user validation is claimed. v0.9 is not an approved IA/product design and A/B/C remain unselected.

## PRD-to-delivery traceability consolidation — 2026-10-04

- **Change:** Added a consolidated PR-01–PR-09 map linking proposed user flows/screens, numbered WP-4 probes, detailed-design authority, candidate delivery slices and current validation evidence. Synchronized the readiness audit and CURRENT handoff.
- **Finding:** The prior architecture matrix linked designs and runtime gaps, while product IA and MVP plan separately linked screens/flows and slices. Joining these references exposed the status of the evidence edge: every WP-4 item remains a planned probe, not a participant finding; v0.9 covers only one synthetic demand-evidence case.
- **Status:** Traceability artifact is more complete; user/site evidence, Owner approval, Gate evidence, production architecture and implementation remain incomplete. No readiness claim was upgraded.


## v0.6 core-workflow overflow / v0.10 navigation review — 2026-10-04

- **Finding:** v0.6 had a 320px body minimum width; with the vertical scrollbar, the available client width was 305px and the page overflowed horizontally.
- **Change:** Preserved v0.6, created v0.10 with the minimum width removed, and made v0.10 the current core-flow study stimulus. v0.9 remains the IA comparison stimulus. Updated README, WP-4 plan, IA status, review packet, readiness audit, PRD traceability, owner summaries, roadmap and CURRENT.
- **Evidence:** At 320/375/768/1024/1440 CSS px, page scroll width matched client width. All nine destination options displayed their matching view and URL; Browser Back restored Recommendations after Evidence & replay; mobile ArrowUp+Enter selected Recommendations and moved focus to its heading. Wide table scrolling was contained inside its labeled wrapper.
- **Status:** Bounded local browser observation. No target-user, screen-reader, 200% zoom, localization or WCAG-conformance evidence; product IA, scope, visual system and frontend framework remain unapproved.

## Step 3D execution-host and runner-lifecycle review (2026-10-04)

- Rechecked GitHub's official Actions limits, self-hosted-runner reference, secure-use guidance and GITHUB_TOKEN lifecycle. Standard hosted jobs have a six-hour cap; self-hosted jobs may run five days, but GITHUB_TOKEN refresh is limited to 24 hours. GitHub recommends ephemeral self-hosted runners and external retention of runner logs; its security guidance warns against using self-hosted runners with public repositories because untrusted pull-request code can compromise the host.
- Expanded the Step 3D readiness plan with a comparison of hosted runners, persistent self-hosted runners, one-job JIT runners and a detached disposable Linux VM. The recommendation for owner review is a disposable owner-controlled Linux x86-64 VM for one controlled run, preserving the same host across the 24-hour soak without exposing credentials/network access to PR code.
- Synchronized CURRENT and ROADMAP. This is test-host guidance only; owner approval of cost, operator, network policy, pins and evidence retention is still required. No runner was provisioned and Step 3D was not run; no production deployment or technology decision is implied.
- Sources: https://docs.github.com/en/actions/reference/limits ; https://docs.github.com/en/actions/reference/runners/self-hosted-runners ; https://docs.github.com/en/actions/reference/security/secure-use ; https://docs.github.com/en/actions/concepts/security/github_token

## PR-01/PR-08 candidate authorization matrix (2026-10-04)

- Added a proposed role-to-action/site-entitlement matrix to the stack-neutral VS-001 identity design so owner, customer and security reviewers can evaluate concrete candidate bundles for energy/facilities, site operations, finance, integration partners, access administrators, ingestion identities and platform workloads.
- The matrix explicitly treats every proposed grant as unapproved and default-deny; it separates site entitlement from organization membership, telemetry summaries from raw data, reads from export, mapping proposal from approval, and customer identity from workload identity. No device-execution grant exists for the SHADOW MVP. Possible second-person review for settlement-impacting changes is a question, not an adopted policy.
- Reconciled the design with NIST SP 800-162 ABAC concepts and OWASP ASVS 5.0 V8 authorization verification prompts (V8.1.1, V8.2.1–V8.2.2, V8.3.1, V8.4.1). These are design references, not compliance claims.
- Updated owner decision #14, PRD-to-architecture traceability, CURRENT and ROADMAP. Role mapping, site scope, approval separation, identity provider, implementation and cross-tenant runtime evidence remain open; no customer data access is authorized.

## Logical persistence and schema-evolution design (2026-10-04)

- Opened task packet ARCH-PERSISTENCE-BOUNDARY-001 and added DATA-PERSISTENCE-AND-SCHEMA-EVOLUTION-DETAILED-DESIGN-v0.1.md, a stack-neutral logical design spanning tenant/access state, graph and settlement facts, raw/normalized telemetry, analyses/replay, recommendation/review evidence and publication/workflow state.
- The design states durability/acknowledgement and cross-store failure boundaries, bitemporal/versioned lineage, tenant scope, append-only correction semantics, retention/privacy and backup/restore questions, plus an additive expand–migrate–contract and rollback policy.
- Linked the design from the logical architecture, architecture README, Master Index, PRD-to-architecture traceability and VS-003/VS-005 acceptance plan. Updated CURRENT and ROADMAP; physical stores, database, migrations, retention/deletion, RPO/RTO and owner decisions remain open.
- This is an architecture review draft only. No schema or application code was changed; no database, migration, application test, backup/restore drill, customer-data access or Gate closure is claimed.

## Logical MVP application and event contract catalog (2026-10-04)

- Opened task packet ARCH-APP-CONTRACT-CATALOG-001 and added MVP-APPLICATION-AND-EVENT-CONTRACT-CATALOG-v0.1.md to map product tasks across PR-01…PR-09 to logical operations, capability owners, authorization scope, status/durability semantics, event boundaries and vertical-slice evidence.
- The catalog separates accepted requests, durable capture, publication, consumer completion, economic eligibility, SHADOW recommendation/review and replay outcomes. It preserves D-065 as the contract authority and does not choose endpoint paths, API protocol, wire format, schema generator or runtime.
- Linked it from the architecture README, Master Index, implementation contract README, PRD-to-architecture traceability, MVP slice plan, roadmap, CURRENT and PR #8.
- Owner decisions #8/#12/#14, wire-contract and event-identity decisions, G1/G3/G6/G6.9-R2 evidence and runtime implementation remain open. No application schema/code was changed and no application tests or external integrations were run.


## AI coding governance adoption model (2026-10-04)

- Added AI-CODING-GOVERNANCE-ADOPTION-PLAN-v0.1.md and task packet ENG-AI-CODING-GOVERNANCE-ADOPTION-001.md to turn the existing proposed AI Coding Quality Baseline into a staged, risk-based operating model for a long-lived commercial product.
- Linked governance adoption to the lifecycle goal's completion evidence, governance README, quality baseline, roadmap and CURRENT handoff. The plan distinguishes written policy from repository controls actually enforced and preserves the requirement for owner adoption.
- References Google Engineering Practices, DORA CI/test automation, Google SRE production readiness/release engineering, NIST SP 800-218 SSDF 1.1 and OWASP ASVS 5.0. These guide adaptation; no compliance/certification claim is made.
- Production stack, stack-specific toolchain, branch/reviewer enforcement, SLOs, and release/rollback authority remain open. No application code or tests, repository permissions, branch protections, customer-data workflow or production release were changed.


## AI coding governance templates (2026-10-04)

- Strengthened the reusable .github/PULL_REQUEST_TEMPLATE.md and TASK-PACKET-TEMPLATE.md to require accountable human ownership/review, risk tier and rationale, governing authority, exact-revision validation evidence, skipped-check reasons, security/privacy/tenant/safety impacts, compatibility, operations and recovery considerations.
- Linked the PR template from the AI coding governance README and reflected its role and limits in the adoption plan, governance task packet and CURRENT handoff.
- These templates improve change context but are not repository-enforced gates. main remains unprotected, required status checks are disabled, and no repository rulesets exist. No permissions or branch settings changed; no application behavior or application tests were involved.


## PR-triggered CI scope clarification (2026-10-04)

- Clarification to the governance-template entry above: although this documentation change did not edit application or test files and no local application tests were initiated, the PR's configured GitHub Actions automatically ran the existing Runtime Bootstrap workflow because the PR also changes that workflow.
- At exact head 3cc910ae57daee0873d36f8466afee78a03cf7f0, the seven named checks passed: authority structure, repository hygiene, JSON contract syntax, platform API, Edge Runtime, Optimizer and Contract Fixtures. Runtime checks exercise the current scaffold and fixtures; they do not validate the new logical application/event design or establish production readiness.
- The latest exact PR-head validation is maintained in PR #8; future commits trigger another run. No application code or test files were changed by this governance update.


## Recommendation demo feedback clarity — prototype v0.11 (2026-10-04)

- UI/UX Pro Max targeted searches and a source/browser review found v0.10's phrase “saved locally” overstated an in-memory DOM state change: no storage, persistence API or server request exists for the demo review dispositions.
- Preserved v0.10 and created v0.11. The status now says the change is displayed only on the page, resets on reload, and is neither persisted nor a measured outcome/command. Product README, WP-4 session protocol, visual-design evaluation, CURRENT and ROADMAP now identify v0.11 as the current nine-destination study stimulus.
- Source checks also found 44px minimum action buttons, visibly disabled controls, text-bearing status badges and the existing polite live-status region. A fresh browser tree showed the initial items unreviewed and controls enabled; an already open browser page showed the resulting in-memory reviewed state.
- No refresh, full keyboard/screen-reader, contrast, localization, user or WCAG-conformance session was performed. No product meaning, launch language, palette, framework or persistent production review behavior is approved.


## G1 U-025 PV contract and settlement evidence bundle (2026-10-04)

- Extended the prepared G1 evidence packet with bundle E for current PV application/interconnection/feed-in contracts, third-party host ownership and self-consumption, any remote allocation/PPA/wheeling/bill-credit arrangement, and a separate GEC offer/retirement path.
- Defined claim-level sufficiency: written current authority/contract terms plus named party, parcel, approval, metering and settlement behavior; an actual customer-credit claim additionally needs authorized matched meter/settlement evidence. A public feed-in tariff, PPA label, GEC purchase or SAR public-generation offset alone does not establish remote CEM bill credit.
- Linked the bundle from G1, U-025 resolution path, CURRENT and Master Index. The packet is not sent; no CEM/customer contact, customer data intake or Gate closure occurred. G1/U-025 remain open.


## PV settlement boundary cross-design review (2026-10-04)

- Cross-reviewed the G1 PV evidence/U-025 against Energy Graph, Tariff & Settlement, Cost Analysis/Evidence Replay, VS-001 result semantics, PRD traceability and VS-004/VS-006. All reviewed drafts keep physical PV/grid flow, producer feed-in settlement, consumer import billing and any approved site-economic aggregation distinct; no contradiction was found.
- Rechecked official DSPA/CEM public counts: DSPA reports 12 systems connected and selling by 2026-08-31; CEM reports 12 connected systems, 4,193 kWp and >6 million kWh as of January 2026. Same count, different cutoffs/status terms; no matched capacity or generation time series is established.
- Recorded limits and open U-025/U-026 status in the readiness audit and CURRENT. Static review only; no site/contract/runtime evidence, user research or Gate closure. U-025 bundle E remains prepared and unsent; owner authorization and secure intake are required.


## Operability and tenant-authorization cross-design review (2026-10-04)

- Cross-reviewed Deployment/Operability/Recovery §§3–9, Security Threat Model §§1–6C and VS-001 Identity/Tenant Authorization §§4–8. Tenant scope, degraded-state, recovery, release and G6 boundaries agree across the drafts.
- Found that the deployment design required sensitive-evidence access logging while the identity draft did not explicitly cover successful sensitive reads or export/support/restore/break-glass paths. Updated identity §6 to require auditable events for data classified as sensitive and those privileged paths; exact read classes remain tied to data classification, and retention/access policy remains open.
- No runtime tests or recovery drills were performed. User/security/operations decisions, actual authorization/restore evidence and G6 closure remain outstanding.


## Cost-result and request-state cross-design review (2026-10-04)

- Cross-reviewed Cost Analysis/Evidence Replay, the CostResult/ReplayManifest proposal, application/event status catalog, recommendation design and D-026.
- Reconciled inconsistent draft vocabulary: economic-result status is COMPLETE/PARTIAL/BLOCKED when a result exists; FAILED belongs to request lifecycle and yields no CostResult/amount; assumption-led scenarios use PROJECT_ASSUMPTION evidence and SCENARIO_ONLY readiness rather than an overloaded result status.
- Kept the contract proposal noncanonical. Product monetary meaning, decimal/rounding rules, G1 evidence, replay identity and D-065 owner review remain open. Static document review only; no application tests or generated bindings were run, and no Gate was closed.

## G4/G5 economic handoff and tariff status mapping (2026-10-04)

- Cross-reviewed G4/G5 Gates, Forecasting/Optimization, Tariff & Settlement, Cost Analysis/Evidence Replay, CostResult/ReplayManifest, the application status catalog and relevant decisions.
- Clarified that Tariff context/component states (including UNKNOWN/CONFLICT), economic result status (COMPLETE/PARTIAL/BLOCKED), evidence basis (including PROJECT_ASSUMPTION), settlement readiness (BILL_GRADE_ELIGIBLE/SCENARIO_ONLY), failed request lifecycle and incomplete replay outcome are separate dimensions. Updated Tariff §§4/7 and cross-references from Forecasting, CostResult and the application catalog.
- Exact bill-grade status still depends on G1/Golden Bill evidence; G4/G5/G6/G7 remain open. No runtime tests, simulator run, Macau-site validation, production implementation or Gate closure is claimed.

## G3 Energy Graph and telemetry identity/status cross-review (2026-10-04)

- Cross-reviewed the Energy Graph design, Telemetry Ingestion/Data Quality, logical application/event catalog, persistence boundary and prepared G3 site evidence packet.
- Corrected the graph request lineage to use the durable raw-capture record ID for an accepted telemetry record; an authenticated producer/source event ID remains optional and separate. The capture ID must not imply duplicate source publications are the same event.
- Split graph mapping validity from telemetry freshness: a known mapping with no applicable revision returns `EXPIRED_MAPPING` (no prior mapping remains `UNMAPPED`); telemetry freshness/coverage/clock quality is a separate quality dimension. Aligned APP-04 and the evidence packet machine vocabulary.
- Updated the readiness audit and CURRENT. Static design review only: no runtime tests, site evidence, source identity guarantees or Gate closure. G3 remains OPEN.
- AI coding governance is already present as a proposed stack-neutral quality baseline and adoption plan with Google Engineering Practices, DORA, Google SRE, OWASP ASVS and NIST SSDF references. Owner adoption and actual enforcement remain separate work; stack-specific rules wait for architecture approval.

## G3 task-packet traceability update (2026-10-04)

- Added the graph/telemetry identity and status cross-review to ARCH-INGEST-RELIABILITY-001 and recorded APP-04 vocabulary alignment in ARCH-APP-CONTRACT-CATALOG-001.
- Both packets remain Review pending owner decision #12, connector-specific receipt semantics, D-065 contract authority and architecture approval. No source identity, runtime behavior or site evidence was validated.
- This closes the documentation traceability loop for the static G3 review; it does not pass G3 or establish production readiness.

## PRD-to-slice G3 state alignment review (2026-10-04)

- Cross-reviewed PR-02/PR-03, Flow A, S-03/S-04, the PRD-to-architecture matrix and VS-003/VS-004 against the G3 Energy Graph/Telemetry design.
- Found product/acceptance language still referred to a “stale mapping” after architecture semantics had split mapping validity from measurement freshness. Updated the PRD, user flows, traceability matrix, vertical-slice acceptance plan, readiness audit and CURRENT handoff.
- The product now describes `EXPIRED_MAPPING` separately from stale/invalid telemetry. This improves design-to-acceptance consistency; no target-user comprehension, Macau site behavior, runtime, or Gate evidence is claimed.

## Nine-PRD requirement closure audit (2026-10-04)

- Re-read PR-01–PR-09 against the current PRD, user flows/screens, PRD-to-architecture traceability, vertical-slice plan, implementation-status evidence and current prototype record.
- Added a requirement-by-requirement closure table to the readiness audit. All nine remain partial/unaccepted: product requirements and logical designs are substantial, but customer validation, domain Gates, canonical/approved contracts, runtime implementation and acceptance evidence are incomplete by requirement.
- Corrected traceability rows to identify prototype v0.11 as the current core-flow stimulus (v0.10 predecessor); v0.9 remains the separate IA comparison. Updated CURRENT.
- QLR-01 localization remains a proposed cross-cutting requirement; launch locales and terminology are not selected or user-validated.
- This is a bounded document/source audit, not a full source-code/runtime audit, user study or Gate decision. No requirement is called complete and the lifecycle goal remains active.

## Owner review packet prototype-status correction (2026-10-04)

- Reconciled the front section of the Product and Architecture Review Packet with its later prototype history and the current handoff.
- Corrected the stale statement that no IA comparison existed and that v0.7 was the usable A/B/C stimulus: v0.7 had a rendered variant-isolation defect, v0.8 overflowed at 320px, v0.9 is the corrected A/B/C comparison stimulus, and v0.11 is the current nine-destination core-flow stimulus (v0.10 predecessor).
- Recorded bounded browser observations and explicitly retained limits: no participant findings, complete accessibility/localization evaluation, IA winner or owner approval.
- Linked the nine-PRD readiness audit from the Owner Decision Summary. No decision was approved by these edits.

## CURRENT handoff deduplication and prototype-state reconciliation (2026-10-04)

- Audited the full branch version of CURRENT.md after finding two duplicate top-level snapshots. Compared the repeated sections before consolidation; retained the newer, more complete first snapshot and its current G3/product/governance updates, and discarded the repeated older snapshot. Distinct append-only update entries after that duplicate are preserved.
- Replaced the stale active-delivery summary that highlighted v0.6/v0.7 with the current product/architecture status: v0.11 is the core-flow stimulus, v0.9 is the A/B/C IA comparison, and v0.7/v0.8 are historical defective stimuli. Updated the WP-4 summary to reflect bounded browser observations and continuing user/accessibility/localization gaps.
- Corrected the Chinese owner-review brief reference from 16 to 17 decisions, including localization item #17. The Owner Decision Summary itself remains a review aid and records no owner approvals.
- The readiness audit still finds PR-01–PR-09 partial/unaccepted. This documentation cleanup changes no product decision, Gate status, implementation or approval boundary.


## Live AI coding governance enforcement recheck (2026-10-04)

- Rechecked the live GitHub branch metadata and rulesets while preparing the proposed governance adoption model: `main` reports `protected: false`; required-status-check enforcement is off with no contexts; repository rulesets are empty.
- PR #8 head `a5b94a7b968990a3fa608a01ef18d98f442bb9e4` had four passing workflows but no submitted reviews or inline review threads. These workflow results are not merge gates.
- The linked integration cannot read the exact protection endpoint (403) and exposes no branch-protection/ruleset write operation. No setting or permission was changed. Requiring GitHub approval needs a second authorized reviewer if the PR author is the sole maintainer; an owner-attestation alternative must not be represented as peer review.
- Updated the adoption plan, task packet and CURRENT with an unactivated stack-neutral proposal and evidence boundary. Owner policy adoption, reviewer model, admin bypass and applying repository rules remain open. No application tests or behavior changes were made.
