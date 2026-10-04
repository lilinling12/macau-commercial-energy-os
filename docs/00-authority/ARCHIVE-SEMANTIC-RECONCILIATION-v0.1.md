# Macau Commercial Energy OS archive semantic reconciliation v0.1

**Review date:** 2026-10-05  
**Purpose:** Reconstruct the authority/Gate version lineage and identify archive claims that cannot safely be carried into the current GitHub authority without an explicit crosswalk.  
**Status:** First semantic audit pass; not a closure record for the remaining archives, Gates, product decisions, or architecture.

## 1. Scope and access evidence

Read-only inventory of `D:\dev\project\lilinling\macau-commercial-energy-os` found 44 ZIPs (40 Macau Energy OS packages and four unrelated remote-control packages) and two loose authority files. All 44 ZIPs opened without read errors. The scan read 1,071,834 uncompressed bytes, recorded SHA-256 values for entries, and found eight repeated embedded paths with different contents across Authority revisions. This proves archive readability and package membership, not that every claim has been semantically reviewed. The remote-control packages are excluded from Macau authority.

This pass semantically read the Authority v1.0–v1.6.2 handoff/status and decision-register material; the v1.7.0–v2.0 transition/current files; the loose v2.0/v2.1 authorities; the G7.1/G7.2/G7.4/G7.5 package bodies; both G7.6 Step 2 variants; G7.8 Step 2/3 technology decisions; and the G7.9 Step 1/2 domain packages. The machine inventory is an audit aid, not evidence of a full content review of every file in every archive.

The linked shared ChatGPT page was retried and returned **Cache miss**. `read_thread` can currently return five recent turns with `hasMore: false` and no older cursor; it does not expose the complete historic transcript. The two attached technology reports were readable: `deep-research-report (6).md` SHA-256 `1E0118807DBFDCA3D13AE1949383B4CBFEFB80DB0CD867D13BD6C8DC0D744495`; `(7).md` SHA-256 `5DB518CBE85402E0A8AD2682B9E52A7782D17748EC95C60F43B4BB748B6CAC82`.

## 2. Authority and Gate lineage

| Source revision | What its own status records say | Reconciliation consequence |
|---|---|---|
| Research Authority v1.0.0–v1.6.2, snapshots 2026-10-02 to 2026-10-03 | G7 is **Reference Simulator & Pilot Validation**. Its early children concern the controller/economics loop, a live BOPTEST R0 baseline/no-op, SitePowerComposer/Macau replay, then a tariff-aware supervisory controller. G1 remains open. By v1.6.2, G7.2 live execution is still pending; G6.9-R2 Steps 3A/3B/3C are complete, while framework-native Step 3D is pending. | These G7.1–G7.4 identifiers describe a reference-simulation/control research sequence, not the later commercialization/productization Gate sequence. Their design completion does not equal live R0 execution or a Macau pilot result. |
| Research Authority v1.7.0 | Calls G6.9-R2 “Technology consolidation” and says final framework-bake-off evidence and a reference-implementation decision are pending; next is G7 Commercialization Research. | “Technology research completed” in later summaries cannot silently be interpreted as a measured production-stack winner. |
| Research Authority v1.7.1 | Says it restores the G6.9 authority format and prepares transition to G7 Productization; technology decisions remain accepted/provisional/open. Its roadmap assigns G7.2 to energy economics/dispatch, G7.3 to Macau electricity-market research, G7.4 to ROI simulation, and G7.5 to the pilot product blueprint. | The G7 namespace was repurposed. This is a new meaning for the same numbers, not evidence that the earlier same-numbered simulator/control sub-Gates closed under the new definition. |
| Authority v1.8.0 | Labels G7.1 market, G7.2 economics, G7.3 dispatch, G7.4 pilot, G7.5 product architecture, and G7.6 engineering as completed/partially completed. | Those are declared package statuses. The separate G7.1 and G7.2 ZIPs are short framework/open-question documents, so their status declarations alone do not prove the research evidence or closure criteria. Later evidence reports must be mapped by subject and source, not Gate number alone. |
| Authority v1.9.0 | Says research/architecture consolidation is complete and identifies G7.7 Repository Foundation as the next Gate; actual Git repository creation had not yet started in that snapshot. | This is a repository-preparation transition snapshot, not proof of an implemented product. |
| Authority v2.0 recovery and Step 2/3/4 packages | Mark recovery/mapping, architecture consolidation, and repository preparation steps complete in their own `CURRENT.md` files. | These are historical authority-recovery checkpoints. Their “completed” status is not an implementation or live-pilot result. |
| Loose Authority v2.0, SHA-256 `BD705A40A34DBE9BE1248B6B8BD792913ED92B398A32EC32E42D99829A1B4661` | Lists G6.9-R2 Steps 3A/3B/3C/3E/3F/3G.1 as completed and 3G.2 as next; describes React/TypeScript, Python, Go, PostgreSQL/Timescale and Wasm-related directions while keeping some cloud-core choices under evaluation. | This conflicts in completion level with the current GitHub main `CURRENT.md`, which still says G6.9-R2 Step 3D is pending. It needs a dated supersession/reconciliation record; neither document can be silently substituted for the other. |
| Loose Authority v2.1, SHA-256 `93AF2811B278FA7B1099A6F5FBD69A2A9F7B60CD26ECDAABECBC82676524A373` | Says G6.9/AI-native engineering are complete, begins G7.1 market/ROI research, and frames the MVP as energy visibility, tariff intelligence, optimization SHADOW mode, and Edge. | This is a broad product thesis, not a detailed dispatch-first PRD. The current PR #8 PRD/IA now make economic source/load scheduling primary, but the old thesis has no explicit supersession record in the loose source. |
| Current GitHub main `docs/00-authority/handoff/CURRENT.md` (snapshot 2026-10-03) | G1 is open; G6.9-R2 Steps 3A/3B/3C complete and Step 3D pending; G7.2 live baseline/no-op pending; C+ provisional and not the measured winner. | This is the controlling repository snapshot for current delivery. It preserves, rather than resolves, the conflict with the loose v2.0/v2.1 files and historical G7.8 freeze. |

