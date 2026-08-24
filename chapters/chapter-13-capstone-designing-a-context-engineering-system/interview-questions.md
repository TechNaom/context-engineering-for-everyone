# Chapter 13 Interview Questions: Capstone: Designing a Context Engineering System

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) This chapter didn't teach a twelfth technique. What did it actually teach?

**Strong answer:** How the eleven recipes from Chapters 1-12 run
together, in the order a real turn actually executes them, and the
handoffs between them — the budget ledger reserving room before a tool
call runs, a compressed summary and recalled memory both becoming inputs
to the ordering recipe, resolved sources and retrieved chunks both
feeding a tool-context step, and a finished bundle finally passing
through an evaluation gate before generation. No single earlier chapter
could show all eleven interacting, because doing so requires one
scenario complex enough to need every recipe at once.

**Red flag:** Names a new recipe or technique this chapter supposedly
introduced, or describes the chapter as "a review," missing that
composition (the order and handoffs) is itself new content, not a repeat
of Chapters 1-12.

**Follow-up:** "Name one place in the DispatchMind worked example where
two different chapters' own recipes touched the same underlying fact."

**What this proves:** Understands the difference between a recipe and
the composition of many recipes — the chapter's own central distinction.

---

### 2. (Beginner) In DispatchMind's incident-replan turn, why does the same waiver get two different freshness verdicts from two different recipes?

**Strong answer:** Chapter 3's short-term pin and Chapter 4's long-term
staleness check answer different questions. The pin asks "did a
dispatcher explicitly flag this as load-bearing in the live
conversation" and correctly says yes; the staleness check asks "has this
record's own stated validity window expired" and correctly says yes too,
because the long-term copy of the same waiver was logged single-use and
this is a second incident on the same shift. Both verdicts are correct
because they're answering different things.

**Red flag:** Calls this a bug or a contradiction that needs fixing,
rather than recognizing it as two independently correct mechanics
checking different properties of the same fact.

**Follow-up:** "What would happen if a system only ran one of these two
checks?"

**What this proves:** Understands that composing recipes can surface
genuine, non-contradictory disagreements — not just additive coverage.

---

### 3. (Intermediate) Chapter 12's deterministic evaluation gate passed on DispatchMind's final bundle at 100% completeness. What did the live LLM completeness check still find?

**Strong answer:** The bundle stated the compliance basis (the
regulation clause and the reasoning not to rely on the stale waiver) but
never stated the resolved `compliant: true` fact itself as literal text
— a real gap the hand-labeled required-fact list missed, because
supporting reasoning and an explicit resolved value are not the same
thing. This shows a deterministic gate passing is a necessary floor, not
a guarantee that the bundle is actually complete in every sense that
matters.

**Red flag:** Says the gate "failed" or was "wrong" — it correctly
computed completeness against the required-fact list it was given; the
finding is that the list itself needed a fix, not that the gate's own
arithmetic was broken.

**Follow-up:** "How would you fix the required-fact list to catch this
specific gap going forward?"

**What this proves:** Distinguishes between a check's own logic being
correct and the check's own inputs being complete — a distinction that
matters well beyond this one example.

---

### 4. (Intermediate) Live Capture 1 showed a customer-message draft that echoed `[eta_delay_min]` literally instead of substituting 95. Did the isolation boundary fail?

**Strong answer:** No — the isolation boundary held perfectly; nothing
about HOS regulation, the waiver, or the Compliance Agent's own internal
reasoning leaked into the message. The unsubstituted placeholder is a
separate, generation-quality defect on the isolated side, unrelated to
whether the right content crossed the boundary. Isolation correctness
and generation quality are two different things to verify.

**Red flag:** Concludes the isolation design itself is flawed, or
conflates "the agent produced a bad draft" with "the agent didn't have
what it needed" — the starvation probe specifically showed it did have
what it needed; it just didn't use one field correctly.

**Follow-up:** "What's the minimal fix here — a prompt-template change,
or a deterministic substitution step, and why?"

**What this proves:** Can separate a context engineering failure from a
generation failure, even when both are visible in the same output.

---

### 5. (Senior) A learner's capstone design document gives ComplianceLedger the exact same eleven-recipe treatment as DispatchMind, at the same depth throughout. Is this a strong submission?

**Strong answer:** No — it's the specific failure mode the rubric's
"mechanical copy" criterion is built to catch. ComplianceLedger is
asynchronous, single-agent, and internal, with a different real profile
than DispatchMind's real-time, multi-agent, user-facing shape; a correct
design should show several recipes applying at meaningfully lighter
depth (no live verbatim window needed, no isolation boundary needed) and
at least one applying at a *stricter* depth than DispatchMind's own
(a tighter completeness/noise threshold, because a filed compliance
record is harder to correct than a live replan). Uniform treatment
across genuinely different components signals the profile was never
actually applied.

