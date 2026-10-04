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
- [Prototype v0.9 — workspace organization comparison](prototype/v0.9/index.html) is the comparative IA stimulus only. It presents one synthetic blocked-demand case in evidence-first, exceptions-first and guided-assessment layouts; it does not represent the full screen set or validate any user outcome. 200% zoom, assistive-technology and user evaluation remain open.
- 中文 Owner 评审摘要 v0.1：[OWNER-REVIEW-BRIEF-zh-CN-v0.1.md](OWNER-REVIEW-BRIEF-zh-CN-v0.1.md)。它是英文决策队列的中文评审入口，不记录任何已批准决定。

- [Prototype v0.10 — core product workflow](prototype/v0.10/index.html) is the current nine-destination interaction study. At 320/375/768/1024/1440 CSS px, the page had no document-level horizontal overflow; any wide synthetic table stayed inside its labeled scroll wrapper. All nine destinations switched to their matching view and URL state, browser Back restored Recommendations after Evidence & replay, and ArrowUp+Enter changed the narrow selector while focus moved to the destination heading. This bounded local observation is not user validation, screen-reader review, a 200% zoom check or WCAG conformance.

## Visual direction palette comparison v0.1

[Open the side-by-side prototype](prototype/visual-directions/v0.1/index.html). It compares Harbor Teal, Mineral Blue and Night Graphite on the same synthetic portfolio/demand-review task, including evidence status, forecast uncertainty and concise Traditional Chinese, Portuguese and English labels. Sample contrast ratios are source calculations only; rendered accessibility and target-user evaluation remain outstanding. No palette is selected.
