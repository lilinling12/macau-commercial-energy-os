# G1 Settlement and G7.2 R0 Evidence Readout v0.1

**Checked:** 2026-10-04  
**Status:** Source-based evidence reconciliation; not bill-grade validation, Gate closure, customer validation, or tariff advice.  
**Primary source:** supplied `macau-commercial-energy-os-research-authority-v1.6.2.zip`, snapshot 2026-10-03, especially `handoff/CURRENT.md`, `OPEN-QUESTIONS.md`, `tariff/TARIFF-AUTHORITY.md`, `reference-building/G7.2-R0-HARNESS-PREFLIGHT.md`, `reference-building/G7.3-SITEPOWER-ECONOMIC-REPLAY.md`, and `reference-building/G7.4-TARIFF-AWARE-SUPERVISORY-CONTROLLER.md`.  
**Cross-check:** [`G7.1-7.5-RESEARCH-READOUT-v0.1.md`](G7.1-7.5-RESEARCH-READOUT-v0.1.md), [`G7.6-7.9-DELIVERY-TRACE-v0.1.md`](G7.6-7.9-DELIVERY-TRACE-v0.1.md), and [`RESEARCH-TIMELINE-AND-AUTHORITY-v0.1.md`](RESEARCH-TIMELINE-AND-AUTHORITY-v0.1.md).

## Finding

The tariff and dispatch design has a meaningful, executable specification, but the evidence does **not** establish a production-ready Macau bill engine or a validated Macau building controller. The defensible near-term product is an evidence-labelled source/load assessment and schedule comparison with unresolved settlement components surfaced, followed by SHADOW recommendations. It must not claim bill-grade savings, PV export revenue, ESS grid export, or a physical control capability without site, meter, contract, and operating evidence.

## Gate status versus evidence

| Area | Source says / evidence found | What this permits us to claim |
|---|---|---|
| G1.1 and G1.2 | `handoff/CURRENT.md` lists both sub-gates complete. Earlier authority specifies a tariff rule engine, effective dating, immutable tariff versions, deterministic evaluation and separation of electrical topology from settlement topology. | The tariff domain and implementation architecture have been designed. This does not close G1 or verify bill reconstruction. |
| G1 overall | v1.6.2 `CURRENT.md`: **OPEN**. It names U-001/U-009/U-010/U-011 as blockers. | Macau commercial tariffs cannot be called bill-grade or production verified on this evidence. |
| G7.2 R0 | Static preflight complete; live BOPTEST runs not executed in the stated environment. Two live baselines and one full-trajectory no-op identity run remain required. | Point bindings and no-op semantics have source-fixture support; the controller/economic trajectory has not been run. |
| G7.3 | Design complete and offline reference implemented; live R0 trajectory pending. Initial replay deliberately limits bill-grade scope to C1 active-energy TOU plus effective-dated TCA. | A bounded replay design exists; this is not full bill reconstruction or customer ROI. |
| G7.4 | Controller design complete and offline policy tests pass; live closed-loop execution pending. U-017 response sign, magnitude, comfort impact and rebound remain unknown. | TariffShaper is a falsifiable research controller, not a proven Macau operating policy. |

## Settlement unknowns and product consequences

| ID | Status in v1.6.2 | Required evidence | Product / architecture rule until resolved |
|---|---|---|---|
| U-001: Pu averaging/integration interval | Unknown; G1 blocker | Actual B/C/D load-profile and bill, CEM meter configuration, or authoritative technical documentation | Never assume 15 minutes. Do not compute bill-grade demand charges or present demand savings as settled value. |
| U-002: PV settlement topology | Contract-specific | PV purchase agreement, meter diagram, CEM interconnection/settlement evidence | Keep physical PV generation/self-consumption distinct from invoice credit/export. Do not assume “PV first”, gross FIT, netting, or surplus export. |
| U-003: third-party CEM AMI access | Unknown | CEM technical/commercial confirmation | First pilot must remain viable on customer-authorized local meters/BMS; do not make CEM API access a prerequisite or capability claim. |
| U-004: ESS grid export | Unknown | Project-specific CEM and interconnection approval plus settlement terms | Default `ESS_EXPORT=false`. Model charge/discharge behind the meter only when metering and site evidence support it. |
| U-005: transformer compensation | Partially verified | Real C1/C2/B2/B3 invoices, contract and meter topology | Carry uncertainty at the site/tariff rule level; avoid asserting a generic loss compensation result. |
| U-009: B/C/D government tax formula | Unknown; G1 blocker | Applicable legislation/CEM billing evidence and exceptions | Do not label the total invoice/tax reconstruction complete. Keep unresolved tax outside a “bill-grade total”. |
| U-010: Golden Bills | Not acquired; G1 blocker | At least one real B/C bill paired with interval/load-profile evidence and a second tariff-class case | Required tariff-engine acceptance: reconstruction error ≤0.5%, with zero unexplained balancing adjustment. No source evidence currently demonstrates that acceptance. |
| U-011: rounding / Odd Amount carry-forward | Open; Golden Bill validation required | Real B/C/D bills plus authoritative billing explanation/contract evidence | Rounding must be an explicit settlement policy. Do not round every interval by default or tune a hidden balancing item to force a match. |
| U-017: supervisory response/rebound | Open; live G7.2/G7.4 required | R0-00/R0-01 identity gates followed by R0-02 response sweep, with site-like power and comfort metrics | Do not assume raising SAT/CHWS lowers total power. Treat comfort, capacity, response sign and rebound as measured outcomes, not optimizer priors. |

