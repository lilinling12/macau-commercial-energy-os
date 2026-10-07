# Logical Architecture Design Baseline

**Status:** Logical boundaries are research-derived draft proposals; product-owner approval is pending. Cloud-core technology remains under G6.9-R2 evaluation. No production framework or runtime is approved by this document.  
**Authority:** G6.8 enterprise deployment and safety boundaries, G6.9-R2 Consolidation Gate, Library v1.6.2, and current handoff.  
**Purpose:** Explain system responsibilities and data/control flow without turning a candidate stack into a production decision.

## Product and operating boundary

```text
Commercial building / site
  Meters · BMS · HVAC/chillers · PV · ESS · EV · other flexible loads
                         |
             site protocols / adapters
                         |
          Site Edge Energy Runtime + Safety Kernel
             local buffering · validation · audit
                         |
              authenticated secure channel
                         |
Cloud Intelligence Plane
  ingestion → Energy Graph → tariff/settlement → analytics
      → forecast/optimization → recommendation/evidence
                         |
             operator review / approval
                         |
       authorized command proposal (only after gates)
                         |
      Edge policy + safety validation → device adapter
```

Cloud analysis and optimization do not directly write to equipment. Edge is the site execution boundary; the Safety Kernel may reject any proposal. Initial product operation is SHADOW/advisory.

## System context and trust boundaries

The following is a logical view for product and architecture review. Boxes are responsibility boundaries, not a mandated microservice or deployment topology. The cloud framework, service decomposition and production runtime remain open under G6.9-R2.

```mermaid
flowchart LR
  Actors["Facilities / operations / finance users"]
  EvidenceSources["CEM tariff rules / site contracts / meter records"]

  subgraph SiteBoundary["Customer site trust boundary"]
    Sources["Meters / BMS / HVAC / PV / ESS / EV"]
    Edge["Site Edge: protocol adapters / local buffer"]
    Safety["Safety Kernel: local policy / veto / audit"]
    Equipment["Device adapters / equipment"]
    Sources --> Edge
    Edge -. "local command validation when enabled" .-> Safety
    Safety -. "only after G6 and site authorization" .-> Equipment
  end

  subgraph CloudBoundary["Cloud platform trust boundary"]
    UI["Operator workspace (framework TBD)"]
    Ingress["Authenticated telemetry ingress / quality"]
    Graph["Energy Graph: physical, electrical and settlement views"]
    Tariff["Tariff and Settlement"]
    Cost["Cost / demand analysis"]
    Intelligence["Forecasting / optimization"]
    Proposal["SHADOW recommendation"]
    Review["Operator review event"]
    Evidence["Evidence / audit / replay"]

    Ingress --> Graph --> Tariff --> Cost --> Intelligence --> Proposal
    Proposal --> UI
    UI --> Review --> Evidence
    Proposal --> Evidence
    Evidence --> UI
  end

  Actors --> UI
  Edge -- "scoped telemetry" --> Ingress
  EvidenceSources --> Tariff
  Proposal -. "future command proposal; G6 + site authorization required" .-> Edge
```

Solid paths show the initial telemetry, analysis, SHADOW and evidence loop. Dashed paths show a possible future command route only; the MVP has no device-write affordance, and a cloud proposal never bypasses the site Edge or Safety Kernel. The diagram does not imply that a particular external contract, tariff source or site connection is already integrated.

## Domain responsibilities

- **Telemetry and provenance:** preserve source, site/tenant, event time, ingestion time, quality, and mapping status.
- **Energy Graph:** keep physical/electrical topology separate from settlement topology; link assets and meters to contracts and tariff versions without making assets own prices.
- **Tariff/Settlement Engine:** resolve meter → contract → tariff version using effective dates and explicit evidence; calculate only when required inputs are known; retain calculation trace and rule version.
- **Cost and demand analysis:** explain bill components and exposure using settled quantities and explicit uncertainty.
- **Forecasting and optimization:** consume versioned, quality-qualified domain data and return proposals with assumptions, constraints, baseline, and expected effect.
- **Evidence and replay:** persist inputs, versions, trace, outputs, and acknowledgements so the result can be deterministically replayed and measured.
- **Command arbitration and Safety Kernel:** separate proposal from authorization and execution; enforce tenant/site scope, freshness, limits, identity, replay protection, audit, and manual/offline behavior.

