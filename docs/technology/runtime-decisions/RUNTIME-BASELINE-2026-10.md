# Runtime Baseline — 2026-10

Evidence status: VERIFIED for public runtime releases; PROJECT_DECISION for repository adoption.

## Control plane

- Node.js 24.21.0 LTS.
- npm 11.19.0 bundled with Node.js 24.21.0.
- NestJS 12.0.3.
- TypeScript 6.0.3 for the initial NestJS 12 compatibility baseline.

The current NestJS 12 migration guidance is centered on ESM and TypeScript 6. Although TypeScript 7 exists, this repository does not adopt it until NestJS compatibility is deliberately re-evaluated.

## Edge runtime

- Go 1.27.1.

## Optimizer

- Python 3.14.8.

## Bun decision

Bun is not the production runtime for the control plane in this baseline.

Reason:
- the governing Authority already selects Node.js LTS + NestJS for the control plane;
- the MVP benefits from one production JavaScript runtime and the package manager already bundled with that runtime;
- introducing Bun here would add a second JavaScript runtime/toolchain before there is evidence that it improves this product.

Bun may be evaluated later as a developer-tooling or isolated-runtime candidate. Such adoption requires its own compatibility evidence and Decision Record.

## Upgrade rule

Patch/minor upgrades within these selected major lines may be proposed through normal engineering governance. A runtime-major change requires a new decision record with compatibility and migration evidence.
