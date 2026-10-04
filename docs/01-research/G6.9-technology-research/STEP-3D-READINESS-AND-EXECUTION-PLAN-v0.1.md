# G6.9-R2 Step 3D Readiness and Execution Plan v0.1

**Status:** Preflight review complete; Step 3D not executed.
**Reviewed:** 2026-10-04 (Asia/Shanghai).
**Inputs:** User-provided stack bake-off archives v0.2.0 and v0.3.0; repository G6.9 authority; current task-host tool inventory.
**Authority:** G6.9-R2 decision rule and experiment pack are controlling. This document does not select a stack.

## 1. Finding

The v0.3.0 archive is a Step 3C semantic-slice pack. It is not evidence that Step 3D pinned framework-native integration or comparative candidate testing has run.

The archive's own README says Step 3D must implement A/B/C+ against the common vertical slice in a pinned integration runner, then execute acceptance, clean-worktree hidden regression/security checks, runtime/load/chaos/24-hour soak, and controlled AI engineering trials.

The machine-readable draft at `docs/01-research/G6.9-technology-research/STEP-3D-RUNNER-MANIFEST-v0.1.json` records the current pin candidates and explicit freeze blockers. It is not an executable Compose file and does not make the runner ready.

The v0.3.0 archive contains Step 3C scripts, candidate semantic-slice examples, contracts, and Step 3C outputs. The archive listing contains no Step 3D result directory, no shared compose/runner manifest, and no dependency lockfiles for the TypeScript candidates. Its infra directory contains a README listing services but no executable environment definition.

## 2. Evidence reviewed

### v0.2.0 to v0.3.0

The v0.2.0 archive contains the bake-off specifications, contracts, candidate stack descriptions, protocol corpus, and pack validator. The v0.3.0 archive adds semantic-slice source and recorded Node/Go/Python outputs for the Step 3C run. This is a meaningful increase in executable semantic evidence, but it does not cover the native candidate frameworks or shared infrastructure.

### Provided archive revalidation (2026-10-04)

The user-provided `macau-energy-os-stack-bakeoff-v0.2.0.zip` and `macau-energy-os-stack-bakeoff-v0.3.0.zip` were rechecked on the current host. Archive SHA-256 values:

- v0.2.0: `189377f4d7757532b310e82db729fd22a580147c3aac7d5d0059fa63736a8389`
- v0.3.0: `b8825e9e93ce3ab612da71701a0712cf9a94c37c3861724a1716d01b47e6767b`

The included `scripts/validate_pack.py` passed for both archives. This pack-only validator verifies required-path presence, parses selected JSON files, and prints hashes for those required files; it does not execute candidate code or establish Step 3C/3D runtime correctness.

The v0.2.0 archive has 38 non-directory entries and v0.3.0 has 67. A full SHA-256 comparison found 29 files added, one removed (a precompiled Go command-verifier binary), and three modified (`README.md`, `spec/VERTICAL-SLICE.md`, `VERSION`). All other overlapping files are byte-identical. The added files include the Step 3C source and recorded outputs; the archive still has no Step 3D runner/results or TypeScript candidate lockfiles.

The host was rechecked: PATH-default Node v22.20.0, Python 3.11.9, and NVM-installed Node v24.9.0 are present; Docker/Compose, Bun, and Go are unavailable on PATH. The exact proposed Step 3D Node pin is 24.21.0, so the installed 24.9.0 does not satisfy it. The required Step 3D execution cannot run on this host as currently provisioned. No Step 3C or Step 3D runtime experiment was run during this revalidation.

### Step 3C environment and scope

The v0.3.0 Step 3C record states that the run used Node 22.16.0, Go 1.23.2, and Python 3.13.5; Bun and Docker were unavailable. It explicitly says MQTT, Postgres/Timescale, Temporal, Hono/Effect, and NestJS/Fastify were not run. The result is semantic conformance evidence for available shells, not a framework winner or performance comparison.