## 3. Gate package contents versus closure labels

The standalone G7.1 market ZIP contains a segment/pain-point research framework, an ROI outline, and a `CURRENT.md` that says research is still underway. The standalone G7.2 economics ZIP contains a high-level dispatch diagram/objective and six explicit open questions (tariff detail, typical hotel load, PV economics, battery payback, demand response, realistic savings percentage). Neither package itself is a complete evidence-backed market/economics study. Later G1/G2 evidence in GitHub may satisfy individual questions, but it must be linked to specific requirements and does not follow merely from these ZIPs' names or later “completed” labels.

The G7.4 Pilot Blueprint ZIP marks the package completed, while ADR-057/058/059 inside it are **Proposed**. Its pilot phases include shadow optimization and M&V, and do not supply named-site results. The G7.5 Step 3 roadmap places “limited closed-loop control” before “PV and battery dispatch”; this conflicts with the current dispatch-first, SHADOW-only MVP boundary unless a later record explicitly supersedes that sequence. Treat it as an old proposed roadmap, not current authorization.

## 4. Technology-authority conflicts found in package bodies

### G7.6 Step 2 duplicate archives

Two different packages share the same nominal version/name family:

- `macau-commercial-energy-os-g7.6-step2-engineering-foundation-v0.1.zip`, 7 entries, ZIP SHA-256 `18704C677AF55A53886806A219A1A5EE22DEA9EF3A0256E286EC9429DD7F2785`: its ADR-068/069/070 update calls the TypeScript + Go + Python hybrid, domain-service boundaries, and contract-first/AI verification **Proposed**; it does not pin runtime or database versions.
- `macau-commercial-energy-os-g7.6-step2-engineering-foundation-v0.1(1).zip`, 39 entries, ZIP SHA-256 `F3955862E9902166F82126A2C489E798413676CF93000D4F3F68F650867D47EB`: its `CURRENT.md`, `DECISION_LOG_UPDATE.md`, ADRs 071–076, and `TECH_STACK_FREEZE.md` say **Accepted/Frozen**, including React/TypeScript/Vite, Node 24/Fastify 5 modular monolith, Python, Go Edge, PostgreSQL 18 initial storage, NATS/JetStream, and no direct cloud-to-equipment control. It explicitly defers splitting telemetry storage until evidence justifies it.

These are materially different authority artifacts, not interchangeable “same version” copies. The detailed archive is a historical accepted freeze, but its current binding status must be reconciled with G6.9-R2 and current main before production architecture approval.

### G7.8 Step 2/3 freeze versus G6.9-R2

G7.8 Step 2 marks technology research complete and Step 3 as the final stack ADR. G7.8 Step 3 then explicitly marks its ADR freeze complete: React/TypeScript, Node LTS TypeScript backend, Go Edge, Python, OpenAPI + JSON Schema, with **Fastify** chosen over NestJS/Hono as the starting backend framework; Bun is evaluation/development tooling, not mandatory production runtime. This is a real historical freeze record in the supplied archive, not a mere recommendation.

