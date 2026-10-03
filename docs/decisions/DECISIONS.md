# Decision Register

Stable project decisions. Do not silently overwrite; supersede with a new decision record when evidence changes.

## D-001 — Product category
**Decision:** Position as a Commercial Energy Operating System / Energy Orchestrator, not a generic EMS dashboard.  
**Status:** ACTIVE

## D-002 — Optimization objective
**Decision:** Optimize total economic energy cost/value, not minimum kWh.  
**Status:** ACTIVE

## D-003 — First controllable asset
**Decision:** HVAC/chiller plant is the first priority controllable asset for the initial Macau pilot. ESS is not the default first asset.  
**Status:** ACTIVE

## D-004 — Battery role
**Decision:** ESS is an optional fast-response and flexibility asset for TOU shifting, Pu clipping, resilience and control support; it must pass a site-specific economic case.  
**Status:** ACTIVE

## D-005 — PV dispatch
**Decision:** PV dispatch and accounting are determined by the customer's verified settlement contract. Do not hard-code “PV first self-consumption”.  
**Status:** ACTIVE

## D-006 — Demand Guard
**Decision:** Demand Guard is a hard control guard, not merely an optimizer penalty term. It may veto optimizer actions.  
**Status:** ACTIVE

## D-007 — LLM boundary
**Decision:** LLMs may support explanation, diagnostics and operator interaction but not safety-critical closed-loop control.  
**Status:** ACTIVE

## D-008 — Control path
**Decision:** Cloud optimization must not directly write to low-level plant controllers. Commands pass through site edge, policy and safety enforcement.  
**Status:** ACTIVE

## D-009 — MVP foundation
**Decision:** MVP foundation is Tariff/Contract Twin + Meter/Settlement Twin + Energy Graph + HVAC model + Shadow Mode + M&V.  
**Status:** ACTIVE

## D-010 — First pilot profile
**Decision:** Prefer a 1–5 MW C1/C2 non-gaming hotel or large commercial building with central chilled-water plant and existing BMS for the first pilot.  
**Status:** ACTIVE / HYPOTHESIS TO VALIDATE WITH GTM

## D-011 — Reactive optimization priority
**Decision:** Reactive-energy optimization is tariff-class dependent and may become high priority for C2/B2/B3 and D customers.  
**Status:** ACTIVE

## D-012 — Immutable tariff versions
**Decision:** Published tariff rule versions are immutable. Policy changes create a new version with a new effective period.  
**Status:** ACTIVE

## D-013 — Separate graphs
**Decision:** Physical/electrical topology and settlement/economic topology are modeled separately and linked explicitly.  
**Status:** ACTIVE

## D-014 — Building ontology baseline
**Decision:** Use a canonical building/asset model compatible with Brick-style semantics rather than a proprietary list of BMS point names. Any concrete library/version must be re-verified before implementation.  
**Status:** ACTIVE

## D-015 — Effective-date billing
**Decision:** Bill reconstruction must be effective-date aware; tariff/TCA changes inside a billing period are evaluated by timestamp, not quarter labels alone.  
**Status:** ACTIVE

## D-016 — Tariff engine architecture
**Decision:** Tariff Engine is a rule-execution system, not a flat tariff table.  
**Status:** ACTIVE

## D-017 — Historical rule preservation
**Decision:** Historical tariff/contract versions remain reproducible for historical bill reconstruction and M&V.  
**Status:** ACTIVE

## D-018 — One engine for history and future
**Decision:** Historical M&V and forward economic optimization use the same rule definitions, with only the input/forecast mode differing.  
**Status:** ACTIVE

## D-019 — Fail closed on unknown regulatory inputs
**Decision:** An unresolved rule may be simulated only when explicitly marked as PROJECT_ASSUMPTION; it may not be represented as exact production settlement.  
**Status:** ACTIVE

## D-020 — Asset price resolution
**Decision:** Assets never store a hard-coded electricity price. Marginal value is resolved via topology, meter, contract and tariff version.  
**Status:** ACTIVE

## D-021 — PV revenue accounting
**Decision:** PV settlement revenue is a separate settlement stream and must not be collapsed into generic negative building load.  
**Status:** ACTIVE

## D-022 — Typed deterministic tariff core
**Decision:** The settlement kernel uses typed deterministic evaluators plus a restricted declarative rule schema; arbitrary scripting/general-purpose rule execution is prohibited in production tariff rules.  
**Status:** ACTIVE

