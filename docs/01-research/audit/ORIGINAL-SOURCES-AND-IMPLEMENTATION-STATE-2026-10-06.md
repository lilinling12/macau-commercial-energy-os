# Original Research Sources and Implementation-State Audit — 2026-10-06

**Status:** Evidence inventory and focused cross-check; not a claim that every archived document has received a full semantic review.  
**Repository target:** lilinling12/macau-commercial-energy-os, GitHub default branch and PRs inspected 2026-10-06.  
**Research source folder:** D:\dev\project\lilinling\macau-commercial-energy-os  
**Download sources:** D:\Downloads

## 1. What was actually accessible

### Original conversation

The Codex read_thread call for ChatGPT conversation 6abf4f5c-b2d4-83ea-b189-6534f517c5a1 returned a bounded recent slice: page limit 10, nextCursor null, hasMore false, and five returned turns. The supplied public share URL is now readable in a browser for some messages, but this is not a full export: multiple research cards show `Failed to fetch template`, and only selected prompt jumps have been reviewed. This audit does not claim to have read every assistant response or attachment.

### Local project folder

The named D: project folder contains 44 ZIP packages and two standalone Authority Markdown files, not a Git checkout. A Git status/log request failed with “not a git repository.” A read-only inventory recorded 735 textual entries across those project ZIPs. The broader read-only inventory across the project folder and Downloads recorded 79 ZIPs and 832 text/document entries, including two supplied stack-bakeoff ZIPs and several separately named remote-control research packages. The ZIP manifest/corpus generated during this audit are working evidence in the Codex task workspace; no source archive was modified.

The project folder has no matching files named prototype-v0.10-review.html or palette-study-v0.1.html, and no project SKILL.md. Those two HTML files are present in the Codex task workspace at the paths supplied in this thread; the project-specific UI skill draft is on PR #8, not on main.

This is a complete filename/hash inventory of the selected archive set, not full semantic review of every one of its 735 texts. Focused reads were made of the authority versions, gate CURRENT/NEXT files, both bake-off packages, both Deep Research reports, selected G7.6–G7.9 packages, current GitHub authority and implementation artifacts. Other archive content remains for staged semantic review.

## 2. Source fingerprints

| Source | SHA-256 / identifier | What it supports |
|---|---|---|
| Deep Research report (6), D:\Downloads\deep-research-report (6).md | 1E0118807DBFDCA3D13AE1949383B4CBFEFB80DB0CD867D13BD6C8DC0D744495 | Provisional C+ recommendation before a full bake-off; not a measured winner. |
| Deep Research report (7), D:\Downloads\deep-research-report (7).md | 5DB518CBE85402E0A8AD2682B9E52A7782D17748EC95C60F43B4BB748B6CAC82 | TypeScript-first hybrid recommendation; React SPA + Node/NestJS Control Plane, Go data/Edge, Python intelligence. |
| Local Authority v2.0 Markdown | BD705A40A34DBE9BE1248B6B8BD792913ED92B398A32EC32E42D99829A1B4661 | Says 3A/3B/3C/3E/3F/3G.1 complete, omits 3D, and retains cloud core/framework under evaluation. |
| Local Authority v2.1 Markdown | 93AF2811B278FA7B1099A6F5FBD69A2A9F7B60CD26ECDAABECBC82676524A373 | Says G6.9 and its AI engineering system complete, moves to G7.1; does not reconcile the missing 3D evidence. |
| Research Authority v1.6.2 ZIP | 6559BD62B1617DA046BB5BE64715A5A723144534A62395F7811B20C5B9DE0989 | G1 open; G6.9-R2 3A/3B/3C complete, framework-native Step 3D pending; G7.2 live baseline/no-op pending. |
| Research Authority v1.7.0 ZIP | FB98EE32AADAD185B0CBC18134D5F5576223225EB65853FE7F7F4ABBB2357B84 | Consolidation release still lists framework bake-off evidence/reference implementation pending. |
| Research Authority v1.7.1 ZIP | B23F71BC29B2DB911D3D1612A286A8901B24E5957F20F8953E07A1ABD1204ADB | Recovery status keeps evidence levels explicit; subsequent G7.1/G7.2 research packages record research states, not runtime closure. |
| Stack bake-off v0.2.0 ZIP | 189377F4D7757532B310E82DB729FD22A580147C3AAC7D5D0059FA63736A8389 | Step 3B signed-command conformance: Node and Go passed the common cases; Bun execution was skipped because runtime was unavailable. |
| Stack bake-off v0.3.0 ZIP | B8825E9E93CE3AB612DA71701A0712CF9A94C37C3861724A1716D01B47E6767B | Step 3C semantic slice for available runtimes; framework-native A/B/C integration, common infrastructure, AI trials, chaos/soak and decision rule remain later work. |
| GitHub main CURRENT.md | blob 5b3da3af0a7e267c34a8a743a30cfc89d8fb24ca at main snapshot a897bf0b1e7e6ceea3862d7d87fa288ecca08203 | Active repository mission, gate state, provisional architecture and next work. |

Project-folder archive inventory includes:
- Authority migration v1.0; Authority v1.8/v1.9 and v2.0 recovery, Step 2 mapping, Step 3 architecture, and Step 4 repository-preparation packages.
- Research Authority v1.0–v1.6.2 and small v1.7.0/v1.7.1 snapshots.
- G7.1, G7.2 and G7.4; G7.5 Steps 2/3; G7.6 Step 2 (two different ZIPs), Step 3, Steps 5/6/7; G7.7 Steps 1–5; G7.8 foundation and Steps 2–5; G7.9 foundation and Step 2.
- No separately named G7.3 ZIP was present in the supplied folder. G7.3 material may be inside Authority packages or other source packages; a standalone G7.3 package cannot be confirmed from this inventory.

## 3. Research and gate chronology recovered from package records

