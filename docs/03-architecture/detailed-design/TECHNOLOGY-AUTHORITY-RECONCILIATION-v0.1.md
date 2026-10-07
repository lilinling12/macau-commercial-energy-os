# Macau Commercial Energy OS — technology authority reconciliation

**Review date:** 2026-10-05  
**Purpose:** preserve conflicting architecture claims as evidence and identify the decision still needed. This note does not freeze a production stack or decide the authority precedence on the owner's behalf.

## Findings

The supplied material contains **three different kinds of statements** that must not be collapsed: historical gate/archive completion labels, current repository authority, and later research recommendations. They disagree about whether the application core and framework are already selected.

### Source and status matrix

| Source | Exact evidence | Recorded conclusion | Authority/status interpretation |
|---|---|---|---|
| G7.8 Step 3 technology-stack ADR-freeze archive | Local ZIP SHA-256 `BD82412488C041FF3879A245F479D091C768B9FCEA9286D5266B835EB8E817E3`; `CURRENT.md` says Step 3 **Completed**, next Step 4. `FINAL_STACK_MATRIX.md` says React/TypeScript, TypeScript backend, Node LTS, pnpm, Go Edge, Python AI/data, OpenAPI + JSON Schema, Docker, GitHub Actions; Bun for evaluation/development tooling, not mandatory production runtime. `BACKEND_FRAMEWORK_DECISION.md` says “Start with Fastify-based architecture.” | A completed local package records a Node/Fastify/pnpm/contract-first baseline. The detailed G7.6 Step 2 archive adds ADR-072 Node 24/Fastify 5 and ADR-071/073/074/075/076. | Strong historical evidence, but the supplied package is not itself a merge or an active authority record on GitHub main. Its relationship to active G6.9 must be explicitly affirmed or superseded.
| Local Authority v2.0 Step 3 architecture-consolidation archive | `ARCHITECTURE_FREEZE_CHECKLIST.md` marks system boundary, Edge/cloud, AI boundary, multi-tenant direction, technology direction and contract strategy complete; its `CURRENT.md` says Step 3 Completed and Step 4 repository preparation next. | Broad architecture consolidation declared complete and ready for repository preparation. | Conflicts with the later/active main authority's framework-native G6.9 Step 3D evidence gate. Checklist completion does not identify a selected winner or reproduce the pinned comparison evidence.
| Local `macau-energy-os-research-authority-v2.0.md` | SHA-256 `BD705A40A34DBE9BE1248B6B8BD792913ED92B398A32EC32E42D99829A1B4661`; current gate G6.9-R2. It lists 3A/3B/3C/3E/3F/3G.1 complete but does not list 3D; cloud core TS vs Go, Bun production runtime, Hono/Effect vs Fastify/NestJS, and Temporal deployment remain under evaluation. | Frontend React/TypeScript, Python intelligence, Go Edge, PostgreSQL and TimescaleDB are confirmed; cloud core/framework selection remains open. Next is Step 3G.2 Architecture as Code & AI Governance. | Local authority snapshot; its content is consistent with a still-open core/framework decision, but its authority/version relationship to GitHub main must be maintained explicitly.
| Local `macau-energy-os-research-authority-v2.1.md` | SHA-256 `93AF2811B278FA7B1099A6F5FBD69A2A9F7B60CD26ECDAABECBC82676524A373`; says G6.9 Technology Selection and G6.9-R2 AI Native Engineering System completed, current gate G7 Productization, next G7.1 market/ROI research. | Moves the project into productization and pilot design. | Later-numbered local snapshot, but the supplied file does not reconcile its G6.9 closure with GitHub main's still-pending Step 3D or identify a winning core/framework. A higher version number alone is not a supersession record.
| Deep Research report (7) | Research date 2026-10-02; file SHA-256 `5DB518CBE85402E0A8AD2682B9E52A7782D17748EC95C60F43B4BB748B6CAC82`. Recommends React SPA, TypeScript + Node LTS + NestJS Control Plane modular monolith, Go ingestion and Edge, Python forecast/optimizer/simulation, PostgreSQL + TimescaleDB, MQTT 5; Kafka is described as a target path, not necessarily month-one. | A TypeScript-first hybrid recommendation; Next.js is optional for a public/customer portal or when server-side UI features materially help, while the operator console is a React SPA. | Research recommendation, not an accepted ADR or G6.9 bake-off winner. It does not prescribe Next.js as the core backend or operator app.
| Deep Research report (6) | File SHA-256 `1E0118807DBFDCA3D13AE1949383B4CBFEFB80DB0CD867D13BD6C8DC0D744495`; observed file modified time 2026-10-04 17:58:29 (mtime is not proof of report publication time). Calls C+ its provisional recommendation **before the bake-off**: Bun/Hono/TypeScript web/BFF, Go authoritative core + Temporal Go, Go Edge, Python intelligence, PostgreSQL 18 + TimescaleDB, NATS JetStream + MQTT 5, Deno initially and Wasm/WASI later. It states a switch rule requiring materially better AI task time-to-green plus all integration/reliability gates before replacing the Go core. | An updated, falsifiable C+ research recommendation that differs from report (7) on Control Plane/core language, runtime, durable worker, and event backbone. | Not a measured winner or owner-approved stack. It explicitly leaves the runtime/framework choice to a common vertical-slice bake-off.
| GitHub main, `docs/00-authority/handoff/CURRENT.md` | Blob `5b3da3af0a7e267c34a8a743a30cfc89d8fb24ca`, snapshot dated 2026-10-03: G6.9 Step 3A/3B/3C complete; **Step 3D pinned framework-native integration pending**. G1 tariff/settlement remains open; G7.2 live R0 remains pending. Mission is commercial multi-energy orchestration, not a generic dashboard; SHADOW first and no cloud direct control. | Active repository status preserves the framework comparison gate. | Current main authority snapshot at the inspected GitHub default branch; strongest operative repository status in this review.
| GitHub main, `docs/00-authority/decisions/DECISIONS.md` | Blob `20df79d798b7c39f85778c70b8843fed94cf9428`: D-064 C+ is **ACTIVE / PROVISIONAL**; D-065 generated OpenAPI/Protobuf/JSON Schema contracts; D-066 Temporal/NATS/MQTT/PostgreSQL distinct responsibilities; D-068 common semantic + AI-engineering bake-off; D-069 suspends Java implementation; D-076 forbids ranking production frameworks from Step 3C shell timings. | C+ is the provisional default, not a frozen choice. | Active decisions require Step 3D common-slice evidence before a winner is claimed.

