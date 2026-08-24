# Chapter 10 Exercises: Multi-Agent Context

These exercises use a fresh scenario, deliberately different from the
lesson's Heronbrook Regional Grantmaking Alliance/GrantPilot hook:
**Prescott County Emergency Housing Placement Network**, a fictional
county emergency-housing agency. Its placement pipeline,
**PlacementLine**, is a three-step pipeline (Intake Agent, Eligibility
Agent, Match Agent) run by a single orchestrator across a long shift,
processing many households back to back in one session. Chapters 1-9's
own recipes have already run for each step: a correct budget, correct
memory handling, nothing over budget needing compression, no positional
risk, no multi-source contradiction, and correct tool-result curation
wherever a step calls a tool. Your job is this chapter's own new skill:
scoping each step's own context contract, budgeting each step as its own
ledger line, isolating context per household (this pipeline's own unit
of work), and deciding what a sub-agent actually needs from the
orchestrator.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match scenarios to pipeline-context approaches** — decide which of
   three PlacementLine scenarios show unscoped session history,
   scoped-but-no-unit-isolation, or the full Pipeline/Multi-Agent
   Context Recipe.
2. **Order the Pipeline/Multi-Agent Context Recipe** — put six recipe
   steps in the correct sequence.
3. **(Production-gear) Per-step budget vs. an unscoped shift history** —
   compute the naive and scoped token costs for the Match Agent's own
   context, and whether each fits its budget.
4. **(Production-gear) Curating a prior step's own output** — decide
   which of the Eligibility Agent's six raw output fields the Match
   Agent's own contract actually needs kept.
5. **(Production-gear) Unit-of-work isolation** — across an unreset
   working context mixing three households' own data, decide which
   items belong to the current household and survive.
6. **(Production-gear) Sub-agent delegation scope** — decide which of
   three candidate payloads handed to the Match Agent are correctly
   scoped to its own delegated sub-task.
7. **(Production-gear) Pipeline-wide ledger, one line per step** —
   confirm each of three steps' own scoped context fits its own budget
   line, and compute the pipeline-wide total.
8. **(Production-gear) Downstream handoff typing** — decide which of
   four candidate final records are correctly typed, curated,
   single-household outputs ready to hand downstream.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly
to see a score report. `solution.py` is the fully filled-in reference
and scores a perfect total when run.
