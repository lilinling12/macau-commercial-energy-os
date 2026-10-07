# UX-PROTOTYPE-DEMO-STATE-CLARITY-001 — Clarify temporary review feedback

## Identity

- **Task ID / title:** UX-PROTOTYPE-DEMO-STATE-CLARITY-001 — Clarify temporary review feedback
- **Type:** Product / UX
- **Gate / workstream:** WP-4 formative usability preparation; PR-06/PR-08
- **Status:** Review
- **Accountable human owner:** Product owner
- **Required human reviewer(s) / expertise:** Product design and accessibility review
- **Risk tier / rationale:** Low. Copy and accessibility-status semantics in a synthetic prototype only; no live records, user accounts, customer data or device actions.
- **Created / updated:** 2026-10-04

## Outcome

- **Problem:** Prototype v0.10 labels an in-memory DOM state change as “saved locally”, which can imply persistence. The page has no storage/API persistence, so that claim overstates what the prototype does.
- **User outcome:** A reviewer understands the action changes only the visible demo page state, resets on reload, and is neither an execution approval nor a measured outcome.
- **Deliverable:** Prototype v0.11 preserving v0.10 and clarifying the review feedback message; updated product/WP-4 handoff links and design review note.
- **Why this is safe before owner decisions:** It improves truthful demo-state communication without selecting product scope, launch language, interaction direction, technology stack or persistence policy.

## Authority and constraints

- **Authority:** docs/02-product/VISUAL-DESIGN-PRINCIPLES-v0.1.md; docs/02-product/USER-FLOWS-AND-IA-v0.1.md; docs/03-architecture/detailed-design/RECOMMENDATION-AND-OPERATOR-REVIEW-DETAILED-DESIGN-v0.1.md; AI Coding Quality Baseline.
- Review annotations remain distinct from execution approval, measured outcome and durable production audit records.
- The prototype remains synthetic, English-only and not a production workflow. It does not persist state, call a command endpoint or contain live Macau data.
- Preserve v0.10 as the prior review stimulus; v0.11 does not establish user preference, accessibility conformance or final visual direction.

## Scope

### In scope

- Replace “saved locally” with explicit temporary, page-only status language for reviewed, dismissed and needs-data demo states.
- Preserve the visible state badge and disabled follow-up controls after a demo disposition.
- Record v0.11 as current for future formative task sessions.

### Out of scope

- Adding browser storage, APIs, authentication, audit persistence or device control.
- Changing recommendation semantics, workflow choices, product scope, palette or framework.
- Claiming user validation, WCAG conformance, localization readiness or production acceptance.

## Acceptance criteria

1. Every demo disposition states that it changes only this page's displayed demo state and resets on reload.
2. Feedback never says a record was saved/persisted or implies command authorization, savings or measured outcome.
3. The state is announced by the existing polite live-status region without moving focus.
4. v0.10 remains unchanged; v0.11 is linked from the product README and WP-4 protocol.
5. The source-level UX review is recorded; rendered/assistive-technology/user validation limitations stay visible.

## Verification and evidence

- Source comparison confirms there is no localStorage, IndexedDB, API call or other persistence path for these demo dispositions.
- In a fresh browser tab the initial recommendation cards are unreviewed and all demo controls are enabled; the previously viewed browser tab showed a post-click in-memory state with disabled controls and a “saved locally” message.
- This is a bounded browser accessibility-tree/source inspection, not a refresh/reload persistence test or screen-reader evaluation.
- GitHub PR workflows run automatically on the final commit; exact latest checks and results are tracked in PR #8. No application test files or runtime implementation are changed.

## Completion record

- **Changes/deliverables:** Created prototype v0.11 by preserving v0.10 and replacing the inaccurate “saved locally” confirmation with a truthful page-only, reset-on-reload, non-persistent status. The recommendation workflow, task content and visual direction did not change.
- **Files updated:** Prototype v0.11; product README; WP-4 research protocol; visual-design evaluation; CURRENT; ROADMAP; HISTORY; this packet.
- **Checks run and results:** Static source inspection found no storage/API persistence path, and a fresh browser accessibility tree showed the initial unreviewed state with demo controls enabled. Exact-head CI and its existing workflow scope are listed in PR #8. No user/screen-reader/WCAG session or manual application test was run.
- **New evidence / decisions / unknowns:** This corrects prototype copy only; no owner decision is made. Launch locale, product review semantics, visual direction and production persistence remain open.
- **PR/branch and review state:** PR #8, docs/product-architecture-roadmap, open/unmerged.
- **Gate or task status after work:** Review; WP-4 remains open.
- **Next task and dependencies:** Owner review and authorized WP-4 sessions; no prototype result is treated as production design evidence until validated.
