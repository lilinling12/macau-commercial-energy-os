"""Generate the pinned synthetic dispatch projection from this optimizer source.

Run from implementation/optimizer:
  python tools/generate_dispatch_projection_fixture.py --write
  python tools/generate_dispatch_projection_fixture.py --check

The source SHA-1 fingerprints intentionally fail closed when either engine module
changes. Update the source pins only after reviewing the regenerated projection.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

SOURCE_COMMIT = "e02ed268c23d9cd62f2641db05923befa88ed281"
SOURCE_BLOBS = {
    "src/macau_energy_optimizer/dispatch_optimizer.py": "2d3256801f0ddce6b849c648c160f5a32fd90a27",
    "src/macau_energy_optimizer/dispatch_assessment.py": "275a1cd79613cf1997456916f1b59833fb683109",
}
FIXTURE_PATH = ROOT / "fixtures" / "dispatch-projection-synthetic-v1.json"


def verify_source_pins() -> None:
    for relative, expected in SOURCE_BLOBS.items():
        data = (ROOT / relative).read_bytes()
        header = f"blob {len(data)}\0".encode("ascii")
        actual = hashlib.sha1(header + data).hexdigest()
        if actual != expected:
            raise SystemExit(f"source pin mismatch for {relative}: expected {expected}, got {actual}")


verify_source_pins()

from datetime import datetime, timedelta
from decimal import Decimal as D
from zoneinfo import ZoneInfo

from macau_energy_optimizer.dispatch_assessment import (
    EconomicContext, EssLimits, EvidenceRef, EvidenceState, FlexibleLoadFlow,
    FlexibleLoadKind, ImportEnergyRate, Schedule, ScheduleInterval,
)
from macau_energy_optimizer.dispatch_optimizer import (
    DispatchSearchRequest, FlexibleEnergyTask, generate_candidate,
)

TZ = ZoneInfo("Asia/Macau")
START = datetime(2026, 10, 8, 9, 0, tzinfo=TZ)
ASSUMED = EvidenceRef("fixture:synthetic-scenario-v1", EvidenceState.PROJECT_ASSUMPTION)
tasks = (
    FlexibleEnergyTask("hvac-task", FlexibleLoadKind.HVAC, D("2"), (True,) * 6, D("1"), D("2"), ASSUMED),
    FlexibleEnergyTask("ev-task", FlexibleLoadKind.EV, D("1"), (True,) * 6, D("1"), D("1"), ASSUMED),
    FlexibleEnergyTask("hot-water-task", FlexibleLoadKind.HOT_WATER, D("1"), (True,) * 6, D("1"), D("1"), ASSUMED),
)
base = [D("8")] * 6
pv = [D("0"), D("0"), D("2"), D("4"), D("2"), D("0")]
flows = [
    (),
    (),
    (),
    (),
    (FlexibleLoadFlow("hvac-task", FlexibleLoadKind.HVAC, D("1")), FlexibleLoadFlow("hot-water-task", FlexibleLoadKind.HOT_WATER, D("1"))),
    (FlexibleLoadFlow("hvac-task", FlexibleLoadKind.HVAC, D("1")), FlexibleLoadFlow("ev-task", FlexibleLoadKind.EV, D("1"))),
]
rates = (D("0.50"), D("0.50"), D("0.50"), D("0.90"), D("1.50"), D("1.50"))
rows = []
for i in range(6):
    start = START + timedelta(hours=i)
    end = start + timedelta(hours=1)
    load = base[i] + sum((x.power_kw for x in flows[i]), D("0"))
    pv_used = min(pv[i], load)
    grid = max(D("0"), load - pv[i])
    rows.append(ScheduleInterval(start, end, grid, pv[i], pv_used, D("0"), pv[i] - pv_used,
                                 D("0"), D("0"), base[i], flows[i], D("0"), D("5"), D("5")))
baseline = Schedule(tuple(rows))
import_rates = tuple(ImportEnergyRate(row.start, row.end, rates[i], ASSUMED) for i, row in enumerate(rows))
context = EconomicContext(ASSUMED, ASSUMED, ASSUMED, import_rates)
ess = EssLimits(D("1"), D("1"), D("0"), D("10"), D("1"), D("1"), ASSUMED)
request = DispatchSearchRequest(
    "tenant-synthetic", "site-synthetic", "Asia/Macau", baseline, tasks, (), (ASSUMED,),
    context, D("1"), D("1"), ess, D("5"), None, None, 100000, 1000000, ASSUMED, ASSUMED,
)
result = generate_candidate(request)


def dec(value):
    return str(value) if value is not None else None


def dt(value):
    return value.isoformat() if value is not None else None


def schedule(value):
    output = []
    for row in value.intervals:
        output.append({
            "start": dt(row.start), "end": dt(row.end), "grid_import_kw": dec(row.grid_import_kw),
            "pv_generation_kw": dec(row.pv_generation_kw), "pv_used_kw": dec(row.pv_used_kw),
            "pv_export_kw": dec(row.pv_export_kw), "pv_curtailed_kw": dec(row.pv_curtailed_kw),
            "ess_charge_kw": dec(row.ess_charge_kw), "ess_discharge_kw": dec(row.ess_discharge_kw),
            "ess_soc_start_kwh": dec(row.ess_soc_start_kwh), "ess_soc_end_kwh": dec(row.ess_soc_end_kwh),
            "base_load_kw": dec(row.base_load_kw),
            "flexible_loads": [
                {"asset_id": flow.asset_id, "kind": flow.kind.value, "power_kw": dec(flow.power_kw)}
                for flow in row.flexible_loads
            ],
            "losses_kw": dec(row.losses_kw),
        })
    return output


assessment = result.assessment
payload = {
    "fixture_id": "pr14-exact-head-generated-synthetic-dispatch-v1",
    "fixture_status": "SYNTHETIC_SCENARIO_ONLY",
    "source": {
        "repository": "lilinling12/macau-commercial-energy-os",
        "pr": 14,
        "commit": SOURCE_COMMIT,
        "optimizer_blob": SOURCE_BLOBS["src/macau_energy_optimizer/dispatch_optimizer.py"],
        "assessment_blob": SOURCE_BLOBS["src/macau_energy_optimizer/dispatch_assessment.py"],
    },
    "scope": "Six one-hour intervals, fixed PV/base load, three aggregate service-energy tasks, simple ESS, import-energy component objective only.",
    "limitations": [
        "Every evidence reference is PROJECT_ASSUMPTION.",
        "HVAC comfort/thermal dynamics and rebound are not modeled.",
        "EV departure deadlines and hot-water temperature/service are not modeled.",
        "This fixture does not establish Macau tariff applicability, real site topology, savings, export compensation, or equipment control.",
        "The exact discrete result is only optimal within the declared 1 kW/1 kWh action grid and bounded horizon.",
    ],
    "inputs": {
        "site_timezone": "Asia/Macau",
        "planning_window_start": dt(rows[0].start),
        "planning_window_end_exclusive": dt(rows[-1].end),
        "interval_seconds": 3600,
        "power_step_kw": "1",
        "soc_step_kwh": "1",
        "initial_soc_kwh": "5",
        "terminal_soc_policy": "equal to baseline end SOC",
        "pv_generation_kw": [dec(value) for value in pv],
        "base_load_kw": [dec(value) for value in base],
        "import_rates_mop_per_kwh": [dec(value) for value in rates],
        "tasks": [
            {
                "asset_id": task.asset_id, "kind": task.kind.value,
                "required_energy_kwh": dec(task.required_energy_kwh),
                "min_on_power_kw": dec(task.min_on_power_kw), "max_power_kw": dec(task.max_power_kw),
                "availability": [bool(value) for value in task.available_intervals],
            }
            for task in tasks
        ],
    },
    "search": {
        "scope": result.search_scope, "transitions_examined": result.transitions_examined,
        "scenario_only": result.scenario_only,
    },
    "physical": {
        "status": assessment.physical_status.value, "claim_scope": assessment.claim_scope.value,
        "reasons": list(assessment.reasons),
        "baseline_import_energy_kwh": dec(assessment.baseline_import_energy_kwh),
        "candidate_import_energy_kwh": dec(assessment.candidate_import_energy_kwh),
        "baseline_peak_grid_import_kw": dec(assessment.baseline_peak_grid_import_kw),
        "candidate_peak_grid_import_kw": dec(assessment.candidate_peak_grid_import_kw),
    },
    "economic": {
        "status": assessment.economic_status.value, "component": assessment.economic_component,
        "baseline_import_energy_charge_mop": dec(assessment.baseline_import_energy_charge_mop),
        "candidate_import_energy_charge_mop": dec(assessment.candidate_import_energy_charge_mop),
        "delta_mop": dec(assessment.import_energy_charge_delta_mop),
        "covered_intervals": [[dt(start), dt(end)] for start, end in assessment.economic_covered_intervals],
        "interval_count": assessment.economic_total_interval_count,
    },
    "claims": [
        {"claim": claim.claim.value, "status": claim.status.value, "scope": claim.scope.value,
         "reasons": list(claim.reasons), "subject": claim.subject}
        for claim in assessment.claim_readiness
    ],
    "baseline": schedule(baseline),
    "candidate": schedule(result.candidate),
}
rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"

parser = argparse.ArgumentParser()
parser.add_argument("--write", action="store_true", help="write the checked fixture to its repository path")
parser.add_argument("--check", action="store_true", help="compare generated bytes with the committed fixture")
args = parser.parse_args()
if args.write:
    FIXTURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    FIXTURE_PATH.write_text(rendered, encoding="utf-8", newline="\n")
elif args.check:
    if not FIXTURE_PATH.is_file() or FIXTURE_PATH.read_text(encoding="utf-8") != rendered:
        raise SystemExit("committed dispatch projection fixture differs; regenerate and review it")
else:
    sys.stdout.write(rendered)
