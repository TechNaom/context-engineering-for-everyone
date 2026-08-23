# Chapter 9 Interview Questions: Tool-Use Context

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) DispatchLine's weather tool executed correctly and returned the correct data every time, including the 52 mph gust reading. Why did the assistant still miss it?

**Strong answer:** The tool's own execution was never the problem — the
failure was in what happened to its result on the way into context.
Every one of the twelve registered tools' schemas was sent on every
call regardless of whether the request type ever used them, which left
little of the tool-output budget free; the weather tool's full
forty-field raw result was then appended verbatim and cut off by raw
character count wherever the budget ran out, landing three characters
into `wind_gust_mph` and losing the gust value and the active advisory
entirely. Correct tool execution is not the same as a well-formed
tool-result source.

**Red flag:** Blames the weather tool, the RPC layer, or the model's
reasoning, rather than the two specific gaps (unscoped schema
inclusion, uncurated/unfit result) that actually caused the loss.

**Follow-up:** "If the weather tool had returned fewer fields to begin
with, would that have fixed the underlying gap?"

**What this proves:** Understands that correct tool execution is not
the same as a well-formed tool-result source — this chapter's central
distinction.

---

### 2. (Beginner) What does "tool-use context" mean, in one sentence a non-technical stakeholder would understand?

**Strong answer:** Before a model can even ask to use a tool, it has to
be told what tools exist and what they accept — that costs tokens on
every single call, whether or not the tool is actually used this turn —
and after a tool runs, someone has to decide which parts of its raw,
often large result are worth keeping, make sure a kept result isn't cut
off mid-value to fit a budget, and make sure a tool's older result from
earlier in a session doesn't sit in context as if it were still current
once a newer call has replaced it.

**Red flag:** Describes it as simply "formatting the tool's output,"
with no mention of the tool-definition cost, boundary-safe fitting, or
history staleness.

**Follow-up:** "Is this the same thing as how the tool call itself gets
authorized and transported?"

**What this proves:** Can distinguish this chapter's context-shaping
job from `mcp-for-everyone`'s own protocol-negotiation subject.

---

### 3. (Intermediate) A teammate says: "we already scope our tool list so the model only sees the tools this request type can call, so our tool context is solid." How do you respond?

**Strong answer:** Scoping tool definitions to the request type is a
real, worthwhile improvement over an unconditional full registry, and
worth keeping — but it says nothing about what happens to a tool's raw
result once the tool is actually called. DispatchLine's own second
approach in this chapter's comparison table shows exactly this gap:
even with ten unused tool schemas correctly excluded, nothing about
scoping prevents a verbose forty-field weather result from being
truncated mid-field, or ensures a stale result from three calls ago
gets evicted before it reaches the model again.

**Red flag:** Treats tool scoping as sufficient on its own, or conflates
"unused tools excluded" with "well-formed tool-result context."

**Follow-up:** "What does your pipeline do right now if the same tool
gets called twice for the same fact ten minutes apart in one session?"

**What this proves:** Understands the real gap between schema scoping
and the rest of the Tool Context Recipe — the two solve different
problems.

---

### 4. (Intermediate) How is this chapter's subject different from what `mcp-for-everyone` teaches?

**Strong answer:** `mcp-for-everyone`'s own Module 5 (Chapters 9-10, as
re-confirmed this session against its current curriculum map) covers
permissions, scopes, sandboxing, and prompt-injection/tool-output trust
— whether a tool call is authorized and whether its output can be
trusted from a security standpoint. This chapter assumes a tool call
already happened correctly, by whatever protocol, and asks a completely
different question: given that a well-formed, trustworthy tool call
occurred, what earns a place in context because of it, and how much?
Scoping a tool's schema, curating its result, and evicting stale
tool-call history are all context-engineering decisions that have
nothing to do with whether the call was permitted or the output was
safe.

**Red flag:** Conflates "deciding what a tool result costs in tokens
and how it's curated" with "deciding whether a tool call was allowed to
happen," or can't name which course owns which question.

**Follow-up:** "If a tool call is fully authorized and its output is
fully trusted, does that mean it's automatically ready to hand to
Chapter 7's own Source Assembly Recipe?"

**What this proves:** Can hold the protocol-agnostic boundary against
`mcp-for-everyone` explicitly, the same boundary this chapter's own
lesson re-confirmed this session.

---

### 5. (Senior) You're reviewing a new agentic tool-calling pipeline before it ships. What do you check beyond "every tool executes correctly and every result is accurate"?

**Strong answer:** Correct tool execution is necessary but not
sufficient. Check that each request type's tool list is scoped on
purpose, not just "every registered tool, always." Check that each
included tool's own schema cost is budgeted as an explicit line item,
separate from the tool-output budget. Check that a called tool's raw
result is curated to only the fields the request type actually needs,
not passed through verbatim. Check that the curated result is fit to
budget at a field boundary, never truncated mid-key or mid-value. And
check that tool-call history across a multi-step loop marks or evicts
superseded results rather than letting every past call sit in context
as if it were still current.

**Red flag:** Signs off purely because every tool call in a test suite
returned correct data, with no scrutiny of what happens to a tool's
definition and result on the way into the model's context.

**Follow-up:** "Walk me through what your pipeline does today when the
same tool is called twice in one session for the same underlying
fact."

**What this proves:** Understands that tool execution correctness is a
floor, and tool-use context needs its own explicit, testable rules
downstream of it.

---

### 6. (Senior) How do you decide how much engineering investment a given request type's tool-context handling deserves?

