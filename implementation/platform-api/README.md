# Platform API

Control-plane boundary for the Energy OS.

Initial responsibilities:
- tenant / organization / site metadata;
- Energy Graph metadata;
- device and telemetry-point registry;
- tariff-contract references;
- recommendation lifecycle;
- audit / evidence references.

Initial runtime direction:
- TypeScript;
- Node.js LTS;
- NestJS modular monolith.

No runtime bootstrap is added until contract and module boundaries are accepted by the current Authority.
