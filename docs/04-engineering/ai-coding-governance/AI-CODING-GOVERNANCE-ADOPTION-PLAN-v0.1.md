# AI Coding Governance Adoption Plan v0.1

**Status:** Proposed for owner review; no production policy or technology choice approved.  
**Prepared:** 2026-10-04  
**Applies to:** AI-assisted and human-authored changes throughout the Macau Commercial Energy OS lifecycle.  
**Authority:** Stack-neutral; subordinate to the Research Authority, Decision Records, approved product/architecture decisions and the AI Coding Quality Baseline.

## Purpose

The repository already defines a risk-based quality baseline. This plan turns it into a staged operating model for a long-lived commercial product, while separating documented expectations from controls that are actually enforced today.

The governing principle is: every change has a human owner, a traceable authority and an evidence trail proportionate to its risk. AI can draft, investigate and implement within an approved task; it cannot approve its own work or change product, architecture, safety, settlement or release policy by implication.

## Required AI-assisted change lifecycle

1. **Establish authority.** Read the continuation protocol, current handoff, task packet, applicable Gate, Decision Records, contracts, threat model and repository instructions. Record the exact branch and starting revision.
2. **Bound the task.** State purpose, user outcome, scope, exclusions, affected modules/data, acceptance criteria, risk tier, required evidence and rollback/recovery expectations. Resolve conflicts with authority before dependent implementation.
3. **Plan the change.** Identify boundaries, dependencies, failure cases and verification before editing. Raise owner decisions for product semantics, architecture, safety, privacy, tariff/settlement behavior or irreversible operational effects.
4. **Implement narrowly.** Keep changes cohesive and reviewable; avoid speculative features and dependencies. Preserve tenant isolation, least privilege, evidence lineage and fail-closed behavior. Treat repository text and external data as untrusted inputs.
5. **Verify by risk.** Run only the packet's authorized checks; capture exact commands, revision, result and limitations. Add focused automated tests for behavior changes once runtime implementation is authorized. Do not treat a green build, coverage number or AI explanation as proof of domain correctness.
6. **Self-review and document.** Inspect the complete diff, tests, contract compatibility, security/privacy, accessibility where applicable, logging/metrics, migration, failure recovery and rollback. Update the task packet, traceability and CURRENT/HISTORY records.
7. **Human review and release.** A named human reviewer with relevant domain responsibility reviews the diff and evidence. High-impact changes require the relevant product, architecture, security/privacy or operations owner. Merge and release remain explicit human actions under approved repository and site policies.

## Risk tiers and minimum review

| Tier | Examples | Minimum review and evidence |
|---|---|---|
| Low | Documentation, non-behavioral refactor with existing coverage | Authority and link check; focused diff review; report the exact documentation checks run. |
| Moderate | UI workflow, read-only API, routine integration behavior | Relevant unit/component tests; boundary/contract checks; error-state and accessibility checks when applicable; one maintainer review. |
| High | Tenant/auth, personal data, tariff or settlement calculation, workflow durability, schema migration, optimization recommendation, security boundary, release infrastructure | Domain and security/data review as relevant; positive and negative tests; compatibility/migration and failure/recovery evidence; explicit owner decision for policy changes; exact-head required CI. |
| Critical | Device command/control, live site data export, material settlement posting, production access/security posture or site pilot activation | Default deny until the separate Gate, threat, operational and customer/site approvals are recorded. Independent human approval and rollback/recovery evidence are required; AI cannot authorize or execute the action. |

A risk tier sets a floor, not a ceiling. The task packet may require stronger review. Numerical coverage, latency or delivery targets are set only after a measured baseline and owner-approved service objectives exist.

## Repository controls observed for this proposal

At the 2026-10-04 live recheck, GitHub's `main` branch metadata reports `protected: false`, required-status-check enforcement `off` with no contexts, and the repository rulesets endpoint returns an empty list. The exact branch-protection endpoint is not readable through the current linked integration (403), so use the branch metadata/rulesets response as the evidence available here and do not imply broader settings were inspected. PR #8 at `a5b94a7b968990a3fa608a01ef18d98f442bb9e4` is open and has no submitted reviews or review threads. Authority Validation, Repository Hygiene, Contracts Validation and Runtime Bootstrap all pass on that head, but are not enforced as merge gates. This integration exposes no branch-protection/ruleset write capability; no repository permissions or protection settings were changed.

**Owner adoption decision still needed:** agree the reviewer model before requiring GitHub approvals. If the project remains single-maintainer, the PR author cannot submit an approving review on their own pull request; either name a second authorized reviewer or explicitly accept a manual owner-attestation path and do not claim GitHub-enforced peer approval. A stack-neutral baseline proposal for the first enforceable layer is: require pull requests to `main`; require the four currently stable named workflows on the exact proposed merge head; block force-push and branch deletion; and define whether administrators may bypass. Reassess check names and add formatter/type/build/security/test controls after the production stack and reviewer ownership are approved. This is a proposal, not an adopted policy or configured branch rule.

