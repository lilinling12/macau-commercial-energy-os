#!/usr/bin/env python3
"""Build a deterministic, noncanonical APP-11 UI projection study artifact."""

import argparse
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE_PATH = ROOT / "dispatch-projection-fixture.json"
OUTPUT_PATH = ROOT / "app11-ui-projection.json"


def build_projection(source: dict) -> dict:
    baseline = source["baseline"]
    candidate = source["candidate"]
    tasks = source["inputs"]["tasks"]
    if len(baseline) != len(candidate):
        raise ValueError("baseline and candidate interval counts differ")

    task_by_id = {task["asset_id"]: task for task in tasks}
    changed: dict[str, list[dict[str, str]]] = {}
    for base_row, candidate_row in zip(baseline, candidate, strict=True):
        if (base_row["start"], base_row["end"]) != (
            candidate_row["start"], candidate_row["end"]
        ):
            raise ValueError("baseline and candidate intervals are not aligned")
        base_loads = {
            item["asset_id"]: Decimal(item["power_kw"])
            for item in base_row.get("flexible_loads", [])
        }
        candidate_loads = {
            item["asset_id"]: Decimal(item["power_kw"])
            for item in candidate_row.get("flexible_loads", [])
        }
        for asset_id in sorted(set(base_loads) | set(candidate_loads)):
            if asset_id not in task_by_id:
                raise ValueError(f"schedule references unknown task: {asset_id}")
            if base_loads.get(asset_id, Decimal(0)) != candidate_loads.get(
                asset_id, Decimal(0)
            ):
                changed.setdefault(asset_id, []).append(
                    {"start": candidate_row["start"], "end": candidate_row["end"]}
                )

    resource_services = [
        {
            "asset_id": task["asset_id"],
            "kind": task["kind"],
            "outcome": "NOT_ASSESSED",
            "outcome_basis": "NO_SERVICE_EVALUATOR_IN_SOURCE_FIXTURE",
            "changed_intervals": changed[task["asset_id"]],
        }
        for task in tasks
        if task["asset_id"] in changed
    ]

    return {
        "projection_id": "app11-ui-projection-study-v0.1",
        "projection_status": "NONCANONICAL_STATIC_UI_VIEW_MODEL",
        "contract_status": "STUDY_ONLY_NOT_APPROVED",
        "generated_from": {
            "path": SOURCE_PATH.name,
            "fixture_id": source["fixture_id"],
            "source": source["source"],
        },
        "source_result": source,
        "resource_services": resource_services,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if the committed projection differs from deterministic output",
    )
    args = parser.parse_args()

    source = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    expected = build_projection(source)
    if args.check:
        try:
            current = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            current = None
        if current != expected:
            raise SystemExit("APP-11 UI projection is stale; regenerate it from the pinned fixture")
        print("APP-11 noncanonical UI projection matches deterministic source mapping")
    else:
        encoded = json.dumps(expected, ensure_ascii=False, indent=2) + "\n"
        OUTPUT_PATH.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"Wrote {OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()