## D-023 — Parameters separated from formulas
**Decision:** Legal/economic constants are effective-dated parameters; evaluator/formula logic is versioned separately when the mechanism changes.  
**Status:** ACTIVE

## D-024 — Bitemporal rule identity
**Decision:** Tariff/contract rules model both valid/effective time and system/knowledge time to support current-knowledge reconstruction and decision-time replay.  
**Status:** ACTIVE

## D-025 — Pure evaluation, explicit state commit
**Decision:** Bill/scenario evaluation is non-mutating and returns proposed demand/contract state transitions; only explicit authorized commands commit state.  
**Status:** ACTIVE

## D-026 — Decimal and unit-safe settlement
**Decision:** Monetary truth uses decimal arithmetic and explicit physical/economic units. Binary floating-point is not used for final bill truth.  
**Status:** ACTIVE

## D-027 — Demand window is first-class
**Decision:** Pu/demand averaging policy is an explicit `DemandMeasurementPolicy`; meter sampling interval must never be treated as the settlement demand window unless verified.  
**Status:** ACTIVE

## D-028 — Exact evaluator plus optimizer compiler
**Decision:** Exact settlement and solver-friendly optimizer cost models are separate runtime representations generated from the same tariff rule package. Proposed schedules are re-evaluated by the exact settlement engine.  
**Status:** ACTIVE

## D-029 — Golden fixtures are version-controlled evidence
**Decision:** Synthetic regression fixtures and anonymized real Golden Bill fixtures are version-controlled separately and form a mandatory release gate for tariff rules.  
**Status:** ACTIVE

## D-030 — Initial tariff implementation stack
**Decision:** Use a pure Java 25 LTS `tariff-core`, Spring Boot 4.1.x as an API/runtime adapter, and PostgreSQL 18 for rule/contract/state/audit metadata. Avoid premature microservice/rule-engine/graph-database complexity.  
**Status:** ACTIVE

## D-031 — DMN boundary
**Decision:** DMN may be used later for readable eligibility/policy decisions, but is not the authoritative monetary settlement kernel.  
**Status:** ACTIVE

## D-032 — BOPTEST harness selection
**Decision:** Use BOPTEST v0.9.0 as the first building-control validation harness. Its existing buildings are engineering test cases, not Macau commercial/hotel ground truth.  
**Status:** ACTIVE

## D-033 — External Macau economics for BOPTEST
**Decision:** BOPTEST provides building physics/control interaction; Macau Tariff Engine provides settlement economics. BOPTEST native electricity-price scenarios/KPIs are not CEM settlement authority.  
**Status:** ACTIVE

## D-034 — Macau simulation weather source
**Decision:** Macau International Airport TMYx 2011–2025 may be used as an initial engineering simulation weather source, subject to later comparison/calibration with official or site measurements.  
**Status:** ACTIVE / ENGINEERING SOURCE

## D-035 — Gate numbering correction
**Decision:** “Reference Building Foundation” is renamed from the inconsistent `G2.0` label to `G7.0 — Reference Simulation Harness Foundation`; G2 remains Commercial Load Flexibility as defined in `RESEARCH-GATES.md`.  
**Status:** ACTIVE
## D-036 — Pin the reference harness
**Decision:** R0 pins BOPTEST v0.9.0/testcase artifacts and never benchmarks against an unpinned master branch.  
**Status:** ACTIVE

## D-037 — R0 does not become “Macau” by swapping weather
**Decision:** Keep official/native R0 weather for harness validation. R1 is a derived Macau case with weather plus equipment/control/humidity revalidation; a weather-only swap is not accepted as a Macau reference model.  
**Status:** ACTIVE

## D-038 — Runtime point introspection + reviewed mapping manifest
**Decision:** BOPTEST points are discovered from metadata and bound to canonical Energy Graph semantics by an explicit versioned manifest. Production semantics may not rely on point-name heuristics alone.  
**Status:** ACTIVE

## D-039 — Settle total site power, not BOPTEST HVAC KPI
**Decision:** Introduce SitePowerComposer; CEM economic evaluation uses the composed settlement-path power including non-HVAC load and later PV/EV/ESS flows.  
**Status:** ACTIVE