The Step 3C result reports deterministic Node/Go aggregate and proposal equality, tenant rejection, duplicate suppression, signed command acceptance, and crash/replay recovery without duplicate field writes. It also states that this is not a substitute for the 100-kill Temporal recovery gate.

Node version clarification (official release status checked 2026-10-04): Node 22.16.0 is only the historical Step 3C runner version, not the Step 3D pin. Node 22 is not EOL: the official release schedule lists 22.x as Maintenance LTS through 2027-04-30, and Node 22.23.3 was published 2026-09-23. Node 24 is the v0.3.0 pack's required LTS line for Candidate B and Candidate A's Temporal TypeScript worker; as of this check, 24.x is Active LTS, 24.21.0 is the latest patch (2026-09-09), and the schedule moves it to Maintenance LTS on 2026-10-20 with EOL 2028-04-30. Node 26 is still Current on 2026-10-04 and is scheduled to enter Active LTS on 2026-10-28. Temporal's TypeScript SDK supports Node 20, 22 and 24 and recommends Active LTS for SDK development. Therefore, keep Node 24.21.0 as the reproducible Step 3D experiment pin because that is what the v0.3.0 candidate spec requires and it is an LTS release; this is not a production-runtime decision. At the actual runner freeze, recheck the latest compatible patch and support phase. Do not silently change the major line to Node 22 or 26: any candidate-major change requires an authority update, refreshed lockfiles, and a comparable rerun of all candidates. Keep Candidate A's Bun service and Node Temporal worker as separate runtimes.
- Node.js release status and schedule: https://nodejs.org/en/about/previous-releases and https://github.com/nodejs/Release#release-schedule
- Node.js 22.23.3 release: https://nodejs.org/en/blog/release/v22.23.3
- Node.js 24.21.0 release: https://nodejs.org/en/blog/release/v24.21.0
- Temporal TypeScript SDK supported Node versions: https://github.com/temporalio/sdk-typescript

Sources:
- Node.js releases: https://nodejs.org/en/about/previous-releases
- Node.js 24.21.0 release: https://nodejs.org/en/blog/release/v24.21.0
- Temporal TypeScript SDK supported Node versions: https://github.com/temporalio/sdk-typescript

### Task-host preflight

A refreshed read-only inventory on 2026-10-04 confirmed PATH Node v22.20.0, Python 3.11.9, and NVM Node v24.9.0 at D:\\dev\\nvm\\v24.9.0\\node.exe. Bun, Go, Docker and Docker Compose remain absent; the host is Windows 10.0.26200 AMD64, and WSL reports no installed Linux distribution. The required Node 24.21.0 pin is not installed. This host therefore cannot satisfy the pinned Linux x86-64 Step 3D runner requirements locally. No Step 3D command, application test, benchmark, software installation or environment mutation was performed.

### GitHub Actions execution-host fit and run-host decision

The repository's ordinary GitHub Actions workflows cover short repository checks; they are not the Step 3D experiment host. The bake-off requires all candidates to use the same Linux x86-64 runner and complete a 24-hour mixed-load soak. The experiment must preserve that same host and its resource envelope across the comparison.

