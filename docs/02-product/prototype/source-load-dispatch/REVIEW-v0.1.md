# Source/Load Dispatch Prototype — Review Record v0.1

**Review date:** 2026-10-04  
**Prototype:** separate dispatch-study v0.3; Traditional Chinese; all values synthetic  
**Status:** interaction study only; not an approved visual system, product scope, tariff evaluation, field capability, user-tested design or production UI.

## Design task and comparison basis

This study asks whether a site operator can read a schedule-first supply/load comparison and spot the evidence boundary. It is separate from the repository's PR #8 v0.11 core-flow stimulus and does not replace its bill/interval/baseline-result comparison.

The local browser opened the prototype through a loopback server. Its accessibility tree exposed the rendered initial state at the browser's default viewport. The viewport's physical CSS pixel dimensions were not captured. The browser snapshot confirmed:

- Traditional Chinese labels, Macau example time context and a visible “synthetic / not site data” notice;
- one-hour example grain and average-power units, explicitly saying the CEM billing interval is unverified;
- baseline and candidate grid import, total-load series, onsite-PV and storage labels;
- the proposed HVAC reduction in 15:00–16:00 and equal rebound at 17:00–18:00;
- illustrative per-period power-balance figures and a table alternative control;
- tariff/contract readiness unverified, no bill-grade amount and no device-control action;
- initial baseline selected; SHADOW candidate state; no measured outcome.

## Corrections made during review

1. Added a candidate-total-load trace after finding that the earlier legend named it without plotting it.
2. Added a 17:00 rebound period so the illustrated HVAC shift does not appear to erase load.
3. Matched the candidate grid-import trace and inspectable example to the rebound hour.
4. Changed the selector/caption from 15-minute intervals to a one-hour synthetic example, matching the displayed hourly points. No implication is made that one hour is CEM's settlement interval.
5. Labeled the balance as power only and noted ESS conversion loss is omitted.
6. Kept the tariff unresolved, withheld bill-grade economics, preserved the SHADOW boundary, and kept equipment control disabled.

## 2026-10-04 interval-model consistency pass

A source review found that the plotted values were described as hourly averages but drawn as interpolated lines, the 18:00 horizon boundary looked like another point, and the chart displayed multiple ESS bars while the table only explained one discharge interval. Updated v0.3 to use six interval-aligned step series from 12:00–18:00, mark 18:00 as the exclusive horizon end, show only the candidate 20 kW ESS discharge during 15:00–16:00 in a separately labelled annotation lane, and expose all six intervals in the data table. The fixture and table now use the same baseline/candidate values and HVAC −30 kW at 15:00 / +30 kW rebound at 17:00.

Added `source-load-dispatch-fixture-v0.1.json` and a standard-library static checker `validate-source-load-dispatch-fixture-v0.1.py`. The checker passed: all six baseline and candidate source/load balances, one-hour interval continuity and +08:00 offsets, total HVAC shift/rebound neutrality, allowed/withheld-claim policy, and all prototype table values/formula strings match. It also checks that the SVG uses step geometry and discloses omitted ESS charge/SOC/efficiency/losses. This validates internal synthetic-example consistency only. It does not prove energy integration, battery feasibility, comfort, tariff/settlement, savings, field capability, or optimizer behavior.

The updated prototype was re-opened in the local browser at its default viewport. Its accessibility tree confirms the six-interval step-chart description, 18:00 end boundary, selected comparison data, unverified tariff, and disabled equipment control. The actual CSS-pixel viewport is still not captured; pixel-level inspection at 1440/1024/768/375, the table-toggle interaction, keyboard/focus/dialog behavior, measured contrast, and screen-reader operation remain unverified.

The figures are still incomplete as an energy schedule: the ESS charge history/SOC path, conversion losses, full-horizon interval integration, comfort limits, constraints and all site mappings are not validated. No saving claim or PV export credit is displayed.

## Inspection coverage

| Dimension | Checked | Not checked |
|---|---|---|
| Rendered state | Initial load at browser default viewport; accessibility-tree snapshot | Pixel screenshot inspection and measured viewport size |
| Responsive sizes | Source contains 1050, 760 and 390 px breakpoints | Rendered 1440, 1024, 768 and 375 px comparisons; clipping/zoom/reflow |
| UI states | Initial synthetic baseline selected, candidate available, SHADOW and control-disabled labels present | Candidate switching, opening evidence modal/table, dismiss/review outcomes, failure states or keyboard focus walkthrough |
| Language | Traditional Chinese only | Portuguese and English, locale fallback, real Macau terminology, date/number/currency formats, screen-reader language metadata |
| Accessibility | Semantic headings, chart name/description, text status alongside color, source-table alternative in source, reduced-motion CSS in source | Measured contrast, visible focus, full keyboard/dialog behavior, screen-reader test, WCAG conformance |
| Validation | Static arithmetic inspection of two example periods and browser semantic content | Domain-expert review, operator/finance usability, customer data, site/contract validation, field behavior |

## Next review pass

Render at agreed desktop/tablet/mobile sizes, inspect hierarchy and horizontal overflow, measure text/status/chart contrast, test all controls by keyboard and assistive technology, and compare the schedule-first view with an evidence-first composition on the same tasks. Translate full flows only after the intended role/site language scope is reviewed. Domain-review a complete interval/SOC-balanced fixture before using it to accept optimizer or product behavior.

## 2026-10-04 source-level accessibility follow-up

A static source pass on the PR #10 prototype changed the two scenario choices from `div[role=button]` to native `button` elements with `aria-pressed`, added visible `:focus-visible` styling, and added `aria-controls`/`aria-expanded` to the table toggle. The evidence dialog now traps Tab focus, closes on Escape/backdrop, and restores focus to its opener. The table's programmatic scroll checks `prefers-reduced-motion`. These are source-level changes, not validated browser behavior.

The previous browser accessibility-tree observation applies to the earlier source. A fresh preview of the updated local HTML was rejected because the browser tool blocks its local-file URL; no alternate serving or browser route was attempted. Therefore current rendered layout, viewport dimensions, candidate switching, table toggle, focus order/dialog behavior, measured contrast and screen-reader behavior remain unchecked. Do not treat these source changes as WCAG conformance or accessibility sign-off.

## Source and authority notes

The schedule-first job follows the explicit user direction and the product objective/boundaries in `main` D-001/002/003/004/005/006/009/013/019/055/056/060/061/077. Product requirements, visual direction, pilot/user hypotheses, locales and production architecture remain proposed until the applicable owner review and evidence are recorded. This review does not close G1/G2/G3/G6/G6.9/G7/G7.9, validate PR #8, or authorize a device write path.


## 2026-10-04 fixture-verifier execution follow-up

A direct check of the PR branch found the verifier still referenced the earlier local filenames, while the committed fixture and prototype are `v0.3/fixtures/synthetic-dispatch.json` and `v0.3/index.html`. Updated `validate-fixture.py` to use those committed paths. The verifier logic was then run against the exact PR-branch fixture and HTML contents (both byte-for-byte matched the inspected local copies, and the verifier matched after only normalizing its input paths). Result: **PASS** for six intervals, source/load balances, explicit HVAC shift/rebound, claim restrictions, and table alignment. This remains a static synthetic example check; it does not validate a live site, tariff, optimizer, visual rendering or device behavior.