## D-040 — Control cadence is independent of demand settlement cadence
**Decision:** Communication step, optimizer grid and `DemandMeasurementPolicy` are separate first-class time scales. None may be inferred from another.  
**Status:** ACTIVE

## D-041 — Split Demand Guard
**Decision:** Separate always-available physical/site-capacity guard from settlement-demand guard. Settlement-demand guard is bill-grade only with verified `DemandMeasurementPolicy`; otherwise it is disabled or explicitly assumption-based.  
**Status:** ACTIVE

## D-042 — External CEM economics remain authoritative around BOPTEST
**Decision:** BOPTEST native price/cost KPIs are diagnostic/controller-benchmark signals only. Macau business economics are computed externally by the Macau Tariff Engine.  
**Status:** ACTIVE

## D-043 — R0 output is integration evidence, not Macau hotel ROI
**Decision:** No R0 office-case saving result may be marketed as a Macau hotel/customer ROI.  
**Status:** ACTIVE

## D-044 — Every reference run is manifest-addressable
**Decision:** Testcase version/hash, container digest, mapping, clock mode, seed, step, tariff hash, controller and guard versions are recorded for reproducibility.  
**Status:** ACTIVE



## D-045 — Exact R0 modeled-electric aggregation
**Decision:** For pinned BOPTEST v0.9.0 `multizone_office_complex_air`, R0 derives modeled HVAC electrical power from the exact 13 `ElectricPower` signals listed in the testcase `kpis.json`; no guessed aggregate point is used.  
**Status:** ACTIVE

## D-046 — R0-A supervisory-only control surface
**Decision:** Initial economic-control experiments enable only reviewed supervisory setpoints (three AHU supply-air-temperature setpoints and chilled-water supply-temperature setpoint). Direct fan/damper/coil/VAV overrides remain disabled until a later safety/control review.  
**Status:** ACTIVE

## D-047 — Release fixtures are preflight authority, not live-run substitute
**Decision:** Pinned BOPTEST v0.9.0 API regression fixtures may establish exact point metadata and adapter semantics for preflight, but G7.2 cannot close until two fresh live baseline runs and a live no-op identity trajectory are executed.  
**Status:** ACTIVE

## D-048 — R0 humidity evidence is partial
**Decision:** R0 may use outdoor humidity, AHU supply/return humidity and latent-gain forecasts, but may not claim zone/guestroom humidity-SLA validation because the pinned measurement surface has no zone relative-humidity measurement.  
**Status:** ACTIVE

## D-049 — Override activation is explicit
**Decision:** BOPTEST adapter commands must always treat the paired activation input as authoritative. A supplied override value with activation false is a no-op; omission/activation semantics are tested explicitly before optimization.  
**Status:** ACTIVE

## D-050 — Separate paired dispatch value from absolute site bill
**Decision:** For the linear C1 active-energy + TCA layer, paired baseline/candidate dispatch value may be evaluated directly from the changed modeled electric trajectory when all non-HVAC exogenous site loads are identical; absolute site cost still requires SitePowerComposer.  
**Status:** ACTIVE

## D-051 — R0 synthetic settlement clock pins to 2026 day-of-year
**Decision:** R0 maps BOPTEST simulation second-of-year to the same day-of-year in `Asia/Macau` calendar year 2026 for tariff/TCA replay. BOPTEST's own simulation weekday/calendar remains separate for internal-load schedules.  
**Status:** ACTIVE / PROJECT ASSUMPTION

## D-052 — R0 peak-cool economic window excludes warmup
**Decision:** For `peak_cool_day`, R0 economic/M&V replay begins at simulation day 177 and ends at day 191; the day-170..177 warmup is excluded.  
**Status:** ACTIVE

## D-053 — Economic replay splits price boundaries before trapezoidal integration
**Decision:** External energy replay preserves BOPTEST's trapezoidal physical integration convention but inserts tariff, TCA, season and contract boundaries first so no trapezoid spans two settlement prices.  
**Status:** ACTIVE

## D-054 — R0 non-HVAC profile is versioned model evidence, not Macau evidence
**Decision:** The official BOPTEST office lighting/plug densities and schedules may be used to build a synthetic R0 site-load profile for absolute-cost harness tests. It is always labeled PROJECT_ASSUMPTION and never treated as representative Macau hotel/commercial load.  
**Status:** ACTIVE

