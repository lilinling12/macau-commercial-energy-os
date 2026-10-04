# Productization Authority

This layer connects research and architecture with commercial execution.

Flow:

Research

-> Evidence

-> Architecture

-> Product Thesis

-> Pilot

-> MVP

Productization does not replace technical authority; it derives from it.

## Product review artifacts

- [Prototype v0.6](prototype/v0.6/index.html) is a synthetic, advisory-only interaction candidate. It provides a compact mobile view selector for all workspace views and increases the scenario-threshold line/swatch contrast.
- v0.6 remains a review draft: a limited local browser accessibility-tree check observed the compact selector in one browser context, desktop navigation in another, and the `#tariffs` deep link opening the tariff view. Exact viewport dimensions and screenshot-level visual behavior were not captured; keyboard, assistive-technology and target-user reviews remain outstanding. It does not select a production frontend framework or settle product scope, visual direction, or production architecture.

- [Prototype v0.7 — workspace organization study](prototype/v0.7/index.html) is retained as the original comparison artifact. A rendered review found that its `display:grid` rule overrode the inactive views' native `hidden` state, so all three workspaces appeared together; do not use v0.7 for variant-comparison sessions.
- [Prototype v0.8 — corrected workspace organization study](prototype/v0.8/index.html) preserves the same synthetic evidence and three unapproved information architectures, restores one-visible-variant behavior, and wraps the three-option selector on narrow screens. A single local browser context confirmed variant changes, hidden inactive content, keyboard selection and the wrapped selector. This remains a design stimulus, not user validation or WCAG conformance evidence.
- [Prototype v0.9 — 320px reflow correction](prototype/v0.9/index.html) is the current IA study stimulus. It removes the 320px body minimum-width that caused 15 CSS pixels of horizontal page overflow at a 320px viewport after the vertical scrollbar. Render inspection at 320, 375, 768, 1024 and 1440 CSS px found no page-level horizontal overflow; only the selected workspace was exposed. 200% browser zoom, full assistive-technology review and user evaluation remain open. v0.7 and v0.8 are preserved history, not the current participant stimulus.
- 中文 Owner 评审摘要 v0.1：[OWNER-REVIEW-BRIEF-zh-CN-v0.1.md](OWNER-REVIEW-BRIEF-zh-CN-v0.1.md)。它是英文决策队列的中文评审入口，不记录任何已批准决定。
