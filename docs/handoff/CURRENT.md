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
- Detailed Decision Register **D-001..D-055** has been restored from the original Research Authority.
- Blocking Unknown Register **U-001..U-017** is restored; U-017 remains open for live SAT/CHWS response/rebound evidence.

## Repository state

Completed on main:
- Authority / handoff / evidence foundation;
- detailed decisions and blocking unknowns restored;
- architecture and technology Authority foundation;
- productization Authority foundation;
- engineering governance;
- PR / issue / CODEOWNERS governance;
- Authority / repository hygiene / contract CI;
- Commit 004 Phase A — contracts-first MVP foundation and VS-001 definition;
- **Commit 004 Phase B — Runtime Bootstrap & Contract Validation merged via PR #2**.

Phase B merge commit:
- `be28ced3361e7d3994251bc0bf9331a8adb3dc6b`

Phase B validation:
- Authority Validation ✅
- Repository Hygiene ✅
- Contracts Validation ✅
- Runtime Bootstrap ✅
  - Platform API typecheck/build
  - Edge Runtime test/build
  - Optimizer unit test
  - Contract fixture validation

## Current gate

**Commit 004 Phase C — Executable VS-001 Domain Path: MERGED.**

Merged via PR #4:
1. platform-api telemetry contract ingestion boundary;
2. explicit Energy Graph / Tariff / Optimizer / Evidence ports;
3. tenant/site boundary enforcement;
4. fail-closed unresolved tariff behavior;
5. SHADOW-only optimizer boundary for VS-001;
6. deterministic Evidence ID generation;
7. deterministic fixture replay;
8. CI coverage for resolved, unresolved, tenant-mismatch, and replay determinism.

Phase C merge commit:
- `83ba35c25b9aa04c80f2f9d592b3b1c6dfed3acb`

Production adapters remain intentionally fail-closed until later Authority binds verified implementations.

## Next gate

**Commit 004 Phase D — Authoritative Tariff Core Bootstrap**

Scope:
1. bootstrap the D-030 Java 25 pure `tariff-core` boundary;
2. model effective-date tariff package identity;
3. model `DemandMeasurementPolicy` explicitly without assuming U-001;
4. expose deterministic evaluation result types;
5. preserve exact-evaluator / optimizer-compiler separation;
6. keep unknown regulatory inputs fail-closed;
7. add initial Golden Fixture harness structure without claiming Golden Bill closure.

## Non-negotiable open evidence

Do not claim:
- G1 closed;
- CEM Pu interval verified;
- G7.2 live baseline complete;
- synthetic reference-building results as Macau customer evidence;
- autonomous control authorized;
- total-site power reduction from SAT/CHWS perturbation until U-017 is resolved.

## Start here in a new conversation

Read, in order:
1. `AGENTS.md`
2. `docs/handoff/README.md`
3. `docs/handoff/CURRENT.md`
4. `docs/handoff/CONTINUE-PROMPT.md`
5. `docs/decisions/DECISIONS.md`
6. `docs/decisions/OPEN-QUESTIONS.md`
7. only the additional Authority files referenced by the current task.

GitHub live state, exact-head CI, verified evidence, and Decision Records take precedence over chat memory.
