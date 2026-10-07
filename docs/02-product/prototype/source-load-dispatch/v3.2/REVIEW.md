# v3.2 Browser Review

**Status:** exploratory design study; synthetic data only; not an approved product UI.

## Scope and lineage

This integrated six-stage source/load workflow combines the current PR #10 v3.1 workflow shell with the detailed synthetic schedule structure reviewed in v2.9. It was reviewed against the files on PR #10 branch `product/source-load-economic-dispatch` at head `7e590a4a0f5b5f9b6c79a95b0aa2e5f51d705d25` on 2026-10-07. The source files used as references were v2.9 blob `fc91d524453ce31bdfe7768fb44c070a48522a08` and v3.1 blob `e7e396e52dfce4640e9776b6e727d6b625044856`.

The reviewed v3.2 HTML is a local design iteration. Its interval values are fixed synthetic examples, not Macau site data, tariff results, forecasts, optimizer output, dispatch feasibility, or savings evidence. It does not connect to a site or equipment and exposes no device command path.

## Browser checks

Reviewed in the Codex in-app Chromium browser on 2026-10-07.

- Stage 3 schedule comparison was rendered at 320, 375, 768, 1024 and 1440 CSS-pixel viewport widths in each of the three prototype locales: Traditional Chinese (`zh-Hant`), Portuguese (`pt`) and English (`en`), for 15 locale/viewport combinations.
- At all 15 combinations, document scroll width matched the browser's available layout width; no page-level horizontal overflow remained. The interval table retained its own horizontal scroll region on narrow layouts (920 CSS px content width at widths through 1024; 1262 CSS px at 1440).
- The first pass found a narrow Portuguese overflow at 320px caused by a non-wrapping scenario badge. The badge now wraps on small screens; the full 15-combination check was repeated and passed.
- The six stage controls were exercised at the desktop viewport and displayed the expected sequence: input validation, physical topology, schedule comparison, cost/constraint evidence, Shadow review and monitoring/replay.
- A page-local Shadow disposition changed to `aria-pressed=true` and remained selected after switching from English to Portuguese. This is prototype-only state; it is not persisted or sent to a service.
- The monitoring/replay stage explicitly says that no real site outcomes or measurements exist in this prototype and describes future version-aligned replay as a requirement.
- No browser console errors were observed during this review.

## Limits

- Portuguese and English copy are draft locale samples, not complete localization or native-speaker-reviewed translations. Dates, numbers, units, currency, legal/contract language and all states still need localization review.
- Responsive coverage was exhaustive only for stage 3 at the listed widths. Other stages were checked for expected content at the desktop viewport, not across every viewport/locale combination.
- This review is not a complete keyboard walkthrough, screen-reader review, measured contrast audit, WCAG conformance result, usability study, operator validation, Macau domain validation, or production readiness assessment.
- Costs and tariff eligibility are not calculated. Physical energy flow and financial settlement are presented separately, and no export credit, savings, controllability, or operational feasibility is claimed.
- The synthetic examples do not establish a canonical API, schema, production architecture, optimizer behavior, or Gate completion.

