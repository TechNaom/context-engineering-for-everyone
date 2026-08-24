# Chapter 12 Practice Bank: Evaluating Context Quality

Eight scenarios, eight different fictional organizations, mixing
judgment calls with production-gear arithmetic and classification.

## How to run

```bash
python3 --version
python3 starter.py
```

## The eight scenarios

1. **(Judgment) Ossbrook Regional Grain Futures Clearinghouse** — does
   confirming a required source category is present, by itself,
   guarantee the specific required fact inside it is actually present?
2. **(Production-gear) Colton Regional Home Inspection Licensing Board**
   — compute a real completeness score across five required facts.
3. **(Judgment) Bramfield Regional Wildfire Evacuation Coordination
   Center** — does fitting a token budget, by itself, guarantee an
   acceptable noise ratio?
4. **(Production-gear) Grendale Regional Court Interpreter Certification
   Board** — compute a real noise ratio and check it against a 10%
   threshold.
5. **(Judgment) Delmoore Regional Pension Fund Audit Office** — does
   passing Chapter 11's own contamination and starvation probes, by
   itself, guarantee this chapter's own completeness, noise, and
   positional checks also pass?
6. **(Production-gear) Sennwick Regional Livestock Export Health
   Certification Bureau** — bucket three required facts' own positions
   as front, middle, or back.
7. **(Production-gear) Bexmoor Regional Building Code Variance Board**
   — evaluate three candidate bundles against the combined context
   quality gate.
8. **(Judgment) Warrenfield Regional Small Business Disaster Loan
   Review Panel** — does perfect completeness and zero noise, alone,
   guarantee a bundle passes the gate if its one critical fact is
   bucketed "middle"?

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your work
automatically. Run either file directly to see a PASS/FAIL report.
`solution.py` is the fully filled-in reference and scores a perfect
total when run.
