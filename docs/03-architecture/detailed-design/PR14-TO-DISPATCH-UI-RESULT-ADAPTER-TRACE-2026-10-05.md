# PR #14 Optimizer to Dispatch UI Result Mapping — 2026-10-05

**Status:** Implementation-grounded integration design proposal. It is not a canonical APP-11 API, approved wire schema, production adapter, or G7.9 exit.  
**Compared revisions:** PR #14 `poc/shadow-dispatch-assessment` head `0b69b7b5db04a2f2454bec691ecc8f609facc552`; PR #10 UI branch at the time of this review `e43238855cb829fdad934e60cbb831e66fe9b435`; main baseline used by the branch's code trace `a897bf0b1e7e6ceea3862d7d87fa288ecca08203`.  
**Purpose:** Prevent the v2.3 static claim-state study from being mistaken for a direct representation of PR #14 enums or output.

## 1. Evidence read

PR #14 has a bounded Python schedule assessor and finite-horizon discrete candidate search. Exact inspected files:

- `implementation/optimizer/src/macau_energy_optimizer/dispatch_assessment.py`, blob `f53254eb41659a8284a0904115a61795adecc899`.
- `implementation/optimizer/src/macau_energy_optimizer/dispatch_optimizer.py`, blob `2d3256801f0ddce6b849c648c160f5a32fd90a27`.
- `implementation/optimizer/SHADOW-ASSESSMENT-PROTOTYPE.md`, blob `731dc465a5d23ef94d40b124a6e07c9ef7dbfe45`.
- `implementation/optimizer/tests/test_dispatch_assessment.py`, blob `f12ffdd0b6f3771851800d80fc0585ba85e8dc2d`.

PR #14 is Draft/open/unmerged. The implementation is not the main-branch APP-11 service. The main-branch implementation trace recorded in PR #10 pins VS-001 to main `a897bf0b1e7e6ceea3862d7d87fa288ecca08203` and describes one telemetry-event endpoint with fail-closed/default in-memory adapters, not an interval source/load assessment, durable APP-11 result, or UI API. Main `docs/00-authority/CURRENT.md` still says Authority v2.0 import is in progress. These two implementation paths must not be conflated.

## 2. Enum and meaning crosswalk

| PR #14 model | Meaning in inspected code | v2.3 display treatment | Adapter rule |
|---|---|---|---|
| `PhysicalStatus.VALIDATED_WITHIN_SCOPE` | Physical schedule validated only for its declared inputs/scope. | Do not reduce this to an unqualified green “COMPLETE.” Say “validated within stated scope,” with the scope visible. | Preserve the scope and boundary in the response. Synthetic inputs remain visibly synthetic. |
| `PhysicalStatus.SCENARIO_ONLY` | Schedule is based on project assumptions/scenario evidence. | “Scenario only”; never a site-validated/feasible claim. | Keep scenario-only status distinct from PARTIAL. |
| `PhysicalStatus.PARTIAL`, `BLOCKED`, `INFEASIBLE` | Different physical assessment outcomes. | Map each distinctly; include affected resource, interval and reason. | Do not collapse BLOCKED and known-constraint INFEASIBLE. |
| `EconomicStatus.COMPONENT_AVAILABLE`, `PARTIAL`, `SCENARIO_ONLY`, `BLOCKED` | Evaluator's import-energy component outcome; not full-bill completion. | Name import-energy component, covered intervals and scope. | `NOT_CALCULATED` is an orchestration/presentation state when no eligible economic evaluation was requested/available; it is not a PR #14 enum. A failure state also needs application-level semantics. |
| `ClaimStatus.ALLOWED` / `WITHHELD` | Whether a claim is permitted. | Use this as the decision; show scope separately. | Do not encode PARTIAL as a third `ClaimStatus`. |
| `ClaimScope.VERIFIED_BOUNDED`, `SCENARIO_ONLY`, `PARTIAL`, `NONE` | Scope/qualification of a claim, independent of disposition. | A partial energy component should read `ALLOWED · PARTIAL COVERAGE` (or equivalent), not claim status `PARTIAL`. | Preserve both dimensions: e.g. `status=ALLOWED, scope=PARTIAL`; a withheld claim uses `status=WITHHELD, scope=NONE`. |
| `EvidenceState.VERIFIED`, `PROJECT_ASSUMPTION`, `UNKNOWN`, `STALE` | Caller-provided assessment inputs. | Show provenance/qualification without treating the word VERIFIED as external proof. | In this prototype, even VERIFIED is a caller assertion; there is no authenticated evidence-service lookup. |
| `ClaimType.COMFORT_SERVICE` | A claim category the assessor can withhold. | It does not mean the engine computed comfort/service outcome. | No per-resource PASS/VIOLATION service evaluator exists in PR #14. Keep service outcome “not assessed” unless another qualified model supplies it. |
| `ClaimType.DEVICE_CONTROL` | A claim that must remain withheld. | Always display SHADOW/no device commands. | No write/control path is present. |

