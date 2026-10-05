#!/usr/bin/env python3
"""Validate catalog integrity and report locale coverage for the v1.9 study.

The candidate catalog is not runtime localization. By default this command
reports incomplete coverage without failing, so an unresolved owner decision
does not block unrelated prototype work. Pass --require-complete when a
review or release gate must require every candidate message to be translated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

CJK = re.compile(r"[\u3400-\u9fff]")
PLACEHOLDERS = re.compile(r"\{\{?([\w.-]+)\}?\}|%(?:\d+\$)?[sdif]")
WORKFLOW_STAGES = {
    "evidence-check",
    "site-model",
    "dispatchComparison",
    "constraint-analysis",
    "shadow-review",
    "outcome-replay",
}


def git_blob_sha(raw: bytes) -> str:
    header = b"blob " + str(len(raw)).encode("ascii") + b"\0"
    return hashlib.sha1(header + raw).hexdigest()


def placeholder_set(value: str) -> Counter[str]:
    return Counter(PLACEHOLDERS.findall(value))


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def inspect(catalog: dict[str, Any], source_path: Path) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    source = catalog.get("source")
    if not isinstance(source, dict) or not isinstance(source.get("blob"), str):
        errors.append("Catalog is missing source.blob.")
    else:
        actual = git_blob_sha(source_path.read_bytes())
        if actual != source["blob"]:
            errors.append(f"Source blob mismatch: catalog={source['blob']} actual={actual}.")

    locales = catalog.get("candidateLocales")
    if not isinstance(locales, list) or not all(isinstance(item, str) for item in locales):
        errors.append("candidateLocales must be a list of locale strings.")
        locales = []
    target_locales = [locale for locale in locales if locale != catalog.get("sourceLocale")]

    messages = catalog.get("messages")
    if not isinstance(messages, list):
        errors.append("messages must be a list.")
        messages = []

    seen_keys: set[str] = set()
    seen_units: set[tuple[str, str, str]] = set()
    stage_counts: Counter[str] = Counter()
    locale_counts: dict[str, Counter[str]] = {locale: Counter() for locale in target_locales}
    missing_by_stage: dict[str, Counter[str]] = {
        locale: Counter() for locale in target_locales
    }
    for index, message in enumerate(messages):
        if not isinstance(message, dict):
            errors.append(f"messages[{index}] must be an object.")
            continue
        key, stage, channel, original = (
            message.get("key"), message.get("stage"), message.get("channel"), message.get("sourceText")
        )
        if not all(isinstance(item, str) and item.strip() for item in (key, stage, channel, original)):
            errors.append(f"messages[{index}] needs non-empty key, stage, channel and sourceText.")
            continue
        if key in seen_keys:
            errors.append(f"Duplicate message key: {key}.")
        seen_keys.add(key)
        identity = (stage, channel, original)
        if identity in seen_units:
            errors.append(f"Duplicate stage/channel/source unit: {key}.")
        seen_units.add(identity)
        stage_counts[stage] += 1

        translations = message.get("translations")
        if not isinstance(translations, dict):
            errors.append(f"{key}: translations must be an object.")
            translations = {}
        for locale in target_locales:
            translated = translations.get(locale)
            if not isinstance(translated, str) or not translated.strip():
                missing_by_stage[locale][stage] += 1
                continue
            if CJK.search(translated):
                errors.append(f"{key} [{locale}]: translation still contains CJK text.")
            if placeholder_set(original) != placeholder_set(translated):
                errors.append(f"{key} [{locale}]: placeholder set differs from source.")
            locale_counts[locale][stage] += 1

    total = len(messages)
    report = {
        "catalogVersion": catalog.get("catalogVersion"),
        "catalogStatus": catalog.get("status"),
        "localeApproval": catalog.get("localeApproval"),
        "sourceLocale": catalog.get("sourceLocale"),
        "sourceBlob": source.get("blob") if isinstance(source, dict) else None,
        "messageUnits": total,
        "workflowStages": len(WORKFLOW_STAGES),
        "stageCounts": dict(sorted(stage_counts.items())),
        "locales": {
            locale: {
                "translated": sum(locale_counts[locale].values()),
                "total": total,
                "coveragePercent": round(100 * sum(locale_counts[locale].values()) / total, 1) if total else 100.0,
                "translatedByStage": dict(sorted(locale_counts[locale].items())),
                "missingByStage": dict(sorted(missing_by_stage[locale].items())),
            }
            for locale in target_locales
        },
        "errors": errors,
    }
    return errors, report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path, help="Review-candidate locale catalog JSON")
    parser.add_argument("source", type=Path, help="Exact HTML source referenced by source.blob")
    parser.add_argument("--require-complete", action="store_true", help="Exit 2 if any candidate locale has missing units")
    parser.add_argument("--list-missing", action="store_true", help="Print missing message keys by locale")
    parser.add_argument("--json", action="store_true", help="Emit a machine-readable report")
    args = parser.parse_args()

    try:
        catalog = read_json(args.catalog)
        errors, report = inspect(catalog, args.source)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"INPUT ERROR: {exc}", file=sys.stderr)
        return 1

    incomplete = any(data["translated"] != data["total"] for data in report["locales"].values())
    report["coverageComplete"] = not incomplete
    report["coverageGate"] = "FAIL" if args.require_complete and incomplete else (
        "PASS" if args.require_complete else "NOT_REQUESTED"
    )
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Catalog {report['catalogVersion']} · {report['catalogStatus']}")
        print(f"Source blob: {report['sourceBlob']}")
        print(f"Message units: {report['messageUnits']} across 6 workflow stages plus shell and interaction messages")
        for locale, data in report["locales"].items():
            print(f"{locale}: {data['translated']}/{data['total']} translated ({data['coveragePercent']:.1f}%)")
            for stage, count in data["missingByStage"].items():
                print(f"  {stage}: {count} missing")
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    if not args.json:
        print(f"Coverage complete: {'yes' if not incomplete else 'no'}")
        if args.require_complete:
            print(f"Coverage gate: {report['coverageGate']}")
    if args.list_missing and incomplete:
        for locale in report["locales"]:
            missing: list[str] = []
            for item in catalog["messages"]:
                value = item.get("translations", {}).get(locale)
                if not isinstance(value, str) or not value.strip():
                    missing.append(item["key"])
            print(f"\n{locale} missing keys ({len(missing)}):")
            print("\n".join(missing))
    if args.require_complete and incomplete:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

