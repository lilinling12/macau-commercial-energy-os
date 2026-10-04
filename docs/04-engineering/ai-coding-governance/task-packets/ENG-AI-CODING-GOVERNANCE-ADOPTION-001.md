# ENG-AI-CODING-GOVERNANCE-ADOPTION-001 — AI coding governance adoption model

## Identity

- **Task ID / title:** ENG-AI-CODING-GOVERNANCE-ADOPTION-001 — AI coding governance adoption model
- **Type:** Engineering governance
- **Workstream:** Cross-cutting continuous AI research and coding; WP-5/WP-6 readiness
- **Status:** Review
- **Owner / reviewer:** Product owner; engineering, security/data and operations review required
- **Created / updated:** 2026-10-04

## Outcome

- **Question:** How should the project turn a stack-neutral AI Coding Quality Baseline into proportionate, enforceable governance for a long-lived commercial product?
- **User/business outcome:** Changes remain traceable, reviewable, tested by risk, secure and operable; AI assists delivery without taking authority over domain policy, architecture, risk acceptance or releases.
- **Deliverables:** AI Coding Governance Adoption Plan v0.1; explicit connection to the lifecycle goal; roadmap and handoff links.
- **Why now:** The repository already has a proposed quality baseline and a sustained product-to-pilot goal. Governance needs staged controls before implementation grows, while exact tools must wait for owner-approved architecture.

## Authority and constraints

- **Authority:** docs/04-engineering/ai-coding-governance/AI-CODING-QUALITY-BASELINE-v0.1.md; docs/00-authority/PRODUCT-ARCHITECTURE-DELIVERY-GOAL-v0.1.md; docs/00-authority/ROADMAP.md; existing Research Authority and Decision Records.
- **Current state:** Baseline and adoption plan are proposals. Production language/framework, reviewer ownership, stack-specific commands, service SLOs and release processes are not established by this task. GitHub reports main unprotected, required status checks disabled and no repository rulesets; four CI workflows exist but are not required merge gates.
- **Constraints:** Do not claim compliance or certification; do not set arbitrary coverage/velocity targets; do not authorize customer-data processing, merge/release changes, live control or pilot operations; preserve owner decision boundaries and SHADOW/advisory scope.

## Scope

### In scope

- Define human accountability, bounded AI authority, task-to-authority traceability, risk-based review/verification and durable evidence.
- Separate written expectations from currently enforced repository controls.
- Stage governance across research/design, pre-implementation, MVP implementation, production readiness and pilot.
- Ground the proposal in mature engineering/security/reliability practices and adapt them to team and domain risk.

### Out of scope

- Owner adoption or final policy approval.
- Selecting a production technology stack or adding stack-specific tool commands.
- Changing repository permissions, branch protection, reviewer assignments or CI workflow enforcement.
- Implementing application/runtime behavior or claiming control, security or reliability validation.
- Setting service SLOs or numerical coverage/delivery targets without an approved baseline.

## Acceptance criteria

1. The plan defines a complete AI-assisted change lifecycle with a named human owner, scope/authority, implementation, risk-appropriate validation, self-review, human review and handoff.
2. Review tiers distinguish low/moderate/high/critical consequences and state minimum evidence without inventing universal numeric targets.
3. A staged adoption map marks each control as proposed, not activated, stack-dependent, or required before pilot/production.
4. AI is explicitly unable to self-approve, accept risk, merge, release, grant access, define unknown business semantics or authorize device commands.
5. The plan references applicable mature practices and states that references do not equal certification.
6. The governance README links to the baseline and adoption plan; templates capture their task/review requirements. Lifecycle charter, roadmap and CURRENT integration is coordinated with PR #8 and remains pending that broader review.
7. The reusable task-packet and PR templates capture accountable human ownership/review, risk tier, authority, exact-revision checks and relevant security/compatibility/operations review.
8. Exact-head documentation/workflow results and limitations are recorded; no application behavior or tests are claimed.

## Verification and evidence

- Check document links and status wording in repository authority records.
- Run the repository's applicable documentation/governance CI on the exact resulting PR head; record workflow names and outcomes in this packet.
- No application/runtime tests, customer-data processing or external integration checks are in scope.

## Completion record

- **Changes/deliverables:** Prepared the proposed staged adoption plan and stack-neutral quality baseline as an independently reviewable policy package. The plan defines the AI-assisted change lifecycle, risk tiers, human accountability, staged enforcement and official mature-practice references. Lifecycle-charter/roadmap/handoff integration remains in the broader PR #8.
- **Files updated:** AI-CODING-GOVERNANCE-ADOPTION-PLAN-v0.1.md; AI-CODING-QUALITY-BASELINE-v0.1.md; governance README; TASK-PACKET-TEMPLATE.md; .github/PULL_REQUEST_TEMPLATE.md; this packet.
- **Evidence / decisions / unknowns:** At the review snapshot, four CI workflows exist (Authority Validation, Repository Hygiene, Runtime Bootstrap, Contracts Validation), but GitHub reports main unprotected, required status checks disabled and no repository rulesets. PR-triggered actions also exercise existing scaffold checks; those results are recorded against the exact head in PR #8 and do not validate the governance proposal's operational enforcement. This task changed no application implementation. Owner adoption, reviewer ownership, stack-specific enforcement, service SLOs and release policy remain open.
- **PR/branch:** This focused policy package is on branch `docs/ai-coding-governance-baseline`; lifecycle-charter, roadmap and handoff integration remains in broader PR #8.
- **Gate status:** No research Gate closed; this is cross-cutting governance proposal work.
- **Next dependency:** Owner review; then inventory live repository controls. Write and enforce a stack-specific annex after the production architecture is approved and before production code merge.
