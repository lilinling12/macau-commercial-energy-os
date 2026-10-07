# Source/Load Dispatch Prototype v2.5 — Unified Synthetic Assessment Study

**Status:** Unapproved, UI-only synthetic study. It does not approve product scope, the visual system, API semantics, accessibility conformance, or production architecture.  
**Base:** PR #10 v2.4 source, HTML blob `35b0843b6b87272c407bc5df2c80c641e69cad1e`. The v2.4 directory remains unchanged.  
**Purpose:** Remove the misleading impression that independently selectable HVAC and claim states describe one result. One fixed synthetic assessment case now drives the local cross-dimension status cards and claim table.

## Change

The four existing claim fixtures remain the only case selector. The selector and live summary now appear above the status cards, in reading order. A selection updates the displayed physical, HVAC-service, ESS, economic and claim states, the named HVAC resource card, the ESS evidence card and the claim-reason table. The separate HVAC radio group and duplicate dimension tiles were removed.

The four examples produce these states:

| Case | Physical | HVAC service | ESS | Economic |
|---|---|---|---|---|
| Partial tariff coverage | PARTIAL | NOT_ASSESSED | WITHHELD | PARTIAL |
| No applicable tariff | COMPLETE | NOT_ASSESSED | WITHHELD | NOT_CALCULATED |
| Missing meter mapping | BLOCKED | UNKNOWN | UNKNOWN | BLOCKED |
| Synthetic service violation | COMPLETE | VIOLATION | WITHHELD | NOT_CALCULATED |

## Browser review — 2026-10-06

Reviewed the v2.5 local rendering in the Codex in-app browser at **1440×900, 1024×900, 768×900, 375×812, and 320×800 CSS px**. All four cases were selected at each viewport (20 viewport/case combinations). The active button exposed `aria-pressed=true`; the corresponding status fields and claim table changed to the selected fixture. At each viewport, document `scrollWidth` equalled `clientWidth` (1425, 1009, 753, 360, and 305 px respectively); no document-level horizontal overflow was observed. These client widths exclude the browser's vertical scrollbar.

Keyboard activation with Enter selected the no-tariff case. No JavaScript console errors were recorded. The fixture still declares `apiConnected=false` and `deviceControlEnabled=false`; the visible device-control action remains disabled.

## Explicit boundary and remaining work

This consolidates the **presentation state only**. The upper source/load schedule chart and its fixed synthetic dispatch fixture do not change with the selected case. There is no optimizer, API, evidence-service, site, tariff, meter, or equipment connection; this is not an integrated dispatch result, field validation, or an MVP implementation. It does not establish savings, export/settlement rights, controllability, feasibility, or permission to operate equipment.

The interface remains Traditional Chinese only. This pass did not perform screen-reader testing, a full keyboard audit, contrast measurement, WCAG conformance review, translation-quality review, or operator/user validation. Product direction, visual system, locales, API/contract, and production architecture remain unapproved; G7.9 Step 3 is not closed.
