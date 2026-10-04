# Dispatch product design direction study v0.1

**Status:** review artifact; no product, visual, locale, or implementation decision is approved by this study.

## Product task represented

Help an energy operator inspect a candidate source/load dispatch schedule, compare it with a baseline across the whole planning horizon, understand what is supported by available evidence, and record a SHADOW review without issuing equipment control.

The prototype communicates the task as a six-hour, one-hour-interval synthetic example. It distinguishes physical energy balance from financial settlement, exposes missing tariff/site/equipment evidence, and shows the HVAC rebound that makes the candidate horizon peak higher (485 kW baseline versus 510 kW candidate). It does not claim savings, bill impact, feasibility, or optimizer output.

## Three information-architecture hypotheses

| Direction | First question answered | Primary layout | Trade-off to evaluate |
| --- | --- | --- | --- |
| A · Timeline first | What changes across the whole horizon? | Time-series panel leads; readiness and comparison follow. | Strong temporal context; less immediate row-by-row comparison. |
| B · Delta first | What differs between baseline and candidate? | Interval table leads; chart and evidence follow. | Fast operational comparison; risk of over-focusing on a single interval. |
| C · Evidence first | What can I safely conclude from these inputs? | Readiness and evidence lead; chart and table follow. | Makes uncertainty prominent; can delay schedule inspection. |

All directions use the same task, six interval values, evidence states, claims, controls and disclosures. Switching direction changes panel order and visual hierarchy only; it does not change scenario calculations.

## Visual and interaction principles in this study

- Use an operator workspace with compact site context, a clear planning horizon, and a task-specific work area.
- Keep system status, data readiness, dispatch comparison, evidence and review state visible as distinct concepts.
- Use aligned interval boundaries and step lines for hourly averages; expose a table as the precise alternative.
- Label baseline and candidate directly and keep color paired with text, line style, and shape.
- Show uncertainty beside the decision it limits. Block unsupported economics instead of displaying invented savings.
- Make the review action explicitly page-only and non-persistent in this prototype.
- Support keyboard focus, skip navigation, narrow screens, and reduced motion in source. These are design intentions pending browser and assistive-technology checks.
- Treat Macau localization as an open product requirement. This artifact is Traditional Chinese only and is not a localization study.

## Color exploration status

A uses a restrained green/teal operational palette, B uses indigo to differentiate the comparison framing, and C uses a quieter evidence-oriented teal palette. They are early hypotheses for testing hierarchy and meaning, not approved brand colors or semantic tokens. Any selected system still needs contrast measurement and validation with status meanings, color-vision differences, light/dark requirements, and localized content.

## Review record and limits

The chart was corrected to show six interval averages as step series aligned to the 12:00–18:00 boundaries. The step chart ends at the 18:00 planning boundary and does not imply an observation at that instant. The synthetic table remains the precise source for values.

Source review confirms the three controls use the same content and update the DOM order to match each visual reading order. The prototype includes keyboard-focus styling, a skip link, live announcements for direction/review changes, a horizontally scrollable table, narrow-screen layout rules, and reduced-motion handling.

No rendered browser review, viewport screenshots, keyboard walkthrough, contrast measurement, screen-reader review, localization review, operator test, or domain validation is recorded here. No direction is selected. The product workflow, role model, permission model, input onboarding, exception handling, approval policy, audit trail, multilingual scope, and production screen inventory still need product/domain review before implementation planning.

## Next review questions

1. Which operator decision should the first screen optimize for: horizon-level effect, interval-level comparison, or evidence readiness?
2. Which roles prepare, review, approve, monitor and replay a dispatch proposal?
3. Which data and site/contract prerequisites should block each class of recommendation?
4. Which languages and locale fallback are required for Macau operators?
5. Which layout performs best in a rendered responsive review and operator walkthrough?

