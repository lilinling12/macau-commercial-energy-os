# Source/Load Dispatch Prototype v2.4 — Narrow-Screen and Claim-State Review

**Status:** Unapproved synthetic UI study. It does not approve the product workflow, final visual direction, API semantics, accessibility conformance, or production architecture.  
**Base:** PR #10 v2.3 at HTML blob `6f199ddaee1f2a416b9925ce310a073b0455b054`.  
**Scope:** Correct narrow-screen sizing discovered during exact-source browser review; make the claim table keyboard-scrollable and disclose horizontal scrolling. Scenario data and claims are unchanged.

## v2.3 review finding

The first rendered check found real document overflow at 320px and 375px. Playwright measured `documentElement.scrollWidth` as 736px at both widths, and the claim study was 684px wide. The 650px minimum table width had propagated through the mobile grid item's automatic minimum size, so the table's inner `overflow:auto` alone did not keep the page within the viewport. This contradicted the earlier source-only expectation that the table stayed contained.

## v2.4 correction

- At 760px and below, the application frame now uses a zero-minimum grid track and the main content can shrink to the viewport.
- The claim study and table scroll region are explicitly allowed to shrink; the table keeps its readable 650px content width inside its own horizontal viewport.
- The scroll region now has keyboard focus, a named `region` role, a visible focus outline, and a Traditional Chinese instruction explaining horizontal scrolling on narrow screens.
- Left/right arrow keys move the focused table region by 180px. The source contains no state or claims changes beyond these usability/accessibility affordances.

## Browser evidence

Rendered in Microsoft Edge via Playwright using the exact v2.4 local review copy derived from the PR #10 v2.3 branch source. The claim study was visible at each CSS viewport. At all five widths the document width equalled the viewport and there were no page JavaScript errors.

| Viewport | Document width | Claim study width | Claim options | Table region / table content | Result |
|---:|---:|---:|---:|---:|---|
| 1440 | 1440 | 1201 | 4 columns | 1159 / 1157 px | Fits without horizontal scroll |
| 1024 | 1024 | 818 | 4 columns | 776 / 774 px | Fits without horizontal scroll |
| 768 | 768 | 583 | 2 columns | 541 / 650 px | Table scroll stays inside region |
| 375 | 375 | 323 | 1 column | 291 / 650 px | No page overflow; table scroll is contained |
| 320 | 320 | 268 | 1 column | 236 / 650 px | No page overflow; table scroll is contained |

The four fixture controls were exercised by pointer. Observed physical/service/economic states were: partial rates → `PARTIAL / NOT_ASSESSED / PARTIAL`; no tariff → `COMPLETE / NOT_ASSESSED / NOT_CALCULATED`; missing core meter mapping → `BLOCKED / UNKNOWN / BLOCKED`; synthetic HVAC service violation → `COMPLETE / VIOLATION / NOT_CALCULATED`. Every case continued to withhold device control. From the first case button, Tab focused the second; Enter selected it. The claim summary exposes `role=status` and `aria-live=polite`. The table region was keyboard-focused; ArrowRight advanced its scroll offset from 0 to 180px (416px maximum). The data-table disclosure also opened successfully.

## Limits and next evidence

- The visual pass focused on the claim-state section, not every page/stage at every viewport.
- Browser automation checked DOM behavior and viewport dimensions; this is not manual screen-reader testing, full keyboard audit, enlarged-text reflow, page-wide contrast measurement, or WCAG conformance.
- Only Traditional Chinese is present. v2.3's separate 489-unit locale inventory remains uncovered by Portuguese and English (0/489 each); v2.4 does not add runtime localization.
- The four cases remain disconnected from the schedule, API, site registry, optimizer and evidence service. They are static synthetic UI fixtures, not Macau site results.

This improves the v2.3 study's narrow-screen and keyboard-table behavior. Product and visual direction remain unapproved; no operator validation, device-control capability, savings, Gate completion, or production readiness is claimed.


### Dynamic claim text at phone widths

After the initial five-width layout pass, all four claim states were also selected at 375px and 320px. In all eight state/viewport combinations, document width stayed equal to the viewport and the claim-summary scroll width equalled its client width (288px at 375; 233px at 320). The longest missing-mapping and service-violation copy did not introduce clipping or page overflow. This supplements the original 1440px interaction pass; it does not extend the review to every workflow stage or locale.


## Full six-stage navigation and SHADOW review follow-up — 2026-10-05

A full-flow browser pass exposed a stage-ownership defect that the earlier claim-state-only review did not cover. Before this follow-up, the three disposition buttons lived in the Stage 03 comparison sidebar, while Stage 05 linked to `#disposition-actions`. Stage navigation hides inactive sections, so the link targeted controls inside the hidden Stage 03 section; Playwright resolved the controls but could not see or activate them. The review actions therefore were not usable from the advertised SHADOW review stage.

The PR #10 branch now moves the status and three page-only actions (reviewed, request evidence, dismiss) into Stage 05. Stage 03 replaces its hidden actions with a visible link to Stage 05. The Stage 05 helper text now points to the controls below. The buttons remain explicitly non-persistent, do not grant authority, and do not issue device commands.

The updated PR-derived local review copy was rendered in Microsoft Edge with Playwright at 1440, 1024, 768, 375 and 320 CSS-pixel widths. Each of the six stages was selected through the stage navigation at every width (30 stage/viewport combinations). The selected stage was visible, inactive workflow sections were hidden, and document width equalled the viewport in all combinations. No page JavaScript errors were observed. Desktop screenshots were captured for Stages 01, 03, 05 and 06; mobile screenshots for Stages 03 and 05.

Interaction evidence after the fix:

- Stage 03 candidate focus changed the announced comparison label; the data-table disclosure opened.
- The Stage 03 link switched to Stage 05, where all three disposition actions were visible and usable.
- The three actions updated the selected state and status copy as expected; copy continues to state that nothing is persisted or executed.
- All four independent claim fixtures produced their expected physical/service/economic labels: partial rates `PARTIAL / NOT_ASSESSED / PARTIAL`; no tariff `COMPLETE / NOT_ASSESSED / NOT_CALCULATED`; missing meter map `BLOCKED / UNKNOWN / BLOCKED`; service violation `COMPLETE / VIOLATION / NOT_CALCULATED`.
- The assumptions modal opened and closed through its “明白” action.

This verifies prototype navigation and these specific interactions only. It is not a manual assistive-technology review, complete keyboard audit, WCAG conformance, translation-quality review, user test, site validation, or approval of product/visual/architecture decisions. The review copy was derived from the PR branch response and exercised after applying the same patch; byte-for-byte local/git-blob identity is not claimed.