| Source/version sequence | Recorded state in that source | Reconciliation |
|---|---|---|
| Research Authority v1.6.2 and matching active main snapshot | G1 OPEN; G6.9-R2 3A protocol/profile, 3B conformance and 3C semantic slice complete; Step 3D framework-native integration pending; G7.2 live baseline/no-op and G7.4 live SAT/CHWS response/rebound still evidence-dependent. | This is the operative state on GitHub main at the inspected revision. |
| Authority v1.7.0/v1.7.1 local recovery snapshots | Consolidation/recovery language, while framework bake-off/final implementation evidence remains pending in v1.7.0. | Does not establish the missing pinned 3D run. |
| Authority v1.8/v1.9 packages | Declare G6.9, G7.1–G7.5 or research/architecture consolidation complete and move toward G7.6/G7.7. | These are historical completion assertions, not proof of the active main 3D evidence gate. |
| G7.6 package family | Step 2 technical freeze/bootstrap, vertical-slice design, MVP bootstrap/implementation plans, then code-skeleton plan. Two Step 2 ZIPs differ materially: 7 entries vs 39 entries and different ADR status. | Do not collapse duplicate package names into a single status. The expanded package records accepted ADRs; the shorter package uses a proposed status. Previous archive semantic review also records the exact SHA distinction. |
| G7.7 Steps 1–5 | Repository foundation, authority import, engineering governance, initialization blueprint and readiness. | Planning/readiness deliverables; actual GitHub repository creation and later merges must be checked separately. |
| G7.8 Steps 1–5 | Foundation, technology selection and a Step 3 Node/Fastify/contract-first ADR-freeze package, repository bootstrap and CI. Step 5 points to G7.9. | The archive's “freeze completed” assertion conflicts with current main's G6.9-R2 Step 3D pending. No main-authority supersession record is present in the inspected CURRENT. |
| G7.9 Step 1 foundation and Step 2 domain/data-contract design | Both local CURRENT files mark their package step complete and point to the next step. Step 2 package says G7.9 Step 3 Service Boundary and Implementation Design is next. | Step 1/2 package completion is not Step 3 completion. |
| Current GitHub PR #8/#10/#14 | PR #8 remains open/unmerged; PR #10 carries product/dispatch, UX and Step 3 design proposals; PR #14 is a bounded SHADOW optimizer experiment. | Current proposals and experiment are not main authority, approved contract, complete MVP, or pilot readiness. PR #10 records G7.9 Step 3 OPEN. |

A later version number is not, by itself, evidence that an earlier open gate was satisfied or formally superseded. The active main CURRENT and D-064/D-068/D-076 are controlling until a reviewed decision changes them.

## 4. Product and UI progression

### Prototype v0.10 and palette study

The supplied v0.10 HTML is a 49,492-byte single-page portfolio/workspace prototype. It opens at “Portfolio overview,” with navigation for site overview, data health, site model, economics, recommendations and evidence/replay. It states values are synthetic and avoids direct-control claims. The physical and settlement models are separated.

However, this version does not make coordinated source/load dispatch the primary operator workflow: its main overview is readiness/energy trend and dispatch is at most implied through recommendations; no end-to-end grid/PV/ESS/flexible-load schedule-comparison flow is evident in the top-level structure. It should be treated as an earlier prototype, not the settled product design.

The supplied palette study presents three unselected visual options (Harbor teal, Mineral blue, Night graphite) on the same portfolio-overview task. Its sample contrast pairs are recorded in the file, but they do not establish full-page WCAG conformance or owner approval. These are palette alternatives, not a selected design system.

### Later source/load dispatch design

The later PR #10 series is a material product correction toward the user's dispatch-first requirement:
- Six-stage workflow: data/contracts → physical site model → schedule comparison → economics/constraints/evidence → SHADOW review → monitoring/replay.
- Later versions add interval source/load schedules, HVAC shift/rebound, ESS SOC, evidence and partial/withheld claim examples.
- v2.6 explicitly labels its four status/evidence examples and its separate fixed schedule example as independent synthetic studies.
- A later v1.9 browser prototype was directly inspected: its dispatch comparison shows grid import, PV, ESS charge/discharge/SOC and HVAC shift/rebound by interval; missing site forecasts block a formal schedule; candidate remains synthetic; the full-window peak is shown as 510 kW vs 485 kW baseline due to rebound; cost/settlement remains unverified.
- The current prototypes remain disconnected from site APIs, optimizer results and field devices. They do not prove localization, operator acceptance, full accessibility, or deployment readiness.

The project-specific UI skill draft exists on PR #8 branch docs/product-architecture-roadmap, blob 133aa421796ad314a1e4678f3d3a65051f532178; PR #8 is open/unmerged. It centers energy source/load coordination, forbids unsupported economic/control claims, requires data-state separation and responsive/accessibility/language review, and says reference work should inform principles rather than be copied. It is not yet active main policy.

## 5. What implementation is actually in GitHub main

Verified on current main:
- PR #2 Phase B is closed and merged at merge commit be28ced3361e7d3994251bc0bf9331a8adb3dc6b. It added Node 24/NestJS platform API, Go Edge bootstrap, Python optimizer package, schemas/fixtures and multi-runtime CI. This proves those runtimes exist in main; it does not settle the conflicting production architecture research.
- PR #4 Phase C is closed and merged at merge commit 83ba35c25b9aa04c80f2f9d592b3b1c6dfed3acb. It added a typed telemetry → Energy Graph → tariff-resolution port → cost → SHADOW recommendation → evidence path and deterministic synthetic replay.
- Main's implementation has an executable code path, but it is a fixture-level slice. The replay adapter hard-codes a synthetic site/meter/contract and MOP cost; the production tariff authority remains a port, not a validated Macau bill engine. The Python main package defines the recommendation boundary and contains no economic dispatch search.
- The main slice is not the later source/load economic dispatch product loop. It has no verified site tariff/meter relationships, optimizer schedule comparison, HVAC/EV/hot-water service model, durable application result/review/replay store, or field control integration.
- Main CURRENT explicitly says NestJS is an implementation path corresponding to Candidate B, not evidence that B won the still-open G6.9-R2 bake-off. C+ is provisional; A/B remain candidates until Step 3D/Step 4 evidence satisfies the common decision rule.
- PR #10 remains Draft/open/unmerged at the latest examined head, carrying the new APP-11 projection proposal, crosswalk and semantic decision packet. PR #14 remains Draft/open/unmerged and is a bounded Python SHADOW search; neither is production implementation or G7.9 Step 3 closure.

