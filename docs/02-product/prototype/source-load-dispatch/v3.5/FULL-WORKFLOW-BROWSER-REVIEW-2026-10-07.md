# Prototype v3.5 — full workflow browser review (2026-10-07)

**Status:** Supplemental verification for an unapproved design study. This does not approve product scope, close G7.9 Step 3, validate a Macau site, certify accessibility, sign off translations, or authorize equipment control.

## Exact source snapshot

- PR: [#10](https://github.com/lilinling12/macau-commercial-energy-os/pull/10), Draft/open/unmerged at review.
- Branch head inspected: `31769891cafbc79ab50dffc69bcc7d808fb00158`.
- Remote page blob: `5c9ec18baf17e41047f9a324359be5289628c015`.
- Local page used for browser execution: Git blob `c03f351a6c7176d4eaea0944cc8d2e9bc9a390dc`. A normalized line comparison confirmed the page code matches the remote page after excluding blank lines; the difference is whitespace/trailing newline only.
- Remote APP-11 projection blob: `a8b0e32a82e363a4cdfb7981a8d1d2299186854c`. Its parsed JSON content matches the local projection used in the run.
- Remote and local source fixture share blob `17906365997be7a529222b3c120e138ef336bb8c`.

## Coverage and result

A headless Microsoft Edge run exercised **90 combinations**: six workflow stages × five CSS viewport widths (1440, 1024, 768, 375 and 320 px) × three displayed locales (Traditional Chinese, Portuguese draft and English).

All 90 combinations passed these assertions:

- The document language follows the selected locale and exactly one workflow stage is marked current.
- No document-level horizontal overflow occurs at any tested stage, viewport or locale.
- The physical energy model and economic settlement mapping appear as separate sections.
- Schedule comparison contains six aligned synthetic intervals.
- The claims/evidence stage renders three resource-level service rows.
- SHADOW review selection updates its page-local status; no Execute/Executar/執行 control is present.
- Monitoring/replay stage contains reviewable content.
- No uncaught browser page errors occurred.

The source/fixture verifier also passed. A separate supplied smoke script passed at Stage 4 at 375 and 1440 px: three service statuses localized in Traditional Chinese and English, no overflow and no page errors.

## Limits

This is bounded prototype evidence for structure, selected state and responsive behavior. It does not prove full copy/translation quality, complete keyboard traversal, text enlargement, screen-reader behavior, non-text contrast, WCAG 2.2 conformance, real-world usability, tariff/settlement correctness, physical site feasibility, savings, equipment controllability or production API integration. Portuguese remains draft. Values are synthetic; economic claims remain blocked, and the prototype has no equipment command path.