## What is shared and what is disputed

**Shared direction:** React + TypeScript product surface, Go for Edge, Python for energy intelligence/simulation, PostgreSQL with a time-series baseline, contract-first boundaries, Cloud proposal versus Edge safety responsibility, and no assumption of direct MVP control.

**Disputed:** Node/NestJS versus Bun/Hono plus Go core; Node/Fastify as either binding historical baseline or superseded candidate; Temporal worker language; Kafka target versus NATS JetStream initial cloud event bus; whether G7.8's contract/framework freeze remains binding. The reports and local archives do not resolve these by themselves.

**Next.js:** report (7) positions it as an optional public/customer portal or server-feature choice. The operator console recommendation is a React SPA. Report (6)'s C+ stack does not include Next.js. Thus the sources reviewed do not establish Next.js as this product's required backend, production API, or selected UI framework; its inclusion should depend on an approved public-portal/server-rendering need.

## Recommendation and next decision

Use GitHub main's active CURRENT and D-064/D-068/D-076 as the operative interim authority, while preserving the local G7.8 and Authority v2.0/v2.1 packages as historical evidence. Do not silently call G7.8 binding, superseded, or equivalent to G6.9 closure. Keep C+ marked **provisional** and finish its common framework-native, fault/recovery, and controlled AI-engineering comparison before production selection.

The owner/maintainer decision is still one of:

1. Affirm the G7.8 Node/Fastify/OpenAPI+JSON-Schema freeze and explicitly reconcile G6.9/D-064; or
2. Record G7.8 as historical and supersede/reopen it under active G6.9, then complete Step 3D; or
3. Reopen only the disputed framework/contract-authoring subset with explicit criteria.

