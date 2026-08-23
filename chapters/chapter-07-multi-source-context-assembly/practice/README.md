# Chapter 7 Practice Bank: Multi-Source Context Assembly

Eight short, independent scenarios, each its own fictional system —
none of them Hadleworth Metro Water Authority/ConfluenceLine or
Corrinvale Independent Pharmacy Network/ScriptLine again. Each scenario
is a few sentences and one judgment or arithmetic question about *this
chapter's own new skill*: deciding which sources belong, ranking their
authority, detecting and resolving contradictions between them, and
deduplicating restated content — not deriving a budget (that's Chapters
2-3's job) or deciding where already-resolved content sits (that's
Chapter 6's job). The point is speed and accuracy across many different
systems, the way a real context-assembly review actually feels.

## How to run

```bash
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch your score climb.

## The eight scenarios

1. **Juniper Ridge Veterinary Partners (judgment)** — does concatenating
   two individually correct sources in arrival order, with no authority
   ranking, guarantee the combined result is coherent?
2. **Quarrydale Auto Diagnostics Cooperative (production-gear)** —
   authority-rank conflict resolution between a retrieved document and
   live tool output.
3. **Tamworth Regional Housing Trust (judgment)** — is stripping exact
   duplicate text across sources, with no authority ranking or
   reworded-contradiction check, a sufficient assembly step on its own?
4. **Wexford Maritime Charter Group (production-gear)** — contradiction
   detection across two claim pairs.
5. **Dovetail Woodcraft Guild (judgment)** — does a big token-savings
   number from deduplication alone guarantee no contradiction remains?
6. **Cinderfield Volunteer Fire Network (production-gear)** —
   deduplication arithmetic: which source to keep, and tokens saved.
7. **Barleycroft Grain & Feed Cooperative (production-gear)** — a
   naive-vs-recipe regression check on a specific load-bearing
   contradiction, including a post-resolution budget check.
8. **Yewmarsh Wildlife Sanctuary (judgment)** — one contradiction found
   where both sources share the same authority rank, with no clear
   winner — safe to ship as-is, or resolve/escalate?

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your answers
automatically. `solution.py` scores a perfect 8/8.
