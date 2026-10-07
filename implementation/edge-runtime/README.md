# Edge Runtime

Site data-plane boundary.

## Proposed responsibilities

- protocol adapters;
- point normalization;
- local buffering;
- retry / reconnect;
- secure telemetry transport;
- local health and audit signals.

## Candidate implementation status

Go is the provisional Edge-role proposal in the project-layer architecture, not an approved production runtime decision. Step 3D/4 and owner architecture review remain open.

The current `cmd/edge/main.go` entrypoint only logs bootstrap status. A telemetry event struct exists, but this tree does not yet provide protocol adapters, ingestion transport, durable capture/recovery, secure telemetry transport, or a Safety Kernel. These capabilities and Gate evidence must not be inferred from the module boundary or language.

The edge does not own tariff truth or optimization policy. Safety-critical execution requires the governed command path and a later explicit gate. See `docs/03-architecture/technology-authority/G6.9-technology-selection/README.md`.
