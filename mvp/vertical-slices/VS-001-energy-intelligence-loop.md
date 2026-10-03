# VS-001 — Energy Intelligence Loop

## Goal

Prove an end-to-end, evidence-producing economic intelligence loop before direct equipment control.

## Flow

Telemetry Event
→ point/device resolution
→ Energy Graph context
→ settlement meter / contract resolution
→ Tariff Version resolution
→ cost calculation
→ optimization shadow-mode recommendation
→ Evidence Record

## Acceptance boundary

The slice is complete only when:
- contract payloads are validated;
- tenant/site boundaries are preserved;
- tariff resolution is effective-date aware;
- unknown settlement semantics fail closed;
- recommendation is advisory by default;
- result links to evidence status and source references;
- replay is deterministic for pinned fixtures.

## Explicitly out of scope

- autonomous safety-critical execution;
- assuming the CEM Pu averaging window;
- claiming Macau customer savings from synthetic fixtures;
- defaulting PV settlement topology;
- defaulting ESS grid-export permission.

## Research dependencies

G1 remains open.
G7.2 live R0 execution remains pending.
The implementation must expose these unknowns rather than conceal them.
