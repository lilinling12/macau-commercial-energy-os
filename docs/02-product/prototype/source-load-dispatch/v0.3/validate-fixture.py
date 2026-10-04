#!/usr/bin/env python3
"""Validate the synthetic dispatch example and its prototype table.

This standard-library-only check is a documentation/fixture verifier, not a
production dispatch engine, tariff evaluator, optimizer, or safety control.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FIXTURE_PATH = ROOT / "source-load-dispatch-fixture-v0.1.json"
HTML_PATH = ROOT / "macau-energy-os-dispatch-prototype-v0.3.html"


class DataTableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_target_container = False
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.rows: list[list[str]] = []
        self.row: list[str] = []
        self.cell: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        if tag == "div" and attrs_map.get("id") == "dataTable":
            self.in_target_container = True
        elif tag == "table" and self.in_target_container:
            self.in_table = True
        elif self.in_table and tag == "tr":
            self.in_row = True
            self.row = []
        elif self.in_table and self.in_row and tag in {"td", "th"}:
            self.in_cell = True
            self.cell = []

    def handle_data(self, data: str) -> None:
        if self.in_cell:
            self.cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.in_cell and tag in {"td", "th"}:
            self.row.append(" ".join("".join(self.cell).split()))
            self.in_cell = False
        elif self.in_row and tag == "tr":
            self.rows.append(self.row)
            self.in_row = False
        elif self.in_table and tag == "table":
            self.in_table = False


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def verify_fixture(fixture: dict) -> None:
    require(fixture["evidenceClass"] == "SYNTHETIC", "fixture must remain synthetic")
    require(fixture["assessmentClass"] == "SCENARIO_ONLY", "fixture is not field assessment")
    horizon = fixture["horizon"]
    require(horizon["settlementIntervalVerified"] is False, "settlement interval must remain unverified")
    require(horizon["intervalSeconds"] == 3600, "example must use declared one-hour intervals")
    policy = fixture["claimPolicy"]
    for key in (
        "billGradeCostEnabled",
        "savingsEnabled",
        "pvExportCreditEnabled",
        "crossSiteNettingEnabled",
        "deviceControlEnabled",
    ):
        require(policy[key] is False, f"unsupported claim/control must remain disabled: {key}")

    intervals = fixture["intervals"]
    require(len(intervals) == 6, "12:00–18:00 horizon must contain six intervals")
    previous_end = None
    hvac_deltas = []
    for index, interval in enumerate(intervals):
        start = datetime.fromisoformat(interval["start"])
        end = datetime.fromisoformat(interval["end"])
        require(start.utcoffset() == end.utcoffset(), f"offset changes within interval {index}")
        require(start.utcoffset().total_seconds() == 8 * 3600, "Macau example must use +08:00")
        require((end - start).total_seconds() == horizon["intervalSeconds"], f"wrong interval duration {index}")
        if previous_end is not None:
            require(start == previous_end, f"gap or overlap before interval {index}")
        previous_end = end

        baseline = interval["baseline"]
        candidate = interval["candidate"]
        for name, row in (("baseline", baseline), ("candidate", candidate)):
            require(
                row["nonHvacLoadKw"] + row["hvacLoadKw"] == row["siteLoadKw"],
                f"{name} end-use loads do not sum at interval {index}",
            )
            require(
                row["gridImportKw"] + row["pvUsedKw"] + row["essDischargeKw"] == row["siteLoadKw"],
                f"{name} source/load balance fails at interval {index}",
            )
        hvac_deltas.append(candidate["hvacLoadKw"] - baseline["hvacLoadKw"])

    require(datetime.fromisoformat(intervals[0]["start"]) == datetime.fromisoformat(horizon["start"]), "horizon start mismatch")
    require(datetime.fromisoformat(intervals[-1]["end"]) == datetime.fromisoformat(horizon["end"]), "horizon end mismatch")
    require(hvac_deltas == [0, 0, 0, -30, 0, 30], "HVAC shift/rebound must be explicit and interval-aligned")
    require(sum(hvac_deltas) == 0, "illustrative HVAC shift must not fabricate net load reduction")
    require(all(i["candidate"]["essDischargeKw"] == 0 for i in intervals if i["start"].startswith("2026-10-04T16:")), "unexpected ESS discharge at 16:00")


def verify_prototype_matches_fixture(fixture: dict) -> None:
    html = HTML_PATH.read_text(encoding="utf-8")
    parser = DataTableParser()
    parser.feed(html)
    data_rows = [row for row in parser.rows if row and row[0].count(":") == 2 and "–" in row[0]]
    require(len(data_rows) == len(fixture["intervals"]), "prototype data table must show all six intervals")
    for row, interval in zip(data_rows, fixture["intervals"], strict=True):
        start = datetime.fromisoformat(interval["start"]).strftime("%H:%M")
        end = datetime.fromisoformat(interval["end"]).strftime("%H:%M")
        baseline = interval["baseline"]
        candidate = interval["candidate"]
        expected = [
            f"{start}–{end}",
            str(baseline["gridImportKw"]),
            str(candidate["gridImportKw"]),
            str(candidate["pvUsedKw"]),
            str(candidate["essDischargeKw"]),
            str(baseline["siteLoadKw"]),
            str(candidate["siteLoadKw"]),
        ]
        require(row[:7] == expected, f"prototype table does not match fixture at {start}")
        expected_hvac = candidate["hvacLoadKw"] - baseline["hvacLoadKw"]
        hvac_cell = row[7].replace("−", "-")
        if expected_hvac == 0:
            require(hvac_cell == "0", f"unexpected HVAC change at {start}")
        elif expected_hvac < 0:
            require(hvac_cell.startswith(str(expected_hvac)), f"HVAC shift mismatch at {start}")
        else:
            require(hvac_cell.startswith(f"+{expected_hvac}"), f"HVAC rebound mismatch at {start}")
        balance = row[8].replace(" ", "")
        ess_term = f"+{candidate['essDischargeKw']}" if candidate["essDischargeKw"] else ""
        expected_balance = (
            f"{candidate['gridImportKw']}+{candidate['pvUsedKw']}"
            f"{ess_term}={candidate['siteLoadKw']}"
        )
        require(balance == expected_balance, f"displayed power balance mismatch at {start}")

    require("viewBox=\"0 0 860 340\"" in html, "prototype chart SVG should include the ESS annotation lane")
    require("H198 V74" in html and "H702 V88" in html, "prototype series should use interval step geometry")
    require("18:00 · 結束" in html, "18:00 must be labelled as the horizon boundary")
    require("不建模 ESS 充電、SOC、效率或損耗" in html, "prototype must disclose omitted storage physics")


def main() -> int:
    try:
        fixture = read_fixture()
        verify_fixture(fixture)
        verify_prototype_matches_fixture(fixture)
    except (AssertionError, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: 6 synthetic intervals, source/load balance, HVAC shift/rebound, claim limits, and prototype table alignment.")
    print("LIMIT: This is a static illustrative fixture check; it does not validate a site, tariff, optimizer, device capability, or control path.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
