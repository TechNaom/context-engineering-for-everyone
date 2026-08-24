# Castellan Fleet Logistics — Context Engineering System Design Document

*Fill in every section below for **both** components (DispatchMind and
ComplianceLedger). Do not delete a section — if a section genuinely
doesn't apply to a component, say so explicitly and name why, rather
than leaving it blank. Keep the two fenced `python` blocks per component
(`ledger` and `evaluation_gate`) exactly as structured below —
`self_check.py` parses them directly to grade the objectively-checkable
parts of this document. See `README.md` for the full business problem
this document is answering.*

---

## Component 1: DispatchMind

### 1.1 Job-to-be-done

*(One real sentence: the actual job a dispatcher or driver is trying to
get done, and who's waiting on the answer.)*

### 1.2 Multi-step/agentic shape

*(Is this genuinely multi-step or multi-agent? Name the actual steps or
sub-agents and what each one's own job is.)*

### 1.3 Context Budget Ledger (Ch. 1-2)

```python
hard_limit = None  # TODO: int, total token budget for one DispatchMind turn

ledger = {
    "line1_system": None,          # TODO: int
    "line2_grounding": None,       # TODO: int
    "line3_history": None,         # TODO: int
    "line4_memory": None,          # TODO: int
    "line5_working_space": None,   # TODO: int
}
```

*(Explain your allocation: why this split across the five lines for
DispatchMind's own real request-type profile — per Chapter 2's Budget
Allocation Recipe.)*

### 1.4 Short-term memory plan (Ch. 3)

### 1.5 Long-term memory plan (Ch. 4)

### 1.6 Compression and ordering plan (Ch. 5-6)

### 1.7 Source assembly and retrieval plan (Ch. 7-8)

### 1.8 Tool context and multi-agent/isolation plan (Ch. 9-11)

### 1.9 Context evaluation gate (Ch. 12)

```python
evaluation_gate = {
    "required_facts": None,          # TODO: list[str], at least 3 items
    "completeness_threshold": None,  # TODO: float, 0.0-1.0
    "noise_ratio_max": None,         # TODO: float, 0.0-1.0
    "positional_check": None,        # TODO: bool
}
```

*(Explain each threshold: why this completeness bar, why this noise
ceiling, and whether a positional audit is warranted for this
component's own bundle size and shape.)*

---

## Component 2: ComplianceLedger

### 2.1 Job-to-be-done

### 2.2 Multi-step/agentic shape

### 2.3 Context Budget Ledger (Ch. 1-2)

```python
hard_limit = None  # TODO: int

ledger = {
    "line1_system": None,          # TODO: int
    "line2_grounding": None,       # TODO: int
    "line3_history": None,         # TODO: int
    "line4_memory": None,          # TODO: int
    "line5_working_space": None,   # TODO: int
}
```

### 2.4 Short-term memory plan (Ch. 3)

### 2.5 Long-term memory plan (Ch. 4)

### 2.6 Compression and ordering plan (Ch. 5-6)

### 2.7 Source assembly and retrieval plan (Ch. 7-8)

### 2.8 Tool context and multi-agent/isolation plan (Ch. 9-11)

### 2.9 Context evaluation gate (Ch. 12)

```python
evaluation_gate = {
    "required_facts": None,          # TODO: list[str], at least 3 items
    "completeness_threshold": None,  # TODO: float, 0.0-1.0
    "noise_ratio_max": None,         # TODO: float, 0.0-1.0
    "positional_check": None,        # TODO: bool
}
```

---

## Part 3: Cross-component synthesis

### 3.1 Why these two components' recipe treatments diverge

*(Name the specific facts — traffic volume, real-time exposure,
multi-step shape, consequence of a wrong answer — not just labels, that
drive each divergence between DispatchMind's and ComplianceLedger's own
treatment across all eleven recipes.)*

### 3.2 What would change each component's profile

*(One concrete, realistic future change for each component that would
meaningfully change its own context engineering treatment — and which
specific recipe(s) would need to be re-applied at a different depth as a
result.)*

### 3.3 Shared infrastructure risk

*(Both components are built and operated by the same small platform
team. Name one real risk of that shared ownership — e.g. a memory store,
a source-assembly library, or a tool-result curator shared between the
two components where a change made for one component's sake could
accidentally affect the other's — and how you'd guard against it.)*
