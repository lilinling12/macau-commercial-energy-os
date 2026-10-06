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
