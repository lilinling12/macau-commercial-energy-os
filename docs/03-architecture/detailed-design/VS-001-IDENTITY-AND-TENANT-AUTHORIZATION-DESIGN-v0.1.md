# VS-001 Identity and Tenant Authorization Design v0.1

**Status:** Draft, technology-neutral; user roles and identity provider are not validated or selected.  
**Purpose:** Define how identity and site authorization govern every VS-001 read/write boundary, and prevent client-supplied tenant/site labels from acting as proof of access.  
**Authority:** PR-01, D-008, D-065, G6-09 in G6-safety-control.md, current PRD/architecture and the source audit.  
**Scope:** Human and service access for the shadow-mode VS-001 product path. This design does not authorize controlled execution and does not select an identity provider or framework.

## 1. Security objective

Every action must be attributable to an authenticated principal and authorized against the exact organization/site resource and operation. Tenant/site scope is established from trusted identity and server-side policy, then carried through API handling, domain ports, persistence, background work and evidence reads.

Identifiers in request bodies, telemetry payloads, URLs, headers or trace context are selectors only. They do not grant authority. If the authenticated principal, authorized site membership and requested resource scope do not agree, deny the operation before domain data is returned or mutated.

The existing VS-001 controller accepts a body directly and the service compares the telemetry tenant/site values with the resolved graph context. That comparison is useful integrity checking, but it does not authenticate the caller or prove the caller may access the site. The inspected controller has no authentication/authorization guard wired into the application module. Treat the endpoint as a development scaffold; it is not safe for a customer-facing deployment.

## 2. Principal types and identity boundaries

| Principal type | Example | Authority source | Scope |
|---|---|---|---|
| Human user | Facilities manager, operator, finance reviewer, integration partner | Authenticated session established by a selected identity provider | Organization membership plus explicit site entitlements and allowed actions |
| Site integration identity | BMS/AMI connector or Edge agent | Provisioned machine credential bound to one organization/site and connector | Ingest only the registered site/device/point set and read only required configuration |
| Platform service identity | API worker or replay worker | Workload identity issued by the selected deployment environment | Explicit service-to-service permissions; no ambient tenant access |
| Simulator/test identity | CI fixture or local replay | Test-only credential/fixture boundary | Synthetic fixtures only; cannot access customer data or real command paths |

The credential and key lifecycle for Edge/device identity is separate from human login and remains subject to U-022. Step-3B HMAC fixtures are not production credentials.

## 3. Authorization context

After authentication, establish a server-controlled authorization context containing:

    principalId
    principalType
    organizationIds
    siteEntitlements
    allowedActions
    authenticationMethod / session context
    policyVersion
    issuedAt and expiry

This context is created at the trusted API/middleware boundary and passed explicitly to application services. Domain code must not reconstruct authorization from request JSON.

### Candidate action families

These action names are an authorization-design vocabulary, not finalized product roles:

- organization/site read;
- telemetry read and ingestion;
- site-model read;
- point-mapping propose/review;
- contract/tariff read and configure;
- cost/evidence read;
- recommendation read and review-annotate;
- membership and audit administration.

No user or machine action for device execution is enabled in VS-001. A future command permission requires a separate product workflow and G6/G7 authorization.

### Candidate role mapping

The PRD roles remain hypotheses. A later role decision may map roles to action families, but the backend must enforce action grants rather than trusting a UI role label. Avoid a single broad administrator role spanning customer data, secrets, tariff approval and field control without separate justification.

### Workflow-to-authorization review map

This map links the PRD/interaction flows to authorization actions and the specific customer/site facts that WP-4 must validate. It is **not** a role grant matrix; candidate job titles do not receive permissions by appearing here.

