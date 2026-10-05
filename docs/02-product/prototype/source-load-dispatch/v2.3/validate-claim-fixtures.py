#!/usr/bin/env python3
"""Verify v2.3 synthetic UI fixtures preserve separate claim decision/scope.

This is a source/fixture consistency guard, not an optimizer, API, browser,
tariff, site, or device-control acceptance test.
"""
from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML_PATH = ROOT / "index.html"
FIXTURE_PATH = ROOT / "fixtures" / "mixed-claim-states.json"
EXPECTED_CASES = {"partial", "no-tariff", "missing-map", "service-violation"}
DIMENSION_STATES = {
    "physical": {"COMPLETE", "PARTIAL", "BLOCKED", "INFEASIBLE", "FAILED"},
    "hvacService": {"NOT_ASSESSED", "PASS", "VIOLATION", "UNKNOWN", "WITHHELD"},
    "essCapability": {"ALLOWED", "WITHHELD", "UNKNOWN"},
    "economic": {"NOT_CALCULATED", "COMPLETE", "PARTIAL", "BLOCKED", "FAILED"},
}
DECISIONS = {"ALLOWED", "WITHHELD"}
SCOPES = {"VERIFIED_BOUNDED", "SCENARIO_ONLY", "PARTIAL", "NONE"}


class EmbeddedFixtureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.capture = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "script" and dict(attrs).get("id") == "claim-fixtures":
            self.capture = True

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self.capture:
            self.capture = False


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_fixtures() -> dict:
    external = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    parser = EmbeddedFixtureParser()
    parser.feed(HTML_PATH.read_text(encoding="utf-8"))
    embedded_text = "".join(parser.parts)
    require(bool(embedded_text), "HTML is missing embedded claim fixtures")
    require(json.loads(embedded_text) == external, "embedded fixture differs from standalone JSON")
    return external


def verify(fixture: dict) -> None:
    meta = fixture["meta"]
    require(meta["evidenceClass"] == "SYNTHETIC", "fixtures must remain synthetic")
    require(meta["siteValidated"] is False, "fixtures must not imply site validation")
    require(meta["apiConnected"] is False, "fixtures must remain disconnected from API")
    require(meta["deviceControlEnabled"] is False, "device control must remain disabled")
    require(meta["resultOrigin"] == "SYNTHETIC_SUPPLIED_SCHEDULE_ASSESSMENT",
            "fixtures must be identified as supplied schedule assessments")
    cases = fixture["cases"]
    ids = [case["id"] for case in cases]
    require(len(ids) == len(set(ids)), "case IDs must be unique")
    require(set(ids) == EXPECTED_CASES, "expected four documented cases")

    for case in cases:
        require(set(case["dimensions"]) == set(DIMENSION_STATES),
                f"{case['id']}: dimension set mismatch")
        claims = case["claims"]
        claim_ids = [claim["id"] for claim in claims]
        require(len(claim_ids) == len(set(claim_ids)), f"{case['id']}: claim IDs must be unique")
        require("device_control" in claim_ids, f"{case['id']}: control decision is required")
        for name, dimension in case["dimensions"].items():
            require(dimension["status"] in DIMENSION_STATES[name],
                    f"{case['id']}: invalid {name} status")
            require(bool(dimension["detail"].strip()), f"{case['id']}: missing {name} reason")
        for claim in claims:
            require(claim["decision"] in DECISIONS, f"{case['id']}: invalid claim decision")
            require(claim["scope"] in SCOPES, f"{case['id']}: invalid claim scope")
            require(claim["tone"] in {"allowed", "partial", "withheld"},
                    f"{case['id']}: invalid text/color treatment")
            require(bool(claim["reason"].strip()), f"{case['id']}: claim reason is required")
            if claim["decision"] == "WITHHELD":
                require(claim["scope"] == "NONE",
                        f"{case['id']}: withheld claim must have NONE scope")
            else:
                require(claim["scope"] != "NONE",
                        f"{case['id']}: allowed claim needs an explicit scope")
            if claim["id"] == "device_control":
                require(claim["decision"] == "WITHHELD" and claim["scope"] == "NONE",
                        f"{case['id']}: device control must always be withheld")

    indexed = {case["id"]: case for case in cases}
    partial = indexed["partial"]
    require(partial["dimensions"]["economic"]["status"] == "PARTIAL",
            "partial-rate assessment must remain separate from claim decision")
    require("4 / 6" in partial["dimensions"]["economic"]["detail"],
            "partial-rate coverage must be explicit")
    partial_claim = next(c for c in partial["claims"] if c["id"] == "import_energy_component")
    require(partial_claim["decision"] == "ALLOWED" and partial_claim["scope"] == "PARTIAL",
            "partial component is an allowed claim with partial scope, not a third decision")
    require(partial_claim["tone"] == "partial", "partial coverage needs distinct visible styling")

    no_tariff = indexed["no-tariff"]
    require(no_tariff["dimensions"]["economic"]["status"] == "NOT_CALCULATED",
            "absent tariff context must not become zero cost")
    require("不生成優化候選" in no_tariff["summary"],
            "tariff-free supplied assessment must not imply optimizer candidate generation")
    no_tariff_claims = {c["id"]: c for c in no_tariff["claims"]}
    for claim_id in ("bill_cost", "savings"):
        require(no_tariff_claims[claim_id]["decision"] == "WITHHELD",
                f"no-tariff case must withhold {claim_id}")

    blocked = indexed["missing-map"]
    require(blocked["dimensions"]["physical"]["status"] == "BLOCKED",
            "unresolved core mapping must block physical scope")
    require(blocked["dimensions"]["economic"]["status"] == "BLOCKED",
            "unresolved core mapping must block dependent settlement")
    require(all(c["decision"] == "WITHHELD" for c in blocked["claims"]),
            "blocked mapping must withhold dependent claims")

    violated = indexed["service-violation"]
    require(violated["dimensions"]["hvacService"]["status"] == "VIOLATION",
            "synthetic service violation must remain visible")
    violated_claims = {c["id"]: c for c in violated["claims"]}
    require(violated_claims["service_feasibility"]["decision"] == "WITHHELD",
            "electrical balance cannot override service violation")
    require(violated_claims["overall_feasibility"]["decision"] == "WITHHELD",
            "overall feasibility must remain withheld")

    html = HTML_PATH.read_text(encoding="utf-8")
    for case_id in EXPECTED_CASES:
        require(f'data-case="{case_id}"' in html, f"missing selector for {case_id}")
    require("claim.decision" in html and "claim.scope" in html,
            "UI must render decision separately from claim scope")
    require('id="claimSummary" role="status" aria-live="polite" aria-atomic="true"' in html,
            "one contextual atomic status announcement is required")
    require("prefers-reduced-motion:reduce" in html, "reduced motion support is required")
    print("PASS: embedded and standalone JSON fixtures are identical")
    print("PASS: 4 synthetic scenarios preserve claim decision/scope and no-control boundaries")


if __name__ == "__main__":
    verify(load_fixtures())
