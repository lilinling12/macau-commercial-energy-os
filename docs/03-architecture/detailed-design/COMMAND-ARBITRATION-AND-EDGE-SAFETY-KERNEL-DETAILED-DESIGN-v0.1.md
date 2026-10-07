# Command Arbitration and Edge Safety Kernel — Detailed Design v0.1

**Status:** Stack-neutral design proposal for product-owner, site-operations and security review. G6 remains OPEN; this document is not a safety case, production approval, G6 closure record or authorization to connect/write equipment.
**Prepared:** 2026-10-04
**Scope:** Future, separately gated controlled operation from an approved recommendation through cloud authorization, site-local command arbitration, a reviewed device adapter, acknowledgement and measured effect.
**MVP boundary:** The first product remains SHADOW/advisory. No MVP device-write API, command worker, signing authority, device adapter or enabled control path is implied.
**Authority:** G6 Safety & Control; D-006/D-007/D-008, D-027/D-040/D-041, D-046/D-049/D-057/D-059/D-061/D-070/D-073/D-075/D-076; U-001/U-022/U-024; G6.9-R2 and G7 status in CURRENT.
**Related designs:** Logical Architecture Design; Security Threat Model; VS-001 Identity and Tenant Authorization; Recommendation and Operator Review; Forecasting and Optimization; Deployment, Operability and Recovery.

## 1. Decision boundary and design intent

This design separates five authorities that must never collapse into one code path:

1. **Optimizer / AI:** creates a bounded proposal with evidence and assumptions. It cannot authorize or execute.
2. **Cloud policy and human authority:** verifies product/site scope, active operating mode, authorized reviewer and any required approval. A human review event is not by itself a device command.
3. **Command issuer:** creates a uniquely identified, narrowly scoped, signed and expiring command only after all applicable cloud-side policy checks pass.
4. **Site Edge Safety Kernel:** independently authenticates the issuer, checks local configuration and current site state, arbitrates conflicts, and may veto. It is the final authority before a device adapter.
5. **Device adapter and physical plant:** perform only a reviewed point/action mapping and report protocol acknowledgement separately from observed physical effect.

Cloud and Edge checks are complementary. Passing a cloud check never bypasses local veto. The Safety Kernel does not infer missing site limits, settlement rules or operator permission. Any required input that is absent, stale, conflicting, unverifiable or outside its approved scope causes rejection or a site-defined safe fallback.

Logical boundaries may be modules or processes; this design selects no framework, deployment topology, database, broker, workflow engine, signing algorithm, device protocol, hardware key store or final product control mode. Those choices require G6.9-R2 evidence, a named site/device scope, threat/hazard review, owner approval and operational acceptance.

## 2. Operating modes

| Mode | Permitted behavior | Device writes |
|---|---|---|
| **SHADOW** | Evaluate, record and display proposals; compare with baselines; collect no control authorization. | Forbidden by architecture and configuration. |
| **ADVISORY** | Present a proposal for an authorized person to consider; record review/disposition. | Forbidden. A review disposition is not an authorization token. |
| **CONTROLLED** | Permit only the site-approved command surface after G6 evidence, exact site/customer authorization, commissioning and an explicit activation record with scope and expiry. | Only through the full arbitration path below. |
| **DEGRADED / SAFE** | Reject new commands; execute only a pre-approved local fallback for the specific action, if the site safety case defines one. | No cloud-originated writes. Fallback behavior is site/action-specific; there is no universal “turn off” or “hold last value” rule. |
| **MAINTENANCE / MANUAL OVERRIDE** | Local operator or physical interlock has the precedence defined by the site safety case; record entry, actor/source and exit. | Automated/cloud commands are inhibited or constrained as commissioned. |

Mode changes are versioned, attributable, scoped to a site and effective time, and cannot be activated by an optimizer, model output, telemetry payload or ordinary recommendation review. The default on missing or unverifiable activation state is SHADOW / command-disabled. Re-entry into CONTROLLED after a safety fault, key change, policy change or loss of local state requires the site-defined re-arm procedure; reconnect alone must not resume queued commands.

## 3. Command envelope (logical fields; not a frozen contract)

Every future command must bind, at minimum:

- immutable command ID and command schema/version;
- issuer identity/key reference and authenticated tenant, organization, site, device and point scope;
- originating recommendation ID plus immutable evidence, optimizer/model, input, tariff and policy references;
- exact action type, target point, canonical engineering unit, canonical decimal-text value and allowed parameter set;
- issue time, not-before time, expiry, maximum age, sequence/epoch and activation/mode reference;
- requested operating envelope and the relevant site configuration revision;
- required human approval record(s), role, scope and expiry where policy requires approval;
- correlation/trace metadata kept separate from semantic/control identity;
- signature/authentication envelope over a canonical serialization; the algorithm and key custody remain U-022 decisions.

