# Research Authority Timeline & Gate Reconciliation v0.1

**Review date:** 2026-10-04  
**Status:** evidence timeline draft; based on directly inspected archive status files plus GitHub file/PR checks recorded in this review. The companion archive manifest lists all package names and embedded status excerpts. It is not an owner-approved authority replacement.

## Status vocabulary

- **Verified in artifact:** directly stated in the named file/package; not necessarily independently reproduced.
- **Accepted:** explicitly labeled Accepted in a decision log/ADR.
- **Provisional:** explicitly temporary/default/candidate.
- **Pending:** source names work as next or unresolved.
- **Later consolidation claim:** a later authority marks a broader research gate complete without including the earlier pending experiment output. Preserve both facts until reconciled.
- **Unknown:** artifact/evidence not located or not readable in this audit.

## Authority and research timeline

| Package/version | Verified status in source | Decision/evidence meaning | Reconciliation |
|---|---|---|---|
| Research Authority v1.6.1 (snapshot 2026-10-03) | `handoff/CURRENT.md`: G1 open; G6.9-R2 Step 3A pack and Step 3B protocol conformance complete; full framework/runtime bake-off pending. Candidate C+ is provisional default; A is challenger, B compatibility baseline. | Step 3A provided candidate topology/manifests, 10 controlled AI tasks/120-run protocol, gates and command-security corpus. Step 3B Node/Go shared corpus 22/22 checks; Bun unavailable. The source expressly says there is no measured winner. | Strong evidence that a C+ provisional architecture direction existed, while comparable framework/runtime evidence remained absent. |
| Research Authority v1.6.2 (snapshot 2026-10-03) | `handoff/CURRENT.md`: Step 3A + 3B + Step 3C semantic end-to-end slice complete; pinned framework-native integration pending; G1 open. | Step 3C tested available Node/Go/Python/Go Edge semantics, common telemetry and command behavior. It expressly says this is not a framework/runtime performance result and that Bun/Hono/Effect, Node 24/Nest/Fastify, Temporal, Postgres/Timescale, NATS/MQTT/OTel were not run together. | Step 3C is meaningful semantic/conformance evidence, not the bake-off winner. Its named next task is Step 3D pinned integration environment. |
| Research Authority v1.7.0 | `CURRENT.md`: G6.9 technology research “completed”; pending framework bake-off final evidence and reference implementation decision; next G7 Commercialization Research. | Consolidation release completed architectural research areas (protocol, vertical slice, data/event, deployment, AI workflow, architecture-as-code), while listing final bake-off evidence as pending. | “G6.9 research complete” means consolidation/architecture research was considered complete; it does not prove the Step 3D bake-off ran. |
| Research Authority v1.7.1 | Recovery transition to G7; decision log: Cloud/Edge separation, Edge safety boundary, AI cannot directly command, PostgreSQL baseline accepted. Hybrid TS product plane + Go Energy Kernel + Python Intelligence, Timescale, NATS marked provisional; final cloud-core framework bake-off/Bun scope/event architecture open. Roadmap proceeds G7.2–G7.5. | Captures principled boundary decisions and a provisional hybrid direction, not a final framework winner. | Confirms the Step 3D open status was not simply converted into a final A/B/C measured result in the recovery release. |
| Authority v1.8.0 | `CURRENT.md`/`ROADMAP.md`: G6.9 technology research and G7.1–G7.5 listed complete; G7.6 Step 2 completed; next G7.6 Step 3 vertical slice. Decision log retains accepted principles and provisional TypeScript Platform, Go Edge, Python Intelligence, PostgreSQL and NATS. | Broad gate consolidation and engineering transition. | G6.9 is labeled complete at the research-gate level; no Step 3D result or measured stack winner is included in this package excerpt. Read with v1.7 pending evidence, not as proof the benchmark passed. |
| Authority v1.9.0 | `CURRENT.md`: research/architecture consolidation completed through G7.6 engineering preparation; G7.7 repository foundation next; actual repository “not started.” | Top-level preparation authority, not a code repository. | Historical snapshot predates or describes planned repo creation; current GitHub has since been created and implemented. |
| Authority v2.0 Recovery → Step 2 → Step 3 → Step 4 | Packages mark authority recovery, mapping audit, decision traceability and repository preparation completed; actual repository initialization next. | Process reconstructs authority structure and records broad TypeScript Platform / Go Edge / Python / OpenAPI directions. | Later current repository contains code; v2.0 package is a preparation-stage snapshot, not current repo status. Its generic stack record does not resolve later Nest/Fastify/C+ conflicts. |
| G7.6 Step 3 / Step 5–7 packs | Vertical slice: simulator → Go Edge → Telemetry API → Energy Model → Forecast/Optimizer → Recommendation API → React portal. Optimizer returns a Recommendation, not equipment command. | Defines first bounded application loop and advisory safety line. | Does not by itself prove commercial source/load dispatch flow, tariff applicability, field control, or a validated optimizer. |
| G7.8 Step 2 and Step 3 ADR packs | Step 2 proposes React/TS, TS cloud backend, Go Edge, Python, OpenAPI/JSON Schema. Step 3 ADR records those boundaries and “Start with Fastify-based architecture.” | Strong package-level ADR evidence for a TypeScript cloud framework direction. | Later Node/Nest code and report (7) conflict; no source in this audit shows a dated superseding ADR explaining the change. G6.9 Step 3D was already explicitly pending in v1.6.2. |
| G7.8 Step 4+ / GitHub Phase B | Main contains Node/NestJS API bootstrap, Go Edge, Python optimizer, schemas/CI. | Implementation reality, not an architecture approval by itself. | Needs explicit deviation/ADR mapping to G7.8 Fastify direction and G6.9 candidates. |
| G7.9 Step 1/2 packages | Step 1 MVP domain foundation marked complete; scope excludes direct control, autonomous complex AI and full billing. Step 2 domain/data/contracts marked complete; Step 3 service boundary and implementation design next. | Domain and contract design authority. | PR #8 adds later detailed drafts and main adds bounded code slices, but neither automatically closes Step 3 or validates the source/load scheduling product workflow. |
| Deep Research report (6) | Recommends conditional Candidate C+ (Go core, Bun/Hono thin layer, Temporal Go, Python, PostgreSQL/Timescale, NATS, MQTT; Wasm/WASI later); requires a measured bake-off and says C+ may be overturned. | Research recommendation, not ADR. | Aligned with v1.6–v1.7 provisional C+; does not prove Step 3D. |
| Deep Research report (7), 2026-10-02 | Recommends TypeScript/Node/NestJS modular monolith, Go ingestion/Edge, Python, PostgreSQL/Timescale, MQTT, Kafka target. Next.js only conditionally for SSR/public portal/server-side composition; operator console recommended React SPA. | A later independent recommendation, not an approved change record. | Conflicts with C+ and G7.8 Fastify. It does not make Next.js a backend or final selection. |

