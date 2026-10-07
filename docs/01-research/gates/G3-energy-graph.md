# G3 Energy Digital Twin / Energy Graph

**Status:** OPEN — logical design exists; no Macau pilot-site topology or settlement mapping has been validated.
**Purpose:** Establish a traceable, time-aware model that connects source points and site assets to physical/electrical topology and, through explicit evidence-backed links, to settlement and economic context.
**Authority:** Original G0–G7 research framework; D-013, D-014, D-020, D-024, D-038–D-040, D-065, D-077; U-005, U-016, U-025; Energy Graph Detailed Design v0.1.
**Boundary:** This Gate establishes evidence and domain semantics. It does not select a database, ontology package/version, production runtime, graph service boundary, or authorize device control.

## Research questions

1. Which canonical entities are needed to represent the selected site's organization/tenant, site, building/zone, equipment, meter, source device/point, electrical boundary, supply account, contract reference, PV producer/export and storage flows?
2. How do source-system identifiers map to stable canonical identity over time? What happens when vendor identifiers are reused, changed, duplicated or unavailable?
3. Which physical and electrical relationships are established by drawings, meter registers, BMS inventories, commissioning records or operator knowledge? Which paths, directions, meter multipliers, losses, aggregation rules or boundaries remain uncertain?
4. How are measured quantities linked to the utility settlement meter, customer account, contract and tariff context without conflating physical topology with commercial settlement?
5. What valid-time and knowledge-time history, provenance, review status and correction trail are needed to reproduce what was known when an assessment was made?
6. How should missing, ambiguous, contradictory, stale, unauthorized or out-of-scope mappings be represented so downstream tariff evaluation and recommendations fail closed?
7. Which PV, ESS, import/export and cross-site relationships are evidenced by physical and contractual records? Do not infer cross-parcel allocation or bill credit from grid interconnection or feed-in purchase alone (U-025).
8. Which site roles may propose, review, approve or administer high-impact graph mappings, and what evidence and audit are required? Keep the provider and role model open pending product and deployment decisions.

## Evidence rules

- Classify inputs as public/aggregate context, site-provided documentary evidence, site-measured/commissioned evidence, operator explanation, engineering simulation, or project assumption. These classes are not interchangeable.
- Prefer authorized site drawings, single-line diagrams, meter schedules/registers, bills/contracts, BMS point lists, equipment schedules, commissioning records and reconciled telemetry. Record source, owner, date/version, scope, validity, access permission and limitations.
- A matching label or naming convention is a candidate mapping, not proof of identity, topology or settlement authority.
- Preserve disagreement between drawings, meter registers, contracts and live observations. Mark the affected relation unresolved until evidence and review resolve it.
- Keep physical/electrical flow separate from contractual allocation and tariff calculation. A graph edge is not, by itself, a legal settlement right.
- Keep public/synthetic/reference-simulator evidence distinct from Macau site evidence. No site topology or customer settlement mapping is claimed validated by the current logical design draft.

## Required outputs

1. A versioned inventory for the selected evidence scope: entities, source namespaces/identifiers, measurements, units, direction, sampling/time quality, owner and access/authorization status.
2. A physical/electrical topology record with source references, validity interval, system/knowledge-time history, uncertainty and explicit unresolved boundaries.
3. A separate settlement/economic mapping inventory linking import/export measurement boundaries to supply/producer account and contract references only where documentary evidence supports the link; tariff rules remain owned by G1/Tariff & Settlement.
4. A mapping/resolution status vocabulary and cardinality/conflict policy for resolved, unmapped, ambiguous, conflicting, stale and out-of-scope cases.
5. A correction/review procedure for high-impact links, preserving previous assertions and identifying who supplied and reviewed the evidence.
6. An explicit scope disposition for each candidate relationship: evidenced/in-scope, excluded, or unresolved/deferred, with downstream consequences.
7. A replay-oriented graph snapshot requirement that identifies the effective instant/range, knowledge-time cutoff, selected relationship revisions and evidence references.

## Exit criteria

G3 may close only when a reviewed evidence packet demonstrates:

- a selected, site-authorized representative site scope and traceable evidence for its relevant assets, source points and meter boundaries;
- stable canonical identity and source-identifier mapping rules, including duplicate/change/reuse cases;
- physical/electrical relationships reconciled against available source records and measurement direction/boundaries, with unresolved areas explicitly bounded;
- settlement-meter/account/contract links supported by applicable documentary evidence and separated from physical topology and tariff computation;
- effective-time and knowledge-time correction semantics sufficient to explain and reproduce a past mapping decision;
- deterministic resolution and fail-closed treatment for missing, ambiguous, contradictory, stale and unauthorized cases;
- explicit PV/import/export and cross-site treatment consistent with G1 and U-025, with no inferred netting or customer bill credit;
- evidence register and relevant U-items updated, and a Gate decision recording what is validated, what is excluded, residual unknowns and approver.

Passing G3 research does not by itself prove a production implementation, bill-grade calculation, tenant-isolation control, or runtime performance. Implementation acceptance and security proof are separate delivery evidence.

## Dependencies and status

- **G1:** settlement meter, account, contract and tariff semantics; unresolved tariff rules remain with G1 and must not be guessed in the graph.
- **G2:** site asset capability, physical inventory and authorized measurement scope.
- **G6:** identity, authorization and operational safety boundaries for any future administrative or control workflow.
- **G6.9-R2:** technology selection is independent; G3 domain semantics must remain stack-neutral until the bake-off selects production technology.
- **G7:** reference simulation can exercise graph scenarios, but cannot substitute for Macau site records or settlement evidence.

Public Macau aggregate data and the current Energy Graph detailed-design draft provide context and proposed semantics only. No pilot site's canonical graph, meter hierarchy, point mapping, or settlement topology has been validated. Existing VS-001 graph adapters fail closed or return synthetic fixtures; they are not a production resolver.

## Related records

- Evidence register: `docs/01-research/evidence/EVIDENCE-REGISTER.md`
- Open questions: `docs/00-authority/decisions/OPEN-QUESTIONS.md`
- Product baseline: `docs/02-product/PRODUCT-DESIGN.md`
- Stack-neutral design: `docs/03-architecture/detailed-design/ENERGY-GRAPH-DETAILED-DESIGN-v0.1.md`
- Cross-Gate implementation traceability: `docs/03-architecture/detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md`
- G3 site evidence acquisition packet (prepared, not sent; site selection, authorization and secure intake remain required): `docs/01-research/gates/G3-SITE-EVIDENCE-ACQUISITION-PACKET-v0.1.md`
