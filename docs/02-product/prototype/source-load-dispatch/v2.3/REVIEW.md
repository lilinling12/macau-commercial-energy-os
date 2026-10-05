# Source/Load Dispatch Prototype v2.3 — Mixed Claim-State Review

**Status:** Static synthetic UI study for product/domain/design review. It does not approve product behavior, visual direction, an API contract, accessibility conformance, or production architecture.  
**Base:** PR #10 v2.2 HTML blob `35124c13d203bc1e5fe73ea215a94ad18b0a90aa`.  
**v2.3 source blob:** recorded after the source and review are fetched back from the branch.  
**Purpose:** Make different physical, service, economic, evidence, and claim outcomes inspectable in one review fixture.

## Correction and continuity from v2.2

v2.2 already had a static example for partial import-energy-rate coverage: 4 of 6 synthetic intervals, marked PARTIAL, without displaying a monetary amount. It also showed independent synthetic HVAC, ESS, EV, hot-water, and SHADOW boundaries. v2.3 preserves this context. The gap was that these examples did not form a selectable, shared mixed-result state or connect to an assessment/API response.

## What changed

- Added four selectable synthetic result combinations: partial exact-rate coverage; a physical profile without an applicable tariff; unresolved core meter mapping; and an HVAC service-bound violation in a synthetic example.
- A single selection updates the contextual announcement, physical/HVAC/ESS/economic dimensions, and a scoped claim ledger.
- A qualified physical profile remains separate from withheld bill, savings, service-feasibility, and device-control claims.
- Native buttons expose `aria-pressed`; status labels use text as well as color. A single polite atomic status summary reports the changed result without moving focus.
- The new controls have visible focus, at least 44px height, responsive four/two/one-column layouts, a contained scroll region for the wide data table, and reduced-motion support.
- The fixture switcher is independent of the schedule chart, existing HVAC selector, optimizer, API, site registry and evidence store. It persists no review or result.

## UI/UX Pro Max guidance applied

A targeted skill search for “live status announcement scoped assessment” returned the web rule **Contextual Live Badge Updates**: announce one meaningful contextual phrase without moving focus; avoid bare values and competing live regions. Source-level implementation follows that rule. The general priority checks applied were semantic controls, visible focus, touch-target size, text labels beyond color, responsive reflow, and reduced motion.

## Source-level verification

- Exact v2.2 source was fetched from the PR #10 branch and used as the base; the new source is versioned v2.3, including its rail badge.
- The four fixture records update every visible dimension and replace the ledger rows from one selected state.
- JavaScript syntax check: pending exact-source extraction and check.
- Browser rendering and interactive review: pending; no visual or runtime browser claim is made here.

## Not verified

- Desktop/tablet/mobile/narrow-mobile rendering, actual pointer and keyboard transitions, table scroll interaction and accessibility-tree announcement remain unverified.
- No measured contrast, full keyboard/screen-reader review, localization, operator review, WCAG conformance, API binding, Macau site/tariff validation, optimizer correctness, or control path is claimed.
- This remains Traditional Chinese UI study content, not complete Traditional Chinese/Portuguese/English support.

## Next review

Inspect the exact v2.3 branch file at 1440, 1024, 768, 375 and 320 CSS pixels. Exercise all four scenario controls using pointer and keyboard; check status announcement, focus retention, long text and table containment. Record only observed outcomes and repair any material issue before treating this version as reviewed.
