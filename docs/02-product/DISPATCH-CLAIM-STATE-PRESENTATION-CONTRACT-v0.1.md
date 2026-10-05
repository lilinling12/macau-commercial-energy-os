# Dispatch Claim-State Presentation Contract v0.1

**Status:** Review proposal only. It is not a canonical API contract, approved product behavior, accessibility conformance result, or production implementation.  
**Rechecked:** 2026-10-05  
**Evidence baseline:** PR #10 head `88a7aa9a9c784ddd3cbc11e3e93220e6c711a507`; PR #14 head `0b69b7b5db04a2f2454bec691ecc8f609facc552`. Both are Draft/open/unmerged.  
**Purpose:** Define how the dispatch product should present electrical, service, economic, evidence, and review outcomes without collapsing them into one readiness badge.

## 1. Finding

The source/load dispatch workflow and G7.9 claim-readiness proposal define independent physical and economic assessments, resource-specific service boundaries, and claim-specific allowed/withheld outcomes. The bounded PR #14 experiment emits separate physical/economic status and claim decisions. Prototype v2.2 adds per-resource service rows, but its state selector is still a static, synthetic HVAC-only control; it is not bound to PR #14 or an API.

This creates a product integration requirement: the UI must preserve the result dimensions when those outputs are eventually connected. A green electrical balance cannot imply service satisfaction, economic eligibility, overall dispatch feasibility, or authority to act.

## 2. Proposed display dimensions

Keep each dimension separately named and scoped. These vocabularies are a presentation proposal; canonical API enums and reason codes remain subject to T0/T1 review.

| Dimension | Proposed values | UI meaning |
|---|---|---|
| Physical assessment | `NOT_REQUESTED`, `COMPLETE`, `PARTIAL`, `BLOCKED`, `INFEASIBLE`, `FAILED` | Whether the declared physical boundary and interval profile were assessed. Always show site/boundary and horizon. |
| Resource electrical feasibility | `ALLOWED`, `WITHHELD`, optionally scoped `PARTIAL` | Whether the result may claim the named resource schedule respects evidenced electrical limits. This is not service satisfaction. |
| Service outcome, per resource | `NOT_ASSESSED`, `PASS`, `VIOLATION`, `UNKNOWN` | Whether an HVAC comfort/recovery, EV departure-energy, or hot-water delivery requirement was assessed against its own evidence and service model. “PASS” requires qualified site evidence; synthetic pass must say “example only.” |
| Economic assessment, per settlement scope and component | `NOT_CALCULATED`, `COMPLETE`, `PARTIAL`, `BLOCKED`, `FAILED` | What account/contract/tariff scope and which billing components were actually evaluated. Never imply a bill total from an energy-only component. |
| Claim disposition | `ALLOWED`, `WITHHELD` | Whether each named assertion (for example, horizon import profile, demand charge, export compensation, savings, service feasibility) may be shown. Include scope and reason. |
| Evidence readiness | Repository evidence state plus missing/ambiguous/stale/assumed | Why a dependent result is qualified or withheld. Evidence class is not an assessment status. Show source, effective period, and affected interval/scope when available. |
| Human review | Existing proposed review disposition | A reviewer may accept for continued SHADOW observation, request evidence, or dismiss. Review does not authorize equipment control. |
| Execution authority | Always unavailable in this MVP | Label as “SHADOW · no device commands.” Do not render an enabled control affordance. |

Do not create a composite green “ready” state from these dimensions. A compact summary may combine them only as explicit text, such as: **“Electrical profile: partial · HVAC service: not assessed · bill economics: not calculated · SHADOW only.”**

## 3. UI mapping rules

1. Show the physical boundary, time window, timezone, data freshness and assessment scope beside the physical result. Label a calculated horizon maximum with its window; never call it tariff `Pu` unless the tariff meter window and billing-period scope are evidenced.
2. Render the claim ledger next to the result it governs. An allowed import profile must not visually promote withheld savings, demand charge, PV compensation, service, or control claims.
3. For each withheld claim, show a plain-language reason and the evidence/action needed to resolve it. Missing is not zero; stale is not current; assumed is not verified.
4. A resource row must separate electrical schedule treatment from service outcome. “Unchanged/fixed in this candidate” does not mean controllable; “electrically balanced” does not mean comfortable or service-feasible.
5. Economic values must name settlement account/scope, currency, period, component and coverage. Partial covered energy charges must not be presented as total bill or savings. Export quantity, compensation and cross-account credit are distinct claims.
6. Use text and icon/shape as well as color. Preserve the exact status in accessible names/live announcements; do not announce every chart update as a new result. Keyboard/touch behavior and reduced motion must remain available.
7. A review action records only a human SHADOW disposition against the identified assessment version. No button may imply deploy, apply, optimize live, or control.