## 6. Technology conclusions and unresolved authority

| Technology / question | Source-grounded current status |
|---|---|
| React + TypeScript | Confirmed product surface in main CURRENT and both reports; the operator console recommendation is SPA-style. |
| Next.js | Report (7) says optional when public/customer portal, SSR or server-side UI composition is materially useful. It is not the recommended operator-console backend or a selected project technology. Report (6)'s C+ diagram does not use Next.js. |
| Node/NestJS | Present in Phase B/C main code, Candidate B implementation fact. Report (7) recommends it as a TypeScript Control Plane. Main says this is not a bake-off winner. |
| Node/Fastify | G7.8 archive contains a completed Node/Fastify/contract-first freeze claim; must be reconciled against active G6.9-R2 Step 3D and the v2.0/v2.1 snapshots before treating as binding. |
| Bun/Hono/Effect | Candidate A/challenger in bake-off and report (6); report (6) calls C+ provisional and requires runtime/integration and AI time-to-green evidence. No winner can be inferred from the available-runtime Step 3C shell. |
| Go authoritative core | C+ provisional architecture in report (6) and main CURRENT; framework-native comparative integration is pending. |
| Go Edge | Shared direction and implemented bootstrap; main's Edge entrypoint is logging/startup, not full protocol acquisition/safety runtime. |
| Python | Shared intelligence/optimizer direction; main has a recommendation skeleton, while PR #14 separately has a bounded economic source/load search prototype. |
| Temporal | Candidate/workflow option; report (6) favors Go SDK for C+ while report (7)/G7.8 material differ or retain open deployment choice. No reviewed production workflow deployment decision is established here. |
| PostgreSQL + Timescale | Baseline/initial telemetry store across sources; production schema/migration/deployment still requires authority reconciliation and evidence. |
| NATS JetStream vs Kafka | Report (6) recommends NATS initially and Kafka/Redpanda when justified; report (7) names Kafka as target path but not required in month one. Main CURRENT calls NATS a candidate. They are not interchangeable frozen decisions. |
| MQTT 5 | Edge-to-cloud/site transport direction in both reports; protocol, identity, deployment and field gateway still require site validation. |
| Wasm/WASI | Future plugin-isolation direction in the user-supplied provisional layer summary and research; not MVP implementation evidence. |
| Java | Historical D-030 tariff semantic implementation choice existed, but main CURRENT says Java Phase D is suspended by D-069 while G6.9-R2 remains open. Tariff semantics remain relevant; Java is not the current MVP default. |

### Specific Next.js conclusion

The reports do not say “Next.js is the backend.” Report (7) explicitly recommends React + TypeScript SPA for the authenticated operator console; it lists Node/NestJS as the API/Control Plane. It suggests Next.js only when SSR, public/customer portal requirements, or server-side UI composition materially help. Report (6) recommends React + TypeScript with a thin Bun/Hono BFF in C+, and does not select Next.js. So no source reviewed establishes Next.js as the production API or a mandatory operator app framework.

## 7. Immediate evidence-based next work

1. Continue full archive semantic crosswalk, starting with the different G7.6 Step 2 ZIPs, G7.8 Step 3 ADR package versus active G6.9-R2, and all local v1.7–v2.1 Authority assertions. Record each source hash and decision status.
2. Add this authority-precedence conflict to the owner review packet: affirm the G7.8 freeze, formally supersede/reopen it under G6.9-R2, or reopen only specified framework/contract choices.
3. Complete G6.9-R2 Step 3D using the same pinned common integration stack and actual framework-native candidates; Step 3C shell checks are insufficient. Do not treat report (6) or report (7) as an executed bake-off.
4. Keep progressing the dispatch product and adapter semantics on PR #10 without freezing API/status vocabulary until the owner review.
5. Proceed to canonical fixture/schema and integrated dispatch UI only after semantic and G6.9 contract-authority decisions are recorded.
6. The product still needs evidence-bearing Macau site discovery, actual meter/contract/tariff reconciliation, user language/role validation, measured operator usability/accessibility review, and G7.2/G7.4 live simulator/site evidence before pilot claims.

## 8. Explicit limitations of this audit

- The full original shared conversation was inaccessible: only a bounded recent slice and a share-page Cache miss were returned.
- The local project folder is an archive/reference folder, not the GitHub clone; local file existence is not repository adoption.
- The inventory covers the supplied archive packages and readable text entries, but not a full semantic review of every text in all 735 project ZIP entries. A separate G7.3-named ZIP was not found.
- Prototype source files were checked; only PR #10 v1.9 was inspected in the live browser during this audit. The earlier v0.10 and palette files were not treated as currently approved or fully accessibility-tested.
- Green GitHub structural CI and historical merged PRs are evidence for their exact scope, not proof of a complete MVP, production architecture selection, research closure or pilot readiness.


## 9. Focused G7.6–G7.8 implementation/governance package cross-check — 2026-10-06

This follow-up semantically read selected files from five source ZIPs, identified by their archive SHA-256 (the D: source folder is a reference archive directory, not a Git checkout):

