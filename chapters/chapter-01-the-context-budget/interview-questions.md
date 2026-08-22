# Chapter 1 Interview Questions: The Context Budget

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) Why isn't "the model has a huge context window now" enough to guarantee it will use everything you put in it correctly?

**Strong answer:** A large context window changes how much content
*fits*, not how reliably the model *uses* every part of it. Research
shows model performance follows a real position effect: information at
the beginning or end of a long context is used more reliably than
information buried in the middle. A window can have plenty of unused
capacity and still lose a fact functionally, because of where that fact
sits, not whether it's technically present.

**Red flag:** Treats "it fits in the window" and "the model will use it
correctly" as the same claim.

**Follow-up:** "Name one concrete technique for making a critical fact
more likely to be used, beyond just including it somewhere."

**What this proves:** Understands this course's central distinction —
presence in the window and reliable use of what's in the window are
different properties.

---

### 2. (Beginner) In the lesson's hook, SignalDesk's prompt template never changed, and it still caused a production incident. How is that possible?

**Strong answer:** The failure wasn't in the versioned, reviewed prompt
template — it was in the dynamic content poured into that template every
request: an unbounded, unsummarized conversation transcript that
eventually got blindly truncated, dropping a load-bearing early fact.
The same well-reviewed template can produce a correct result on one
request and a broken one on the next, purely because of what filled it
that specific time.

**Red flag:** Assumes the incident means the prompt itself was badly
written or under-reviewed, rather than recognizing the failure was in
the per-request content, not the template.

**Follow-up:** "Which ledger line was actually responsible, and which
one wasn't?"

**What this proves:** Separates "the template is broken" from "the
content that filled the template this request was mismanaged" — the
exact distinction that separates this course from prompt-template
versioning.

---

### 3. (Intermediate) Walk through why treating a context window as "just keep appending everything" eventually fails, even with a very large window.

**Strong answer:** Two separate mechanisms compound. First, cost and
latency scale with every token sent, so unbounded appending gets
expensive and slow well before it gets impossible. Second, and more
subtly, models show measurable accuracy degradation as token count
grows — "context rot" — driven by an attention budget that depletes with
each additional token, meaning relevant content becomes *less* reliably
used even while it's still technically present. A bigger window delays
the hard failure but doesn't fix the accuracy degradation, which starts
well before the window's limit is reached.

**Red flag:** Suggests a bigger context window alone solves unbounded
appending, without naming the accuracy-degradation mechanism.

**Follow-up:** "What would you actually build instead of 'just keep
appending'?"

**What this proves:** Understands why compression and curation (Module
3) are a distinct discipline from "get a bigger window."

---

### 4. (Intermediate) A teammate says "we don't need a memory system — the model just remembers everything in the conversation." What's the gap in that reasoning?

**Strong answer:** A model doesn't "remember" anything between requests
— every request is a fresh construction job built from whatever the
surrounding code decides to include. Within one long conversation, an
unmanaged transcript can also silently drop early facts through
truncation, exactly like SignalDesk did. "The model remembers" describes
an illusion created by faithfully replaying history back to it each
time, an illusion that breaks the moment history has to be trimmed,
compressed, or the conversation ends and a new one begins with no
persistent store behind it.

**Red flag:** Treats in-context conversation replay as equivalent to a
real, engineered memory system with deliberate storage and recall
policies.

**Follow-up:** "What's the difference between short-term and long-term
memory in this course's terms, and why does that distinction matter?"

**What this proves:** Understands memory as a system to be designed
(Module 2), not an emergent property of a big enough context window.

---

### 5. (Senior) You inherit a long-running assistant with a well-managed, versioned prompt template and nothing else — no budget policy, no memory system, no compression, no multi-source assembly discipline, no context evaluation. Where do you start, and why?

