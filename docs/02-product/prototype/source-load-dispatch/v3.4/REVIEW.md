# Source/load dispatch study v3.4 — review record

**Status:** Unapproved operator-workflow and UI study on PR #10 draft branch `product/source-load-economic-dispatch`. It does not close G7.9 Step 3, select a production architecture, validate a Macau site, or authorize equipment control.

## Source and artifact pins

- PR #14 generated fixture source commit: `e02ed268c23d9cd62f2641db05923befa88ed281`.
- Optimizer blob: `2d3256801f0ddce6b849c648c160f5a32fd90a27`; assessment blob: `275a1cd79613cf1997456916f1b59833fb683109`.
- v3.4 Git blobs — index.html: `44e980844c82cc0206c71ab70741eb98a65e9277`; dispatch-projection-fixture.json: `17906365997be7a529222b3c120e138ef336bb8c`; validate.py: `3c6e93205330e39965c03b510e4355cafc8a875b`.

## What changed

- v3.4 is the first UI study version pinned to the corrected PR #14 feasibility output. When changed HVAC/EV/hot-water schedules have no service evaluator, the fixture retains scoped physical/electrical profile claims but withholds `DISPATCH_FEASIBILITY` with scope `NONE`; `COMFORT_SERVICE` remains withheld.
- Stage 4 names the overall feasibility claim and explains that changed-load service is not modeled while the electrical profile remains independently inspectable.
- Generic withheld labels now direct the user to the claim-specific reason. They do not assume every withheld state means missing evidence.
- Economics remain blocked. The rates are project assumptions, not verified Macau tariffs. No service/API, persistence, site connection, or device command path is added.

## Verification

- The static validator passed: source pins, six contiguous intervals, PV partition and bus balance, horizon import/peak totals, blocked economics, withheld overall-feasibility status/scope/reason, localized claim/status labels, and local-only fixture loading.
- Extracted inline JavaScript passed `node --check`.
- Browser review opened Stage 4 with the current fixture. Traditional Chinese, English, and Portuguese draft showed the withheld state and its reason. A narrow in-app browser view was inspected; no formal viewport-overflow measurement was performed for v3.4.
- PR #14 exact head `ccbfa7011f66f86d0a2d541776b02c80eea3df7a` passed Runtime Bootstrap (Optimizer, Contract Fixtures, Edge Runtime, Platform API), Authority Validation, and Repository Hygiene. These checks do not prove service models, site suitability, tariff validity, WCAG conformance, or operator usability.

## Limits

Portuguese remains draft. HVAC thermal response/comfort/recovery, EV departure-energy service, hot-water delivery, Macau site evidence, contract/tariff applicability, demand billing, realized savings, screen-reader support, full WCAG review, and owner approval remain open.