| Archive | SHA-256 | Inspected conclusion |
|---|---|---|
| G7.6 Step 3 vertical-slice design | `A9ECD890FED6A25FF84A226D1873C899E0BF4AC8ED414AE590A8ABF89C980567` | Specifies an HVAC optimization recommendation loop: simulator → Go Edge → telemetry API → Energy Model → forecast/optimizer → recommendation API → React Portal. It establishes an earlier first-slice design, not a full source/load dispatch workflow or proof that the slice was implemented. |
| G7.6 Step 5 MVP bootstrap | `E84EEA8553781A071ECDE6F37F9B0098875CA4BB2B03EC93E6611452D7BE030D` | AI coding protocol requires reading authority/ADR, contract-first changes, small PRs, validation evidence, and prohibits silent architecture or equipment-control changes. |
| G7.7 Step 3 engineering governance | `A512103B8167FCDCBBB5E2DC2614E7D849A56C0B12704F9408A93ADC8249E324` | Final AGENTS draft says authority before implementation, contract before code, reversible changes and evidence-based validation; the AI coding workflow includes automated validation and human review. |
| G7.8 Step 4 repository bootstrap | `3770F38952EE8D4ED8C44BFDEC0FEC7D96FFBC968678354A2E2516259CDAA222` | Proposes a pnpm monorepo with React/TypeScript portal, Fastify/TypeScript platform API, Go Edge, Python optimizer, contracts/schemas and simulator. It is a historical implementation blueprint, not proof of a winning production stack. |
| G7.8 Step 5 CI bootstrap | `0CD05A69F4324E26DA1E093FFA775ED0A14F8A889EFE762C81698F38E90217DB` | Marks its package step completed and describes CI, contract validation, tests and review as merge gates; the status text is package-local evidence, not a GitHub merge record. |

### Repository adoption check

On inspected GitHub main, the general governance intent is **partially implemented**: `AGENTS.md`, `CONTRIBUTING.md`, a PR template, authority validation, repository hygiene, contract JSON validation, and runtime bootstrap workflows exist. The runtime workflow runs TypeScript typecheck/tests and deterministic VS-001 replay, Go tests/build, Python unit tests, and contract-fixture validation. These are real repository artifacts; they do not make every G7.7/G7.8 blueprint item complete.

The current main tree also has a canonical-path inconsistency: its authority/handoff files are under `docs/00-authority/handoff`, while the inspected main repository-hygiene and authority-validation scripts still require legacy `docs/handoff`, `docs/decisions`, and related paths that were not found at those exact paths. This is directly addressed by separate open Draft PR #13, `fix/canonical-authority-ci-paths`, head `68c955b936faddfbdbdbdf043688b3696efa87a3`; its Authority Validation run #941 and Repository Hygiene run #940 succeeded. PR #10 also contains the canonical-path repair, but it remains a broad product/design proposal and is not merged. No branch protection or PR has been changed by this audit.

The main branch's `contracts-validation.yml` and `runtime-bootstrap.yml` show that the source packages' general CI/test intent has concrete counterparts. However, the current main workflow names alone do not prove the full G7.8 gate coverage, an accepted review policy, code-owner enforcement, release governance, or source-package-to-file equivalence. Those need a dedicated repository-wide path/content crosswalk before claiming complete G7.7/G7.8 adoption.

### Product/implementation implication

The original G7.6 vertical slice prioritizes an HVAC recommendation loop. The later dispatch-first proposal broadens the operator task to coordinate grid import, verified on-site PV, ESS charge/discharge, and flexible loads under physical, tariff/contract, service, safety and evidence constraints. HVAC remains a key flexible asset and is consistent with the active main decision D-003; this is a product-scope evolution that needs explicit traceability, not evidence that the earlier package already specified or implemented the later dispatch loop.

This focused read covers five packages and selected GitHub paths only. It does not complete semantic review of the remaining source archives or certify repository-wide adoption.


## 10. G7.9 Step 1/2 scope and completion-claim cross-check — 2026-10-06

The two supplied G7.9 package archives were read by their indexed entry contents and entry hashes:

- Step 1, `macau-commercial-energy-os-g7.9-mvp-domain-foundation-v0.1.zip`, SHA-256 `CB144A2B57C612A78C80F39FD0A0BB2911CECE6453566DD0F90C70D5FD2CD30A`.
- Step 2, `macau-commercial-energy-os-g7.9-step2-domain-data-contract-design-v0.1.zip`, SHA-256 `B70CAFDA01B6F19FAC8731154A90D24930CB2A66ADA449EA9BB8E5AA4B149A6C`.

Step 1's `CURRENT.md` marks the domain-foundation package completed and points to Step 2. Its MVP scope is tenant isolation, building/asset/device registration, telemetry ingestion, an energy dashboard and basic recommendation output; it excludes direct control, autonomous AI and a full billing system. Its first slice is simulator → Edge → telemetry contract → Platform API → storage → optimizer, followed by a portal dashboard. This is a high-level foundation and older dashboard/recommendation-centered scope.

Step 2's `CURRENT.md` marks its package complete and says G7.9 Step 3 Service Boundary and Implementation Design is next. Its model lists Tenant, Organization, Site, Building, Energy Asset, Device, Telemetry Point/Record, Optimization Run and Recommendation. Its illustrative storage list omits Site despite listing Site as an entity; the API examples are only `POST /telemetry`, `GET /buildings`, `GET /assets`, and `GET /recommendations`. It proposes shared-database `tenant_id` isolation and basic versioned contracts, but does not supply a concrete OpenAPI/JSON Schema file in this archive.

Against the user's dispatch-first product objective, these two package completion labels do **not** mean that the business source/load dispatch model or operator workflow is complete. The inspected Step 1/2 texts do not define interval schedules, tariff/contract qualification, physical-versus-settlement scopes, grid/PV/ESS/flexible-load dispatch, forecast and service constraints, economics comparison, evidence-qualified claims, operator SHADOW review, or durable replay. Those semantics are proposed in the later PR #8/#10 design work and remain proposals pending authority/domain/owner review. Step 3 is therefore the next G7.9 package step in the supplied lineage; PR #10's detailed Step 3 map is not a Gate-completion record.

