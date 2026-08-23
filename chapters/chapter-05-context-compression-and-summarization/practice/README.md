# Chapter 5 Practice Bank: Context Compression and Summarization

Eight short, independent scenarios, each its own fictional system —
none of them Brannigan Home Energy Services/GridLine or Kirkholme
Public Transit Safety Board/TransitLine again. Each scenario is a few
sentences and one judgment or arithmetic question about *the real
mechanics of compressing content without losing what a downstream step
depends on*, not deriving a compression target itself (that's Chapter
2 and Chapter 3's job). The point is speed and accuracy across many
different systems, the way a real compression-pipeline review actually
feels.

## How to run

```bash
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch your score climb.

## The eight scenarios

1. **Lynhaven Community Health Partners (judgment)** — does compressing
   a long conversation automatically lose load-bearing facts, or only
   when there's no fidelity check?
2. **Sablewood Legal Trust (production-gear)** — compression ratio
   arithmetic against a fixed target.
3. **Coalridge Municipal Transit Authority (judgment)** — is "ask the
   model to summarize and trust the result" a sufficient compression
   policy on its own?
4. **Pikestone Logistics Group (production-gear)** — find missing
   candidates in a produced summary and whether the fidelity check
   passes.
5. **Rowancraig Insurance Underwriters (judgment)** — does an
   extractive strategy matter more for structured or for narrative
   content?
6. **Draymoor Agricultural Cooperative (production-gear)** — an
   extractive-vs-abstractive strategy call on a specific content type.
7. **Osprey Ridge Wealth Management (production-gear)** — a
   naive-vs-fidelity-checked regression check on a specific dollar
   figure.
8. **Talmarsh Veterinary Alliance (judgment)** — if a fidelity check
   fails once, is it safe to just retry the exact same naive prompt
   again unchanged?

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your answers
automatically. `solution.py` scores a perfect 8/8.
