# Customer Discovery and Usability Research Plan v0.1

**Status:** Proposed research protocol; no customer or usability evidence is recorded here.  
**Purpose:** Make WP-4 executable by validating the product's user, buyer, site, job, evidence needs and primary workflows before product scope is baselined.  
**Authority:** G0 market rationale, `PRODUCT-DESIGN.md`, `PRD-v0.1.md`, `USER-FLOWS-AND-IA-v0.1.md`, and current G1/G6/G7 constraints.  
**Scope:** Research planning only. This document does not approve product scope, make a savings claim, close a research Gate, or authorize live system access or control.

## 1. Research objectives

Answer with observed customer evidence rather than assumptions:

1. Which Macau commercial-site segment has a frequent, consequential energy decision that this product can improve?
2. Who experiences the problem, who owns the workflow, who approves a change, who controls data access, and who pays?
3. What do users do today to understand bills, demand exposure, meter/BMS quality, plant constraints, and proposed actions?
4. Which records do finance and operations accept as evidence, and what would make a cost or savings result untrustworthy?
5. What site data is realistically available, who can provide it, and what integration effort, permission and operational risk does it create?
6. Do the six proposed product tasks and IA match actual work? Where do users get confused, stop, or require another role?
7. Which language, terminology, accessibility, deployment, support and commercial expectations affect a first pilot?

The work separates **problem discovery**, **workflow observation**, **prototype usability**, and **commercial validation**. A positive reaction to a concept is not evidence of purchase intent or willingness to pay.

## 2. Current hypotheses to test

Treat these as hypotheses, not interview premises:

- Candidate sites: integrated resorts/hotels, shopping malls, office towers and public buildings.
- Candidate roles: energy/facilities manager, building operator/control-room staff, finance/asset owner, and energy-service/integration partner.
- Candidate first product loop: qualify data → understand site and settlement context → explain a supported cost result → inspect a SHADOW recommendation → retain/replay evidence.
- Candidate differentiation: connect physical/settlement context and traceable economic evidence with operationally constrained recommendations.
- Candidate trust boundary: unknown tariff, incomplete data, synthetic evidence, forecast output and SHADOW proposals must never be mistaken for verified bills, measured savings or executed control.

Do not present these propositions to participants until after asking about their actual past work.

## 3. Sampling and recruitment plan

Use purposive recruitment across different site types and responsibilities. Record why each participant matches a role; do not treat job titles as proof of decision authority.
**Evidence-informed site strata to seek (proposal only):** DSEC reports 147 hotel establishments and about 45,000 rooms for 2025; CEM's 2026 hotel/resort energy-saving activity groups a resort complex as one participant despite multiple supply points and uses 1,600 kVA subscribed demand to distinguish two program groups. If access permits, seek (1) a large hotel/resort complex at or above that published threshold, (2) a standard/economical accommodation site below or near it, and (3) a non-hotel commercial site to test whether the workflow transfers. These are discovery strata, not selected target markets or representative sampling quotas. Do not infer subscribed demand from room count. For every site, record supply-point/meter boundaries, energy and finance roles, procurement/approval authority, and whether redacted bill and interval artifacts can be reviewed. Source details and evidence limits: `docs/01-research/evidence/G2-MACAU-COMMERCIAL-LOAD-FLEXIBILITY-EVIDENCE-2026-10.md`.



### Discovery wave

Plan an initial 8–12 interviews across the candidate roles and at least two site contexts, where access permits. This is a learning sample, not a statistically representative market estimate. Include people close to the work as well as a buyer/finance perspective. Expand or rebalance the sample if key roles, decision paths or site types remain unrepresented or evidence conflicts.

Seek participants who can describe a recent concrete example and, where permitted, walk through the artifact or workflow they used. Prefer actual recent bills, interval data, exception reports, operator logs or vendor proposals in redacted form over hypothetical opinions. A participant may decline to share artifacts without being excluded.

### Usability wave

After revising the prototype from discovery findings, run a formative task session with 5–8 relevant users per iteration as an initial planning target, sampling across the roles that will perform the tested tasks. This small qualitative round is intended to expose workflow and comprehension problems; it cannot establish population-level usability or market demand. Repeat after material design changes.

Recruit through direct, authorized introductions or the user's existing customer/research relationships. Do not claim an organization or participant has endorsed the product unless they explicitly have.

## 4. Discovery interview guide (45–60 minutes)

### A. Context and responsibility (5–10 min)

