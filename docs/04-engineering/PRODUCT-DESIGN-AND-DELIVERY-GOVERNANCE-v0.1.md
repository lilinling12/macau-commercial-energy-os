# Product Design and Engineering Delivery Governance v0.1

**Status:** Proposed project working rules; pending owner review.
**Scope:** Product design, UI/UX, architecture decisions, AI-assisted implementation, validation, and release.
**Authority:** Existing research/Gate records remain controlling. This document adds a review process; it does not select product scope, visual style, framework, or production stack.

## 1. Decision and approval boundary

Research findings, standards, and skill-generated recommendations are inputs to decisions, not approval by themselves. Mark each statement as evidence, derived recommendation, hypothesis, open question, or approved decision.

The following require explicit product-owner review before becoming a baseline:

- target customer, buyer, user roles, product scope, MVP boundary, and commercial promise;
- primary user tasks, information architecture, navigation, interaction model, and major visual direction;
- technology/framework/runtime choices and deployment topology;
- safety, tariff/settlement, identity, data-retention, and external integration policies.

Present consequential choices as a review packet: problem and evidence, options considered, trade-offs, recommended option, unresolved risks, and the exact decision requested. Record approval in the relevant PRD, Decision Record/ADR, or product design record. A document or PR is not approval by itself.

Routine implementation details may proceed under an approved design and ADR when they do not change those boundaries. If new evidence requires such a change, stop that dependent implementation and reopen the decision.

## 2. Product and visual design principles

Design for the verified job and context of Macau commercial-energy users. Do not assume that a familiar admin template, fashionable visual treatment, or interaction pattern is appropriate merely because it is common elsewhere.

- Start from observed user goals, language, environment, frequency, risk, and accessibility needs. Keep unvalidated personas and workflows labeled as hypotheses.
- Use mature design systems and research as reference material, then explain what is adopted, adapted, or rejected for this product. References are not templates to copy wholesale.
- Keep the interface current and purposeful: do not default to dated dashboard conventions, decorative gradients, needless cards, dense tables without hierarchy, or interaction patterns retained only from old prototypes. Test any familiar pattern against the actual task.
- For energy and operational data, communicate units, time range, freshness, source coverage, uncertainty, missing evidence, and action consequences. Never let color alone express status.
- Show clear system feedback, error recovery, user control, and confirmation for consequential actions. Do not imply that a shadow recommendation is an approved or executed control.
- Support responsive layouts and input modes appropriate to the validated device and work context; do not force a mobile-first or desktop-only shape without evidence.
- Treat visual polish as part of usability, not a substitute for task success, trust, or accessibility.

## 3. Required UI/UX Pro Max workflow

For a new product-wide visual direction or new page, use the installed UI/UX Pro Max skill at https://github.com/nextlevelbuilder/ui-ux-pro-max-skill:

1. Establish product type, target users/context, design intent, and the stack actually detected in the repository. Do not assume Next.js or another framework.
2. Run the skill's --design-system search for product-wide direction. Use focused domain searches for specific UX, accessibility, chart, typography, or stack questions.
3. Review the result for fit with energy operations, user evidence, accessibility, responsive needs, brand/product constraints, and current project authority. Preserve useful results and the reasoning; reject irrelevant recommendations rather than blindly applying them.
4. Present major visual and interaction choices as reviewable alternatives with rationale. Keep the design provisional until product-owner approval.
5. Evaluate flows with representative users when possible. Until then, label prototype feedback as heuristic/synthetic and avoid claims of user validation.
6. Before implementation acceptance, review keyboard and assistive-technology use, focus and error states, responsive behavior, chart interpretation, and reduced-motion behavior.

Use WCAG 2.2 AA as the proposed accessibility evaluation target for web UI, subject to applicability and project-owner review. The skill's search results are recommendations, not project authority.

## 4. Product/design review packet

Every substantial product or UI/UX review should include:

- user/problem statement and supporting research/evidence;
- users, context, top tasks, and explicit unknowns;
- proposed scope and non-goals;
- information architecture and key flows, including loading, empty, stale, partial, error, permission-denied, and recovery states;
- wireframe/prototype or concrete screen descriptions;
- visual-system rationale and skill searches used;
- usability/accessibility/responsive review plan;
- success and acceptance criteria;
- decisions requested from the product owner.

Approval records should state approver, date, artifact/version, and decision. If not approved, keep the work in draft/review status and capture requested changes.

## 5. Engineering delivery workflow

Use small, traceable increments:

1. **Research and discovery:** define the question, evidence quality, Gate dependencies, assumptions, and unresolved items.
2. **Product review:** confirm the target outcome, user workflow, scope, and acceptance evidence.
3. **Architecture review:** compare options; record boundaries and trade-offs in an ADR. Keep bake-off candidates provisional until the approved decision rule is satisfied.
4. **Detailed design:** define contracts, data ownership, failure behavior, authorization, observability, migration/rollback, and test/verification strategy.
5. **Task packet:** identify exact scope, affected modules, authority, non-goals, acceptance criteria, safety constraints, and deliverables.
6. **Implementation:** work in a branch and focused pull request; keep changes reviewable and generated work traceable to the packet.
7. **Validation and review:** run the checks required by the task packet and CI; review correctness, security, compatibility, accessibility where UI changes, and operational effects. Report checks not run.
8. **Release and learning:** deploy only through the approved release path; verify health and outcomes, retain rollback/recovery steps, and update evidence, decisions, Gate state, and CURRENT handoff.

A green CI run proves only the checks that actually ran. It does not by itself prove product fit, safety, bill correctness, Gate completion, or pilot authorization. Do not claim tests or validation that were not performed.

## 6. Definition of ready and done

A substantial task is **ready** when its owner, outcome, authority, dependencies, scope, acceptance evidence, and review path are explicit.

It is **done** when the deliverable is reviewable; approved boundaries are respected; required validation results and limitations are recorded; relevant product/architecture/evidence/handoff records are updated; and the next dependency-ready task is clear.

## 7. Reference sources

References are starting points for evaluation, not substitute approvals:

- UI/UX Pro Max skill: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- W3C, WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Google Material Design 3 foundations: https://m3.material.io/foundations/
- Nielsen Norman Group, 10 Usability Heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/
- Google Cloud DORA capabilities: https://docs.cloud.google.com/architecture/devops

Record retrieval date and relevant section when these references materially support a decision. Prefer direct user research and project-specific evidence when evaluating product fit.
