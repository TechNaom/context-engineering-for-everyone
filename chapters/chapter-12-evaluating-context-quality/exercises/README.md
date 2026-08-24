# Chapter 12 Exercises: Evaluating Context Quality

Scenario: **Merrivale County Emergency Housing Placement Network**, a
fictional county agency. Its placement pipeline, **PlacementGuard**,
assembles context for a Housing Placement Agent from four sources —
applicant intake, shelter availability, medical needs flags, and prior
placement notes — every one of them correctly budgeted, fresh,
retrieved, and isolated per Chapters 1-11's own recipes. Your job is
this chapter's own new skill: checking the *finished* bundle itself for
completeness, noise, and positional risk, rather than trusting that a
correctly-run assembly pipeline guarantees a good result.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match scenarios to evaluation approaches** — decide which of three
   PlacementGuard scenarios show no evaluation, proxy-only evaluation
   (source presence), or the full Context Evaluation Recipe.
2. **Order the Context Evaluation Recipe** — put six recipe steps in the
   correct sequence.
3. **(Production-gear) Completeness score** — compute a real
   found/required fraction for Case MC-5521's own four required facts.
4. **(Production-gear) Noise ratio** — compute what fraction of the
   assembled bundle is unrelated material, and whether it exceeds a 10%
   threshold.
5. **(Production-gear) Positional audit** — bucket three required
   facts' own positions as front, middle, or back.
6. **(Production-gear) Combined context quality gate** — evaluate three
   candidate bundles against completeness, noise, and positional rules
   together.
7. **(Production-gear) Fix-simulation arithmetic** — compute the
   after-fix token total once noise is removed and a missing fact and a
   promoted summary are added.
8. **(Production-gear) Combined completeness/quality classification** —
   classify four final bundles as compliant, completeness_fail,
   quality_fail, or both_fail.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly to
see a score report. `solution.py` is the fully filled-in reference and
scores a perfect total when run.