**Strong answer:** Start with an explicit budget allocation across the
five ledger lines (Chapter 2's subject) before touching anything else —
without a real budget, you can't tell whether conversation history,
grounding context, or output reservation is actually the bottleneck, you
can only guess. Once the budget is explicit, conversation-history
compression (Module 3) is usually the next highest-leverage fix, since
unmanaged history is the fastest-growing, most common failure mode.
Multi-source assembly and context evaluation matter, but have a smaller
blast radius if the budget and memory layers underneath them are still
broken — evaluating or assembling context well is much less valuable if
the underlying budget is already silently starving something.

**Red flag:** Picks one line in isolation without justifying the
ordering, or claims all five lines are equally urgent with no
prioritization logic.

**Follow-up:** "If you only had budget for two of the five lines this
quarter, which two, and what would you explicitly accept as residual
risk?"

**What this proves:** Can prioritize context engineering work under real
constraints, not just list all five lines as equally important.

---

### 6. (Senior) How would you explain to a skeptical engineering manager why "just use a bigger context window" isn't a complete fix for a long-running assistant's quality problems?

**Strong answer:** A bigger window increases how much content
*technically fits*, but doesn't change two real, independently
documented mechanisms: content in the middle of a long context is used
less reliably regardless of window size (a position effect, not a
capacity effect), and model accuracy measurably degrades as token count
grows even before the window fills ("context rot"). A bigger window also
directly increases cost and latency on every request that fills more of
it. The fix for both is deliberate curation — deciding what actually
earns a place in the budget and where it sits — not a bigger container
to be less careful with.

**Red flag:** Argues "just upgrade to the larger-context model" as a
sufficient fix on its own, without naming either mechanism.

**Follow-up:** "Give a concrete example of a system that would still
fail with a 10x larger context window, unchanged otherwise."

**What this proves:** Can communicate the real, structural difference
between capacity and reliable use to a non-specialist stakeholder.

---

### 7. (Architect) Design an org-wide "context readiness" gate that every team's long-running or multi-step LLM feature must pass before its first production deploy. What does it check, and why?

**Strong answer:** Frame the gate around the five-line ledger as
concrete, checkable criteria: (1) an explicit, documented token budget
exists for each of the five lines, including a reserved output
allowance; (2) conversation history has a real eviction/compression
policy (not a blind end-of-window truncation) with a defined test case
demonstrating it preserves a planted load-bearing fact; (3) any
persistent memory layer has a defined recall policy stating what's
re-fetched, when, independent of transcript survival; (4) any multi-
source assembly has a defined resolution rule for when sources
disagree; (5) a context-quality check runs before the assembled context
reaches the model, not only after a bad final answer is observed. Make
it a checklist a team self-attests against with evidence (a link to the
eviction-policy test, the recall-policy spec), not a subjective sign-
off — and allow a documented exception process for genuinely low-stakes,
short-lived interactions.

**Red flag:** Proposes a vague "review board" with no concrete,
checkable criteria, or a gate so heavy every team would need an
exception.

**Follow-up:** "How would this gate differ for a short, single-turn
feature versus a long-running multi-agent pipeline?"

**What this proves:** Architect-level judgment — turns a mental model
into an enforceable, proportionate organizational process.

---

### 8. (Architect) A leadership team asks: "we already have a RAG pipeline and a solid, versioned prompt template — isn't our context handled?" How do you explain what those two things don't cover?

**Strong answer:** A RAG pipeline (`rag-for-everyone`'s subject)
produces a ranked list of *candidate* context — it says nothing about
whether those candidates actually fit the current request's token
budget, what order they should appear in once combined with unrelated
sources, or whether they crowd out conversation history or persistent
memory that also needs space. A versioned prompt template
(`ai-engineering-for-everyone` Chapter 3's subject) manages the
*static* structure a request is built from — it says nothing about the
*dynamic*, per-request content that fills that structure's variable
slots, which is decided fresh on every single call. Neither answers this
chapter's actual questions: is the total assembled context within
budget, is a critical fact positioned where the model will actually use
it, and is memory recalled deliberately rather than accidentally lost.
This chapter's hook, Brackwater's incident, would have passed both a RAG
quality review and a prompt-template code review untouched, because
neither one was the point of failure.

**Red flag:** Claims a good retriever or a well-managed prompt template
already covers context engineering, or can't name a concrete failure
mode neither one would catch.

**Follow-up:** "Where in your org's existing review process would you
insert a context-budget check, and who owns the eviction/recall
policies over time?"

**What this proves:** Can position this course's discipline correctly
relative to its two closest neighbors without conflating them.

## Strategy Tips

- Ground every answer in a specific ledger line's mechanism, not just
  its name — interviewers at every level probe past the label.
- For senior/architect questions, always name a concrete trade-off or
  prioritization, not a claim that every line matters equally in every
  context.
- If you're new to engineering interviews: it's fine to think out loud
  by naming the specific failure mode first ("what would actually go
  wrong here, and which ledger line would have caught it") — that's
  exactly the reasoning this chapter's walkthrough modeled.
