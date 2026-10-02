# Authority Validation CI

## Purpose

The first CI gate protects the repository's research and architecture continuity before application code exists.

It deliberately avoids pretending that runtime tests exist before the runtime exists.

## Current checks

- required Authority entrypoints exist;
- the evidence-status vocabulary remains present;
- AGENTS.md points contributors to the current Authority;
- merge-conflict markers are rejected;
- tracked .env-style secret files are rejected;
- the cross-chat handoff entrypoint remains present.

## Expansion rule

As implementation lands, CI must add module-specific validation rather than weakening this gate.

Planned additions include:

- contract/schema compatibility;
- tenant-isolation tests;
- tariff Golden Bill fixtures;
- historical settlement replay;
- simulator regression;
- optimization feasibility;
- Safety Kernel and command-arbitration tests;
- edge protocol compatibility;
- supply-chain and dependency checks.

A green workflow never upgrades UNKNOWN or PROJECT_ASSUMPTION evidence into VERIFIED evidence.
