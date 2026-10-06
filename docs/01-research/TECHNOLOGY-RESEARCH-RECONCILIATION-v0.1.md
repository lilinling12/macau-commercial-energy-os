# Technology Research Reconciliation — Reports (6)/(7), G7.8 and G6.9 v0.1

**Checked:** 2026-10-04 (Asia/Bangkok)  
**Status:** Evidence reconciliation for review. This is not a technology decision, ADR replacement, or production architecture approval.  
**Repository:** `lilinling12/macau-commercial-energy-os`

## Finding

The research did **not** select Next.js as the Energy OS backend or as the operator-console framework. Deep Research (7) explicitly recommends React + TypeScript as an SPA for the authenticated operator console and describes Next.js only as a conditional option for a public/customer portal or where its server-side features materially help. That is a use case option, not a backend selection. The same report recommends Node LTS + NestJS for the cloud API/control plane.

Deep Research (6) presents a materially different **provisional pre-bake-off recommendation**: React/TypeScript, a thin Bun/Hono web/BFF surface, Go as authoritative Energy Core, Temporal Go workers, Go Edge/Safety, and Python intelligence. Its text does not mention Next.js. Neither research recommendation is the measured G6.9 winner.

The currently controlling `main` handoff records a provisional layer summary and says C+ is not a measured winner; it keeps G6.9-R2 Step 3D pending. Therefore this report does not freeze either report's stack.

## Source identity

| Source | Identity / hash | What it establishes |
|---|---|---|
| User-supplied `D:\Downloads\deep-research-report (6).md` | SHA-256 `1E0118807DBFDCA3D13AE1949383B4CBFEFB80DB0CD867D13BD6C8DC0D744495` | Recommends Candidate C+ before the bake-off; names React/TS, Bun/Hono BFF, Go core, Temporal Go, Python, NATS/Timescale and Go Edge. Node 24 is the compatibility control/candidate in its A/B/C+ matrix. |
| User-supplied `D:\Downloads\deep-research-report (7).md` | Research date shown in file: 2026-10-02; SHA-256 `5DB518CBE85402E0A8AD2682B9E52A7782D17748EC95C60F43B4BB748B6CAC82` | Recommends a TypeScript-first hybrid: React/TS SPA, Node LTS + NestJS control plane, Go ingestion/Edge, Python intelligence. Its Next.js text is conditional and discusses public/customer portal or useful server-side UI composition. |
| User-supplied G7.8 Step 3 archive `macau-commercial-energy-os-g7.8-step3-technology-stack-adr-freeze-v0.1.zip` | Local source at `D:\dev\project\lilinling\macau-commercial-energy-os` | Historical `ADR-TECH-001.md` says TypeScript cloud platform; `BACKEND_FRAMEWORK_DECISION.md` says “Start with Fastify-based architecture”; `FINAL_STACK_MATRIX.md` says Node.js LTS. Package marks G7.8 Step 3 complete and Step 4 bootstrap next. |
| Main authority `docs/00-authority/handoff/CURRENT.md` and `docs/03-architecture/technology-authority/G6.9-technology-selection/README.md` | `main`, checked 2026-10-04 | Current authority describes React/TS and TS/Go responsibility split as provisional; A/B/C+ remain candidates, C+ provisional only; Step 3D and Step 4 selection evidence remain pending. |
| G7.9 Step 2 archive | `macau-commercial-energy-os-g7.9-step2-domain-data-contract-design-v0.1.zip` in the same local source folder | Step 2 is marked complete; G7.9 Step 3 Service Boundary and Implementation Design is next. The package says no business implementation code yet. |
| Draft PR #8 | [PR #8](https://github.com/lilinling12/macau-commercial-energy-os/pull/8), open and unmerged at check | Contains proposed updates and a Step 3D preflight/readiness plan; those are branch proposals and do not supersede `main` or demonstrate a completed Step 3D run. |
| Draft PR #10 | [PR #10](https://github.com/lilinling12/macau-commercial-energy-os/pull/10), open and unmerged at check | Adds APP-11 source/load dispatch product and logical boundary proposals; explicitly leaves wire schemas, module/deployment split and stack unapproved. |

## Decision and implementation timeline

| Stage | Evidence | Status and interpretation |
|---|---|---|
| G7.8 Step 3 “Technology Stack ADR Freeze” | Package says completed; TypeScript cloud platform, Node LTS, Fastify-based architecture, React/TS, Go Edge, Python and OpenAPI/JSON Schema. | A historical direction was frozen at that gate. The archive itself has a mismatch: its broad ADR chooses TypeScript backend, the framework note selects Fastify, and the later repository bootstrap/main implementation uses NestJS. Preserve the mismatch in the history. |
| G7.8 Step 4 / repository bootstrap | G7.8 package sequence proceeds to repository implementation bootstrap; current main documents Phase B/C Node/NestJS. | NestJS is an implemented Candidate B path. Main authority expressly says implementation does not prove that Candidate B won. |
| G6.9-R2 re-evaluation | Main G6.9 authority defines A (Bun/Hono/Effect with Node Temporal worker), B (Node 24 + NestJS/Fastify + Temporal TS), and C+ (Go authoritative core with thin TS/Bun/Hono surface and Temporal Go). | Later bake-off authority reopened stack selection. C+ is called a provisional default hypothesis, not winner; A and B remain candidates. |
| Deep Research (6) | Candidate comparison and recommendation made before the common bake-off. | C+ recommendation; includes no Next.js decision. Report recommendation is not measured gate evidence. |
| Deep Research (7) | TypeScript-first hybrid recommendation; scored alternatives include NestJS/Go-first. | Node/NestJS control-plane recommendation; Next.js is optional for separate portal/server features. Scores and team estimates are report analysis, not measured project results. |
| Current G6.9/G7.9 work | Main handoff; G7.9 Step 2 package; open PR proposals. | G6.9-R2 Step 3D remains pending. G7.9 Step 3 boundary/design remains next. PR #10's APP-11 is a Step 3 proposal input, not G7.9 Step 3 completion. |

