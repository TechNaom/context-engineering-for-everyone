# Chapter 4 Exercises: Long-Term and Persistent Memory Systems

These exercises use a fresh scenario, deliberately different from the
lesson's Nightbourne Senior Living Network/HearthLine hook:
**Caldermere Home Health Alliance**, a fictional home health agency.
Its aide-support assistant, **CareLine**, works with the same
recurring clients across many separate visits over the life of a care
plan. Chapter 2's recipe already ran for this request type: Line 4
(Recalled Long-Term Memory) was correctly allocated **1,800 tokens**.
That number is a given here, not something to re-derive — your job is
the real write and retrieval *policy* that decides what gets persisted
across visits, what gets pulled back into Line 4 for a given visit, and
what gets excluded because it has gone stale.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match scenarios to long-term memory approaches** — decide which of
   three CareLine scenarios need a real persistent-memory policy at
   all, which need a curated store, and which show the append-only
   anti-pattern.
2. **Order the Long-Term Memory Policy Recipe** — put six policy steps
   in the correct sequence.
3. **(Production-gear) Uncurated growth, first visit over budget** —
   real cumulative-token arithmetic showing why an uncurated store
   eventually exceeds Line 4's budget on its own.
4. **(Production-gear) Retrieval budget sizing** — compute how many
   additional facts a turn's retrieval can afford once a core reserve
   is subtracted from the Line 4 budget.
5. **(Production-gear) Write/no-write classification** — decide which
   facts from a real client relationship are durable enough to persist
   at all.
6. **(Production-gear) Staleness resolution** — for facts that changed
   over time, determine which version should remain active and which
   is superseded.
7. **(Production-gear) Build and validate the retrieved Line 4
   package** — verify a core-facts-plus-scoped-facts retrieval fits
   inside budget.
8. **(Production-gear) Naive-append-vs-curated regression gate** —
   confirm a superseded fact that a naive "retrieve everything ever
   stored" policy would incorrectly surface is correctly excluded by
   the curated policy.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly
to see a score report. `solution.py` is the fully filled-in reference
and scores a perfect total when run.
