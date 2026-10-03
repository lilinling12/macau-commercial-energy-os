# VS-001 Cost Result and Replay Manifest — Contract Proposal v0.1

**Status:** Design proposal only; not an accepted cross-module contract or production API.  
**Purpose:** Close identified design gaps for cost-result precision, evidence status propagation and reproducible replay.  
**Authority:** D-012, D-015, D-019, D-022–D-029, D-044, D-065, D-073–D-076; current telemetry/recommendation/evidence schemas; VS-001 detailed design.  
**Stack boundary:** Payload semantics are technology-neutral. D-065 requires versioned canonical contracts and generated bindings; this proposal does not choose OpenAPI, JSON Schema or Protobuf as the final authoring format.

## 1. Design requirements

The VS-001 result and replay contract must:

1. preserve decimal monetary truth and explicit units (D-026);
2. distinguish complete, partial, assumption-based and blocked calculations;
3. carry meter/contract/tariff/evaluator/mapping provenance with effective time (D-012, D-015, D-017, D-024);
4. prevent unresolved settlement inputs from being represented as verified customer economics (D-019);
5. preserve fixed aggregation boundaries independently from sample quality (D-040, D-074);
6. reproduce a result from the original immutable input and version set, never “latest” dependencies;
7. exclude trace/correlation IDs from semantic identities and result equality (D-073);
8. remain separate from command identity, approval and field-write semantics (D-008, D-025, D-070, D-075).

## 2. Proposed CostEvaluationResult shape

The following is illustrative JSON-like structure, not a committed schema:

    {
      "contractVersion": "proposal-0.1",
      "evaluationId": "stable semantic evaluation identity",
      "tenantId": "tenant reference",
      "siteId": "site reference",
      "period": {
        "start": "RFC3339 instant",
        "end": "RFC3339 instant",
        "timeZone": "IANA timezone"
      },
      "resultStatus": "COMPLETE | PARTIAL | SCENARIO | BLOCKED",
      "evidenceStatus": "VERIFIED | DERIVED | PROJECT_ASSUMPTION | UNKNOWN",
      "settlementReadiness": "BILL_GRADE_ELIGIBLE | SCENARIO_ONLY | NOT_CALCULATED",
      "currency": "ISO currency code",
      "totalAmount": "canonical decimal string or null",
      "components": [
        {
          "componentCode": "stable rule/component code",
          "amount": "canonical decimal string",
          "quantity": "canonical decimal string or null",
          "unit": "explicit physical or economic unit",
          "tariffRuleRef": "immutable rule/version reference",
          "sourceRefs": ["immutable source references"],
          "evidenceStatus": "evidence status"
        }
      ],
      "inputCoverage": {
        "expected": "integer count",
        "accepted": "integer count",
        "excluded": "integer count",
        "missing": "integer count",
        "qualityPolicyRef": "versioned policy reference"
      },
      "unresolved": [
        {
          "code": "stable open-rule or data-quality code",
          "severity": "BLOCKING | LIMITING | INFORMATIONAL",
          "message": "operator-readable explanation",
          "sourceRef": "optional Authority or evidence reference"
        }
      ],
      "provenance": {
        "meterRef": "meter reference",
        "contractRef": "immutable contract version reference",
        "tariffPackageRef": "immutable package/version/hash reference",
        "measurementPolicyRef": "immutable interval/quality policy reference",
        "mappingSnapshotRef": "immutable mapping snapshot reference",
        "evaluatorBuildRef": "immutable build/version reference"
      },
      "evidenceRefs": ["evidence record references"],
      "replayManifestRef": "immutable replay manifest reference or null"
    }

### Result semantics

- COMPLETE means the calculation ran against all required declared inputs. It does not by itself claim a verified customer bill.
- PARTIAL means a clearly bounded subset was evaluated; excluded components, periods and input coverage must be visible.
- SCENARIO means at least one material input/rule is a PROJECT_ASSUMPTION; monetary output must be visibly scenario-labelled.
- BLOCKED means a required input or rule is missing/conflicting and no authoritative amount is emitted.
- BILL_GRADE_ELIGIBLE is allowed only when every tariff, contract, meter and measurement rule required for the declared scope has sufficient evidence, and the applicable Golden Bill gate is satisfied. Before that, use SCENARIO_ONLY or NOT_CALCULATED. G1 remains open.
- VERIFIED, DERIVED, PROJECT_ASSUMPTION and UNKNOWN retain the Evidence Authority meanings; do not assign VERIFIED merely because software returned a value.
- Monetary amounts are canonical decimal text, not binary floating-point JSON numbers. Rounding mode and scale must come from a versioned settlement policy; do not invent interval rounding.
- Missing/null monetary values must not serialize as zero. A missing amount is not a zero charge.
- Components remain separate; PV producer feed-in settlement cannot be collapsed into consumer load (D-021/D-077).

### Compatibility implications

The existing Recommendation schema allows objective.estimatedValue as a JSON number. That field cannot be treated as authoritative monetary truth under D-026. Before economics are put into a recommendation, either reference a CostEvaluationResult as the monetary authority or revise the recommendation contract to use an explicit currency plus canonical decimal text. The current schema must not be silently reinterpreted.

## 3. Proposed ReplayManifest shape