Other important calibration gaps: U-006 BMS quality, U-007 Macau HVAC flexibility, U-008 comfort/humidity SLA, U-012 Macau reference-building calibration, U-014 lack of zone humidity measurements in R0, U-015 weather validation beyond TMYx, and U-016 real absolute non-HVAC site-load composition. These prevent describing the synthetic office harness as representative Macau hotel evidence.

## What the R0 experiment does and does not prove

The pinned harness is IBPSA BOPTEST v0.9.0 `multizone_office_complex_air`. The preflight cites official API regression fixtures and an official no-op override fixture; it identifies 182 inputs, 204 measurements, 134 forecast points and 15 zone temperatures. It also correctly distinguishes those static fixture checks from live test runs.

R0's initial economic replay intentionally enables only:

```text
C1 active-energy TOU + effective-dated TCA
```

It leaves Pu/demand, Pc state transitions, reactive energy, government tax, PV settlement, ESS settlement/export and EV tariff disabled. The design separates **paired incremental dispatch value** (same exogenous non-HVAC profile) from **absolute synthetic site cost**. The linear cancellation argument applies only to the bounded active-energy/TCA case and only absent import/export regime change; it must not be generalized to demand charges, PV/ESS settlement, nonlinear taxes or differing schedules.

The preflight explicitly records live R0-00 baseline run #1/#2 and R0-01 full-trajectory identity as **not executed**. Offline policy tests do not establish live site power response, comfort impact, tariff correctness, Macau representativeness, savings, or control safety.

## Implications for source/load dispatch MVP

1. Make physical flow and settlement views separate but linked. Show grid import, PV production/use/export, ESS charge/discharge, and flexible load only when the corresponding meter, asset and permission evidence exists. Separately show which of those flows affect the customer's bill and under what versioned contract rule.
2. Give every scenario a settlement coverage label: `verified`, `assumption`, `excluded`, or `unresolved`, with the evidence source and effective period. An unresolved component must lower the confidence and prevent a bill-grade savings claim.
3. Keep deterministic constraint and safety outcomes explicit. Demand Guard may veto independently of the optimizer; comfort, equipment, meter quality, export permission and contract rights are not silently converted into soft economic penalties.
4. Run an advisory/SHADOW schedule review: proposed source/load trajectory, baseline comparison, tariff coverage, constraints, uncertainty, evidence and replay. The interface must not imply device writes are enabled.
5. Permit bounded research calculations such as C1 active-energy/TCA replay only when the scenario clearly states that scope. Never present synthetic non-HVAC composition or office model results as a Macau hotel bill or ROI.

## Verification path and evidence required to advance

| Work item | Gate evidence required | Result unlocked |
|---|---|---|
| G1 closeout | Resolve U-001, U-009, U-010 and U-011 with authoritative source + real Golden Bill fixtures; meet the stated ≤0.5% / zero-unexplained-adjustment criterion across the required cases. | Bill-grade tariff evaluation only for the explicitly covered tariff classes, components and effective periods. |
| G7.2 live R0 | Reproduce pinned harness metadata hashes/counts in the live environment; execute two baselines, full-trajectory no-op identity, persist outputs/hashes and confirm trajectory tolerance. | Reproducible harness evidence for the reference model, not Macau validation. |
| G7.4 R0-02 onward | Execute setpoint response/aggressiveness, guarded, uncertainty and rebound cases; retain power, comfort and trace evidence. | Falsifiable controller behavior for the pinned office model, not an automatic hotel policy. |
| Site pilot readiness | Acquire site-specific bills, meter topology, PV/ESS rights, BMS history/quality, comfort and humidity rules, and measured load/asset capability; agree M&V baseline and responsibilities. | Site-bounded schedule economics and shadow comparison. Field control remains a separate safety/approval gate. |

## Research-source limitations

This readout directly extracts the named files from the supplied v1.6.2 archive and cross-checks the existing G7.1–G7.5 readout. It does not independently re-verify current CEM tariff values against live official sources; any archived prices are historical snapshots. It does not claim to have read every file in all archives or the full original ChatGPT shared conversation. The exact current branch and PR are verified separately in the current GitHub audit.

