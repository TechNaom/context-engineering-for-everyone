# Chapter 7 Exercises: Multi-Source Context Assembly

These exercises use a fresh scenario, deliberately different from the
lesson's Hadleworth Metro Water Authority/ConfluenceLine hook:
**Corrinvale Independent Pharmacy Network**, a fictional independent
pharmacy chain. Its pharmacist-facing assistant, **ScriptLine**,
assembles context for "Refill Safety Review" requests from several
sources at once: a retrieved chart-summary document (sometimes stale), a
live tool call to the pharmacy-benefit and EHR systems, the conversation
so far with the patient, and the pharmacy's own system instructions.
Chapters 1-6's own recipes have already run for this request type — a
correct budget, correct short-term/long-term memory handling, nothing
over budget needing compression, and no positional risk. Every source is
individually correct — your job is this chapter's own new skill:
deciding which sources belong, ranking their authority, detecting and
resolving contradictions between them, and deduplicating restated
content, before Chapter 6's own ordering recipe ever runs.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match scenarios to assembly approaches** — decide which of three
   ScriptLine scenarios show naive concatenation, string-dedup-only, or
   the full Source Assembly Recipe.
2. **Order the Source Assembly Recipe** — put six recipe steps in the
   correct sequence.
3. **(Production-gear) Authority-rank conflict resolution** — given an
   authority ranking and three source conflicts, compute which source
   wins each one.
4. **(Production-gear) Contradiction detection** — decide which of six
   claim pairs are genuine contradictions versus restatements or
   unrelated facts.
5. **(Production-gear) Deduplication arithmetic** — for three claims
   asserted by multiple sources, compute which source to keep and how
   many tokens dropping the rest saves.
6. **(Production-gear) Budget check after resolution** — compute the
   resolved token total after dedup savings and confirm it fits the
   request type's budget.
7. **(Production-gear) Naive-vs-recipe regression gate** — confirm a
   load-bearing contradiction naive concatenation would leave unresolved
   is correctly resolved by the recipe, within budget.
8. **(Production-gear) Escalation decision** — for three assembly-review
   outcomes, decide whether it's safe to ship or the pipeline must
   resolve/escalate.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly
to see a score report. `solution.py` is the fully filled-in reference
and scores a perfect total when run.