## Technology authority and decision state

| Layer | Current authority state |
|---|---|
| Product UI | React + TypeScript appeared in the provisional architecture; framework and frontend implementation choice require product-owner review and are not approved. |
| Application core | TypeScript/Go hybrid responsibilities are under evaluation; do not collapse this into a final framework choice. |
| Workflow | Temporal is a candidate; framework-native behavior is part of G6.9-R2 Step 3D. |
| Persistence | PostgreSQL + Timescale is the baseline for evaluation. |
| Eventing | NATS JetStream is a candidate. |
| AI / optimization / forecasting / simulation | Python is a provisional responsibility proposal; model/library/runtime, workload isolation and deployment remain open. |
| Site Edge and safety-critical execution | Go is a provisional responsibility proposal; target hardware, protocols, local storage, updates and key custody remain to be validated. |
| Future plugin isolation | Wasm/WASI direction; outside the first MVP. |
| Cloud-core candidates | A, B, and C+ remain in bake-off. C+ is provisional default, not winner. |
| Existing Node/NestJS code | Candidate B implementation path; not a stack-selection result. |
| Java tariff implementation | D-030 semantic tariff architecture remains relevant; Java/Spring implementation authority is suspended by D-069 pending bake-off or a separately approved boundary. |
| Next.js (conditional public/customer portal UI; not a backend selection) | Report (7) recommends React + TypeScript SPA for the authenticated operator console and says Next.js may serve a public/customer portal or where its server features are useful. Its separate reference to Next.js version-matched docs concerns AI coding context, not this product stack. Next.js is outside G6.9-R2 candidates and is not the selected API/BFF or backend. Assess only if an approved portal/SSR requirement justifies it. |

See `docs/03-architecture/technology-authority/` and the G6.9-R2 bake-off Authority for exact candidate topology and decision rules.

## Historical architecture decisions and current-state reconciliation — 2026-10-07

This addendum separates historical acceptance, later research recommendations, the open G6.9-R2 evaluation, and code that happens to exist. It does not silently supersede an ADR or approve the production architecture.

| Source/time | Evidence | Status and effect |
|---|---|---|
| G7.6 Step 2 detailed engineering-foundation archive (the separately named `(1)` package) | `TECH_STACK_FREEZE.md` and ADR-072/073/074/076 record React 19.3 + TypeScript 6 + Vite 8; Node 24 + Fastify 5; PostgreSQL 18 initially, with Timescale/dedicated TSDB deferred until pilot evidence; NATS + JetStream; Python 3.14; Go 1.27; and no direct cloud equipment control. It says the authenticated MVP portal has no SSR requirement. | Historically accepted Step 2 baseline. The archive is not a complete canonical ADR set on current `main`; later G6.9 reopened the cloud-core comparison. Preserve it as prior authority until a valid superseding decision is recorded. |
| G7.8 Step 2/3 archives | Step 2 proposes React/TypeScript, TypeScript cloud responsibilities, Go Edge, Python optimization and OpenAPI/JSON Schema. Step 3's ADR-TECH-001 accepts broad language/boundary direction; its companion `BACKEND_FRAMEWORK_DECISION.md` says to start with Fastify. | Accepted historical direction, with framework detail clearer in the companion record and G7.6 ADR-072. It does not decide the later G6.9 bake-off. |
| Deep Research report (6), 2026-10-02 | Recommends Candidate C+ before the bake-off: thin Bun/Hono/TypeScript product surface, authoritative Go Energy Core, Temporal Go workers, Go Edge/Safety and Python intelligence. | Research recommendation, not a measured result or owner-approved supersession. |
| Deep Research report (7), 2026-10-02 | Recommends React/Vite SPA for the authenticated operator UI; Node LTS + NestJS modular-monolith API/control plane; Go cloud data plane and Edge; Python intelligence. Allows Next.js conditionally for a public/customer portal or valuable server-side UI features. | A materially different research recommendation from report (6), not a decision record. The report does not choose Next.js as backend or as the operator-console framework. |
| G6.9-R2 current authority on `main` | Steps 3A–3C are recorded complete; Step 3D framework-native integration/failure comparison remains pending. Candidate A (Bun/Hono/Effect), B (Node/NestJS/Fastify), and C+ (Go core + thin Bun/Hono surface) remain in the bake-off; C+ is provisional hypothesis only. | Current selection process controls. No measured winner or owner-approved supersession of the G7.6 historical baseline is evidenced. |
| Current `main` implementation bootstrap | `implementation/platform-api/package.json` pins Node 24.21.x and NestJS 12.0.3 with `@nestjs/platform-express`; it does not use Fastify. That package has no PostgreSQL, Timescale or NATS client dependency. | Implemented bootstrap/deviation evidence, not a production selection or proof that those infrastructure systems are integrated. It does not match the historical Fastify adapter or Candidate B's Fastify variant. |

