# Macau Commercial Energy OS Authority Master Index

## Purpose

This is the entry point for project knowledge. The repository's numbered documentation structure follows the original research-to-delivery framework:

Research → Decision → Architecture → Engineering → Implementation.

## Canonical directory structure

- `docs/00-authority/`: project state, roadmap, decisions, open questions and handoff instructions.
- `docs/01-research/`: domain and technology research, research gates, evidence register and source-backed evidence notes.
- `docs/02-product/`: product thesis, customer segments, commercial model, MVP definition and pilot design.
- `docs/03-architecture/`: system boundaries and architecture records, including technology selection authority.
- `docs/04-engineering/`: development workflow, module boundaries, AI coding governance and CI/CD.
- `docs/05-mvp/`: executable MVP plans and vertical slices.

## Core planning and continuity documents

- Research-to-delivery Gate sequence and work packets: `docs/00-authority/ROADMAP.md`
- Cross-conversation research/coding continuity: `docs/00-authority/handoff/CONTINUATION-PROTOCOL.md`
- New-conversation entry prompt: `docs/00-authority/handoff/CONTINUE-PROMPT.md`
- Reusable research and coding task packet: `docs/04-engineering/ai-coding-governance/TASK-PACKET-TEMPLATE.md`
- Research-derived product scope and user workflow: `docs/02-product/PRODUCT-DESIGN.md`
- Logical system architecture and technology decision states: `docs/03-architecture/ARCHITECTURE-DESIGN.md`
- Current status and next authorized work: `docs/00-authority/handoff/CURRENT.md`

All authoritative project documentation belongs under these six numbered directories. Do not create parallel unnumbered documentation roots under `docs/`. Keep implementation source code in the repository's `implementation/` directory.

## Authority chain

Research → Evidence → Decision → Product / Architecture → Engineering → Implementation → Validation → Handoff.

Every implementation decision must trace to an approved decision and supporting evidence. Research conclusions, assumptions, and unresolved questions must retain their status.

## Rule

When adding or moving documentation, update this index and every affected internal link in the same change.
