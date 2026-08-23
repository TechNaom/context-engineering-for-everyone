# Chapter 4 Practice Bank: Long-Term and Persistent Memory Systems

Eight short, independent scenarios, each its own fictional system —
none of them Nightbourne Senior Living Network/HearthLine or Caldermere
Home Health Alliance/CareLine again. Each scenario is a few sentences
and one judgment or arithmetic question about *what a system persists
across sessions and what real policy pulls it back into Line 4 for a
given turn*, not deriving Line 4's budget itself (that's Chapter 2's
job). The point is speed and accuracy across many different systems,
the way a real long-term memory policy review actually feels.

## How to run

```bash
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch your score climb.

## The eight scenarios

1. **Underholt Family Medicine Network (judgment)** — does raising Line
   4's token budget alone fix contradictory facts showing up in
   retrieval?
2. **Presswick Disability Services Cooperative (production-gear)** —
   retrieval budget sizing arithmetic after a core-facts reserve.
3. **Dunmere Memory Care Residences (judgment)** — should the
   write-criteria list include every fact ever disclosed, unbounded?
4. **Oxbridge Pediatric Home Care (production-gear)** — find the visit
   where an uncurated store's raw total first exceeds its budget.
5. **Wetherby Insurance Trust (judgment)** — is a persisted fact with no
   expiration or update mechanism sound design when its real-world
   value can change?
6. **Camberwell Independent Pharmacy Group (production-gear)** — a
   write/no-write call on a documented drug interaction warning.
7. **Penrose Estate Planning Partners (production-gear)** — does a built
   retrieval package fit inside its Line 4 budget?
8. **Rushbrook K-12 Special Education Cooperative (judgment)** — does
   adding staleness handling remove the need for worst-case validation?

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your answers
automatically. `solution.py` scores a perfect 8/8.