### Technology status ledger

| Technology / boundary | Evidence-based status now | What is not established |
|---|---|---|
| React + TypeScript | Historical G7.6 accepted UI baseline and repeated in later research; React/Vite SPA is report (7)'s operator-console recommendation. | Current product-owner approval, final visual direction and complete production UI scope. |
| Next.js | Conditional public/customer portal or useful server-side UI option in report (7); not in the G6.9 candidate set. The report's AI-coding documentation mention is not a stack recommendation. | Backend/API selection, operator-console selection, or a requirement to adopt it. |
| Node + Fastify | Historically accepted in G7.6 and named by the G7.8 companion; Candidate B later tests NestJS/Fastify. | Current winner; Step 3D and Step 4 remain open. |
| Node + NestJS + Express | Present in the current API bootstrap. Report (7) favors NestJS generally, while current implementation uses Express adapter. | Approval as the production stack; equivalence to the Fastify bake-off candidate. |
| Bun + Hono | Candidate A's application surface and C+'s thin product/BFF surface. | Production suitability or winner; Step 3D remains unrun. |
| Go authoritative Energy Core | C+ and report (6) recommendation. Go Edge is a separate, consistently proposed responsibility. | Selection of C+, or proof that Go must own cloud domain authority. |
| Temporal | G6.9 candidate and workflow-runner comparison item; TypeScript/Go worker choices depend on candidate topology. | Adoption, operational fit or a deployed workflow service. |
| PostgreSQL + Timescale | Current G6.9 evaluation baseline; report (6) also recommends it. | Superseding G7.6's PostgreSQL-only initial system-of-record decision, or evidence that Timescale is required for the first pilot. |
| NATS JetStream | G7.6 historically accepted; current G6.9 layer summary calls it a candidate. | Current adoption or production integration. |
| MQTT 5 | A protocol candidate in the pinned G6.9 Step 3D comparison and report (7)'s Edge/cloud recommendation. | A deployed broker/transport choice or a verified first-site integration. |
| Python | Historical/research-supported intelligence, forecasting and optimization responsibility; report (7) explicitly recommends it for those workloads. | Specific model/solver, service topology, isolation or production deployment. |
| Go Edge / Safety Kernel | Consistent research and historical responsibility direction; no direct cloud device write in the MVP. | Site hardware/protocol validation, field-control authorization or G6 closure. |
| Wasm/WASI | Future plugin-isolation direction in the provisional layer summary. | MVP requirement, runtime choice, plugin API or implementation commitment. |

The conflict is therefore not “Next.js versus backend.” It is the unresolved cloud application/core topology: the TypeScript/NestJS proposal in report (7), report (6)'s Go-authoritative C+ proposal, the earlier Fastify baseline, the current NestJS/Express bootstrap, and the still-open G6.9 comparison. Keep these states distinct; only a documented owner-approved supersession after the required evidence can resolve them.

## Principal data and control flow

1. Receive telemetry with tenant/site identity, source timestamps, quality, and provenance.
2. Resolve records against the Energy Graph; reject cross-tenant or unmapped data rather than guessing.
3. Resolve applicable contract and tariff version for the meter and time interval. Unknown or conflicting tariff inputs fail closed.
4. Produce cost analysis and forecasts with source coverage and uncertainty.
5. Generate shadow recommendations from a versioned optimizer and compare to an explicit baseline.
6. Store an Evidence Record and deterministic replay inputs.
7. If a later gate authorizes control, convert a proposal into a scoped command; Edge revalidates freshness, identity, policy, and local safety before any device write.
8. Record acknowledgement and physical effect separately; retries must not create duplicate physical writes.

## Logical runtime view for review

