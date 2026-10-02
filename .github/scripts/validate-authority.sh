#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "AGENTS.md"
  "docs/handoff/README.md"
  "docs/handoff/CURRENT.md"
  "docs/handoff/CONTINUE-PROMPT.md"
  "docs/decisions/DECISIONS.md"
  "docs/decisions/OPEN-QUESTIONS.md"
  "docs/evidence/EVIDENCE-REGISTER.md"
  "docs/research-gates/README.md"
  "docs/architecture/README.md"
  "docs/technology/README.md"
  "docs/productization/README.md"
  "docs/engineering/README.md"
)

for path in "${required_files[@]}"; do
  if [[ ! -f "$path" ]]; then
    echo "::error file=$path::Required authority file is missing"
    exit 1
  fi
done

required_statuses=(
  "VERIFIED"
  "DERIVED"
  "HYPOTHESIS"
  "PROJECT_ASSUMPTION"
  "UNKNOWN"
  "CONTRACT_VERIFIED"
)

for status in "${required_statuses[@]}"; do
  if ! grep -q -- "$status" docs/evidence/EVIDENCE-REGISTER.md; then
    echo "::error file=docs/evidence/EVIDENCE-REGISTER.md::Missing evidence status: $status"
    exit 1
  fi
done

if ! grep -q "docs/handoff/CURRENT.md" AGENTS.md && ! grep -q "CURRENT.md" AGENTS.md; then
  echo "::error file=AGENTS.md::AGENTS.md must direct agents to CURRENT.md"
  exit 1
fi

echo "Authority validation passed."