This reading strengthens, but does not widen, the earlier source-conformance note: Step 1/2 were completed as small foundation/design packages; their “completed” status must not be promoted into completion of the later commercial dispatch product or implementation. Archive hashes identify the source packages; this section does not claim full semantic review of all 735 indexed project-folder text entries.


## 11. G7.9 Step 1/2 source-design detail crosswalk — 2026-10-06

The source archives were also compared against the present dispatch-first design in more detail. Step 1 SHA-256 is `CB144A2B57C612A78C80F39FD0A0BB2911CECE6453566DD0F90C70D5FD2CD30A`; Step 2 SHA-256 is `B70CAFDA01B6F19FAC8731154A90D24930CB2A66ADA449EA9BB8E5AA4B149A6C`.

| Concern | Step 1/2 package content | Consequence for current design |
|---|---|---|
| Domain | Tenant → Building → Energy Asset → Device → Telemetry Record → Recommendation; Step 2 extends names with Organization, Site, Telemetry Point and Optimization Run. | The source gives a useful asset/telemetry foundation, but does not yet specify site topology and economic/physical scopes deeply enough for multi-resource dispatch. |
| API/events | Tenant/asset/device/telemetry/recommendation APIs; Step 2 examples cover telemetry, buildings, assets and recommendations. Events are registration, connection, telemetry and recommendation lifecycle examples. | Assessment, scenario comparison, operator review, evidence, decision/replay and settlement qualification need detailed Step 3 semantics. |
| Economics | Step 1 explicitly excludes a full billing system. Neither inspected package defines the source/load schedule economics or Macau contract/tariff evidence required for bill-grade value. | The product must label economic outputs as unavailable/scenario-only until applicable meter, contract, tariff and settlement evidence are qualified. |
| Data quality | Step 2 says contracts are versioned, breaking changes require migration, and shared-database `tenant_id` isolation is enforced in application and data-access layers. | This is a direction, not a concrete schema, threat model, RLS design, migration implementation or cross-tenant test result. |
| Step status | Step 1 `CURRENT.md` says completed and points to Step 2. Step 2 `CURRENT.md` says completed and points to Step 3. | Package-local completion is verified; detailed current dispatch product/contract approval and implementation remain OPEN. |

### Correspondence to current GitHub work

PR #10's G7.9 Step 3 map, product workflow and UI studies are a concrete proposal for the missing dispatch-specific layer. The proposal is substantially more detailed than the archived Step 1/2 package, but remains an unmerged review branch; its synthetic fixture checks do not validate the source packages, Macau commercial tariffs, production contracts, field capability, or a live optimizer. Main's existing telemetry-to-SHADOW VS-001 code remains a fixture-level predecessor and does not supply the dispatch-specific contracts or operator lifecycle.

Accordingly, the evidence-based next gate in the supplied G7.9 sequence is still **Step 3 Service Boundary and Implementation Design review/consolidation**. The owner must later approve any canonical contracts, persistence schema, module/service split and resulting implementation slice. No package status or PR body should be interpreted as Step 3 closure until those decisions and acceptance evidence are recorded.


## 12. Current PR #14 Macau tariff-period code slice — 2026-10-06

After checking the published Macau tariff rules and the previous source-to-code gap, PR #14 (`poc/shadow-dispatch-assessment`) now includes a bounded period mapper at head `5d6392d3157335d21f3c0f3104f1f3bda250479b`:

- `implementation/optimizer/src/macau_energy_optimizer/macau_tariff_periods.py`, blob `f3f2e7db37ad7b502788335b282596d7dca5aa41`: maps caller-supplied effective-dated rate cards for B1 and C1 into per-interval active-energy rates; recognizes B1 09:00–20:00 busy hours and C1 low/high seasons plus the separate high-season full-load and busy windows; adds caller-supplied TCA; preserves the rate evidence reference; rejects intervals crossing tariff/effective-date boundaries and rejects unsupported B2/B3/C2 variants.
- `implementation/optimizer/tests/test_macau_tariff_periods.py`, blob `fb6a9364a96e1763bfe8ebebd537f06a1ada3a07`: 10 focused cases for tariff boundaries/seasons, TCA addition, effective-window rejection, interval validation, boundary crossing and evidence-reference preservation.
- The local focused suite passed under Python 3.11.9. The package declares Python `>=3.14,<3.15`; this local run is only a compatibility signal, not proof on the declared runtime. Runtime Bootstrap, Authority Validation and Repository Hygiene were queued for the exact PR #14 head when checked.

This is only a period-to-rate input adapter. It does not qualify the customer's tariff, authenticate evidence, calculate B2/B3/C2 transformer-loss adjustments, Pu/Pc demand charges, reactive energy, taxes, PV feed-in settlement or a complete bill. It remains a PR #14 draft experiment; PR #14 and PR #10 are unmerged, and the main branch is unchanged. G7.9 Step 3 remains OPEN. The PR #10 gap crosswalk was updated to reflect this partial implementation rather than the earlier “no tariff clock” status.


## 13. Original share transcript — prompt 1 and early product thesis (2026-10-06)

The public share page was reopened and Prompt 1 selected. The first user request is: “目前想在澳门落地一个智能用电调度系统，可以让商业体省钱，请深入研究澳门目前的用电模式”. The visible first research answer explicitly frames the product as commercial energy dispatch/autopilot, not a generic energy dashboard. Its initial hypotheses include:

