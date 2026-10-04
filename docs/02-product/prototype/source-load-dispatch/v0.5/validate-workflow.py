#!/usr/bin/env python3
"""Check synthetic interval, battery SOC and UI data alignment.

This is a static scenario consistency checker, not a site model, optimizer,
settlement calculator, safety case, or equipment-control test.
"""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FIXTURE = ROOT / "fixtures" / "synthetic-dispatch.json"
HTML = ROOT / "index.html"


class TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.active = False
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.rows: list[list[str]] = []
        self.row: list[str] = []
        self.cell: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        if tag == "div" and attrs_map.get("id") == "dataTable":
            self.active = True
        elif self.active and tag == "table":
            self.in_table = True
        elif self.in_table and tag == "tr":
            self.in_row, self.row = True, []
        elif self.in_row and tag in {"td", "th"}:
            self.in_cell, self.cell = True, []

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


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def close(actual: float, expected: float, message: str, tol: float = 1e-5) -> None:
    require(math.isclose(actual, expected, rel_tol=0, abs_tol=tol), f"{message}: {actual} != {expected}")


def display_number(value: float) -> str:
    return f"{value:g}"


def main() -> int:
    try:
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        html = HTML.read_text(encoding="utf-8")
        require(fixture["evidenceClass"] == "SYNTHETIC", "fixture must remain synthetic")
        require(fixture["assessmentClass"] == "SCENARIO_ONLY", "must remain scenario-only")
        policy = fixture["claimPolicy"]
        for flag in ("billGradeCostEnabled", "savingsEnabled", "pvExportCreditEnabled", "crossSiteNettingEnabled", "deviceControlEnabled"):
            require(policy[flag] is False, f"unsupported claim/control enabled: {flag}")

        assets = fixture["assets"]
        ess = assets["ess"]
        hvac = assets["hvac"]
        intervals = fixture["intervals"]
        require(len(intervals) == 6, "expected six one-hour intervals")
        require(ess["evidenceClass"] == "SYNTHETIC_UNVERIFIED_SITE_CAPABILITY", "ESS must not read as field evidence")
        require(hvac["comfortModel"] == "NOT_MODELLED", "do not imply thermal comfort validation")
        previous_end = None
        previous_soc = ess["initialSocKwh"]
        hvac_delta = []
        for index, interval in enumerate(intervals):
            start = datetime.fromisoformat(interval["start"])
            end = datetime.fromisoformat(interval["end"])
            require(start.utcoffset().total_seconds() == 8 * 3600, "timezone must be Macau +08:00")
            require((end - start).total_seconds() == fixture["horizon"]["intervalSeconds"], f"interval duration mismatch {index}")
            require(previous_end is None or start == previous_end, f"interval gap/overlap {index}")
            previous_end = end
            base, cand = interval["baseline"], interval["candidate"]
            for label, row in (("baseline", base), ("candidate", cand)):
                close(row["nonHvacLoadKw"] + row["hvacLoadKw"], row["siteLoadKw"], f"{label} end-use balance {index}")
                close(row["gridImportKw"] + row["pvUsedKw"] + row["essDischargeKw"], row["siteLoadKw"] + row["essChargeKw"], f"{label} physical balance {index}")
            close(cand["essSocStartKwh"], previous_soc, f"SOC continuity at interval {index}")
            interval_hours = (end - start).total_seconds() / 3600
            expected_soc = cand["essSocStartKwh"] + cand["essChargeKw"] * interval_hours * ess["chargeEfficiency"] - cand["essDischargeKw"] * interval_hours / ess["dischargeEfficiency"]
            close(cand["essSocEndKwh"], expected_soc, f"SOC integration {index}")
            require(ess["minimumSocKwh"] <= cand["essSocEndKwh"] <= ess["maximumSocKwh"] <= ess["capacityKwh"], f"SOC limit violation {index}")
            require(cand["essChargeKw"] <= ess["maximumChargeKw"], f"charge rating exceeded {index}")
            require(cand["essDischargeKw"] <= ess["maximumDischargeKw"], f"discharge rating exceeded {index}")
            require(hvac["illustrativePowerBoundsKw"]["minimum"] <= cand["hvacLoadKw"] <= hvac["illustrativePowerBoundsKw"]["maximum"], f"illustrative HVAC power bound exceeded {index}")
            previous_soc = cand["essSocEndKwh"]
            hvac_delta.append(cand["hvacLoadKw"] - base["hvacLoadKw"])

        require(hvac_delta == [0, 0, 0, -30, 0, 30] and sum(hvac_delta) == 0, "HVAC shift/rebound must preserve synthetic horizon energy")
        close(previous_soc, ess["initialSocKwh"], "ESS cycle must restore initial SOC")
        close(intervals[4]["candidate"]["gridImportKw"], 509.691358, "battery recharge import")
        baseline_peak = max(i["baseline"]["gridImportKw"] for i in intervals)
        candidate_peak = max(i["candidate"]["gridImportKw"] for i in intervals)
        close(baseline_peak, 485, "baseline horizon peak")
        close(candidate_peak, 510, "candidate horizon peak")

        parser = TableParser()
        parser.feed(html)
        data_rows = [row for row in parser.rows if row and row[0].count(":") == 2 and "–" in row[0]]
        require(len(data_rows) == 6, "prototype table must expose all intervals")
        for row, interval in zip(data_rows, intervals, strict=True):
            b, c = interval["baseline"], interval["candidate"]
            expected_prefix = [
                f"{interval['start'][11:16]}–{interval['end'][11:16]}", str(b["gridImportKw"]),
                display_number(c["gridImportKw"]), str(c["pvUsedKw"]), str(c["essDischargeKw"]),
                display_number(c["essChargeKw"]),
                f"{display_number(c['essSocStartKwh'])} → {display_number(c['essSocEndKwh'])}",
                str(b["siteLoadKw"]), str(c["siteLoadKw"]),
            ]
            require(row[:9] == expected_prefix, f"prototype table mismatch at {interval['start']}")

        for fragment in (
            "ESS 充電 候選", "SOC 候選 kWh", "24.691", "17.7778", "509.691",
            "ESS 充放電與 SOC", "設備控制未啟用", "預測、外部操作和量測結果分開記錄",
            "Dispatch workflow study v0.5", '<div class="railend">v0.5</div>',
        ):
            require(fragment in html, f"prototype missing required text/data: {fragment}")
        require('id="evidence-check"' in html and 'id="site-model"' in html and 'id="dispatchComparison"' in html, "six-stage workflow anchors must remain")
        require("viewBox=\"0 0 860 365\"" in html, "ESS annotation lane must have adequate SVG canvas")
        print("PASS: six hourly balances; HVAC shift/rebound; ESS power, SOC continuity, 90% charge/discharge efficiency and limits; table values; economic/control claim boundary; six-stage workflow.")
        print("LIMIT: synthetic arithmetic and source alignment only; not site capability, thermal comfort, tariff/settlement, forecast, optimization, visual/accessibility, or user-validation evidence.")
    except (AssertionError, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


