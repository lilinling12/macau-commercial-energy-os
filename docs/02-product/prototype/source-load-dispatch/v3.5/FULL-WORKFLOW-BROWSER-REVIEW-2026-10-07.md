# Prototype v3.5 — full workflow browser review (2026-10-07)

**Status:** local supplemental browser evidence for the unapproved prototype study. This is not a repository-integrated check, G7.9 exit, product approval, accessibility conformance result, localization sign-off, operator validation, or Macau-site validation.

## Reviewed artifact

- Page: `work/ui-current-head/v3.5/index.html`
- SHA-256: `5558FC036333C92C68A59B694B502196DD9051BEA8F67BD7318018775C4EA709`
- Projection SHA-256: `657D6641F3DC87B59926E5D2D4F3A731CB2510F6729625159A512D63A1FFCEA6`
- Source fixture SHA-256: `E63D7F61F7580313A344DDF837D7837065FDB2E8E83AA9DCBEC5C803AEA64ED1`
- Related project review: `work/ui-current-head/v3.5/REVIEW.md`.

## Coverage and result

A headless Microsoft Edge run exercised 90 combinations: six workflow stages × five CSS viewport widths (1440, 1024, 768, 375, 320 px) × three displayed locales (Traditional Chinese, Portuguese draft, English).

All 90 combinations passed these assertions:

- `<html lang>` follows the selected locale and exactly one workflow stage is marked current.
- No document-level horizontal overflow occurs at any tested stage, viewport, or locale.
- The physical energy model and economic settlement mapping are presented in separate sections.
- Schedule comparison contains six aligned synthetic intervals.
- The claim/evidence stage renders three resource-level service rows.
- The SHADOW review selection updates its page-local status; no Execute/Executar/執行 control is present.
- Monitoring/replay stage contains reviewable content.
- No uncaught browser page errors occurred.

A separate supplied smoke script also passed for Stage 4 at 375 and 1440 px: three `NOT_ASSESSED` service statuses localized in Traditional Chinese and English, no overflow, no page errors.

The repeatable harness is `full_flow_review.js`. It uses the installed Playwright package and an Edge executable supplied via `EDGE_EXECUTABLE_PATH`; it serves only the local prototype and its JSON fixtures on loopback for the browser run.

## Limits and implications

This validates visible structure, selected state and bounded responsive behavior for this prototype artifact only. It does not prove copy completeness/translation quality, full keyboard traversal, text enlargement, screen-reader behavior, non-text contrast, WCAG 2.2 conformance, real-world usability, actual tariff/settlement correctness, physical site feasibility, savings, equipment controllability, a production API integration, or a safe control path. Portuguese remains draft. The prototype and all values are synthetic; economics remain blocked and no equipment control is available.

The supplemental review is now attached to Draft PR #10 as commit `3df76cc2ff2bb699aec94f9f7a4343f5496e328e` at `docs/02-product/prototype/source-load-dispatch/v3.5/FULL-WORKFLOW-BROWSER-REVIEW-2026-10-07.md`. The PR remained open, Draft and unmerged after the update. Exact-head checks later completed successfully: Repository Hygiene run 37645524655 (#1592), Authority Validation run 37645524687 (#1593), and Dispatch Projection Validation run 37645524683 (#78). The dispatch job `Validate pinned projections and T7.1 semantic examples` succeeded. These CI checks cover repository structure and pinned projection/semantic examples; they do not rerun the 90 browser cases. The browser run itself was performed locally against a source copy whose page code matches the remote page after blank lines are excluded; projection JSON values match and the source fixture is byte-identical.


