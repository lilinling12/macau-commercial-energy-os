# CURRENT — Macau Commercial Energy OS

**Snapshot:** 2026-10-03  
**Repository:** lilinling12/macau-commercial-energy-os  
**Authority mode:** research-first / evidence-governed

## Research state

- **G1 — Macau Tariff & Settlement Foundation:** OPEN.
- **G1.1 / G1.2:** completed.
- **G7 — Reference Simulator & Pilot Validation:** active in parallel.
- **G7.1 / G7.3 / G7.4 research:** completed.
- **G7.2 R0 live execution:** still pending.
- Known blocking unknowns remain authoritative until evidence closes them.

## Repository state

Completed on main:
- Authority / handoff / decisions / evidence foundation;
- G0–G7 research-gate index;
- architecture and G6.9 technology Authority foundation;
- productization Authority foundation;
- engineering governance;
- PR / issue / CODEOWNERS governance;
- Authority and repository-hygiene CI;
- Commit 004 Phase A — contracts-first MVP foundation and VS-001 definition.

Ready for review on PR #2:
- runtime baseline pinned;
- Node.js 24.21.0 + NestJS 12.0.3 platform-api bootstrap;
- Go 1.27.1 edge-runtime bootstrap;
- Python 3.14.8 optimizer bootstrap;
- contract fixtures and Draft 2020-12 machine validation;
- multi-runtime CI gate.

## Exact-head validation

PR #2 exact head is green for:
- Authority Validation;
- Repository Hygiene;
- Contracts Validation;
- Runtime Bootstrap:
  - Platform API typecheck/build;
  - Edge Runtime test/build;
  - Optimizer unit test;
  - Contract fixture validation.

The first Runtime Bootstrap attempt exposed an explicit TypeScript 6 Node-global configuration gap; it was fixed by adding `types: ["node"]` and the exact-head rerun is green.

## Current gate

**Commit 004 — MVP Engineering Foundation: Phase B READY FOR REVIEW.**

Issue: #1 — Runtime Bootstrap & Contract Validation.  
PR: #2 — Runtime Bootstrap & Contract Validation.

## Next work after Phase B merge

**Commit 004 Phase C — Executable VS-001 Domain Path**

Planned:
1. platform-api contract ingestion boundary;
2. minimal Energy Graph identifiers and resolution interfaces;
3. fail-closed tariff-resolution port;
4. optimizer shadow-mode request/response path;
5. evidence-record persistence boundary;
6. deterministic fixture replay.

## Non-negotiable open evidence

Do not claim:
- G1 closed;
- CEM Pu interval verified;
- G7.2 live baseline complete;
- synthetic reference-building results as Macau customer evidence;
- autonomous control authorized.

## Start here in a new conversation

Read, in order:
1. `AGENTS.md`
2. `docs/handoff/README.md`
3. `docs/handoff/CURRENT.md`
4. `docs/handoff/CONTINUE-PROMPT.md`
5. the Authority files referenced by the current task.

GitHub live state, exact-head CI, verified evidence, and later Decision Records take precedence over chat memory.