| Execution option | Fit to the bake-off | Security / evidence limits | Disposition |
|---|---|---|---|
| Standard GitHub-hosted runner | Each job is capped at 6 hours; splitting the soak into separate jobs would not preserve the same VM or process state. | GitHub-hosted VMs are clean and ephemeral, which is useful for normal CI. | Not suitable for the required continuous 24-hour job. |
| Persistent self-hosted runner attached to this public repository | The documented job limit is 5 days, so duration fits. | GitHub warns self-hosted runners should almost never be used for public repositories: arbitrary PR code can compromise a persistent host. | Reject for this experiment. |
| One-job ephemeral / JIT Actions runner | The 5-day self-hosted job limit fits the soak; GitHub recommends ephemeral runners and says each receives at most one job. | Hardware must actually be clean for every run; forward runner logs externally before destruction. A job longer than 24 hours also outlives the effective GITHUB_TOKEN lifetime, so artifact upload and all GitHub API actions must not depend on that token after expiry. | Conditional alternative only behind an owner-controlled dispatch path, one-job isolation, no customer/production secrets, external log capture, and a verified result-export route. |
| Owner-controlled disposable Linux VM, detached from PR automation | Can preserve one fixed Linux x86-64 host for setup, candidate runs, and the soak without hosted-job duration limits. | Requires owner-approved resource budget, exact pinning, access restriction, controlled build inputs, and an auditable way to export raw evidence; the VM must be destroyed or rebuilt from a clean image after the experiment. | **Preferred for review**, subject to owner approval of cost, operator, network policy, image/build inputs, and evidence retention. |

**Recommendation (not approval):** provision a dedicated, disposable Linux x86-64 VM for a single controlled Step 3D run, triggered manually after the manifest is frozen. Do not expose its credentials or private network to public pull-request code. Fetch only the reviewed commit and pinned inputs; record host identity, resource limits, image digests, logs, raw measurements, and result hashes; export evidence through a separately controlled path; then destroy the VM or return it to a verified clean image. If the owner prefers Actions orchestration, use a protected one-job JIT runner and explicitly solve token expiry and external runner-log retention before freezing the run.

This is a test-execution recommendation, not a production deployment or architecture decision. No provider, spend, runner, network access, or experiment has been approved or provisioned.

