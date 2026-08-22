# Chapter 1 Project (L1 Guided): Diagnose CaseNote's Ledger Gaps

This is the course's first project — the **L1 Guided** project (per the
curriculum map's project ladder), shipping in full with Chapter 1
itself rather than deferred to a later chapter, since Chapter 1's
five-line ledger is everything this project needs.

## The task

Meridian Legal Aid Network's fictional intake assistant, CaseNote, has
been running for three months. `starter.py` gives you five real,
specific facts about how it operates today — no attack, no exotic
failure, just a team that shipped fast and never came back to add
context engineering discipline. Your job:

1. **Diagnose** — for each of the five facts, name the single ledger
   line it maps to, restate the evidence in your own words, and propose
   one concrete engineering fix.
2. **Prioritize** — order the five fixes from most to least urgent, in
   your own judgment, and justify the ordering in 2-4 sentences.

This mirrors exactly what Chapter 1's own walkthrough did for
Brackwater Home Internet's SignalDesk — you're now doing it yourself,
on a fresh system, without the lesson doing it for you first.

## Why this project, not something more open-ended

A first project that asked "go build a context-engineered feature"
before you've practiced *diagnosing* gaps in an existing one would skip
the more foundational skill. Diagnosis — can you look at a real system
and correctly name what's missing, using the five-line vocabulary — is
the skill every later chapter's hands-on work depends on. Building new
systems with the missing lines already filled in is what Chapters
2-12's own exercises and projects have you practice, one line at a
time.

## How to run it

```bash
python3 starter.py
```

This project is intentionally open-ended (there's more than one
defensible fix for most of these gaps), so the script runs a
**structural self-check**: are all five facts diagnosed, does each map
to a genuinely different line, is every field real (not a placeholder
one-word answer), and does your prioritized order use all five lines
exactly once. It does not grade whether your specific wording matches
a reference answer.

## How to check your work for real

1. Run the structural self-check above until it passes.
2. Compare your full diagnosis against `solution.py` — not to match
   its exact wording, but to check whether your reasoning is
   comparably concrete and whether your fixes are genuinely
   engineering changes, not "be more careful."
3. Self-grade against `RUBRIC.md`.

## Files

- `starter.py` — the scenario, your diagnosis template, and the
  self-check.
- `solution.py` — one complete, valid reference diagnosis.
- `RUBRIC.md` — the grading criteria.
- `index.html` — the styled project page (same content as this file,
  for browser reading).
