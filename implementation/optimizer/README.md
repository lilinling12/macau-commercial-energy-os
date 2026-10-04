# Optimizer

Forecasting, simulation, and optimization boundary.

Initial product mode: SHADOW.

Responsibilities:
- consume normalized site state and forecast inputs;
- evaluate economic schedules;
- generate recommendations;
- expose feasibility and evidence references.

Runtime direction: Python.

The optimizer does not directly execute device commands and cannot override the Safety Kernel.


## Source/load SHADOW assessment prototype

A bounded supplied-schedule assessment experiment is documented in [`SHADOW-ASSESSMENT-PROTOTYPE.md`](SHADOW-ASSESSMENT-PROTOTYPE.md). It validates interval alignment, power balance, supplied flexible-load and ESS envelopes, and an optional candidate import guard. It does not optimize, verify the referenced evidence, prove Macau site conditions, reconstruct a full bill, or control equipment. This remains a review proposal and does not close G7.9 Step 3 or select production architecture.
