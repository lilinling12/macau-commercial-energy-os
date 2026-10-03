# Continue Prompt

Continue the Macau Commercial Energy OS from the repository's Research Authority. The repository, not prior chat memory, is the durable project record.

## Start here in every new conversation

Before research, product design, architecture, or implementation work, read:
1. `AGENTS.md`
2. `docs/00-authority/handoff/README.md`
3. `docs/00-authority/handoff/CONTINUATION-PROTOCOL.md`
4. `docs/00-authority/handoff/CURRENT.md`
5. `docs/00-authority/ROADMAP.md`
6. `docs/00-authority/decisions/DECISIONS.md`
7. `docs/00-authority/decisions/OPEN-QUESTIONS.md`
8. the current task packet, referenced evidence, Gate, product, architecture, and contract documents.

Check the live repository/PR state for work that may have changed since the last conversation. State the active Gate, verified status, missing evidence, and concrete durable output before substantial work.

## Authority chain

Research → Evidence → Decision → Product / Architecture → Engineering → Implementation → Validation → Handoff.

For research, follow `docs/00-authority/handoff/CONTINUATION-PROTOCOL.md`. For AI-assisted implementation, follow `docs/04-engineering/ai-coding-governance/README.md` and use `docs/04-engineering/ai-coding-governance/TASK-PACKET-TEMPLATE.md`.

Do not treat chat history as authority when it conflicts with verified evidence and versioned Decision Records. Do not silently change architecture, turn a candidate into a selected stack, or claim a Gate is complete without its required evidence and recorded decision.

## Current gates

- G1 Macau Tariff & Settlement remains OPEN.
- G6.9-R2 Step 3D framework-native pinned bake-off remains pending; Step 3C proves semantics only.
- G7.2 live R0 baseline/no-op remains pending.
- D-030's Java tariff implementation choice is suspended by D-069 while the bake-off remains open.
- Phase A/B/C code in main is retained; Node/NestJS is a provisional Candidate B implementation path, not a measured stack winner.

Continue the dependency-ready task in `docs/00-authority/handoff/CURRENT.md`. Preserve distinctions among verified Macau facts, derived calculations, hypotheses, project assumptions, unknowns, and customer-contract-specific evidence.

## End every substantial session

Persist research findings, source provenance, decisions, open questions, product/architecture impact, work results, and the next task in the appropriate repository files. Update CURRENT/HISTORY when the handoff changes so another conversation can continue without this chat.
