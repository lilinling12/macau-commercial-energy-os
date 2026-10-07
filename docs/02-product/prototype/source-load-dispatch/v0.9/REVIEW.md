# Prototype v0.9 interaction and responsive review

**Review date:** 2026-10-05  
**Status:** reviewable design hypothesis; not approved production UX or product scope.

## Exact source

- Repository: `lilinling12/macau-commercial-energy-os`
- Branch: `product/source-load-economic-dispatch`
- HTML commit: `222b608179ea2cb9794c5f200447fc8cfa56918a`
- HTML path: `docs/02-product/prototype/source-load-dispatch/v0.9/index.html`
- GitHub Contents API blob SHA: `0ea8dfd1985b4463c1d76673cb7b938d3cbed05d`
- v0.9 was derived from v0.8 source blob `4e87ff38e69f429ca158e0959fc8ec0b428874d4` at PR head `f65fb2a68f7608bb1680837fa999e52954bc1fe8`.
- The fetched v0.9 branch HTML was rendered from a local copy in Microsoft Edge using Playwright.

## Changes tested

- Replaced the six-stage long-form page with six navigable stages and one visible stage at a time. The default stage is the primary source/load dispatch comparison; users can open each stage from the step navigation or previous/next controls.
- Made the missing forecast explicit: the candidate is a synthetic scenario; without site load/PV forecasts the interface says a formal optimized schedule cannot be produced. This is a display boundary, not an optimizer test.
- Moved SHADOW review actions to the review stage and collapsed the long economics/assumption explanation behind a disclosure.
- On narrow screens, exposed the schedule chart as a keyboard-focusable horizontal scroll region with a visible instruction and kept the full interval table as an alternative.
- Increased secondary mobile copy and table text from v0.8's smaller sizes. The palette remains the existing unselected prototype palette.

## Browser checks

| Viewport (CSS px) | Active-stage document height | Document width | Result |
|---|---:|---:|---|
| 1440 × 1000 | 1512 | 1440 | No document-level horizontal overflow |
| 1024 × 900 | 1719 | 1024 | No document-level horizontal overflow |
| 768 × 1024 | 1906 | 768 | No document-level horizontal overflow |
| 375 × 844 | 3081 | 375 | No document-level horizontal overflow |

At these widths only one workflow stage is visible; the four dispatch metrics use 4/2/2/1 columns. At 375 px, the chart viewport is 345 px wide over a 650 px schedule graphic; pressing the right arrow after focusing the chart scrolls it by 160 px. The full table can be opened, and remains in its own scroll region.

The workflow navigation was exercised across all six stages; each showed the selected stage only. The in-chart forecast-evidence link also switches to the evidence stage. The next-stage control advanced from schedule comparison to constraints. The review actions moved to stage 05; selecting REVIEWED, REQUEST_EVIDENCE or DISMISSED updates the page-only state, and reload resets it. No page JavaScript errors were observed.

## Iteration findings

The progressive stage view reduces the full document from v0.8's approximately 4,419 px desktop / 7,555 px mobile long page to one active stage. It also makes the dispatch task visible at entry.

Remaining items before a product owner could approve a visual direction:

- The 375 px dispatch stage remains tall at about 3,081 px because the schedule, readiness and comparison content are all retained. A further mobile hierarchy study may reduce or reorganize this material.
- The schedule chart is internally scrollable on mobile, so users must discover and use the visible hint; confirm with representative operators. Full keyboard and assistive-technology review is still needed.
- Axis annotations, Chinese/Portuguese/English text lengths, contrast at all states, zoom/text enlargement, dark theme, and a complete component/token system are not validated.
- The default at stage 03 is a product hypothesis. Confirm whether returning users should land in dispatch or return to their last workflow state.
- No product visual direction or palette is selected; no award outcome is claimed.

## Design basis and limits

Used the `ui-ux-pro-max` responsive and chart guidance and the project-specific `.agents/skills/macau-energy-os-ui-ux/` draft. The Pro Max generic operations pattern returned a landing-page direction, which was rejected for this persistent operator task. The iteration instead tests progressive disclosure, a schedule-first workspace, visible forecast blockers, direct chart labels, and a tabular alternative.

Reference principles consulted include Apple HIG hierarchy/progressive disclosure, Material 3 adaptive layout, and WCAG 2.2 focus/accessibility guidance. Webby criteria cover content, structure/navigation, visual design, functionality, interactivity and overall experience; Awwwards emphasizes design, usability, creativity and content; FWA describes digital creativity, originality and technical excellence. These inform review dimensions only; this prototype does not copy an award site. No award-case study establishes operator usability.

This review is Traditional-Chinese-only, synthetic and local-browser-only. It does not prove WCAG conformance, complete localization, screen-reader support, representative-user success, tariff/contract/site validity, forecast or optimizer quality, dispatch feasibility, savings, production architecture, Gate closure, or authorization to control equipment.


## Exact-head warning-contrast correction — 2026-10-05

- Warning status icons now use the dedicated foreground `#9e4d27` on `#fae7dc`; the earlier orange foreground `#c86131` measured 3.36:1 on that warning background. The corrected pair measures **4.95:1** using the WCAG relative-luminance contrast formula.
- Selected comparison pairs were also rechecked: ink/paper 13.35:1, muted/paper 4.50:1, muted/white 4.93:1, teal/white 4.92:1, navigation/white 14.63:1, and focus/white 5.56:1.
- The browser review was rerun against the v0.9 source submitted in the immediately preceding exact-head commit. At 1440, 1024, 768 and 375 CSS px, document width equaled viewport width; the stage navigation, next-stage control, evidence shortcut, data-table disclosure, SHADOW disposition state/reset, and keyboard-scrollable chart were exercised. No JavaScript errors were observed.
- Latest HTML commit: `f709fd6c436a57d089b399ea04008725cef92cec`; GitHub Contents API blob SHA: `a5adb1ba0f2d6821190be36affe4ba0a570c34d8`.
- These are selected color-pair checks and prototype interaction evidence only. They do not establish WCAG conformance, screen-reader usability, complete localization, production readiness, or user validation. PR #10 remains a draft proposal.


## Chart annotation clipping correction — 2026-10-05

Rendered visual review found two chart annotations exceeded the 800-unit SVG viewBox or crowded the HVAC-shift label. The peak annotation now starts at x=500; the HVAC rebound label is shortened to `17:00 HVAC 回彈` and placed at x=670. Re-render at 1440 CSS px shows both labels fully inside the chart with clear separation; responsive checks at 1024, 768 and 375 CSS px still show no document-level horizontal overflow. The six-stage navigation and workflow interaction review was rerun without JavaScript errors.

Superseding HTML commit: `23e513415d581d7be23fbd4a4c30e01ff609d6d5`; GitHub Contents API blob SHA: `415761b3b11fd21961a0fd67d3d57b48bdb123b0`. This visual correction does not imply approval of the palette, complete accessibility, localization or product direction.