## G6.9-R2 actual completion finding

The archive contains detailed G6.9-R2 authority inside Research Authority v1.6.1 and v1.6.2, even though no standalone filename is named G6.9.

- **Step 3A:** bake-off pack/design created; full candidate trial not run.
- **Step 3B:** protocol/Edge conformance marked complete for available runtimes; Node/Go passed the shared corpus; Bun unavailable in that environment.
- **Step 3C:** semantic end-to-end slice marked complete for available runtimes; useful contract/idempotency/replay behavior was tested. This was explicitly not comparative performance or full-stack framework-native execution.
- **Step 3D:** v1.6.2 identifies the pinned Linux framework-native environment and A/B/C+ integrations/fault injection as next. The package contains no Step 3D result. v1.7.0 still lists final bake-off evidence pending; v1.7.1 keeps cloud-core framework bake-off open. Later v1.8/v1.9 call G6.9 technology research complete broadly, but no retrieved source supplies the missing Step 3D comparison result.

**Conclusion:** G6.9 architecture research/consolidation was treated as complete by later authority versions; the exact G6.9-R2 framework-native comparative bake-off is **not evidenced complete** in the inspected archives. Do not report a measured A/B/C+ winner.

## What was not proven in this timeline

- The external `/mnt/data/macau-energy-os-stack-bakeoff/` pack referenced by v1.6.1/1.6.2 was not available as a readable local path in this session; archive packages contain documentation, not the complete executable trial workspace.
- No Step 3D pinned runtime output (framework-native results, worker kill/recovery, broker partition, persistence fault injection or comparison metrics) was found in the inspected v1.6.2 archive.
- This timeline has not yet read every file inside every archive or every shared conversation turn. It is a material authority reconciliation, not a full closure audit.
- Current repo/PR details are summarized from the earlier browser inspection in `CURRENT-STATE-AUDIT-v0.1.md`; current branch contents should be re-read before any repository change.