The later/current G6.9-R2 authority instead keeps C+ (Go Energy Core + Temporal Go + thin Bun/Hono/TypeScript surface + Go Edge + Python) provisional and requires a comparable Step 3D/Step 4 result. The archive set contains no explicit accepted record saying exactly whether G7.8 remains binding, is superseded by G6.9 evidence, or must be rerun. That authority-priority decision remains open in the PR #8 owner review materials.

### G7.9 Step 1/2 status versus actual design depth

Both G7.9 ZIPs mark their own step **Completed**. The Step 1 package is an initial tenant/building/device/telemetry/recommendation scope and explicitly excludes direct control and full billing. Step 2 lists Site as an entity, yet the relationship fragment omits Site; its table list omits Site; its API list is only telemetry/buildings/assets/recommendations; and the archive contains no schema artifact despite saying APIs are generated from schemas. There are no account, meter-settlement, tariff, dispatch assessment/result, review, or replay operations in the package. Therefore Step 2 is a completed **historical package status**, but it is not a complete source/load-dispatch domain contract. The current PR #10 Step 3 map correctly treats the dispatch, settlement and evidence extensions as new proposal work and keeps Step 3 open.

## 5. Research-report reconciliation and Next.js role

Deep Research (6) is a **pre-bake-off provisional C+ recommendation**: Go Energy Core and Temporal Go, thin Bun/Hono TypeScript BFF, Go Edge, Python, PostgreSQL/Timescale, NATS plus MQTT, and Deno initially for the plugin sandbox. It explicitly says to use a falsifiable bake-off; this is not a measured winner.

Deep Research (7), dated 2026-10-02, recommends React/TypeScript with a simple SPA for the authenticated operator console, a Node LTS + NestJS modular-monolith control plane, Go ingestion/Edge, Python intelligence, PostgreSQL/Timescale initially and Kafka as a longer-term target. It says Next.js **may** serve a customer/public portal or where its server features are valuable, but the core authenticated Energy OS is a rich interactive app and does not need SSR by default. It does not select Next.js as the backend and does not add it to G6.9-R2's actual A/B/C+ candidates. The current product UI framework remains a proposal separate from that backend bake-off.

The two reports are competing recommendations with different boundaries and evidence dates. Current main preserves C+ as provisional and A/B/C+ as candidates. The existing Node/NestJS scaffold is implementation evidence for B, not proof B won. The historic G7.8 Fastify freeze and later report (7) NestJS recommendation are distinct decisions/evidence and need an explicit owner decision; one cannot be silently rewritten as the other.

## 6. GitHub mapping and unresolved work

Current PR #8 contains a research/evidence register, Gate records, PRD, user-flow/IA, product review packet, architecture/detailed designs, traceability and readiness audit. PR #10 contains the dispatch-first product proposal, synthetic v0.3–v0.5 studies, the three layout study, and the G7.9 Step 3 proposal/map. Both PRs remain unmerged; they are reviewable proposals, not current main baselines. The PR changed-file lists do not contain the supplied ZIP archives themselves. This pass does not prove that every source document is represented or correctly traced in GitHub.

The original shared page could not be fetched; `read_thread` exposes only five recent turns and no older cursor. That is an explicit source gap. The two Deep Research files and the named project folder archives above were directly readable.

### Next audit sequence

1. Continue full semantic cross-check of every G7.1–G7.9 package and every Authority/G6.9 package against the current GitHub evidence register and Gate exit criteria, recording exact archive/file hashes and “present / partial / absent / contradicted / unknown” status per artifact.
2. Resolve the old/new G7 numbering crosswalk and whether v1.7.0/v1.7.1/G6.9 authority transitions supersede one another; do not mark historical design-only work as a live Gate closure.
3. Resolve G7.6/G7.8 versus G6.9 stack authority, including the explicit G7.8 Fastify freeze, D-064 provisional C+, D-068 bake-off requirement, Next.js optional UI/server role, and main's actual Node/NestJS code status.
4. Reconcile G7.9 Step 1/2 completion labels with the package omissions and current Step 3 design; preserve the distinction between a source package's status and validated implementation.
5. Record the owner-approved product, locale, visual and architecture decisions only after the evidence packet is complete. No merge, freeze or equipment control is authorized by this audit.

