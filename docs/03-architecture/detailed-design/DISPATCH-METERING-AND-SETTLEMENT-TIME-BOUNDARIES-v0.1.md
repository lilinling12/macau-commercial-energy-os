# Dispatch, Metering and Settlement Time-Boundary Model v0.1

**Status:** Stack-neutral product/domain design proposal. Not an approved contract, tariff implementation, billing result, meter configuration, or solver requirement.
**Checked:** 2026-10-05.
**Authority:** Main D-055 limits initial R0 economics; U-001 keeps exact Pu demand measurement semantics open. G1 and G7.9 remain open. This design preserves those statuses.

## 1. Why one interval is not enough

A schedule timestep, source telemetry interval, utility demand measurement interval, tariff time band, billing period, tariff adjustment effective period, and equipment response horizon are different clocks. Treating them as one interval can assign energy to the wrong tariff band, miss a meter peak, overstate demand savings, or declare a schedule feasible while omitting thermal rebound or ESS terminal state.

The runtime must preserve each original clock and explicitly transform between them. It must not invent a missing meter interval, resample coarse observations into apparent high-frequency evidence, or equate a six-hour demonstration horizon with a complete billing cycle.

## 2. Macau public-rule evidence

### Verified in primary sources

- Administrative Regulation 25/2022 establishes tariff groups and defines tariff charging seasons/time bands; specific periods/times are set by Chief Executive dispatch published in the Official Gazette. It is an effective-dated tariff calendar, not a universal constant. The regulation also defines Group B demand as the greatest average active power measured periodically by the meter; groups C and D refer back to the same measured-demand concept. [Official Gazette — Regulation 25/2022, Chinese](https://bo.dsaj.gov.mo/bo/i/2022/26/regadm25_cn.asp) · [Official Gazette — Regulation 25/2022, Portuguese](https://bo.io.gov.mo/bo/i/2022/26/regadm25.asp)
- CEM's Group B/C/D pages describe Pu as the highest measured demand during a billing period and published demand charges use 0.2Pc + 0.8Pu, with group/class-specific rules. CEM's bill guide distinguishes the consumption period, contract number, meter multiplier, subscribed demand and tariff group. [CEM — Group B](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-b/) · [CEM — Group C](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-c/) · [CEM — Group D](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-d/) · [CEM — bill guide](https://www.cem-macau.com/en/customer-service/billing-service/understand-my-bill/)
- The regulation uses periodically measured average power but the public rule pages reviewed here do not establish the site's actual averaging/integration duration, meter configuration, subinterval alignment or missing-reading policy in all cases. CEM's public summary says “highest measured demand” but is not sufficient to infer the customer's exact Pu window. This remains U-001 and requires meter/bill/contract evidence or authoritative clarification.
- CEM states Tariff Clause Adjustment (TCA) is updated quarterly and publishes effective dates/values. The value must therefore be versioned by its actual effective period. [CEM — Tariff Clause Adjustment](https://www.cem-macau.com/en/customer-service/billing-service/tariff-clause-adjustment/)
- CEM documents the site's PV connection point and bidirectional metering separately from feed-in settlement. Those flows retain their own meter/effective periods; a PV register is not a substitute for the site's supply-meter billing interval. See [Macau PV grid/settlement research](MACAU-PV-GRID-SETTLEMENT-RESEARCH-v0.1.md).

### What remains unknown

For a particular site/account: Pu integration duration and alignment, meter register mapping/multiplier, demand reset/replacement rules, exact read boundaries, estimate handling, tariff selection and effective date, bill cycle, applicable season/time-band dispatch, meter-clock quality, and any customer-specific contractual departures. No public page reviewed supplies an authorized pilot's actual bill/meter configuration.

## 3. Separate temporal axes

| Axis | Semantics | Evidence needed |
|---|---|---|
| Observation interval | The interval a source value represents; distinguish instantaneous sample from interval average/energy accumulation. | Device/utility point definition, unit, quality, clock, read/receipt times, multiplier and mapping. |
| Dispatch interval | The interval over which a candidate power schedule is held or varied; kW integrated over duration produces kWh. | Product task/horizon and optimizer input policy; initially a scenario choice, not a tariff fact. |
| Forecast issue/valid interval | When a forecast was created versus the period it predicts, with uncertainty and source. | Forecast artifact/model version and issue/valid timestamps. |
| Equipment response interval | Ramp, dwell, minimum on/off, response delay, recovery/rebound, EV window and hot-water service interval. | Asset-specific capability and service evidence; unknown bounds block that flexibility claim. |
| Tariff time-band interval | Local effective season/hour mapping for active/reactive energy, including official changes. | Correct group/class and Official Gazette dispatch effective dates. |
| Pu demand averaging interval | The meter's periodic average-power window used to find the greatest measured average within the bill period. | Exact meter configuration and matched official account/bill evidence; U-001 unresolved. |
| Billing period | Exact start/end and meter-read/settlement context over which tariff components and Pu are determined. | Account bill, CEM read schedule/contract and estimate/correction status. |
| TCA effective period | Quarterly adjustment with specific effective-from/to dates. | Official CEM publication/version for that period. |
| Evidence valid/recorded time | When a mapping/rule was true in the domain versus when the platform learned/recorded it. | Source provenance and bitemporal history for correction/replay. |

Use explicit instants in UTC and the site’s named local timezone. Preserve original source timestamps and offset/clock-quality. Represent interval quantities as half-open [start, end) ranges. Do not move a sample across local tariff boundaries because its storage timestamp is UTC. Where a schedule interval crosses a TOU/season/TCA boundary, split the energy calculation by exact overlap or return an explicit unsupported state; never assign the entire interval by start-time label.

## 4. Settlement calculation boundary

### Active-energy component

For a verified account and tariff version, partition measured or scenario kWh by the tariff calendar in force for each subinterval and apply only the approved class/rule. Effective-dated TCA must follow its published change instant and the applicable contract/bill convention. Preserve raw metered quantity separately from any tariff-class loss adjustment or billed quantity.

Do not infer CEM tariff applicability from an asset, site archetype, voltage guess or public price list. CEM groups have distinct classes, eligibility conditions and calculation rules; D-055's initial R0 bill-grade scope remains authoritative and is not expanded here.

### Demand component

Demand cost is not an interval-wise linear rate. For a verified tariff context, the public B/C/D formula includes Pc and Pu; Pu is the maximum of specified meter-period average demand over the billing period, with class-specific additions/adjustments. Exact customer Pu calculation still depends on U-001.

A short candidate horizon cannot by itself determine the billing-period Pu or demand-charge change. The evaluator needs, at minimum:

1. current account and billing period, including exact boundaries;
2. the account's valid Pc for that period;
3. exact Pu integration duration, alignment, meter register and multiplier;
4. the observed maximum-to-date and its pinned evidence;
5. the candidate's contribution over the horizon, aligned to Pu windows;
6. remaining-period context if the product claims an expected full-period peak/cost rather than reporting only a bounded impact scenario;
7. the applicable tariff version, group/class, adjustments and correction/estimated-reading state.

If evidence for these is missing, the UI may show an interval peak within the candidate horizon as a **physical scenario metric**, but must not call it the bill-period Pu, demand charge, demand saving or optimized bill. It may report a conditional range or “impact not calculated” only if assumptions and method are visible and reviewed.

A prior period maximum may remain higher than every interval in today's horizon. In that case, lowering the local candidate peak does not prove the account's billed demand falls. Conversely, a candidate creates a new bill-period maximum only if its exact Pu-window average exceeds the existing/predicted period maximum. The comparison needs the same account, Pc, meter basis, window and rest-of-period policy for baseline and candidate.

### Billing-cycle completeness

Maintain two claims separately:

- **Horizon energy-cost estimate:** only the eligible energy components over the selected schedule horizon and verified tariff subintervals.
- **Full billing-period bill/demand result:** requires the entire relevant bill-period context, including actual existing peaks, exact demand measurement semantics, effective tariff/rules, other billed components and reconciliation evidence.

Never add a full fixed demand charge to each hourly interval. Never distribute the monthly demand component proportionally by kWh without an explicitly approved allocation policy. Reconcile against the same contract and bill period; compare forecast schedules against equivalent baselines.

## 5. Product and API behavior

1. Intake stores source interval semantics and raw timestamps, not just a normalized time series.
2. Readiness identifies which clocks are known, which are inferred and which are missing; missing Pu duration blocks the bill-demand claim but does not automatically block an otherwise supportable physical schedule.
3. The site model shows telemetry/forecast freshness and selected dispatch horizon separately from tariff-band and billing-period context.
4. Scenario comparison exposes both the highest candidate-horizon import (physical) and the account's observed billing-period Pu/current peak state only when supported. Labels must distinguish “horizon peak”, “observed billing-period maximum”, and “projected billing-period maximum”.
5. Cost explanation decomposes eligible active-energy, reactive-energy, demand, TCA, taxes/adjustments and PV proceeds by account and period. Unsupported components are withheld with reason codes, never silently treated as zero.
6. Shadow review pins all input/time/calendar versions. Replay uses historical clocks and effective periods, or returns incomplete/unavailable.
7. If a horizon crosses a billing-period boundary, either evaluate the portions under their independent account periods or state why a requested aggregate is unavailable. Never silently reset Pu at midnight, month-end or the forecast boundary.
8. Keep energy source/load physical balance per interval separate from billed kWh, tariff-period sums, Pu windows and bill totals.

## 6. Acceptance cases

| Case | Expected result |
|---|---|
| One-hour dispatch interval crosses an official peak/off-peak boundary | Split energy by exact overlap using the applicable effective tariff calendar; if unavailable, withhold economic calculation for the affected slice. |
| Input is hourly energy but a model displays 15-minute load | Do not invent quarter-hour peak evidence; keep hourly energy and mark Pu-demand impact unavailable. |
| CEM tariff rule says periodic average demand but customer Pu window is unknown | Physical profile/horizon peak may be shown with a scenario label; no bill-period Pu/demand charge/savings claim. |
| Current billing period already has an observed peak above every candidate-horizon interval | Keep observed Pu evidence; do not claim demand charge reduction solely from the lower candidate horizon peak. |
| Candidate has the highest exact Pu-window average this period | Mark new projected period peak only after alignment/meter evidence and same-basis baseline comparison; expose contributing intervals. |
| Schedule interval is coarser than a tariff change instant or TCA effective instant | Split by timestamp overlap only if input quantity supports it; otherwise report precision limit and do not over-allocate the tariff. |
| Forecast horizon ends before billing-period end | Do not present a full-period bill or period-maximum forecast unless remaining-period assumptions/model and uncertainty are explicit and approved. |
| Billing period crosses a tariff season or rate update | Apply effective-dated calendar/rates to the relevant portions; preserve original rule versions for replay. |
| Meter time clock has drift or a DST/offset issue | Preserve original timestamps and quality; quarantine/resolve the affected boundary rather than guessing local TOU assignment. |
| TCA changes during a billing period | Apply the verified contractual/billing treatment to each effective subperiod; if treatment is unclear, withhold the affected component. |
| Baseline and candidate use different sampling quality, horizon, meter mapping or Pu windows | Reject bill-impact comparison as non-comparable; explain the evidence mismatch. |
| ESS/HVAC schedule shifts load outside the displayed horizon | Include terminal SOC and rebound/recovery context or label schedule truncated/incomplete; do not claim feasibility/cost effect as complete. |

## 7. Verification plan and unresolved facts

- Retrieve an authorized anonymized bill and interval export for one candidate pilot account; record contract, group/class, Pc, meter identifiers, multipliers, read period, time zone/clock, registers and actual tariff calendar.
- Obtain CEM's written or contract-backed definition of the account's Pu averaging duration, alignment, meter calculation and missing-read/estimate treatment; reconcile to at least one billed Pu/demand line.
- Use the legally effective tariff text and relevant Chief Executive dispatch for TOU/season/effective dates; version them and compare to current CEM customer-facing pages.
- Verify TCA effective dates from official publication and reconcile to the exact bill.
- Construct two equal-input candidate schedules with same billing-period context but distinct peaks; demonstrate that horizon maximum, Pu maximum and tariff cost remain separate.
- Validate partial-period and full-period results against matched bill evidence under G1 Golden Bill criteria. Do not claim Macau bill-grade accuracy from synthetic cases.
- Keep the dispatch interval (e.g. hourly in the existing illustrative fixture) labeled synthetic until product/asset data evidence establishes useful operational resolution. This document does not select the MVP interval or production solver cadence.