## D-055 — First R0 economic truth is energy + TCA only
**Decision:** R0 bill-grade economic replay initially enables only verified C1 active-energy TOU + effective-dated TCA. Pu/demand charge, reactive, commercial government tax, PV, ESS and EV settlement remain disabled/scenario-only until their respective evidence/model requirements are satisfied.  
**Status:** ACTIVE


## D-056 — Deterministic controller before MPC
**Decision:** R0 first executes a deterministic tariff-aware supervisory state machine (`TariffShaper v0`) before any MPC is promoted. Its purpose is to falsify naive TOU control, validate guard semantics and establish setpoint-response evidence.  
**Status:** ACTIVE


## D-057 — R0 first-controller control authority remains four supervisory setpoints
**Decision:** G7.4 retains the R0-A four-point surface: three AHU supply-air-temperature setpoints plus one chilled-water-supply-temperature setpoint. Zone thermostats and low-level fan/damper/valve/VAV overrides remain disabled.  
**Status:** ACTIVE


## D-058 — Comfort/IAQ boundaries come from dynamic testcase boundaries
**Decision:** R0 guard logic uses BOPTEST `LowerSetp`, `UpperSetp`, `UpperCO2` and measured zone state rather than inventing fixed hotel comfort/IAQ limits. R0 model values are never generalized to Macau customer SLA.  
**Status:** ACTIVE


## D-059 — Physical capacity guard stays separate from rebound diagnostic and Pu
**Decision:** Physical/site-capacity protection requires an explicit verified or scenario capacity threshold. `NO_NEW_PEAK` baseline comparison and 5/15/30/60-minute rolling peaks are diagnostic metrics only and are not CEM Pu.  
**Status:** ACTIVE


## D-060 — Recovery is a first-class control state
**Decision:** A tariff-shift controller must model post-peak recovery explicitly instead of immediately snapping all setpoints to baseline, because rebound may erase energy savings or create a new site peak.  
**Status:** ACTIVE


## D-061 — MPC receives no privileged control path
**Decision:** Future MPC proposals must pass through the same Policy/Safety Kernel, command activation semantics and audit path as `TariffShaper v0`.  
**Status:** ACTIVE

## D-062 — Three primary language ceiling for MVP
**Decision:** The default MVP architecture is constrained to TypeScript, Go and Python as the three primary implementation languages unless a customer/protocol requirement provides evidence for adding another. TypeScript owns product surfaces, Go is the provisional authoritative core/Edge language, and Python owns optimization/forecast/simulation.  
**Status:** ACTIVE / PROVISIONAL STACK DEFAULT


## D-063 — Bun is first-class, but not assumed compatible with Node-native authority paths
**Decision:** Pin Bun as the preferred TypeScript workspace/tooling and Candidate-A API runtime. Do not infer Node-native compatibility from Bun performance or general Node-compatibility claims. Temporal TypeScript Workers remain on authentic Node while that is the official support boundary.  
**Status:** ACTIVE


## D-064 — C+ is provisional default pending falsifiable bake-off
**Decision:** Use Go authoritative Energy Core + Temporal Go workers + Go Edge/Safety Kernel, with Bun/Hono/TypeScript on the product/BFF surface and Python for intelligence, as the provisional MVP default. It can be displaced only by the common bake-off decision rule.  
**Status:** ACTIVE / PROVISIONAL


## D-065 — Cross-language contracts are generated, not manually duplicated
**Decision:** Use versioned OpenAPI/Protobuf/JSON Schema contracts as the source of truth and generate Go/TypeScript bindings. A multi-language architecture may not rely on hand-maintained duplicate DTOs.  
**Status:** ACTIVE


## D-066 — Temporal, cloud events and site messaging have separate responsibilities
**Decision:** Temporal owns durable workflow state/outcome; NATS JetStream owns replayable cloud domain events; MQTT 5 owns resilient site/cloud messaging; PostgreSQL owns authoritative business/audit state. A broker is not used as a substitute workflow engine.  
**Status:** ACTIVE


## D-067 — Effect 4 adoption is selective until measured
**Decision:** Effect 4 participates in Candidate A for typed errors, dependencies, resource safety and structured concurrency, but is not made pervasive platform authority until the bake-off demonstrates lower total engineering cost without hidden/regression cost.  
**Status:** ACTIVE / EXPERIMENTAL BOUNDARY


