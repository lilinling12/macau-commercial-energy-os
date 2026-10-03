# CURRENT — Macau Commercial Energy OS

**Snapshot:** 2026-10-03  
**Authority mode:** research-first / evidence-governed  
**Research authority:** Library Research Authority v1.6.2 + G6.9-R2 Step 3C bake-off evidence  
**Repository:** lilinling12/macau-commercial-energy-os

## Project mission

Build a commercial multi-energy orchestration system for Macau commercial buildings and sites. It connects meters, BMS, HVAC/chiller plants, PV, ESS, EV and other flexible loads to physical topology, customer contracts and tariff/settlement rules. It evaluates total economic energy cost/value, recommends safe actions, and preserves evidence for replay and measurement & verification.

This is not a generic energy dashboard, chatbot, BMS replacement, or kWh-only optimizer. Cloud recommendations do not directly control devices; site Edge and the Safety Kernel own command validation and execution. Initial operation remains SHADOW/advisory until evidence and authorization gates are met.

## Research state

- **G1 — Macau Tariff & Settlement Foundation:** OPEN. G1.1/G1.2 completed; commercial bill, demand-window and cross-site PV questions remain; U-026 tracks an official PV-count discrepancy.
- **G6.9-R2 — Technology Stack Bake-off:** Step 3A, 3B and 3C complete; **Step 3D pinned framework-native integration pending**.
- **G7 — Reference Simulator & Pilot Validation:** active in parallel; G7.2 live baseline/no-op still pending; U-017 live response/rebound remains open.
- Research Authority v1.6.2 contains D-001..D-076 and U-001..U-024. This repository must preserve the same records; see the technology and decision documents.
- Official CEM PV material confirms an approved grid-interconnection and feed-in-tariff route. It does **not** establish cross-building virtual netting or a customer's right to claim another building's PV generation; U-025 tracks that question.

## Repository implementation state

Completed on main:
- Authority / handoff / evidence foundation;
- detailed decisions D-001..D-055 and unknowns U-001..U-017;
- Commit 004 Phase A contracts-first foundation;
- Phase B Node/NestJS, Go Edge and Python Optimizer bootstrap;
- Phase C VS-001 domain path, merged via PR #4.

The Phase B Node/NestJS code is an existing implementation path corresponding to Candidate B. It is not evidence that Candidate B won the open G6.9-R2 bake-off. Treat it as provisional until Step 3D evidence and an explicit Decision Record select or revise the production stack.

## Current authority for technical architecture

The owner-confirmed provisional layer summary is:
- Frontend: React + TypeScript.
- Application: TypeScript/Go hybrid responsibilities under evaluation.
- Workflow: Temporal candidate.
- Data: PostgreSQL + Timescale baseline.
- Event: NATS JetStream candidate.
- AI / Optimization: Python.
- Edge: Go.
- Future plugin isolation: Wasm/WASI direction.

This layer summary does not replace the bake-off's topology candidates. C+ (Go authoritative Energy Core + Temporal Go workers + Go Edge/Safety, thin Bun/Hono/TypeScript product surface, Python intelligence) remains a **provisional default**, not a measured winner. A and B remain candidates until the common Step 3D/Step 4 decision rule is satisfied. See D-062..D-076.

## Research sequence and next work

The research-to-delivery chain is:
**Research → Evidence → Decision → Architecture → Engineering → Implementation.**

Immediate work:
1. Continue G1 with authoritative Macau tariff/billing evidence, including U-025 cross-site PV rights and settlement.
2. Execute G6.9-R2 Step 3D in the pinned environment; do not infer a framework winner from Step 3C.
3. Execute G7.2 live baseline/no-op when the pinned BOPTEST runtime is available.
4. Only then revise technology decisions and authorize dependent production implementation.

## Suspended implementation gate

The previous “Phase D — Java 25 tariff-core bootstrap” is **SUSPENDED** by D-069 while G6.9-R2 remains open. D-030's tariff semantic architecture remains active, but its Java/Spring implementation choice is not current production authority. Do not start or describe Java Phase D as the next implementation gate absent a completed bake-off or a separately justified, approved decision.

## Non-negotiable open evidence

Do not claim:
- G1 is closed;
- CEM Pu averaging interval is verified;
- cross-site/virtual PV netting is authorized;
- G7.2 live baseline is complete;
- synthetic reference-building results are Macau customer evidence;
- autonomous control is authorized;
- SAT/CHWS perturbations reduce total site power until U-017 is resolved.

## Start here in a new conversation

Read:
1. `AGENTS.md`
2. `docs/handoff/README.md`
3. `docs/handoff/CURRENT.md`
4. `docs/decisions/DECISIONS.md`
5. `docs/decisions/OPEN-QUESTIONS.md`
6. `docs/technology/G6.9-technology-selection/README.md`
7. `docs/evidence/G1-PV-GRID-INTERCONNECTION-2026-10.md`
8. Authority files referenced by the current task.

GitHub live state, exact-head CI, verified evidence, and Decision Records take precedence over chat memory.
