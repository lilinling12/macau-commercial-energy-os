# Tariff Engine Architecture

## Purpose

Tariff Engine is the economic truth layer of Energy OS.

## Principles

- Immutable tariff definitions
- Versioned tariff rules
- Effective-date aware resolution
- Traceable settlement calculation

## Boundary

Assets do not directly own prices.

Resolution flow:

Meter -> Contract -> Tariff Version -> Price Resolution

This keeps physical topology separated from settlement topology.
