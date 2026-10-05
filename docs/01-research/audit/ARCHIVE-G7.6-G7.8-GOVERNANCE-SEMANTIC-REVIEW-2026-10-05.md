# Direct semantic review — G7.6 implementation, G7.7 governance, G7.8 bootstrap

**Review date:** 2026-10-05  
**Repository baseline:** GitHub `main` commit `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`.  
**Source rule:** Status labels are read as what each package claims; they do not prove runtime behavior or supersede current main by themselves.

## Sources read from the ZIPs

All Markdown members in these 12 packages were extracted and read. The package hashes below were checked against the deep archive index.

| Gate package | ZIP SHA-256 | Entries |
|---|---|---:|
| G7.6 Step 3 vertical slice | `a9ecd890fed6a25ff84a226d1873c899e0bf4ac8ed414ae590a8abf89c980567` | 9 |
| G7.6 Step 5 MVP bootstrap | `e84eea8553781a071ecde6f37f9b0098875ca4bb2b03ec93e6611452d7be030d` | 7 |
| G7.6 Step 6 MVP implementation | `87317bf3eafa7b6d53602884217a558277ce7914c3a5bfde72d5b64e4255f758` | 9 |
| G7.6 Step 7 code skeleton | `6b72f9ba75a73b47ec0b8c39ec90ef25049388e480631eda1294518c37d79569` | 9 |
| G7.7 repository foundation Step 1 | `0fb7db37d4e0f8b334b937cb54767b2c10e4afe82c8067b60f89c494a70ab4da` | 6 |
| G7.7 repository foundation Step 2 | `012fb0e7f7c1c78f6182d36f656fc98d2db66fdd617f6f586d85130e7dbc9369` | 8 |
| G7.7 engineering governance Step 3 | `a512103b8167fcdcbbb5e2dc2614e7d849a56c0b12704f9408a93adc8249e324` | 9 |
| G7.7 initialization blueprint Step 4 | `c7adf1b33ce1ea1164188e04babc06cf73a0617ecfabbc631e3b3a250381204e` | 9 |
| G7.7 creation readiness Step 5 | `0306a64c4250334477e38b665e73dab2f897779685c4768fdbeb44ed775ffb77` | 10 |
| G7.8 implementation repository foundation | `72a6d7dc5458e68272c0959402352c61d3f0ae97f21dd276931ca353cbd104b4` | 6 |
| G7.8 repository bootstrap Step 4 | `3770f38952ee8d4ed8c44bfdec0fec7d96ffbc968678354a2e2516259cdaa222` | 10 |
| G7.8 dev environment/CI Step 5 | `0cd05a69f4324e26da1e093ffa775ed0a14f8a889efe762c81698f38e90217db` | 10 |

## Reconstructed intent and status

### G7.6 Steps 3/5/6/7 — a planned HVAC telemetry recommendation loop

- Step 3 designs simulator → Go Edge → telemetry API → energy model/forecast/optimizer → recommendation API → React portal. It marks ADR-071/072 **Proposed**, and `CURRENT.md` says design completed, next implementation/validation. Portal scope lists overview/map/asset/recommendation/savings pages. Its acceptance list says an audit trail exists but does not define persistence, evidence semantics or settlement boundaries.
- Step 5 defines repository/bootstrap sequence and an AI coding protocol: read authority/ADR, contract first, small PR, validation evidence, no silent architecture/security/control changes. Its gate is repository build/CI/Docker plus the complete telemetry-to-portal demo.
- Step 6 calls out no equipment control, full ML optimization or full microservice split; its Docker environment and migrations are plans, not evidence of execution.
- Step 7 still calls itself a **code skeleton design** and says the next step is to implement and validate the telemetry demo. Its acceptance gate requires repository build, runtime start, simulator → Edge → API, portal display; no autonomous control.

These packages support the historical direction of a recommendation-only telemetry vertical slice. They do not show that G7.6 Step 7 runtime acceptance passed. Their HVAC-first overview/recommendation/savings scope is narrower and older than current dispatch-first product proposals. “Savings Report” cannot be treated as a supported MVP claim without the later evidence/M&V boundary.

Current main contains a bounded VS-001 single telemetry-event path, typed platform ports, schemas and a Go Edge bootstrap, but its tree has no complete simulator→Edge acquisition/forwarding→persisted dispatch assessment→portal flow. Therefore the old Step 7 acceptance is not proven by the main implementation. PR #14 is a separate unmerged experiment and does not supply that integrated path.

### G7.7 Steps 1–5 — governance before repository creation

- Step 1 defines authority/implementation separation, `main`/`develop` plus feature/release/hotfix branch conventions, architecture ADRs, domain review and AI evidence.
- Step 2 proposes `AGENTS.md`, contribution workflow, authority import structure and documentation-first CI.
- Step 3 adds AI workflow, CODEOWNERS ownership areas, PR validation template, ADR template and release process. AI is explicitly not the architecture authority.
- Steps 4/5 are **readiness blueprints**. Step 4 checklist leaves actual repository creation and first implementation unchecked. Step 5 says repository creation is the next procedure and its final checklist still leaves creation/first commit pending. These packages do not mean those actions had already occurred.
- G7.7 “Research/Product/Architecture ready” is a readiness statement, not detailed product approval or a production architecture freeze. License selection is still deferred until public release.

