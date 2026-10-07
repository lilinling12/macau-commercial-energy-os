# Site, Meter, Account and Settlement Boundary Model v0.1

**Status:** Stack-neutral domain proposal for product/domain/architecture review. It is not an approved database schema, legal opinion, customer tariff determination, or production contract.
**Checked:** 2026-10-05.
**Authority preserved:** Main D-013 separates physical and economic topology; D-005 requires verified PV settlement; D-055 restricts initial bill-grade claims; D-077/U-025 keep cross-site PV settlement rights unresolved. G7.9 Step 2 lists Site but omits it from the relationship sketch and core table list. This proposal fills the conceptual gap for review; it does not change main authority or close G7.9.

## 1. Problem this model prevents

“Site”, “building”, “meter”, “CEM contract/account”, and “PV interconnection” describe different boundaries. Treating any two as synonyms can create a physically impossible schedule, apply the wrong tariff, combine separate demand peaks, assign export proceeds to the wrong party, or leak one utility customer’s data to another application tenant.

The product therefore needs two linked but distinct models:

- **Physical model:** where generation, loads, storage and grid exchange occur, and which measurement points observe those flows.
- **Economic/settlement model:** which customer/installation, supply contract, tariff, bill period, PV purchase agreement, meter/register and payee govern charges or proceeds.

The link between these models is an evidenced, effective-dated mapping—not an implicit join on a shared site name or building address.

## 2. Direct evidence from Macau utility sources

CEM's bill guide distinguishes contract holder, installation address, contract number, consumption period, meter multiplier, subscribed demand and tariff group. Group B/C/D billing information describes tariff-specific demand, active/reactive energy, tariff periods and billing-period measured demand. CEM documents Groups B and C as applying to defined voltage, subscribed-demand and consumption conditions; Group D applies to high-voltage supply. For B/C/D, published demand charge uses the formula 0.2Pc + 0.8Pu, with class-specific loss treatment. The official tariff-clause page publishes quarterly effective adjustments, including 2026 periods. These facts mean tariff applicability and billing calculation are attached to the exact installation/contract/metering context and effective period; an hourly dispatch interval alone is insufficient to calculate the bill.

CEM's PV sources describe a separate application/interconnection process, bidirectional meter at the connection point, signed PV interconnection contract and feed-in purchase. The PV agreement/payee and eligible export register must therefore not be silently merged into the electricity supply account.

Sources accessed 2026-10-05:

