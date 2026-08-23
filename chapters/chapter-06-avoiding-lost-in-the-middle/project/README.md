# Module 3 Project: Build Brackholt County Court Records Office's ArchiveLine Compression + Ordering Pipeline

This is Module 3's closing lab, drawing on **both** chapters this
module built — Chapter 5's Compression Fidelity Recipe and Chapter 6's
own Context Ordering Recipe — not just Chapter 6's material in
isolation, per the curriculum map's own Module 3 labs: "build a
summarization pipeline that preserves load-bearing facts; reorder a
context window to fix a lost-in-the-middle failure." Chapter 5's own
session deliberately deferred its project here (see
`quality-audits/chapter-05-audit.md`), and this project is where that
commitment is honored.

## A note on this project's tier

The curriculum map's own four-tier project ladder (L1 after Ch. 2, L2
after Ch. 4, L3 after Ch. 8, L4 the Ch. 13 capstone) does not assign a
numbered tier to Module 3 — it jumps directly from L2 (Ch. 4) to L3 (Ch.
8). This project is the course's own separate "one project per module"
convention (confirmed in Chapter 4's session, applied again here)
filling that gap, not a claim to be the literal L3 tier early — see
`quality-audits/chapter-06-audit.md` for the full reasoning. In scaffold
terms it sits between L2's partial scaffold and L3's no-scaffold: a full
spec is given, like L2, but you design both halves (compression AND
ordering) together, with no part solved for you.

## The task

Brackholt County Court Records Office's fictional docket-review
assistant, ArchiveLine, helps a public defender review an active case
file before a hearing. `starter.py` gives you the full spec in two
parts:

1. **Part 1 (Chapter 5's own skill, reused as this project's own
   exercise of it):** compress a 3,000-token aged-out conversation
   segment down to a fixed 600-token target, preserving three
   already-flagged load-bearing candidates and choosing a compression
   strategy for each.
2. **Part 2 (this chapter's own new skill):** decide where six
   already-correctly-included content blocks — including Part 1's own
   compressed output — belong inside a final, 3,200-token-budget
   assembled window: which get the start anchor, which one (the query)
   gets the end anchor nearest generation, and which belong in the
   middle.

## Why this project touches both chapters, not just this one

Module 3's own two labs are stated as a pair in the curriculum map, not
as two separate single-chapter tasks. A real production pipeline never
compresses in isolation from how the result gets positioned afterward —
this project tests whether you can hold both skills at once: Chapter
5's fidelity discipline for what survives compression, and this
chapter's own positional discipline for where the survivor (and every
other already-included block) actually goes.

## How to run it

```bash
python3 starter.py
```

Most of this project's self-check IS fully mechanical: it verifies your
Part 1 candidate/strategy choices exactly as Chapter 5's own recipe
would, and separately verifies your Part 2 block placements obey the
anchor/middle rules and the assembled window fits its budget. Only the
QUALITY of your two write-ups is open-ended.

## How to check your work for real

1. Run the self-check above until it passes.
2. Compare your full reasoning against `solution.py` — not to match its
   exact wording, but to check whether your justification is comparably
   specific, especially about *why* each low-weight block is correctly
   left in the middle, not just that it is.
3. Self-grade against `RUBRIC.md`.

## Files

- `starter.py` — the spec, both parts' templates, and the self-check.
- `solution.py` — one complete, valid reference design.
- `RUBRIC.md` — the grading criteria.
- `index.html` — the styled project page (same content as this file,
  for browser reading).