## Technology status matrix

| Technology / boundary | Evidence-based status | Do not claim |
|---|---|---|
| React + TypeScript | Current provisional web layer in main; both reports recommend it. | That a production UI framework/bundler has been finally selected. |
| Next.js | Report (7) conditional option for public/customer portal or useful server-side UI composition; not in the defined G6.9 A/B/C+ candidate matrix; not selected by inspected ADRs. | That it is the chosen Energy OS backend or default authenticated operator-console stack. |
| Node.js | Production-LTS compatibility/candidate runtime in reports and G6.9 B; Node/NestJS exists in current bootstrap. | That the existing runtime path is the measured winner. |
| NestJS | Candidate B and current main implementation path; preferred control plane in report (7). | That it supersedes the historic G7.8 Fastify record or closes G6.9. |
| Fastify | Explicitly selected in G7.8 Step 3 framework note; also an option in G6.9 B. | That current main establishes it as the active production framework. |
| Bun + Hono | G6.9 A and thin surface in C+; report (6) recommends C+; not measured as a G6.9 winner. | That it is already approved or the only viable TypeScript backend surface. |
| Go | Edge/Safety proposal in the layer summary; authoritative core in C+; ingestion/Edge in report (7). | One approved production service topology. |
| Temporal | Workflow candidate; Go workers in C+, TypeScript workers in A/B. | A finalized language/worker deployment choice. |
| PostgreSQL + Timescale, NATS JetStream, Python, Wasm/WASI | Provisional baseline/candidate/responsibility/future direction per main and research. | That each component's deployment boundary, version, operational model or final inclusion is frozen. |
| Java/Spring | Historical tariff implementation path explicitly suspended by D-069 in main. | That Java is current MVP authority or the next implementation step. |

## What “Next.js as backend” means here

Next.js can expose server-side features, but the reviewed reports do not recommend it as the project's backend/control plane. Report (7) separates the authenticated React/TypeScript SPA from the Node/NestJS control plane and mentions Next.js as optional portal/server composition. Report (6) recommends a thin Hono BFF and Go core in its provisional C+ design. Thus the evidence-backed answer is: **Next.js was researched as a conditional web option in report (7), not selected as the Energy OS backend.**

If the product later gains a concrete server-rendered/public portal or BFF need, compare that need explicitly. Adding Next.js to the G6.9 bake-off would require changing the candidate authority and running comparable evidence; it should not be inferred from the framework's ability to host server routes.

## Current conclusion and next evidence

1. Keep current main authority controlling until an owner-approved decision changes it.
2. Preserve the G7.8 Fastify decision as history, while recording the later NestJS implementation and G6.9 re-evaluation.
3. Do not declare a production architecture selected. Execute the authorized G6.9-R2 Step 3D common integration/failure experiment and its decision rule; review Step 4 evidence before any final stack freeze.
4. Continue G7.9 Step 3 using the existing Step 2 model and contracts. Reconcile APP-11 with APP-01…APP-10; define service/API modules, Edge and optimizer boundaries, canonical contracts and repository tasks as proposals. PR #10 covers only part of this work.
5. Present a Next.js candidate only if an evidenced SSR/public portal/server composition requirement exists and the owner approves adding it to a comparable experiment.

## Verification limits

- The shared original ChatGPT conversation is not proven fully readable in this task. This document uses the supplied research reports, local authority archives, fetched GitHub files and open PR state listed above.
- The research reports remain local files; their hashes identify the inspected copies but do not show they are versioned in GitHub.
- No Step 3D candidate integration or benchmark was executed in this task.
- No owner has approved a final product UI, production topology, or Next.js adoption through the evidence inspected here.


## Addendum — Authority v1.6.2 through v2.1 status conflict (2026-10-04)

The earlier timeline above was incomplete because it compared reports (6)/(7), G7.8, G7.9 Step 2 and the current main handoff, but did not include the later local Authority v2.0 and v2.1 source files and recovery packages. This addendum records the conflict without choosing one source by version number alone.

