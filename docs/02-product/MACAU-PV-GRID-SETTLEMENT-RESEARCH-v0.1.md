# Macau PV Grid Injection and Settlement Evidence v0.1

**Status:** Source-based research note for product/domain review. It is not legal advice, a customer contract interpretation, an owner decision, or proof of any pilot site's eligibility.
**Checked:** 2026-10-05.
**Product implication:** Model grid-connected PV as a physical site resource and grid injection at its own connection boundary. Model compensation as a separate, evidence-bound settlement relationship. Do not treat another building's PV as electricity directly routed to, or automatically credited against, this site's meter.

## 1. Findings

### Verified in current official sources

1. **Grid connection is an established path for eligible PV installations.** CEM describes public low-voltage and medium-voltage grid connection, direct or through electrical distribution systems. It says bidirectional meters are installed at the connection point and CEM buys PV electricity under a feed-in tariff. The cited government rule covers PV installations on public and private buildings. [CEM — PV introduction](https://www.cem-macau.com/en/smart-living/photovoltaic-system-%28pv%29/pv-introduction/) · [Administrative Regulation 20/2014](https://bo.dsaj.gov.mo/bo/i/2014/43/regadm20.asp)

2. **Interconnection is a project-specific approval and contract process.** CEM's process calls for rights to use the installation site, technical design by a registered professional, project/license steps, commissioning tests, DSSCU acceptance, application to CEM, a meter at the connection point, and a PV interconnection contract before interconnection. The published procedure also flags that a non-grid-connected PV system connected to a consumer's electrical network may need anti-backflow protection. [CEM — application procedure](https://www.cem-macau.com/en/smart-living/photovoltaic-system-%28pv%29/application-procedure/)

3. **The published feed-in schedule is capacity-tiered.** CEM currently publishes four installed-capacity tiers with displayed rates of MOP 3.7/kWh (below 10 kW), 3.4/kWh (10–100 kW), 3.0/kWh (over 100–500 kW), and 2.8/kWh (over 500 kW). The government environmental page says the purchase period is 20 years and that tariffs in already signed contracts were not affected by the 2018 revision. These are public schedule facts, not a substitute for a specific installation's signed agreement, start date, eligible metered quantity, payee or current applicability. [CEM — feed-in tariff](https://www.cem-macau.com/zh/smart-living/photovoltaic-system-%28pv%29/feed-in-tariff/) · [DSPA — solar PV policy and tariff history](https://www.dspa.gov.mo/energytopics/solar/p1.html)

4. **CEM's public description says that the feed-in arrangement pays for generated PV electricity.** The connection meter records electricity exported to CEM's network. This supports a distinct export-energy and purchase-settlement concept alongside a site's imported energy. It does not make the export amount an on-bill credit by default.

### Not established by these sources

- A right to net one building's PV export against a different building's electricity consumption or bill.
- A “virtual power plant,” community solar, wheeling, peer-to-peer sale, cross-account allocation or time-matched retail supply arrangement.
- That every system in the public capacity tier schedule has identical contract terms or that a given project has an executed purchase agreement.
- A customer's own load can be served by identifiable electrons generated at another site through the public grid.
- Site-level self-consumption, curtailment, export capacity, feeder constraints, dispatch rights, settlement timing or a specific PV system's measured profile.

The distinction is important: CEM's sources verify that PV can be connected to and inject energy into the public network and that a feed-in purchase mechanism exists. **The conclusion that this does not itself prove cross-building bill netting is an evidence-bound inference from the published scope and process.** A legal or commercial arrangement beyond those pages would need to be produced and reviewed before the product represents it.

## 2. Physical and economic model

### Physical layer (per site and connection boundary)

- Represent PV generation at the site where the array, inverter, electrical connection and generation measurements are evidenced.
- Represent local behind-the-meter consumption/self-consumption only where the meter/topology evidence supports it.
- At the CEM interconnection point, represent measured import and export as distinct signed/typed interval flows. Do not infer export by subtracting unrelated meters or by assuming all PV surplus is exported.
- Represent grid supply as a network source for each connected site. Do not draw a physical link from Building A's PV to Building B's load merely because both connect to the Macau grid.
- Keep multiple sites as separate physical boundaries unless an evidenced private electrical network or other permitted topology exists.

### Economic layer (per applicable meter/account/agreement)

- Keep the site's electricity supply tariff/account and PV purchase agreement as separate effective-dated relationships.
- Attribute PV export compensation only from the eligible export meter/quantity, applicable feed-in class/rate, contract period, payee and settlement statement/evidence.
- Do not subtract PV export from another meter's import, tariff demand, account bill or portfolio cost unless a reviewed rule/agreement explicitly permits that treatment.
- Preserve both gross import charges and PV export purchase proceeds as separate components; show any net portfolio view only as an aggregation of independently evidenced results.
- If contract applicability, tariff class, meter mapping, agreement term or payee is unknown, keep the physical flow if adequately measured but mark the corresponding monetary claim withheld. Unknown is not zero.

## 3. Product and dispatch consequences

1. **Site workspace:** show local PV, grid import/export and load schedule on one site timeline only when they share a supported site boundary. Label every series as measured, forecast, estimated, scenario or synthetic.
2. **Portfolio workspace:** allow site-by-site comparison and carefully labeled aggregation of eligible costs/proceeds. Do not present a portfolio sum as a common physical schedule or cross-site energy transfer.
3. **Scenario comparison:** permit a portfolio planning scenario only if the user has authority and the system identifies it as coordinated planning; each site's physical constraints remain separate and any cross-account economic effect remains blocked until contractual rules are evidenced.
4. **Evidence states:** show interconnection approval, connection contract, bidirectional meter mapping, generation/export measurements, feed-in agreement, installed-capacity tier, effective period and payee as separately inspectable evidence.
5. **SHADOW boundary:** a suggested PV/ESS/load schedule is advisory. Interconnection permission to export is not proof that the OS may command an inverter, storage system or building control.
6. **MVP exclusions:** do not claim cross-site PV allocation, bill credit, cost savings, dispatch feasibility, export capability or curtailment authority from public policy pages or synthetic fixtures.

## 4. Acceptance examples

| Evidence/input | Physical result allowed | Economic result allowed |
|---|---|---|
| PV generation and same-site load mapped; no export meter/contract evidence | Show generation; show only supported local flow. Mark boundary/export unknown. | No export revenue or net-bill claim. |
| Approved interconnection, export meter and eligible PV purchase contract mapped to Site A's payee/account | Show Site A import/export at the connection boundary. | Calculate a separate Site A feed-in component only from applicable contract terms and meter evidence. |
| Site A has PV export; Site B has load; only both sites' CEM grid connections are known | Keep both site boundaries separate; no A→B physical dispatch link. | No B bill offset or cross-account savings claim. |
| A signed, reviewed agreement explicitly defines a permitted cross-account allocation and the relevant meters/time rules are available | Show physical flows independently; annotate the contractual allocation as a separate ledger relation. | Calculate only the contract-defined allocation, period and counterparty; retain gross site results. |
| Published tier/rate known, but installation capacity class, contract date, payee or eligible meter data is missing | Keep the measured PV/injection profile if available. | Rate is not automatically applied; monetary result stays blocked/partial with missing evidence. |
| CEM interconnection is approved but no control authorization/capability evidence exists | Include PV in an advisory scenario only if its behavior is appropriately bounded. | No controllability or command claim. |

## 5. Sources and limits

- CEM, “Photovoltaic System (PV)” — public LV/MV interconnection, bidirectional meter, feed-in purchase and published system count/capacity. Accessed 2026-10-05.
- CEM, “Application Procedure” — site rights, technical/approval/testing sequence, CEM meter and signed interconnection contract; note on anti-backflow for consumer-network PV not connected to public grid. Accessed 2026-10-05.
- CEM, “Feed-in Tariff” — displayed capacity tiers and rates. The page states the feed-in system took effect 2018-07-01. Accessed 2026-10-05.
- Macao Environmental Protection Bureau (DSPA), solar PV policy page — 20-year purchase period, tariff revision history, treatment of already signed contracts, and regulatory/utility responsibilities. Accessed 2026-10-05.
- Administrative Regulation No. 20/2014 — technical safety conditions and direct/through-distribution connection of PV systems to the public electricity network. The official gazette endpoint returned an internal error in this web session; its title/scope was cross-checked against CEM and DSPA pages. Do not treat this note as a complete legal interpretation.

No site contracts, PV interconnection agreements, bills, interval meter data or legal advice were reviewed. Obtain and assess those materials before asserting any specific customer's eligibility, export settlement, portfolio netting or dispatch rights.
