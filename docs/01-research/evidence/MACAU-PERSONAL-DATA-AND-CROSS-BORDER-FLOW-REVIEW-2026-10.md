# Macau personal-data and cross-border-flow review

**Reviewed:** 2026-10-04  
**Status:** Official-law and regulator-guidance review; not legal advice, project-specific legal determination, or deployment approval.

## Scope and verified public boundary

This note reviews Macau Law 8/2005 (Personal Data Protection Act) and the Macau Personal Data Protection Bureau (GPDP/DSPDP) public guidance on transfers outside Macau.

- Law 8/2005, Article 4(1)(1), defines personal data around information relating to an identified or identifiable natural person. Whether a particular meter, occupancy, staff, access, support, or operational record meets that definition depends on its content and how it can be linked to a person.
- Article 19 establishes the general condition for transfer of personal data outside Macau: the destination must ensure an adequate level of protection, assessed by the competent public authority with regard to factors including the data, purpose and duration, destination rules and safeguards.
- Article 20 provides specified conditions under which transfers may proceed, including notification in the circumstances set out in Article 20(1), and permits the authority to authorize a transfer with sufficient safeguards under Article 20(2). The applicable route depends on the actual transfer and facts.
- Article 21(1) separately provides a notification requirement for wholly or partly automated processing. It should not be conflated with the transfer-related conditions in Article 20.
- GPDP's public transfer guidance says controllers should comply with Articles 19/20 and that the Bureau had not published a list of countries/regions deemed to provide adequate protection on the reviewed guidance page. Its examples also treat personal data hosted on foreign servers as a transfer. This does not decide whether a particular Energy OS dataset is personal data or which transfer route applies.

## Product and architecture implications

Before accepting customer or site data, create a data-flow inventory covering source and fields, identifiability/linkage, purpose, controller/processor roles, recipient and sub-processors, primary and backup locations, remote support access, retention/deletion, and any external AI/API processing. Include logs, diagnostics and support exports rather than mapping only the primary database.

Use data minimization and least-privilege access as design requirements. Keep provider regions, subprocessors and support locations explicit and reviewable. If a flow involves personal data outside Macau, route that concrete flow to the responsible privacy/legal reviewer for Articles 19/20 and any applicable notification/authorization analysis before enabling it.

## Boundaries and unresolved work

This review does not conclude that Macau-only hosting is required, that Macau hosting alone resolves compliance, or that building/energy telemetry is categorically personal or non-personal. No project dataset inventory, vendor-region inventory, controller/processor determination, legal basis/notice review, or legal approval has been completed. U-027 remains open until the actual flows and responsible review are documented. Do not use customer personal data with an external AI service before this review.

## Primary sources

- [Macau Law 8/2005 — Chinese official Gazette text](https://bo.dsaj.gov.mo/bo/i/2005/34/lei08_cn.asp)
- [Macau Law 8/2005 — Portuguese official Gazette text](https://bo.dsaj.gov.mo/bo/i/2005/34/lei08.asp?printer=1)
- [GPDP: Transfer of personal data out of Macau](https://www.dspdp.gov.mo/en/abstract_detail_copy/article/l13av000.html)
- [GPDP: Data transfer and customers' consent](https://www.dspdp.gov.mo/en/abstract_detail_copy/article/l13av3a1.html)
- [GPDP: Personal data transfer to foreign servers](https://www.dspdp.gov.mo/en/abstract_detail/article/l13bxgm1.html)
- [GPDP: Basic concepts of personal data](https://www.dspdp.gov.mo/en/basic_concepts.html)
