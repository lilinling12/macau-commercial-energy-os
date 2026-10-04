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


The current branch also contains an experimental discrete finite-horizon search (`src/macau_energy_optimizer/dispatch_optimizer.py`). It proposes a schedule for aggregate flexible-load energy tasks and ESS power/SOC within a short horizon, then runs the same bounded assessment. This is exact only within declared action steps and search limits; it does not implement a continuous production optimizer or close G7.9 Step 3.