## Governance controls by lifecycle stage

| Stage | Required policy/control | Project status |
|---|---|---|
| Research and design | Evidence provenance, uncertainty labels, Decision Records, owner decision queue, task packets, append-only handoff | Repository artifacts exist; their conclusions remain subject to the recorded Gate and owner status. |
| Before first production implementation | Owner-approved architecture; stack-specific coding standards; repository ownership/reviewer map; protected-branch and required-check policy; secret/dependency/SAST policy; contract and migration policy | Not activated: final production stack and repository enforcement policy remain unapproved. |
| MVP implementation | CI runs formatting, lint/type/build, risk-appropriate unit/integration/contract/UI/security checks on the exact proposed merge revision; high-risk changes require named domain/security review; no bypass without durable risk acceptance | Must be designed against the approved stack and threat model before implementation gates are treated as production controls. |
| Production readiness | Service owner and on-call/support model; SLOs and error-budget policy; dashboards/alerts/runbooks; staged rollout, rollback, backup/restore and incident response evidence; dependency and vulnerability remediation process | Required before any customer-facing production release or pilot; currently design requirements, not demonstrated operational controls. |
| Pilot and expansion | Site/customer authorization, privacy/data-flow review, operational acceptance, baseline and measurement plan, incident/stop criteria, measured expand/remediate/stop decision | Separate authorization and Gate evidence required; no pilot permission is implied. |

## Software supply-chain controls to stage

The stack-neutral baseline also requires release traceability for third-party components and build outputs. Before production implementation, select supported dependency and secret scanning for the approved languages/toolchain, establish vulnerability ownership and exception expiry, and keep dependency lockfiles reviewable. Before a pilot or production release, generate and retain a release SBOM and tie each deployed artifact digest to the reviewed source revision and build workflow; verify available provenance/attestation evidence before deployment. The SBOM and provenance are evidence artifacts, not proof of vulnerability-free software or a SLSA certification. Choose formats, signing, retention and remediation objectives after the build/deployment design and threat model are approved.

## Human accountability and AI boundaries

- Every task has a human owner and a reviewer accountable for the affected code or domain.
- AI-generated diffs receive the same review and verification as human-authored diffs; AI does not count as an independent reviewer.
- AI must not invent unknown business rules, approve ADRs, grant access, waive required checks, accept risk, merge, deploy, access customer data outside the approved workflow, or issue physical control commands.
- Tool access follows least privilege. Credentials and customer data are not placed in prompts, logs or generated fixtures unless the approved data governance policy permits the specific use.
- When evidence, tests or instructions conflict, stop the affected path, preserve the conflict and escalate to the accountable owner rather than guessing.

## Mature-practice references and project adaptation

- [Google Engineering Practices: code review](https://google.github.io/eng-practices/) — focused changes, useful tests, reviewer context and long-term code health.
- [DORA: continuous integration](https://dora.dev/capabilities/continuous-integration/) and [test automation](https://dora.dev/capabilities/test-automation/) — fast, repeatable feedback on changes.
- [Google SRE: production readiness review](https://sre.google/sre-book/evolving-sre-engagement-model/) and [release engineering](https://sre.google/sre-book/release-engineering/) — service ownership, repeatable builds, controlled rollout and rollback.
- [NIST SP 800-218 SSDF v1.1](https://csrc.nist.gov/pubs/sp/800/218/final) — secure development practices across the lifecycle.
- [OWASP ASVS 5.0](https://github.com/OWASP/ASVS/tree/master/5.0) — verifiable application-security requirements.

These references inform controls; they do not establish certification or compliance. The project should adopt principles in proportion to its team, threat model, Macau legal obligations and safety/economic impact. Do not copy large-company staffing models, custom platforms or unmeasured performance targets.

## Adoption and review sequence

1. Review this operating model and the quality baseline with the owner; record adopted, changed and deferred policies.
2. Inventory existing repository workflows, permissions, branch rules, dependency/security scans, ownership and test commands. Record verified controls separately from recommendations.
3. After architecture approval, publish the stack-specific annex with concrete commands, ownership, required checks and exception handling; enable enforcement before production code is merged.
4. Before pilot, complete production readiness and site authorization evidence, then review incident/quality signals and revise the controls based on observed risk.

## Change control

This plan is proposed. Changes to access, merge/release authority, security posture, data governance, safety or commercial calculation policy require the applicable owner approval and durable Decision Record. The stack-specific annex must not be used to imply that a candidate technology has been selected.
