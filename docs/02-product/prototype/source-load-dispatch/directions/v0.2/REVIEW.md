# Dispatch visual direction study v0.2 — review record

**Date:** 2026-10-05  
**Artifact:** `index.html` (local study source: `work/dispatch-direction-v02-study.html`)  
**Status:** exploratory; direction A and direction B are both unapproved. This review does not freeze product scope, palette, production UI, locale set, or architecture.

## Review task

Help an energy operator compare one synthetic six-hour source/load schedule, identify the HVAC rebound and ESS recharge effect on the displayed window peak, inspect interval evidence, and understand why no bill-level cost or savings conclusion is available. The prototype is a dispatch-operations study, not a marketing homepage.

## Concepts compared

- **A — 潮線:** light, timeline-first workspace. Grid import/load and PV are read across the whole interval window, with an evidence rail alongside on wide screens and a disclosure table for exact interval values.
- **B — 夜航:** dark, interval-first workspace. The operator selects an interval and reads import, load, PV, ESS, HVAC and SOC values before expanding the same-window schedule.

Both directions use the same values and claims. The visual comparison does not establish operator preference. The UI/UX Pro Max searches recorded during this iteration returned generic marketing/conversion or unrelated visual patterns, so they were rejected as off-fit evidence rather than adopted as a design system. The project UI/UX skill and review checklist guided the task and boundary review. No Apple/Google/Awwwards/Webby/FWA compliance, award quality, or user validation is claimed by this candidate review.

## Evidence and limits shown in the prototype

- Six synthetic one-hour intervals; 18:00 is the exclusive window end.
- At 15:00–16:00, grid import is shown as 480 → 430 kW; ESS discharges 20 kW and HVAC changes by −30 kW.
- At 16:00–17:00, ESS recharge is 24.691 kW in the example; the displayed candidate import is 509.691 kW.
- At 17:00–18:00, HVAC rebounds by +30 kW and displayed import is 480 → 510 kW. The six-hour candidate maximum (510 kW) exceeds the baseline maximum (485 kW).
- This window maximum is not represented as billing-period Pu. No contract, tariff, account/meter mapping, settlement rule, field device capability, comfort envelope, or site data is supplied. The prototype therefore withholds bill amount, savings, export income, feasible-control and live-control claims.
- All scenarios are synthetic. SHADOW review controls change page-local state only; they do not persist, audit, authorize or send commands.

## Changes made after inspection

- Replaced four shell navigation links that targeted absent page anchors with static current-section labels; this file is a single-screen visual study, not a multi-page application.
- Replaced the evidence-rail link to a nonexistent `#evidence` target with explicit text that a full-product evidence-list entry point is not implemented.
- Corrected the orange chart legend from HVAC movement/rebound to candidate total load, matching the plotted series.
- Added a narrow-screen instruction that the curve can scroll horizontally and exact numbers are in the table.
- Added a visible keyboard focus outline for the horizontally scrolling chart region.
- Raised selected small status/interval labels from 9px to 10px and kept touch navigation labels at a minimum 44px target height.

## Checks performed

- Rendered the local candidate in the in-app browser. Captured preview image dimensions were 418 × 591 pixels; the available browser tool did not expose the CSS viewport or device scale, so this is recorded as screenshot size, not as a verified CSS viewport.
- Accessibility-tree inspection confirmed both concepts are exposed, direction switching changes the active concept, and the synthetic/non-field and SHADOW/no-control limits remain present.
- Switched from A to B. Selected 15:00–16:00 and verified 480 → 430 kW import, 590 → 560 kW load, 110 kW PV self-use, 20 kW ESS discharge, HVAC −30 kW, and SOC 40 → 17.778 kWh. Then selected 17:00–18:00 and verified 480 → 510 kW import, 540 → 570 kW load, 60 kW PV self-use, HVAC +30 kW rebound, and SOC 40 → 40 kWh.
- Changed SHADOW disposition to “需補證據”; the page exposed only its local, non-persistent status message. Expanded the six-interval table and checked that it exposed all six rows and the corresponding interval values.
- Source inspection found no remaining anchors after removing the dead links. No automated test suite was added or run for this visual study.

## Selected text/background contrast pairs

Ratios use the WCAG relative-luminance contrast formula on the literal CSS hex values. This is a limited color-pair calculation, not a full WCAG audit; it does not cover every state, chart line, SVG label, focus indicator, disabled state, font size, or actual user setting.

| Direction | Foreground / background | Ratio |
|---|---|---:|
| A | body `#152c3a` / paper `#f5f5ef` | 13.20:1 |
| A | muted `#5c7077` / white `#ffffff` | 5.20:1 |
| A | teal `#007f78` / white `#ffffff` | 4.88:1 |
| A | orange `#b7502c` / white `#ffffff` | 5.00:1 |
| A | amber `#654708` / `#fff0c9` | 7.55:1 |
| B | body `#e8f1f3` / paper `#101f2b` | 14.61:1 |
| B | muted `#aec1c7` / surface `#172c39` | 7.73:1 |
| B | teal `#50d5c1` / surface `#172c39` | 7.99:1 |
| B | orange `#ff986e` / surface `#172c39` | 6.85:1 |
| B | amber `#ffd782` / `#3a3323` | 9.12:1 |

## Still open

- Compare at controlled desktop/tablet/mobile CSS viewports and text enlargement; inspect chart and table behavior at narrow widths.
- Complete keyboard coverage, screen-reader review, reduced-motion review and broader contrast checks.
- Produce and review full Traditional Chinese, Portuguese and English task flows; this study is Traditional Chinese only and is not multilingual support.
- Validate terminology, interval data, evidence needs and task priorities with Macau commercial-building operators and relevant local reviewers.
- Revisit whether the timeline-first or interval-first information hierarchy best supports the agreed MVP after product scope and owner decisions are available.


