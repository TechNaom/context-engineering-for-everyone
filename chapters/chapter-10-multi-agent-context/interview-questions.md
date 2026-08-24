# Chapter 10 Interview Questions: Context Engineering for Multi-Agent Systems

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) Every one of GrantPilot's sub-agents reasoned correctly about whatever data it was actually shown. Why did the pipeline still recommend denying the wrong applicant?

**Strong answer:** The failure was never in any individual sub-agent's
own reasoning — it was in what the orchestrator decided to hand each
step. The orchestrator appended every applicant's own record to a
single, ever-growing session history, current applicant last, and cut
that history off wherever a step's own token budget ran out. By
Applicant 12's own turn, eleven prior applicants' own records already
filled the Recommendation Agent's own budget, and Applicant 12's own
data — appended last — never made it in at all. The Recommendation
Agent, asked to reason about "the applicant most recently added to the
log," correctly reasoned about whatever record actually survived the
cutoff, which happened to be a different, already-decided applicant.

**Red flag:** Blames the Recommendation Agent's own reasoning, the
Eligibility or Budget agents, or "the model getting confused," rather
than the orchestrator's own unscoped, ever-growing hand-off.

**Follow-up:** "If the Recommendation Agent had been told explicitly
which applicant ID was current, would that have fixed the underlying
gap?"

**What this proves:** Understands that correct per-agent reasoning is
not the same as a well-scoped pipeline — this chapter's central
distinction.

---

### 2. (Beginner) What does "multi-agent context engineering" mean, in one sentence a non-technical stakeholder would understand?

**Strong answer:** When a task is broken into steps handled by an
orchestrator and several specialized sub-agents, someone has to decide,
for each step, exactly which facts and which earlier steps' own findings
it actually needs — not hand every step the entire history of everything
the whole pipeline has ever processed, and not let one already-finished
case's own conclusions leak into the next case's own review just because
they ran back to back in the same session.

**Red flag:** Describes it as simply "connecting the agents together,"
with no mention of per-step scoping, curated hand-offs, or isolating one
unit of work's own context from the next.

**Follow-up:** "Is this the same thing as building or prompting one of
the individual agents in the pipeline?"

**What this proves:** Can distinguish this chapter's inter-step/inter-agent
scoping job from `ai-coding-agents-for-everyone`'s own single-agent-loop
subject.

---

### 3. (Intermediate) A teammate says: "each of our pipeline's steps only ever sees the current request's own data, so our multi-agent context is solid." How do you respond?

**Strong answer:** Scoping each step to the current request's own data is
a real, worthwhile improvement over an unscoped full session history,
and worth keeping — but it says nothing about whether that scoped
context actually gets reset between one unit of work and the next. This
chapter's own second live-capture pair shows exactly this gap: even with
each step correctly scoped to "the current household" in general, a
prior household's own already-resolved finding can still linger in a
shared working context that was never explicitly cleared, and bleed into
the next household's own review.

**Red flag:** Treats per-request scoping as sufficient on its own, or
conflates "each step only receives request-shaped data" with
"unit-of-work boundaries are actually enforced."

**Follow-up:** "What does your pipeline do right now, concretely, at the
moment one request finishes and the next one begins?"

**What this proves:** Understands the real gap between per-step scoping
and full unit-of-work isolation.

---

### 4. (Intermediate) How is this chapter's subject different from what `ai-coding-agents-for-everyone` teaches?

**Strong answer:** That course goes deep on building, prompting, and
operating a single coding agent — its own agentic loop, its own tools,
reviewing its own generated diffs, sandboxing and CI-hardening it. Every
outcome in its own 13-chapter roadmap is phrased in terms of one agent
working on one codebase; the closest chapter (Chapter 6, context windows
and codebase-scale understanding) is about that one agent's own context
budget against a large codebase, not about what context a *second* agent
or pipeline step should or shouldn't receive from the first. This
chapter assumes each individual step or sub-agent already works
correctly on its own and asks a different question entirely: what does
a *given* step or sub-agent in a *larger* pipeline actually need from
everything that came before it, and how does context get isolated
between independent units of work run through that same pipeline.

**Red flag:** Says the two courses are "basically the same because
they're both about agents," without naming the actual boundary (one
agent's own internals vs. what a step or sub-agent receives from the
rest of a multi-step/multi-agent system).

**Follow-up:** "If a team is building a single coding agent with no
orchestrator and no sub-agents at all, does this chapter's own recipe
apply to them?"

**What this proves:** Can articulate the specific, re-verified boundary
between this chapter and `ai-coding-agents-for-everyone`, not just that
"they're different courses."

---

### 5. (Senior) You're reviewing a new multi-step pipeline before it ships. What do you check beyond "every step's own output is correct when tested in isolation"?

