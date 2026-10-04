
# Dispatch workflow prototype v0.4 — review record

**Status:** synthetic interaction/design study; no owner approval, site validation, tariff evaluation, user validation, or production UI claim.
**Locale:** Traditional Chinese only.
**Source:** v0.3 focused dispatch-comparison study; evidence-linked to PR #10 dispatch design and current G1/G2/G3/G6/G7 boundaries.

## What this revision covers

The single-screen v0.3 study only demonstrated baseline/candidate schedule comparison and evidence claims. v0.4 places it into a six-stage task path: data/contract readiness → physical site energy model → aligned forecast/dispatch comparison → cost/constraint/evidence explanation → SHADOW review → monitoring/replay status.

The new stages state which inputs are synthetic or missing, keep physical flow separate from tariff/account settlement, expose that the example's interval reduction raises the whole-horizon import maximum during rebound, and show that no cost, feasibility, execution, measured outcome or savings result is available. Existing controls remain page-local and no equipment command path is represented.

## Verification scope

The branch verifier checks the six stages, anchor navigation, claims boundary, workflow labels, source/load fixture balance, HVAC rebound, corrected horizon peak, table alignment, scenario-focus and page-only-review source behavior. It is a static source/fixture check, not browser interaction, keyboard traversal, visual rendering, contrast measurement, site/contract truth, optimizer output or user research.

## Rendered browser review — 2026-10-04

The exact PR branch HTML was fetched and rendered in the Codex in-app browser. The browser page title and six-stage workflow match v0.4; a desktop screenshot at 1265 × 712 shows the dispatch workspace, planning context, six workflow anchors and input-evidence stage. Prior viewport measurements on this same exact HTML covered 1440, 1024, 768 and 375 CSS px. At each width the document itself did not overflow horizontally; at 375 px the data table is contained by its own horizontal-scroll wrapper. This is layout evidence only, not device testing or full user validation.

The browser accessibility tree exposed the six stage headings and anchors, chart name/description and a disabled equipment-control button. The Traditional Chinese footer correctly says that this is not full multilingual support. Only Traditional Chinese is present; Portuguese and English coverage, locale switching, date/number formatting and translation completeness remain unreviewed.

The visible rail badge said v0.3 while the document title and footer identified v0.4. This inconsistency was corrected on this branch to v0.4.

Interaction verification is incomplete. The current browser automation focused/scroll-positioned the input-evidence, table and scenario controls but did not produce observable activation or state change; therefore the modal, table toggle, scenario highlight and page-only review action are not claimed as runtime verified. Source handlers exist, but static source inspection is not interaction proof.

A separate rendering of product prototype v0.11 showed that its initial workspace remains a portfolio dashboard with a conventional left rail and KPI cards. It is useful as an overview hypothesis, but it does not make source/load dispatch the primary task. The v0.4 dispatch workflow is the stronger current proposal for the requested dispatch-first direction; both remain unapproved prototypes.

The screenshot and viewport checks do not establish WCAG conformance. Contrast ratios, keyboard traversal through all controls, reduced-motion behavior, chart data-table equivalence, Portuguese/English layouts and customer usability still require explicit review.

## Source-review corrections — follow-up

A focused source audit found two prototype semantics issues after v0.4 was added: the scenario-only example was labelled as a forecast/SHADOW result, and the stage-5 jump link targeted a nonexistent `#reviewBox` id. The follow-up changes relabel stage 3 as a time-series/scenario comparison, mark the candidate as synthetic, remove the static current-step marker from a page that does not track scroll position, and point the review jump at the actual review button. The opening copy also uses consistent Traditional Chinese wording.

The verifier now guards those labels and the destination anchor. These checks confirm source-level consistency only; they do not replace rendered interaction or accessibility review.
