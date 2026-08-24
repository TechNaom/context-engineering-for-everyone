# Chapter 11 Exercises: Context Isolation and Scoping

These exercises use a fresh scenario, deliberately different from the
lesson's Vesteroak Regional Appeals Review Board/AppealLine hook:
**Calloway County Child Welfare Case Review Network**, a fictional
county child-welfare agency. Its case pipeline, **CaseShield**, has two
stages: a Primary Caseworker Agent makes an initial risk assessment, and
— required by county policy, to preserve a genuinely independent second
read — a Second-Opinion Reviewer Agent reviews the same case separately.
The Second-Opinion Reviewer must never see the Primary Caseworker's own
risk score, narrative reasoning, or recommendation. It *should* still
receive the shared, objective Risk Assessment Rubric version both stages
are required to apply, and the case's own identifying facts. Your job is
this chapter's own new skill: naming an isolation goal precisely,
separating "opinion" from "shared fact" when drawing a boundary,
building a curated hand-off contract for whatever legitimately crosses
it, and testing the result with both a contamination probe and a
starvation probe.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match scenarios to isolation approaches** — decide which of three
   CaseShield scenarios show no isolation, isolation drawn too broadly,
   or the full Context Isolation Recipe.
2. **Order the Context Isolation Recipe** — put six recipe steps in the
   correct sequence.
3. **(Production-gear) Per-approach budget and correctness** — compute
   the Second-Opinion Reviewer's own token cost under all three
   approaches.
4. **(Production-gear) Separating opinion from shared fact** — decide
   which of the Primary Caseworker's five raw output fields are its own
   opinion versus shared, objective facts.
5. **(Production-gear) Build the Step 4 hand-off contract** — construct
   the curated dict that should cross the isolation boundary.
6. **(Production-gear) Contamination probe** — decide, for three
   candidate bundles, whether the Primary Caseworker's own opinion
   leaked in.
7. **(Production-gear) Starvation probe** — decide, for three candidate
   bundles, whether a required shared fact was walled off by mistake.
8. **(Production-gear) Combined 2x2 classification** — classify four
   final bundles as compliant, contamination-fail, starvation-fail, or
   both-fail.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly to
see a score report. `solution.py` is the fully filled-in reference and
scores a perfect total when run.