**Strong answer:** Whether each step's own context contract is
explicitly scoped, rather than inheriting whatever the orchestrator
happens to have accumulated by that point; whether each step's context
is budgeted as its own ledger line rather than sharing one implicit pool
with every other step; whether prior steps' outputs arrive as curated,
typed results rather than raw reasoning transcripts; whether context is
actually reset at each unit-of-work boundary, not just scoped in
principle; and whether any sub-agent receives only its own delegated
sub-task rather than the orchestrator's full session. A pipeline can
pass every per-step unit test and still fail exactly the way GrantPilot's
own hook did, because per-step correctness was never the thing that
broke.

**Red flag:** Treats "each step passed its own unit tests" as sufficient
evidence the pipeline's own context handling is sound.

**Follow-up:** "Walk me through what happens to this pipeline's own
working context the moment one unit of work finishes and a new one
begins."

**What this proves:** Reviews pipeline-level context handling as its own
distinct risk surface, not assumed covered by per-step correctness
testing.

---

### 6. (Senior) How do you decide how much engineering investment a given pipeline's own context scoping deserves?

**Strong answer:** By how many independent units of work the pipeline
processes per session and how costly a cross-unit contamination failure
would be — a pipeline that runs once per session with no accumulated
history has little to isolate; a long-running pipeline processing dozens
of independent cases back to back, the way GrantPilot does across a
review cycle, has a compounding token cost and a compounding
contamination risk that gets worse with every additional unit processed
in the same session. The worked math in this chapter shows this
concretely: an unscoped pipeline's own per-step token cost scales
directly with how many units of work have already been processed this
session, while a properly scoped pipeline's own per-step cost stays flat
regardless of session length.

**Red flag:** Applies the same fixed level of scoping rigor to every
pipeline regardless of session length or unit-of-work count, or assumes
a pipeline that works correctly in a short test session will behave the
same way after fifty units of work in production.

**Follow-up:** "If this pipeline currently only ever processes one unit
of work per session, does it still need Step 4's own unit-of-work
isolation?"

**What this proves:** Applies proportional engineering judgment rather
than a uniform standard, scaled to session length and unit-of-work
volume specifically.

---

### 7. (Architect) Design a lightweight governance process so every multi-step or multi-agent pipeline in a production system actually gets its context scoping reviewed, not just its per-step correctness tested.

**Strong answer:** A short checklist attached to each pipeline's own
design review, distinct from its functional test suite: (1) does every
step have an explicit, written context contract naming exactly what
upstream facts and prior-step outputs it needs; (2) is each step's
context budgeted as its own ledger line in the system's own token
budget documentation; (3) do prior steps hand off curated, typed results
rather than raw reasoning transcripts; (4) is there an explicit,
testable reset or eviction point at each unit-of-work boundary; (5) does
every sub-agent's own delegated payload get audited for whether it
includes any other unit of work's own data. Each item should be
checkable against the pipeline's own code, not just its documentation —
this chapter's own `full_pipeline.py` and `ledger_and_eviction.py` show
that all five are small enough to assert against directly in a script,
not just describe in a design doc.

**Red flag:** Proposes a purely documentation-based review with no
mechanism to verify the pipeline's own code actually implements the
scoping it claims, or a checklist that only fires once at initial design
rather than being re-checked as a pipeline's own step count or expected
session length changes.

**Follow-up:** "How would this checklist have caught GrantPilot's own
hook failure before it shipped?"

**What this proves:** Designs governance around this chapter's actual
recipe, assertable against real code, not a paperwork exercise disconnected
from what the pipeline's own code does.

---

### 8. (Architect) Leadership says: "our new model can hold a much larger context window, so we can just send the full session history to every step and every sub-agent — do we still need per-step scoping, curated hand-offs, and unit-of-work isolation?"

**Strong answer:** Yes, on both cost and correctness grounds, and this
chapter's own worked math and live captures show why a bigger window
doesn't resolve either one. On cost: GrantPilot's own naive pipeline
used 8,420 tokens across four steps to review one applicant after just
eleven prior applicants, a cost that scales linearly with every
additional unit of work processed in the same session regardless of how
large the window is — a bigger window raises the ceiling before this
becomes an outright overflow, but the token cost (and the real-money
cost behind it) keeps compounding either way, echoing Anthropic's own
reported finding that multi-agent systems already run roughly 15x the
token cost of a single chat interaction, before this pattern is added on
top. On correctness: this chapter's own live captures showed contamination
failures that were never actually about running out of room — the naive,
unevicted eligibility check confidently borrowed a prior applicant's own
"eligible" finding for a new applicant with plenty of budget to spare,
because nothing about a bigger window stops a resolved finding from one
completed unit of work from being mistaken for the current one's own
finding, if nothing evicts it.

**Red flag:** Treats "the window is big enough to hold everything" as
equivalent to "the model will correctly attribute everything in it to
the right unit of work," or ignores the compounding, real token cost of
carrying every unit of work's own full history into every subsequent
step regardless of window size.

**Follow-up:** "If cost weren't a constraint at all, would eviction
between units of work still matter?"

**What this proves:** Distinguishes a context-window-capacity argument
from a context-scoping-correctness argument — the second doesn't go away
just because the first gets easier.
