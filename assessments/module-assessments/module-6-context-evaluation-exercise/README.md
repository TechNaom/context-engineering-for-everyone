# Module 6 Assessment, Part 1: Context-Evaluation Exercise

Per `docs/curriculum/CURRICULUM_MAP.md`, Module 6's stated assessment is
"context-evaluation exercise (Ch. 12) + capstone rubric (Ch. 13,
architecture challenge, Level 4)" — two separate deliverables, one per
chapter, not one combined review built at the end the way
`ai-engineering-for-everyone`'s own Module 5 combined assessment was.
This is Chapter 12's own half: a single, applied exercise running the
full Context Evaluation Recipe against one fresh case, built during
Chapter 12's own session. Chapter 13's own capstone rubric, covering the
L4 architecture challenge, ships separately with that chapter — see
`quality-audits/chapter-12-audit.md`'s "Module 6 assessment groundwork"
section for the reasoning on why this scope, and why it lives here
rather than inside Chapter 12's own `exercises/` or `practice/`
directories.

## The scenario

Ternfield Regional Disability Benefits Review Office's ClaimLens system
(the lesson's own fictional agency, a fresh case rather than a new
organization) is reviewing Case TF-9102. The assembled 3,000-token
context bundle has three independent problems, all at once — this
exercise's own point is running the Context Evaluation Recipe as one
integrated check, not isolating a single failure mode the way the
lesson's own worked math or this chapter's exercises each did
separately.

## The task

Using `starter.py`, produce:

1. **Completeness score** (Steps 1-2) — score the bundle against Case
   TF-9102's own four required facts.
2. **Noise ratio** (Step 3) — compute the real noise ratio against the
   bundle's own 3,000-token total.
3. **Positional audit** (Step 4) — bucket each required fact's own
   position as front, middle, or back.
4. **Combined gate decision** (Step 5) — determine whether this bundle
   passes the combined context quality gate.
5. **Written justification** — the one genuinely open-ended task: name
   all three problems this specific bundle has (not just one), citing
   the actual computed numbers, not a generic "this bundle needs work."

## Why this exercise, and why this scope

This deliberately reuses the exact functions this chapter's own
`context_evaluation_recipe.py` and exercises already built and tested,
applied together to one case with all three problems present at once —
the point is synthesis across all three checks in a single pass, not new
mechanics. It is intentionally smaller than a full chapter project: one
case instead of eleven-plus fictional organizations, five tasks instead
of a full exercises + practice buildout, because Chapter 12 already
shipped both of those in full.

## How to run it

```bash
python3 starter.py
```

The written justification is open-ended (there's more than one
defensible way to phrase it), so the script runs a **structural
self-check**: are the completeness score, noise ratio, positional
buckets, and gate decision all correctly computed, and is the
justification a real, descriptive note that names all three problems
rather than a placeholder. It does not grade whether your justification
prose matches the reference solution's exact wording.

## How to check your work for real

1. Run the structural self-check above until it passes.
2. Compare your full response against `solution.py` — check whether your
   justification actually names all three problems (incomplete,
   over-threshold noise, and a buried critical fact), not just the one
   that seems most obvious.
3. Self-grade against `RUBRIC.md`.

## Files

- `starter.py` — the scenario, your response template, and the structural
  self-check.
- `solution.py` — one complete, valid reference response.
- `RUBRIC.md` — the grading criteria.
