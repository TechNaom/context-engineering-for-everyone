# Chapter 13 Project: Castellan Fleet Logistics — DispatchMind and ComplianceLedger

This is the course's Level 4 "Architecture Challenge" — the final
project, and a genuinely different shape from every project before it.
Chapters 1 through 12 each taught one recipe at a time, most with a
provided scaffold. This one gives you a business problem only, no
scaffold, no provided pipeline — the same shape a real architecture-review
request actually arrives in.

## The business problem

Castellan Fleet Logistics is a fictional long-haul trucking company
operating across the western United States. Its platform team wants to
build two LLM-powered, context-heavy components:

- **DispatchMind** — the real-time dispatch copilot embedded in both the
  dispatcher console and every driver's in-cab app. It is genuinely
  agentic: a route-planning agent, an Hours-of-Service (HOS)
  compliance-check agent, and a customer-communications agent, each
  handling live incidents (closures, weather, mechanical issues) across
  Castellan's entire active fleet — thousands of loads in motion on a
  given day, dispatchers and drivers both actively watching for a
  response in real time. Chapter 13's own lesson (`../lesson.html`)
  walked through one single incident inside this exact system in full
  detail — this project asks you to design the complete context
  engineering treatment DispatchMind needs across every load, every
  incident type, not just the one worked example.
- **ComplianceLedger** — an internal tool used by Castellan's small
  compliance team. After each completed route, it assembles the route's
  raw ELD/HOS logs, any DispatchMind incident records generated along the
  way, and the driver's own long-term compliance history into one
  structured, regulator-ready compliance-report entry. A compliance
  officer reviews every generated entry before it's filed into
  Castellan's permanent regulatory record. Used a modest number of times
  per day, by a handful of people, never customer-facing.

Both components are built and operated by the same small Castellan
platform team.

## What you produce

A complete design document, using `DESIGN_DOCUMENT_TEMPLATE.md` as your
starting structure, covering **both** components, applying this course's
own recipe stack — Chapter 1-2's Context Budget Ledger and Budget
Allocation Recipe, Chapter 3's Short-Term Memory Policy Recipe, Chapter
4's Long-Term Memory Policy Recipe, Chapter 5's Compression Fidelity
Recipe, Chapter 6's Context Ordering Recipe, Chapter 7's Source Assembly
Recipe, Chapter 8's Retrieval Integration Recipe, Chapter 9's Tool
Context Recipe, Chapter 10's Pipeline/Multi-Agent Context Recipe,
Chapter 11's Context Isolation Recipe, and Chapter 12's Context
Evaluation Recipe — to both components, at whatever depth each
component's own real shape actually calls for. Specifically:

1. For each component: a job-to-be-done statement and an honest
   assessment of whether (and how) it is genuinely multi-step/agentic.
2. For each component: a real Context Budget Ledger (Chapter 1-2), with
   working arithmetic that actually fits inside a stated hard limit.
3. For each component, at the depth this component's own real traffic,
   real-time exposure, and consequence profile calls for: a real
   short-term memory plan, long-term memory plan, compression/ordering
   plan, source-assembly/retrieval plan, tool/multi-agent/isolation
   plan, and evaluation-gate plan — naming specific mechanisms from the
   relevant chapter, not generic "best practices."
4. A cross-component synthesis: why DispatchMind's and ComplianceLedger's
   own treatments diverge (or don't) across all eleven recipes, what
   would change either component's profile in the future, and one real
   shared-infrastructure risk from having both built and operated by the
   same small team.

## Why this artifact shape, not a `starter.py`

Read `../../quality-audits/chapter-13-audit.md`'s "L4 artifact-shape
decision" section for the full reasoning — the short version, following
`ai-engineering-for-everyone` Chapter 13's own precedent directly: a
business problem with no provided pipeline and no scaffold has no
fixture data for a Python script to grade against. The deliverable is
closer to a real architecture-decision-record-style document (see
`../lesson.html`'s own Sources section for the Architecture Decision
Record citation this template's structure borrows) than a filled-in
exercise file. This project still includes real, objectively-checkable
arithmetic per component — a Context Budget Ledger that must actually
fit its own stated hard limit, and an evaluation-gate specification with
real, in-range thresholds — checked mechanically by `self_check.py`. The
rest — which recipe treatments apply at which depth, and why — is graded
qualitatively, against `RUBRIC.md`, the same way a real architecture
review would be.

## How to do this project

1. Copy `DESIGN_DOCUMENT_TEMPLATE.md` to your own file (e.g.
   `my_design_document.md`) and fill in every section for both
   components. Keep the fenced `python` code blocks' structure exactly
   as given — `self_check.py` parses them directly.
2. Run the structural self-check against your own file:

   ```bash
   python3 self_check.py my_design_document.md
   ```

   This confirms every required section is present, and that your
   declared budget ledgers and evaluation gates are arithmetically valid
   — it does not grade your prose or your recipe-depth judgment calls.
3. Compare your document against
   `solution/SOLUTION_DESIGN_DOCUMENT.md` — not to match its exact
   wording, but to check whether your reasoning names real, specific
   mechanisms the way the reference does.
4. Self-grade against `RUBRIC.md`.

## Files

- `DESIGN_DOCUMENT_TEMPLATE.md` — the business problem's required
  document structure, with TODOs.
- `self_check.py` — the structural self-check (section-presence and
  budget-ledger/evaluation-gate arithmetic only).
- `solution.py` — runs `self_check.py` against the reference document and
  confirms it passes.
- `solution/SOLUTION_DESIGN_DOCUMENT.md` — one complete, valid reference
  response.
- `RUBRIC.md` — the qualitative grading criteria.
- `index.html` — the styled project page (same content as this file, for
  browser reading).
