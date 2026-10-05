# Macau tariff evidence to SHADOW code crosswalk — 2026-10-06

**Status:** implementation-gap review for the G7.9 Step 3 proposal; recommendations only.  
**Compared revisions:** dispatch evidence note on PR #10 commit `7c04125243e54e16219c529d89c5cbb403395ae0`; optimizer PR #14 head `5d6392d3157335d21f3c0f3104f1f3bda250479b`.  
**Decision boundary:** does not approve a billing contract, change an ADR, close G7.9 Step 3, or enable control.

## Evidence reviewed

- Official tariff/PV evidence captured in [Macau commercial electricity tariff and PV settlement evidence](../../01-research/macau-commercial-electricity-tariff-and-pv-settlement-evidence-2026-10-06.md).
- PR #14's `dispatch_assessment.py`, `dispatch_optimizer.py`, `test_dispatch_assessment.py`, and `SHADOW-ASSESSMENT-PROTOTYPE.md`, fetched from its exact branch at the revisions listed below.
- PR #14 is Draft/open. The prototype is bounded SHADOW code, not the main implementation and not a bill-grade tariff engine.

## What the code actually calculates

PR #14 can calculate an evidenced **grid-import energy component** by multiplying aligned interval import kW × interval duration × caller-supplied MOP/kWh rate. Its assessment requires evidence references for account/meter mapping, contract and tariff, and rate evidence; partial rate coverage is reported as partial and uncovered intervals are not treated as zero. The code explicitly says demand, tax, export credit and full-bill settlement are excluded.

The dispatch result separately exposes a schedule-window peak and explicitly labels that the horizon peak is **not** billing-period Pu. PV export is represented as a physical schedule flow, but this review found no PV feed-in amount in the current economic component. A new `macau_tariff_periods.py` adapter now classifies the official B1 busy/off-peak periods and C1 seasonal/multi-window periods in fixed Macau UTC+08:00 time, adds caller-supplied TCA, preserves the evidence reference, and maps them to the existing optimizer's interval-rate input. It rejects unsupported subclasses (B2/B3/C2), invalid effective windows, naive or nonpositive intervals, and intervals that cross a tariff boundary. It does not derive or authenticate a customer's tariff from a bill/contract; a synthetic `VERIFIED` marker is still only a caller assertion. The code is intentionally an active-energy rate mapper, not a billing-period or full-bill calculator.

Source files:

