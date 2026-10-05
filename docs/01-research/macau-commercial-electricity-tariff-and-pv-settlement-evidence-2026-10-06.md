# Macau commercial electricity tariff and PV settlement evidence — 2026-10-06

**Purpose:** turn current official Macau utility/government evidence into product and model requirements for source/load economic dispatch.  
**Status:** dated research input; not legal advice, not a customer-specific tariff determination, and not an approved architecture or tariff engine.  
**Repository context:** proposed on PR #10 `product/source-load-economic-dispatch`; draft PR, no merge.

## Findings supported by official sources

### 1. Macau has an official PV grid-interconnection and feed-in tariff path

The Macau Environmental Protection Bureau's current solar-energy guidance describes a government-set feed-in tariff, states that CEM purchases PV electricity when the system satisfies the applicable technical conditions, and lists capacity bands and current rates: below 10 kW — MOP 3.7/kWh; 10–100 kW — MOP 3.4/kWh; over 100–500 kW — MOP 3.0/kWh; over 500 kW — MOP 2.8/kWh. The page also describes a purchase term of up to 20 years and identifies separate government/CEM roles. At its latest information section it reports 39 installation cases consulted by DSSCU or the Public Works Bureau through August 2026, 12 of which had connected and sold electricity. [DSPA solar-energy guidance](https://www.dspa.gov.mo/energytopics/solar/c1.html)

CEM describes the interconnection process: confirm the right to use the installation site and available solar resource; have the works designed by a registered technician; obtain required approval/acceptance; submit technical descriptions, responsibility declarations and test records; agree the connection point; install the CEM meter; and sign the PV interconnection contract. CEM also says a non-grid-connected PV system that is connected to a consumer's electrical network may require an anti-backflow device. [CEM PV application procedure](https://www.cem-macau.com/en/smart-living/photovoltaic-system-%28pv%29/application-procedure/)

CEM's feed-in tariff page repeats the four current capacity bands and says the scheme took effect on 1 July 2018. [CEM feed-in tariff](https://www.cem-macau.com/en/smart-living/photovoltaic-system-%28pv%29/feed-in-tariff/)

**Product consequence:** the earlier blanket statement that Macau has no established PV export mechanism would be incorrect. A government/CEM export-purchase path exists. That does **not** prove a given building has roof rights, an approved/interconnected system, a current purchase contract, a particular meter arrangement, or the right to aggregate energy across buildings. The dispatch model must represent physical PV generation, site import/export metering, and PV purchase-contract settlement as separate evidence-qualified facts. Never infer that generation on another building's roof offsets this site's bill.

### 2. Commercial tariffs include demand and time-of-use components

CEM says Tariff Group B applies to qualifying medium- or low-voltage customers with subscribed demand of at least 69 kVA and monthly consumption of at least 10,000 kWh. Its demand charge uses **0.2 × subscribed demand Pc + 0.8 × highest measured demand Pu** in the billing period. For B2/B3, the published rules also include transformer/network loss adjustments and reactive-energy treatment. Full-load hours are 09:00–20:00; low-load hours are 00:00–09:00 and 20:00–24:00. The displayed base prices are MOP 19.797/kW (B1) or 21.484/kW (B2/B3) for demand; MOP 0.874/kWh full-load and 0.767/kWh low-load; reactive charges are also listed. [CEM Tariff Group B](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-b/)

CEM says Tariff Group D applies to high-voltage supply. It uses the same 0.2Pc + 0.8Pu demand formula, has full-load hours 08:00–23:00 and low-load hours 23:00–08:00, and publishes separate active/reactive energy charges. [CEM Tariff Group D](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-d/)