## D-068 — Stack selection requires semantic and AI-engineering bake-off
**Decision:** Framework/runtime selection is made against one canonical Energy OS vertical slice, common hard safety/security gates and controlled Codex/Claude engineering trials. Hello-world throughput and vendor benchmarks cannot decide the stack.  
**Status:** ACTIVE


## D-069 — Suspend the Java-specific implementation portion of D-030
**Decision:** The semantic Tariff Engine architecture from G1.1/G1.2 remains active, but the Java 25 + Spring Boot implementation choice in D-030 is no longer production authority while G6.9-R2 is open. The tariff implementation language must follow the platform bake-off or a separately justified isolation boundary.  
**Status:** ACTIVE / SUPERSEDES D-030 IMPLEMENTATION STACK ONLY

## D-070 — Signed command values use canonical decimal text at the authority boundary
**Decision:** External cloud-to-Edge command setpoints are signed using canonical decimal text rather than runtime-native floating-point JSON formatting. Conversion to equipment numeric types happens only after signature/scope/time/replay checks.  
**Status:** ACTIVE


## D-071 — Protocol semantics precede framework choice
**Decision:** Command verification semantics and reason-code ordering are frozen independently of Hono/Nest/Go service frameworks. Candidate implementations must conform to the same corpus; framework convenience may not change authority semantics.  
**Status:** ACTIVE


## D-072 — Step-3B HMAC is a test fixture, not production key architecture
**Decision:** HMAC-SHA256 is used only to make cross-runtime conformance reproducible. Production Edge identity, signing algorithm, key provisioning/rotation and hardware-backed storage remain separate Safety Kernel security decisions.  
**Status:** ACTIVE



## D-073 — Observability identity cannot alter control/business identity
**Decision:** Correlation/trace IDs are propagation metadata only. They MUST NOT participate in deterministic proposal IDs, command IDs, tariff results, optimizer semantic identity or field-write idempotency keys.  
**Evidence:** Step 3C first run exposed cross-runtime proposal divergence caused solely by distinct correlation IDs; removing trace identity restored identical proposal/command identities.  
**Status:** ACTIVE


## D-074 — Aggregation window authority precedes quality filtering
**Decision:** Telemetry quality controls eligible samples but never defines or slides the fixed aggregation/settlement window. Time buckets are established from the declared clock/boundary policy first, then quality rules are applied.  
**Evidence:** Step 3C first run shifted a 15-minute bucket by 10 seconds when the boundary sample was `UNCERTAIN`; fixed-boundary logic restored deterministic Node/Go equality.  
**Status:** ACTIVE


## D-075 — Edge replay protection is a normal workflow-recovery boundary
**Decision:** If the cloud retries a command after the field write has succeeded but workflow completion was not committed, Edge replay state prevents another physical write. A replay/already-applied outcome is recoverable workflow evidence, not automatically an exceptional control failure.  
**Evidence:** Step 3C crash-after-field-write scenario completed with exactly one field write for both Node and Go semantic cloud paths.  
**Status:** ACTIVE


## D-076 — Step 3C is semantic evidence, not framework winner evidence
**Decision:** Node 22/stdlib and Go 1.23 local shell timings from Step 3C may prove shared semantics only. They MUST NOT be used to rank Bun/Hono/Effect, Node/Nest/Fastify or Go 1.27 production candidates. Comparative runtime/framework claims require the pinned Step-3D environment.  
**Status:** ACTIVE



## D-077 — Macau grid-connected PV injection and settlement boundary
**Decision:** For an approved customer PV installation, model public-grid interconnection as a regulated, metered process requiring the applicable project acceptance, CEM interconnection arrangement, connection-point meter and contract. CEM's published feed-in tariff is producer-side export settlement. Do not treat another building's injected PV kWh as a consuming customer's bill credit or procurement entitlement without separate verified legal, CEM, metering and contract evidence. Keep producer export revenue as a separate settlement stream unless an approved arrangement explicitly links the accounts.  
**Evidence:** CEM PV introduction, application procedure and feed-in-tariff pages reviewed 2026-10-03; see `docs/evidence/G1-PV-GRID-INTERCONNECTION-2026-10.md`.  
**Status:** ACTIVE for modeling boundary; U-025 remains open for cross-site rights.
