# AI Coding Quality Baseline v0.1

**Status:** Proposed engineering quality baseline; pending owner review.  
**Prepared:** 2026-10-04  
**Scope:** AI-assisted and human-authored code for the long-lived Macau Commercial Energy OS product.  
**Authority:** Stack-neutral. This document does not approve a language, framework, deployment platform, release topology, or production architecture.

## 1. Quality objective

AI coding is a governed engineering workflow, not code generation followed by a superficial green build. Every change must be traceable to approved product/architecture authority, understandable by a human reviewer, tested against its risk, safe to operate, and maintainable by a future engineer who did not author it.

Use mature internet engineering practices as evidence-informed references. Adapt their principles to this project's team size, energy/settlement domain and safety boundaries; do not copy large-company bureaucracy, tooling, or numerical targets without a reason.

## 2. Non-negotiable change rules

- Work starts from a linked task packet or approved issue with scope, authority, acceptance criteria, non-goals, risks and required evidence.
- A change is focused and reviewable. Separate unrelated refactors from behavior changes. If implementation discovers a necessary scope or architecture change, stop dependent work and raise the decision.
- Keep module boundaries, public contracts, tenant isolation, audit trails and fail-closed behaviors intact. Do not invent tariff, settlement, safety or customer-data semantics.
- Every logic or behavior change includes automated tests for the changed behavior and relevant regressions. Pure documentation changes use the documentation checks applicable to the repository.
- Run the required checks on the exact revision submitted for review. Report exact commands/results and checks not run; do not claim more evidence than a check provides.
- AI output is reviewed by a human with responsibility for the affected domain. AI cannot approve its own code, architecture, safety boundary, or release.
- Do not add a dependency, change a contract, loosen a security boundary, or alter a migration/release policy silently. Record the reason, compatibility/security review, and owner approval where the decision boundary requires it.

## 3. Risk-based verification

Select checks from changed behavior and failure impact. The task packet states the minimum set before implementation; reviewers can add checks when new risk is found.

| Change area | Minimum evidence to consider |
|---|---|
| Pure domain logic (tariffs, cost, forecasts, optimization) | Unit tests for normal, boundary, invalid and missing-evidence cases; deterministic/reproducibility checks where relevant; regression fixtures tied to approved evidence. |
| API, event, or shared contract | Schema/contract compatibility checks; consumer/provider tests; explicit versioning and migration path for breaking changes. |
| Database or persistence | Migration forward/rollback strategy, upgrade-path tests, data-integrity constraints and recovery evidence. |
| Authentication, authorization, tenancy, privacy or audit | Positive and negative authorization tests, cross-tenant isolation tests, abuse/failure scenarios, data-flow and retention review; security review for consequential changes. |
| Workflow, queues, retries or external integration | Idempotency, duplicate delivery, timeout, retry/backoff, partial failure, ordering and recovery tests appropriate to the contract. |
| User interface | Component/flow tests for important states; keyboard and focus checks; responsive and localization checks; accessibility review appropriate to the interface. |
| Release/runtime/infrastructure | Reproducible build, configuration/secrets checks, health/telemetry, deployment/rollback, backup/restore or recovery evidence as applicable. |

Use fast unit tests for rapid feedback and smaller numbers of integration/contract/end-to-end tests for system boundaries and critical user journeys. A single end-to-end suite is not a substitute for domain tests, and high line coverage is not proof of correctness. Do not impose a blanket coverage percentage without a measured baseline and a justified risk policy.

## 4. Required review gates

### Before implementation

- Read the task packet, current handoff, applicable architecture/Decision Records, contracts, safety constraints and repository-specific agent instructions.
- Confirm affected modules and dependency direction; identify data migrations, external effects, security/privacy boundaries and recovery needs.
- Define the acceptance evidence and exact validations. Ask for a decision when the task conflicts with authority.

### During implementation

- Follow repository formatting, lint, type/compiler and dependency-management rules after the stack is approved.
- Prefer clear domain names, cohesive modules, explicit errors and bounded side effects over clever or speculative abstractions.
- Keep configuration and secrets out of source. Validate untrusted inputs at boundaries. Make authorization and tenant scoping explicit.
- Consider timeout, cancellation, idempotency, concurrency, partial failure and observability when the feature crosses a process or service boundary.
- Keep dependency changes minimal; review maintenance status, license, vulnerability exposure, compatibility and lockfile updates.

