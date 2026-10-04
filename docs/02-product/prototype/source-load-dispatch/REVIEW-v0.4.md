
# Dispatch workflow prototype v0.4 — review record

**Status:** synthetic interaction/design study; no owner approval, site validation, tariff evaluation, user validation, or production UI claim.
**Locale:** Traditional Chinese only.
**Source:** v0.3 focused dispatch-comparison study; evidence-linked to PR #10 dispatch design and current G1/G2/G3/G6/G7 boundaries.

## What this revision covers

The single-screen v0.3 study only demonstrated baseline/candidate schedule comparison and evidence claims. v0.4 places it into a six-stage task path: data/contract readiness → physical site energy model → aligned forecast/dispatch comparison → cost/constraint/evidence explanation → SHADOW review → monitoring/replay status.

The new stages state which inputs are synthetic or missing, keep physical flow separate from tariff/account settlement, expose that the example's interval reduction raises the whole-horizon import maximum during rebound, and show that no cost, feasibility, execution, measured outcome or savings result is available. Existing controls remain page-local and no equipment command path is represented.

## Verification scope

The branch verifier checks the six stages, anchor navigation, claims boundary, workflow labels, source/load fixture balance, HVAC rebound, corrected horizon peak, table alignment, scenario-focus and page-only-review source behavior. It is a static source/fixture check, not browser interaction, keyboard traversal, visual rendering, contrast measurement, site/contract truth, optimizer output or user research.

No rendered checks are claimed for desktop, tablet, mobile or alternate languages; browser preview remains unavailable in this task. The review handoff should record the screen/viewport/state when a permitted browser surface becomes available.
