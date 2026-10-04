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
FIXTURE_PATH = ROOT / "fixtures" / "synthetic-dispatch.json"
HTML_PATH = ROOT / "index.html"


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
    baseline_peak_kw = max(row["baseline"]["gridImportKw"] for row in intervals)
    candidate_peak = max(intervals, key=lambda row: row["candidate"]["gridImportKw"])
    require(baseline_peak_kw == 485, "baseline grid-import horizon peak must be 485 kW")
    require(candidate_peak["candidate"]["gridImportKw"] == 510, "candidate rebound must set a 510 kW horizon peak")
    require(candidate_peak["start"].startswith("2026-10-04T17:00:00"), "candidate grid-import peak must occur during rebound")
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
    require("全時段最大電網輸入 · 基線 → 候選" in html, "prototype must label the horizon peak comparison")
    require("485 → 510 kW" in html and "回彈時段 +25 kW" in html, "prototype must disclose the rebound-driven peak increase")
    require("候選尖峰電網輸入" not in html, "prototype must not mislabel the 430 kW interval as the horizon peak")
    require("id=\"reviewBtn\"" in html and "重新載入後重設" in html, "review state must be visibly page-only")

    require('<a class="skip-link" href="#mainContent">跳至主要內容</a>' in html, "keyboard users must have a skip link")
    require('id="mainContent" tabindex="-1"' in html, "skip link must target the main region")
    require('class="content focus-baseline"' in html and 'classList.toggle("focus-candidate",isCandidate)' in html, "scenario selection must visibly emphasize the chosen curve")
    require('id="comparisonFocus" class="small" aria-live="polite"' in html, "scenario change must announce its focus")
    require(".railnav button{width:44px;height:44px}" in html, "narrow navigation target must meet 44px minimum")


    flow_ids = ("evidence-check", "site-model", "dispatchComparison", "constraint-analysis", "shadow-review", "outcome-replay")
    for flow_id in flow_ids:
        require(f'id="{flow_id}"' in html, f"missing workflow stage: {flow_id}")
        require(f'href="#{flow_id}"' in html, f"missing workflow navigation link: {flow_id}")
    require('aria-label="調度工作流程"' in html, "workflow navigation must have an accessible label")
    require("未提供證據，經濟輸出阻擋" in html, "workflow must keep economic readiness blocked")
    require("預測、外部操作和量測結果分開記錄" in html, "workflow must separate outcomes and replay")



def main() -> int:
    try:
        fixture = read_fixture()
        verify_fixture(fixture)
        verify_prototype_matches_fixture(fixture)
    except (AssertionError, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: 6 synthetic intervals, source/load balance, HVAC shift/rebound, horizon peak disclosure, claim limits, and prototype table/review alignment.")
    print("LIMIT: This is a static illustrative fixture check; it does not validate a site, tariff, optimizer, device capability, or control path.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
