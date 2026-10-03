# Energy Graph Detailed Design v0.1

**Status:** Stack-neutral design draft; product owner, site evidence and G3 validation remain pending.  
**Scope:** Canonical site/asset/meter identity and effective-dated resolution across physical/electrical and settlement/economic views.  
**Authority:** D-013, D-014, D-020, D-024, D-038–D-040, D-065, PR-01/PR-02/PR-03 and G3.  
**Production status:** Not an approved canonical schema, graph database choice, or production implementation.

## 1. Purpose and invariants

The Energy Graph connects source telemetry and site assets to the physical/electrical context and, through explicit reviewed relationships, to settlement meters, contracts and economic evaluation. It answers “what does this point measure, at this site and time?” and “which settlement context can use that measurement?” with provenance and uncertainty.

The Energy Graph is a logical capability. It may be implemented in a relational model or another evaluated store; this document does not select a database, framework, ontology library or service boundary.

Invariants:

1. Keep **physical/electrical topology** distinct from **settlement/economic topology**; connect them only through explicit, versioned mappings (D-013).
2. Use stable tenant-scoped canonical IDs. BMS point names, meter labels, utility account numbers and vendor IDs are source identifiers, not canonical identity.
3. Every relationship is effective-dated and carries source evidence, author/reviewer and status. Preserve both valid time and system/knowledge time for correction and replay (D-024).
4. An ambiguous, missing, contradictory or out-of-scope resolution is an explicit result. Never select the “closest” asset, latest edge, or first match as a fallback.
5. Assets do not own tariff prices. Marginal value is resolved through settlement meter, contract and applicable tariff rules (D-020); the Tariff Engine evaluates commercial terms.
6. PV export/producers, grid import, consumption meters and battery flows remain distinct physical and settlement roles. The 2025 concession amendment effective 2026-01-01 contemplates private self-generated electricity distribution only within the same concession/private land parcel with prior written SAR authorization; represent any such arrangement as an explicitly approved, evidence-backed physical relation, separate from retail settlement. No cross-parcel PV credit or netting is inferred (D-021, D-077, U-025).
7. Telemetry interval/sample cadence is not a settlement demand window or an optimizer/control cadence (D-027, D-040, U-001).

## 2. Graph views and ownership

| View | Owns | Example relationships | Explicitly does not own |
|---|---|---|---|
| **Physical asset view** | Site/building/floor/zone and equipment identity; parent/part-of, serves, contains, controls, feeds | chiller plant serves chilled-water loop; meter measures feeder; AHU serves zones | Retail tariff, customer bill calculation, inferred savings |
| **Electrical topology view** | Utility point of connection, transformer/switchboard/feeder/meter topology, direction and measurement boundary | grid import meter measures point of connection; submeter measures branch; PV inverter injects at bus | Contract pricing or legal right to allocate export |
| **Settlement/economic view** | Customer supply account, settlement meter, contract reference, tariff-class/context reference, producer/export agreement reference, valid interval | CEM supply account settled by import meter under a contract reference; producer meter settled under FIT purchase reference | Asset physics, device control, tariff formula implementation |
| **Cross-view mappings** | Reviewed links from source point/device and physical/electrical measurement to canonical measurement role and settlement context | BMS point maps to chiller power; utility meter maps to site-import settlement meter | Guessing equivalence based only on matching names |

Contractual terms and tariff rules remain owned by the Tariff & Settlement capability. The graph stores references and applicability links; it does not duplicate executable pricing logic or treat a contract label as proof of a rule.

## 3. Canonical identity and relationship model

The following is a logical model, not an approved serialization contract:

- **Entity:** stable ID, tenant ID, entity type, display label, lifecycle state, source identifiers, ontology/class references, provenance, created/retired system time.
- **Relationship:** stable ID, tenant ID, typed predicate, source entity, target entity, valid-time interval, system-time interval, cardinality policy, provenance, review/evidence status, optional confidence only when confidence semantics are defined.
- **External identifier:** source system, source namespace, source key, entity ID, valid/system intervals. Enforce uniqueness within the declared namespace; do not assume IDs are globally unique across BMS vendors or meters.
- **Point mapping:** producer/device/point identity, metric, raw unit, canonical measurement meaning/unit, mapped entity/measurement boundary, mapping revision, validity, conversion reference (if approved), quality/freshness policy reference.
- **Settlement link:** canonical settlement-meter identity, customer/producer account reference, contract reference, settlement role, tariff context reference, valid/system intervals and evidence status.
- **Graph snapshot:** immutable query-result identity, query scope, effective instant/range, knowledge-time cutoff, selected entity/edge revisions, source evidence references and resolver version.

A Brick-compatible semantic layer is the project baseline (D-014). Canonical identity and stable contract IDs must not depend on any particular Brick release, namespace URI, package or database extension. Concrete ontology terms and version must be checked against the selected data sources before implementation. Preserve source/vendor classifications alongside canonical semantics instead of discarding them.