Official sources (rechecked 2026-10-04): [Actions limits](https://docs.github.com/en/actions/reference/limits) (six-hour GitHub-hosted and five-day self-hosted job limits); [self-hosted runner security and ephemeral lifecycle](https://docs.github.com/en/actions/reference/runners/self-hosted-runners) (one job per ephemeral runner, recommendation to retain external runner logs); [secure use for public repositories](https://docs.github.com/en/actions/reference/security/secure-use) (risk of untrusted PR code on self-hosted runners); [GITHUB_TOKEN lifetime](https://docs.github.com/en/actions/concepts/security/github_token) (self-hosted jobs may run five days, but token refresh is limited to 24 hours).


## 3. Required Step 3D environment

Build one reproducible Linux x86-64 runner shared by all candidates. Before execution, record:

- exact OS image and architecture, CPU/memory/disk limits, kernel, and clean-runner procedure;
- exact runtime/framework versions and immutable image digests where available;
- dependency lockfiles and package-manager versions;
- shared PostgreSQL 18 + TimescaleDB, Temporal, NATS JetStream, MQTT 5, OpenTelemetry Collector, metrics/Grafana, and pinned BOPTEST v0.9.0 profile;
- BOPTEST source/build provenance: release tag/commit, build context digest, all base-image digests, OS package snapshot, exact Node/Conda/Python/pip dependencies, external Spawn artifact checksum, and resulting web/worker image digests;
- service configuration, health checks, startup order, reset/cleanup procedure, and test-data isolation;
- benchmark commands, workload seeds, warm-up and run duration, repeat count, measurement collection, and raw-result retention;
- candidate commit SHAs, contracts/schema hashes, generated bindings, and exact AI agent/model/tool versions for controlled trials.

The versions named by the archive are inputs to verify and pin; do not silently substitute a newer runtime or service. Record deviations and rerun all candidates on the same environment if any pin changes.

### BOPTEST v0.9.0 buildability and pinning boundary

The official v0.9.0 release is a signed source tag at commit `9b1610b`; its documented local deployment builds the web and worker services from source instead of prescribing a single immutable v0.9.0 service image. In the tagged build recipe, the web image starts from `ubuntu:focal` and installs Node through the moving NodeSource `setup_16.x` channel. The worker pins its Miniconda installer URL but then updates Conda, requests Python `3.11` without a patch pin, upgrades pip/setuptools, and installs a requirements file. The tag therefore pins model/application source but does not, by itself, freeze the full simulation runtime.

For a repeatable Step 3D run, build BOPTEST from the exact signed tag in a controlled builder, pin base images and all OS/runtime/package sources, checksum the external Spawn archive, and retain the resulting web/worker image digests plus build logs. If those inputs cannot be frozen without changing the upstream model/build semantics, record that deviation and the precise patch; do not describe a source-tag-only build as an immutable runner.

Official sources:
- BOPTEST v0.9.0 signed source release: https://github.com/ibpsa/project1-boptest/releases/tag/v0.9.0
- Official local deployment Compose at the v0.9.0 commit: https://github.com/ibpsa/project1-boptest/blob/9b1610b/docker-compose.yml
- Web build recipe: https://github.com/ibpsa/project1-boptest/blob/9b1610b/service/web/Dockerfile
- Worker build recipe: https://github.com/ibpsa/project1-boptest/blob/9b1610b/service/worker/Dockerfile

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
| Shared database | `timescale/timescaledb:2.30.2-pg18` | Official image tag exists; its published image metadata reports PostgreSQL 18.6 and TimescaleDB 2.30.2. Proposed Linux x86-64 platform digest must still be captured at runner freeze. |
| Shared workflow service | Temporal Server 1.32.0 (`temporalio/server:1.32.0`) | Official image tag exists. This is only the server binary image; select and configure its persistence backend, schema setup/migrations, namespace bootstrap, and health checks before a runner can start it. Avoid assuming the deprecated/legacy auto-setup image is a complete production-like runner. |
| Temporal persistence database (runner proposal) | Dedicated PostgreSQL 16 service shared by all candidates | Temporal's official persistence page says PostgreSQL 12+ is available for modern server versions, but its active pre-release test matrix lists PostgreSQL 13.18, 14.15, 15.10 and 16.6—not 18. That is not evidence PG18 is incompatible; it means PG18 has no positive active-test evidence in this matrix. PostgreSQL 16.15 is the latest supported PG16 patch at the 2026-10-04 check date; it is in the actively tested major line but is not the exact 16.6 patch listed by Temporal. Recommend PG16.15 as a test-only Temporal service, separate from the candidate application PostgreSQL 18 + TimescaleDB, then validate schema bootstrap, workflow persistence and restart/replay in the pinned runner. This remains an owner-approved runner-topology decision and does not choose production persistence. |
| Shared event service | NATS Server 2.15.0 | Official stable release (Sep 17, 2026); includes JetStream. Pin image digest and record configuration. |
| MQTT 5 broker | Eclipse Mosquitto 2.1.2 (`eclipse-mosquitto:2.1.2-alpine`) | Proposed common MQTT 5 broker; the Docker Official Image documents MQTT 5 support and this exact tag. Decide auth/TLS, persistence, listener, and test-network policy, then capture the platform-specific digest at runner freeze. |
| Telemetry collection | `otel/opentelemetry-collector-contrib:0.162.0-amd64` | Official 0.162.0 release and Linux x86-64 tag are visible; freeze the exact distribution, verify required receivers/exporters, and capture its immutable digest. |
| Metrics dashboard | `prom/prometheus:v3.15.0` + Grafana 13.2.3 version candidate | Prometheus image tag is visible. Grafana 13.2.3 package/release is available, but the exact OSS/Enterprise container reference and its license/features are not yet frozen; verify that image before writing Compose. |

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
- TimescaleDB 2.30.2 release: https://github.com/timescale/timescaledb/releases/tag/2.30.2
- TimescaleDB official Docker tags and PostgreSQL 18.6 image metadata: https://hub.docker.com/r/timescale/timescaledb/tags
- Temporal Server 1.32.0 release: https://github.com/temporalio/temporal/releases/tag/v1.32.0
- Temporal Server 1.32.0 image tag: https://hub.docker.com/r/temporalio/server/tags
- Temporal Admin Tools 1.32.0 image tag: https://hub.docker.com/r/temporalio/admin-tools/tags
- Temporal UI 2.54.1 image tag: https://hub.docker.com/r/temporalio/ui/tags
- Temporal persistence support and tested PostgreSQL versions: https://github.com/temporalio/documentation/blob/main/docs/encyclopedia/temporal-service/persistence.mdx
- PostgreSQL Project — 16.15 release notes (2026-08-13): https://www.postgresql.org/docs/16/release-16-15.html
- Temporal official PostgreSQL Compose sample and version pins: https://github.com/temporalio/samples-server/blob/main/compose/.env
- Temporal official PostgreSQL schema setup: https://github.com/temporalio/samples-server/blob/main/compose/scripts/setup-postgres.sh
- NATS Server 2.15.0: https://github.com/nats-io/nats-server/releases/tag/v2.15.0
- NATS official image tags: https://hub.docker.com/_/nats/tags
- OpenTelemetry Collector 0.162.0: https://github.com/open-telemetry/opentelemetry-collector-releases/releases/tag/v0.162.0
- OpenTelemetry Collector Contrib 0.162.0 linux/amd64 image tag: https://hub.docker.com/layers/otel/opentelemetry-collector-contrib/0.162.0-amd64/images/sha256-340885ab6f46822374f00c58c067396b53b8d612559842e8821585567579d9e3
- Mosquitto official image and MQTT 5 support: https://hub.docker.com/_/eclipse-mosquitto
- Prometheus 3.15.0: https://github.com/prometheus/prometheus/releases/tag/v3.15.0
- Grafana 13.2.3: https://github.com/grafana/grafana/releases/tag/v13.2.3
- Grafana official Docker tags: https://hub.docker.com/r/grafana/grafana/tags

Before freeze, confirm image availability, cross-component compatibility, security advisories, and actual package-level pins. Any selected older version needs a recorded compatibility or stability reason. The application database image check is satisfied by the official `2.30.2-pg18` image metadata (PostgreSQL 18.6 + TimescaleDB 2.30.2); the MQTT broker is provisionally named as Mosquitto 2.1.2. Temporal's `temporalio/server:1.32.0` image tag is verified. Current Temporal docs actively test PostgreSQL 13–16, and the current official sample configuration pins PostgreSQL 16. The v0.3.0 pack's `infra/README.md` explicitly requires PostgreSQL 18 + TimescaleDB and a Temporal dev/prod-equivalent service, and says candidates may not substitute a different database, broker or workflow engine. It does not specify Temporal's persistence database version or whether persistence must use the same instance as the candidate application database. Keep PostgreSQL 18 + TimescaleDB as the common candidate application service. A dedicated PostgreSQL 16 persistence service is an additional shared runner service proposal—not a candidate-specific replacement—and remains subject to owner approval before freeze. If that addition is not approved, do not assume PostgreSQL 18 compatibility from the current tested-version list; resolve and document the supported Temporal persistence configuration before execution. Schema setup, namespace bootstrap, server configuration, and health checks remain open execution blockers. Exact versions alone do not make a runner reproducible: retain image digests, lockfiles, resource limits, configuration, benchmark commit SHAs, and raw results.

## 5. Candidate UI-scope finding verified against the supplied v0.3.0 pack

The original v0.3.0 sources expose different levels of UI responsibility:

| Source in the supplied pack | What it specifies | Evidence of the measured UI boundary |
|---|---|---|
| Candidate A `STACK.md` | Bun/Hono/Effect product/API services; the Temporal TypeScript worker stays on Node. | No browser rendering scope. |
| Candidate B `STACK.md` | Node 24, NestJS/Fastify API and worker. | No browser rendering scope. |
| Candidate C+ `STACK.md` | Go authoritative core and Temporal Go, with a thin Bun/Hono/TypeScript product BFF/UI. | BFF/UI wording is broader than the other candidate descriptions and is not tied to common UI tasks. |
| `spec/VERTICAL-SLICE.md` | The canonical flow ends with immutable audit and a “live UI event”. | Specifies an event output, not a browser framework or rendered screen acceptance. |
| `tasks/T01-telemetry-quality.md` | Adds a telemetry quality state through persistence, API contract, aggregate filtering and UI contract. | Tests the UI contract/data shape; it does not define browser rendering. |
| `tasks/T07-live-stream-filter.md` and `spec/METRICS.md` | Tenant/site authorization on live stream/reconnect; a reference live-stream push metric. | Tests stream/API behavior, not browser UI implementation. |
| `spec/AI-ENGINEERING-TRIALS.md` and `spec/METRICS.md` | Scores time-to-green, hidden tests, review burden, API readiness, HTTP, telemetry ingest, live stream and recovery. | No browser visual, task-usability or frontend implementation metric is defined. |

The separate provisional architecture proposal names React + TypeScript for the browser frontend. It does not amend the pack or make React part of Step 3D.

**Recommended interpretation of the current pack:** keep browser rendering and React framework evaluation outside the G6.9-R2 stack score. Require all candidates to pass the same UI contract, API and live-stream acceptance checks. Clarify whether C+'s “BFF/UI” means only a thin adapter to those same contracts or includes browser UI work; do not give it unscored candidate-specific surface area. This interpretation best matches T01/T07 and the metrics, but must be recorded as an owner-approved clarification/amendment in G6.9-R2 authority before runner freeze.

If the owner wants frontend implementation included in the technology comparison, amend the pack to include equivalent browser workflows for A/B/C+ and separate UI effort/review metrics. Neither interpretation selects the production frontend. React + TypeScript remains a proposal until separately reviewed.

### Next.js backend/API candidate fit — Owner decision #16

Official Next.js documentation confirms that Route Handlers expose server-side HTTP endpoints and describes Next.js backend capabilities as an API/BFF layer, while cautioning that this is not a full backend replacement. Next.js 16 requires Node.js 20.9 or later, so the current proposed Step 3D Node 24.21.0 pin meets its documented minimum. Self-hosting on a Node.js server or Docker is supported, and the App Router supports streaming; however, the full deployment path must preserve chunked/HTTP/2 streaming and avoid proxy buffering. Serverless deployment behavior can impose timeouts and restrictions on persistent connections, so host choice must be pinned and measured.

This establishes **technical plausibility for an API/BFF candidate**, not bake-off compatibility, performance, or production suitability. If Owner decision #16 includes Next.js, define it as an API/backend candidate with the same contract, auth, telemetry/live-stream and workflow acceptance cases; specify whether browser rendering is excluded and whether Temporal runs in a separate authentic Node worker. Pin Next.js/React and lockfiles, and amend the G6.9-R2 experiment authority before runner freeze. If it becomes a fourth candidate and the current per-candidate 10-task × 2-agent × 2-repetition AI trial design remains, the trial count changes from 120 to 160. If it is deferred, record “not assessed” without changing the current A/B/C+ candidate list.

Sources: [Next.js Backend for Frontend guidance](https://nextjs.org/docs/app/guides/backend-for-frontend), [Route Handlers](https://nextjs.org/docs/app/getting-started/route-handlers), [Next.js 16 Node requirement](https://nextjs.org/docs/app/guides/upgrading/version-16), [self-hosting and streaming](https://nextjs.org/docs/app/guides/self-hosting), [platform deployment requirements](https://nextjs.org/docs/app/guides/deploying-to-platforms).

## 6. Ordered execution packet

1. Resolve the candidate UI scope using the source-backed evidence in §5; record whether browser rendering is excluded (common UI contract/API/stream tests only) or added equally to all candidates, then preserve the approved interpretation in G6.9-R2 authority.
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
