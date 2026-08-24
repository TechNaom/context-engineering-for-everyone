# Chapter 10 Practice Bank: Multi-Agent Context

Eight short, independent scenarios, each its own fictional multi-step or
multi-agent pipeline — none of them Heronbrook Regional Grantmaking
Alliance/GrantPilot or Prescott County Emergency Housing Placement
Network/PlacementLine again. Each scenario is a few sentences and one
judgment or arithmetic question about *this chapter's own new skill*:
scoping a step's own context contract, budgeting each step as its own
ledger line, isolating context per unit of work, and deciding what a
sub-agent's own delegated payload should and shouldn't include — not
tool-result curation within a single step (that's Chapter 9's job), and
not deciding when withholding context is the right design choice on
purpose (that's Chapter 11's job). The point is speed and accuracy
across many different pipelines, the way a real multi-agent context
review actually feels.

## How to run

```bash
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch your score climb.

## The eight scenarios

1. **Bramwell County Court Interpreter Scheduling Service (judgment)** —
   does every step in a scheduling pipeline reasoning correctly about an
   unscoped full shift history guarantee the right schedule for the
   current case?
2. **Solmere Regional Disaster Shelter Intake Network (production-gear)**
   — naive vs. scoped per-step token arithmetic for a shelter-assignment
   pipeline.
3. **Anchorfield Regional Small Business Loan Consortium (judgment)** —
   does correct per-applicant scoping alone guarantee working context
   resets between one applicant's review and the next?
4. **Hawkridge Regional Reforestation Grants Program (production-gear)**
   — curate a site-assessment agent's raw output to what the receiving
   step's own contract needs.
5. **Havermill County Meals-on-Wheels Route Optimization Service
   (judgment)** — does a route agent correctly scoped to the current
   route's own data guarantee an earlier route's driver assignment won't
   be reused for it?
6. **Ledgemont Regional Water Utility Leak Response Pipeline
   (production-gear)** — sub-agent delegation scoping across three
   candidate dispatch payloads.
7. **Tessington Regional Scholarship Review Board (production-gear)** —
   a pipeline-wide ledger check across four steps, each with its own
   budget line.
8. **Cresswell Regional Building Permit Review Pipeline (judgment)** — a
   final decision record mixes fields from two different applications
   reviewed in the same session; is it ready to hand downstream?

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your answers
automatically. `solution.py` scores a perfect 8/8.
