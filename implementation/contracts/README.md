# Contracts

Contracts are versioned before consumers depend on them.

Initial contract set:
- `telemetry-event.v1.schema.json`
- `recommendation.v1.schema.json`
- `evidence-record.v1.schema.json`

Rules:
1. Breaking changes require a new contract version.
2. Tenant/site boundaries are explicit.
3. Timestamps are ISO 8601 date-time values.
4. Units are explicit.
5. Evidence status uses repository Authority vocabulary.
6. UNKNOWN and PROJECT_ASSUMPTION values must not silently become production facts.

Logical application operations and asynchronous state semantics across the PRD workflows are catalogued in docs/03-architecture/detailed-design/MVP-APPLICATION-AND-EVENT-CONTRACT-CATALOG-v0.1.md. That catalog is design review input only; it does not promote any V1 schema or choose an API protocol, schema format or generator.
