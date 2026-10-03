# Edge Runtime

Site data-plane boundary.

Initial responsibilities:
- protocol adapters;
- point normalization;
- local buffering;
- retry / reconnect;
- secure telemetry transport;
- local health and audit signals.

Runtime direction: Go.

The edge does not own tariff truth or optimization policy. Safety-critical execution requires the governed command path and a later explicit gate.