| Source | What the source itself asserts | Reconciliation |
|---|---|---|
| Research Authority v1.6.2 package | G6.9-R2 Steps 3A/3B/3C complete; pinned framework-native Step 3D is pending. G1 and the G7.2 live baseline/no-op remain open. | Direct gate-status source, but it predates later Authority files. |
| Authority v1.7.0 package | G6.9-R2 consolidation release; technology research, architecture and related research are complete, while final framework bake-off evidence and reference-implementation decision remain pending. | Broad research completion does not itself select a measured framework winner. |
| Authority v1.7.1 package | Provisional TS Product Plane + Go Energy Kernel + Python Intelligence; cloud framework, Bun scope and event architecture remain open. G7.2–G7.5 are sequenced as subsequent research. | Explicitly retains stack questions as unresolved. |
| Authority v2.0 recovery / Step 2 / Step 3 / Step 4 packages | Recovery and mapping work is described as complete; the architecture consolidation records broad system boundaries; repository-preparation work is marked complete, while actual repository initialization/bootstrap remains a later step in that package's checklist. | These packages establish recovery/preparation outputs, not by themselves a runnable Step 3D comparison or production implementation. |
| Loose Authority v2.0 Markdown | Lists several G6.9-R2 substeps, including 3G.1 complete and 3G.2 next, while leaving the cloud-core framework and implementation questions under evaluation. It does not list Step 3D as completed. | Does not support treating the framework bake-off as closed. |
| Loose Authority v2.1 Markdown | States that G6.9 Technology Selection / G6.9-R2 AI Native Engineering is complete and that the project is entering G7, with G7.1 next. It does not provide Step 3D comparison results or a measured winner in the inspected text. | A material later closure assertion, but its evidence and supersession relationship to v2.0, v1.7.x and main are not established by that file alone. |
| GitHub main docs/00-authority/handoff/CURRENT.md | Snapshot 2026-10-03: G6.9-R2 Step 3D pending; G7.2 live baseline/no-op pending; C+ provisional. | Controlling repository state until an authorized, reviewed change updates it. |
| Open PR #8 | Snapshot 2026-10-04: G6.9 Step 3D integration pending; G1–G7 open/incomplete. | More recent proposal branch, but unmerged; it does not supersede main. |

### Corrected interpretation

The local sources contain a **Gate-authority conflict**, not sufficient evidence to announce either “G6.9 is definitely complete” or “the v2.1 completion statement is invalid.” Authority v2.1 is a later assertion of completion, but the inspected source does not link the required framework-native Step 3D run, decision rule, results, approver, or an explicit supersession record. Main and PR #8 still record Step 3D as pending. Accordingly, the defensible GitHub status remains **unresolved pending authority reconciliation**; production framework selection remains unproven.

The lettered G6.9 workstream entries (for example, Step 3G.1/3G.2) are not evidence that the separately named Step 3D framework comparison was executed. Likewise, completion of a recovery, architecture-boundary, or repository-preparation package must not be substituted for actual repository implementation or runtime evidence.

### Required authority repair

1. Add a dated, owner-reviewed supersession/decision record identifying which Authority version controls and why.
2. If Step 3D was executed, link the exact pinned candidate/runtime/lockfile versions, shared workload and fixtures, run logs, failure-injection results, scoring rule, reviewer and accepted decision.
3. If Step 3D was waived or replaced, record the approver, rationale, replacement evidence and explicit impact on the G6.9 exit criteria.
4. Update main CURRENT.md, the gate register, and technology ADR only after that review; until then preserve the conflicting assertions as unresolved history.

This addendum is a reconciliation correction only. It closes no Gate, selects no stack, and does not supersede main authority.


## Addendum — G7.6 Step 2 accepted MVP ADRs (2026-10-04)

A second G7.6 Step 2 archive is materially more detailed than the short 7-entry package: `macau-commercial-energy-os-g7.6-step2-engineering-foundation-v0.1(1).zip` (39 entries; Authority v1.7.1). Its detailed package includes ADRs marked Accepted for the MVP baseline:

**Duplicate status discrepancy verified:** the short `macau-commercial-energy-os-g7.6-step2-engineering-foundation-v0.1.zip` has SHA-256 `18704C677AF55A53886806A219A1A5EE22DEA9EF3A0256E286EC9429DD7F2785`; its seven-entry `DECISION_LOG_UPDATE.md` labels ADR-068 **Proposed** and it contains no separate ADR files. The 39-entry `(1)` archive has SHA-256 `F3955862E9902166F82126A2C489E798413676CF93000D4F3F68F650867D47EB`; it contains detailed ADR-068/071–076 files all marked **Accepted**, and `TECH_STACK_FREEZE.md` is dated 2026-10-03. These are distinct local artifacts with conflicting status, not merely two names for one byte-identical file. Preserve the discrepancy until an authority/lineage record identifies which package supersedes the other.

| ADR / artifact | Accepted package decision | Current reconciliation |
|---|---|---|
| ADR-068 | TypeScript/Node product platform, Python intelligence, Go Edge runtime. | Corroborates the language split, but not the current NestJS-vs-Fastify or Go-core decision. |
| ADR-071 | Start the platform as one deployable modular monolith; preserve explicit/testable domain modules. Reject separate identity/tenant/asset/telemetry/energy/report services absent demonstrated scale/team needs. | More specific than G7.5 Step 3's proposed initial microservice list; it explicitly clarifies those as logical boundaries, not a mandate for separate deployables. |
| ADR-072 | Node.js 24 LTS + Fastify 5 stable baseline. | Stronger and more specific historical framework/runtime decision than G7.8's generic TypeScript backend. It conflicts with main's NestJS bootstrap and with the G6.9 current handoff that still marks the framework-native comparison pending. |
| ADR-073 | PostgreSQL 18 as initial transactional system of record and telemetry store using partitioning; defer a dedicated time-series/OLAP database until actual pressure remains after partitioning/indexing/rollups/retention. | Conflicts with reports (6)/(7) and current main's provisional PostgreSQL + Timescale baseline. The evidence does not show that Timescale was measured necessary or that ADR-073 was superseded in a current accepted ADR. |
| ADR-074 | NATS + JetStream as low-latency/durable event backbone. | An explicit historical accepted choice, not merely a report recommendation. Its current status must be reconciled against G6.9 provisional event architecture and current implementation. |
| ADR-075 | Contract-first versioned HTTP/event boundaries; generated clients/types derive from contract; no direct database coupling across deployable runtimes. | Strongly corroborates contract-first governance; exact schema source, protocol coverage and CI enforcement still require repository mapping. |
| ADR-076 | No direct cloud-to-equipment control; cloud creates recommendations or future CommandProposal, physical execution passes Edge safety boundary. | Strongly corroborates the advisory MVP boundary; does not prove a production command/safety system exists. |