- Please describe your site, role and responsibilities related to energy, facilities, finance or building operations.
- Which decisions do you personally make? Which do you recommend, approve, fund or execute?
- Who else is involved, and what information does each person need?
- What systems, suppliers or internal teams do you rely on?

### B. Recent real event (15–20 min)

Ask for the most recent example, not a general opinion:

- Tell me about the last time an energy cost, demand peak, plant issue or data problem required attention.
- What triggered the work? What did you do first, next and last?
- Which tools, spreadsheets, bills, screenshots or people did you use?
- What was difficult, slow, uncertain or repeated?
- What was the consequence of acting late or getting it wrong?
- How often has a similar event happened in the last month/quarter/year?
- What did you decide, and how did you know the outcome was acceptable?

With permission, ask the participant to show a redacted artifact or reconstruct the workflow. Note actual workarounds and handoffs.

### C. Economics and evidence (10 min)

- How do you reconcile the operational view with the bill or contract today?
- Which meter, demand window, tariff, contract, tax, PV or settlement details can change the answer?
- Who is trusted to confirm those details?
- What level of discrepancy is acceptable for exploration, budgeting or a formal savings claim?
- What proof would finance, an operator or a customer require before believing a result?
- When are you unable to reach a reliable answer? What do you do then?

Do not assume the research team can determine bill-grade truth from one participant's explanation. Capture contradictions and request authoritative artifacts or follow-up validation.

### D. Data and integration (10 min)

- Which meters, BMS points, equipment records and billing data are available, at what intervals and with what delay?
- Who owns each system and can authorize access?
- How are units, timestamps, missing/stale values and point mappings handled?
- What integration has been attempted before? What took time or failed?
- Are there network, cybersecurity, procurement, vendor or operational restrictions?
- What data cannot leave the site, and what deployment model is acceptable?

### Site-context probes (use selectively; 5–10 min)

After the behavior-first questions, use only the probes that fit the participant's actual site. Ask them to map the physical site, supply account/contract, meters and responsible roles; do not assume one complex equals one bill or one decision-maker.

- **Hotel or resort complex:** How many supply points, meters and contracts cover the operation, and how are they reconciled? Which central plant, chillers, BMS or vendor systems affect energy decisions, and who can change or only observe them? How do occupancy, events and guest-service requirements change operating practice? Which facilities, finance and central teams review the evidence?
- **Smaller accommodation:** Which energy review and operating tasks are handled by the owner, a small facilities team or an external provider? What tools or vendor services are already used? What data connection, setup effort and ongoing support would be manageable?
- **Non-hotel commercial site:** Which operating hours, tenants, processes or service constraints shape energy decisions? Which parts of the described workflow match existing practice, and which depend specifically on hotel operations?
- **Across site types:** What are the actual approval, procurement, data-access and operational handoffs? Which redacted artifacts could confirm the meter/account boundary, recent event or workflow, if the participant is willing?

Treat differences between contexts as evidence to investigate, not as proof that a segment is preferable. Do not request confidential plant diagrams or vendor/network details; a verbal boundary map or redacted, approved artifact is sufficient.

Do not request credentials, live control access, personal data, unredacted bills or sensitive building/network diagrams during discovery.

### E. Concept check (5–10 min, only after open discovery)

Show the product proposition and synthetic prototype after the participant has described their current work:

- Which part, if any, maps to a task you actually perform?
- What seems inaccurate or missing for your site?
- Which part would you ignore? Why?
- What would you need to verify before relying on a cost result or recommendation?
- What would make this unsafe or politically difficult to introduce?
- What alternative is already good enough?

Avoid leading questions such as “Would you use this?” or “Would this save money?” Record concrete commitments separately from favorable opinions.

### F. Commercial and next-step evidence (5 min)

- Who owns the budget and procurement decision for this kind of capability?
- What existing spend, contract or internal project would this replace or complement?
- What would a pilot need to prove, and what would stop it?
- Who else should be interviewed to understand the decision?
- Is there a safe, authorized next step (for example, a redacted bill review or workflow observation)?

Do not infer willingness to pay from hypothetical price reactions alone. Record actual budget, procurement, pilot or data-sharing commitments only when the participant makes them.

## 5. Prototype usability session (45 minutes)

