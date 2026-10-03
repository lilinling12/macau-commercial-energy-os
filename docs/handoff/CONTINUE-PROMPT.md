# Continue Prompt

Continue the Macau Commercial Energy OS from the repository's Research Authority.

Before research, architecture, or implementation work, read:
1. `AGENTS.md`
2. `docs/handoff/README.md`
3. `docs/handoff/CURRENT.md`
4. `docs/decisions/DECISIONS.md`
5. `docs/decisions/OPEN-QUESTIONS.md`
6. the current task's referenced evidence and gate documents.

## Authority chain

Research → Evidence → Decision → Architecture → Engineering → Implementation.

Do not treat chat history as authority when it conflicts with verified evidence and versioned Decision Records. Do not silently change architecture or convert a candidate into a selected stack.

## Current gates

- G1 Macau Tariff & Settlement remains OPEN.
- G6.9-R2 Step 3D framework-native pinned bake-off remains pending; Step 3C proves semantics only.
- G7.2 live R0 baseline/no-op remains pending.
- D-030's Java tariff implementation choice is suspended by D-069 while the bake-off remains open.
- Phase A/B/C code in main is retained; Node/NestJS is a provisional Candidate B implementation path, not a measured stack winner.

Continue the active research gate listed in `docs/handoff/CURRENT.md`. Preserve the distinctions among verified Macau facts, derived calculations, hypotheses, project assumptions, unknowns, and customer-contract-specific evidence.
