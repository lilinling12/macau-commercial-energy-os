# MVP Module Boundaries

## Control plane — platform-api

Owns:
- tenant / organization / site metadata;
- Energy Graph metadata;
- tariff-contract references;
- telemetry metadata registration;
- recommendation lifecycle;
- audit and evidence references.

Does not own:
- field-bus protocol implementation;
- optimization algorithms;
- safety-critical device execution.

## Edge data plane — edge-runtime

Owns:
- protocol adapters;
- point normalization;
- buffering / retry;
- local transport security;
- site-to-cloud telemetry delivery.

Does not own:
- tariff truth;
- enterprise workflows;
- optimizer business decisions.

## Intelligence — optimizer

Owns:
- forecast inputs;
- simulation;
- optimization shadow mode;
- recommendation generation;
- feasibility outputs.

Does not own:
- settlement source of truth;
- direct safety-critical execution;
- regulatory assumptions.

## Reference validation — simulator

Owns:
- reference-building harnesses;
- replay;
- regression fixtures;
- synthetic scenarios;
- evidence-producing validation runs.

Synthetic fixtures remain PROJECT_ASSUMPTION unless replaced by verified site evidence.

## Cross-module boundary — contracts

All cross-runtime payloads must be versioned here before implementation depends on them.
