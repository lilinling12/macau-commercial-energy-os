# Source/load dispatch prototype v1.1 review

**Review date:** 2026-10-05  
**Status:** Progressive-disclosure iteration for product/design review; not approved production UX.  
**Base:** PR #10 v1.0 HTML blob `d896378094cc1c26fd762829cd5dbe5247b7e94f`.

## Changes

- On compact viewports (≤680 CSS px), the six-step workflow becomes a keyboard-operable native disclosure showing the current stage and progress. Opening it reveals all six destinations; choosing a stage closes the menu, updates the URL fragment and stage label, and moves focus to that stage heading.
- The six source/resource eligibility cards retain their name and evidence state in the summary while the explanatory paragraph collapses on compact viewports. Each explanation remains available on demand. On wider layouts, the detailed cards remain expanded.
- The disclosure indicator now sits in the resource-card header instead of consuming a separate line.
- The full six-stage flow, six mobile interval summaries, full interval table and SHADOW-only review remain present.

This responds to the v1.0 mobile review: the flow already used one active stage, but the always-visible step grid and six expanded resource explanations consumed avoidable vertical space. It keeps the core schedule values and evidence state visible while moving secondary explanation behind native disclosure controls.

## Verification performed

Rendered the local prototype in Microsoft Edge with Playwright. Captured mobile stage 2 and stage 3 at 375×844 and a stage 3 viewport at 768×1024. Checked document width and height at 375, 680, 681, 760, 761, 768, 800, 1024 and 1440 CSS px.

| State / viewport | v1.0 height | v1.1 height | Observation |
|---|---:|---:|---|
| Stage 2, 375px, resource explanations initially collapsed | 3,083px | 2,631px | 452px shorter (14.7%); all six resource names and evidence states remain visible. |
| Stage 3, 375px | 3,125px | 2,975px | 150px shorter (4.8%); all six interval summaries remain visible. |
| Stage 3, 768×1024 | 1,906px | 1,906px | Existing three-column stage navigation remains visible; screenshot reviewed. |
| Stage 3, 1024px / 1440px | Previously reviewed at 1024px; desktop source retained | No horizontal document overflow; native stage and resource disclosures remain open | Desktop/tablet content remains expanded. |

Interaction checks at 375px:
- Keyboard Enter opens the workflow disclosure; Tab reaches the first and second stage links; Enter selects the second stage.
- The selection updates the fragment to `#site-model`, updates the current-stage summary, closes the menu, and focuses `#modelTitle`.
- Keyboard Enter expands a resource explanation.
- The schedule stage still presents six interval summaries; the complete table control sets `aria-expanded=true` and reveals the table.
- Hidden stages are marked `aria-hidden=true`; no page-level horizontal overflow or JavaScript errors were observed at the checked states.

The 375px page remains long, particularly in the schedule stage. The iteration reduces, but does not eliminate, vertical scrolling. The previously documented trade-off remains: compact interval values take precedence over a horizontally panned chart on narrow screens.

## Limitations

- Synthetic scenario only; no Macau site, contract, device, savings or feasibility claim is established.
- Traditional Chinese only; Portuguese and English localization, locale-specific values and terminology remain unimplemented.
- No representative-operator task study, screen-reader test, touch-device test, text-zoom test, or complete WCAG conformance audit was performed.
- No palette, typography system, product scope, or production architecture is selected.
- The project UI/UX skill and product baseline remain on PR #8, which is open and unmerged. This prototype iteration does not make that draft an active main-branch rule.

## Review references

Local captures used for visual review:
- `work/dispatch-v11-stage2-375-default.png`
- `work/dispatch-v11-stage2-375-expanded.png`
- `work/dispatch-v11-stage3-375.png`
- `work/dispatch-v11-768.png`

These captures are review evidence for this synthetic prototype only. They are not user research or production acceptance.
