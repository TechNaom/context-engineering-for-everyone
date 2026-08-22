# Changelog

All notable changes to this course are documented here. Format is
loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added — 2026-08-22 — Initial build: discovery, curriculum map, full scaffold, Chapter 1

- **Step 1: Discovery** — `docs/discovery-notes.md`: course vision, 4
  personas, prerequisites, learning outcomes, 6-module/13-chapter
  structure, project ladder (L1-L4), capstone shape, differentiators,
  and an explicit, grep/read-verified cross-course overlap check
  against `rag-for-everyone`, `mcp-for-everyone`, and
  `ai-engineering-for-everyone` (including a full read of that course's
  Chapter 3 lesson content, the closest single-chapter overlap risk).
- **Step 2: Curriculum map** — `docs/curriculum/CURRICULUM_MAP.md`.
- **Step 3: Repository architecture scaffolded** — 13 chapter
  directories (Chapter 1 fully built; Chapters 2-13 with `.gitkeep`
  from the start, avoiding the bootstrap bug documented in sibling
  courses), `templates/` (copied and rebranded from
  `ai-engineering-for-everyone`), shared `assets/` rebranded
  (`CEFE_MODULES`, `CEFEProgress`, `cefe-progress`), CI
  (`.github/workflows/ci.yml`, `scripts/local_check.sh`) copied from
  `ai-engineering-for-everyone` and adapted, README, `PROJECT_STATE.md`,
  `AI_HANDOFF.md`, `LICENSE`/`LICENSE-CONTENT`, `CONTRIBUTING.md`, this
  file.
- Homepage (`index.html`) and roadmap (`docs/curriculum/index.html`)
  built as part of the initial scaffold, showing Chapter 1 live and
  Chapters 2-13 as planned — not deferred.
- **Ollama checked fresh this session**: `/api/tags` responded
  normally (`llama3.2:latest` installed); `/api/chat` did not return
  within a 20-second timeout — the same persistent hang every sibling
  TechNaom course has independently reported in this sandbox. Disclosed
  directly in `lesson.html`, not just here.
- **Chapter 1 built and live — reference chapter**: "The Context
  Budget." Hook: Brackwater Home Internet's SignalDesk, a customer
  support chat assistant whose unbounded, unsummarized conversation
  history — combined with a naive end-of-pipeline truncation — silently
  dropped a load-bearing early fact (a customer's incompatible gateway
  hardware) after that fact had already become less reliably used due
  to its buried position in a long context (the "lost in the middle"
  effect), causing a wrong recommendation with no attacker and no model
  bug involved. Builds the five-line Context Budget Ledger (System
  Instructions, Grounding Context, Conversation History, Recalled
  Long-Term Memory, Working Space) as the course's core mental model,
  walks it against the hook end to end in a full diagnosis table, and
  states the course's positioning explicitly relative to every sibling
  course by name — including a detailed distinction from
  `ai-engineering-for-everyone` Chapter 3 ("prompt as versioned software
  artifact") that this course explicitly does not re-teach. Grounded in
  5 real, live-verified sources fetched this session (Anthropic's
  "Effective context engineering for AI agents," Liu et al.'s "Lost in
  the Middle" arXiv paper, OpenAI's Prompt Engineering guide, Anthropic/
  Claude's context-management blog post, and LangChain's "Memory for
  agents" post — two of five required following a live redirect this
  session, disclosed honestly in both `lesson.html` and the quality
  audit). 8 exercises (5 production-gear: fix evaluation, budget
  arithmetic, eviction-policy selection, lost-in-the-middle ordering,
  context-health monitor design) on Cobalt Home Security/GuardLine, 8
  practice scenarios (2 judgment calls, 2 production-gear) across 8
  fresh fictional orgs, 8 interview questions across all 4 levels, and
  a real, gradeable **L1 Guided project** — diagnosing a third fictional
  system (Meridian Legal Aid Network/CaseNote) end to end, with a
  structural self-check harness and a 5-criterion/20-point
  `RUBRIC.md`. Honest Ollama live-testing disclosure stated directly in
  the lesson text itself.
- **Quality audit** (`quality-audits/chapter-01-audit.md`) — honest
  self-critique, a fictional-org exclusion check (11 new orgs, checked
  against `ai-engineering-for-everyone`'s full compiled list with zero
  collision found), and documented citation-redirect handling for two
  of five sources.
