# Development Workflow

The repository is an executable knowledge base: research, decisions, architecture, implementation, and validation evidence evolve together.

## Workflow

Issue
→ Authority check
→ Architecture / contract impact check
→ Task scope
→ Implementation
→ Validation
→ Review
→ Merge
→ Handoff update when current state changes

## Change rules

Changes to Energy Graph, tariff settlement semantics, safety/control boundaries, public contracts, or deployment trust boundaries require explicit architecture review.

Unknown regulatory or customer-specific inputs fail closed.

Research and implementation may proceed in parallel only when assumptions are explicitly tagged and cannot leak into production behavior as verified facts.

## Merge evidence

Every non-trivial change should identify:
- governing Authority;
- validation method;
- compatibility impact;
- unresolved unknowns;
- follow-up gate, if any.
