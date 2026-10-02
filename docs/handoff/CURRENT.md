# CURRENT — Macau Commercial Energy OS

**Snapshot:** 2026-10-03  
**Repository:** lilinling12/macau-commercial-energy-os  
**Authority mode:** research-first / evidence-governed

## Research state recovered from the original Authority

- **G1 — Macau Tariff & Settlement Foundation:** OPEN.
- **G1.1 / G1.2:** completed.
- **G7 — Reference Simulator & Pilot Validation:** active in parallel.
- **G7.1 / G7.3 / G7.4 research:** completed.
- **G7.2 R0 live execution:** still pending; static preflight alone is not sufficient.
- Known blocking unknowns remain authoritative until evidence closes them.

## Repository migration state

Completed:
- handoff / decisions / evidence foundation;
- G0–G7 research-gate index;
- architecture Authority foundation;
- G6.9 technology Authority foundation;
- productization Authority foundation;
- engineering governance foundation;
- PR / issue / CODEOWNERS governance;
- AI-coding and development workflow governance;
- first real GitHub Actions CI gates.

## Current work

**Commit 003 — Engineering Governance Bootstrap: substantially complete.**

Current CI:
- authority structure validation;
- evidence vocabulary validation;
- repository hygiene checks.

## Next gate

**Commit 004 — MVP Engineering Foundation**

Before generating application code:
1. define the repository/module skeleton;
2. establish contracts-first package boundaries;
3. map the first vertical slice:
   Telemetry → Energy Graph → Tariff Resolution → Cost Analysis → Recommendation → Evidence;
4. preserve the original research unknowns and safety boundaries;
5. do not claim G1 or G7.2 closed without the required evidence.

## Start here in a new conversation

Read, in order:
1. `AGENTS.md`
2. `docs/handoff/README.md`
3. `docs/handoff/CURRENT.md`
4. `docs/handoff/CONTINUE-PROMPT.md`
5. only the Authority files referenced by the current task.

Repository state, verified evidence, and later Decision Records take precedence over chat memory.