- Segment tariff groups and whole-bill economics; it prioritizes large C-group commercial sites, with B as a secondary segment, and says small A-group merchants are not the first customer.
- Coordinate grid import, site PV, ESS, HVAC/chilled-water/thermal storage, EV, and hot water; include TOU, Pu/Pc, reactive charges, degradation, comfort/service and business risk.
- Treat HVAC/thermal inertia as a possible virtual battery, avoid assuming battery arbitrage is profitable, and include EV as flexible load.
- Keep physical energy flow separate from tariff/contract settlement; PV export versus self-use/storage depends on actual FIT eligibility and contract rights.
- Proposed product chain: meter/context → forecasts → constrained optimizer → dispatch → measurement and verification. First pilot hypothesis is one large C-group site with central chilled-water plant and BMS, beginning in SHADOW mode; later human approval/semi-automation/closed-loop control was described as a possible staged future, not first-stage capability.
- The response itself states it had not found clear evidence of a high-frequency third-party CEM AMI API and says the first product should not depend on that assumption.

The same answer contains specific tariff, TCA, C-group time-window, 2025 consumption, PV feed-in, EV-rate and savings figures. These are recorded as claims made by that historical answer only. They are time-sensitive and need independent source/date verification before product logic, prototype data or commercial ROI uses them. In particular, the answer's high-PV-feed-in comparison cannot establish any customer's eligibility, export rights, settlement, or realized revenue.

This initial thesis is direct transcript evidence and clarifies that dispatch-first and source/load coordination were present from the first user request/research answer. It does not establish that the numerical Macau tariff/market claims remain current, that a customer segment is validated, or that the product/stack was owner-approved. The staged-control proposal must be read against current project scope: the MVP stays SHADOW-only unless a later explicit decision and safety/site evidence authorize more.

Transcript read boundary: Prompt 1's visible exchange has been examined; the 136-button prompt index exists, but assistant answers, attachments, later Gate decisions and all package outputs have not been exhaustively read.

## 14. Original share Prompt 2–3 — dispatch thesis and architecture progression (2026-10-06)

Prompt 2 asks whether dispatch should decide between PV on other/available sources and government/CEM electricity, and whether PV without storage is wasted. Prompt 3 explicitly confirms: “是的，要做多能源商业调度系统，请深入研究”.

The visible Prompt 2 research answer sharpens the objective from generic demand reduction to per-interval economic dispatch: decide whether PV serves the building, charges ESS, or is exported; decide whether building load is served by PV, ESS or grid; model flexible HVAC/EV/hot-water loads; preserve separate physical-flow and settlement-flow views. Its suggested objective includes grid energy cost, PV export revenue, demand/reactive charges, degradation and comfort, subject to energy balance and equipment/SOC constraints. It asserts qualifying grid-tied PV can be purchased by CEM under FIT, while off-grid or export-limited surplus may be curtailed. **This supports an on-site PV/export scenario where the contract and meter topology qualify; it does not establish cross-building wheeling, aggregation, virtual net metering, or another site's PV serving this building.**

The answer also proposes distinct ESS roles (demand clipping, possible TOU shifting, backup, PV curtailment handling, fast response) and HVAC/EV as slower flexibility. Its concrete values and simplified arbitrage arithmetic depend on tariff group, FIT eligibility, metering and contract and remain historical hypotheses, not validated customer economics.

The Prompt 3 research response broadens the product and engineering frame:
- Product: Macau Commercial Energy Orchestrator / Energy Autopilot. Core question is where energy should come from, where it should flow, and which flexible loads should shift while respecting service/comfort and minimizing total energy cost.
- Economic model: tariff/contract digital twin plus physical asset/building digital twin; their boundary is where customer-specific data and settlement evidence must be explicit.
- Optimization proposal: constrained MPC/MILP/QP plus forecasting; the answer says not to use an LLM or RL as an unconstrained real-time controller. LLMs are suggested for explanation/reporting, not safety-critical actuation.
- Physical scope: CEM grid, PV, ESS, HVAC/chiller/thermal storage, EV, hot water, inflexible load; objective includes energy, Pu/Pc/demand, reactive, degradation, comfort and SLA. It proposes a source/load balance equation and keeps GEC/carbon accounting distinct from physical electron flow.
- Edge/safety proposal: cloud planning/management separated from site supervisory control and existing BMS/PLC protections; local fallback and manual override; protocol candidates include BACnet, Modbus, OPC UA and OCPP. These are research proposals, not approved deployment topology or site integration.
- Pilot hypothesis evolves from the first answer's large C-group hotel/mall to a lower-complexity first pilot: non-gaming C1/C2 commercial building around 1–5 MW, existing BMS, 15-minute-or-better data, cooperative engineering team, optionally PV/EV, before approaching integrated resorts. This is a candidate segment to validate, not a confirmed user decision.
- Maturity route: bill audit → data connect → SHADOW → advisory → human-approved dispatch → closed-loop autopilot. Only the first SHADOW phase fits current MVP boundary; later phases require explicit product/safety/site decisions.
- Proposed first product set: tariff engine, data gateway, load forecast, demand guard, chiller/flexible-load model, MPC scheduler and savings M&V; first site need not have PV, battery and EV simultaneously.

The responses repeatedly compare FIT revenues (including 2.8 MOP/kWh for >500 kW PV) to C-group import energy rates and illustrate export-first dispatch. Treat this as a research hypothesis with referenced public sources, not as a universal rule. Before implementation or ROI use, verify current effective tariff schedules, PV connection/FIT eligibility, export metering, whether the contract is full-output or surplus export, import/export account boundaries, network/transformer constraints, and any applicable settlement charges. A high FIT alone does not prove another-building PV can be shared or earns that rate.

**Decision lineage implication:** dispatch-first product intent is verified from the original first three user turns; source/load economic orchestration is not a recent reinterpretation. The exact production architecture and product scope are still not approved by these research messages. The later GitHub main Authority and open proposals govern current implementation status, while this source establishes original research intent and evolving hypotheses.


## 15. Source review correction — Prompt 2 is complete and Prompt 3 is broader (2026-10-06)

The live share view exposes the first three user prompts and the corresponding first two research answers:
1. Initial Macau commercial electricity-pattern research.
2. Whether the product should dispatch between available PV and CEM grid power, and whether PV without storage is wasted.
3. Explicit request to research a multi-energy commercial dispatch system.

