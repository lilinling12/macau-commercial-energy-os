#!/usr/bin/env python3
"""Check v2.3 synthetic claim fixtures and their embedded prototype copy.

This is a source/fixture consistency guard, not an optimizer, tariff evaluator,
API contract test, browser test, site validation, or control-safety certification.
"""
from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML_PATH = ROOT / "index.html"
FIXTURE_PATH = ROOT / "fixtures" / "mixed-claim-states.json"
ALLOWED_DIMENSION_STATES = {
    "physical": {"COMPLETE", "PARTIAL", "BLOCKED", "INFEASIBLE", "FAILED"},
    "hvacService": {"NOT_ASSESSED", "PASS", "VIOLATION", "UNKNOWN", "WITHHELD"},
    "essCapability": {"ALLOWED", "WITHHELD", "UNKNOWN"},
    "economic": {"NOT_CALCULATED", "COMPLETE", "PARTIAL", "BLOCKED", "FAILED"},
}
ALLOWED_CLAIM_STATES = {"ALLOWED", "PARTIAL", "WITHHELD"}
EXPECTED_CASES = {"partial", "no-tariff", "missing-map", "service-violation"}


class FixtureScriptParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.capture = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        if tag == "script" and attrs_map.get("id") == "claim-fixtures":
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


def load_fixture() -> dict:
    external = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    parser = FixtureScriptParser()
    parser.feed(HTML_PATH.read_text(encoding="utf-8"))
    embedded_text = "".join(parser.parts)
    require(bool(embedded_text), "HTML is missing embedded claim fixtures")
    embedded = json.loads(embedded_text)
    require(embedded == external, "embedded fixture differs from versioned JSON file")
    return external


def verify(fixture: dict) -> None:
    meta = fixture["meta"]
    require(meta["evidenceClass"] == "SYNTHETIC", "fixtures must be synthetic")
    require(meta["siteValidated"] is False, "fixtures must not imply site validation")
    require(meta["apiConnected"] is False, "prototype must remain unconnected to an API")
    require(meta["deviceControlEnabled"] is False, "fixture must never enable device control")
    require(meta["locale"] == "zh-Hant", "record the current prototype locale accurately")

    cases = fixture["cases"]
    ids = [case["id"] for case in cases]
    require(len(ids) == len(set(ids)), "case IDs must be unique")
    require(set(ids) == EXPECTED_CASES, "expected four documented mixed-state cases")

    for case in cases:
        dimensions = case["dimensions"]
        require(set(dimensions) == set(ALLOWED_DIMENSION_STATES), f"{case['id']}: dimension set mismatch")
        claims = case["claims"]
        claim_ids = [claim["id"] for claim in claims]
        require(len(claim_ids) == len(set(claim_ids)), f"{case['id']}: claim IDs must be unique")
        require("device_control" in claim_ids, f"{case['id']}: device-control disposition is required")
        for name, dimension in dimensions.items():
            require(dimension["status"] in ALLOWED_DIMENSION_STATES[name], f"{case['id']}: invalid {name} state")
            require(bool(dimension["detail"].strip()), f"{case['id']}: {name} needs a reason")
        for claim in claims:
            require(claim["status"] in ALLOWED_CLAIM_STATES, f"{case['id']}: invalid claim state")
            require(claim["tone"] in {"allowed", "partial", "withheld"}, f"{case['id']}: invalid non-color tone")
            require(bool(claim["reason"].strip()), f"{case['id']}: claim reason is required")
            if claim["id"] == "device_control":
                require(claim["status"] == "WITHHELD", f"{case['id']}: device control must stay withheld")

    indexed = {case["id"]: case for case in cases}
    partial = indexed["partial"]
    require(partial["dimensions"]["economic"]["status"] == "PARTIAL", "partial-rate example must remain PARTIAL")
    require("4 / 6" in partial["dimensions"]["economic"]["detail"], "partial-rate coverage must be explicit")
    require(not any("MOP" in claim["label"] or "金額" in claim["label"] for claim in partial["claims"]),
            "partial-rate example must not invent/display an amount")

    no_tariff = indexed["no-tariff"]
    require(no_tariff["dimensions"]["economic"]["status"] == "NOT_CALCULATED",
            "missing tariff context must not become a zero-cost result")
    no_tariff_claims = {claim["id"]: claim for claim in no_tariff["claims"]}
    for claim_id in ("bill_cost", "savings"):
        require(no_tariff_claims[claim_id]["status"] == "WITHHELD",
                f"no-tariff case must withhold {claim_id}")

    blocked = indexed["missing-map"]
    require(blocked["dimensions"]["physical"]["status"] == "BLOCKED",
            "unresolved core mapping must block the affected physical scope")
    require(blocked["dimensions"]["economic"]["status"] == "BLOCKED",
            "unresolved core mapping must block dependent settlement")
    require(all(claim["status"] == "WITHHELD" for claim in blocked["claims"]),
            "missing-map case must not expose dependent numeric/feasibility claims")

    violated = indexed["service-violation"]
    require(violated["dimensions"]["hvacService"]["status"] == "VIOLATION",
            "synthetic service violation must remain visible")
    violated_claims = {claim["id"]: claim for claim in violated["claims"]}
    require(violated_claims["service_feasibility"]["status"] == "WITHHELD",
            "electrical balance cannot override service violation")
    require(violated_claims["overall_feasibility"]["status"] == "WITHHELD",
            "overall feasibility must stay withheld when service fails")

    html = HTML_PATH.read_text(encoding="utf-8")
    for case_id in EXPECTED_CASES:
        require(f'data-case="{case_id}"' in html, f"missing selector for {case_id}")
    require('id="claimSummary" role="status" aria-live="polite" aria-atomic="true"' in html,
            "use one contextual atomic polite status announcement")
    require("prefers-reduced-motion:reduce" in html, "reduced-motion rule is required")
    print(f"PASS: {len(cases)} synthetic mixed-state fixtures match the embedded prototype data")
    print("PASS: core mapping, missing tariff, partial rate, service violation, and no-control boundaries")


if __name__ == "__main__":
    verify(load_fixture())
