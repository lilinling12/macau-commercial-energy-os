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


## 2026-10-04 — Limited local browser render check for v0.6

- **Change:** Opened the exact v0.6 HTML through a local preview in the Codex in-app browser after direct access to the raw GitHub URL was blocked by the browser. Accessibility-tree output showed the compact selector in one browser context, desktop navigation in a second, and the `#tariffs` deep link opening the matching tariff view and breadcrumb.
- **Status:** Limited rendered DOM/accessibility-tree evidence only. Exact viewport pixel sizes and screenshot-level visual layout were not captured. No 200% zoom, keyboard traversal, screen-reader, participant or WCAG evaluation is claimed; the planned responsive/accessibility review remains incomplete.

## 2026-10-04 — WP-4 usability protocol aligned with v0.6

- **Change:** Updated the formative usability protocol to use the current synthetic v0.6 prototype. Added a no-coaching, phone-sized task to find tariff and integration/access subviews and return with browser history; defined task-specific success and observation measures for selector discoverability and state synchronization.
- **Status:** Research preparation only. No participant recruitment, user contact or session is authorized or claimed. The mobile selector remains a design hypothesis until rendered review and authorized formative sessions.
- **Next:** Render the prototype at relevant widths and inspect keyboard/focus behavior, then conduct WP-4 only after participant access is authorized.
