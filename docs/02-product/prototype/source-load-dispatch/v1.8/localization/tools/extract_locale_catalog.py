#!/usr/bin/env python3
"""Extract a review-only zh-Hant locale catalog from the v1.8 HTML prototype.

This creates candidate translation units, not a runtime catalog. Portuguese and
English values intentionally remain null until reviewed translations exist.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

CJK = re.compile(r"[\u3400-\u9fff]")
STAGES = {
    "evidence-check",
    "site-model",
    "dispatchComparison",
    "constraint-analysis",
    "shadow-review",
    "outcome-replay",
}
TEXT_ATTRIBUTES = ("aria-label", "title", "placeholder", "alt")


def slug(value: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return result or "shell"


def catalog_key(stage: str, channel: str, source: str) -> str:
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()[:10]
    return f"dispatch.v1_8.{slug(stage)}.{slug(channel)}.{digest}"


class LocaleInventoryParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, dict[str, str]]] = []
        self.units: dict[tuple[str, str, str], dict[str, Any]] = {}
        self.text_node_count = 0
        self.unique_text: set[str] = set()
        self.unique_chinese_text: set[str] = set()
        self.attribute_value_count = 0
        self.unique_chinese_attributes: set[str] = set()

    def _stage(self) -> str:
        for _, attrs in reversed(self.stack):
            if attrs.get("id") in STAGES:
                return attrs["id"]
        return "shell"

    def _context(self) -> str:
        parts: list[str] = []
        for tag, attrs in self.stack[-7:]:
            part = tag
            if attrs.get("id"):
                part += f"#{attrs['id']}"
            elif attrs.get("class"):
                part += "." + ".".join(attrs["class"].split()[:2])
            parts.append(part)
        return "/".join(parts)

    def _add(self, channel: str, source: str, line: int, *, attr: str | None = None) -> None:
        stage = self._stage()
        key = (stage, channel, source)
        row = self.units.setdefault(
            key,
            {
                "key": catalog_key(stage, channel, source),
                "channel": channel,
                "stage": stage,
                "sourceText": source,
                "translations": {"pt": None, "en": None},
                "locations": [],
            },
        )
        if line not in row["locations"]:
            row["locations"].append(line)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value or "" for name, value in attrs}
        self.stack.append((tag, values))
        for name in TEXT_ATTRIBUTES:
            value = values.get(name, "").strip()
            if value:
                self.attribute_value_count += 1
            if value and CJK.search(value):
                self.unique_chinese_attributes.add(value)
                self._add(f"attribute-{name}", value, self.getpos()[0], attr=name)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data: str) -> None:
        if self.stack and self.stack[-1][0] in {"script", "style"}:
            return
        value = data.strip()
        if not value:
            return
        self.text_node_count += 1
        self.unique_text.add(value)
        if CJK.search(value):
            self.unique_chinese_text.add(value)
            self._add("text", value, self.getpos()[0])


def extract_script_literals(source: str, parser: LocaleInventoryParser) -> int:
    scripts = re.finditer(r"<script\b[^>]*>(.*?)</script\s*>", source, re.I | re.S)
    patterns = (
        re.compile(r'"((?:\\.|[^"\\])*)"'),
        re.compile(r"'((?:\\.|[^'\\])*)'"),
        re.compile(r"`((?:\\.|[^`\\])*)`"),
    )
    before = len(parser.units)
    for script in scripts:
        body = script.group(1)
        line_offset = source.count("\n", 0, script.start(1))
        for pattern in patterns:
            for match in pattern.finditer(body):
                raw = match.group(1)
                value = raw.replace(r"\'", "'").replace(r'\"', '"').replace(r"\`", "`")
                if value.strip() and CJK.search(value):
                    key = ("interaction-code", "dynamic-script", value)
                    row = parser.units.setdefault(
                        key,
                        {
                            "key": catalog_key("interaction-code", "dynamic-script", value),
                            "channel": "dynamic-script",
                            "stage": "interaction-code",
                            "sourceText": value,
                            "translations": {"pt": None, "en": None},
                            "locations": [],
                            "reviewNote": "Literal may be an interpolation fragment; human review required.",
                        },
                    )
                    line = line_offset + body.count("\n", 0, match.start()) + 1
                    if line not in row["locations"]:
                        row["locations"].append(line)
    return len(parser.units) - before


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--source-blob", required=True, help="Git blob SHA of the inspected prototype")
    args = ap.parse_args()

    raw = args.source.read_bytes()
    actual_blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + bytes([0]) + raw).hexdigest()
    if actual_blob != args.source_blob:
        raise SystemExit(f"Source blob mismatch: expected {args.source_blob}, got {actual_blob}")
    html = raw.decode("utf-8")
    parser = LocaleInventoryParser()
    parser.feed(html)
    dynamic_unit_count = extract_script_literals(html, parser)
    units = sorted(parser.units.values(), key=lambda row: row["key"])
    for unit in units:
        unit["locations"].sort()

    payload = {
        "catalogVersion": "0.1.0",
        "status": "REVIEW_CANDIDATE_NOT_RUNTIME",
        "defaultReviewState": "UNTRANSLATED_CANDIDATE",
        "sourceLocale": "zh-Hant",
        "source": {
            "path": "docs/02-product/prototype/source-load-dispatch/v1.8/index.html",
            "blob": args.source_blob,
            "sourceLocale": "zh-Hant",
        },
        "candidateLocales": ["zh-Hant", "pt", "en"],
        "localeApproval": "UNRESOLVED",
        "extraction": {
            "method": "Python html.parser text/attribute extraction plus inline-script literal scan",
            "textNodes": parser.text_node_count,
            "uniqueTextValues": len(parser.unique_text),
            "uniqueChineseTextValues": len(parser.unique_chinese_text),
            "nonEmptyTextAttributes": parser.attribute_value_count,
            "uniqueChineseAttributeValues": len(parser.unique_chinese_attributes),
            "dynamicChineseLiteralValues": dynamic_unit_count,
            "catalogUnitsIncludingContextAndChannels": len(units),
            "limitations": [
                "Source text is not translated.",
                "Dynamic string literals can be sentence fragments and need manual key/context review.",
                "Static source counts exclude runtime-created pager nodes; their source literals are in dynamic-script entries.",
                "Repeated text in distinct stages/channels may intentionally have separate keys.",
                "This candidate catalog is not wired into the prototype and does not constitute multilingual support.",
            ],
        },
        "messages": units,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(payload["extraction"], ensure_ascii=False))


if __name__ == "__main__":
    main()