## Consequence for current decisions

Keep architecture as: **accepted boundaries** (cloud/edge separation, edge safety ownership, AI not direct command; tenant isolation and contract-first design) + **provisional stack direction** (polyglot TS/Go/Python) + **unresolved production implementation choices** (Node/Nest vs Node/Fastify vs Bun/Hono/Go-core; workflow and event infrastructure). A production stack freeze needs the missing benchmark evidence or an explicit owner-approved replacement ADR that explains why the bake-off was waived.

## Conversation-history evidence boundary — 2026-10-04

The referenced shared page `https://chatgpt.com/share/6ac10df8-a30c-83e9-83bd-f8de8ec31ca1` opens with the title “研究澳门用电模式” but, in the current logged-out browser session, the conversation content area exposes no messages and shows a login prompt. The related ChatGPT conversation record `6abf4f5c-b2d4-83ea-b189-6534f517c5a1` is readable through the conversation archive tool, but only four recent turns are returned and the page reports `hasMore=false`; those turns mostly summarize recent Phase B/C repository work. This does not provide the older full research transcript or every assistant output.

Therefore this timeline is based on directly readable Authority/Gate archives, Deep Research reports (6)/(7), current GitHub main and PR pages, and the limited recent conversation record. The original share conversation's full body and any older linked outputs remain **unverified**. Do not report the historical chat as fully reviewed until a readable export or accessible copy is available.


## Addendum — Complete package inventory and Authority v2 conflict (2026-10-04)

A filename/status-file inventory was generated for all **40 Macau Energy OS ZIP packages**, both loose Authority Markdown files, and four explicitly excluded remote-control ZIP packages. See [`ARCHIVE-INVENTORY-v0.1.md`](ARCHIVE-INVENTORY-v0.1.md). This inventory is not equivalent to a semantic review of every archive entry. The current evidence is now classified below; no source is silently discarded.

### Later authority assertions versus GitHub authority