Do not freeze final architecture or author/generate dispatch bindings until that authority decision and the required evidence are recorded. Domain semantics and product design can continue independently.

## Access and verification limits

- The two Deep Research Markdown files and project-folder archives were readable locally and fingerprinted above; the G7.8 and G7.6 archive contents were inspected directly without extraction to the project folder.
- The referenced ChatGPT share page returned a cache miss to the web reader and showed a login-only page in the available in-app browser. The `read_thread` call for the supplied conversation ID returned only a bounded recent ChatGPT conversation slice with no older-page cursor. Therefore this review does **not** claim to have inspected the full shared conversation transcript or every Library attachment.
- This is a focused authority/source reconciliation, not a complete review of all G6.9/G7.1–G7.9 package contents, all GitHub PRs/files, or a fresh runtime bake-off.

## Implementation-state recheck — 2026-10-07

This addendum traces the current default-branch code separately from archive decisions, research recommendations and PR experiments. **Code present on main is implementation evidence; it does not by itself select or approve the production architecture.**

### Current-main implementation evidence

| Concern | Fetched main artifact | What it shows | What it does not establish |
|---|---|---|---|
| Application/API | `implementation/platform-api/README.md` blob `d01c76815d0122ba112264c7b22aa1e49a542206`; `package.json` blob `c42fcbca6b423c392c920080999b0d3c6022a2cc`; `src/main.ts` blob `e4937fe3c6e33caf86d3b439f192034671d8290f` | Node `24.21.x`, npm `11.19.x`, NestJS `12.0.3`, and `@nestjs/platform-express`. `main.ts` calls `NestFactory.create` and listens on the API port. The module wires the VS-001 controller/service and fail-closed ports. | It is not Fastify, not a measured G6.9 winner, and not a completed dispatch control plane. The README says no runtime bootstrap until boundaries are accepted, while the fetched main.ts already bootstraps; this is a documentation/code mismatch to reconcile. |
| Current API slice | `implementation/platform-api/src/vs001/vs001.controller.ts` blob `de93bc59354890f1e8be6274123ecf51f24fb3ca`; `vs001.service.ts` blob `a35cf74b4587fad75415689341de40d88e623ede`; `adapters.ts` blob `d4b0872fd9a52dedf8745cc45bdcbcd2fb3e83d6`; `ports.ts` blob `4dc5303af249f9a5e8f55592063eacc64bba5b32` | The endpoint is a single-event VS-001 evaluation path. Energy Graph and tariff adapters fail closed; the optimizer adapter cannot run until tariff context resolves; evidence storage is in-memory. | It does not implement APP-11 source/load schedule assessment, a durable replay path, a verified Macau tariff/account graph, an authenticated evidence resolver, or a production dispatch service. |
| Go Edge | `implementation/edge-runtime/README.md` blob `7ec8850b88529569ea81667382af6401c1b8436d`; `go.mod` blob `f2869eb831a7380015e5a3d1bee1e1d5d290b805` | The module declares Go `1.27.1`. The README assigns protocol adapters, point normalization, local buffering, retry/reconnect, secure telemetry transport and local health/audit signals to the Edge boundary; it excludes tariff truth and optimization policy. | The README and module declaration alone do not prove production adapter coverage, device commissioning, safety certification or a field-control authorization. Source implementation completeness was not established by these two files. |
| Contracts | `implementation/contracts/README.md` blob `31aef1f622ae22e3cf32ae82dd53bbd2cc8dd204`; schemas `telemetry-event.v1` `b066a0efc149042f70e11113918588169333fcca`, `recommendation.v1` `e558389d6c62c2635475dc443989beef20d1bcab`, `evidence-record.v1` `0d3d1bb2d28ec46ed9ba111ffe9a6e598c2c2fc7` | Versioned JSON Schema contracts exist for telemetry, recommendation and evidence. Their README requires explicit tenant/site, timestamp, unit and evidence-status semantics. | These are not the missing canonical multi-interval dispatch, tariff/settlement-scope, claim-ledger, human-review or replay contracts; an early recommendation contract is not proof of a schedulable/feasible plan. |
| Optimizer | Main `implementation/optimizer/README.md` blob `10b88c297a25a04c6d738530689c3797cd807e8b` | Python is the stated forecasting/simulation/optimization boundary and initial product mode is SHADOW. | No integrated production optimizer or site-calibrated forecast is established on main by this README. |

