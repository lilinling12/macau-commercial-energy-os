# G6.9-R2 Step 3D Readiness and Execution Plan v0.1

**Status:** Preflight review complete; Step 3D not executed.
**Reviewed:** 2026-10-04 (Asia/Shanghai).
**Inputs:** User-provided stack bake-off archives v0.2.0 and v0.3.0; repository G6.9 authority; current task-host tool inventory.
**Authority:** G6.9-R2 decision rule and experiment pack are controlling. This document does not select a stack.

## 1. Finding

The v0.3.0 archive is a Step 3C semantic-slice pack. It is not evidence that Step 3D pinned framework-native integration or comparative candidate testing has run.

The archive's own README says Step 3D must implement A/B/C+ against the common vertical slice in a pinned integration runner, then execute acceptance, clean-worktree hidden regression/security checks, runtime/load/chaos/24-hour soak, and controlled AI engineering trials.

The v0.3.0 archive contains Step 3C scripts, candidate semantic-slice examples, contracts, and Step 3C outputs. The archive listing contains no Step 3D result directory, no shared compose/runner manifest, and no dependency lockfiles for the TypeScript candidates. Its infra directory contains a README listing services but no executable environment definition.

## 2. Evidence reviewed

### v0.2.0 to v0.3.0

The v0.2.0 archive contains the bake-off specifications, contracts, candidate stack descriptions, protocol corpus, and pack validator. The v0.3.0 archive adds semantic-slice source and recorded Node/Go/Python outputs for the Step 3C run. This is a meaningful increase in executable semantic evidence, but it does not cover the native candidate frameworks or shared infrastructure.

### Step 3C environment and scope

The v0.3.0 Step 3C record states that the run used Node 22.16.0, Go 1.23.2, and Python 3.13.5; Bun and Docker were unavailable. It explicitly says MQTT, Postgres/Timescale, Temporal, Hono/Effect, and NestJS/Fastify were not run. The result is semantic conformance evidence for available shells, not a framework winner or performance comparison.

The Step 3C result reports deterministic Node/Go aggregate and proposal equality, tenant rejection, duplicate suppression, signed command acceptance, and crash/replay recovery without duplicate field writes. It also states that this is not a substitute for the 100-kill Temporal recovery gate.

Node version clarification (official release status checked 2026-10-04): Node 22.16.0 is only the historical Step 3C runner version; it is not the Step 3D pin. The v0.3.0 candidate spec calls for Node 24 LTS for Candidate B and for Candidate A's Temporal TypeScript worker. Node.js official releases list 24.21.0 as the latest LTS release published on 2026-09-09; Temporal's TypeScript SDK lists Node 20, 22, and 24 as supported and recommends using Active LTS for development. Therefore, pin Node 24.21.0 for those Step 3D Node processes unless an official compatibility check at environment freeze requires a newer 24.x patch. Do not use a floating "24" tag, and keep Candidate A's Bun service and its Node Temporal worker as separate runtimes.

Sources:
- Node.js releases: https://nodejs.org/en/about/previous-releases
- Node.js 24.21.0 release: https://nodejs.org/en/blog/release/v24.21.0
- Temporal TypeScript SDK supported Node versions: https://github.com/temporalio/sdk-typescript

### Task-host preflight

A read-only inventory on the current task host reported Node v22.20.0 and Python 3.11.9; Docker, Bun, Go, and the Python launcher were unavailable. This host therefore does not satisfy the pack's stated Step 3D runner requirements. No Step 3D command, application test, benchmark, or environment mutation was performed.

## 3. Required Step 3D environment

Build one reproducible Linux x86-64 runner shared by all candidates. Before execution, record:

- exact OS image and architecture, CPU/memory/disk limits, kernel, and clean-runner procedure;
- exact runtime/framework versions and immutable image digests where available;
- dependency lockfiles and package-manager versions;
- shared PostgreSQL 18 + TimescaleDB, Temporal, NATS JetStream, MQTT 5, OpenTelemetry Collector, metrics/Grafana, and pinned BOPTEST v0.9.0 profile;
- service configuration, health checks, startup order, reset/cleanup procedure, and test-data isolation;
- benchmark commands, workload seeds, warm-up and run duration, repeat count, measurement collection, and raw-result retention;
- candidate commit SHAs, contracts/schema hashes, generated bindings, and exact AI agent/model/tool versions for controlled trials.

