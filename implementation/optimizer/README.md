# Optimizer

Forecasting, simulation, and optimization boundary.

Initial product mode: SHADOW.

Proposed responsibilities:
- consume normalized site state and forecast inputs;
- evaluate economic schedules;
- generate recommendations;
- expose feasibility and evidence references.

## Candidate implementation status

Python is the provisional intelligence-role proposal in the project-layer architecture, not an approved production runtime decision. Step 3D/4 and owner architecture review remain open.

The current Python module contains a recommendation data model and mode boundary; it does not implement a validated forecasting or optimization engine and has no Macau site-performance evidence. It does not directly execute device commands and cannot override the Safety Kernel.

See `docs/03-architecture/technology-authority/G6.9-technology-selection/README.md`.