This view makes runtime responsibilities and trust boundaries concrete enough for product-owner and engineering review. It describes logical runtime groups, not a one-process-per-box mandate. Candidate A/B/C+ may group the cloud responsibilities differently; deployment, provider, region and shared/dedicated/private mode remain open.

```mermaid
flowchart LR
  Browser["User browser / product UI<br/>React + TypeScript proposal; not approved"]
  API["Authenticated product API / BFF<br/>framework and placement TBD"]
  Core["Energy application core<br/>identity scope · graph · tariff/cost<br/>recommendation · review · evidence"]
  Ingest["Authenticated telemetry ingress<br/>producer and site authorization"]
  RawCapture[("Durable raw capture<br/>logical store; physical placement TBD")]
  Bus["Event transport<br/>NATS JetStream candidate"]
  Workflow["Durable workflow orchestration<br/>Temporal candidate"]
  Workers["Domain workers<br/>TS/Go candidate responsibilities"]
  AI["Forecast / optimization jobs<br/>Python responsibility; execution mode TBD"]
  DB[("Operational + time-series persistence<br/>PostgreSQL + Timescale baseline for evaluation")]
  Evidence[("Durable evidence / artifact persistence<br/>physical store, immutability and retention TBD")]
  Edge["Site Edge agent<br/>Go responsibility proposal<br/>protocol adapters · bounded local buffer"]
  Site["Meters / BMS / approved read-only sources"]
  Safety["Future local Safety Kernel<br/>no MVP device-write path"]
  Device["Equipment write boundary<br/>only after G6/G7 + site authorization"]

  Browser -->|"authenticated HTTPS"| API
  API -->|"authorized scoped use cases"| Core
  Site --> Edge
  Edge -->|"authenticated scoped telemetry"| Ingest
  Ingest -->|"authorized submission payload + receipt metadata"| RawCapture
  RawCapture -->|"publish only after durable capture"| Bus
  Bus --> Workers
  Workers -->|"canonical event / quality / mapping"| DB
  DB --> Core
  Core --> DB
  Core --> Evidence
  Core --> Workflow
  Workflow --> Workers
  Workers --> AI
  AI -->|"versioned proposal inputs/results"| Core
  Core -.->|"future proposal only; G6/G7 and site authorization"| Edge
  Edge -.-> Safety
  Safety -.-> Device
```

The browser is untrusted; API authentication does not itself establish a tenant/site grant. The application core must enforce scope in synchronous requests and in persisted/queued work. Event-bus payload fields do not establish producer identity. Telemetry acceptance order is explicit: authenticate and authorize the producer, durably capture the original payload and receipt metadata, and only then issue an application-level capture receipt or publish downstream. Protocol/broker acknowledgements are tracked separately and may count as RAW_DURABLE only when that broker is explicitly the authoritative raw store and its persistence, failover and recovery are verified. If the authoritative raw capture cannot be made durable, apply backpressure and do not issue the application capture receipt. Normalization and downstream publication retain a reference to that raw record. Logical data authorities, durability/transaction requirements, tenant scope, recovery, replay lineage and schema-evolution policy are drafted in the [Data Persistence and Schema Evolution Detailed Design](detailed-design/DATA-PERSISTENCE-AND-SCHEMA-EVOLUTION-DETAILED-DESIGN-v0.1.md); physical raw/evidence stores, transaction mechanism, and retention remain undecided. The design must recover a crash between durable capture and event publication: pending captures need a discoverable/replayable publication path, and consumers must tolerate redelivery under the still-open event-identity policy. An outbox or equivalent mechanism is a design candidate, not selected. Do not claim exactly-once delivery. Derived evidence writes must likewise be durable before the system reports a completed material result.