Use synthetic prototype v0.6 for the established task flow, or v0.8 for a comparative workspace-organization session; label all records as synthetic and do not connect either prototype to a live site or enter credentials. v0.8 presents one demand-evidence case in three organizations (evidence-first, exceptions-first, guided assessment) with the content and visual styling held constant. Navigation and workflow remain hypotheses. Do not use v0.7 for comparative sessions: rendered review found that all variants remained visible because the grid display rule overrode the inactive sections' native `hidden` state. Retain v0.2–v0.5 only when the session explicitly evaluates their historical interaction changes. Tell participants the interface is being evaluated, not their expertise. Ask them to think aloud while allowing natural work. Where relevant, compare the result-kind choices and review dispositions without coaching.

Choose the tasks relevant to the participant's role:

1. **Check site readiness and access:** identify whether source data is current and trustworthy; inspect site scope and permission purpose; say what is missing, who would need to authorize access, and what functions are affected. No credentials are requested.
2. **Explain an economic result and its evidence:** identify whether the view is bill reconstruction, interval assessment, or baseline comparison; inspect the separate regulation, customer-contract, site-configuration and assumption records; find the meter, period, coverage and blockers; explain why an unknown Pu interval or monthly-charge formula prevents a bill-grade result.
3. **Distinguish energy streams:** explain consumer settlement versus PV producer export and say whether one can be credited to the other site's bill from the evidence shown.
4. **Review a SHADOW recommendation:** identify its baseline, horizon, proposed action, predicted effect, uncertainty and constraints; choose or interpret reviewed/dismissed/needs-data; explain why that disposition neither authorizes execution nor proves an outcome.
5. **Inspect evidence/replay:** find pinned source/rule/model versions, separate replay state from measured-outcome state, and determine whether replay is complete or unavailable and whether an outcome has actually been measured.
6. **Recover from a failure state:** respond to stale/partial data, missing authorization, or a failed integration without silently treating the result as verified.
7. **Read the trend without relying on the graphic alone:** use the chart, text summary, or expandable sample table to describe the approximate synthetic pattern; identify the values as illustrative rather than measured site demand or CEM settlement demand. Record whether the alternate text/table representation helps the participant understand the trend.
8. **Find a secondary view on a narrow screen:** at a phone-sized viewport, locate Tariff & contract evidence and Integrations & site access without coaching; return to a previous view using browser back and explain what changed. Record whether the participant notices, understands and can operate the compact selector. Repeat at a wider viewport only to compare navigation discoverability; do not imply a preferred interaction before testing.

Do not coach during the first attempt. If the participant is stuck, ask what they expect to happen; then provide neutral assistance and record it.

### Observation measures

Record per task:

