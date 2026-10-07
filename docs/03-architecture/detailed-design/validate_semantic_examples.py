#!/usr/bin/env python3
"""Validate T7.1 schema-neutral semantic examples; not a wire-schema validator."""
import json
import pathlib
import sys

path = pathlib.Path(__file__).with_name("semantic-examples.v0.1.json")
data = json.loads(path.read_text(encoding="utf-8"))
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

check(data.get("artifact_status") == "STUDY_ONLY_NOT_WIRE_CONTRACT", "artifact must remain explicitly study-only")
check(data.get("canonical_contract") is False, "canonical contract must remain false")
check(data.get("control_authorized") is False, "device control must remain unauthorized")
cases = {case.get("id"): case for case in data.get("cases", [])}
required = {"T71-01-synthetic-service-not-assessed", "T71-02-partial-rate-presentation-only", "T71-03-stale-resource-evidence", "T71-04-unknown-core-evidence", "T71-05-operational-failure", "T71-06-known-hard-bound-violation"}
check(set(cases) == required, "case set must contain exactly the six reviewed semantic cases")
for case_id, case in cases.items():
    check(case.get("source_relation"), f"{case_id}: source relation is required")
    check(case.get("lifecycle") is not None, f"{case_id}: lifecycle axis is required")
    for claim in case.get("claims", []):
        check(claim.get("disposition") in {"ALLOWED", "WITHHELD"}, f"{case_id}: invalid claim disposition")
        check(claim.get("disposition") != "PARTIAL", f"{case_id}: PARTIAL is not a claim disposition")
        check(claim.get("amount") is None, f"{case_id}: this corpus must not invent monetary amounts")
    for service in case.get("services", []):
        check(service.get("status") in {"NOT_ASSESSED", "UNKNOWN", "PARTIAL", "WITHIN_DECLARED_PROFILE", "VIOLATION"}, f"{case_id}: unsupported proposed service status")
partial = cases["T71-02-partial-rate-presentation-only"]
econ = partial["economic"]
check(econ["status"] == "PARTIAL", "partial-rate case must retain partial evaluation scope")
check(len(econ["covered_interval_ids"]) == 4 and len(econ["uncovered_interval_ids"]) == 2, "partial-rate coverage must be exact 4/6")
check(econ["amount"] is None and econ["currency"] is None, "presentation-only partial case must not show an amount")
component = next((c for c in partial["claims"] if c["id"] == "grid_import_energy_component"), {})
check(component.get("disposition") == "ALLOWED" and component.get("scope_interval_ids") == econ["covered_interval_ids"], "allowed component must match exact covered interval set")
check(all(c["disposition"] == "WITHHELD" for c in partial["claims"] if c["id"] in {"full_bill", "savings", "demand_charge", "export_compensation"}), "broader financial claims must remain withheld")
stale = cases["T71-03-stale-resource-evidence"]
check(stale["physical"]["status"] == "PARTIAL", "resource-scoped stale example must not be request-wide infeasible")
check(stale["services"][0]["status"] == "UNKNOWN" and stale["services"][0]["hard_bound_breach_evidenced"] is False, "stale evidence must not become a service violation")
check(cases["T71-04-unknown-core-evidence"]["physical"]["status"] == "BLOCKED", "unknown core evidence must be blocked")
check(cases["T71-04-unknown-core-evidence"]["physical"]["metrics"] is None, "blocked core evidence must not expose invented metrics")
failure = cases["T71-05-operational-failure"]
check(failure["lifecycle"]["state"] == "FAILED" and failure["physical"] is None and failure["economic"] is None, "operational failure must not fabricate assessment dimensions")
violation = cases["T71-06-known-hard-bound-violation"]["services"][0]
check(violation["status"] == "VIOLATION" and violation["hard_bound_breach_evidenced"] is True, "VIOLATION requires an evidenced hard-bound breach")
if errors:
    print("\n".join(f"FAIL: {error}" for error in errors))
    sys.exit(1)
print(f"PASS: {len(cases)} T7.1 semantic examples; fail-closed money, claim, evidence, service, failure, and scope assertions")
