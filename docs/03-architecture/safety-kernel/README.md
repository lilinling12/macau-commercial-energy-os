# Safety Kernel Architecture

## Purpose

Safety Kernel protects operational boundaries between optimization and execution.

## Principles

Optimizer recommendations must pass safety validation.

Safety Kernel may reject or veto unsafe actions.

See `../detailed-design/COMMAND-ARBITRATION-AND-EDGE-SAFETY-KERNEL-DETAILED-DESIGN-v0.1.md` for the review-only lifecycle, local checks, offline behavior and required G6 evidence. It does not authorize implementation or device control.

LLM or AI reasoning components must not directly bypass safety-critical control boundaries.
