#!/usr/bin/env python3
"""Static semantic guard for the v2.9 synthetic SHADOW projection.

This validates the pinned fixture and its authored UI boundary. It is not a
browser test, runtime API contract test, accessibility audit, or site validation.
"""
from __future__ import annotations

import json
from datetime import datetime
from decimal import Decimal
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
HTML_PATH = HERE / "index.html"
FIXTURE_PATH = HERE / "dispatch-projection-fixture.json"
EXPECTED_SOURCE = {
    "commit": "9b80adca9243a0ae9a7bd666f0efee1acfc6309a",
    "optimizer_blob": "2d3256801f0ddce6b849c648c160f5a32fd90a27",
    "assessment_blob": "534ae269a7949601bd4504271e0076369807a68f",
}
PROHIBITED_CLAIMS = {
    "DEMAND_CHARGE",
    "EXPORT_COMPENSATION",
    "FULL_BILL",
    "SAVINGS",
    "CONTROLLABILITY",
    "COMFORT_SERVICE",
    "CROSS_SITE_CREDIT",
    "DEVICE_CONTROL",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"dispatch projection validation failed: {message}")


data = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
html = HTML_PATH.read_text(encoding="utf-8")
require(data.get("fixture_status") == "SYNTHETIC_SCENARIO_ONLY", "fixture must remain synthetic")
require(data.get("source", {}).get("commit") == EXPECTED_SOURCE["commit"], "engine commit pin changed")
for key in ("optimizer_blob", "assessment_blob"):
    require(data["source"].get(key) == EXPECTED_SOURCE[key], f"source blob pin changed: {key}")

physical = data["physical"]
economic = data["economic"]
require(physical.get("status") == "SCENARIO_ONLY", "physical result must remain scenario-only")
require(economic.get("status") == "BLOCKED", "unverified economic context must remain blocked")
for key in (
    "baseline_import_energy_charge_mop",
    "candidate_import_energy_charge_mop",
    "delta_mop",
):
    require(economic.get(key) is None, f"blocked monetary value must be null: {key}")
require(economic.get("covered_intervals") == [], "assumption-tagged rates must not be priced")
require(physical.get("baseline_import_energy_kwh") == "44.0", "baseline energy changed")
require(physical.get("candidate_import_energy_kwh") == "44.0", "candidate energy changed")
require(physical.get("baseline_peak_grid_import_kw") == "10", "baseline horizon peak changed")
require(physical.get("candidate_peak_grid_import_kw") == "11", "candidate horizon peak changed")

claims = {item["claim"]: item for item in data["claims"]}
for name in PROHIBITED_CLAIMS:
    claim = claims.get(name)
    require(claim is not None, f"missing explicit withheld claim: {name}")
    require(claim.get("status") == "WITHHELD" and claim.get("scope") == "NONE",
            f"prohibited claim must remain withheld: {name}")
    require(bool(claim.get("reasons")), f"withheld claim needs an explanation: {name}")

def validate_schedule(name: str) -> None:
    rows = data[name]
    require(len(rows) == 6, f"{name} must contain six intervals")
    previous_end = None
    total_kwh = Decimal("0")
    peak = Decimal("0")
    for index, row in enumerate(rows):
        start = datetime.fromisoformat(row["start"])
        end = datetime.fromisoformat(row["end"])
        require(start.tzinfo is not None and end.tzinfo is not None, f"{name}[{index}] needs timezone")
        require(end > start, f"{name}[{index}] must be a positive interval")
        require(previous_end is None or start == previous_end, f"{name}[{index}] is not contiguous")
        previous_end = end
        hours = Decimal(str((end - start).total_seconds())) / Decimal("3600")
        grid = Decimal(row["grid_import_kw"])
        pv = Decimal(row["pv_generation_kw"])
        pv_used = Decimal(row["pv_used_kw"])
        export = Decimal(row["pv_export_kw"])
        curtailed = Decimal(row["pv_curtailed_kw"])
        charge = Decimal(row["ess_charge_kw"])
        discharge = Decimal(row["ess_discharge_kw"])
        losses = Decimal(row["losses_kw"])
        load = Decimal(row["base_load_kw"]) + sum(
            (Decimal(item["power_kw"]) for item in row["flexible_loads"]), Decimal("0")
        )
        require(pv == pv_used + export + curtailed, f"{name}[{index}] PV partition does not balance")
        require(grid + pv_used + discharge == load + charge + losses,
                f"{name}[{index}] site-bus balance does not reconcile")
        total_kwh += grid * hours
        peak = max(peak, grid)
    expected_energy = Decimal(physical["baseline_import_energy_kwh"] if name == "baseline"
                              else physical["candidate_import_energy_kwh"])
    expected_peak = Decimal(physical["baseline_peak_grid_import_kw"] if name == "baseline"
                             else physical["candidate_peak_grid_import_kw"])
    require(total_kwh == expected_energy, f"{name} intervals disagree with reported horizon energy")
    require(peak == expected_peak, f"{name} intervals disagree with reported horizon peak")

validate_schedule("baseline")
validate_schedule("candidate")

require('fetch("./dispatch-projection-fixture.json")' in html,
        "page must load the pinned local fixture")
fetches = re.findall(r"\bfetch\s*\(", html)
require(len(fetches) == 1, "prototype should have only the local fixture fetch, not a service call")
for locale_copy in (
    "not an economic optimum under an applicable Macau contract",
    "No equipment command path",
    "not saved, sent to a service or connected to field actions",
    "這不是澳門適用電價下的經濟最優結論",
    "沒有設備指令路徑",
    "不會保存、提交服務或觸發現場動作",
    "não é um ótimo económico segundo um contrato aplicável em Macau",
    "Sem via de comando para equipamentos",
    "Não são guardadas, enviadas a um serviço nem ligadas a ações no local",
):
    require(locale_copy in html, f"missing localized scope disclosure: {locale_copy}")

# The separate partial-coverage UI state is a presentation contract example,
# not a claim emitted by this pinned blocked projection or optimizer fixture.
require('value="partial-demo"' in html, "partial-coverage presentation state must be selectable")
require('claimViewMode==="partial-demo"' in html, "partial state must use an explicit display-only branch")
require("claimDemoBanner:" in html, "every locale must disclose that the partial state is a UI example")
require("partialImportScope:" in html and "4 / 6" in html, "partial scope must state the exact covered interval count")
require("wholeWindowScope:" in html and "savingsReason:" in html and "demandReason:" in html,
        "whole-window bill, savings, and demand-charge claims must remain independently withheld")
require("uncovered intervals must not be treated as zero" in html,
        "English copy must explain uncovered-interval handling")
require("不得把未覆蓋時段當作零" in html,
        "Traditional Chinese copy must explain uncovered-interval handling")
require("não podem ser tratados como zero" in html,
        "Portuguese draft copy must explain uncovered-interval handling")
require('data-i18n="claimModeLegend"' in html and 'querySelectorAll("[data-i18n]")' in html,
        "new state controls must participate in locale switching")
print("v2.9 projection semantics and source pins passed (static fixture/source guard only).")