### Relationship integrity

- Tenant and site scope are required on every entity and relationship; cross-tenant edges are invalid unless a reviewed organization-level sharing contract explicitly authorizes that relation.
- Parent/contains/part-of relations must be acyclic within their defined hierarchy. Electrical paths may form loops only when the topology type explicitly allows them and the source diagram supports them.
- One point mapping cannot resolve to multiple canonical measurement meanings over overlapping valid-time intervals unless the point contract explicitly declares a multi-channel/derived mapping.
- Multiple meters may aggregate to a settlement boundary only under an explicit composition policy with units, interval alignment, direction and loss treatment. No implicit sum of child meters.
- A settlement meter may have one authoritative account/contract context for a given valid interval, unless the applicable contract explicitly supports multiple roles; overlap becomes a conflict, not a precedence guess.
- Retired entities remain addressable in historical snapshots and replay. IDs are never recycled.

## 4. Resolution request and response

### Resolution inputs

A graph resolution request includes:

- authenticated tenant/site scope derived from the caller's identity and authorization context;
- source namespace, producer/device/point identifiers, metric and unit;
- event/measurement valid time, plus a system-time cutoff for historical replay;
- optional expected measurement role or settlement purpose;
- requested resolution profile (telemetry-to-asset, meter-to-settlement, or topology traversal);
- immutable source event identity and provenance references.

A request-body tenant/site selector is only a requested scope. The resolver must compare it with authorization context; caller-supplied IDs are not authorization.

### Resolution response

Return an explicit status:

- `RESOLVED`: exactly one valid mapping, with graph snapshot ID and complete path/provenance.
- `UNMAPPED`: no eligible mapping exists.
- `AMBIGUOUS`: multiple eligible mappings or paths violate cardinality.
- `CONFLICT`: overlapping/inconsistent authoritative relationships or incompatible source facts.
- `OUT_OF_SCOPE`: requested entity belongs to another tenant/site or is not authorized for the caller.
- `INVALID_INPUT`: required source identifiers, metric, unit or time are malformed.
- `STALE`: source identity is known, but current valid relationship expired or its freshness requirement fails.

On success, return canonical measurement meaning/unit; source-to-canonical conversion reference (if any); physical asset and electrical boundary; settlement role/context only where explicitly linked; selected entity/edge IDs and revisions; evidence status; coverage/quality policy reference; and warnings. Never return a bare `assetRef`/ `meterRef`/ `contractRef` tuple without the path and temporal snapshot that justified it.

On non-success, return stable reason codes and the missing/conflicting references. Do not invoke exact tariff evaluation or optimizer ranking using an unresolved graph context.

## 5. Resolution sequence

1. Authenticate caller and derive authorized tenant/site scope before graph lookup.
2. Validate source namespace, key, measurement time, metric and unit against the ingress contract.
3. Resolve the external source identifier to a canonical point/device using the requested valid time and knowledge-time cutoff.
4. Resolve the point mapping and traverse only typed physical/electrical relations allowed by the requested profile.
5. If settlement context is requested, traverse explicit settlement-meter/account/contract references separately. Confirm the settlement boundary and measurement direction.
6. Enforce cardinality, effective-time, status, tenant isolation, unit compatibility, topology and evidence rules.
7. Construct and persist/identify an immutable graph snapshot with all selected edge versions and evidence.
8. Return a result status. Exact tariff evaluation proceeds only on `RESOLVED` and only if the Tariff Engine independently resolves rule and measurement policies.

Graph resolution establishes identity and relationships; it does not assert that every sensor is accurate, every meter is a legal settlement meter, or every contract reference authorizes a commercial allocation.

## 6. Change governance and temporal semantics

Graph updates use a proposed → reviewed → active → superseded/retired lifecycle. High-impact links—settlement meter to customer account, tariff context, PV producer/export, transformer-loss topology and control authority—require evidence and a second-person review before activation. The review policy/roles remain to be confirmed in the identity and governance design.

An update creates a new relationship revision with both:
- **valid time:** when the relation is true in the physical/commercial world;
- **system time:** when the platform recorded/accepted the relation.

Backdated corrections preserve prior revisions. Queries can reconstruct (a) what the graph currently believes was true then and (b) what the system believed at a past decision time. Snapshot replay pins one mode explicitly.

Conflicting evidence is retained and raised for review. It must not silently overwrite an active high-impact relation. For a correction, issue a new revision and link the superseded assertion and its explanation.

## 7. Integration with Tariff & Settlement and Energy OS

