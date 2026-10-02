# Runtime Decisions

## Purpose

Record runtime and deployment boundary decisions for Macau Commercial Energy OS.

## Runtime Boundary

Control Plane:
- TypeScript
- Node.js LTS
- NestJS

Edge/Data Plane:
- Go

Optimization:
- Python where scientific computing and optimization workloads require it.

## Principles

Technology follows system boundaries, not language preference.

Runtime choices must preserve:

- reliability
- observability
- security boundaries
- AI-assisted engineering governance

## Evolution

Initial platform design should avoid unnecessary distribution complexity while keeping clear separation between control, edge, and optimization workloads.