- [CEM — Understand My Bill](https://www.cem-macau.com/en/customer-service/billing-service/understand-my-bill/)
- [CEM — Tariff Group B](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-b/)
- [CEM — Tariff Group C](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-c/)
- [CEM — Tariff Group D](https://www.cem-macau.com/en/customer-service/billing-service/tariff-group-d/)
- [CEM — Tariff Clause Adjustment](https://www.cem-macau.com/en/customer-service/billing-service/tariff-clause-adjustment/)
- [CEM — PV interconnection application](https://www.cem-macau.com/en/smart-living/photovoltaic-system-%28pv%29/application-procedure/)
- [CEM — PV feed-in tariff](https://www.cem-macau.com/zh/smart-living/photovoltaic-system-%28pv%29/feed-in-tariff/)
- [Macau PV grid/settlement research note](MACAU-PV-GRID-SETTLEMENT-RESEARCH-v0.1.md)

These public sources do not identify any pilot customer's tariff, billing interval, contract, account relationships, export settlement, or multi-site allocation rights.

## 3. Proposed conceptual objects

Names are concepts for domain review, not table/schema commitments.

| Concept | Meaning | Must not be conflated with |
|---|---|---|
| Application Tenant | Security/ownership boundary inside this product; authorizes users and scopes records. | CEM customer, legal entity, utility account or physical site |
| Organization / Legal Party | Portfolio owner, operator, tenant, landlord, supplier or other party with a documented role. | Application tenant by default |
| Site | Operational planning context, location and site timezone; may group buildings and physical boundaries for a workflow. | One utility contract or one electrical island |
| Building | Physical structure/facility grouping. | Metering or settlement boundary |
| Electrical Boundary / Connection Point | Physical interface, bus or point where a grid/feed/source/load connection is represented. | Legal account or entire site |
| Meter / Register | Instrument identity plus directional/quantity register, multiplier, unit, clock, effective mapping and evidence. | A generic telemetry point; a bill line by itself |
| Energy Asset / Load | PV, ESS, HVAC/chiller, EV charger, hot-water load or other evidenced resource with capability version. | Controllable device or unconstrained flexibility |
| Supply Installation / Account | Utility contract/installation context, contract holder, contract number, tariff class, subscribed demand and effective billing period. | Product tenant or site name |
| Tariff Profile / Rule Version | Effective-dated applicable tariff/rule set and source/version for one supply context. | A current public tariff page without account applicability |
| PV Interconnection Agreement | Approved grid connection terms, connection point, capacity class, effective dates and technical constraints. | Electricity supply contract |
| PV Purchase / Feed-in Agreement | Purchase terms, eligible export measurement, rate/term and payee/counterparty. | An automatic credit against any other building's bill |
| Settlement Statement / Bill Snapshot | Immutable bill period, meter readings/registers, multipliers, tariff version and components used for reconciliation. | A modeled dispatch cost or forecast |
| Evidence Reference | Source document/data sample, issuer, collection time, valid period, hash/version, quality and authorization. | An unqualified status badge |

## 4. Relationship and cardinality rules to validate

The exact cardinalities must be confirmed from the customer's asset and bill evidence. The design must support these independently rather than hard-code “one site = one bill”:

1. A product tenant can be authorized for multiple organizations/sites; an organization may operate sites without being the legal electricity-account holder.
2. A site can contain multiple buildings and multiple electrical/settlement boundaries. The site object is a workspace and planning context, not proof of one shared electrical network.
3. A building can contain multiple meters or account installations; one account/install location may also cover several physically mapped assets. Represent the actual metering diagram and contract scope.
4. Each meter/register mapping to physical quantity and each meter-to-account/tariff association has an evidence reference and valid-time interval. Conflicting or overlapping active mappings block affected calculations.
5. A PV plant is physically attached to an evidenced electrical boundary. An interconnection point and PV export register are separate from the supply import register even if CEM uses one bidirectional-meter assembly.
6. A PV purchase agreement identifies the eligible installation/connection, applicable output measure, valid dates and payee. It does not grant a credit to another account unless a separate reviewed rule/agreement explicitly provides it.
7. A tariff profile is applied to the exact supply context and billing period. Public tariff eligibility conditions are inputs/checks, not permission to infer a customer's tariff group from building type or estimated load.
8. Aggregation across meters/accounts is an explicit portfolio calculation. Preserve component results and gross import/export; do not collapse separate demand charges into a synthetic site peak unless the contract rules say those meters share one billing boundary.
9. Application authorization follows trusted tenant/organization/site entitlements, while utility contract identity follows evidenced legal and supply records. Similar names or shared ownership do not establish access rights.
10. A change of owner, tenant, account, meter, tariff or agreement is effective-dated. Historical assessment and replay use the mapping/rules that applied then; they do not inherit the current mapping.

## 5. Schedule-to-settlement evaluation path

For each selected site and horizon:

1. Resolve the physical boundary, topology version, interval clock, meters/registers and evidence needed for the physical profile.
2. Establish a common time grid for forecast/schedule comparison while retaining each source's original sampling/aggregation and quality.
3. Calculate grid import/export, PV generation/use, ESS charge/discharge/SOC and loads only from supported physical mappings. Preserve directional registers and avoid double counting.
4. Resolve the schedule's impact on each relevant supply-installation/account. Do not aggregate across accounts before their independent tariff calculation.
5. Select the effective tariff profile, billing period, time-of-use calendar, TCA, subscribed demand and tariff-specific demand rule. Resolve Pu measurement window from authoritative meter/bill evidence; do not substitute 15-minute or optimizer intervals.
6. Resolve the PV purchase agreement separately. Calculate feed-in proceeds only from eligible export quantity, contract rule, effective period and payee.
7. Return physical readiness and economic eligibility separately. If a physical profile is supported but account/tariff evidence is missing, retain the permitted physical result and withhold monetary total/ranking/savings for the affected account.
8. Reconcile any modeled bill to an anonymized, authorized bill snapshot before enabling bill-grade claims. Maintain gross account components and explain residuals.
9. Portfolio reporting may sum independently eligible costs/proceeds under an explicit user scope; it must not imply energy transfer or netting among sites.

Proposed result-state labels (not wire enums): PHYSICAL_READY / PHYSICAL_PARTIAL / PHYSICAL_BLOCKED and independent ECONOMIC_ELIGIBLE / ECONOMIC_PARTIAL / ECONOMIC_BLOCKED / NOT_CALCULATED. Exact vocabulary and transitions remain subject to D-055/G1 and contract-authority review.

## 6. Acceptance examples

| Case | Expected physical handling | Expected economic handling |
|---|---|---|
| One building has multiple supply meters with separate contract numbers | Maintain separate connection/meter mappings and report each supported physical boundary. | Calculate each account independently; do not combine demand peaks. |
| One product site contains two buildings but no private interconnection topology is supplied | Keep two physical subgraphs under one workspace; no building-to-building energy edge. | Separate accounts; portfolio sum only when both are eligible. |
| A meter exists but multiplier, direction/register or asset mapping is ambiguous | Mark affected measured flow incomplete; do not infer sign or conversion. | Block charges/proceeds relying on that register. |
| PV export is metered and CEM feed-in agreement is verified for Site A | Show the export at Site A’s connection point. | Calculate a separate feed-in component for its specified payee/period. |
| Site A PV exports and Site B consumes; there is no cross-account agreement | Keep independent import/export physical histories; do not draw A-to-B branch. | No Site B credit or savings from Site A export. |
| Tariff Group B/C/D is selected but Pu’s measured interval/meter basis is unavailable | Physical time-series comparison can remain available if its own inputs qualify. | Withhold demand-charge or demand-saving component; do not infer billing interval from schedule interval. |
| Tariff-Clause Adjustment changes mid-assessment or billing period | Preserve physical schedule unchanged. | Split/re-evaluate by official effective date and applicable contract/bill convention; never use a stale global rate. |
| Property owner, utility contract holder and product operator differ | Preserve each party and authorized role separately. | Require evidence of the supply and PV purchase counterparty/payee before assigning amounts or access. |
| Historical assessment replay occurs after account/tariff/meter mapping changes | Load the pinned historical mappings and evidence versions. | Reproduce historical result or return explicit incomplete/unavailable; never silently use current terms. |

## 7. Open decisions and validation

- Confirm the pilot site's organization/owner/operator/contract-holder relationships, account count, installation addresses, meter IDs/registers and billing periods.
- Obtain authorized bills and relevant supply, PV interconnection and PV purchase agreements; verify which meter registers feed each bill component.
- Reconcile the exact Pu demand measurement window and billing calculations with tariff-class documents and matched Golden Bills (G1/U-001).
- Determine whether an actual portfolio contract grants any inter-account allocation or if the pilot has strictly separate billing; no such right is assumed.
- Review retention, access, personal/commercial data classification and deletion obligations before persistence/schema design.
- Confirm whether current G7.9 Step 2 entity vocabulary is retained, amended or formally superseded in the authority record.

Until these validations, this model can guide SHADOW design and synthetic tests, but cannot certify a Macau customer's bill or dispatch plan.