# VS-001 Implementation Evidence and Dispatch Gap — 2026-10-05

**Status:** source-code audit on `main`; implementation evidence, not a Gate closure, production validation, product approval, or dispatch acceptance.

## Finding

The current VS-001 vertical slice is an executable **single telemetry event → tenant/site context → tariff result → Shadow recommendation/evidence** path. It is not yet the requested multi-source, multi-load economic dispatch workflow.

### Evidence present in main

- `implementation/platform-api/src/vs001/contracts.ts` models one `TelemetryEventV1` with a scalar value, unit, metric, identity, quality and timestamps. It has no interval schedule, source/load portfolio, forecast horizon, energy balance, battery state, or equipment capability contract.
- `implementation/platform-api/src/vs001/ports.ts` defines ports for Energy Graph lookup, tariff evaluation, optimizer recommendation and evidence persistence. The optimizer receives one telemetry event and one resolved cost; there is no schedule/constraint/equipment model in this interface.
- `implementation/platform-api/src/vs001/vs001.service.ts` validates the event, fails closed when graph context or tariff is unresolved, verifies tenant/site identity, writes derived evidence, and enforces `recommendation.mode === 'SHADOW'`.
- `implementation/platform-api/src/vs001/vs001.service.spec.ts` uses `StaticGraph`, `StaticTariff`, `StaticOptimizer`, and `MemoryEvidence`. Its successful fixture is synthetic (10 kWh and MOP 12.500000), produces an empty action list, and checks fail-closed tariff and tenant/site mismatch cases plus deterministic evidence ID.
- `implementation/platform-api/src/vs001/replay.ts` repeats the same synthetic path with static in-process adapters; the evidence adapter is deliberately side-effect free.
- `implementation/platform-api/src/app.module.ts` binds the running Nest application to fail-closed graph and tariff adapters, a guard optimizer and an in-memory evidence repository. Therefore the checked-in default app does not calculate a successful recommendation from authoritative live/site data. A successful service unit test does not prove a successful running integration.
- `.github/workflows/runtime-bootstrap.yml` runs typecheck/tests and compares two VS-001 fixture replay outputs; it also runs Go build/tests, Python unit tests and contract fixture validation. This is useful structural/runtime-bootstrap evidence, but it is not a dispatch-quality or site-validation test.

## Evidence classification

| Claim | Status | Evidence / limit |
|---|---|---|
| API path is constrained to Shadow recommendations | **Verified in service implementation** | VS-001 throws if optimizer returns a mode other than SHADOW. This does not substitute for proving every downstream system has no control path. |
| Unresolved tariff and mismatched tenant/site fail closed | **Verified in code and unit test doubles** | Tests prove service behavior under supplied test doubles; they do not test production adapters, auth, database isolation, or cross-tenant API access. |
| Deterministic replay exists | **Verified as synthetic fixture replay** | Static adapters and side-effect-free evidence repository; deterministic output is not schedule replay from persisted inputs. |
| Default API can calculate a live tariff-backed recommendation | **Not demonstrated; default bindings fail closed** | `app.module.ts` binds explicit fail-closed adapters. |
| Durable, immutable evidence store exists | **Not demonstrated** | Default repository is in memory; replay adapter does not persist. |
| Source/load economic dispatch exists | **Not demonstrated** | Current contract is a scalar telemetry event and per-event cost, with no common-horizon schedule or physical balance. |
| PV export/credit, battery dispatch, demand charge optimization, HVAC rebound or comfort constraints are modeled | **Not demonstrated by VS-001** | No such fields or constraints appear in the reviewed VS-001 event/ports/service/replay path. This is a bounded source inspection, not a claim about every file in every archive. |
| G7.9 Step 3 is complete | **No** | This implementation path does not satisfy the G7.9 Step 3 service-boundary and implementation evidence needed for dispatch. Keep the package's Step 3 next-step declaration and PR #10 proposal distinct from delivered integration proof. |

## Dispatch acceptance work still needed

To turn this foundation into a reviewable dispatch MVP, define and evidence the following before claiming dispatch completion:

1. A time-indexed site input contract: interval meter/import/export, PV generation/curtailment, battery SOC/power/efficiency, controllable load telemetry, forecasts, timestamps, quality/provenance, and site/time-zone semantics.
2. Separate physical energy balance from tariff/contract settlement. Each settlement calculation must cite the applicable versioned tariff/contract evidence; absent evidence withholds financial claims.
3. A common-horizon baseline and candidate schedule for grid, PV, optional storage and enabled loads, with explicit device capability, comfort, safety, demand and operational constraints.
4. Explainable results: objective, cost components, constraint binding/slack, source/load contribution, uncertainty, evidence references, and withheld/unknown values.
5. Shadow-only review, approval state, versioned input/model/solver references, persisted evidence, deterministic replay and post-run measurement/verification. Keep actuation outside this MVP.
6. Replace static test doubles with contract-backed adapters and integration tests. Prove fail-closed behavior under missing/stale/poor-quality data, unresolved tariff, tenant boundary violations, optimizer failure and replay drift.
7. Confirm CI reports correspond to the exact commit under review; a configured workflow is not evidence that a particular head passed.

## Scope and next step

This note audits only the named main-branch VS-001 implementation and the runtime-bootstrap workflow as observed on 2026-10-05. It does not close G7.9, approve the provisional architecture, or assert absence of all related functionality elsewhere.

**Recommended next artifact:** update the PR #10 dispatch contract/implementation map with these exact VS-001 interfaces and default bindings, then make dispatch acceptance criteria trace to data contracts, domain services, persistent evidence/replay and integration tests. Keep the product, visual direction and production stack open for owner review.
