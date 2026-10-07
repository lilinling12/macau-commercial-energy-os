#!/usr/bin/env python3
"""Static source/fixture checks for the v3.5 service-coverage presentation study."""

import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
fixture = json.loads((ROOT / "dispatch-projection-fixture.json").read_text(encoding="utf-8"))
html = (ROOT / "index.html").read_text(encoding="utf-8")
measurements = json.loads((ROOT / "measurements.json").read_text(encoding="utf-8"))

assert fixture["fixture_status"] == "SYNTHETIC_SCENARIO_ONLY"
assert fixture["source"] == {
    "repository": "lilinling12/macau-commercial-energy-os",
    "pr": 14,
    "commit": "e02ed268c23d9cd62f2641db05923befa88ed281",
    "optimizer_blob": "2d3256801f0ddce6b849c648c160f5a32fd90a27",
    "assessment_blob": "275a1cd79613cf1997456916f1b59833fb683109",
}
assert len(fixture["baseline"]) == len(fixture["candidate"]) == 6
assert len(fixture["inputs"]["tasks"]) == 3
assert "HVAC comfort/thermal dynamics and rebound are not modeled." in fixture["limitations"]
assert "EV departure deadlines and hot-water temperature/service are not modeled." in fixture["limitations"]

# Protect the bounded result projection actually consumed by the prototype.
# These checks do not establish an API contract or a Macau site outcome.
assert fixture["physical"]["status"] == "SCENARIO_ONLY"
assert fixture["economic"]["status"] == "BLOCKED"
assert fixture["economic"]["baseline_import_energy_charge_mop"] is None
assert fixture["economic"]["candidate_import_energy_charge_mop"] is None
assert fixture["economic"]["delta_mop"] is None
assert fixture["economic"]["covered_intervals"] == []
claim_rows = fixture["claims"]
claim_by_name = {row["claim"]: row for row in claim_rows}
assert claim_by_name["GRID_IMPORT_PROFILE"]["status"] == "ALLOWED"
assert claim_by_name["GRID_IMPORT_PROFILE"]["scope"] == "SCENARIO_ONLY"
assert claim_by_name["DISPATCH_FEASIBILITY"]["status"] == "WITHHELD"
assert claim_by_name["GRID_IMPORT_ENERGY_COMPONENT"]["status"] == "WITHHELD"
for name in ("DEMAND_CHARGE", "EXPORT_COMPENSATION", "FULL_BILL", "SAVINGS",
             "CONTROLLABILITY", "COMFORT_SERVICE", "CROSS_SITE_CREDIT", "DEVICE_CONTROL"):
    assert claim_by_name[name]["status"] == "WITHHELD", name
    assert claim_by_name[name]["scope"] == "NONE", name
for rows in (fixture["baseline"], fixture["candidate"]):
    for previous, current in zip(rows, rows[1:]):
        assert datetime.fromisoformat(previous["end"]) == datetime.fromisoformat(current["start"])

def by_resource(rows):
    output = {}
    for row in rows:
        for load in row.get("flexible_loads", []):
            output.setdefault(load["asset_id"], {})[row["start"]] = float(load["power_kw"])
    return output

base = by_resource(fixture["baseline"])
candidate = by_resource(fixture["candidate"])
expected = {
    "hvac-task": ["11:00", "13:00", "14:00"],
    "ev-task": ["11:00", "14:00"],
    "hot-water-task": ["11:00", "13:00"],
}
actual = {}
for task in fixture["inputs"]["tasks"]:
    asset_id = task["asset_id"]
    changed = []
    for interval in fixture["candidate"]:
        start = interval["start"]
        if abs(base.get(asset_id, {}).get(start, 0.0) - candidate.get(asset_id, {}).get(start, 0.0)) > 1e-9:
            changed.append(start[11:16])
    actual[asset_id] = changed
assert actual == expected, actual

for required in (
    'function resultMetrics(t)',
    'fixtureData.physical',
    'fixtureData.economic',
    'function renderFixtureClaims(t)',
    'fixtureData.claims.filter',
    'c.status==="ALLOWED"?actual.allowed:actual.withheld',
    'function renderServiceOutcomes(t)',
    'out+=renderServiceOutcomes(t);',
    'aria-labelledby="serviceReviewTitle"',
    "interval.start+'–'+interval.end",
    'Not assessed',
    '暫未評估',
    'Não avaliado',
    'Synthetic schedule example.',
    'Exemplo de horário sintético.',
    'Service and recovery windows are not assessed.',
    'DEVICE_CONTROL',
    'v3.5',
):
    assert required in html, required

assert 'data-command=' not in html and 'type="submit"' not in html
assert measurements["matrix_cases"] == len(measurements["viewports_css_px"]) * len(measurements["locales"]) == 15
assert measurements["result"]["document_level_horizontal_overflow"] is False
assert measurements["result"]["three_changed_resource_rows_present_in_every_case"] is True
assert measurements["screenshots_committed"] is True
assert [item["path"] for item in measurements["screenshot_artifacts"]] == [
    "evidence/stage4-zh-Hant-1440.png",
    "evidence/stage4-pt-375.png",
]
assert measurements["screenshot_artifacts"][0]["css_viewport"] == {"width": 1440, "height": 900}
assert measurements["screenshot_artifacts"][1]["css_viewport"] == {"width": 375, "height": 800}
print("v3.5 source/fixture checks passed: 6 aligned intervals; 3 resources; exact changed intervals; 3 localized NOT_ASSESSED displays; no command form.")