The four v2.3 scenarios are UI fixtures, not PR #14 output payloads. Their display labels are presentation examples and must be normalized by an explicit adapter before any API binding.

## 3. Important cross-layer gaps

1. **v2.3 claim status correction:** the first fixture draft used `status=PARTIAL` for covered import energy, unlike PR #14's binary `ClaimStatus` and separate `ClaimScope`. This has now been corrected in the v2.3 branch fixture: `decision=ALLOWED, scope=PARTIAL`; the economic assessment dimension remains PARTIAL. The UI renders “ALLOWED · 部分覆蓋.” The standalone JSON and embedded HTML are checked for exact equality by `validate-claim-fixtures.py`.
2. **Synthetic “COMPLETE”:** v2.3 uses `COMPLETE` for synthetic physical examples. PR #14 has no `COMPLETE` physical enum and explicitly scopes validation. The UI should make this a presentation label for its declared synthetic example and must never imply a site result. The application adapter should map an engine state, not infer one from UI copy.
3. **No-tariff case:** `generate_candidate()` requires an `EconomicContext` with aligned import rates and optimizes the supplied import-energy charge. Its tariff-free UI case can demonstrate assessment of a supplied schedule or a blocked/not-calculated economic result; it cannot claim that the current PR #14 generator produced an optimized candidate without an economic context.
4. **Service result:** the assessor's `COMFORT_SERVICE` claim remains withheld; it does not calculate an HVAC/EV/hot-water service outcome. v2.3's service-violation state is only a synthetic UI thought experiment.
5. **Evidence trust:** input `EvidenceRef.state` and references are caller-supplied. Passing a fixture marked VERIFIED proves neither a Macau site fact nor authenticated source lineage.
6. **No serving integration:** PR #14 contains no API DTO, HTTP endpoint, durable assessment lifecycle, immutable input snapshot, or browser client binding for these UI fixtures. Current main VS-001 does not fill that gap.

## 4. Required adapter boundary before an integrated slice

Before connecting UI and optimizer, define and review an application-owned result DTO that:

- has separate physical assessment, economic assessment per settlement scope/component, per-claim disposition and scope, per-resource service state, evidence provenance, review disposition, and lifecycle;
- maps the pinned optimizer enums without renaming away scope/unknown semantics;
- supplies `NOT_CALCULATED` only as an explicit application state, with a reason; does not synthesize a full-bill result from import-energy components;
- distinguishes generated candidates from supplied-schedule assessments and carries optimizer identity/version/search scope;
- carries authenticated evidence references and an immutable input manifest or marks those capabilities explicitly unavailable;
- denies cross-tenant/site access before returning status or result; and
- contains no device-command or execution-authority field in the SHADOW MVP.

Contract format, API operation ownership (APP-11 vs APP-05/06/07/08 composition), persistence and production runtime remain blocked on the applicable T0 decisions and review.

## 5. Acceptance cases for adapter/UI conformance

Use the same pinned input/output fixture and test that:

1. `ClaimStatus.ALLOWED + ClaimScope.PARTIAL` renders an allowed claim with explicitly partial scope, while the economic dimension reads PARTIAL.
2. `WITHHELD + NONE` renders a withheld claim with its reason and no numeric placeholder.
3. `SCENARIO_ONLY` never renders as verified/site-valid, even when the electrical balance is arithmetically valid.
4. Physical `BLOCKED` because core mapping is unresolved withholds dependent site-level physical/economic claims; independently qualified scopes, if supported later, remain separately named.
5. No economic context yields NOT_CALCULATED/blocking explanation at the application boundary and does not claim the PR #14 generator produced a candidate.
6. `COMFORT_SERVICE` withheld renders “service not assessed” (not pass); service violation examples stay synthetic.
7. Device control remains withheld in every result and review disposition.

