# Source/load dispatch study v3.3 — review record

**Status:** Unapproved product and UI study on PR #10 draft branch `product/source-load-economic-dispatch`. It does not close G7.9 Step 3, select production architecture, validate a Macau site, or authorize equipment control.

**Local artifact fingerprints:** `index.html` SHA-256 `FC989B8BCB800BEEB2BB29CFB8FE1CF1B4616B4A0C2679124AA077F16996AD79`; fixture SHA-256 `82B38BA9F6FBC431C09B2DD1143C4659BC76D35207228D8A182DE701879170D4`; validator SHA-256 `F8287C3B82844C6F290F6CDA8DE77FBBE42B4DE2A3440DA6B0C36D5268387E07`.

## What changed

v3.3 connects the six-stage review page to the PR #14 synthetic dispatch fixture. The schedule chart, interval table, import-energy and horizon-peak metrics, and Stage 4 claim states now derive from the same fixture. Stage 4 exposes two explicit views:

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
