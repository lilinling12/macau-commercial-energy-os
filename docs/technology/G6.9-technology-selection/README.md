# G6.9 Technology Selection — Current Authority

**Snapshot:** 2026-10-03  
**Authority source:** Research Authority v1.6.2 and G6.9-R2 Step 3A–3C evidence  
**Status:** Candidate evaluation remains open; no measured production-stack winner.

## Project-level provisional architecture

- **Frontend:** React + TypeScript.
- **Application:** TypeScript / Go responsibility split under evaluation.
- **Durable workflow:** Temporal candidate.
- **Data:** PostgreSQL + Timescale baseline.
- **Cloud events:** NATS JetStream candidate.
- **AI / forecasting / optimization / simulation:** Python.
- **Site Edge and Safety Kernel:** Go.
- **Future plugin isolation:** Wasm/WASI direction; not an MVP implementation commitment.

## G6.9-R2 topology candidates

- **A — TS Native:** Bun + Hono + Effect 4 product/API surface, with an authentic Node runtime for Temporal TypeScript workers while that SDK support boundary applies.
- **B — TS Enterprise:** Node 24 LTS + NestJS/Fastify + Temporal TypeScript workers.
- **C+ — Go authoritative core:** Go Energy Core + Temporal Go workers + Go Edge/Safety Kernel, with a thin Bun/Hono/TypeScript product/BFF surface and Python intelligence.

C+ is the **provisional default hypothesis**, not the bake-off winner. A and B remain candidates. The layer summary above and topology candidates are different levels of description; neither should be silently substituted for the other.

## Evidence completed and pending

Step 3A established a common experiment pack. Step 3B checked protocol semantics across available Node and Go runtimes. Step 3C ran a semantic vertical slice and recovery case using the available Node/Go/Python shells. Step 3C did not run the candidate frameworks or common Postgres/Timescale, Temporal, NATS, MQTT 5 and OpenTelemetry stack together; it did not produce comparable performance or AI engineering results.

**Next:** Step 3D pinned framework-native integration and failure testing, followed by the controlled candidate comparison. Keep U-018..U-024 open until their evidence criteria are met.

## Existing Node/NestJS implementation

The repository contains Phase B/C implementation work using Node/NestJS. This is retained as a provisional Candidate B path and does not constitute a decision that B won. No implementation status may close a research gate without its specified evidence.

## Java and D-030

D-030's tariff semantic design remains active. Its Java 25 / Spring Boot implementation selection is historical and is **suspended by D-069** while G6.9-R2 is open. Java is not the default MVP stack. Resume that implementation choice only after the bake-off or a separate approved, evidence-backed decision.

## Decision records

See D-062..D-076 in `docs/decisions/DECISIONS.md`. In particular: D-064 (C+ provisional only), D-068 (common bake-off required), D-069 (suspend Java implementation authority), and D-076 (Step 3C is semantic evidence only).
