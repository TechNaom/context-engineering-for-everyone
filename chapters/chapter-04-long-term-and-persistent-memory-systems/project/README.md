# Chapter 4 Project (L2 Assisted): Design Brightmoor Elder Law Group's CaseLine Short-Term AND Long-Term Memory

This is Module 2's closing lab, per the curriculum map's own project
ladder: **"L2 Assisted — Design short-term and long-term memory for a
provided long-running assistant, partial scaffold (ships after Ch.
4)."** Unlike Chapters 1-3, which each shipped a second, module-internal
L1-tier project (a judgment call logged in `quality-audits/chapter-02-
audit.md` and `quality-audits/chapter-03-audit.md`), this project
finally ships the curriculum map's own literal L2 tier, once, solo,
closing Module 2 — see `quality-audits/chapter-04-audit.md` for the
full reasoning behind resolving the open question this way.

## The task

Brightmoor Elder Law Group's case assistant, CaseLine, supports a
guardianship case that has run for over a year across many separate
sessions. `starter.py` gives you the full spec in two parts:

1. **Part 1 (Chapter 3's own skill, reused as a given constraint):**
   design the short-term memory policy for THIS currently open
   session — pin choices and a verbatim window sized against a fixed
   3,800-token Line 3 budget and a fixed 900-token running summary.
2. **Part 2 (this chapter's own new skill):** design the long-term
   retrieval policy — given a persistent store of 6 fact records
   already written from prior, now-closed sessions on this same case
   (some active, some superseded, some expired), decide which records
   get recalled into THIS turn's 250-token Line 4 budget, obeying the
   required/forbidden categories and the staleness rule that a
   non-active record must never be retrieved.

This mirrors exactly the boundary this chapter's lesson establishes:
Line 3 governs one open session; Line 4 governs what survives across
sessions and what real policy pulls it back for a specific turn.

## Why this project touches both lines, not just Line 4

A partial-scaffold "Assisted" project is deliberately less hand-held
than Chapters 1-3's fully guided L1 projects: it doesn't isolate this
chapter's own skill in a vacuum. A real long-term memory review always
happens alongside an already-open session's own short-term policy —
this project tests whether you can hold both constraints at once
(Line 3's budget for this session, Line 4's budget for what crosses
into it from before) without either one silently breaking the other.

## How to run it

```bash
python3 starter.py
```

Most of this project's self-check IS fully mechanical: it verifies
your Part 1 pin choices and budget fit exactly as Chapter 3's project
did, and separately verifies your Part 2 retrieval choices obey the
required/forbidden categories and the staleness exclusion rule, and
that the retrieved package fits the given Line 4 budget. Only the two
judgment calls (the one administrative pin in Part 1, the one
administrative retrieval in Part 2) and the quality of your two
write-ups are open-ended.

## How to check your work for real

1. Run the self-check above until it passes.
2. Compare your full reasoning against `solution.py` — not to match its
   exact judgment-call choices, but to check whether your justification
   is comparably specific, especially about *why* the superseded/
   expired records are excluded, not just that they are.
3. Self-grade against `RUBRIC.md`.

## Files

- `starter.py` — the spec, both parts' templates, and the self-check.
- `solution.py` — one complete, valid reference design.
- `RUBRIC.md` — the grading criteria.
- `index.html` — the styled project page (same content as this file,
  for browser reading).