| Product workflow | Candidate action family | Scope that must be enforced | Product/site question before role mapping |
|---|---|---|---|
| Connect/qualify a site and review data health | Site read; integration configuration; mapping propose/review; telemetry read | Explicit organization and site entitlement; ingestion identity is additionally bound to registered source/device/point IDs. | Who may connect a source, propose a point/asset mapping, approve the mapping, and view raw versus summarized telemetry? Must propose and approve be separated for this site? |
| Explain cost, demand or settlement evidence | Cost read; tariff/contract read; evidence read/export | Explicit site entitlement. Portfolio/cross-site queries must resolve to the exact authorized site set; organization membership alone must not widen data access. | Which finance/asset users may see bill artifacts, tariff/contract terms, raw inputs and cross-site rollups? Which evidence may be exported/shared? |
| Review a SHADOW recommendation | Recommendation read; review annotation | Site-scoped recommendation and actor attribution; annotation is not command authority. | Which roles may record reviewed/dismissed/needs-data, and can a reviewer annotate across assigned sites? No device-execution action exists in this MVP. |
| Inspect evidence and request replay | Evidence read; replay request | Authorize the evidence record and every source/result reference; replay work inherits persisted actor and site scope and cannot broaden it. | Who may request a replay, access its derived result, and export lineage? Are compute quotas or approvals needed? |
| Manage organization membership and site access | Membership/access administration | Explicit admin action grant; membership administration is distinct from entitlement to read every site's economic or operational data. | Does the organization administrator also receive site data access, or must each site grant be separate? Who approves high-impact membership changes? |
| Partner configuration / delegated support | Time-bounded delegated configuration or support actions | Named organization/site, explicit action set, expiry/revocation, attributable human sponsor; no credential sharing. | Which partner actions are needed, who sponsors them, how long access lasts, and how the customer can revoke it? |
| Telemetry service or Edge ingestion | Telemetry ingest; source health report | Workload identity bound to registered tenant/site/source/device/point; no human UI role or economic-review capability is inherited. | Which connector credentials and provisioning/rotation method apply to each pilot source? |

**Stable design boundary:** enforce authenticated principal → explicit action grant → exact resource scope on the server. Candidate human roles may group grants for usability, but a UI role label, organization membership, request body, site selector or service identity cannot create a grant. Do not add control permission to the MVP.

## 4. Request authorization sequence

For each HTTP/API request:

1. Authenticate the presented session or service credential. Reject missing, invalid, expired, revoked or malformed credentials.
2. Resolve the requested organization/site from a route/resource identifier.
3. Load authoritative membership/entitlement from server-owned policy data.
4. Authorize the specific operation and resource. Default deny when policy is absent, stale or ambiguous.
5. Bind a server-derived tenant/site scope to the request context.
6. Validate body resource references against that scope. A body tenantId/siteId mismatch is rejected; a match does not create access.
7. Invoke the domain operation using the server-derived context and scope every repository/port call with it.
8. Record a minimal audit event for successful privileged changes and denied cross-scope attempts.
9. Return only data authorized for that principal and resource.

For event ingestion, the producer identity is first authorized for a site and registered device/point set. The payload tenantId/siteId/deviceId/pointId are then checked against that registration. A producer cannot choose another tenant by changing JSON fields.

## 5. Enforcement by layer

| Layer | Required enforcement |
|---|---|
| Web/API boundary | Authentication middleware/guard; explicit action authorization; request-size/schema limits; CSRF/session policy if cookie sessions are selected; no anonymous access to customer endpoints |
| Application service | Accept a typed, trusted authorization context; authorize use case and validate target resource; do not accept a body-provided tenant scope as authority |
| Domain ports | Include tenant/site scope explicitly in read/write method contracts; return not-found/denied semantics without leaking foreign resource data |
| Persistence | Every tenant-owned row and query carries tenant scope; writes use the same authorized context; unique constraints include owning scope where appropriate; transaction boundaries prevent scope switching |
| Background jobs/workflows | Persist the requesting principal/service identity and authorized scope; revalidate resource/policy version before sensitive effects; never run as an unrestricted global worker by default |
| Cache | Include tenant/site and policy version in cache key; prevent shared cache entries from serving across scopes; define invalidation on access revocation |
| Evidence/replay | Authorize both the evidence record and every referenced source/result; do not allow a valid evidence ID to bypass site entitlement |
| Connector/Edge | Machine identity is bound to a site/device set; user identity is not reused as device identity; Edge command trust/key lifecycle remains separately gated by U-022 |

Database row-level security may be evaluated as defense in depth when the persistence design is selected. It does not replace application authorization, service-level tests or scoped repository queries.

## 6. Denial, enumeration and audit behavior

