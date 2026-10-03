# G6 Safety & Control — Gate Evidence and Closure Plan

**Status:** OPEN / partially evidenced; no formal G6 closure record is present.  
**Snapshot:** 2026-10-03  
**Scope:** Safety and control authority for recommendations that may affect site equipment. G6 is independent from G6.9-R2 Technology Stack Bake-off.  
**Authority:** Research Gate framework, `docs/00-authority/ROADMAP.md`, current Decision/Open Question registers, and handoff. This file operationalizes those requirements for evidence tracking; it does not supersede source Authority or authorize control.

## Gate question

Can the system accept an optimizer proposal and prove that only an authenticated, authorized, fresh, site-scoped, policy-compliant command can pass local safety checks to a device—and that unsafe, stale, duplicated, unauthorized, or disconnected operation fails safely and remains auditable?

## Required safety properties

| ID | Required property | Existing authority | Current evidence/status | Closure evidence still required |
|---|---|---|---|---|
| G6-01 | Optimizer and AI propose only; neither can bypass policy or execution authority | D-006, D-007, D-008, D-061 | Authority principles exist; VS-001 is SHADOW-only; no runtime command/Safety Kernel package found in implementation tree | Approved data/control-flow design and negative tests proving no optimizer/LLM route reaches device I/O without the governed path |
| G6-02 | Physical/site-capacity guard and settlement-demand guard are separate; unknown Pu policy cannot weaken physical safety | D-027, D-040, D-041, D-059; U-001 | Semantic decisions exist; Pu settlement interval remains unknown; no executable Safety Kernel found | Site-specific limits and ownership defined; settlement guard remains disabled or explicitly assumption-based when demand policy is unknown; tests cover both guards and conflicts |
| G6-03 | Only a reviewed, bounded control surface is enabled; lower-level commands remain disabled absent review | D-046, D-057, D-061 | R0-A research bounds reference experiments to reviewed supervisory setpoints; not evidence of field-site approval; no command executor found | Site-specific approved point/action allowlist, units/ranges/rates, interlocks, and rejected-command evidence; explicit approval for any expansion |
| G6-04 | Activation, expiry, freshness, scope, and policy are authoritative and fail closed | D-049, D-070, D-071 | Semantic authority exists; production framework integration is pending; current VS-001 is not a command API | Versioned command contract and verifier; rejection corpus for wrong tenant/site, expired/stale, inactive, unsupported, malformed, and out-of-range inputs |
| G6-05 | Command identity/signing and Edge identity have a production key lifecycle | D-070, D-072; U-022 OPEN / G6 SECURITY | Step-3B HMAC is explicitly a test fixture, not production key authority. No production identity/key implementation found | Approved signing algorithm and canonical serialization; device identity, secure provisioning, rotation, revocation, recovery and any hardware-backed storage decisions; key-compromise response and test evidence |
| G6-06 | Retries/replay cannot cause duplicate physical writes; command, acknowledgement and observed effect remain distinct | D-073, D-075; U-024 OPEN / G6.9-R2 HARD GATE | Step-3C semantic crash-after-write evidence exists for local Node/Go shells; no Edge command implementation exists; framework-native hard-gate execution pending | Durable Edge deduplication/reconciliation implementation, persistent-state behavior, acknowledgement/effect model, failure injection, and evidence under approved runtime topology |
| G6-07 | Site operation remains safe during cloud, broker, network, or worker failure; local fallback and manual override work | G6 exit criteria in ROADMAP; D-008, D-046 | Architecture principle only; no offline command/runtime or manual override implementation found | Defined safe state per action/site, local limit enforcement, stale-command behavior, override precedence/audit and recovery/reconciliation protocol; site/hardware test evidence |
| G6-08 | Every decision, veto, attempted write, acknowledgement, override and recovery is attributable and replayable | D-073–D-075 | VS-001 evidence is in-memory and concerns shadow calculation; no control audit trail exists in implementation | Durable append-only audit/evidence model, actor/device/key/version references, redaction/retention policy and replay manifest; tamper/access controls and recovery evidence |
| G6-09 | Tenant/site isolation and least privilege hold across command proposals, keys, workflows and Edge devices | PR-01; D-008 and G6 security principles | VS-001 checks resolved context matches event, but inspected HTTP endpoint has no auth guard; no Edge identity or authorization implementation found. A technology-neutral design draft is at docs/03-architecture/detailed-design/VS-001-IDENTITY-AND-TENANT-AUTHORIZATION-DESIGN-v0.1.md | Review the design, then prove authenticated principal-to-site binding, key/device-to-site mapping, service authorization, cross-tenant negative tests and audit in the selected runtime |
| G6-10 | Changes are observable and safely operable, including health, alerting, deployment and rollback | ROADMAP WP-5/WP-7 operational evidence | Platform health endpoint returns UP unconditionally; Edge entry only logs bootstrap; no command ops runbook found | Dependency readiness, safety-state telemetry, alerts, operator procedures, rollback/recovery and tested deployment/restore evidence |

## Evidence classification

### Established semantic constraints

- Demand Guard is a hard veto (D-006); LLMs do not operate safety-critical closed loops (D-007); cloud does not directly write to low-level plant controllers (D-008).
- Settlement-demand semantics are distinct from the physical/site guard (D-041), and control cadence is not inferred from settlement cadence (D-040).
- R0-A limits reference experiments to reviewed supervisory SAT/CHWS setpoints; low-level overrides remain disabled (D-046/D-057).
- Activation is authoritative (D-049); command values use canonical decimal text (D-070); trace IDs cannot alter business/control identity (D-073).
- Edge replay protection is a recovery boundary (D-075). Step-3C evidence demonstrates semantic behavior only (D-076), not production framework or cryptographic proof.

### Current implementation evidence

The inspected `implementation/` tree contains no executable command arbitration, Safety Kernel, command signer/verifier, Edge identity/key lifecycle, physical-device adapter, offline control path, or manual override workflow. The current Platform API binds fail-closed VS-001 adapters and an in-memory evidence repository. The VS-001 controller is shadow evaluation, not an authorized command endpoint.

### Open blockers

- **U-022:** production command signing, Edge identity, provisioning, rotation, revocation and hardware-backed key storage choices remain open.
- **U-024:** durable exactly-once-effect behavior under framework-native workflow/broker failures remains an open G6.9-R2 hard gate.
- G7.2 live baseline/no-op and U-017 remain prerequisites for any R0 controller performance claims; passing G6 alone would not supply Macau performance or economic evidence.
- Site-specific physical limits, approved action points, control authority and customer/site authorization have not been supplied in this repository.

## Gate exit and change control

G6 may be marked **CLOSED** only when all safety properties applicable to the declared deployment scope have linked, reviewable evidence and an approved Gate Decision Record. The closure record must identify:

1. exact software, protocol and key-policy versions tested;
2. site/device/action scope and explicit disabled capabilities;
3. threat and hazard assumptions, failure matrix and safe-state decisions;
4. test method, environment, raw results and independent reviewer;
5. fail-closed, manual override, offline recovery, replay/idempotency and audit evidence;
6. residual risks, expiry/review date and operational owner;
7. authorization to proceed to the next deployment tier.

A design document, semantic harness, green build, or completion of G6.9-R2 does not close G6 by itself. G6.9-R2 Step 3D/4 remains a separate technology-selection dependency; G7 remains a separate simulation/site-validation dependency. Until G6 is closed for the intended deployment scope, keep the product SHADOW/advisory and keep device command execution disabled.
