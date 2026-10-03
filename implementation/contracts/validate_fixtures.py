from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent

CASES = (
    ("telemetry-event.v1.schema.json", "fixtures/telemetry-event.valid.json"),
    ("recommendation.v1.schema.json", "fixtures/recommendation.valid.json"),
    ("evidence-record.v1.schema.json", "fixtures/evidence-record.valid.json"),
)


def main() -> None:
    for schema_name, fixture_name in CASES:
        schema = json.loads((ROOT / schema_name).read_text(encoding="utf-8"))
        fixture = json.loads((ROOT / fixture_name).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema, format_checker=None).validate(fixture)
        print(f"validated: {fixture_name}")


if __name__ == "__main__":
    main()
