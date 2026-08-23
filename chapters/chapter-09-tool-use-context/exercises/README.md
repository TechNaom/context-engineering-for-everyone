# Chapter 9 Exercises: Tool-Use Context

These exercises use a fresh scenario, deliberately different from the
lesson's Sagebrush Regional Field Services Cooperative/DispatchLine
hook: **Kestrel Regional Grid Operations Cooperative**, a fictional
multi-substation electric grid operator. Its dispatcher-support
assistant, **RelayLine**, has nine registered tools (substation-status
lookup, load-forecast query, crew-roster lookup, outage-map query,
weather-alert lookup, breaker-history lookup, maintenance-ticket
create, fuel-reserve lookup, and vendor-contact lookup) but only ever
calls two of them for a "Substation Overload Risk Check" request.
Chapters 1-8's own recipes have already run for this request type — a
correct budget, correct memory handling, nothing over budget needing
compression, no positional risk, and no multi-source contradiction
left unresolved. The protocol that carries a tool call is correct and
out of scope — your job is this chapter's own new skill: scoping which
tool definitions belong in context, curating and boundary-safely
fitting a tool's raw result, and managing tool-call history across a
multi-step loop.

## How to run

```bash
python3 --version
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Match scenarios to tool-context approaches** — decide which of
   three RelayLine scenarios show unconditional full-registry
   inclusion, scoped-tools-but-raw-passthrough, or the full Tool
   Context Recipe.
2. **Order the Tool Context Recipe** — put six recipe steps in the
   correct sequence.
3. **(Production-gear) Request-type tool scoping and schema budget** —
   given nine registered tools' schema token costs and the two tools
   "Substation Overload Risk Check" actually calls, compute the
   scoped-vs-unconditional schema token cost and the tokens saved.
4. **(Production-gear) Result curation** — decide which of a
   substation-status tool's eleven raw fields the request type actually
   needs kept.
5. **(Production-gear) Field-boundary-safe budget fit** — fit the
   curated result to a token budget, keeping whole fields only, never
   truncating mid-field.
6. **(Production-gear) Tool-call history eviction** — across a
   four-call agentic loop, decide which prior tool-call results are
   superseded and should be evicted or marked stale.
7. **(Production-gear) Naive-vs-recipe regression gate** — confirm a
   load-bearing field a naive character-count cutoff would drop is
   correctly preserved by the recipe, within budget.
8. **(Production-gear) Source-assembly handoff typing** — decide which
   of four candidate context items are correctly typed, curated
   `tool_result` sources ready to hand to Chapter 7's own Source
   Assembly Recipe.

## Checking your work

`score_exercise_*()` functions built into both `starter.py` and
`solution.py` grade your work automatically. Run either file directly
to see a score report. `solution.py` is the fully filled-in reference
and scores a perfect total when run.
