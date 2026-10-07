# Energy Operations UX Reference

Use this when designing site, portfolio, economics, dispatch, recommendation, or evidence screens. It is a product-specific guide, not a claim that every behavior is already approved.

## Model the energy decision

Represent the site's supply/use picture at the level supported by evidence:

- Sources: grid import; on-site PV generation and self-consumption; storage discharge; verified other generation.
- Destinations/flexibility: building load, HVAC/chillers, EV charging, hot water, storage charging, and verified export/curtailment where applicable.
- State explicitly when a source, meter mapping, export agreement, availability window, equipment capability, or tariff rule is unknown. Never invent an energy flow to make a Sankey or balance graphic look complete.
- Keep physical power balance and settlement/economic interpretation distinct. A source-flow visualization is not itself a bill calculation.

A useful decision view answers, in order:

1. What is happening now, and for which site and interval?
2. Which sources are supplying the load, and what evidence supports that reading?
3. What can be shifted, stored, curtailed, or left unchanged within approved constraints?
4. What is the expected effect, with baseline, uncertainty, tariff assumptions, and excluded effects visible?
5. What needs review, who can act, and what will happen after that action?

## Evidence and uncertainty

Use explicit labels alongside visual encoding, for example `Measured`, `Forecast`, `Estimate`, `Scenario`, `Synthetic`, `Stale`, `Incomplete`, `Unverified`. Put freshness and interval near the affected figure. Show a confidence/uncertainty range only when its semantics are documented. Keep actual and forecast visually distinct using more than hue (e.g. solid vs dashed line plus direct labels).

When data is stale or mapping is unresolved, preserve context but block or qualify downstream cost/savings conclusions. Provide a direct path to the evidence, data-health finding, contract/tariff record, or replay that explains the status.

## Recommendations and control boundaries

For a recommendation, show the proposed change, site and time window, current/reference state, constraints, expected effect, assumptions, confidence/evidence, and review state. Distinguish `reviewed`, `approved`, `executed`, and `measured outcome`; never conflate them. In Shadow-only scope, do not show a misleading execute control or imply a physical command endpoint exists.

## Useful screen patterns (not templates)

Choose patterns to fit the task rather than forcing a familiar dashboard layout:

- **Portfolio scan:** exceptions, site comparison and freshness before aggregate headline metrics.
- **Site energy view:** source-to-load relationship, current interval and constraints; let users move from a flow to its meter/evidence.
- **Economics:** tariff period and cost components aligned to the same time window; separate verified settlement from scenario-only components.
- **Dispatch planning:** compare baseline and candidate source/load schedules across time, expose constraints and trade-offs, and preserve a readable tabular alternative to complex charts.
- **Evidence/replay:** reconstruct inputs, rule/version, decision, recommendation and observed outcome with timestamps and provenance.

These are task affordances, not fixed page layouts. Prefer a focused canvas or contextual detail view when a persistent sidebar, card grid, or chart is not the clearest representation.

## Multi-locale content

Design for English, Traditional Chinese and Portuguese if/when confirmed for the release. Allow wrapping and reflow rather than clipping; avoid hard-coded widths based on English. Localize units, time zones, date/currency formatting, pluralization and status terminology. Preserve IDs, raw values, and audit records independent of presentation locale.

