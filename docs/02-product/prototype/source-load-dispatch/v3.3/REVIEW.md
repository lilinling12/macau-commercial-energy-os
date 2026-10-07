# Source/load dispatch study v3.3 — review record

**Status:** Unapproved product and UI study on PR #10 draft branch `product/source-load-economic-dispatch`. It does not close G7.9 Step 3, select production architecture, validate a Macau site, or authorize equipment control.

**Local artifact fingerprints:** `index.html` SHA-256 `86C79C77ED1EEADD84C15080DAD2CDEFD53D7DB3BCCCA352AB9FABB76E34FA57`; fixture SHA-256 `82B38BA9F6FBC431C09B2DD1143C4659BC76D35207228D8A182DE701879170D4`; validator SHA-256 `A67612BE0DBC0DA9E43A0A043AC5B818B333CBB19EAF6A8C844260973F4EEEC0`.

## What changed

v3.3 connects the six-stage review page to the PR #14 synthetic dispatch fixture. The schedule chart, interval table, import-energy and horizon-peak metrics, and Stage 4 claim states now derive from the same fixture. It discloses that the optimizer objective uses assumed sample import rates; those rates do not establish a Macau contract, and economic assessment remains blocked. Stage 4 exposes two explicit views:

- **PR #14 fixture output:** the fixture's six allowed scenario-scoped claims and its withheld claims, including bill, demand, export compensation, savings, service, controllability, cross-site credit and device control. It identifies the source commit and shows economic assessment as `BLOCKED`.
- **Partial-coverage UI example:** a separately labeled presentation state for four covered intervals (09:00–13:00) and two uncovered intervals (13:00–15:00). It shows no amount, does not treat missing intervals as zero, and withholds a whole-window bill, savings and demand charge. It is not emitted by the PR #14 fixture or optimizer.

No service/API request or device command path is added. The page performs one local fetch for its fixture. `SHADOW` review remains page-local and is not persisted or submitted.

## Source lineage

- PR #10 branch head before this addition: `f5642e58e1c933de3af37ce42fb002e78e02b177`.
- PR #14 was open, draft and unmerged at head `deed7683a8b0ce3a811966ab8fc3b030695debad` when reviewed.
- Fixture file is copied from PR #10 v2.9 blob `0e746cbe54532e58221529f38c7a2583d1787c4b`. Its declared engine source is commit `9b80adca9243a0ae9a7bd666f0efee1acfc6309a`, optimizer blob `2d3256801f0ddce6b849c648c160f5a32fd90a27`, assessment blob `534ae269a7949601bd4504271e0076369807a68f`.
- Fixture status is `SYNTHETIC_SCENARIO_ONLY`; physical status is `SCENARIO_ONLY`; economic status is `BLOCKED`, with no covered intervals or monetary delta. All input evidence is project assumption data.

## Verification performed

- `validate.py` passed. It checks source pins, six contiguous intervals, PV partition and site-bus balance, horizon energy/peak totals, economic-blocked and withheld-claim invariants, local-only fixture loading, and the distinction between optimizer output and the UI-only partial-coverage example.
- Extracted JavaScript passed `node --check`.
- Rendered in the in-app browser; no console errors were observed.
- Reviewed CSS viewports **320×900, 375×900, 768×900, 1024×900 and 1440×900**. The tested page states had no document/body horizontal overflow. At 375×812, the six-stage rail and wide schedule table remain internally scrollable; the page itself stays within the viewport.
- Exercised fixture output and partial-coverage selection, Traditional Chinese/English/Portuguese draft labels, schedule values and SOC pairs, and page-local Shadow review. The review selection did not call a service.
- UI/UX Pro Max targeted searches returned: visible labels for controls, avoid horizontal overflow, and use a contained horizontal-scroll or card treatment for wide tables. The existing table uses a labeled scroll region; stage navigation can scroll horizontally on narrow screens. The output was applied as review input, not adopted as a product-wide design system.

## Limits and next evidence needed

This is browser and static-fixture evidence only. It does not prove tariff applicability, meter topology, PV export rights, equipment capability, comfort/service feasibility, demand billing, savings, production security, durable reviews, replay, full localization quality, WCAG conformance, or operator usability. Portuguese remains marked draft. Screen-reader and full keyboard audits, measured contrast across all states, localization review and site/operator validation remain open.

The existing visual direction remains unapproved. The prototype is an operator-workflow study and should not be treated as a marketing homepage or final production UI. G7.9 Step 3, APP-11 semantics, and production contract/schema authority remain open.


## Overall feasibility wording reconciliation — 2026-10-07

Cross-review found a contract mismatch: PR #14's fixture emits `DISPATCH_FEASIBILITY=ALLOWED` when the HVAC electrical schedule is within its supplied envelope, while `COMFORT_SERVICE` is withheld because service is not modeled. PR #10's draft `DISPATCH-CLAIM-STATE-PRESENTATION-CONTRACT-v0.1.md` acceptance example says an HVAC shift without service evidence may be shown as an electrical scenario, with service “Not assessed” and **overall dispatch feasibility withheld**.

The v3.3 claim label now says “Electrical constraints only” in Traditional Chinese, English and Portuguese draft, and explains that service is unassessed and the overall feasibility conclusion should not be claimed under the product presentation proposal. This intentionally exposes the discrepancy; it does not rewrite the PR #14 fixture's emitted claim or pretend the two draft artifacts are already reconciled. PR #14 subsequently aligned the experimental `DISPATCH_FEASIBILITY` status to that draft rule at exact head `ccbfa7011f66f86d0a2d541776b02c80eea3df7a`, while keeping its service claim withheld. This v3.3 page remains pinned to earlier source commit `9b80adca9243a0ae9a7bd666f0efee1acfc6309a`; it is not current PR #14 output. A later prototype version should regenerate and pin the fixture to the corrected experiment before claiming current behavior. Owner/domain approval and service model coverage remain open.

The existing static validator passed after the copy change. This validates its pinned synthetic fixture and existing presentation-boundary assertions only; it does not validate the claim semantics, localization quality, browser layout after the longer copy, or owner approval.
