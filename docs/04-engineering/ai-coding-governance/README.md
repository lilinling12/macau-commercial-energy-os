# AI Coding and Research Governance

AI is a continuous research and engineering capability for this project. Its continuity comes from versioned repository records, not from retaining one chat or assuming a new conversation can see the old one.

## Operating loop

Research Question → Evidence → Synthesis → Decision → Product / Architecture → Task Packet → AI-Assisted Work → Validation → Human Review → Durable Handoff

Use `docs/00-authority/handoff/CONTINUATION-PROTOCOL.md` to run and persist the research loop across conversations. Use `TASK-PACKET-TEMPLATE.md` to define substantial research, product, architecture, engineering, or pilot work.

## Required start sequence

1. Read `AGENTS.md`, `docs/00-authority/handoff/README.md`, `CONTINUATION-PROTOCOL.md`, `CURRENT.md`, and `ROADMAP.md`.
2. Read the relevant Decision Register, Open Questions, Gate, evidence, product, architecture, contract, and task packet.
3. Check current GitHub branch, PR, and file status when task progress may have changed.
4. State the active Gate, verified status, dependencies, and expected durable output.
5. Classify claims as verified, derived, hypothesis/project assumption, unknown, or approved decision.

## Research requirements

- Define the question, claim, Gate, and evidence needed before gathering sources.
- Prefer primary Macau regulator, utility, tariff, contract, meter, customer, and site evidence for Macau-specific claims.
- Record source, issuing body, URL/file, effective/publication/retrieval dates, relevant section, supported claim, and limitations.
- Preserve conflicting evidence and distinguish absence of evidence from evidence of absence.
- Update evidence, Gate outcomes, Open Questions, Decision Records, and CURRENT when their state changes.
- Do not treat an answer or plan in chat as durable project knowledge until it is written to the repository.

## AI-assisted implementation requirements

Follow [`AI-CODING-QUALITY-BASELINE-v0.1.md`](AI-CODING-QUALITY-BASELINE-v0.1.md) for task-risk-based verification, human review, security/compatibility/operability evidence, and release readiness. Use [`AI-CODING-GOVERNANCE-ADOPTION-PLAN-v0.1.md`](AI-CODING-GOVERNANCE-ADOPTION-PLAN-v0.1.md) to distinguish documented policy from enforced controls and to stage adoption. Both remain proposed and stack-neutral until owner review and architecture approval.

1. Define scope, non-goals, relevant Authority, contracts, safety constraints, acceptance evidence, and rollback/recovery expectations in a task packet.
2. Routine work may proceed under existing Authority. Architecture, contract, safety, settlement, or research-direction changes require an explicit Decision Record / ADR before implementation.
3. Keep provisional technology choices replaceable.
4. Run and report the packet's required validation; record exact checks and results, including checks not run.
5. Update relevant files and leave a cross-conversation handoff. Human review remains required for Authority, architecture, and operational decisions.

## AI agents must not

- silently change architecture or promote a candidate to a selected stack;
- weaken Safety Kernel or command-arbitration rules;
- invent unknown tariff, regulatory, or customer-contract semantics;
- break contracts without an approved migration;
- remove tenant, security, audit, or evidence boundaries;
- present PROJECT_ASSUMPTION as VERIFIED evidence;
- claim research, validation, pilot authorization, or Gate completion that was not evidenced.

## Definition of done

A substantial task is complete when its deliverable is reviewable, required checks/evidence are recorded, relevant project records are updated, and the next conversation can resume from the repository without depending on the prior chat. AI-generated work follows the same review, security, compatibility, and evidence requirements as human-authored work.
