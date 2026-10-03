# Cross-Conversation Research and Engineering Continuity

**Purpose:** Make research and AI-assisted engineering resumable from repository state in any new conversation. Conversation history is a working interface, not the project's system of record.

## Durable source of truth

Persist project knowledge in the numbered repository structure:

- Research questions, sources, evidence, and Gate outcomes: `docs/01-research/`
- Decisions and unresolved questions: `docs/00-authority/decisions/`
- Product scope and user workflows: `docs/02-product/`
- Architecture and technology authority: `docs/03-architecture/`
- AI coding workflow and task packets: `docs/04-engineering/ai-coding-governance/`
- Current status and the next task: `docs/00-authority/handoff/CURRENT.md`
- Historical handoffs: `docs/00-authority/handoff/HISTORY.md`

Do not rely on an earlier chat being available or complete. If a statement is not recorded with its status and source in the repository, treat it as unverified working context.

## Start of every new research or coding conversation

1. Read `AGENTS.md`, `docs/00-authority/handoff/README.md`, this protocol, `CURRENT.md`, and `CONTINUE-PROMPT.md`.
2. Read the relevant Decision Register, Open Questions, Gate record, product/architecture record, contracts, and evidence referenced by CURRENT or the task packet.
3. Check the live repository branch, open PRs, and current file contents when the task depends on GitHub state. Do not assume a previous chat's status is current.
4. Identify the active Gate, its status, dependencies, and the exact user-requested outcome. If the task packet is missing, create one before substantial work.
5. Preserve the distinction between:
   - **VERIFIED:** directly supported by an authoritative source, controlled measurement, or approved customer evidence;
   - **DERIVED:** reproducible calculation from named inputs;
   - **PROJECT_ASSUMPTION / HYPOTHESIS:** useful working proposition not yet validated;
   - **UNKNOWN / OPEN:** unresolved question, with owner/evidence needed where known;
   - **DECISION:** approved project choice with rationale, scope, and date.
   
Use the repository's canonical status vocabulary if a relevant Authority file defines a more specific scheme.

## Continuous research loop

For each research task:

1. State the Gate and the question it is meant to resolve.
2. Define the claim and evidence needed before searching; prioritize primary Macau regulatory, utility, meter, tariff, customer, and site sources where applicable.
3. Record source title, issuing organization, URL or file, publication/effective date, retrieval date, exact relevant section/page, and what claim it supports. Keep conflicting sources and measurement limitations visible.
4. Separate source facts from calculations, hypotheses, and interpretation. Never convert absence of public evidence into proof that something is prohibited or impossible.
5. Compare new evidence against the existing Decision Register, Open Questions, and prior Gate outputs. Identify what changes and what remains unchanged.
6. If evidence changes an approved choice, prepare a Decision Record/ADR describing the prior decision, new evidence, consequences, and required approval. Do not silently rewrite Authority.
7. Record the Gate result, remaining unknowns, product and architecture impacts, and next dependency-ready task in the relevant Gate/evidence files and CURRENT.

A research task is not complete merely because sources were collected. It must produce a traceable synthesis and a durable next step.

## AI Coding loop

For each implementation task:

1. Create or complete a task packet using `TASK-PACKET-TEMPLATE.md`; cite the Gate, approved decisions, architecture boundaries, contracts, scope, non-goals, acceptance evidence, and rollback/recovery expectations.
2. Confirm the task can proceed under current Authority. If it changes architecture, safety, settlement semantics, contracts, or research direction, prepare a Decision Record before implementation.
3. Make the smallest change that satisfies the packet while preserving replaceability for provisional technology choices.
4. Validate against the packet's required checks. Record commands, results, and limitations; do not claim checks that were not run.
5. Update relevant docs, evidence, task status, and CURRENT when the next task or Gate changes. Open a PR that explains evidence and Authority impact; human review/approval remains required for architecture or operational decisions.

AI agents may draft analysis, code, tests, and documentation. They may not approve their own Authority changes, infer field authorization, or bypass the Safety Kernel.

## End-of-session handoff

Before ending substantial work, leave a durable handoff:

- Update the relevant research, evidence, decision, product, architecture, or engineering artifact.
- Update CURRENT only when status, active work, or next-task instructions changed; include exact Gate/status and a specific next task.
- Add a short HISTORY entry for material transitions, completed evidence runs, or approved decisions.
- Preserve open PR/branch links and whether changes are draft, ready, merged, or blocked.
- Ensure the next task can start from the repository without needing the prior conversation.

Do not rewrite CURRENT with speculative dates or claim Gate completion without its required evidence and decision.

## New-conversation opening prompt

Use `CONTINUE-PROMPT.md` as the opening instruction. The first response in a resumed task should state the current Gate, known status, relevant authority files, and planned durable output. Continue from repository state; ask only for missing access or evidence that cannot be inferred safely.