- completion: independent / completed with neutral prompt / not completed;
- first action and navigation path;
- errors, backtracks, hesitation, terminology mismatch and mistaken assumptions;
- whether the participant can explain evidence status and downstream impact in their own words;
- confidence (participant's own rating and rationale);
- accessibility, keyboard, viewport or localization barriers, including narrow-screen navigation discoverability and browser back/forward synchronization;
- severity and frequency of each issue;
- proposed design change and the evidence supporting it.

Task time is contextual only; do not compare users with different task familiarity as if it were a benchmark. For task 8, success requires independently finding both secondary views at phone size and returning with browser back while the visible selection follows the active view. A task is not successful if the participant reaches the right screen but misunderstands bill reconstruction vs interval estimate vs modeled comparison; review disposition vs execution vs measured outcome; verified vs assumed; SHADOW vs execution; or consumer vs PV-export settlement.

### v0.8 comparative information-architecture protocol

Use this extension only when the study question is which workspace organization helps a particular role understand and progress the evidence task. The prototype is a discussion stimulus, not a realistic operational system.

- Assign one focal organization per participant for the unaided core task. Balance the focal organization across role and site-context categories as recruitment permits; do not let every participant begin with the same version.
- After the focal task, participants may inspect the other two organizations in a rotated order. Ask where they expected to find the blocker, source evidence, affected work and safe next step. Record stated preference separately from observed task performance.
- Do not repeat the exact task three times and compare task times as if the variants were controlled benchmarks: later attempts benefit from learning the scenario. If all three organizations must be tested for task success, design separate, matched scenario prompts and counterbalance variant/task order before recruitment.
- Keep every fact and task-critical status identical across variants. Record any content mismatch or visual imbalance as a prototype confound, not as a user preference.
- The existing 5–8 participant target is an initial formative iteration size, not enough by itself to rank three IA options across all user/site roles. Report variant-level signals and uncertainty; do not declare a winner from vote counts or stated preference. If the owner needs a comparative conclusion, propose an adequate role-balanced sample and session plan before recruitment.

No recruitment, comparison session or user finding is authorized or claimed by this protocol update.

## 6. Evidence handling and synthesis

For each session assign an opaque participant code and record only the minimum role/site context needed for analysis. Obtain explicit permission before recording audio/video or retaining artifacts. Prefer notes; redact names, account numbers, addresses, meter identifiers and commercially sensitive details. Store research records only in the approved, access-controlled project location. Agree retention and deletion with the project owner before collection.

A finding record should include:

- finding ID and date;
- participant code, role, site-type category and recruitment basis;
- method (interview, observation, prototype task, artifact review);
- observed behavior or paraphrased statement, clearly separated from researcher interpretation;
- artifact/evidence reference and permission status, if any;
- supporting and conflicting cases;
- confidence/status: single signal, repeated signal, contradicted, or validated by independent evidence;
- affected user need, PRD requirement, workflow/screen and architecture implication;
- decision needed, owner, and next validation step.

Do not put identifiable customer evidence in public repository history. Store only anonymized synthesis and access-controlled references there. Do not turn a participant statement about tariff, settlement or safety into a project-wide fact without checking the relevant primary evidence and applicable customer contract.

## 7. Synthesis and decision rules

After each wave:

1. Build a role × task × site-context map and identify missing perspectives.
2. Map observed steps, handoffs, artifacts and failure points to the six product tasks and PR-01..PR-09.
3. Separate observed behavior, participant interpretation, researcher inference and external/source-verified fact.
4. List contradictory findings instead of averaging them away.
5. Update hypotheses and product/design options; preserve rejected options and rationale.
6. Decide whether evidence is strong enough to change PRD wording, IA, visual hierarchy, access model or MVP scope.
7. Review decisions with the product owner; record owner choices separately from research findings.

Use these status meanings:

- **Supported:** repeated, relevant evidence from independent participants or artifacts supports the hypothesis; scope and counterexamples are documented.
- **Mixed:** credible evidence conflicts across roles/sites or the sample is not sufficient to explain the difference.
- **Not supported:** relevant evidence contradicts the hypothesis or actual workflows do not require the proposed capability.
- **Untested:** no adequate evidence was collected.

A small qualitative study can support workflow and design revision, not market sizing, statistical confidence, guaranteed ROI or proof of willingness to pay.

## 8. Decision outputs and completion criteria

The study is ready for synthesis when it has evidence for, or explicit remaining unknowns on:

- lead site/segment and buyer/user/approver/data-owner relationships;
- at least one recurring, consequential job and its present workflow;
- evidence requirements for operational use and finance/customer claims;
- data access and integration feasibility, including authority and burden;
- usability of the primary workflows and comprehension of evidence/safety states;
- language, accessibility, deployment, service and support expectations;
- product changes to PRD, information architecture, prototype and requirement acceptance criteria.

No research plan alone closes WP-4. Exit requires anonymized interview/observation evidence, prototype task findings, a product-owner review record, updated PRD/flows/prototype with remaining uncertainty explicit, and traceable decisions. Commercial demand and pilot willingness remain unproven until actual buyer and site evidence exists.

## 9. Session capture template

```text
Study/session ID:
Date:
Researcher:
Participant code:
Role / authority:
Site context:
Recruitment basis:
Consent and recording permission:
Artifacts shown/shared (redacted? permission?):
Recent event:
Observed workflow and tools:
Frequency / consequence:
Data access and integration constraints:
Evidence trusted / evidence gaps:
Prototype tasks and completion:
Misunderstandings / safety or economic interpretation:
Conflicting evidence:
Researcher inference (separate from observation):
Potential PRD / IA / architecture impact:
Follow-up authorized:
Finding IDs:
```

## 10. Current status

- No customer interviews, artifact reviews or prototype usability sessions are evidenced by this plan.
- The role, site and workflow hypotheses remain open.
- This plan is an executable preparation artifact for WP-4; it does not authorize contacting participants, collecting customer data or altering the PRD based on invented evidence.
- The next research action is to arrange authorized access to representative Macau site users, then conduct the discovery wave and assign either the v0.6 workflow tasks or the v0.7 comparative IA protocol according to the approved study question, while continuing independent Gate research.


### v0.8 rendering note

A bounded browser observation at the available narrow viewport confirmed that only the selected variant is exposed after switching and that the A/B/C selector wraps instead of requiring horizontal scrolling. Keyboard Shift+Tab/Space changed the selected variant and exposed its corresponding workspace in the accessibility tree. This is one local browser context and does not establish fixed CSS viewport coverage, screen-reader behavior, full keyboard traversal, or target-user success. Recheck the exact deployed prototype version before any authorized participant session.