- Telemetry ingestion calls graph resolution only after authentication and schema validation; preserve the raw event and source identity.
- Resolved graph context supplies canonical quantities and references to settlement meter, account, contract and tariff context. The Tariff Engine independently validates effective dates, policies and rates.
- The Energy Graph does not compute demand Pu; it identifies the meter/measurement boundary and may reference a verified demand policy. The Tariff Engine consumes utility-settled Pu or a policy-backed derivation with sufficient measurements (U-001).
- Recommendations and Evidence Records pin graph snapshot ID and mapping revisions. Reprocessing after a mapping correction creates a new assessment/replay; it does not rewrite the past result.
- The optimizer receives an explicit topology/asset view and versioned constraints; it cannot infer actuator authority from physical connectivity. Control authorization is a separate G6/Safety Kernel concern.
- Site/asset displays show mapping status and provenance so an operator can correct mappings without weakening the resolver's fail-closed behavior.

## 8. Failure and security behavior

| Condition | Required behavior | Economic/control consequence |
|---|---|---|
| Unknown BMS point or vendor namespace | preserve raw event; `UNMAPPED`; request reviewed mapping | no asset attribution or economic ranking |
| Conflicting point mappings | `AMBIGUOUS` or `CONFLICT`; show candidate edges and validity | block exact calculation for affected quantity |
| Expired mapping / late event | resolve against event valid time if historical version exists; otherwise `STALE` | no current mapping substitution |
| Unauthorized cross-tenant/site reference | `OUT_OF_SCOPE`, security audit, no information leak through candidate list | deny tariff, evidence and optimizer access |
| Utility meter vs submeters disagree | surface reconciliation discrepancy and source coverage; do not pick one silently | block bill-grade total until settlement boundary is established |
| Import/export direction unknown | preserve unsigned/unknown flow semantics; do not net generation against load | block PV credit and signed economic roll-up |
| Overlapping contract/account links | `CONFLICT`; require contract evidence and reviewer resolution | no exact settlement |
| Topology edge changes during the evaluated range | split graph resolution at effective-time boundary and pin each snapshot | calculate only if the tariff path supports the same split |
| Graph store unavailable | use a previously pinned, authorized immutable snapshot only for deterministic replay; otherwise fail closed | no new current recommendation/settlement |
| Replay references a missing/superseded edge revision | report incomplete replay; do not use latest edge | no replay-valid claim |

API/job authorization, scoped persistence/cache, audit and revocation must be enforced at every access path, not just the UI. Sensitive customer identifiers are not written to ordinary logs. Detailed authentication provider/roles and retention/encryption policy remain open pending owner/product/deployment review.

## 9. Acceptance evidence

Before PR-03 can be marked implementation-ready:

1. Validate representative Macau site drawings and meter/contract documents for the selected pilot candidate, including utility import, submeters, transformer boundary, BMS point inventory and any PV/ESS meter.
2. Approve canonical entity/predicate catalog and source namespaces; verify the Brick-compatible semantic mapping and exact ontology version against actual source systems.
3. Prove effective-time and knowledge-time queries, corrections, graph snapshots and historical replay.
4. Demonstrate deterministic resolution of unique, missing, ambiguous, conflicting, stale and cross-tenant cases; measure query latency at an agreed scale/SLO.
5. Reconcile utility settlement meter against submeters/topology; document losses, missing meters and aggregation limitations.
6. Verify that unmapped or low-quality data cannot produce exact cost, savings attribution or executable recommendation.
7. Review graph-administration workflow, reviewer roles, audit, export, backup/restore and tenant isolation.
8. Link every graph relationship used by bill reconstruction to evidence and the Tariff Engine's resolved context; retain real/synthetic test evidence separately.

No site has been validated by this draft. G3 remains open until its research gate evidence and decision record satisfy the project's exit criteria.

## 10. Unresolved design and research inputs

- Actual first pilot site and site topology documents (D-010 remains a hypothesis to validate).
- Canonical building ontology release and point-mapping policy under D-014.
- Source ID stability, meter register direction, multiplier, clock quality and sampling behavior by integration.
- Settlement meter hierarchy, transformer loss treatment and meter/submeter reconciliation by tariff class (U-005/U-016).
- PV owner/host/customer relationship and any approved cross-account allocation (U-025).
- Tenant/admin/partner roles, delegated site access and approval workflow.
- Graph snapshot storage, indexing, scale, retention and SLO after deployment discovery.
- Contract/tariff resolvers remain owned by the Tariff & Settlement Engine; exact tariffs remain subject to G1.

## References

- Project decisions: `docs/00-authority/decisions/DECISIONS.md` (D-013, D-014, D-020, D-024, D-038–D-040).
- G3 gate and unresolved questions: `docs/00-authority/decisions/OPEN-QUESTIONS.md`, relevant G2/G3 research gate records.
- Tariff calculation interface: `docs/03-architecture/detailed-design/TARIFF-SETTLEMENT-DETAILED-DESIGN-v0.1.md`.
- Existing VS-001 graph port and fixture adapters: `implementation/platform-api/src/vs001/ports.ts`, `adapters.ts`, `replay.ts`.
