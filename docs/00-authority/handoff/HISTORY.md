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
