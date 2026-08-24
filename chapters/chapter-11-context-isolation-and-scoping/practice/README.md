# Chapter 11 Practice Bank: Context Isolation and Scoping

Eight scenarios, eight different fictional organizations, mixing
judgment calls with production-gear arithmetic and classification.

## How to run

```bash
python3 --version
python3 starter.py
```

## The eight scenarios

1. **(Judgment) Brightfen Regional Utility Outage Response Cooperative**
   — does isolating a Root-Cause Review Agent from a Dispatch Agent's
   own classification, by itself, guarantee it still gets the shared
   outage-classification rubric it needs?
2. **(Production-gear) Norwick Regional Medical Second-Opinion Network**
   — compute the naive (no-isolation) and scoped (recipe) token totals
   for a Second-Opinion Agent's own budget.
3. **(Judgment) Marrenfield Regional Crop Insurance Claims Bureau** — is
   deleting an initial agent's ENTIRE output sufficient isolation, if the
   shared per-acre payout schedule gets deleted along with it?
4. **(Production-gear) Coalport Regional Ferry Safety Inspection
   Authority** — curate an inspector's own raw output down to the fields
   safe to hand off to an independent re-inspection.
5. **(Judgment) Sallowbrook Regional Land Trust Conservation Board** —
   does isolating an Appeals Panel from a Review Committee's own vote
   guarantee it still has the shared, current eligibility formula?
6. **(Production-gear) Vantree Regional Air Quality Monitoring Network**
   — classify candidate payloads as compliant, contamination-fail, or
   starvation-fail.
7. **(Production-gear) Kesterly Regional Public Records Redaction
   Service** — a three-step pipeline-wide ledger, one line per step.
8. **(Judgment) Wolvercote Regional Peer Review Grant Panel** — does
   isolating two reviewers from each other's own scores mean neither
   should get the shared, objective funding cap they both need?

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your work
automatically. Run either file directly to see a PASS/FAIL report.
`solution.py` is the fully filled-in reference and scores a perfect
total when run.