**Red flag:** Argues uniform treatment is "safer" or "more thorough,"
missing that the L4 tier is specifically testing whether depth decisions
track real facts about each component, not defaulting to maximum
everywhere.

**Follow-up:** "Which specific recipe would you expect to diverge most
strongly between the two components, and why?"

**What this proves:** Can apply proportional judgment, not just recall
which recipes exist — the architect-level skill this tier is built to
test.

---

### 6. (Senior) The capstone's own cited source, Anthropic's "Building Effective Agents," warns against adding complexity unless it demonstrably improves outcomes. How does DispatchMind's own three-sub-agent design satisfy that bar rather than violate it?

**Strong answer:** DispatchMind's own complexity (three sub-agents, one
isolation boundary, contradiction resolution across four sources) is
justified by genuine, independently-motivated needs already present in
the scenario: real-time route replanning is a different job than HOS
compliance reasoning, which is a different job than customer-facing
communication, and the isolation boundary exists specifically because a
customer message drafted with visibility into an internal regulatory
dispute is a real professionalism and correctness risk, not an
abstraction added for its own sake. The test isn't "is this
architecture complex" but "does each piece of the complexity trace to a
real requirement this specific scenario has."

**Red flag:** Argues multi-agent designs are inherently better, or that
DispatchMind's design proves more sub-agents is always the right
architecture — missing that the citation's own point is restraint, and
ComplianceLedger's own single-agent design in the same business problem
is the counter-example proving the point.

**Follow-up:** "Where in the capstone's own rubric does this restraint
principle actually get graded?"

**What this proves:** Understands architectural complexity as a
cost that needs justifying per-component, not a feature to maximize.

---

### 7. (Architect) Design the context engineering treatment for a third, hypothetical Castellan component — a driver-facing safety-alert push notification triggered automatically by a sudden hard-braking event, no human review before it fires. Which recipes need the deepest treatment, and which barely apply?

**Strong answer:** Budget allocation (Ch. 1-2) and the evaluation gate
(Ch. 12) need the deepest treatment, because this is the one Castellan
component with no human review step at all before an action fires —
every completeness and noise check has to run automatically and
correctly with zero safety net, and the budget has to guarantee Line 5
(Working Space) is never starved by an oversized Line 2, since a
delayed or malformed alert has real safety consequences. Short-term and
long-term memory barely apply — there's no multi-turn conversation and
minimal need for recalled history in a single-purpose, single-trigger
alert. Multi-agent isolation doesn't apply at all — there's only one
step. Source assembly stays simple (one source: the braking-event
sensor feed) but tool-context curation matters a lot, since the raw
sensor payload almost certainly needs aggressive field-boundary curation
before it becomes a two-sentence alert.

**Red flag:** Applies uniform "full" depth everywhere out of caution, or
misses that "no human review" is exactly the fact that should push
evaluation-gate depth to maximum rather than being treated as a reason
to skip it.

**Follow-up:** "How would positional ordering (Ch. 6) apply, or not, to
a two-sentence push notification?"

**What this proves:** Can extend this course's own recipe stack to a
genuinely new scenario, under interview pressure, without a written
business problem already scoping the answer — the actual skill the L4
capstone is built to certify.

---

### 8. (Architect) The course opened with a single mental model in Chapter 1 — every token competes for a limited, costed budget. What, if anything, about that model changed by Chapter 13?

**Strong answer:** Nothing about the model itself changed — Line 1 of
DispatchMind's own budget ledger in this chapter's worked example is the
same five-line ledger Chapter 1 introduced. What changed is everything
built on top of it across twelve chapters: memory, compression,
ordering, assembly, retrieval, tool use, multi-agent isolation, and
evaluation, each engineered once, each still running, unmodified, inside
one real turn of one real system. The mental model was never revised
because it didn't need to be — every later chapter's own recipe is a
constraint operating *within* that same budget, not a replacement for
it.

**Red flag:** Claims the budget model was "extended" or "upgraded" by
later chapters, missing that its own stability across twelve chapters of
added complexity is itself the point — a foundational mental model
should still hold, unmodified, once a system built on top of it gets
genuinely complex.

**Follow-up:** "If you had to defend, in one sentence, why Chapter 1's
model didn't need a Chapter 13 revision, what would you say?"

**What this proves:** Can articulate what actually held constant across
an entire course, not just recall its final, most complex example — the
kind of synthesis a real architecture review expects from a senior
engineer defending a system end to end.
