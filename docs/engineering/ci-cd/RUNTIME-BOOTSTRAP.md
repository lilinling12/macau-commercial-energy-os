# Runtime Bootstrap CI

This gate validates the first executable boundaries without pretending the MVP is complete.

## Pinned baseline

- Node.js 24.21.0 LTS / npm 11.19.0
- NestJS 12.0.3
- TypeScript 6.0.3
- Go 1.27.1
- Python 3.14.8

## Jobs

### Platform API
- install declared dependencies;
- TypeScript strict typecheck;
- production build.

### Edge Runtime
- Go tests;
- build the edge entrypoint.

### Optimizer
- run standard-library unit tests with the package on PYTHONPATH.

### Contracts
- load JSON Schema Draft 2020-12;
- validate schema definitions;
- validate pinned VS-001 fixtures;
- enforce date-time formats.

## Limitations

This is a bootstrap gate. It does not yet prove:
- production dependency lock reproducibility;
- tenant isolation;
- tariff Golden Bill compatibility;
- live BOPTEST execution;
- Safety Kernel execution;
- site-specific control safety.

Those remain later gates.