The package's `CURRENT.md` calls this engineering shape frozen and marks the related decisions Accepted. Its `NEXT_GATE.md` asks the following Step 3 to bootstrap a simulated chiller vertical slice with tenant-scoped API checks, determinism and recovery. The ZIP also contains a prototype bootstrap tree, CI baseline and AI coding governance; those package files are proposed implementation artifacts until matched to the actual GitHub tree and verified behavior.

### Updated stack timeline interpretation

The current record now contains three distinct stages that must remain visible:

1. **G6.9-R2 v1.6.2:** Step 3C semantic slice complete; pinned framework-native Step 3D still pending.
2. **G7.6 Step 2 / G7.8 Step 3:** explicit package decisions accept Node 24 + Fastify, PostgreSQL 18 without a separate time-series store initially, NATS JetStream, contract-first boundaries and modular-monolith deployment.
3. **Current GitHub main and later research:** main has a NestJS platform bootstrap; main handoff calls the larger stack provisional and Step 3D pending; report (6) recommends conditional C+; report (7) recommends NestJS/Go-ingestion/Kafka-target. These later implementation/research facts do not silently revoke the accepted Fastify/PostgreSQL/NATS ADRs.

Therefore the previous shorthand “no production framework direction was selected anywhere” was too broad: **G7.6/G7.8 do record a concrete accepted Fastify-based MVP baseline.** The unresolved question is whether that historical accepted baseline is the currently controlling production decision, was later superseded by an approved change, or was implemented differently without a recorded deviation. Main's NestJS path alone cannot answer that. Likewise, the data/event records contain a concrete PostgreSQL-only initial-store and NATS+JetStream baseline that conflicts with current provisional PostgreSQL+Timescale/event-candidate wording.

Before any architecture freeze, maintainers should trace each ADR-068/071/072/073/074/075/076 into the current decision register and implementation paths, identify explicit supersession/deviation records, and compare the actual lockfiles/workflows/deployment files. The G6.9 Step 3D status conflict remains open; the package-level accepted ADRs should not be erased merely because main has a different scaffold.


## Addendum — Exact main implementation and G7.9 domain boundary (2026-10-04)

Current main files and its recursive Git tree were fetched directly after the archive comparison.

### Runtime and repository implementation actually present on main

| Area | Main-branch evidence | Interpretation |
|---|---|---|
| Platform API | `implementation/platform-api/package.json`: Node `24.21.x`, npm `11.19.x`, Nest `12.0.3` with `@nestjs/platform-express`, TypeScript `6.0.3`. | Actual Candidate B-style NestJS bootstrap, not Fastify. The main handoff explicitly says it does not prove a bake-off winner. |
| Go Edge | `implementation/edge-runtime/go.mod`: Go `1.27.1`; typed telemetry event and test exist. | Small implementation slice; not production site protocol/safety commissioning. |
| Python optimizer | `implementation/optimizer/pyproject.toml`: Python `>=3.14,<3.15`, no runtime dependencies declared. | Recommendation-boundary skeleton, not a demonstrated solver or forecast stack. |
| Monorepo/package governance | Recursive main tree shows per-area directories but no root pnpm workspace, Turborepo config, Docker/Compose file, database migration tree, NATS/Timescale deployment config or application lockfile under `implementation/`. | The detailed G7.6 Step 2 bootstrap tree/tooling baseline has not been imported wholesale into main. Presence/absence here is scoped to the inspected recursive tree and paths. |
| CI | Main has authority, contract-fixture, repository-hygiene and runtime-bootstrap workflows. | Some checks are active; this does not prove every G7.6 proposed gate (DB migrations, NATS/Postgres integration, security/secret scans, optimizer evaluation fixtures) is adopted. |

Thus the repo's concrete toolchain is more specific than the main architecture summary: Node 24.21/npm 11.19/Nest 12 Express adapter/TS 6.0.3, Go 1.27.1, Python 3.14.x. Those are implementation facts, not a resolution of the conflicting Fastify ADR and G6.9 Step 3D status.

### G7.9 Step 1/2 scope versus source/load scheduling

The supplied G7.9 Step 1 package marks its domain foundation complete. Its `MVP_SCOPE.md` includes tenant isolation, building/asset/device registration, telemetry, an energy dashboard and basic recommendations; it excludes direct control, autonomous complex AI and a full billing system. Its vertical slice is simulator → Edge → telemetry contract → platform/storage → optimizer → recommendation → portal. This is the earlier implementation foundation, but it does not yet make interval-aligned grid/PV/ESS/flexible-load economic schedule comparison an explicit first-class user workflow.