Unknown fields, unsupported action versions, non-canonical values, missing provenance, mismatched scope, duplicate IDs with changed content, expired commands and unverifiable signatures are rejected. Trace IDs never make two different commands equivalent or change command identity. The exact canonical byte representation, signature algorithm and key lifecycle are not selected here.

## 4. Cloud-to-device state model

| State | Meaning and allowed transition |
|---|---|
| **PROPOSED** | Optimizer output exists; no authority to write. |
| **REVIEWED** | Human reviewed or dispositioned it. Review alone does not authorize execution. |
| **AUTHORIZED** | Policy and required human approval passed for a named scope and short validity window; approval is bound to the immutable proposal/configuration. |
| **ISSUED** | Command envelope and signature were durably recorded before transmission. |
| **RECEIVED** | Edge authenticated the command and durably journaled its ID/content digest before replying. This acknowledges custody only. |
| **VETOED / REJECTED** | A named cloud or local validation failed; reason and policy revision are recorded. Terminal for that command ID. A changed proposal is a new command. |
| **EXPIRED / CANCELLED** | Validity elapsed or a higher authority cancelled it before execution. |
| **ACCEPTED_FOR_EXECUTION** | Local authorization, mode, freshness, interlocks and safety checks passed and the adapter may be invoked. This is not proof that the device accepted or changed state. |
| **WRITE_ATTEMPTED** | Adapter invocation was durably journaled before the physical/protocol write. |
| **DEVICE_ACKNOWLEDGED** | Device/protocol acknowledged a write. This is not proof of physical effect. |
| **EFFECT_OBSERVED** | Independent or explicitly qualified telemetry confirms the expected physical state within a declared tolerance/window. It does not alone prove economic savings or causality. |
| **OUTCOME_UNKNOWN** | A crash, timeout or disconnect happened after a possible write and before reliable acknowledgement/effect reconciliation. Do not blindly retry. |
| **RECONCILED** | Authorized reconciliation linked command, device state and subsequent telemetry; record whether the action occurred, did not occur or remains indeterminate. |

Transitions are append-only evidence events. State projections are rebuildable from the journal. Terminal rejection/expiry does not mutate into success; a new authorization creates a new command lineage. An operator stop, physical interlock, manual override or Safety Kernel veto takes precedence as defined by site policy.

## 5. Site-local arbitration pipeline

The Edge Safety Kernel evaluates the following checks in order. A rejection at any stage prevents device-adapter invocation:

1. **Mode and activation:** controlled mode is explicitly active for this site/action/device and has not expired or been revoked.
2. **Issuer and signature:** authenticated cloud/workload issuer is in the site allowlist; signature, canonical bytes, key status and command integrity validate.
3. **Identity and scope:** issuer, tenant, site, device, point, adapter and command match the provisioned local registry; caller-provided IDs do not grant scope.
4. **Time and replay:** command is not-before/expiry-valid under a monitored clock policy; sequence/epoch and unique ID are valid; an exact duplicate returns its recorded status without a second write; same ID with different content is a security fault.
5. **Local readiness:** Edge, adapter, sensors, configuration, clock, durable journal and required interlocks are healthy and fresh. A missing safety input is not healthy.
6. **Action allowlist:** command names a commissioned high-level action/point, unit, range, rate, duration and operating window. Low-level writes remain disabled unless separately hazard-reviewed and approved.
7. **Physical/site guard:** enforce locally approved equipment and site constraints, including hard bounds, ramp limits, min/max run/off times, sequencing, thermal/process constraints, interlocks, capacity and operator-defined comfort/service envelopes as applicable.
8. **Settlement/economic guard (separate):** apply only when its tariff/measurement policy is verified for the command horizon. Unknown U-001 Pu interval or unsettled cost rules must never relax physical limits; an unavailable economic guard may reject an economically dependent action or leave only a separately approved physical-safe policy.
9. **Conflict arbitration:** resolve simultaneous commands using a site-approved priority/serialization policy; prevent incompatible writes to the same or coupled points; avoid oscillation and enforce rate limits.
10. **Human authority:** verify required approval, role, exact command digest, scope and freshness; changes after review invalidate approval.
11. **Durable intent:** persist the accepted decision and write intent before invoking the device adapter.
12. **Execute and reconcile:** invoke exactly the reviewed adapter operation; persist protocol outcome; compare subsequent measured state against expected effect; surface mismatch, timeout or uncertainty.

