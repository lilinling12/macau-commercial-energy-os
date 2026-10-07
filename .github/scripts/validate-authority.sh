#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "AGENTS.md"
  "docs/00-authority/MASTER_INDEX.md"
  "docs/00-authority/ROADMAP.md"
  "docs/00-authority/handoff/README.md"
  "docs/00-authority/handoff/CURRENT.md"
  "docs/00-authority/handoff/CONTINUE-PROMPT.md"
  "docs/00-authority/decisions/DECISIONS.md"
  "docs/00-authority/decisions/OPEN-QUESTIONS.md"
  "docs/01-research/evidence/EVIDENCE-REGISTER.md"
  "docs/01-research/gates/README.md"
  "docs/02-product/README.md"
  "docs/03-architecture/README.md"
  "docs/03-architecture/technology-authority/README.md"
  "docs/04-engineering/README.md"
)

# These canonical design entrypoints are introduced by the broader product/architecture PR.
# Validate them when present in the checked-out tree while allowing focused governance PRs
# against main to run before those documents are merged.
optional_authority_files=(
  "docs/02-product/PRODUCT-DESIGN.md"
  "docs/03-architecture/ARCHITECTURE-DESIGN.md"
)

for path in "${optional_authority_files[@]}"; do
  if [[ -e "$path" ]]; then
    required_files+=("$path")
  fi
done

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
  if ! grep -q -- "$status" docs/01-research/evidence/EVIDENCE-REGISTER.md; then
    echo "::error file=docs/01-research/evidence/EVIDENCE-REGISTER.md::Missing evidence status: $status"
    exit 1
  fi
done

if ! grep -q "docs/00-authority/handoff/CURRENT.md" AGENTS.md; then
  echo "::error file=AGENTS.md::AGENTS.md must direct agents to docs/00-authority/handoff/CURRENT.md"
  exit 1
fi

echo "Authority validation passed."
