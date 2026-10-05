# Source/Load Dispatch Prototype v2.2 — Resource Service State Review

**Status:** Synthetic UI study for product/domain/design review. It does not approve a pilot resource set, service model, visual system, API contract, or production architecture.  
**Base:** PR #10 v2.1 HTML blob ec478939ad2c0a3d2fce57c08b4b8b05066f4d2e.  
**Change:** Adds per-resource service/eligibility visibility tied to the flexible-load service boundary proposal.

## What changed

- Reframed the existing four-state selector as an HVAC/chiller service-evidence state. Selecting unassessed, stale, unmet, or synthetic-pass updates the HVAC summary, the HVAC resource row, and the existing live announcement together.
- Added separate resource rows for HVAC/chiller, ESS, EV charging, and hot-water service. ESS remains marked as synthetic/unverified; EV and hot water remain explicitly outside this candidate because their asset/service evidence is absent.
- Added the next evidence needed for each resource: thermal/comfort/recovery; SOC, power, efficiency and reserve; charger availability/departure target/meter; hot-water state/draw/delivery/recovery.
- Kept electrical balance, account economics, and SHADOW/no-control as independent claims. A synthetic HVAC pass does not qualify the ESS, the full schedule, economics, or execution.
- Added a two-column resource-card layout that switches to one column below the 560px CSS breakpoint.

## Checks completed

- Updated the title/footer version labels to v2.2.
- Source inspection confirms the state selector is a native radio fieldset, resource cards are list items, and the existing polite live region announces the selected HVAC state.
- The updated inline JavaScript passed node --check from the exact v2.2 source held in the local preview copy.

## Not verified

- No browser render or interaction session was run for v2.2. Its visual layout at desktop, tablet, mobile and narrow-mobile widths remains unverified; the inherited v2.1 rendering evidence is not transferred to this new version.
- No measured color-contrast audit, full keyboard/screen-reader/reduced-motion session, Portuguese/English flow, Macau operator review, usability study or WCAG conformance is claimed.
- All displayed service states and evidence are synthetic UI fixtures. The cards are not connected to the optimizer/API, site registry, evidence store, or control path.

## Design basis

The change follows the proposed [Flexible-Load Service Boundary Design](../../../../03-architecture/detailed-design/FLEXIBLE-LOAD-SERVICE-BOUNDARY-DESIGN-v0.1.md) and keeps the SHADOW-only boundary.


## Claim-state integration follow-up

The separate [Dispatch Claim-State Presentation Contract proposal](../../DISPATCH-CLAIM-STATE-PRESENTATION-CONTRACT-v0.1.md) maps future UI states to independent physical, resource-service, economic, evidence, claim, review, and execution dimensions. It records that this v2.2 study is not bound to PR #14/API output and enumerates mixed-state acceptance examples for a future vertical slice.
