# Chapter 6 Exercises: Avoiding Lost-in-the-Middle

These exercises use a fresh scenario, deliberately different from the
lesson's Marchside Regional Trauma Network/VitalsLine hook: **Calverton
Public Defender's Office**, a fictional public defender's office. Its
case-file review assistant, **DocketLine**, handles "Case File Review"
conversations before a hearing — a real case file can run long,
accumulating a defendant's background, prior filings, a transcript of
plea negotiations, and evidence logs, before the specific question the
attorney actually needs answered ever gets asked. Chapters 1-5's own
recipes have already run for this request type: a correct budget, a
correct pin/summary/window shape, a correct long-term recall policy,
and a fidelity-checked compression pipeline. Every fact in the window
is present, unmodified, and within budget — your job is this chapter's
own new skill: deciding *where* each already-included fact goes so the
model actually uses it.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match scenarios to ordering approaches** — decide which of three
   DocketLine scenarios show arrival order, the naive "move everything
   to the top" anti-pattern, or the full weight-ranked, both-anchors
   pipeline.
2. **Order the Context Ordering Recipe** — put five recipe steps in
   the correct sequence.
3. **(Production-gear) Position-percentile arithmetic** — compute
   where a fact's midpoint sits as a percentile of a 3,200-token
   window, and whether it falls inside the high-risk middle band.
4. **(Production-gear) Load-bearing weight classification** — decide
   which of six case-file details carry enough weight to require an
   anchor position.
5. **(Production-gear) Positional probe: anchor-required facts** —
   given a set of facts that require an anchor position and a
   produced window's actual anchor placements, find which are missing
   and whether the placement passes its own probe.
6. **(Production-gear) Query/instruction anchor classification** —
   classify six content types by whether they belong at the end anchor
   nearest generation or elsewhere in the window.
7. **(Production-gear) Arrival-order-vs-weight-ranked regression
   gate** — confirm a load-bearing detail arrival order would bury is
   correctly surfaced by weight-ranked placement, and would be
   correctly flagged if it weren't.
8. **(Production-gear) Retest/escalation decision** — for three
   positional-probe outcomes, decide whether it's safe to ship or the
   pipeline must retest/reposition.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly
to see a score report. `solution.py` is the fully filled-in reference
and scores a perfect total when run.