A policy/configuration update has an explicit version, effective time, approver and rollback reference. If it changes after authorization but before local execution, the command is evaluated against current policy and rejected when no longer valid. Local configuration must be authenticated and validated before activation; rollback cannot silently restore a revoked key, expired activation or weaker safety limit.

## 6. Failure, offline and recovery behavior

| Failure point | Required behavior |
|---|---|
| Cloud, broker or WAN unavailable before Edge receipt | Do not execute from a queue after expiry. Preserve cloud proposal/issue state; report delivery unknown until reconciled. |
| Edge cannot durably journal receipt/decision/write intent | Reject or withhold receipt; do not call the adapter. |
| Edge restarts before adapter invocation | Recover journal, revalidate mode, expiry, configuration and local inputs; do not execute stale work. |
| Crash/timeout after adapter may have written but before outcome is durable | Enter OUTCOME_UNKNOWN. Query device/readback or await qualified telemetry; never repeat solely because an ACK was lost. |
| Broker redelivery or exact duplicate command | Return durable prior status; at most one adapter invocation per command identity unless a reviewed device-specific reconciliation policy proves safe retry. |
| Changed command reuses an existing ID | Reject, raise security/consistency alert and retain both digests. |
| Stale/missing local sensor or safety input | Veto new command; transition to the commissioned site/action fallback and alert. Never invent a generic fallback. |
| Manual override / physical interlock | Inhibit conflicting automated action immediately according to local behavior; record source/time and require defined re-arm to resume. |
| Disk full, journal corruption, clock uncertainty or key-revocation state unavailable | Fail closed for new writes; preserve the last independently enforced physical limits; alert and require recovery/reconciliation. |
| Cloud reconnect | Reconcile status and evidence. Do not drain expired or superseded commands; do not auto-reactivate CONTROLLED mode. |

The site hazard analysis must specify the safe behavior for each actuator and fault. “Hold last value,” “turn off,” or “return to default” is not a global safe-state definition; either action can create a hazard on some plant.

## 7. Idempotency, physical effects and audit

U-024 is an open hard gate: no system may claim exactly-once physical effect from broker semantics, workflow retries or a command ID alone. The implementation must provide a durable Edge journal, command-scoped deduplication, adapter-specific idempotency where supported, and reconciliation for ambiguous outcomes. If a device/protocol cannot prove whether a write happened, expose OUTCOME_UNKNOWN and require site policy/operator reconciliation; do not retry blindly.

Record a privacy/security-reviewed append-only event for proposal lineage, review/approval, authorization, issue, receipt, local decision/veto, write intent, adapter request/response, protocol acknowledgement, measured effect, override, cancellation, restart, key/policy change and reconciliation. Each event contains actor/workload/device identity, tenant/site scope, command ID and digest, policy/configuration/key references, timestamps and reason/outcome. Do not place private keys, credentials or unrestricted raw telemetry in logs. Define retention, access control, tamper evidence, backup and export under the data-governance review; this design chooses no audit store.

## 8. Identity, keys and least privilege

U-022 remains open. Future design and implementation must separately provision and authorize human approvers, cloud workloads, site Edge agents and device/adapter identities. A cloud identity cannot impersonate an operator or local safety authority.

The selected credential design must define issuance/provisioning, device binding, storage protection, rotation overlap, revocation propagation during disconnection, expiry, compromise response, recovery/replacement, audit, and deletion/decommissioning. Production use requires a reviewed cryptographic algorithm, canonical message encoding, key separation, protected signing service, Edge verification trust roots and any hardware-backed storage decision. Step-3B fixture keys and Step-3C semantic parity are not production cryptographic proof. No credential or signing mechanism is chosen by this document.

## 9. Required evidence and acceptance plan

Before controlled operation at a declared site scope, the Gate record must link evidence for at least:

- authorized point/action allowlist, units, ranges, rates, coupled constraints and site hazard review;
- no direct optimizer/LLM-to-device path, verified by architecture and negative tests;
- wrong tenant/site/device, role, issuer, signature, policy version, activation, time, expiry, replay, duplicate and altered-command rejections;
- physical guard, separate settlement guard, unknown-demand-rule behavior, boundary/ramp/min-on/min-off/anti-cycle/interlock/conflict tests;
- manual override, physical emergency stop, cloud/broker/network/worker loss, stale/missing sensor, clock skew, disk full, key revocation while disconnected and restart recovery;
- crash injection before/after durable receipt, before/after write intent, during/after device write, after device ACK and before physical effect observation;
- persistence/recovery evidence proving duplicate deliveries do not create duplicate physical writes under U-024's required framework-native trial count/environment;
- independent operator audit linking approval to exact command content and distinguishing issue, custody, acceptance, ACK, measured effect and economics;
- restore/replay, tamper/access protection, observability, incident runbook, rollback and named operational ownership;
- G7 site baseline/no-op, commissioning and customer/site authorization before any site performance, savings or field-control claim.