The Step 2 package marks domain/data/contracts complete and says **“No business implementation code yet.”** It lists Tenant, Organization, Site, Building, Energy Asset, Device, Telemetry Point/Record, Optimization Run and Recommendation; however, its relationship sketch omits Site. Its telemetry example contains tenant/site/device IDs, metric, value, unit and timestamp, while quality/provenance, separate observed/received time, interval semantics, idempotency and settlement evidence are not fully specified. Its next gate is G7.9 Step 3 Service Boundary and Implementation Design with Platform API, Edge, Optimizer and repository tasks.

Main later implements Phase C VS-001 typed telemetry/evidence/recommendation/replay semantics. That bounded vertical slice and PR #10's APP-11 source/load assessment proposal are relevant implementation/design advances, but neither demonstrates a complete site-level economic dispatch engine, bill-grade Macau settlement, all G7.9 Step 3 outputs or pilot validation.

### Corrected architecture/product status

- Historical package ADRs do record an **accepted MVP baseline** (Node 24 + Fastify 5, PostgreSQL 18 without an initial dedicated time-series store, NATS JetStream, modular monolith).
- Current main records a **different implemented path** (Node 24.21 + NestJS 12 / Express adapter), but explicitly leaves Candidate B unselected while G6.9 Step 3D is pending and C+ is provisional.
- Therefore use “historically accepted G7.6 baseline” for the Fastify/PostgreSQL/NATS decisions and “currently implemented, still provisional main path” for NestJS. Do not collapse these into one current approved stack.
- Product-wise, the direction is coherent at the mission level (economic source/load orchestration under constraints), but the early G7.1/G7.5 go-to-market phases and G7.9 dashboard/recommendation MVP defer dispatch relative to the present dispatch-first requirement. PR #10 is the current draft proposing that product-flow reconciliation.


## 2026-10-05 — Current SHADOW optimizer experiment cross-check

The technology status above is supplemented by the separately reviewed implementation experiment. This updates the implementation inventory, not the architecture authority.

- `main` remains at `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`. Its Python optimizer package remains a recommendation-boundary skeleton.
- PR #14 `poc/shadow-dispatch-assessment` is a separate open Draft, unmerged branch at exact head `b7ae02fe8dd4b346961235a7db523471c239b883`. It adds a finite-horizon discrete dynamic-programming search and schedule assessor in Python. The code accepts one site, one EconomicContext and one account/meter/contract/tariff reference set; it calculates only interval-qualified grid-import energy charges and labels partial coverage. It does not add an integrated Platform API, authenticated evidence service, durable snapshot/replay, full tariff settlement, or device control.
- At that exact head, Runtime Bootstrap `37255779321` passed Optimizer (27 tests), Platform API, Go Edge and Contract Fixtures. Authority Validation `37255779320` and Repository Hygiene `37255779342` failed on main-base authority/handoff path expectations. These results establish a bounded prototype execution, not a production optimizer or architecture benchmark.
- PR #10's G7.9 Step 3 map now records this experiment at its exact head in commit `3ae590b0823f70802f4fe8a53020c018aaf41a21`; PR #10 remains open/Draft/unmerged, and the design still requires a canonical APP-11/service boundary, authority decision and authenticated, immutable multi-scope inputs before integration. The newer PR #10 product-direction reconciliation commit is `086dd675a0a3b0cfc4381e8d0551a4971990e2f5`.
- The Python experiment does not compare Python against Go/Node candidate implementations on the authorized common workload. It supplies evidence that one bounded algorithm can run in the existing Python workspace; it does not select Python as the production solver boundary or affect the NestJS/Fastify/Go-core/Next.js status matrix.

Next.js remains a conditional public/customer portal or server-side composition option mentioned in report (7), absent from the defined G6.9 A/B/C+ candidates, and not selected. No new source in this update closes G6.9 Step 3D, resolves G7.6/G7.8 versus G6.9 authority precedence, or freezes the production stack.

## Live GitHub state refresh — 2026-10-06

This refresh updates only the repository implementation/proposal status. It does not supersede main authority or select a production stack.

| Evidence | Current status checked |
|---|---|
| Main | Base remains `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`; main's G6.9-R2 Step 3D is pending and C+ remains provisional. |
| PR #8 | Readiness audit refresh `8b73b9ff4e0ab49e67ed6f293383cfd98ee26e55`; exact-head Authority Validation, Repository Hygiene, Contracts Validation and Runtime Bootstrap passed. Open/unmerged. |
| PR #10 | Optimizer/UI cross-branch trace `c23ef73fe4952255e31cef444ade81d66972f626`; exact-head Authority Validation and Repository Hygiene passed. A follow-up owner-packet refresh `c827b6f9c7bf228c29a85c0ff1daff430bc8b386` is now on the same branch; its check was queued at this refresh. Open Draft/unmerged. |
| PR #11 | Current source-reconciliation branch remains open Draft/unmerged; the prior recorded exact head is `8ec91db5ad08cb289daf6ba62ba79ac3603c818b`. |
| PR #14 | The service-separation assertion correction is at `c235388db1678927f2c875bba6be88b0f01f25e2`; the PR #10 cross-review reports 32 optimizer tests and all Runtime Bootstrap, Authority Validation and Repository Hygiene checks passed. Open Draft/unmerged. |