- [PR #14 assessment implementation](https://github.com/lilinling12/macau-commercial-energy-os/blob/poc/shadow-dispatch-assessment/implementation/optimizer/src/macau_energy_optimizer/dispatch_assessment.py) (blob `4986bb546d675c469646881ab151dfd847725790`)
- [PR #14 schedule-search implementation](https://github.com/lilinling12/macau-commercial-energy-os/blob/poc/shadow-dispatch-assessment/implementation/optimizer/src/macau_energy_optimizer/dispatch_optimizer.py) (blob `2d3256801f0ddce6b849c648c160f5a32fd90a27`)
- [PR #14 prototype scope and exclusions](https://github.com/lilinling12/macau-commercial-energy-os/blob/poc/shadow-dispatch-assessment/implementation/optimizer/SHADOW-ASSESSMENT-PROTOTYPE.md) (blob `731dc465a5d23ef94d40b124a6e07c9ef7dbfe45`)
- [PR #14 assessment tests](https://github.com/lilinling12/macau-commercial-energy-os/blob/poc/shadow-dispatch-assessment/implementation/optimizer/tests/test_dispatch_assessment.py) (blob `29aae2565692da75703efb5977634a90ae6c4d04`)

## Crosswalk: public Macau facts versus implemented behavior

| Concern | Public-source fact | PR #14 behavior | Gap/status |
|---|---|---|---|
| Energy-flow schedule | Grid import, local PV, storage and flexible load are represented as synthetic interval values | Performs bounded schedule checks/search; cannot establish a real site topology | Scenario/site evidence remains caller-supplied; no connected pilot meter |
| Retail import energy | CEM tariff periods and rates vary by group/subclass; TCA is quarterly | Prices aligned intervals with supplied rates; evidence gate is a reference/state check | Can support a bounded input-rate component, but tariff classification, bill ingestion, effective-dated rate derivation and independent evidence authentication are absent |
| Group C seasonal tariff | Executive Dispatch 105/2022 splits C into low season (Oct–May) and high season (Jun–Sep), with high-season full-load windows 10:30–13:00 and 14:30–16:00, busy periods 09:30–10:30, 13:00–14:30 and 16:00–20:30, and a low-load period 20:30–09:30; Group C applies to qualifying large MV customers under Regulation 25/2022 | C1 period classification and supplied-rate mapping are now implemented; C2 loss correction, applicability verification, billing demand, reactive items and settlement remain unimplemented | Partial: C1 can supply an interval active-energy objective when its rate card is explicitly provided; the result remains `GRID_IMPORT_ENERGY_ONLY` |\n| Group B time-of-use | Full-load/busy 09:00–20:00; low-load 00:00–09:00 and 20:00–24:00 | B1 period classification and supplied-rate mapping are implemented with strict boundary splitting | Partial: rate selection is covered, but B2/B3 loss adjustments, customer applicability and full settlement are not |
| Demand charge | Group B uses 0.2Pc + 0.8Pu; Pu is highest measured demand in billing period; Pc has contract/update rules | Reports schedule-horizon import peak only and correctly withholds billing-period interpretation | No Pu/Pc history, tariff billing period, peak window integration, or demand-charge replay |
| Reactive energy/losses | B includes reactive-energy treatment and B2/B3 loss adjustments | Not part of current economic component | Withhold full-bill comparison until meter and class-specific line items are modeled |
| Quarterly TCA/tax | TCA changes quarterly; bill also includes applicable tax | Tax/full bill excluded; rate is supplied as input | Need effective dates, bill-period proration/settlement rules and bill-line reconciliation |
| PV export remuneration | Qualified, interconnected systems may have FIT contracts and CEM metering | Export is a physical flow only; no export credit calculated | Correctly excluded today. Add only after contract, meter, approval, FIT band and effective dates are qualified |
| Cross-building credit | Public sources reviewed do not prove another building's PV offsets this site's bill | No cross-site credit calculation | Keep separate meter/settlement accounts unless explicit legal/utility/contract evidence exists |
| Claim semantics | General rules do not prove any particular customer's applicability | Assessment gates bounded claims; assumes caller-provided evidence status | Production trust, authenticated provenance, immutable input snapshot and independent bill replay remain open |

## Implemented tariff-period slice and verification

At PR #14 head `5d6392d3157335d21f3c0f3104f1f3bda250479b`, the new [B1/C1 tariff period mapper](https://github.com/lilinling12/macau-commercial-energy-os/blob/poc/shadow-dispatch-assessment/implementation/optimizer/src/macau_energy_optimizer/macau_tariff_periods.py) (blob `f3f2e7db37ad7b502788335b282596d7dca5aa41`) and [focused tests](https://github.com/lilinling12/macau-commercial-energy-os/blob/poc/shadow-dispatch-assessment/implementation/optimizer/tests/test_macau_tariff_periods.py) (blob `fb6a9364a96e1763bfe8ebebd537f06a1ada3a07`) cover B1 busy/off-peak, C1 seasonal and all high-season boundaries, TCA addition, effective-window checking, boundary-crossing rejection, and evidence-reference preservation. Ten focused tests passed locally under Python 3.11.9; the package declares Python 3.14, so the exact supported-runtime CI remains the required confirmation. PR #14's Runtime Bootstrap, Authority Validation and Repository Hygiene runs for that head were queued at the time of this audit.

This slice fixes period selection only. Rate-card construction/application is still caller-supplied and not authenticated. The calculation still does not derive bill-period demand, tariff subclass/transformer adjustments, reactive energy, tax, PV FIT, or full-bill settlement. Its outputs remain the existing bounded import-energy component. The source code's fixed UTC+08:00 Macau offset supports the contemporary tariff dates under review; the UI/optimizer must keep effective dates and tariff evidence explicit.

## Required next implementation boundary

Preserve the present output name and disclaimer **GRID_IMPORT_ENERGY_ONLY** for the existing component. Do not rename it “bill savings,” “electricity cost savings,” or “economic dispatch savings.” The next bounded implementation should be a tariff-evidence adapter and replay contract that can say exactly which component is available and why, without changing the production-stack decision.

Recommended contract concepts (names illustrative, not approved wire vocabulary):

- tariff group/subclass and effective-dated tariff version;
- account/installation/meter mapping, meter multiplier, register direction, units, interval source and quality;
- subscribed-demand history Pc and evidence for when it changes;
- billing-period start/end and the measured demand series required to derive Pu;
- local timezone and tariff-period definition/version for each interval;
- base active/reactive rate schedule and effective-dated quarterly TCA;
- tax and explicit treatment of non-energy bill lines;
- PV installation/connection approval, installed-capacity band, bidirectional meter channels, signed purchase contract, applicable FIT/effective dates and settlement scope;
- source document/reference, custodian, observed/valid time, verification method, and immutable evidence-manifest identity.

Do not fold physical PV export into import energy cost as a negative rate. Evaluate an approved PV purchase agreement as a separate settlement component, independently reconciled with meter registers and the bill.

## Acceptance examples before bill-grade comparison

1. **Incomplete contract or tariff evidence:** assessment may show physical schedule only; no monetary amount is displayed.
2. **Group C season and multi-window periods:** test October/May vs June/September, all six high-season boundary times, the two full-load windows, busy windows and night window against the effective legal tariff version; a Group C customer must never be priced with Group B hours.\n3. **Group B interval boundary:** intervals starting/ending at 09:00, 20:00, 00:00 and midnight map to the correct full-/low-load period in Macau local time; daylight/time-zone conversion does not create duplicate or missing intervals.
4. **Historical TCA change:** a billing horizon crossing an effective-date boundary applies the correct dated value to the right intervals and records the source.
5. **Demand charge:** recompute baseline and candidate Pu over the *entire applicable billing period*, then apply the evidenced Pc/Pu rule; a shorter dispatch horizon's peak must never be substituted.
6. **Demand history:** missing, stale or contradictory Pc/Pu evidence withholds demand-charge delta and full-bill claim while preserving any separately qualified import-energy component.
7. **Reactive energy and tariff subclass:** B1/B2/B3 treatment cannot be interchanged; missing kvarh/register mapping withholds the affected bill component.
8. **PV without export agreement:** retain physical PV export only as a scenario or withhold its field feasibility; do not add revenue.
9. **Qualified PV export:** only a matching installation, approval, meter register and signed effective agreement permits a separately named FIT settlement line; unmatched interval/register coverage is partial.
10. **Other building PV:** a different meter/account cannot reduce this site's settlement absent explicit approved allocation/contract evidence.
11. **Historical bill reconciliation:** independently recompute line items from source bills and meter data, compare each line and total within agreed rounding/tolerance, and preserve the replay inputs and source versions.
12. **Partial coverage:** only exactly covered, supported components appear; missing intervals are never priced at zero.
13. **SHADOW-only:** review/acceptance states never invoke device control or imply execution.

## Source and validation limits

This review establishes a mismatch boundary and a sequence of work, not correctness of a future bill engine. The published CEM pages are general customer information. Exact legal/tariff revision, tariff applicability, billing interval and integration method, PV agreement terms, and local meter semantics must be validated with the target customer's current signed records and the responsible Macau parties. No actual customer bill, meter stream, contract, site topology, or field-device evidence was available for this review.

G7.9 Step 3 remains **OPEN**. The production architecture, canonical API/schema, tariff contract, and production implementation remain subject to their controlling authority and owner review.