Passing source checks or synthetic fixtures establishes no real tariff/site, service capability, savings, operator usability, or production readiness.

## 6. Next work

Correct the v2.3 claim fixture to represent claim **decision** and **scope** independently; pin the PR #14-to-UI mapping in an adapter proposal; then implement a contract-conformant vertical slice only after T0/contract-authority approval. Keep the browser render/interaction review separately open.


## v2.3 reconciliation update — 2026-10-05

The static UI fixtures were corrected to use separate claim `decision` and `scope` fields and to identify every scenario as a synthetic supplied-schedule assessment. A tariff-free scenario explicitly does not generate an optimizer candidate. The v2.3 fixture JSON was fetched back from PR #10 and its standalone copy matched the embedded JSON; both executable inline scripts passed `node --check` and the standard-library fixture validator passed. Current source blobs: HTML `6f199ddaee1f2a416b9925ce310a073b0455b054`, fixture `2d378478786b33ba24dc0024e0315a638d3d6624`, validator `ebd8c7bab94752a3cc1e9bc15e5b8df8454cc466`. No browser/API/optimizer integration is established.


## v2.4 and service-separation regression update — 2026-10-05

**Current compared revisions:** PR #14 head `99e0a7e943fdd66c987f28293658610b022b0a3b`; PR #10 v2.4 review source is recorded in `docs/02-product/prototype/source-load-dispatch/v2.4/REVIEW.md` (review blob `9350b7c38c892358bd6f887f61ec72414bc8664a`). These remain separate open proposal branches.

The v2.4 browser study fixes the narrow-screen overflow found in v2.3 and makes the synthetic claim table keyboard-scrollable. It still uses static synthetic states and is not fed by PR #14. In particular, v2.4's synthetic HVAC service-violation selector is not evidence that the optimizer evaluates comfort or service outcomes.

A missing regression assertion has now been added in PR #14 test blob `ffef3f40d8e46336160ebee2a29ec776628f26fd`:

- Test: `test_electrical_feasibility_does_not_assert_comfort_service`.
- With a balanced HVAC schedule and a supplied flexible-load limit, it asserts `PhysicalStatus.VALIDATED_WITHIN_SCOPE` and `DISPATCH_FEASIBILITY=ALLOWED`.
- For the same assessment it asserts `COMFORT_SERVICE=WITHHELD`, scope `NONE`, with the reason that service constraints are “not modeled.”

This pins the intended distinction in executable regression coverage without adding a comfort model, wire contract, device control, or canonical API. The check run started for PR #14 commit `99e0a7e943fdd66c987f28293658610b022b0a3b`; its completion and result must be verified separately before claiming the test passed.

The older v2.3-specific sections above remain historical. v2.4's exact-source browser review covers the claim-state section at 1440, 1024, 768, 375, and 320 CSS px and the four synthetic claim states at desktop and phone widths. It does not establish complete workflow, locale, screen-reader, operator, or WCAG validation. No UI/API adapter binding exists.


### Completed CI result for service-separation regression — 2026-10-05

The initial run exposed a test-only attribute typo (`ClaimReadiness.reason` instead of `reasons`); it was corrected on PR #14. The corrected exact head is `c235388db1678927f2c875bba6be88b0f01f25e2`, test blob `1f48655f21455c8f4918b82e3dcc15a4bcf2c170`. Runtime Bootstrap [#37336858769](https://github.com/lilinling12/macau-commercial-energy-os/actions/runs/37336858769) passed all four jobs; the Optimizer job ran **32 tests**, including the new service-separation regression. Authority Validation [#37336858856](https://github.com/lilinling12/macau-commercial-energy-os/actions/runs/37336858856) and Repository Hygiene [#37336858826](https://github.com/lilinling12/macau-commercial-energy-os/actions/runs/37336858826) also passed.

The test establishes only a code invariant for this bounded prototype: a supplied balanced HVAC schedule can be physically validated within scope while `DISPATCH_FEASIBILITY` is ALLOWED and `COMFORT_SERVICE` remains WITHHELD/NONE with a “not modeled” reason. It does not calculate comfort, establish real HVAC service, validate site inputs, or connect v2.4 to optimizer results. PR #14 and PR #10 remain proposals; no G7.9 exit or production architecture approval follows.