### Before review / merge

- Build and required automated checks pass on the exact PR head; failed or skipped checks are visible and explained.
- The PR is linked to its task packet, describes behavior and risk, names important alternatives, records exact validation, and has a human reviewer.
- Review the actual diff for correctness, security/privacy, contract compatibility, error handling, readability, test quality, operational visibility and rollback.
- No unresolved critical/high security finding or required failed check is waived implicitly. Any risk acceptance names an accountable owner and durable decision record.
- Database/API/event changes have an explicit compatibility and rollout strategy. Runtime changes have health/readiness and failure/recovery behavior.
- Changes that affect service operation include the relevant dashboards/alerts, runbook, SLO/acceptance impact, and rollback plan before production release.

### Before production release

- Meet the approved product, security, privacy, reliability, performance and operational acceptance criteria for the declared release scope.
- Use a repeatable build and release process, staged rollout or equivalent risk-appropriate deployment, health verification, and a tested rollback/recovery path.
- Record release identity, configuration, approvals, known limitations, operational owner and post-release observation plan.
- Do not deploy to a customer/site or enable live energy control without the separate site/customer authorization and Gate evidence required by project authority.

## 5. AI-specific evidence and handoff

For every substantial AI-assisted coding task, the completion record states:

- task packet and authority followed;
- files/modules and behavior changed;
- design/contract decisions made or escalated;
- tests/checks actually run, exact revision, results and limitations;
- security, compatibility, migration and operations implications;
- unresolved risks, follow-up tasks and reviewer needed.

The final human reviewer should be able to understand the code and its tests without relying on the AI conversation. Persist required decisions, rationale, research and handoff in repository artifacts.

## 6. Quality signals

Use production and engineering signals to find systemic weaknesses, not to reward output volume. Establish baselines before setting targets. Review, as the service matures:

- escaped defects, incident severity and repeat incidents;
- change failure/rollback rate and recovery time;
- test feedback time, flaky-test rate and time-to-repair;
- PR review wait/size and rework;
- security/dependency findings and remediation age;
- SLO/error-budget performance, latency, capacity and data-quality failures;
- task success, user errors and accessibility defects.

Use measures to improve the system and workflow. Do not use lines of generated code, raw PR count, or test coverage alone as quality proxies.

## 7. Stack-specific annex after architecture approval

After G6.9-R2 Step 4 and owner architecture decisions, create or update a stack-specific standard with concrete tools and commands for:

- formatter, linter, compiler/type checker and build;
- unit, integration, contract, end-to-end and migration checks;
- dependency, secret, static-analysis and container/supply-chain checks;
- code ownership, PR approval and required CI rules;
- telemetry, SLOs, deployment, rollback and recovery;
- framework/language-specific error handling and security controls.

Until then, keep the baseline technology-neutral. Node/NestJS, React/TypeScript, Go, Python, Temporal, PostgreSQL/Timescale and other candidates retain their current provisional status.

## 8. Mature practice references

Use the relevant principles and record retrieval date when they materially inform a decision:

- [Google Engineering Practices: code review](https://google.github.io/eng-practices/) — focused changes, clear review context and tests.
- [DORA: test automation](https://dora.dev/capabilities/test-automation/) and [continuous delivery](https://dora.dev/capabilities/continuous-delivery/) — build quality throughout delivery and reduce release risk.
- [Google SRE: production readiness review](https://sre.google/sre-book/evolving-sre-engagement-model/) and [release engineering](https://sre.google/sre-book/release-engineering/) — production ownership, observability, repeatable release, staged rollout and rollback.
- [OWASP Application Security Verification Standard 5.0](https://github.com/OWASP/ASVS/tree/master/5.0) — verifiable application-security requirements.
- [OpenSSF Secure Software Development Framework (SSDF)](https://csrc.nist.gov/Projects/ssdf) — secure development practices across the lifecycle.

These references are not certifications or automatic proof of compliance. Select applicable controls based on the approved threat model, system scope, applicable law and owner-approved risk posture.
