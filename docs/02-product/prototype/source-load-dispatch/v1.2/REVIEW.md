# Source/load dispatch prototype v1.2 review

**Review date:** 2026-10-05  
**Status:** Static source review for product and UX semantics; not production UX approval.  
**Base:** v1.1 six-stage workflow.  
**HTML blob:** aa36108ad4781d8906afe00d41d2a3308e15f94f

## Changes reviewed

- Added an explicitly synthetic settlement-scope state in stage 1: no customer account is represented, zero verified settlement scopes, and site authorization is not treated as account authorization.
- Added a visually separate, synthetic UI-state example in stage 4 showing partial import-energy-rate coverage (4 of 6 intervals). It contains no energy quantity, rate or monetary total and says missing intervals are withheld rather than zero-filled.
- Added an explicit stage 6 statement that snapshot identity/version pinning is not implemented in this static prototype; replay must be unavailable/incomplete when the original snapshot is missing, never silently use the latest input.
- Preserved the six-stage source/load workflow and labeled synthetic scenario boundary.

## Static checks

- Six workflow stage anchors are still present.
- The scope, partial-coverage and snapshot states are present in the expected workflow stages.
- Both new state panels have accessible names through `aria-labelledby`.
- Added state grid switches from two columns to one at compact widths (≤680 CSS px).
- Partial coverage example does not display any account, rate, energy or money values.

## Visual and interaction review

Browser rendering, keyboard interaction, screen-reader review, contrast measurement and touch-device review were not performed for v1.2. The local HTML page could not be opened in the available browser due to its local-file URL security policy, and no alternate browser path was used. Existing v1.1 rendered measurements do not verify v1.2.

## Limits

Traditional Chinese only. No Portuguese/English localization, real site, tariff, persistence, immutable snapshot implementation, user study, WCAG conformance or production readiness is claimed.
