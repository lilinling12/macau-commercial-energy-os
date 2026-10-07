#!/usr/bin/env python3
"""Static fidelity guard for the v3.3 fixture-backed study prototype.

This validates local fixture consistency and the authored display boundary. It
does not validate browser behavior, tariff correctness, field feasibility, or
production runtime behavior.
"""
from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
fixture = json.loads((HERE / "dispatch-projection-fixture.json").read_text(encoding="utf-8"))
html = (HERE / "index.html").read_text(encoding="utf-8-sig")

assert fixture["fixture_status"] == "SYNTHETIC_SCENARIO_ONLY"
assert fixture["source"]["pr"] == 14
assert fixture["source"]["commit"] == "9b80adca9243a0ae9a7bd666f0efee1acfc6309a"
assert fixture["source"]["optimizer_blob"] == "2d3256801f0ddce6b849c648c160f5a32fd90a27"
assert fixture["source"]["assessment_blob"] == "534ae269a7949601bd4504271e0076369807a68f"
assert fixture["physical"]["status"] == "SCENARIO_ONLY"
assert fixture["economic"]["status"] == "BLOCKED"
assert fixture["economic"]["covered_intervals"] == []
assert fixture["economic"]["delta_mop"] is None

for name in ("baseline", "candidate"):
    rows = fixture[name]
    assert len(rows) == 6
    energy = Decimal("0")
    peak = Decimal("0")
    previous_end = None
    for row in rows:
        start, end = row["start"], row["end"]
        if previous_end is not None:
            assert start == previous_end, f"{name} intervals are not contiguous"
        previous_end = end
        hours = Decimal("1")
        grid, pv = Decimal(row["grid_import_kw"]), Decimal(row["pv_generation_kw"])
        used, export = Decimal(row["pv_used_kw"]), Decimal(row["pv_export_kw"])
        curtailed = Decimal(row["pv_curtailed_kw"])
        charge, discharge = Decimal(row["ess_charge_kw"]), Decimal(row["ess_discharge_kw"])
        flexible = sum((Decimal(x["power_kw"]) for x in row["flexible_loads"]), Decimal("0"))
        load = Decimal(row["base_load_kw"]) + flexible
        assert pv == used + export + curtailed, f"{name} PV partition mismatch"
        assert grid + used + discharge == load + charge + Decimal(row["losses_kw"]), f"{name} bus balance mismatch"
        energy += grid * hours
        peak = max(peak, grid)
    assert energy == Decimal(fixture["physical"][f"{name}_import_energy_kwh"])
    assert peak == Decimal(fixture["physical"][f"{name}_peak_grid_import_kw"])

assert len(re.findall(r"\bfetch\s*\(", html)) == 1
assert 'fetch("./dispatch-projection-fixture.json")' in html
assert 'claimViewMode="actual"' in html
assert 'claimViewMode==="partial-demo"' in html
assert 'fixtureData.claims' in html and 'fixtureData.baseline' in html and 'fixtureData.candidate' in html
assert "Display-state example; it is not output from the PR #14 fixture or optimizer." in html
assert "has no device-command path" in html
assert "não é saída do fixture nem do otimizador PR #14" in html
assert "不是 PR #14 夾具或優化器的輸出" in html
assert "Missing intervals are not treated as zero" in html
assert "未覆蓋時段不視為零" in html
assert "não são tratados como zero" in html
assert "09:00–13:00" in html and "13:00–15:00" in html
for claim in ("DEMAND_CHARGE", "EXPORT_COMPENSATION", "FULL_BILL", "SAVINGS", "CONTROLLABILITY", "COMFORT_SERVICE", "CROSS_SITE_CREDIT", "DEVICE_CONTROL"):
    assert any(x["claim"] == claim and x["status"] == "WITHHELD" and x["scope"] == "NONE" for x in fixture["claims"])

print("v3.3 fixture pins, interval balance, claim boundary, and local-only source passed.")
print("Scope: static synthetic fixture/source guard only; browser, service, site, and tariff validation are excluded.")