The versions named by the archive are inputs to verify and pin; do not silently substitute a newer runtime or service. Record deviations and rerun all candidates on the same environment if any pin changes.

## 4. Official release check for Step 3D pin candidates

**Checked:** 2026-10-04. These are proposed exact versions to evaluate and freeze with immutable image digests; they are not final architecture choices or proof of compatibility. The experiment should preserve a version manifest and retrieval date so all candidates use the same shared services.

| Role | Proposed pin candidate | Evidence / remaining check |
|---|---|---|
| Candidate A API/product runtime and packages | Bun 1.4.2 + Hono 4.13.12 + Effect 4.0.0 | Official latest stable package/runtime releases at the check date. Freeze exact packages in bun.lock and verify Bun/platform support in the pinned runner. |
| Candidate A Temporal TypeScript worker | Node 24.21.0 + Temporal TypeScript SDK 1.24.0 | Official Node LTS release; SDK officially supports Node 24. |
| Candidate B API/worker | Node 24.21.0 + NestJS 12.1.1 + Fastify 5.12.5 + Temporal TypeScript SDK 1.24.0 | Official stable releases. Verify adapter compatibility and freeze package lock before running. |
| Candidate C+ core | Go 1.27.1 + Temporal Go SDK 1.49.0 | Official stable releases; freeze all module versions in go.mod/go.sum. |
| Candidate C+ thin BFF | Bun 1.4.2 + Hono 4.13.12 | Keep separate from Go core; freeze packages in bun.lock. |
| Shared optimizer | Python 3.14.8 | Official Python security/maintenance release (Sep 30, 2026); confirm optimizer dependency wheels and runtime compatibility before freezing. |
| Shared database | PostgreSQL 18.6 + TimescaleDB 2.30.2 | Both official current releases at the check date. Verify the official image/extension combination supports PostgreSQL 18, then pin the image digest. |
| Shared workflow service | Temporal Server 1.32.0 | Official stable release (Sep 11, 2026). Pin the matching image and record server/SDK compatibility. |
| Shared event service | NATS Server 2.15.0 | Official stable release (Sep 17, 2026); includes JetStream. Pin image digest and record configuration. |
| MQTT 5 broker | Not selected in pack | The pack requires MQTT 5 but does not name a broker or exact version. Select one common broker, document why, and pin it before the experiment. |
| Telemetry collection | OpenTelemetry Collector 0.162.0 | Official release (Sep 29, 2026); pin distribution and image digest. |
| Metrics dashboard | Prometheus 3.15.0 + Grafana 13.2.3 | Official stable releases found (Sep 2026); verify common dashboard/config and pin image digests. |

Official sources:
- Node.js 24.21.0: https://nodejs.org/en/blog/release/v24.21.0
- Temporal TypeScript SDK Node support: https://github.com/temporalio/sdk-typescript
- Hono 4.13.12: https://github.com/honojs/hono/releases/tag/v4.13.12
- Effect 4.0.0 stable/LTS release: https://github.com/Effect-TS/effect/releases
- NestJS 12.1.1: https://github.com/nestjs/nest/releases/tag/v12.1.1
- Fastify 5.12.5: https://github.com/fastify/fastify/releases/tag/v5.12.5
- Temporal TypeScript SDK 1.24.0: https://github.com/temporalio/sdk-typescript/releases/tag/v1.24.0
- Temporal Go SDK 1.49.0: https://github.com/temporalio/sdk-go/releases/tag/v1.49.0
- Bun 1.4.2: https://bun.sh/blog/bun-v1.4.2
- Go 1.27.1: https://go.dev/doc/devel/release#go1.27.1
- Python 3.14.8: https://www.python.org/downloads/release/python-3148/
- PostgreSQL 18.6: https://www.postgresql.org/docs/current/release-18-6.html
- TimescaleDB 2.30.2: https://github.com/timescale/timescaledb/releases/tag/2.30.2
- Temporal Server 1.32.0: https://github.com/temporalio/temporal/releases/tag/v1.32.0
- NATS Server 2.15.0: https://github.com/nats-io/nats-server/releases/tag/v2.15.0
- OpenTelemetry Collector 0.162.0: https://github.com/open-telemetry/opentelemetry-collector-releases/releases/tag/v0.162.0
- Prometheus 3.15.0: https://github.com/prometheus/prometheus/releases/tag/v3.15.0
- Grafana 13.2.3: https://github.com/grafana/grafana/releases/tag/v13.2.3