## 4. Acceptance examples for a future UI/API vertical slice

| Fixture result | Required visible state | Forbidden implication |
|---|---|---|
| Valid mapped physical profile; no account/contract/tariff | Physical profile may be shown for its named scope; economics “Not calculated”; bill/savings claims withheld. | A bill total, tariff ranking, savings, or implied “zero cost.” |
| Core site/meter mapping missing or stale | Affected physical scope blocked with the mapping/source and interval reason; independent qualified scope may remain separately visible. | A site-wide profile or cost across the unresolved boundary. |
| Electrical balance qualifies; ESS limits absent/unknown | Retain only the qualified supplied/no-ESS profile if the result explicitly identifies that scope; ESS-dependent dispatch feasibility withheld. | ESS-safe/feasible, assumed SOC/reserve, or treating unknown limits as unlimited. |
| HVAC electrical shift is present; service model/comfort evidence absent | Identify the schedule as a scenario or fixed/unqualified electrical profile; HVAC service “Not assessed”; overall dispatch feasibility withheld. | Comfort maintained, controllable HVAC, service pass, or savings from the shift. |
| HVAC service fixture passes using synthetic values | Say “Synthetic example passes its stated bound”; retain the synthetic badge and keep site service unverified. | Site/user comfort validation. |
| Some exact VERIFIED import-rate intervals qualify, others do not | Show the economic component as partial with covered intervals/amount scope and withheld intervals/reasons; keep the physical profile separate. | Full-horizon tariff cost, full bill, or full-horizon savings. |
| PV export is measured but contract/payee/rate applicability is absent | Show evidenced physical export only; export compensation withheld. | Feed-in revenue, netting, or another building/account receiving a credit. |
| Reviewer accepts an assessment for observation | Append a dated SHADOW review disposition and preserve its assessment version. | Execution permission or equipment command readiness. |

The visible acceptance criteria should be tested against the same pinned synthetic fixture and API result once a vertical slice exists. Static prototype text alone is not evidence of API binding or runtime behavior.

## 5. v2.2 source audit and remaining UI work

The exact v2.2 source:
- has independent static cells for synthetic electrical balance, HVAC service, bill economics and SHADOW/control;
- provides four HVAC-only synthetic selector states and resource-specific evidence-needed text for HVAC, ESS, EV and hot water;
- explicitly marks ESS evidence synthetic/unverified and excludes EV/hot water from the candidate;
- does **not** represent claim-level `ALLOWED/WITHHELD`, assessment-level `PARTIAL/BLOCKED`, per-component economic coverage, or a mixed physical/economic/API result;
- is not connected to the optimizer, API, evidence store, site registry, or device path.

Therefore, treat v2.2 as a static service-state study, not the UI implementation of PR #14 claim semantics. The next prototype increment should add one mixed-state review fixture with independent dimension/claim rows, then inspect the actual render at desktop, tablet, mobile and narrow-mobile widths and exercise state changes. Do not connect it to real site data or imply production readiness in this increment.

## 6. Traceability and open decisions

- Source/load product flow and UI: PR #10 `SOURCE-AND-LOAD-DISPATCH-DESIGN-v0.1.md`, `v2.2/REVIEW.md`, and `v2.2/index.html`.
- Domain semantics: PR #10 `G7.9-STEP3-DISPATCH-CONTRACT-IMPLEMENTATION-MAP-v0.1.md`, `FLEXIBLE-LOAD-SERVICE-BOUNDARY-DESIGN-v0.1.md`, and `G7.9-STEP3-IMPLEMENTATION-BACKLOG-v0.1.md`.
- Experiment evidence: PR #14 implementation and its exact-head record. It remains a bounded Python SHADOW experiment, not accepted APP-11 or a production solver.
- Open: canonical status/reason vocabulary; multi-account/meter settlement representation; authenticated evidence references and immutable snapshots; complete tariff and demand-charge semantics; localized production copy; mixed-state browser review; operator/domain review; accessibility review; product owner acceptance.
- PR #10 and PR #14 remain Draft/open/unmerged. G7.9 Step 3 remains open. This document does not resolve APP-11 ownership, D-065 contract authority, G6.9/G7.8 stack precedence, or production architecture.

