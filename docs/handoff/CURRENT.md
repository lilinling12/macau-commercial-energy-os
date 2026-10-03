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

Completed:
- Authority / handoff / decisions / evidence foundation;
- G0–G7 research-gate index;
- architecture and G6.9 technology Authority foundation;
- productization Authority foundation;
- engineering governance;
- PR / issue / CODEOWNERS governance;
- Authority and repository-hygiene CI;
- **Commit 004 Phase A — MVP Engineering Foundation**:
  - implementation module boundaries;
  - contracts-first package;
  - TelemetryEventV1;
  - OptimizationRecommendationV1;
  - EvidenceRecordV1;
  - platform-api / edge-runtime / optimizer / simulator boundaries;
  - VS-001 Energy Intelligence Loop;
  - contract JSON syntax CI.

## Current gate

**Commit 004 — MVP Engineering Foundation: Phase A complete.**

No application runtime bootstrap has been created yet.

## Next work

**Commit 004 Phase B — Runtime Bootstrap & Contract Validation**

Planned:
1. platform-api workspace bootstrap under the frozen TypeScript/Node/NestJS direction;
2. edge-runtime Go module bootstrap;
3. optimizer Python package bootstrap;
4. machine validation beyond JSON syntax;
5. first executable VS-001 fixture path;
6. keep tariff and simulator unknowns fail-closed.

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

GitHub state, verified evidence, and later Decision Records take precedence over chat memory.