| Source/version | Status recorded in that source | Evidence limit / current treatment |
|---|---|---|
| Authority v1.6.2 | G6.9-R2 Steps 3A–3C complete; pinned Step 3D integration pending; G1 and G7.2 live baseline/no-op open. | Strong, explicit checkpoint for actual experiment scope and next step. |
| Authority v1.7.0/v1.7.1 | Broad architecture/research consolidation is complete; framework bake-off evidence/reference implementation remains pending and cloud framework remains open. | Gate consolidation does not supply Step 3D results or a measured winner. |
| Authority v1.8.0/v1.9.0 | Marks broad G6.9 and several G7 research gates complete, and advances to engineering/repository preparation; v1.9.0 says repository creation is still next. | Later high-level gate assertions, but they do not include a supersession record or the missing Step 3D evidence. The v1.9 repository-preparation status is historical; the GitHub repository now exists. |
| Authority v2.0 recovery and Step 2–4 packages | Marks authority recovery, research mapping, architecture consolidation and repository preparation stages complete; actual repository initialization remains a later item in the package checklist. | These are recovery/preparation deliverables; they do not prove runtime experiments or current GitHub implementation. |
| Loose Authority v2.0 Markdown | G6.9-R2 lists work including 3G.1 complete / 3G.2 next, while technology framework questions remain under evaluation; Step 3D is not listed as completed. | Lettered 3G work does not prove the separate framework-native 3D bake-off. |
| Loose Authority v2.1 Markdown | Says G6.9 Technology Selection / AI Native Engineering is complete and G7.1 is next. | Later closure assertion, but inspected file does not identify Step 3D run artifacts, a measured framework winner, an approver, or an explicit supersession of previous status. |
| GitHub main `docs/00-authority/handoff/CURRENT.md` | G6.9-R2 Step 3D pending; G7.2 live baseline/no-op pending; C+ remains provisional. | Current repository authority is controlling until changed through its governance process. |
| Open PR #8 | Draft branch says G1–G7 remain open/incomplete and G6.9 Step 3D integration remains pending. | Unmerged draft, useful newer proposal evidence but not controlling main. |

**Reconciled conclusion:** There is a material authority conflict. Broad G6.9 research was marked complete in later snapshots, while the required framework-native comparison/decision is not evidenced in the inspected package contents and is still pending on main and PR #8. Therefore “G6.9 research consolidation was declared complete” and “G6.9-R2 Step 3D has no verified closure evidence” can both be true. The final stack winner and formal Gate closure are unresolved until an owner-reviewed supersession or Step 3D evidence is linked.

### G7 gate status by package claim versus actual repository evidence

| Gate | Package-level state found | What can be claimed now |
|---|---|---|
| G7.1 | Standalone market package exists; later Authority v1.8–v1.9 calls market research complete. | Research package and a later completion claim exist; no independent customer/site validation is established by package status alone. |
| G7.2 | Economics/dispatch package exists; v1.3–v1.6.2 says static preflight completed but live R0 baseline/no-op pending; later Authority snapshots broaden completed-gate claims. | Keep live baseline/no-op and G1 settlement limits explicit; do not equate economics design with validated bill result. |
| G7.3 | No standalone G7.3 ZIP in the supplied folder; research appears embedded in Research Authority v1.6.2. Later Authority calls dispatch research complete. | Research artifact is embedded; standalone closure/evidence package was not located in inventory. |
| G7.4 | Pilot/ROI blueprint package says research/design package completed and G7.5 next. | Pilot blueprint exists; this is not evidence of an agreed customer pilot or measured ROI. |
| G7.5 | Step 2 tenant/security and Step 3 platform blueprint packages mark their design outputs completed. | Platform/security design exists in archives; implementation/adoption remains separate. |
| G7.6 | Step 3 vertical slice is design-complete; Steps 5–7 are bootstrap/implementation/code-skeleton plans or blueprints marked complete in their packages. | Main later has bounded Phase B/C code, but these archived design completions do not establish full MVP or field validation. |
| G7.7 | Repository foundation Steps 1–5 are marked completed in individual packages. | Repository was subsequently created; verify each policy against current GitHub workflows and branch rules before calling governance active. |
| G7.8 | Step 3 stack ADR freeze and Steps 4–5 repository/CI bootstrap packages mark their historical outputs complete. | Fastify-based ADR record conflicts with NestJS implementation; current architecture authority still needs reconciliation. |
| G7.9 | Step 1 MVP domain foundation and Step 2 data/contracts marked complete. Step 2 `NEXT_GATE.md` explicitly names Step 3 Service Boundary and Implementation Design next. | Step 3 remains open. PR #10 APP-11/product/boundary documents are proposals and cover only part of Step 3; they do not close the gate. |

### Current GitHub placement audit (verified 2026-10-04)

