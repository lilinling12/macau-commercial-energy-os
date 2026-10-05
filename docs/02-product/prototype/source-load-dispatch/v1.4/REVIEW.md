# Source/load dispatch prototype v1.4 review

**Review date:** 2026-10-05  
**Status:** EV settlement-boundary clarification; not production UX approval.  
**Base:** v1.3 six-stage workflow.  
**Base HTML blob:** aeead4dc9545a9857c87a58eb3f230320d6ebaf6

## Research basis

The product design addendum **“2026-10-05 — Tariff profile and EV charging settlement boundary”** states that an EV charger may remain a physical flexible load while its settlement tariff must be bound to the verified serving meter, account, contract and tariff profile. It explicitly rejects presuming that every charger inherits the building tariff or that a separate EV tariff or allocation applies. This prototype update carries that evidence rule into the visible workflow; it does not assert an applicable tariff for any Macau site.

## Change

- The stage 2 site-resource list describes EV charging as a **physical-load candidate** that may be modeled when evidence exists, while stating that the synthetic candidate does not model or schedule EV.
- Stage 4 adds a separate **EV charging settlement attribution** row. It says the building tariff and cost-allocation rule cannot be presumed and names the charger-serving meter, account, effective contract/tariff and matching bill as required evidence.
- No EV energy, charger power, tariff, charge schedule, savings or bill amount has been added to the synthetic dispatch scenario.

## Rendered review

Opened the exact v1.4 branch source in Microsoft Edge through the local review server. The accessibility tree exposed version **v1.4** and, in stage 4, the full EV row text:

- Status: **unverified**.
- Impact: do not presume the building tariff or a cost-allocation rule.
- Evidence: charger-serving meter, account, effective contract/tariff and matching bill.

A desktop screenshot at 1265×712 showed the cost table contained in its own horizontal scroll region. The added evidence cell extends beyond the initially visible portion of the table, consistent with the existing table interaction. The new row was not rendered at a narrow viewport in this pass: the local Playwright headless browser executable was unavailable. Do not treat inherited v1.3 mobile measurements as v1.4 mobile verification.

## Remaining limits

This is a synthetic product/UI review. It does not verify CEM tariff applicability for a real EV charger, customer account or building; establish cost allocation; add EV dispatch capability; validate optimization or savings; or authorize equipment control. Narrow viewport review of the new row, keyboard and screen-reader review, touch review, measured contrast, text scaling, complete Portuguese/English localization, user validation and WCAG conformance remain open.
