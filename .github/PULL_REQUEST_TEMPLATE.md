# Pull Request

## Change record
- Task packet / issue:
- Accountable change owner (human):
- Primary reviewer (human):
- Risk tier (low / moderate / high / critical) and rationale:

## Context and intended outcome
Why is this change needed, and what user or operational outcome should it produce?

## Authority
List the governing files, approved decisions, ADRs, contracts, or research evidence. Label items that remain proposals or hypotheses.

## Scope
What is changed? What is explicitly not changed?

## Evidence status
Use one or more where relevant:
- VERIFIED
- DERIVED
- HYPOTHESIS
- PROJECT_ASSUMPTION
- UNKNOWN
- CONTRACT_VERIFIED

## Architecture, safety, security and data impact
- [ ] No architecture change
- [ ] Architecture change is covered by an ADR / decision record
- [ ] No safety-critical behavior changed
- [ ] Safety Kernel / command arbitration impact reviewed
- [ ] Tenant isolation, authorization and audit impact reviewed
- [ ] Personal-data, privacy, retention or external-processing impact reviewed
Describe applicable effects and the required domain/security review.

## Compatibility and operations
Describe contract, data, deployment, migration, observability, failure/recovery and rollback impact. Identify runbook or SLO changes when applicable.

## Validation evidence
List exact checks, simulations, replay evidence, schema checks or manual verification; include the commit SHA tested, result and anything skipped. If no check applies, explain why. Do not claim checks that did not run.

## Human review
Summarize relevant review feedback and unresolved risks. AI output is not an independent review or approval; include the responsible human reviewers for the affected domain and security/operations when risk requires it.

## Pre-merge checklist
- [ ] Read docs/00-authority/handoff/CURRENT.md and relevant Authority
- [ ] Linked task packet includes scope, non-goals, acceptance criteria and risk
- [ ] No silent architecture or contract change
- [ ] No silent weakening of tenant, security, privacy or safety boundaries
- [ ] Required validation passed on the exact PR head, or an approved exception is linked
- [ ] Human review is complete; AI is not counted as reviewer
- [ ] Migration, rollout, recovery and rollback plans are addressed where applicable
- [ ] PR body and durable project records are current