The PR #14 description itself stops at the earlier `0b69...` entry. Its later `c235...` test correction is evidenced by the source commit and the PR #10 cross-branch review; do not use the stale PR description as the latest code head.

### Architecture decision status remains unchanged

- The detailed supplied G7.6/G7.8 archives record accepted Fastify/Node, PostgreSQL-first-store, NATS JetStream and contract-first choices; distinct short and detailed G7.6 archives disagree on ADR-068 status. They remain local source evidence and are not all present in main as canonical decision artifacts.
- Main's G6.9 authority still requires Step 3D/Step 4 evidence and labels C+ provisional; the actual NestJS path is implementation evidence, not the comparative winner.
- Reports (6) and (7) remain different pre-bake-off recommendations. Report (6) proposes C+ without Next.js. Report (7) recommends a React/TypeScript SPA and Node/NestJS control plane, with Next.js only a conditional public/customer portal/server-composition option.
- PR #14 proves a bounded synthetic Python experiment only. It does not establish a production optimizer boundary or change the Node/Fastify/NestJS/Go-core decision.
- PR #10's exact-source mapping and 2026-10-06 browser recheck show that v2.4 has interactive fixed-fixture claim cases plus a separate synthetic HVAC-state control, but neither is connected to the optimizer/API or one common assessment result. The adapter contract, durable result lifecycle and replay remain design work.

The reviewed owner packet in PR #10 keeps authority precedence, APP-11 logical ownership, product scope/locales and contract authoring as explicit decisions with options and consequences. Until an owner-reviewed authority record resolves those dependencies, keep architecture comparisons evidence-based and stack-neutral. No Gate is closed by this refresh.

### UI-state evidence wording correction — 2026-10-06

The v2.4 source is not interaction-free: its synthetic claim fixture selector and separate HVAC radio group update visible statuses and announcements. At 375 CSS px, the four claim cases and four HVAC states were exercised without page errors or horizontal overflow. The fixed fixtures are local presentation studies, not runtime/API outputs; their separate controls are not connected to the same assessment, schedule or optimizer. This corrects only the interaction description, not the production integration status or architecture decision.


# Technical authority live recheck — 2026-10-07

**Scope:** exact G7.6/G7.8 source-package recheck, live GitHub `main`, implementation manifests, current review PR state, and access status for the referenced original conversation. This supplements the broader technology reconciliation; it does not approve or freeze a production stack.

## 1. Current repository authority is internally inconsistent

At the inspected `main` SHA `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`:

- `docs/00-authority/CURRENT.md` says Authority v2.0 is being imported and research, product, architecture and engineering layers are still being migrated.
- `docs/00-authority/handoff/CURRENT.md` uses Research Authority v1.6.2 plus G6.9-R2 Steps 3A–3C, says Step 3D pinned framework integration is pending, and calls C+ a provisional default rather than a winner.
- `docs/03-architecture/technology-authority/G6.9-technology-selection/README.md` records the layer summary React/TS, TS/Go responsibilities under evaluation, Temporal candidate, PostgreSQL + Timescale baseline, NATS JetStream candidate, Python, Go Edge and future Wasm/WASI. It explicitly says C+ is only a provisional hypothesis and Step 3D remains next.

These are two current-state entrypoints with different authority/scope claims. `handoff/CURRENT.md` is operationally more detailed, but the repository does not clearly declare how it supersedes or relates to the short Authority v2.0 import status. Do not silently collapse them into one authority statement.

## 2. Exact historical technology records

| Source archive | SHA-256 | Exact decision evidence | Interpretation today |
|---|---|---|---|
| `macau-commercial-energy-os-g7.6-step2-engineering-foundation-v0.1.zip` | `18704C677AF55A53886806A219A1A5EE22DEA9EF3A0256E286EC9429DD7F2785` | Seven-entry short package; `CURRENT.md` says research package completed. It does not contain the detailed ADR set. | Distinct summary artifact; cannot be treated as byte-equivalent to `(1)`. |
| `macau-commercial-energy-os-g7.6-step2-engineering-foundation-v0.1(1).zip` | `F3955862E9902166F82126A2C489E798413676CF93000D4F3F68F650867D47EB` | Detailed package says G7.6 Step 2 completed and the engineering shape frozen. ADR-072 accepts Node 24 LTS + Fastify 5; ADR-073 accepts PostgreSQL 18 as initial system of record and defers Timescale/dedicated TSDB until pilot evidence; ADR-074 accepts NATS + JetStream; ADR-076 prohibits direct cloud equipment control. `TECH_STACK_FREEZE.md` selects React 19.3 + TypeScript 6 + Vite 8, Node 24/Fastify 5, Python 3.14, Go 1.27, PostgreSQL 18, NATS 2.12 + JetStream, and says no SSR requirement for the MVP operations portal. | Concrete accepted historical MVP baseline. It is not present as a complete canonical ADR set in current `main`; later G6.9 reopened technology evaluation, but no superseding decision was found in current `main`. |
| `macau-commercial-energy-os-g7.8-step2-technology-stack-decision-v0.1.zip` | `4F8C41AD3E5FA8F2BF61AECEE71DB6BD02260446CBB1E739AA47CDE66FD02EF5` | Proposed React/TS frontend, TypeScript cloud platform, Go Edge, Python optimization, OpenAPI + JSON Schema. `NEXT_GATE.md` calls for Step 3 ADR freeze. | Language/boundary direction, not an exact framework/runtime decision. |
| `macau-commercial-energy-os-g7.8-step3-technology-stack-adr-freeze-v0.1.zip` | `BD82412488C041FF3879A245F479D091C768B9FCEA9286D5266B835EB8E817E3` | `ADR-TECH-001` adopts React/TS, TypeScript cloud platform, Go Edge, Python optimization and OpenAPI/JSON Schema. Companion `BACKEND_FRAMEWORK_DECISION.md` says “Start with Fastify-based architecture.” `CURRENT.md` marks Step 3 complete and Step 4 repository bootstrap next. | Preserve both sources: the broad ADR does not name Fastify; its companion does. The subsequent G7.6 detailed freeze makes the Node/Fastify baseline explicit. |