CEM describes the Tariff Clause Adjustment (TCA) as a quarterly adjustment reflecting energy production cost. Its current published table shows MOP 0.36/kWh for Groups B/C/D for 2026 Q3, effective 22 July 2026. [CEM TCA history](https://www.cem-macau.com/en/customer-service/billing-service/tariff-clause-adjustment/)

CEM's bill guide explains that bills expose contract number, subscribed demand, tariff group, consumption period, meter multiplier, demand, consumption, TCA and tax. [CEM bill guide](https://www.cem-macau.com/en/customer-service/billing-service/understand-my-bill/)

**Date and application limit:** rates and tariff pages were reviewed on 2026-10-06. The pages cite Administrative Regulation 25/2022 and Executive Decree 105/2022 for tariff definitions/base prices; the TCA changes quarterly. The public page is not a substitute for a customer's current bill, contract, meter setup, applicable decrees, or confirmation of billing measurement intervals and exceptions. The optimizer must not hard-code these values as timeless defaults.

## Model and product requirements

1. **Separate physics from settlement.** The interval energy balance represents grid import, on-site PV generation/consumption/export, ESS charge/discharge/losses, and building/flexible load. A separate settlement evaluator maps the *qualified* site's meter channels and contract to bill items. PV feed-in remuneration is a separate contract line; it is not automatically a negative retail import price or a universal net-metering credit.
2. **Capture the actual tariff identity.** Store tariff group/subclass, supply voltage, account/installation and meter identity, subscribed demand Pc with effective dates, meter multiplier, billing-period boundaries, import/export registers, active/reactive measurements and their tariff periods, current base-price schedule, TCA value/effective window, taxes, and evidence source/version. Missing or conflicting critical fields block bill-grade cost comparison.
3. **Represent demand-charge impact across the full billing horizon.** A one-interval import reduction is not itself a demand-charge saving. The baseline and candidate must replay the applicable billing-period maximum Pu and subscribed-demand Pc rules; whether a candidate changes billed Pc requires the actual rule and effective contract evidence. Report interval peak and billing-period peak separately.
4. **Use tariff-specific intervals and units.** Preserve local site time and daylight/clock rules for full/low-load periods, UTC instants for interval identity, kW/kWh/kvar/kvarh units, meter multiplier, and missing/estimated meter values. Obtain the actual meter sampling and billing integration method before claiming a bill reproduction.
5. **Keep PV export claims contract-gated.** For an export candidate require the site/system capacity and applicable band, approved installation/interconnection evidence, CEM meter/register mapping, signed purchase/interconnection agreement and effective dates, and measured or forecast generation evidence. If these are absent, show physical scenario flow only or withhold export revenue/feasibility claims.
6. **Do not assume cross-building wheeling.** A portfolio may contain multiple sites and PV assets, but each physical connection and settlement scope remains separate until legal, utility, metering and contract evidence explicitly establish aggregation or allocation rights.
7. **MVP posture remains SHADOW.** These sources justify building a tariff/PV evidence intake and a deterministic bill-replay comparison for qualified cases. They do not authorize device control or establish customer savings. Asset controllability, HVAC comfort/safety constraints, ESS SOC and inverter capabilities still require site-specific evidence.

## Suggested first-pilot evidence packet

For one candidate commercial site, request (with customer authorization): recent full bills covering the relevant seasonal period; supply contract and tariff amendments; meter/account list and meter multipliers; interval import/export active-energy and demand data with timestamps and units; reactive-energy registers if billed; current TCA/bill period; single-line electrical diagram; PV installation/interconnection approvals and signed CEM agreement if PV exists; inverter and protection settings; ESS nameplate/BMS and warranty/operating limits if present; HVAC/EV/hot-water asset inventory and operator-approved service constraints; and the provenance/owner/effective dates for every imported record.

The first reconciliation deliverable should reproduce the site's historical bill line items from its own evidence before a candidate-vs-baseline cost claim is enabled. Keep unobserved export, self-consumption allocation, remote-building supply, device flexibility and savings explicitly unknown.

## Open validation questions

- Verify current legal text and tariff-decree revisions, exact PV contract term and transition rules with the responsible Macau authorities/CEM and the pilot customer's signed documents.
- Verify the meter interval length and demand-window integration rules for each selected tariff/customer.
- Verify how import and export registers appear in the exact bidirectional meter/bill and whether settlement is simultaneous, interval-based, or separately metered for the specific contract.
- Confirm whether the prospective customer has rights to use the PV installation site and whether any proposed multi-building operation has a lawful contractual and metering basis.
- Independently validate bill replay against multiple real anonymized bills before presenting savings or payback.

## Evidence classification

| Claim | Status | Evidence scope |
|---|---|---|
| Macau publishes PV grid interconnection and feed-in tariff rules | Verified from official DSPA/CEM public pages | General policy/process, not a specific site |
| CEM purchases qualifying interconnected PV electricity | Verified as a general official statement | Qualification, actual contract, meter and rate remain site-specific |
| PV electricity from another building offsets this building's bill | Unknown; no reviewed evidence establishes this | Requires legal, utility, metering and contract basis |
| Group B has demand, full/low-load, reactive and quarterly TCA components | Verified from current CEM page | Exact customer's group/subclass and bill data remain unverified |
| Current 2026 Q3 TCA is MOP 0.36/kWh for B/C/D | Verified from CEM published table | Effective period shown there; refresh each quarter |
| Candidate savings, control capability, or export income at a pilot site | Unknown until evidence and bill replay | No pilot-site records were reviewed here |