The manifest pins the complete semantic input set needed to reproduce one VS-001 evaluation:

    {
      "manifestVersion": "proposal-0.1",
      "manifestId": "stable replay-manifest identity",
      "subjectRef": "evaluation or recommendation reference",
      "createdAt": "RFC3339 instant",
      "scope": {
        "tenantId": "tenant reference",
        "siteId": "site reference"
      },
      "period": {
        "start": "RFC3339 instant",
        "end": "RFC3339 instant",
        "timeZone": "IANA timezone",
        "clockPolicyRef": "immutable clock/boundary policy"
      },
      "inputs": [
        {
          "kind": "TELEMETRY_EVENT | MAPPING_SNAPSHOT | GRAPH_SNAPSHOT | CONTRACT_VERSION | TARIFF_PACKAGE | POLICY | FORECAST | OPTIMIZER_INPUT",
          "immutableRef": "content-addressed or immutable versioned reference",
          "contentDigest": "digest value or null while digest scheme is undecided",
          "schemaVersion": "input contract version"
        }
      ],
      "evaluator": {
        "name": "evaluator identity",
        "version": "semantic version",
        "buildRef": "immutable build/container/source reference"
      },
      "optimizer": {
        "name": "optimizer identity or null",
        "version": "model/build version or null",
        "seed": "explicit seed or null"
      },
      "policies": {
        "qualityPolicyRef": "immutable quality policy",
        "aggregationPolicyRef": "fixed boundary and aggregation policy",
        "settlementPolicyRef": "immutable settlement policy"
      },
      "expectedOutput": {
        "resultRef": "immutable result reference",
        "semanticDigest": "digest of canonical semantic output or null"
      },
      "evidenceRefs": ["evidence record references"],
      "manifestStatus": "REPLAYABLE | INCOMPLETE | INVALIDATED"
    }

### Replay rules

- All references must resolve to immutable content/version identities. Mutable aliases such as “current tariff” are insufficient.
- Inputs are canonicalized and ordered deterministically before replay. The canonicalization rule must be versioned and generated from the shared contract definition.
- Timestamps preserve event time, receipt time and evaluation period separately. Trace/correlation IDs and wall-clock processing timestamps do not enter the semantic output digest.
- If any required input, build, mapping, rule or policy is missing, mark INCOMPLETE and list the missing reference; never substitute its latest version.
- If source data or a rule is intentionally corrected, create a new manifest/evaluation with a link to the superseded evaluation; do not mutate the historical manifest.
- Replay compares business-semantic output, not byte-for-byte transport envelopes. The semantic equality definition must specify decimal normalization, collection ordering and excluded operational metadata.
- Hash/digest algorithm, signature, immutable storage, retention and correction policy require separate architecture/security decisions. This proposal does not make a cryptographic or storage decision.
- VS-001 replay is an analytical replay. It is not the Edge command replay/idempotency record required by D-075 and does not prove exactly-once field writes.

## 4. Missing source identity and contract gaps

The current TelemetryEventV1 has no producer event ID or idempotency key. Before a durable replay manifest can refer unambiguously to a source event, a subsequent contract decision must define event identity and duplicate semantics. It must not overload trace IDs (D-073).

The current EvidenceRecordV1 supports generic sourceRefs, derivation and notes but has no typed evaluation/manifest links, immutable storage reference, content digest or supersession relation. Candidate approaches include a separately versioned evaluation record or a backward-compatible extension; select only after contract ownership and migration policy are reviewed.

The current RecommendationV1 objective accepts numeric estimatedValue and lacks a typed CostEvaluationResult reference. Keep this incompatibility visible until a new version is approved.

Other unresolved details include:
- decimal grammar, normalization and scale/rounding policy;
- required component catalogue and aggregation semantics;
- clock, timezone and late-data/correction policy;
- content-addressing scheme and immutable retention;
- schema-authoring format and code generation pipeline under D-065;
- access control and redaction for source and replay data.

These are contract decisions. Do not code hidden defaults into an adapter.

## 5. Acceptance scenarios for a future contract implementation

These scenarios define evidence to collect after the proposal is approved; they have not been executed here:

1. Same pinned inputs and versions produce the same semantic evaluation result and evidence identity despite different trace IDs.
2. A missing tariff version, mapping snapshot or source payload yields INCOMPLETE/BLOCKED with no substitute-latest lookup.
3. An assumption-based input yields SCENARIO_ONLY and cannot be displayed as bill-grade.
4. An unresolved material settlement rule yields BLOCKED or an explicitly bounded non-bill-grade partial result.
5. Decimal serialization round-trips without binary-float drift and follows the referenced policy.
6. Event quality exclusion does not move the declared fixed aggregation boundary (D-074).
7. Replaying a superseded/corrected input creates a new evaluation and preserves the earlier result.
8. No analytical replay action can invoke the command/Edge path.
9. Contract-generated TypeScript and Go bindings, once the generator decision is made, conform to the same fixtures and semantic corpus (D-065).

## 6. Decision status and next work

This proposal closes no Gate, does not modify existing canonical contracts and is not implementation authorization. Review it against D-065 and the G6.9-R2 contract/bake-off process. Then:

1. decide whether the shapes and status vocabulary meet PR-04/PR-05/PR-07 and Energy OS accounting needs;
2. record a Decision Record and Open Question updates for accepted changes;
3. select the canonical contract authoring/generation path without choosing a production runtime by implication;
4. version canonical schemas and valid/invalid fixtures;
5. update VS-001 detailed design, implementation ports and acceptance evidence together;
6. keep bill-grade economics gated by G1 and controlled execution gated by G6/G7.
