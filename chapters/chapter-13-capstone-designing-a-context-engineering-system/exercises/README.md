# Chapter 13 Exercises: Capstone: Designing a Context Engineering System

These exercises use a second Castellan Fleet Logistics scenario,
deliberately different from the lesson's own I-80 closure hook: a
cold-chain load (CFL-90410, Boise to Reno, Unit 2290) reporting a reefer
(refrigeration) mechanical warning mid-route — a cargo-integrity
incident, not a road-closure incident. Applying the full recipe stack to
a fresh scenario, from scratch, is the point. Recalling the lesson's own
I-80 answers by heart won't get you through these.

## How to run

You'll need Python 3 installed. Check with:

```bash
python3 --version
```

Then run the starter file:

```bash
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The five tasks

1. **Recipe-matching judgment** — match six situations to the one recipe
   (of all eleven from Chapters 1-12) that actually resolves each.
2. **Context Budget Ledger arithmetic** — sum a five-line ledger, check it
   against a hard limit, and compute spare budget (Ch. 1-2).
3. **Short-term memory classification** — apply the verbatim-window +
   pinning + compress-the-rest recipe to five real conversation turns
   (Ch. 3).
4. **Isolation boundary judgment** — decide what crosses a real
   Cargo-Integrity-Agent-to-Customer-Comms-Agent boundary and what stays
   (Ch. 11).
5. **Evaluation gate arithmetic** — compute completeness and noise ratio
   for a bundle missing one required fact, and determine whether the
   gate passes (Ch. 12).

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly to
see a score report. `solution.py` is the fully filled-in reference and
scores a perfect total when run.
