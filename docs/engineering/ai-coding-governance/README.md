# AI Coding Governance

AI-assisted implementation is allowed and expected, but it operates under repository Authority.

## Required sequence

1. Read AGENTS.md.
2. Read docs/handoff/CURRENT.md.
3. Read only the Authority relevant to the task.
4. Identify contracts and architectural boundaries.
5. Define an explicit implementation scope.
6. Implement.
7. Validate.
8. Record evidence and update handoff when the gate changes.

## AI agents must not

- silently change architecture;
- weaken Safety Kernel or command-arbitration rules;
- invent unknown tariff or regulatory semantics;
- silently break contracts;
- remove tenant, security, audit, or evidence boundaries;
- present PROJECT_ASSUMPTION as VERIFIED evidence.

## Change classes

Routine implementation may proceed under existing Authority.

Architecture, contract, safety, settlement, or research-direction changes require an explicit Decision Record / ADR before implementation.

## Definition of done

Generated code is subject to the same tests, review, security checks, compatibility requirements, and evidence requirements as human-written code.