Before freeze, confirm image availability, cross-component compatibility, security advisories, and actual package-level pins. Any selected older version needs a recorded compatibility or stability reason. Exact versions alone do not make a runner reproducible: retain image digests, lockfiles, resource limits, configuration, benchmark commit SHAs, and raw results.

## 5. Candidate interpretation that remains open

The archive describes C+ with a thin Bun/Hono/TypeScript product BFF/UI surface while the separate provisional layer summary mentions React + TypeScript. These statements may mean a React frontend plus a Bun/Hono BFF, or they may describe competing UI approaches. The product/frontend boundary is unresolved and must not be silently inferred from the C+ topology. Record the exact API, BFF, and browser UI responsibilities consistently across candidates before treating the comparison as equivalent.

Candidate A also uses Bun for its API/product service while keeping the Temporal TypeScript worker on authentic Node; Candidate B uses Node/NestJS/Fastify; Candidate C+ uses Go core/Temporal Go and a thin TypeScript surface. Compare equivalent user-visible flows and common contracts, not different product scopes.

## 6. Ordered execution packet

1. Resolve the product/API/BFF/browser-UI boundary across A/B/C+ and preserve it as an experiment assumption or approved decision.
2. Create the pinned runner and a machine-readable environment manifest; freeze dependencies, image digests, workload, and resource limits.
3. Validate the experiment pack and verify source/contract hashes. Preserve the validation output as preflight evidence.
4. Implement framework-native vertical-slice integrations for all candidates against the exact same contracts and services.
5. Run the public acceptance suite, then hidden regression/security checks from clean worktrees.
6. Execute broker partition, worker kill/restart, database restart, command replay, backpressure, and offline Edge scenarios; preserve exact audit and field-write evidence.
7. Collect the common performance, resource, startup, load, and soak measurements. Do not compare results from different hosts or pins.
8. Run the 120 controlled engineering trials (3 candidates × 10 tasks × 2 coding agents × 2 repetitions) from equivalent baselines; record code corrections and reviewer burden.
9. Apply the hard gates and decision rule in the pack. Write raw results and the resulting Decision Record; keep C+ provisional until this evidence exists.

The order above reflects the experiment pack. Work items 3–8 have not been performed as part of this preflight.

## 7. Exit criteria and authority status

Step 3D is complete only when all candidates have comparable framework-native integrations and raw evidence for the agreed failure, acceptance, performance, soak, and AI engineering experiments; deviations and failures are preserved; hard-gate status is explicit; and the evidence is reviewed under the published decision rule.

Until then:

- G6.9-R2 Step 3D/4 remains pending;
- C+ remains a provisional default hypothesis, not a measured winner;
- Node/NestJS remains existing Candidate B implementation evidence, not a stack decision;
- no framework or production stack is approved by this readiness review;
- G6 Safety & Control remains OPEN independently of the bake-off.

## 8. Source artifacts

- User-provided archive: macau-energy-os-stack-bakeoff-v0.2.0.zip
- User-provided archive: macau-energy-os-stack-bakeoff-v0.3.0.zip
- v0.3.0 internal references: README.md; VERSION; spec/STEP-3C-RESULT.md; spec/VERTICAL-SLICE.md; spec/METRICS.md; spec/DECISION-RULE.md; spec/AI-ENGINEERING-TRIALS.md; infra/README.md; scripts/validate_pack.py.
- Repository authority: docs/03-architecture/technology-authority/G6.9-technology-selection/README.md and G6.9-R2 decision records D-062..D-076.
