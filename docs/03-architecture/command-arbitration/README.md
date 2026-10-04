# Command Arbitration

## Purpose

Define how optimization recommendations become executable actions.

## Flow

Optimizer

↓

Policy Evaluation

↓

Safety Boundary

↓

Execution Layer

## Principles

- Optimizer proposes; execution authority is controlled.
- Safety constraints can reject commands.
- AI components cannot bypass operational safeguards.

See `../detailed-design/COMMAND-ARBITRATION-AND-EDGE-SAFETY-KERNEL-DETAILED-DESIGN-v0.1.md` for the review-only command envelope, lifecycle, arbitration and recovery proposal. It does not select a production stack or authorize device writes.