The fetched Platform API dependency manifest contains NestJS and the Express adapter, but no Fastify adapter, Temporal SDK, NATS client or database driver. This statement is limited to that manifest; it is not a repository-wide proof that those dependencies occur nowhere else. The inspected Edge `go.mod` declares no dependency lines beyond its module path and Go version.

### Candidate implementations on separate PR branches

PR #14's current bounded Python experiment is separate from main. Its assessment module validates a **supplied** schedule and its adjacent finite-horizon search enumerates declared discrete flexible-load and ESS actions. The PR #10 acceptance audit source-pins the code/tests and records the exact PR #14 head and checks. It also identifies material unimplemented or partial cases, including tenant/site authorization, per-interval physical evidence coverage, non-overlapping meter topology, authenticated evidence resolution, durable assessment/replay and real-site tariff validation. The experiment is neither the canonical APP-11 contract nor an integrated production optimizer/API; its green branch checks do not close G7.9.

PR #10 itself contains product, UI/UX, contract and architecture proposals, including newer localized design studies. Those remain on an unmerged Draft branch and do not update the operative main authority.

### Technology-by-technology status after the code trace

- **React + TypeScript:** research/owner-review product-surface direction. No inspected main artifact establishes an approved or integrated operator-console frontend.
- **Node + NestJS:** implemented Candidate B path on main (Node 24.21.x, NestJS 12.0.3, Express adapter). This is an implementation state, not evidence that B won.
- **Node + Fastify:** accepted historical G7.6/G7.8 package claim; not the adapter used by the fetched main Platform API manifest. Binding/superseded status remains unresolved.
- **Go Edge:** main module and responsibility README exist; deployment, protocol, site integration and control-safety acceptance remain unproven.
- **Go Energy Core + Temporal Go:** Deep Research (6) C+ recommendation only. No inspected main code establishes this topology.
- **Bun + Hono:** Deep Research (6) provisional product/BFF proposal; not the fetched main API runtime.
- **Temporal:** candidate in the layer summary/C+ topology. No Temporal SDK or worker was observed in the fetched API manifest or inspected current-main files; no workflow selection is established.
- **PostgreSQL + Timescale:** evaluation baseline/research direction. The fetched API manifest and inspected bootstrap do not establish a database integration, migrations, retention policy or replay persistence.
- **NATS JetStream:** cloud-event candidate. No runtime integration was established by the inspected main manifests.
- **MQTT 5:** telemetry/edge candidate in research. The inspected Edge README describes secure telemetry transport but does not specify an MQTT adapter; protocol implementation was not verified in this pass.
- **Python:** named optimizer boundary on main; the more substantive source/load assessment/search is on separate PR #14, not integrated.
- **Wasm/WASI:** future plugin-isolation direction; no MVP runtime or sandbox implementation was observed in the inspected main files.
- **Next.js:** Deep Research (7) describes a conditional public/customer portal or server-feature option. It is not the recommended authenticated operator console, the proposed backend, or a G6.9-R2 candidate in the reviewed matrix.

### Architecture and implementation implication

Two separate decisions are still being conflated in some historical notes: **which topology is authorized as the target** and **which scaffold currently exists**. Main currently runs a Node/NestJS + Express VS-001 API path, while the binding-status question for the historical Node/Fastify freeze and the active G6.9 C+ provisional default remains unresolved. Neither the current code nor the historical freeze should silently supersede the operative main CURRENT/D-064/D-068/D-076 record.

Product and domain work can advance without that selection. The implementation next needs a reviewed APP-11 contract and evidence/scope decision, then a vertical slice joining site/meter/contract evidence, physical schedule assessment, separately scoped settlement claims, human review and replay. Production framework selection and infrastructure adoption remain behind the authority/bake-off decision. No owner decision, Gate closure or field-control authority is inferred here.