- Missing/invalid authentication returns an unauthenticated result. Authenticated but unauthorized operations are denied.
- A request for a resource outside the caller's site scope must not return the resource, its tenant identity, contract data or evidence references. The exact 403 versus indistinguishable 404 policy is a product/security decision to record consistently.
- Do not reveal whether a foreign tenant's site, meter, recommendation or evidence ID exists.
- Denials and privileged configuration changes record principal, action, target scope, outcome, policy version, timestamp and trace reference; never log bearer tokens, passwords, secret material or full sensitive payloads.
- Retain authorization audit separately from ordinary diagnostic logs and apply an approved retention/access policy.
- Access revocation must take effect within a defined policy/cache bound; the duration is not yet specified and must be decided before production.

## 7. Tenant isolation invariants

1. Every customer-owned record has a single owning organization and site scope or an explicit documented portfolio scope.
2. No query, cache lookup, workflow, export, evidence lookup or replay may omit the authorized scope.
3. A resource ID is not a capability token.
4. A request body cannot widen scope; repeated tenant/site identifiers are consistency checks only.
5. Service identities receive the minimum operations and site set needed for the workload.
6. Scope and entitlement are rechecked at trust boundaries and before any later irreversible effect.
7. Test fixtures and synthetic demo data cannot silently share a namespace or credential with customer data.

## 8. Required verification scenarios

These scenarios define future acceptance evidence; they have not been executed as part of this design draft:

- Unauthenticated request cannot call VS-001 evaluate or read evidence.
- Authenticated user for tenant A cannot read tenant B's site, telemetry, tariff, cost, recommendation or evidence by changing URL IDs.
- Tenant A caller submits a body claiming tenant B/site B; reject before graph, tariff or optimizer ports are called.
- Authorized tenant A user submits tenant A IDs but an unauthorized site B reference; deny based on membership, not matching payload values.
- Read-only user cannot change mappings, contracts, memberships or recommendation annotations.
- Integration identity for site A cannot publish telemetry under site B or an unregistered device/point.
- Revoked/expired service credential is rejected; retries do not restore revoked authority.
- Background job cannot use an unscoped global repository method to read a site outside its persisted authorized scope.
- Evidence reference from another tenant or an unentitled site does not disclose subject, derivation, source refs or related recommendation.
- Organization membership administration does not implicitly grant data-read access to every site; any granted site set is explicit and auditable.
- A delegated partner grant expires/revokes at its recorded scope and cannot be reused for another site or for economic/recommendation review unless those exact actions are granted.
- A replay job remains confined to its persisted actor and authorized site scope even when referenced inputs span sites; cross-scope inputs fail closed.
- Cache hit produced under a different tenant/site or policy version is not returned.
- Audit record contains actor/action/scope/outcome but no credentials or sensitive raw payload.

Acceptance requires executable negative tests and reviewable evidence in the selected runtime/deployment, not only this checklist.

## 9. Open decisions

- Identity provider and federation protocols, including enterprise SSO requirements.
- Session/token type, lifetime, refresh/revocation behavior, MFA and recovery policies.
- Validated human roles and role-to-action mapping, membership lifecycle, delegated integration access, configuration proposal/approval responsibilities and high-impact membership approvals.
- Organization/portfolio/site hierarchy and exact site-entitlement semantics, including whether organization administrators have data access and how cross-site finance/reporting grants are explicitly assembled.
- Service/workload identity mechanism across selected deployment modes.
- Persistence isolation mechanism, including whether database row-level security is required.
- Authorization cache policy and revocation bound.
- Audit retention, data residency, privacy and support-access policy.
- Machine identity/key provisioning, rotation and revocation for Edge remain U-022 and a separate security decision.
- Controlled-execution permissions remain disabled until the G6/G7 conditions and customer/site authorization are satisfied.

These decisions require customer/security review and deployment context. Do not infer them from the provisional stack, candidate roles, existing code or this draft.

## 10. Traceability and status

- PRD: PR-01 tenant/site scope; PR-08 operator authority and review.
- G6: G6-09 tenant/site isolation and least privilege; G6-05 Edge identity/key lifecycle remains separate.
- Architecture: ARCHITECTURE-DESIGN.md; VS-001-DETAILED-DESIGN-v0.1.md.
- Open questions: U-022 for production command signing and Edge key lifecycle; product identity/role decisions remain unvalidated.
- Current code finding: VS-001 HTTP path has no auth guard; AppModule binds synthetic/fail-closed adapters; no production identity or persistence module appears in the inspected implementation tree.

This document narrows the design gap but does not prove implementation, customer role validation, production identity, complete tenant isolation, G6 closure or control authorization.