### G7.8 Steps 1/4/5 — implementation foundation and environment

- Step 1's tree proposes portal, API, edge, optimizer, simulator, contracts/schemas and infrastructure. It explicitly says “No Code Yet” and says finalize stack, module boundaries, contracts and local runtime before business code.
- Step 4 adopts a contract-first flow and plans pnpm for TS workspaces, independent Go module, and Python/uv optimizer. Package boundaries place orchestration in platform API, device I/O at Edge, algorithms in Python and cross-service contracts in a separate package. Its `CURRENT.md` marks bootstrap plan completed and environment/CI as next; this alone is not a running-system test.
- Step 5 proposes PostgreSQL/Redis/broker/local containers, Node LTS, pnpm/Corepack, Go, Python/uv and Docker; CI should validate contracts/tests/build/lint and report evidence. Its status says bootstrap complete and G7.9 is next, but this source does not provide CI run logs or site data.

The Step 4/5 composition is a historical repository bootstrap proposal following the G7.8 Fastify ADR freeze. It is not interchangeable with the later G6.9-R2 stack bake-off; current main's NestJS bootstrap is implementation evidence, not authority to silently replace the historical Fastify decision.

## GitHub main governance adoption check

Fetched main files and the complete non-truncated Git tree at `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`.

| Archived control | Current main evidence | Assessment |
|---|---|---|
| AI must read authority/ADR; no silent architecture or contract break | `AGENTS.md` (blob `acfbc9e…`) and `CONTRIBUTING.md` (blob `666d2f4…`) present | Adopted in abbreviated form; authority now lives in `docs/00-authority/handoff/CURRENT.md`. |
| CODEOWNERS product/architecture/security/engineering areas | `CODEOWNERS` exists but assigns all paths to `@lilinling12` | File exists; area-specific ownership has not been adopted. |
| PR evidence, architecture impact, safety/control boundary | `.github/PULL_REQUEST_TEMPLATE.md` exists and asks for authority, evidence status, validation, architecture/safety impact | Materially adopted and expanded. |
| PR quality checks | Four workflows exist: authority validation, contracts validation, repository hygiene, runtime bootstrap | Adopted; exact coverage varies. `main` authority/handoff validator still expects old `docs/handoff/*` paths. PR #10 carries a repair on its unmerged branch. |
| `SECURITY.md` and secret handling | `SECURITY.md` exists; hygiene workflow rejects committed secret env files | Partially adopted; package's production secret-manager and full security assurance requirements need separate proof. |
| `CHANGELOG.md`, release process, ADR template | `CHANGELOG.md` is absent; main tree does not contain the archived ADR template/release-process file at those names | Not fully adopted. Main has authority decision records but no demonstrated release-versioning process in this checked tree. |
| `main` branch protection / required review | GitHub rulesets endpoint returned `[]`; branch-protection API returned 403 “Resource not accessible by integration” | Ruleset list is empty; actual classic branch protection remains **unknown** because API access was denied. Do not claim enforcement is enabled or disabled. |
| `develop` integration branch | Current live branch list has no `develop`; work proceeds on named proposal/feature branches | Archived branch model was not adopted verbatim. This may be intentional; no ADR establishing a replacement branch strategy was found in this check. |

## Decisions and evidence gaps carried forward

1. Keep G7.6 Step 3/5/6/7 packages as historical proposed/planned vertical-slice evidence; they do not prove end-to-end execution.
2. Treat G7.7 Steps 1–5 as governance/readiness preparation; the actual repository was created later under G7.8, while some old checklist language remained pending.
3. Current main has meaningful AI/PR/CI governance, but not all G7.7 controls are fully adopted or verifiably enforced. In particular CODEOWNERS granularity, changelog/release semantics and classic branch protection remain open/unknown.
4. Historical G7.8 Fastify/contract-first/bootstrap records remain in the source timeline; G6.9-R2 reopening, current main's NestJS implementation, and PR proposals must be reconciled by explicit authority decisions before a production framework freeze.
5. Current G7.9 Step 3 dispatch-first design improves on the old recommendation-dashboard/savings-report outline, but its PR remains unmerged and owner/domain review is pending.

## Coverage limit

This pass directly reads the 12 packages listed above, extending prior direct reads of major Authority, G7.1/2/4/5/6.9/G7.6 Step 2/G7.8 Step 2/3/G7.9 sources. It does not assert that every document in all 40 Macau ZIP packages has now been semantically reviewed. Four unrelated remote-control research ZIPs remain excluded; full original share-dialogue text remains unavailable.