The answer following Prompt 2 is substantially broader than the short thesis summarized above. It proposes (as research, not accepted requirements) an interval decision among PV-to-building, PV-to-ESS, PV-export, grid-to-load, grid-to-ESS, ESS-to-load and flexible-load shifts. It describes CEM purchase of qualifying grid-connected PV under FIT, off-grid PV curtailment, separate energy/settlement graphs, and an optimizer objective that compares grid cost and PV FIT revenue with battery degradation, demand/reactive charges and comfort. This does **not** show another building's PV may be wheeled/shared with this customer. Cross-site energy sharing remains unknown until the applicable legal, market, account, meter, connection and contract mechanisms are proven.

The long answer after Prompt 3 also includes a later, more qualified proposal:
- **Pilot segment changed:** instead of first targeting a large resort, it leans toward a non-gaming C1/C2 commercial building around 1–5 MW, with an existing BMS, 15-minute-or-finer data, and a cooperative engineering team. PV/EV are preferred evidence opportunities, not mandatory prerequisites.
- **Control maturity:** Stage 0 bill audit; Stage 1 data connection; Stage 2 SHADOW; Stage 3 advisory; Stage 4 human-approved dispatch; Stage 5 closed loop. Current project MVP remains SHADOW-only.
- **Optimizer:** use constrained/replayable MPC or MILP/QP and forecast models for dispatch. Keep LLMs for explanation and reporting rather than unconstrained real-time control.
- **Architecture direction:** cloud planning and business functions are separated from site-edge supervisory control, existing BMS/PLC loops and local safety interlocks. Offline fallback, manual override, audit, allowlists and segmented OT access are proposed. BACnet, Modbus, OPC UA and OCPP are candidate interfaces, not field-validated integrations.
- **First functional slice suggested in the answer:** tariff engine, meter/data gateway, load forecast, demand guard, chiller/flexible-load model, MPC scheduler and savings M&V. PV/ESS/EV support can be modeled or phased; the first customer need not have all three.
- **Model boundary:** tariff/contract digital twin (“money”) and physical asset/building digital twin (“physics”) should stay distinct and only join through qualified evidence, meter topology and settlement rules. GEC/carbon accounting is not physical dispatch.

Prompt 2–3 additionally contain specific FIT prices, tariff/TCA values, site examples, operating schedules, savings estimates and market statistics. They remain versioned source claims, not verified present-day parameters or commercial proof. Some examples simplify settlement and opportunity-cost assumptions. Do not use their numerical output as an ROI, customer promise, universal PV-export rule or approved architecture without revalidation.

The first two prompts and Prompt 3 request/body are now directly visible from the shared transcript. This strengthens the original research lineage and explains why PR #10 centers source/load dispatch. It does not make the long response, candidate segment, control roadmap or architecture owner-approved.


## 16. Original research-framework request — v1.0 structure and early Gate plan (2026-10-06)

The shared conversation Prompt 6 asks for a durable research framework because the conversation may become too long and a new conversation may lose context. The immediately following response proposes “Research Authority + Handoff” and provides a detailed “Macau Multi-energy Commercial Dispatch System — Research & Product Authority Framework v1.0”. This is direct evidence that the project began with an intended persistent research framework and explicit repository-shaped knowledge structure, not only free-form discussion.

### Proposed original information architecture

The v1.0 proposal names root authority/handoff files (README.md, CURRENT.md, DECISIONS.md, OPEN-QUESTIONS.md) and these research/product domains:
- 00-thesis/
- 01-macau-energy-market/
- 02-cem-tariff/
- 03-energy-assets/
- 04-energy-digital-twin/
- 05-optimizer/
- 06-reference-model/
- 07-pilot/
- 08-product/
- 09-competition/
- 10-evidence/
- 11-decisions/
- handoff/

The proposal requires new conversations to restore README/handoff CURRENT/decisions/open questions first; only then read the current Gate's relevant authority. It asks that each research turn report new evidence, changed conclusions, decisions, unknowns, model impact, authority updates and next Gate. It recommends stable evidence/decision/unknown/assumption IDs and append-only handoff history.

### Original preliminary Gate sequence and priority

The v1.0 framework lists G0 Thesis, G1 Macau Electricity Economics, G2 Commercial Load Flexibility, G3 Energy Digital Twin, G4 Forecasting, G5 Optimization, G6 Safety & Control and G7 Reference Simulator, followed by product/pilot outputs. Initial G1 output is Tariff Engine v1; G3 output is Energy Graph v1. It puts tariff/settlement and meter topology first, then HVAC flexibility/reference building/M&V/pilot, with PV/EV/reactive/ESS, carbon and portfolio work at later priority tiers.

Its historic CURRENT example says next: Tariff Engine v1 + Energy Graph v1, and expressly preserves as unknown the exact CEM Pu averaging interval, commercial PV settlement topology, third-party high-frequency AMI access, ESS export rules, actual C1/C2 transformer losses, BMS data quality and site HVAC flexibility. It says not to hardcode a 15-minute Pu interval, gross FIT eligibility or a Reference Building as real customer data, and not to start full product UI or an RL controller yet. These are historically strong research guardrails; the historical Gate labels are not the current G6.9/G7.9 status.

### Substantive research immediately preceding the framework request

The prior visible answer (Simulator v0.2 research) adds significant design detail beyond Prompts 1–3: Pu interval remained UNKNOWN; C1/C2 metering position and transformer loss were modeled separately; reactive-energy charges were included; PV capacity/settlement modes were evidence-gated; HVAC used empirical → grey-box → high-fidelity modeling levels; BOPTEST was proposed for control validation; Brick was proposed for equipment semantics; IPMVP-style M&V, a distinct deterministic safety kernel/Demand Guard and concrete pilot acceptance measures were proposed. It recommended a first SHADOW chain of bill + main meter + BMS/chiller → Energy Graph/twins → forecasting/MPC → Safety Kernel → SHADOW → M&V, then Tariff Engine v1 + Energy Graph schema as the next technical research. These are proposal-era content, not proof of accepted designs or measured site performance; all numeric examples remain synthetic/source claims pending verification.

