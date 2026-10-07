# Platform API

Control-plane boundary for the Energy OS.

Initial responsibilities:
- tenant / organization / site metadata;
- Energy Graph metadata;
- device and telemetry-point registry;
- tariff-contract references;
- recommendation lifecycle;
- audit / evidence references.

## Candidate implementation status

The existing TypeScript/Node.js/NestJS path is **Candidate B implementation evidence only**. It is not an approved production runtime or architecture decision. G6.9-R2 Step 3D has not been executed and Step 4 remains pending; candidate and project-layer boundaries remain subject to owner review. See `docs/03-architecture/technology-authority/G6.9-technology-selection/README.md`.

The current code is a partial VS-001 scaffold. In particular, the inspected route lacks an authentication/authorization guard, graph and tariff adapters fail closed, and evidence storage is in memory. It is not production-ready functionality.

No runtime bootstrap or production adapter should be inferred from this README; follow repository Authority and approved Decision Records.