| Logical runtime group | Responsibility / proposed boundary | Deployment decision still open |
|---|---|---|
| Browser experience | Present onboarding, evidence, cost-analysis and SHADOW review workflows; no direct device authority. React + TypeScript is a proposal only. | Framework, hosting, localization, supported browsers and responsive/accessibility acceptance after owner and user review. |
| Product API and application core | Authenticate, resolve authorization context and execute scoped product use cases. Preserve domain boundaries for Energy Graph, settlement, cost, recommendation and evidence. | Candidate A/B/C+ determines framework/process grouping after Step 3D/4; do not turn every module into a service by default. |
| Telemetry ingress and async transport | Authenticate producer identity, validate source/site/point binding and persist accepted/rejected raw evidence before downstream processing. Broker decouples ingest only if measured workloads/failure needs support it. | NATS JetStream is a candidate, not a requirement; transport, acknowledgement and replay semantics depend on connector and Step 3D evidence. |
| Workflow and domain workers | Run long-lived/retried business workflows with explicit state, idempotency and tenant/site scope. | Temporal is a candidate; runner persistence is still a Step 3D owner decision. Worker language/process placement follows candidate evidence. |
| AI/forecast/optimization jobs | Produce versioned, bounded SHADOW proposals with assumptions, constraints, uncertainty and evidence refs; no authority to change tariff truth or invoke field writes. | Python is the proposed responsibility boundary; model/solver/provider, isolation and execution mode remain open. |
| Persistence and evidence | Keep operational/series data distinct from immutable or append-only evidence semantics; preserve versioned lineage and tenant scope. | PostgreSQL + Timescale is the evaluation baseline; evidence object store, canonical digest, retention, region, backup and deployment mode remain open. |
| Site Edge | Authenticate and scope telemetry, buffer only under approved policy, report source/device health. In the MVP it has no device-write path. | Go is the responsibility proposal; target hardware, protocols, local store, update/support model and key custody require site/security evidence. |
| Safety Kernel and device adapter | Future local veto, limits, manual/offline behavior and command replay protection; separate proposal from acknowledgement and measured physical effect. | Outside current MVP; command authority, hardware/key design and every field integration require G6/G7 closure and explicit site/customer authorization. |

### Runtime review boundary

Review this view as responsibilities and trust boundaries. The owner may revise the product/authority boundary. Do not approve production containers, provider, region, HA topology, datastore split, protocol, cryptographic mechanism or microservice count from this diagram. Those need the selected product scope, G6.9-R2 evidence, deployment context, security review and operational targets.

## Macau-specific settlement constraint

Grid-connected PV export and the generator's feed-in settlement must be represented independently from another building customer's retail meter and bill. The amended public electricity-supply concession contract effective 2026-01-01 contemplates distribution of privately generated electricity only within the same concession/private land parcel and with prior written SAR authorization; model this only as a distinct, explicitly authorized physical distribution relationship. It does not establish cross-parcel allocation or retail bill credit. Do not allocate remote PV generation as customer bill credit unless the applicable contract, regulatory permission, meter topology, and CEM settlement evidence establish that right. U-025 remains open.

## Deployment and trust boundaries

- Model tenant and organization hierarchy explicitly; enforce isolation in APIs, events, storage, workflows, and Edge identity.
- Treat cloud-to-site messages as authenticated, scoped, versioned, expiring, and replay-protected.
- Make Edge behavior safe during cloud/broker outage; buffer telemetry where allowed and reject unsafe or stale commands.
- Preserve immutable audit/evidence needed to explain tariff results and command outcomes.
- Keep service/module boundaries aligned with domain and failure boundaries; do not require each logical module to become a separate microservice.
- Shared, Dedicated, and Private deployment modes are product/operations options from G6.8; their isolation, upgrade, and support costs require explicit engineering decisions.

The future command path is detailed in `docs/03-architecture/detailed-design/COMMAND-ARBITRATION-AND-EDGE-SAFETY-KERNEL-DETAILED-DESIGN-v0.1.md`. That proposal preserves the SHADOW-only MVP boundary; it selects no runtime or signing mechanism and provides no G6 closure evidence.

## Security threat model

The stack-neutral STRIDE threat register, assets, trust boundaries, architecture invariants and required verification scenarios are in `docs/03-architecture/detailed-design/SECURITY-THREAT-MODEL-v0.1.md`. It is a review draft; threat likelihood/impact scoring, owner risk acceptance, deployment-specific controls and G6 closure evidence remain outstanding.

## Architecture decisions still open

1. G6.9-R2 Step 3D pinned integrations and fault-injection results.
2. Step 4 candidate decision under the bake-off hard gates and published decision rule.
3. G1 real bill/measurement evidence that finalizes bill-grade tariff semantics.
4. G2/G3 evidence that fixes in-scope asset and Energy Graph semantics.
5. G7.2 live R0 baseline/no-op and U-017 response/rebound evidence before field-control claims.
6. Product deployment and commercial model after segment and pilot discovery.

Any implementation proposal must identify which of these decisions it depends on and remain replaceable where the authority is still provisional.