The current `main` G6.9 record is a later re-evaluation: it preserves React/TS, Go Edge and Python, calls PostgreSQL + Timescale a provisional baseline, lists NATS JetStream as a candidate, and sets C+ as a provisional hypothesis while A/B remain candidates. It explicitly requires Step 3D. No owner-approved supersession of G7.6 ADR-072/073/074 was found on `main`.

## 3. What the repository implements versus what its architecture summaries claim

At the same exact `main` SHA:

- `implementation/platform-api/package.json` pins Node 24.21.x/npm 11.19.x and NestJS 12.0.3 with `@nestjs/platform-express`; this is not Fastify. `platform-api/README.md` calls it a NestJS modular-monolith direction.
- The inspected platform package manifest has no PostgreSQL, Timescale or NATS client dependency; it is not evidence those data/event systems are deployed or integrated.
- `implementation/optimizer/pyproject.toml` has no dependencies; `implementation/edge-runtime/go.mod` declares the Go module/version. These are bootstrap facts, not evidence of a pilot-ready optimizer/Edge integration.
- Current-main runtime governance separately documents Node 24.21/NestJS 12/TypeScript 6, Go 1.27.1 and Python 3.14.8. Runtime pinning does not resolve the historical Fastify ADR conflict or prove production-stack selection.

Accordingly, label the states separately: **historically accepted** G7.6 Node/Fastify + PostgreSQL-only initial store + NATS JetStream; **implemented bootstrap** Node/NestJS Express; **current G6.9 proposal state** C+ provisional, A/B candidates, PostgreSQL+Timescale provisional and NATS candidate; **measured production winner** none evidenced.

## 4. Next.js finding

Deep Research (6) does not recommend Next.js. Deep Research (7) favors React/TypeScript SPA for the authenticated operator console and Node/NestJS for the cloud control plane; it mentions Next.js conditionally for a public/customer portal or useful server-side UI composition. Next.js is outside the main G6.9 A/B/C+ matrix and absent from the inspected G7.6/G7.8 ADRs. It is neither the selected backend nor the operator-console framework. Adding it to a bake-off would require an explicit requirement, an amended candidate set and comparable evidence.

## 5. Live PR and source access state

At this recheck: `main` remains `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`; PR #8 is open/ready-for-review at `9e3dec0bccf5acb5122f94c688814e7f4e026a1b`; PR #10 is open/Draft at `a9ac1889978b873bed5efe070a7d1021af11b651`; PR #11 was open/Draft at `d13fc834ed6274a134eddb48d7e64455572f32d0`; PR #14 is open/Draft at `d5180703df3730779f1f180a89d07c620e7e349d`. None is merged. PR #10's v2.8 UI/APP-11 supplement does not alter the stack or Gate status.

The referenced ChatGPT share URL `https://chatgpt.com/share/6ac10df8-a30c-83e9-83bd-f8de8ec31ca1` could not be fetched in the current browser tool (cache miss). Reading conversation `6abf4f5c-b2d4-83ea-b189-6534f517c5a1` returns only its newest 10 turns, `hasMore=false`, with no attachments. Thus this recheck does not claim to have read the full original research conversation. The two local research reports and the named local archives above were available and directly inspected.

## 6. Required next architecture work

1. Establish one versioned, owner-approved current-authority entrypoint and an explicit precedence/supersession map across Authority v1.6.2/v1.7.x/v2.0/v2.1, G7.6/G7.8 accepted ADRs, G6.9-R2, later reports and live implementation.
2. Reconcile the actual Node/NestJS Express bootstrap against accepted Fastify ADR-072; record whether it is a deliberate deviation, a supersession, or a provisional prototype.
3. Reconcile PostgreSQL-only initial store against PostgreSQL + Timescale current provisional wording, and NATS accepted baseline against later candidate wording.
4. Either execute the exact pinned G6.9-R2 Step 3D/Step 4 common integration/failure comparison with reproducible evidence or record the approved waiver/replacement and its effect on the Gate. Do not call the stack selected until the relevant authority decision is approved.



## Live authority and proposal recheck — 2026-10-07

This recheck updates the branch-level status above from live GitHub reads. It records repository state; it does not amend the governing authority.

### Main-branch technical authority