**Strong answer:** Look at how many tools are registered overall versus
how many a given request type actually calls (a large gap means schema
scoping saves real, recurring tokens), how large and how variable a
called tool's raw result typically is relative to its own output
budget (a small, fixed-shape result needs less curation discipline than
a forty-field API dump), how often the same fact gets re-queried across
a multi-step loop for this request type, and what's at stake if a
truncated or superseded field goes unnoticed — a safety-critical field
like a wind-gust reading or a landing-zone hazard, versus a low-stakes
lookup where a slightly stale field rarely matters. High-stakes,
high-tool-count, high-result-variability request types justify the
full Tool Context Recipe; a single-tool, small-fixed-result lookup may
reasonably need only basic scoping.

**Red flag:** Proposes the full six-step recipe for every tool-calling
request type "to be safe" with no engagement with actual tool count,
result size, or re-query frequency, or the reverse — skips curation and
history eviction for a request type where a real, observed truncation
or staleness incident already happened.

**Follow-up:** "Your highest-traffic request type calls exactly one
tool that always returns the same three small fields. Does it still
need the full recipe?"

**What this proves:** Applies proportionate judgment consistently,
rather than treating this chapter's recipe as free or universally
required — the same discipline every prior chapter's own comparison
table required.

---

### 7. (Architect) Design a lightweight governance process so every tool-calling pipeline in a production system actually gets its tool-use context reviewed, not just its tool-execution correctness tested.

**Strong answer:** Require a standard artifact per request type that
calls any tool: the scoped tool list and the reasoning behind excluding
every other registered tool, the schema token cost of each included
tool tracked as its own budget line item, a documented field-curation
rule per tool (which fields this request type keeps and why), evidence
that budget fitting is field-boundary-safe (a test that verifies no
field is ever partially included), and a documented tool-call-history
eviction rule for any request type whose loop can call the same tool
more than once. Pair it with a regression suite built from known
load-bearing fields (like DispatchLine's own wind-gust reading) that
must survive curation and fitting intact before a pipeline change
ships, and track truncated-field and stale-history-reused rates as
first-class production metrics, the same way Chapter 8's own architect
answer required tracking truncation and empty-result rates for
retrieval integration.

**Red flag:** A process that only tracks whether each tool call
returned correct data, with no requirement that tool-context
handling — schema scoping, curation, boundary-safe fit, history
eviction — was ever tested directly.

**Follow-up:** "A tool gets a new field added to its response schema
next quarter. How does your process catch that the existing curation
rule for that tool might now need to include or explicitly exclude it?"

**What this proves:** Architect-level judgment — treats tool-use
context as something that needs continuous verification as tools and
request types evolve, not a one-time pipeline setting.

---

### 8. (Architect) Leadership says: "our new model has a much larger context window, so we can just send every tool's full schema and every tool's full raw result on every call — do we still need scoping, curation, and boundary-safe fitting?"

**Strong answer:** A larger window changes the calculus but doesn't
eliminate the need. A bigger window reduces how often truncation
actually triggers, but every unscoped tool schema and every uncurated
result is still competing with every other token for the model's
actual attention and cost budget, not just for raw window space — and
DispatchLine's own hook shows the deciding failure wasn't running out
of window room in the abstract, it was a real, avoidable choice not to
scope or curate at all. A bigger window also does nothing about
tool-call history staleness: a superseded result from three calls ago
is just as wrong sitting comfortably inside a large window as it is
crowding a small one. A claim that a larger window makes tool-context
engineering unnecessary needs its own regression evidence against known
load-bearing fields for the new system, not an assumption that more
room solves a problem about what earns a place in context at all.

**Red flag:** Treats a larger context window as a sufficient
replacement for explicit tool-context engineering, with no engagement
with the specific failure mode (correctly executed, incorrectly
contextualized) this chapter's own hook demonstrated, or no mention of
tool-call-history staleness at all.

**Follow-up:** "What's the smallest, cheapest test you'd run against the
new model's larger window before removing your field-curation rules for
a high-stakes tool?"

**What this proves:** Can reason about context-window growth as a
reason to keep testing tool-context handling specifically, not a reason
to remove it — the same discipline this chapter's own live captures
demonstrated concretely.

## Strategy Tips

- Ground every answer in DispatchLine's actual failure (a correctly
  executing weather tool, still mishandled between the tool call and
  the model by unscoped schema inclusion and a boundary-blind cutoff)
  rather than a generic "tool calling is hard" answer.
- For senior/architect questions, always name the specific tool-context
  mechanism at risk — schema scoping, schema budgeting, result
  curation, field-boundary-safe fit, or tool-call-history eviction —
  rather than treating "a bigger window" or "a better tool" as a
  universal fix for problems that happen after a tool call already
  executed correctly.
- If you're new to engineering interviews: reason out loud by naming
  which of this chapter's own failure-prone moments (deciding which
  tools even need to be defined for this request type, curating a raw
  result down to what matters, fitting it safely to budget, or
  recognizing that an old result has been superseded) a given scenario
  is testing, before proposing a fix.

## A note on this chapter's project

This chapter ships no project of its own. Per the curriculum map's own
project ladder (L1 after Ch. 2, L2 after Ch. 4, L3 after Ch. 8, L4 the
Ch. 13 capstone), Module 5 (Chapters 9-11) carries no dedicated project
slot at all — its own two labs are folded directly into the Ch. 13
capstone's own system design instead. See
`quality-audits/chapter-09-audit.md` for the full reasoning.