### Current-repository comparison remains a separate task

This transcript confirms the original proposed structure, but does not prove it was implemented verbatim. The active repository uses its own docs/00-authority, docs/01-research, docs/02-product, docs/03-architecture, implementation/ and handoff/ organization, and the later G7.9 Step 3 outputs map selected artifacts into that organization. A file-by-file crosswalk is still required to identify preserved, renamed, split, absent and superseded v1.0 domains and to distinguish a semantic equivalent from the exact original directory structure. Do not call the original tree “strictly implemented” until that crosswalk is verified on main and relevant PR heads.

This evidence corrects earlier claims that the original share could not be read. The public share exposes the Prompt 6 framework content, but many later research cards still fail to load; full chronology/attachment review remains incomplete.


## Original conversation phase history reconciled with live GitHub — 2026-10-07

The bounded ChatGPT thread read for conversation 6abf4f5c-b2d4-83ea-b189-6534f517c5a1 returned five turns (requested limit 10, no cursor, hasMore=false). It is not a full transcript of every historic or shared-page message. Among the returned assistant messages, the following engineering timeline was reported and then cross-checked against live GitHub:

| Historical report in the conversation | Live repository evidence | Reconciled status |
|---|---|---|
| Commit 004 Phase A created contract-first structure and VS-001 plan; base 8c12669a72eb7a0fca01718f92d4110a63515447. | PR #2's base is that SHA; main CURRENT records Phase A on main. | Verified historical foundation. |
| Phase B PR #2 was Ready for Review at head a6db97808d7a6f3e9ecc4c4187c35f8ddeef599e, then merged. | Live PR #2 is closed/merged with merge commit be28ced3361e7d3994251bc0bf9331a8adb3dc6b. Main package files confirm Node 24.21.x, NestJS 12.0.3 and TypeScript 6.0.3; Go module declares 1.27.1; optimizer pyproject requires Python >=3.14,<3.15. | Verified implementation history, not a G6.9 winner. Current authority still calls Node/NestJS Candidate B and G6.9-R2 Step 3D pending. |
| Phase C initially proceeded as Issue #3 / mvp/vs001-phase-c; a later response said to implement it. | Live PR #4 is closed/merged, titled “Commit 004 Phase C — Executable VS-001 Domain Path”, head c46ea305bf874a46c34b17dbaac2158ba8ce07a3, merge commit 83ba35c25b9aa04c80f2f9d592b3b1c6dfed3acb. Main CURRENT snapshot (2026-10-03) also records Phase C merged via PR #4. | The branch/issue state in the older conversation was interim; the merged PR is the later verified state. |
| Phase C was described as telemetry → Energy Graph → fail-closed tariff → cost → SHADOW recommendation → evidence → replay. | Main controller exposes POST /v1/vs001/evaluate; current service uses a single parsed telemetry event; default Energy Graph and tariff adapters fail closed; evidence storage is in-memory; the replay/test adapters are static and synthetic. The test recommendation has empty actions. | Phase C is a real, tested vertical slice, but it is a single-event economic-intelligence scaffold. It is not interval-level PV/ESS/HVAC/EV scheduling, a durable dispatch workflow, or the six-stage operator product. |
| Original messages report restoration of D-001..D-055 and U-001..U-016/017, followed by G7.4 U-017. | Current main authority snapshot records synchronized D-001..D-077 and U-001..U-026, with the newer unknowns and PV follow-up. | Later authority state supersedes the older counts; preserve historical progression rather than treating the earlier register as current. |

### Phase C code-reference integrity finding

Source inspection found that Phase C records several sourceRefs under pre-migration paths which return 404 on current main: mvp/vertical-slices/VS-001-energy-intelligence-loop.md, docs/engineering/module-boundaries/README.md, docs/decisions/OPEN-QUESTIONS.md, and docs/architecture/tariff-engine/README.md. The current canonical files include docs/05-mvp/vertical-slices/VS-001-energy-intelligence-loop.md, docs/04-engineering/module-boundaries/README.md, and docs/00-authority/decisions/OPEN-QUESTIONS.md; tariff decisions live in the current authority decision register. This is a source-reference defect in emitted evidence records, distinct from the correct fail-closed behavior. A focused code PR should repair these references and add a regression assertion that every emitted repository sourceRef resolves on the default branch.

### Scope limitation

This reconciliation validates the bounded thread messages and named GitHub commits/files. The public shared conversation still has not been completely exported or semantically reviewed; all archive text entries have not been read; the full contents of the user's D: research folder and all deep research reports are not re-audited in this update. The products, architecture and design proposals in PR #8/#10/#11/#14 remain unmerged unless a later live PR state says otherwise.


### Follow-up — Phase C evidence-reference repair proposed on PR #15 — 2026-10-07

The stale Phase C source references identified above are corrected in open Draft PR #15, head a9865ec4686131e32120862e2f59361f09717a50. The change points emitted VS-001 evidence records to existing canonical VS-001, module-boundary, open-question and decision-register documents. A platform test exercises completed and fail-closed graph/site/tariff paths and checks every emitted documentation-path reference resolves. PR #15 also aligns the repository's existing Authority and Hygiene checks and AGENTS.md with the migrated canonical documentation paths.

All six exact-head CI jobs passed on PR #15: Platform API, Edge Runtime, Optimizer, Contract Fixtures, Repository hygiene and Validate authority structure. PR #15 remains unmerged, so main still contains the stale references and stale-path checks until that proposal is reviewed and merged. These green checks validate the bounded code regression and repository gates only; they do not change the Phase C or product/architecture scope.