Each test result must identify software/contract/policy/key/adapter versions, site/device/action scope, environment, stimulus, raw logs, expected result, actual result, reviewer and residual risk. Simulation, a static design, unit test or CI green check cannot substitute for physical/site evidence.

## 10. G6 traceability

| G6 item | Design section | Evidence still required |
|---|---|---|
| G6-01 AI/optimizer cannot bypass authority | §§1, 5, 9 | Runtime negative path tests and review |
| G6-02 physical and settlement-demand guards separate | §§5, 9 | Approved site limits; unknown Pu behavior; site fault tests |
| G6-03 bounded command surface | §§3, 5, 9 | Site-approved point/action allowlist and commissioning |
| G6-04 activation, freshness, scope and policy | §§3–5, 9 | Versioned contract, verifier and rejection corpus |
| G6-05 production signing and Edge key lifecycle | §8 | U-022 resolution and security evidence |
| G6-06 retries, duplicate write prevention and effect distinction | §§4, 6–7, 9 | U-024 hard gate under durable runtime and device adapter |
| G6-07 offline/manual behavior | §6 | Per-site/action hazard decision and field evidence |
| G6-08 audit and replay | §7, §9 | Durable evidence, access/tamper, retention and restore |
| G6-09 tenant/site isolation and least privilege | §§3, 5, 8–9 | Identity review and cross-scope runtime tests |
| G6-10 observability and safe operation | §§6–9 | SLO/ownership, alerts, deployment/rollback/restore proof |

## 11. Decisions deliberately left open

- Product mode and controlled-operation need, lead user, controllable asset and customer approval (owner review; G0/G2/G3).
- Site-specific equipment, point allowlist, local physical/comfort/process limits, safe fallback, interlocks and human/on-call responsibility (site evidence and hazard review).
- Whether settlement-demand constraints can be used for any future action while U-001 remains open (G1).
- Canonical command/event/evidence contracts, signing algorithm, cryptographic library, HSM/TPM/secure-element decisions, Edge identity, provisioning, rotation/revocation and recovery (U-022).
- Device protocol/adapter, readback quality and device-specific retry/reconciliation semantics (G3/source inventory and commissioning).
- Durable journal/evidence topology, local storage durability, backup, retention, data classification, deployment mode, SLO/RPO/RTO and incident response (product/security/operations/G6.9).
- Whether the future route ever enables automated execution or remains human-mediated (owner and customer review plus G6/G7 evidence).
- Exact G6/G7 scope, independent reviewer, evidence retention and approval record.

## 12. Review and closure rule

This design is ready for review as a boundary proposal, not for implementation or deployment. Record owner/security/site-operation responses as explicit Decision Records. Resolve each dependency before its corresponding design is baselined. G6 may close only through its approved Gate Decision Record with complete, scoped and independently reviewed evidence. Until then, all command execution remains disabled and the product stays SHADOW/advisory.

## References

- `docs/01-research/gates/G6-safety-control.md` (G6 closure criteria)
- `docs/03-architecture/ARCHITECTURE-DESIGN.md` (logical boundary)
- `docs/03-architecture/detailed-design/SECURITY-THREAT-MODEL-v0.1.md`
- `docs/03-architecture/detailed-design/VS-001-IDENTITY-AND-TENANT-AUTHORIZATION-DESIGN-v0.1.md`
- `docs/03-architecture/detailed-design/RECOMMENDATION-AND-OPERATOR-REVIEW-DETAILED-DESIGN-v0.1.md`
- `docs/03-architecture/detailed-design/FORECASTING-AND-OPTIMIZATION-DETAILED-DESIGN-v0.1.md`
- `docs/03-architecture/detailed-design/DEPLOYMENT-OPERABILITY-AND-RECOVERY-DETAILED-DESIGN-v0.1.md`
- `docs/03-architecture/command-arbitration/README.md` and `docs/03-architecture/safety-kernel/README.md`
- `docs/00-authority/decisions/` (decision and open-question registers)
