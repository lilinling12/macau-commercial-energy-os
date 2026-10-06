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

## Public-rule and interconnection recheck — 2026-10-07

**Status:** Dated source update for product/domain review. This updates selected public-rule evidence only; it does not change site-specific G1 blockers, authorize a product claim, or close a Gate.

### Confirmed source details

1. **The PV interconnection rule contains a capacity constraint.** The full primary text of Macao Administrative Regulation 20/2014 is now accessible in this review. It applies to PV equipment installed in public and private buildings; defines interconnection to the public grid directly or through the distribution system; and sets technical safety/installation conditions. Article 12(4) states that total installed PV capacity must not exceed 50% of the public-grid supplied capacity for the served premises, or of the upstream segment's supply capacity for the transformer serving the premises. Treat this as a project-specific engineering/regulatory screening rule: the relevant supply/transformer boundary, approved project, later technical orders and CEM/DSSCU interpretation must be confirmed for a site. Do not treat the ratio as a universal optimizer limit without those inputs. [Administrative Regulation 20/2014, Portuguese primary text](https://bo.dsaj.gov.mo/bo/i/2014/43/regadm20.asp) · [Chinese primary text](https://bo.dsaj.gov.mo/bo/i/2014/43/regadm20_cn.asp)

2. **The documented process is site- and project-specific.** CEM's current procedure asks the applicant to establish legal rights to use the installation site and adequate solar access, prepare a project through a registered technician, complete the applicable DSSCU submission/license, installation tests and acceptance, then submit interconnection materials to CEM. CEM identifies the connection point and installs the meter there; interconnection proceeds after signing a PV interconnection contract. Its note also says an anti-backflow device may be required for an independent PV system connected to a consumer network. The procedure supports an onboarding evidence checklist; it is not evidence that a particular roof, building or third-party installation is available to this product's customer. [CEM — Application Procedure](https://www.cem-macau.com/en/smart-living/photovoltaic-system-%28pv%29/application-procedure/)

3. **The feed-in arrangement is a purchase contract, not a general bill-credit rule.** CEM's published capacity tiers remain: below 10 kW, MOP 3.7/kWh; 10–100 kW, 3.4; over 100–500 kW, 3.0; over 500 kW, 2.8. DSPA describes a standardized CEM–PV-owner purchase agreement of **up to 20 years**, and says the 2018 tariff revision did not change already signed contracts. DSPA's page updated 2026-09-01 reports 39 inquiries referred for opinions by end-August 2026 and 12 PV systems connected to the grid and selling electricity. These figures confirm real deployment, but establish no candidate customer's eligibility, ownership, meter quantity, payee, rate vintage or contract terms. Do not simplify “electricity generated” into a revenue calculation until the contract and eligible meter/register definition are available. [CEM — Feed-in Tariff](https://www.cem-macau.com/en/smart-living/photovoltaic-system-%28pv%29/feed-in-tariff/) · [DSPA — PV policy, tariffs and deployment update](https://www.dspa.gov.mo/energytopics/solar/p1.html)

4. **Current public Group B charges are multiple components.** CEM's Group B page retrieved for this review shows full-load hours 09:00–20:00, low-load hours 00:00–09:00 and 20:00–24:00; billed demand is described as `0.2Pc + 0.8Pu`. The published active-energy prices are MOP 0.874/kWh full-load and 0.767/kWh low-load; demand prices are MOP 19.797/kW for B1 and 21.484/kW for B2/B3; reactive-energy prices are MOP 0.348/kvarh full-load and 0.116/kvarh low-load. CEM lists B2/B3 loss adjustments and reactive charges separately. Its tariff-adjustment table currently shows 2026 Q3 TCA of MOP 0.36/kWh, effective 2026-07-22, for groups A and B/C/D. This is a dated public-rate snapshot, not an account bill or an assertion that a given site's customer group, contract or tax treatment is known. Optimize only a disclosed component set and effective period; preserve demand, reactive energy, TCA, loss adjustments and government tax as distinct components. [CEM — Group B tariff](https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-b/) · [CEM — tariff clause adjustment](https://www-origin.cem-macau.com/zh/customer-service/billing-service/tariff-clause-adjustment/)

### Consequences for product and dispatch design

- Add site-onboarding evidence for installation-site rights, design/approval/acceptance, PV installed kW, the applicable supply/transformer capacity boundary, CEM connection point, meter/register mapping, PV interconnection contract, feed-in purchase contract, contract vintage, effective term and payee. Evidence fields remain proposed requirements, not a frozen schema.
- Keep four quantities separate where evidence permits: PV production; local same-site consumption; metered import/export at the CEM connection; and feed-in purchase quantity/payment. Do not infer one from another when the meter topology or register semantics are absent.
- Treat the public 50% rule as a feasibility/approval evidence requirement, not an automatic “export limit” or dispatch setpoint. Interconnection approval, inverter capability, curtailment authority and OS control permission remain separate.
- Keep customer import charges and PV-owner purchase proceeds separate. A public-grid interconnection and a feed-in contract do not establish that Building B may net Building A's injection against its bill, even if a site or owner group is related. Any portfolio aggregation must retain the underlying site, meter, account, counterparty and rule.
- The published feed-in prices and Group B rates are not directly interchangeable prices: they have different eligibility and settlement bases. No comparison, savings, bill-credit or investment conclusion should be shown without the actual supply tariff, applicable purchase agreement and eligible measured quantities.
- No Q4 2026 TCA is shown in the CEM table retrieved on 2026-10-07. Do not extrapolate Q3 forward; select the rate by effective time and retain “not yet published/unknown” outside the confirmed window.

### Correction to the prior source note

The v0.1 body said the Official Gazette endpoint returned an internal error and that Regulation 20/2014 had only been cross-checked indirectly. That limitation no longer applies to this recheck: the Portuguese and Chinese primary texts are now retrievable. The full rule confirms direct or distribution-mediated grid connection and contains the 50% installed-capacity constraint summarized above. This update still is not a complete legal interpretation.

### Sources checked

- Macao Official Gazette, [Administrative Regulation 20/2014 — Portuguese](https://bo.dsaj.gov.mo/bo/i/2014/43/regadm20.asp) and [Chinese](https://bo.dsaj.gov.mo/bo/i/2014/43/regadm20_cn.asp).
- CEM, [PV application procedure](https://www.cem-macau.com/en/smart-living/photovoltaic-system-%28pv%29/application-procedure/), [feed-in tariff](https://www.cem-macau.com/en/smart-living/photovoltaic-system-%28pv%29/feed-in-tariff/), [Group B tariff](https://www.cem-macau.com/zh/customer-service/billing-service/tariff-group-b/), and [tariff clause adjustment](https://www-origin.cem-macau.com/zh/customer-service/billing-service/tariff-clause-adjustment/).
- Macao Environmental Protection Bureau, [solar PV policy and deployment update](https://www.dspa.gov.mo/energytopics/solar/p1.html), page states last update 2026-09-01.

No pilot contract, bill, meter register configuration, PV inverter record, site capacity record, interconnection approval, cross-account agreement or legal opinion was reviewed. Site-specific settlement and dispatch claims remain withheld until those are supplied and verified.
