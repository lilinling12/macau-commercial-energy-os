# Six-stage source/load dispatch prototype v3.0 — review record

**Review date:** 2026-10-07  
**Status:** Design-study prototype on PR #10; not product approval, site validation, or architecture approval.  
**PR branch before this addition:** `product/source-load-economic-dispatch`, head `7f7c4a1cb87e260845acab761455f6133debdab6`.  
**Prototype source:** `docs/02-product/prototype/source-load-dispatch/v3.0/index.html`, SHA-256 `CC2B4FDD1B147F2A1B66B370EDBAC6E5484479AD64F8CEAFAD193789EB2ED0FF` (38,992 bytes at review time).  
**Source scenario:** v2.9 fixture `docs/02-product/prototype/source-load-dispatch/v2.9/dispatch-projection-fixture.json`, branch blob `0e746cbe54532e58221529f38c7a2583d1787c4b`; all evidence is project-assumption data.

## What this iteration adds

v3.0 brings the existing result comparison into one navigable six-stage study flow:

1. Data, contract, meter, forecast and asset evidence with missing inputs visible.
2. Site physical-energy model separated from account/contract/settlement scope.
3. Baseline and candidate comparison for grid import, on-site PV, ESS charge/discharge/SOC, and flexible-load tasks.
4. Economic, physical, service and claim limits shown separately.
5. Page-local human research review with no server submission or field action.
6. Monitoring/replay prerequisites, with current replay unavailable until measurements and immutable inputs exist.

A review pass found that the stage label could imply an actual forecast. Stage 1 now lists forecast inputs as missing, and stage 3 says it uses the fixed v2.9 synthetic schedule without forecast data or a site service model.

The displayed baseline import is 8, 8, 6, 4, 8, 10 kW; the candidate is 9, 9, 11, 3, 5, 7 kW. Both total 44 kWh over six hours, while the interval maximum rises from 10 to 11 kW. The page explicitly says this is not billing demand/Pu. PV export, settlement credit, bill savings, service feasibility, controllability and execution are not asserted.

## Browser and interaction review

The local page was rendered and reviewed at CSS viewports **320×900, 375×812, 768×900, 1024×900 and 1440×900**. At each width, document and body scroll widths stayed within the viewport. The compact chart summary and six interval cards appear at 320/375; the SVG and full table are used at wider widths. Screenshots were visually inspected at 375×812 and 1440×900.

Interaction checks:

- All six stages were opened and their content/state labels were reviewed.
- ArrowRight from stage 3 selected stage 4; tab selection and roving tabindex updated.
- Selecting “要求修改情景” updated the live review status. The choice is explicitly page-local and resets on reload.
- Workflow buttons have a 44 px minimum height; no duplicate IDs were found.
- Browser console reported no errors.

These are focused prototype checks. They do not establish full keyboard-only coverage, screen-reader usability, WCAG conformance, localization quality or user validation.

## UI/UX skill review

Applied the `ui-ux-pro-max` skill and ran a design-system search. Its first match returned a real-time operations **landing-page** pattern with glassmorphism and prominent conversion actions; that pattern does not fit this evidence-first dispatch console, so it was rejected. A narrower sustainable-energy product search returned energy/utilities dashboard, paper-like/data-dense and earth/sky/solar palette suggestions. These are useful references for further exploration, not selected tokens or an owner-approved visual direction.

The current prototype uses a light paper surface, dark text, teal energy series and amber evidence status. Sample token contrast calculations were: ink on white 14.32:1; muted text on white 5.86:1; teal on white 5.01:1; white on teal 5.01:1; focus blue on white 5.71:1; white on navy 14.25:1; warning text on warning surface 8.16:1. This is a token sample, not an exhaustive contrast audit. Some dense metadata remains 11 px and should be reviewed at larger text settings.

## Scope and remaining work

- This integrated flow is Traditional Chinese only. It is not complete localization. PR #10 v2.9 separately contains Chinese, English and draft Portuguese for a single result page; that does not prove full-flow coverage or settle locale selection/Portuguese region.
- No Macau site, meter topology, contract, tariff, PV export right, weather/load forecast, asset service model or authorization was supplied.
- The schedule is a fixed synthetic example, not a validated optimizer recommendation, forecast, bill calculation, dispatch feasibility result or device command.
- No award-level or user-research claim is made. This iteration did not re-evaluate Awwwards, Webby or FWA case studies; see the existing UX direction review for prior reference research and its limits.
- Next design pass: bring approved locale scope into the full flow; review long/short copy at small screens and text enlargement; complete state-by-state keyboard and contrast review; reconcile this flow with the existing localized studies before deciding which prototype should become the product baseline.

No production architecture, product scope, palette, locale set, Gate or technology is frozen by this prototype. G7.9 Step 3 remains open.
