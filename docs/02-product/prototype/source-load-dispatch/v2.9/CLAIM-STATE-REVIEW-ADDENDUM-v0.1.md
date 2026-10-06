# v2.9 claim-scope presentation addendum v0.1

**Date:** 2026-10-07  
**Status:** UI-only review proposal; not an approved product contract or operator validation.  
**Parent:** PR #10, `product/source-load-economic-dispatch`.

## Finding and change

The v2.9 projection page rendered claim readiness as a binary “shown in scenario / not provided” label. It did not display a claim’s scope or interval coverage. The independent v2.7 state study had a PARTIAL-rate case, but that state was not connected to the v2.9 result page. PR #14’s partial-rate behavior therefore lacked an integrated presentation example.

The v2.9 claim section now lets a reviewer compare:
- **Current projection result:** the status emitted by the pinned v2.9 fixture, whose economics remain `BLOCKED`.
- **Partial-coverage state example:** a display-only contract example showing one energy-cost component as `PARTIAL · 4 / 6 intervals covered`, while full-horizon bill total, savings and demand charge stay `WITHHELD`.

The example shows no currency amount and does not change the optimizer fixture, physical schedule, or current economic result. Uncovered intervals are never represented as zero. Every locale visibly states that the partial case is a UI example, not the current projection or PR #14 optimizer output. English and Portuguese strings remain draft review copy; this is not a localization approval.

## Evidence basis and limits

PR #14’s bounded prototype has focused tests for partial verified import-rate coverage and marks the economic component `PARTIAL`; the current PR #10 v2.9 fixture is different: its rates are project assumptions and economics are `BLOCKED`. The presentation example is deliberately separated from that fixture. It proves only that the interface can communicate exact scope and independent withheld claims. It is not API-bound and does not establish tariff applicability, Macau site evidence, eligible bill calculations, savings, or G7.9 Step 3 acceptance.

## Review checks

The static verifier now checks that:
- the actual projection fixture remains synthetic and economically blocked;
- the separate partial example is selectable and explicitly labelled as display-only;
- 4/6 interval coverage is visible;
- full-window total, savings and demand charge have separate withheld reasons;
- uncovered intervals are not treated as zero in the three candidate locales.

Browser interaction and rendered-state checks are recorded after review. No WCAG conformance, translation approval, user testing, site validation or production-contract claim is made.

## Browser observation — 2026-10-07

Reviewed the branch artifact at commit `24171f4b33d234ee5776575b77bd884ef9563143` in the local in-app browser. The visible screenshot viewport was approximately 1265 × 705 CSS pixels.

- Traditional Chinese loaded the actual v2.9 output first; its economics remained BLOCKED.
- Switched to the partial-coverage state and confirmed the display-only warning, `PARTIAL · 4 / 6 intervals covered`, and separate WITHHELD rows for full-horizon bill total, savings and demand charge.
- Switched to English and Portuguese draft while the partial example remained selected; the claim names, scope, reason text and synthetic-only boundary changed with the locale.
- Switched back to the actual projection in Portuguese; the original projection claims returned, including unverified tariff and withheld economics.
- The schedule/chart stayed the pinned synthetic scenario while only the claim-list presentation state changed.

The state picker is a native radio group with a legend. This browser pass did not include a full keyboard-only sequence, screen reader, mobile viewport after this change, formal contrast audit, translation review, operator/user task test, Macau site evidence or WCAG conformance. Portuguese remains draft. The prior v2.9 responsive review predates this new panel and cannot substitute for narrow-screen validation of this addition.

## Semantic separation correction — 2026-10-07

The G7.9 T1 scoped-evidence matrix defines `PARTIAL` as an assessment/coverage state; claim disposition remains `ALLOWED` or `WITHHELD`. The first UI example attached the PARTIAL label directly to the energy-component row, which could imply a third claim disposition. Corrected the rendering:
- the economic evaluation reports `PARTIAL` and the exact sample ranges 09:00–13:00 covered (4/6), 13:00–15:00 uncovered (2/6);
- the energy-component claim is `ALLOWED` only within the covered intervals;
- full-horizon total, savings and demand charge remain separately `WITHHELD`;
- no monetary amount is shown, and the sample remains separate from the actual blocked v2.9 projection.

Added `G7.9-T1-APP11-CLAIM-TO-UI-MAPPING-v0.1.md` as a schema-neutral proposal connecting these UI semantics to the scoped evidence matrix and future APP-11 view model. It does not approve a wire schema or close G7.9.

The static verifier now checks the separation and coverage language. 

## Browser review after semantic correction — 2026-10-07

Reviewed the corrected branch copy at `e9429ff25ae4f56e65e14a44587f0bdff0207043` in the local in-app browser at approximately 1265 × 705 CSS pixels.

- Traditional Chinese actual-result mode showed the unchanged synthetic projection and its blocked economics.
- Selecting the partial display example changed only the claim list. The banner identified the economic assessment as `PARTIAL`, listed 09:00–13:00 Macau time as covered (4/6) and 13:00–15:00 as uncovered (2/6); the energy-component claim read `ALLOWED` only in covered intervals.
- Full-horizon bill, savings and demand charge each remained separately `WITHHELD`. No monetary value appeared.
- English retained the same selected state, exact ranges, claim disposition and withheld boundaries after locale switching.
- The previous Portuguese draft browser pass exercised the prior copy; this semantic correction has not yet been browser-reviewed in Portuguese.

The browser evidence covers this desktop viewport and the state/locale actions described above. Narrow-screen rendering after this change, Portuguese review after semantic correction, complete keyboard coverage, screen-reader review, contrast measurement, operator validation, WCAG conformance, site evidence and production API binding remain unverified.
