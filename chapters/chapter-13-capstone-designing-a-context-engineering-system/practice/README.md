# Chapter 13 Practice Bank: Capstone: Designing a Context Engineering System

Four short, independent Castellan Fleet Logistics scenarios — fresh loads
and incidents, none of them the lesson's own I-80 closure or the
exercises' own reefer warning. Each is a few sentences and one recipe
judgment or arithmetic call, covering ground the lesson and exercises
didn't touch directly: budget worst-case validation, compression
fidelity, source authority ranking, and tool-result curation.

## How to run

```bash
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch your score climb.

## The four scenarios

1. **Load CFL-77120 (judgment)** — budget-validation judgment: does a
   ledger fitting comfortably on a routine day, with no incident, prove
   it's validated per Chapter 2's own Step 5 (worst realistic case)?
2. **Load CFL-63305 (production-gear)** — compression fidelity check:
   did all load-bearing facts survive a compressed summary?
3. **Load CFL-40218 (production-gear)** — source authority resolution:
   two sources disagree on a driver's own remaining HOS hours; resolve
   by authority rank.
4. **Load CFL-51190 (production-gear)** — tool-result curation: curate a
   raw 6-field weather-tool result down to the 3 fields this request
   type actually needs, and compute the curated token count.

## Checking your work

`score_scenario_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly to
see a score report. `solution.py` is the fully filled-in reference and
scores a perfect total when run.
