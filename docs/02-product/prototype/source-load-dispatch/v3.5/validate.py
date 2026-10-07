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
assert len(fixture["baseline"]) == len(fixture["candidate"]) == 6
assert len(fixture["inputs"]["tasks"]) == 3
assert "HVAC comfort/thermal dynamics and rebound are not modeled." in fixture["limitations"]
assert "EV departure deadlines and hot-water temperature/service are not modeled." in fixture["limitations"]
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
assert measurements["screenshots_committed"] is False
print("v3.5 source/fixture checks passed: 6 aligned intervals; 3 resources; exact changed intervals; 3 localized NOT_ASSESSED displays; no command form.")
