# Chapter 2 Exercises: Designing Context Window Budgets

These exercises use a second scenario, deliberately different from the
lesson's Vantry Health Network/TriageLine hook: **Corravine Freight**, a
fictional freight-dispatch company. Its internal dispatcher assistant,
**DispatchLine**, serves several distinct request types on the same
16,000-token-context-window model — a quick status lookup, a multi-leg
route exception review, a carrier tool-dispatch turn, and a full
manifest audit. Applying the five-step allocation recipe to fresh
request types, with fresh numbers, is the point — recalling the
lesson's own TriageLine arithmetic by heart won't get you through
these.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match request types to profiles** — assign the correct archetype
   profile (short lookup, long recurring, tool-heavy, long-document) to
   four DispatchLine request types.
2. **Order the allocation recipe steps** — put the five allocation
   steps from the lesson in the correct sequence.
3. **(Production-gear) Reserve output + system, compute remaining
   budget** — real subtraction arithmetic for a new request type.
4. **(Production-gear) Profile-split arithmetic** — split a remaining
   budget across Lines 2, 3, and 4 using a named profile's percentages.
5. **(Production-gear) Worst-case validation** — classify each line as
   surplus or deficit against its real worst-case need.
6. **(Production-gear) Reuse-safety judgment** — decide whether it's
   safe to reuse one request type's budget for a differently shaped one.
7. **(Production-gear) Design a new allocation from scratch** — apply
   the full recipe to a brand-new request type and window size.
8. **(Production-gear) Recipe completeness gate** — confirm all five
   recipe steps were actually applied, the same completeness discipline
   a real team runs before a new request type's budget ships.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly
to see a score report. `solution.py` is the fully filled-in reference
and scores a perfect total when run.