- The fetched main handoff is blob `5b3da3af0a7e267c34a8a743a30cfc89d8fb24ca`; its declared snapshot remains **2026-10-03**. It says G6.9-R2 Step 3A/3B/3C complete and Step 3D pending, and labels C+ a provisional default rather than a measured winner. It also records the existing Node/NestJS Phase B/C implementation as a bootstrap path, not evidence that Candidate B won. [CURRENT.md](https://github.com/lilinling12/macau-commercial-energy-os/blob/main/docs/00-authority/handoff/CURRENT.md)
- The fetched main decision register blob is `20df79d798b7c39f85778c70b8843fed94cf9428). D-064 keeps Go Energy Core + Temporal Go + Go Edge/Safety, thin Bun/Hono/TypeScript product surface and Python intelligence as the **provisional** default. D-065 requires generated cross-language bindings from versioned OpenAPI, Protobuf or JSON Schema. D-066 separates Temporal workflow state, NATS cloud events, MQTT site/cloud messaging and PostgreSQL business/audit state. D-068 requires a common semantic vertical slice, hard safety/security gates and controlled AI-engineering trials. D-069 suspends only the Java/Spring implementation choice while retaining tariff semantics. [DECISIONS.md](https://github.com/lilinling12/macau-commercial-energy-os/blob/main/docs/00-authority/decisions/DECISIONS.md)
- This does not silently cancel the accepted G7.6 Step 2 ADR package or G7.8 Step 3 Fastify record. The present trace is: **historical package decision = Node 24/Fastify 5, PostgreSQL initial store without a separate time-series database, NATS/JetStream; later main authority = C+ provisional pending bake-off; current repository code = NestJS bootstrap.** The missing evidence is an explicit, owner-reviewed supersession/deviation record plus the Step 3D/4 experiment or approved waiver. “Later” alone does not settle precedence.

### Current review branches and exact-head checks

| Proposal | Live state at this recheck | What the evidence establishes |
|---|---|---|
| [PR #8](https://github.com/lilinling12/macau-commercial-energy-os/pull/8) — roadmap, product/architecture and continuity | Open, unmerged, Ready for review; head `9e3dec0bccf5acb5122f94c688814e7f4e026a1b`; 98 changed files. | Broad review package; its own authority says product, interface, production topology and Gate closure are not approved. Review must remain grouped by subject; successful repository checks cannot replace semantic owner review. |
| [PR #10](https://github.com/lilinling12/macau-commercial-energy-os/pull/10) — source/load dispatch | Open, unmerged, Draft; exact head `5ca2449f1bd9c0e6d78fd2bed4ea8cc880ba6f23). | Authority Validation and Repository Hygiene both succeeded on that head. Its dispatch workflow, APP-11 boundary and fixtures are proposals; they do not choose the production stack or close G7.9 Step 3. |
| [PR #11](https://github.com/lilinling12/macau-commercial-energy-os/pull/11) — this technology reconciliation | Open, unmerged, Draft; exact head before this addendum `e161cf1fe4a61509bff8ce191285360f1a9485f5). | Authority Validation and Repository Hygiene succeeded on that exact head. Those checks validate repository structure/hygiene, not the interpretation or an architecture decision. This addendum requires new exact-head checks after commit. |
| [PR #14](https://github.com/lilinling12/macau-commercial-energy-os/pull/14) — bounded SHADOW optimizer | Open, unmerged, Draft; exact head `9b80adca9243a0ae9a7bd666f0efee1acfc6309a). | Authority, Repository Hygiene, Platform API, Edge Runtime, Optimizer and Contract Fixtures checks succeeded on that head. It is an isolated bounded synthetic optimizer experiment; it is not an integrated dispatch service, site proof, production architecture decision or field-control authorization. |

### Consequences and next architecture work

1. Keep G6.9 Step 3D status **pending/unresolved** in the active handoff until an exact run/decision or approved replacement is linked. Do not treat PR checks or the PR #14 synthetic optimizer tests as Step 3D evidence.
2. Put the G7.6/G7.8 Fastify decision, main D-064 C+ provisional default and NestJS implementation into one owner-reviewed supersession/deviation record. Include the actual runtime/adapter, migration cost and the result of the chosen common decision rule.
3. Reconcile the data/event decisions explicitly: G7.6's initial PostgreSQL-only store and NATS/JetStream record versus main's PostgreSQL system-of-record, Timescale provisional wording and D-066 event responsibilities. Separate “database baseline” from “Timescale extension selected”; separate event broker from workflow engine.
4. Keep G7.9 Step 3 OPEN. PR #10 is a dispatch design proposal and PR #14 is a bounded code experiment; integrate them only after the API/event contract, optimizer boundary, persistence/replay semantics and product acceptance evidence are reviewed.
5. The product work is more advanced as review material than as an approved product: PR #8 contains the PRD, design, prototypes and detailed-design package; PR #10 adds the dispatch-first workflow; PR #14 adds synthetic behavior. All three remain unmerged. None is user-tested or site-validated merely because it exists as a prototype or passes repository CI.
6. Next.js remains an unselected, unassessed candidate-fit question from PR #8 outside the G6.9 A/B/C+ set; report (7)'s conditional portal/server-composition discussion is not an Energy OS backend selection.

This dated supplement does not change main, choose between conflicting ADRs, approve the broad PR #8 review bundle, close a Gate, or authorize production implementation/control.