- **Research authority:** current `main` has the controlling handoff; several later package assertions, v2.0 recovery files, and v2.1 assertion are not reconciled into it.
- **Product design:** main/PR #8 contain a broad PRD and prototype v0.11. PR #10 adds the source/load dispatch product design, synthetic prototype and APP-11 logical-boundary proposal. PR #10 is open, draft and unmerged.
- **Architecture/ADR:** main has NestJS/Go/Python bootstrap and bounded Phase C VS-001 evidence. PR #8 contains stack-neutral detailed-design drafts. G7.8 Fastify ADR vs NestJS implementation vs C+ report recommendation remains a traceable conflict, not an approved winner.
- **UI/UX:** PR #8 has visual-design principles, an English synthetic v0.11 prototype, and a project-specific UI/UX skill under `.agents/skills/macau-energy-os-ui-ux/` on its open branch (head `91a184603cc4f8ffeb8b89afbe0daac3fe7c8ec1`). Root `AGENTS.md` on that branch points interface work to the skill. PR #10 has a dispatch UX review and Traditional-Chinese synthetic study. The skill is not on `main` until PR #8 is approved/merged; no full locale, multi-viewport visual review, representative user test, or award-level outcome is claimed.
- **Technology reconciliation:** PR #11 has been updated with the Authority v1.6.2–v2.1 conflict addendum; PR #11 remains open/draft and does not modify controlling main.
- **Engineering governance:** PR #9 remains a proposal; required branch checks/branch protection have not been established as adopted policy in the inspected evidence.
- **Original shared ChatGPT conversation:** still not fully readable in this environment. The page only displays its title/login surface; the conversation tool returns recent turns, not the older full transcript.

The audit remains partial at the per-file semantic level. The manifest gives complete package coverage; the next review should read the remaining package bodies and map each authoritative artifact to a specific repository path/commit/PR, with “not found” distinguished from “not merged”.



## Supplemental source-access and skill status — 2026-10-04

- Reopened the original share URL in the in-app browser: the page title is visible, but its message area is empty and the page shows a Login action. Re-read the related conversation record through the archive tool: exactly four recent turns are returned, with no next cursor and hasMore=false. The share URL and conversation record therefore still do not prove access to the complete original research dialogue.
- The local project-specific UI/UX skill and its two references are now present on open PR #8 under `.agents/skills/macau-energy-os-ui-ux/`; root `AGENTS.md` links UI work to it. This is a proposal branch, not merged main authority. Exact PR #8 head `91a184603cc4f8ffeb8b89afbe0daac3fe7c8ec1` passed Authority Validation #962, Repository Hygiene #961, Contracts Validation #128 and Runtime Bootstrap #358. Those checks do not validate visual rendering or user experience.


## Public Macau tariff/PV current-source follow-up — 2026-10-05

This is a dated source update, not a change to the repository's controlling Authority or a Gate closure. Selected public CEM tariff/PV pages and Official Gazette regulations were checked and recorded in `docs/01-research/G1-SETTLEMENT-AND-R0-EVIDENCE-READOUT-v0.1.md` on the open audit branch:

- CEM's public Group B page states eligibility conditions and billed-demand formula `0.2Pc + 0.8Pu`; it defines Pu as the billing-period highest measured demand. The actual customer class, Pc, meter setup and Pu measurement window are still unverified (U-001).
- CEM's TCA table shows the 2026 Q3 parameter and effective date; this is a dated published value, not a complete customer invoice.
- Macao's PV interconnection regulation and CEM's published feed-in schedule document public interconnection/purchase mechanisms subject to applicable conditions. They do not establish a particular installation's approval, payee/account or another building's bill-credit/netting rights (U-002/U-004/U-025).

Placement/status at this update: the evidence readout and research timeline are on PR #12's open Draft audit branch; PR #10's open Draft dispatch proposal now references the Group B rule and maps U-001/PV gates into provisional G7.9 Step 3 acceptance cases. Neither PR is merged. Main's authority, G1 status, G7.9 Step 3 status and product/architecture approval are unchanged. Main code, user/site bills and Golden Bill evidence do not establish customer-specific economics.
