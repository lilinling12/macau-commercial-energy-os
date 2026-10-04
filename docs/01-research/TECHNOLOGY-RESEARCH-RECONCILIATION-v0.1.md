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
