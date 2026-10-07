# Source/load dispatch study v3.5 — service-scope review

**Status:** Unapproved operator-workflow and UI study. It does not close G7.9 Step 3, approve service semantics, validate a Macau site, or authorize equipment control.

## User task and design decision

At Stage 4, an operator needs to see which changed resources prevent an overall dispatch-feasibility claim, what is not evaluated, and what site evidence would be needed next. A single site-wide withheld badge was insufficient because it concealed the HVAC, EV, and hot-water service gaps present in the pinned synthetic schedule.

The study keeps the schedule and claim summary primary, then adds a compact resource-level service section. It uses separated rows rather than another KPI-card grid. Each row shows resource kind/fixture ID, schedule intervals changed, a text status, and the missing service evidence. It does not surface an execution control.

## Source and semantic pins

- Base UI: PR #10 v3.4 index blob `44e980844c82cc0206c71ab70741eb98a65e9277`.
- Fixture: PR #10 v3.4 fixture blob `17906365997be7a529222b3c120e138ef336bb8c`.
- Fixture source: PR #14 commit `e02ed268c23d9cd62f2641db05923befa88ed281`; optimizer blob `2d3256801f0ddce6b849c648c160f5a32fd90a27`; assessment blob `275a1cd79613cf1997456916f1b59833fb683109`.
- Service outcome vocabulary follows the review proposal in `FLEXIBLE-LOAD-SERVICE-BOUNDARY-DESIGN-v0.1.md` §9. The current fixture has no service evaluators, so all three changed loads display “Not assessed.” This is neither a service pass nor a known violation.

## What the prototype displays

- HVAC/chiller: schedule differs at 11:00–12:00, 13:00–14:00 and 14:00–15:00; the fixture has no thermal/comfort or full recovery model.
- EV charging: schedule differs at 11:00–12:00 and 14:00–15:00; no authorized departure window or target energy/SOC exists in the fixture.
- Hot water: schedule differs at 11:00–12:00 and 13:00–14:00; no draw/delivery, reserve or hygiene-cycle service model exists in the fixture.
- Service and recovery horizon remain unassessed. The exact times above are schedule-difference intervals in the fixed synthetic scenario; they do not identify a site's equipment or service-response period.
- ESS remains under the electrical operating-envelope view (charge/discharge/SOC). Its SOC is not represented as a user-service outcome.
- Economic assessment remains blocked; the assumed rates do not become a Macau tariff, saving or bill amount. SHADOW review remains page-local; no device command path is present.

## UI/UX guidance applied

- The project `energy-operations-ux.md` says to keep schedule comparison, evidence scope and service constraints inspectable, distinguish physical flows from settlement, and avoid familiar layouts when they do not serve the task. This is why the addition is a three-column, text-labeled evidence list rather than another dashboard tile group.
- The project `quality-review.md` and UI/UX Pro Max search emphasize explicit status feedback and meaningful, contextual labels. The search's generic data-dense dashboard recommendation was rejected as a template; the UX search did not return a domain-specific service-status pattern, so the project guidance and source semantics govern this targeted panel.
- Status is written in words and uses an amber neutral/unassessed treatment; color is not the only status carrier. New text is localized in Traditional Chinese, English and Portuguese draft.
- This is not a complete localization review. Existing prototype translation drafts, legal terminology, dates/units/currency, Portuguese review and full workflow parity remain open.

## Validation and review coverage

- `validate.py` passes its source/fixture checks: six aligned intervals, three changed resources, exact changed schedule times, synthetic/not-assessed copy in all three locales, and no command form.
- Inline JavaScript syntax validation passed.
- Browser rendering covered Stage 4 at 1440×900, 1024×900, 768×900, 375×800 and 320×800 CSS pixels, each in Traditional Chinese, English and Portuguese draft. All 15 combinations retained the three resource rows and had no document-level horizontal overflow. At 375/320px, service rows stack into one column and long evidence text wraps.
- Interactions exercised: keyboard-navigate to Stage 4, switch each locale, and keyboard-switch the claims display to its UI-only partial-coverage example while preserving the service panel. The focused Stage 4 step showed a 3px solid outline plus inset teal focus ring. No browser script errors occurred. The Stage 4 panel exposed one heading, three resource rows, textual statuses and evidence descriptions in the rendered page.
- Visual review inspected full-page captures at 1440px Traditional Chinese and 375px Portuguese. No clipping, overlap, or status-color-only meaning was visible in the new panel. The text color `#684a19` on `#fff8e9` has a calculated 7.69:1 contrast ratio; this is only the new status label pair, not a full-page contrast audit.
- Full-page screenshot evidence is stored at `evidence/stage4-zh-Hant-1440.png` (CSS viewport 1440×900) and `evidence/stage4-pt-375.png` (CSS viewport 375×800; Portuguese draft copy). These show two representative cases from the 15-case matrix, not every viewport/locale combination.
- Full keyboard traversal of all six stages and controls, zoom/text enlargement, screen-reader output, non-text contrast, complete locale review, and formal WCAG 2.2 conformance remain unreviewed. No representative operator or site-domain user tested this study. It makes no claim of usability validation, production readiness or award-level quality.

## Remaining product decisions

- Product/domain owners must accept or revise the service outcome vocabulary, uncertainty rule, affected scope and overall-feasibility composition before a canonical API or production behavior is frozen.
- The first pilot's user, building, service obligations, asset identifiers, evidence sources, service/recovery horizon and locale priorities remain unknown.
- The three language labels are prototype copy only; complete reviewed locale catalogs are still needed before calling the product multilingual.

## Result-projection check refinement — 2026-10-07

The static verifier now pins the optimizer/assessor source blobs and checks the result semantics consumed by the page: physical scope remains scenario-only; economic status stays blocked with null monetary fields and no covered intervals; the import profile is allowed only as scenario scope; overall dispatch feasibility and bill, savings, control, service and cross-site claims remain withheld. It also checks that the page's result-metric and claim-rendering functions read those fixture fields.

This is source/fixture consistency coverage, not a browser assertion that every mapped value is correctly announced, not an API adapter test, and not an operator or site validation.
