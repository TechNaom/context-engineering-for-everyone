# Chapter 9 Practice Bank: Tool-Use Context

Eight short, independent scenarios, each its own fictional system —
none of them Sagebrush Regional Field Services Cooperative/DispatchLine
or Kestrel Regional Grid Operations Cooperative/RelayLine again. Each
scenario is a few sentences and one judgment or arithmetic question
about *this chapter's own new skill*: scoping tool definitions to a
request type, budgeting a tool schema's own token cost, curating and
boundary-safely fitting a tool's raw result, and evicting or marking
superseded tool-call history — not the protocol that carries a tool
call, and not multi-source assembly across different source types
(that's Chapter 7's job). The point is speed and accuracy across many
different systems, the way a real tool-context review actually feels.

## How to run

```bash
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch your score climb.

## The eight scenarios

1. **Winslow County Emergency Medical Services (judgment)** — does
   registering every tool's schema unconditionally guarantee the model
   selects the correct tool for a given request?
2. **Gullwick Harbor Pilotage Authority (production-gear)** —
   request-type tool scoping and schema-token arithmetic across five
   registered tools.
3. **Sparrowmere Independent News Network (judgment)** — does curating
   a tool's raw result down to fewer fields guarantee the curated
   result fits the token budget?
4. **Hazelcombe Regional Blood Bank Network (production-gear)** —
   field-boundary-safe budget fit across four prioritized fields.
5. **Renfrew Municipal Snow Removal Cooperative (judgment)** — does a
   correctly curated, boundary-fit tool result from this turn guarantee
   an earlier turn's tool-call result is no longer treated as current?
6. **Dunbar Ridge Avalanche Forecast Center (production-gear)** —
   tool-call history supersession across two call pairs.
7. **Corvale Regional Air Ambulance Consortium (production-gear)** — a
   naive-vs-recipe regression check on a load-bearing field, including a
   post-resolution budget check.
8. **Whitmore County Livestock Health Cooperative (judgment)** — a
   tool call times out this turn; safe to silently reuse a stale cached
   result from three calls ago, or surface that the tool result is
   currently unavailable?

## Checking your work

`score()` in both `starter.py` and `solution.py` grades your answers
automatically. `solution.py` scores a perfect 8/8.
