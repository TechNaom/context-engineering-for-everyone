# Chapter 11 Interview Questions: Context Isolation and Scoping

Grouped by level — beginner, intermediate, senior, architect. Each includes
a strong answer, a red flag, a follow-up, and what the question actually
proves. This is the plain-text companion to `interview-questions.html`.

---

### 1. (Beginner) Vesteroak's Appeals Reviewer Agent was deliberately isolated from the Initial Determination Agent's own opinion, for exactly the right reason. Why did it still uphold the wrong denial?

**Strong answer:** The isolation goal itself was correct — an appeals
review should form an independent judgment, not simply agree with a
prior agent's own conclusion. The failure was in how broadly the
isolation boundary was drawn: instead of stripping specifically the
Initial Determination Agent's own reasoning and conclusion, the
orchestrator's own implementation stripped everything associated with
that step, including a shared, objective fact both stages were supposed
to draw from — the current eligibility threshold. With that fact gone,
the Appeals Reviewer fell back to a stale default baked into its own
base instructions and reached the wrong conclusion for a different
reason than the original denial.

**Red flag:** Says the isolation itself was the mistake, or argues
Vesteroak should never isolate the Appeals Reviewer from the Initial
Determination Agent at all — missing that the isolation goal was correct
and the scoping of it was wrong.

**Follow-up:** "If the shared eligibility threshold had been included but
the Initial Determination Agent's own reasoning trace also leaked in,
would that be the same failure or a different one?"

**What this proves:** Understands that a correctly-motivated isolation
boundary and a correctly-scoped one are two separate claims — this
chapter's central distinction.

---

### 2. (Beginner) What does "context isolation" mean, in one sentence a non-technical stakeholder would understand?

**Strong answer:** Deliberately keeping a specific piece of information
away from a specific step or agent, on purpose, for a real reason — like
making sure a second reviewer forms their own opinion instead of just
agreeing with the first one — while still making sure that step still
gets whatever objective, shared facts it legitimately needs to do its
job correctly.

**Red flag:** Describes isolation as simply "not sharing everything,"
with no mention of a specific goal, or conflates it with Chapter 10's
own default per-step scoping.

**Follow-up:** "Is isolating a step from something the same thing as that
step just not having a large enough context window?"

**What this proves:** Distinguishes deliberate isolation as its own
design decision from ordinary scoping or budget constraints.

---

### 3. (Intermediate) A teammate says: "our second-opinion agent never sees the first agent's own conclusion, so our isolation is solid." How do you respond?

**Strong answer:** Isolating the second agent from the first agent's own
opinion is real and worth keeping — this chapter's own live captures
showed it directly fixing an anchoring failure. But it says nothing
about whether the isolation boundary was drawn narrowly enough to
preserve everything else the second agent legitimately needs. This
chapter's own hook shows exactly this gap: an Appeals Reviewer correctly
isolated from a prior agent's own opinion, but also cut off from a
shared, current policy fact it needed, producing a wrong outcome despite
the isolation working exactly as intended on the axis it was tested on.

**Red flag:** Treats "isolated from the other agent's opinion" as
equivalent to "correctly scoped," or assumes a contamination check alone
is sufficient evidence the isolation boundary is sound.

**Follow-up:** "What does your second-opinion agent do right now if a
shared fact both agents need changes after the isolation boundary was
built?"

**What this proves:** Understands the real gap between successfully
withholding an opinion and correctly scoping everything else around it.

---

### 4. (Intermediate) How is this chapter's subject different from what Chapter 10 already covers?

**Strong answer:** Chapter 10 decides a pipeline step's own *default*
scope — what it needs from everything that came before it, as an
ordinary design decision, treating any gap between that default and
reality as a bug to fix. This chapter operates one layer inside that:
given that a step's default scope has already been decided, it asks when
a *specific, additional* piece of that scope should be deliberately
walled off from a specific consumer, for a specific reason (an
independent judgment, a reduced blast radius, a bias firewall) — and,
symmetrically, how to keep that deliberate wall from taking more with it
than it meant to.

**Red flag:** Says the two chapters are "basically the same because
they're both about limiting context," without naming the specific
distinction (default scope vs. a deliberate, goal-driven wall inside
that scope).

**Follow-up:** "If a pipeline step's own Chapter 10 scope already
excludes something, does that same exclusion also need this chapter's
own hand-off contract and two-probe testing?"

**What this proves:** Can articulate the layered relationship between
Chapter 10's default scoping and this chapter's own deliberate isolation,
not just that "they're different chapters."

---

### 5. (Senior) You're reviewing a new isolation boundary before it ships. What do you check beyond "the thing it's supposed to withhold is actually withheld"?

**Strong answer:** Whether the isolation goal was written down
specifically enough to distinguish "the prior agent's own opinion" from
"everything associated with that step" (Step 1 and Step 2); whether the
isolated step is run as a genuinely separate call rather than a filter
on a shared history (Step 3); whether an explicit, curated hand-off
contract exists for whatever legitimately needs to cross the boundary
(Step 4); whether the boundary gets re-verified when the shared facts it
depends on change (Step 5); and whether it's been tested with both a
contamination probe and a starvation probe, not just one (Step 6). A
boundary can pass a contamination check perfectly and still fail exactly
the way Vesteroak's own hook did.

**Red flag:** Treats "nothing leaked in that shouldn't have" as
sufficient evidence an isolation boundary is correctly built.

**Follow-up:** "Walk me through what specifically gets stripped by this
boundary, field by field, and why each one is on that list."

**What this proves:** Reviews isolation boundaries against both failure
directions, not just the leak-prevention direction most reviewers
default to checking.

---

### 6. (Senior) How do you decide whether a given step or agent actually needs a deliberate isolation boundary at all, versus just Chapter 10's own ordinary scoping?

**Strong answer:** By whether there's a specific, nameable goal an
ordinary scoped contract doesn't already serve — an independent second
opinion that must not anchor on a first one, a reduced blast radius for
a step that handles untrusted or injected input, or a bias firewall
between two agents whose outputs shouldn't influence each other. If the
answer is "we just don't want to pay the token cost of including it,"
that's Chapter 10's own budgeting question, not an isolation goal — the
two are easy to conflate but call for different tools (a smaller,
curated scope vs. an explicit, goal-driven wall with its own hand-off
contract).

**Red flag:** Applies deliberate isolation machinery (Steps 1-6) to every
excluded field regardless of whether a specific goal motivates it, or
conversely treats every isolation need as solvable by ordinary scoping
alone.

**Follow-up:** "If cost were the only reason a field was excluded, would
this chapter's own two-probe testing still be worth running on it?"

**What this proves:** Distinguishes a deliberate, goal-driven isolation
decision from an ordinary budget-driven scoping decision, applying the
right recipe to each.

---

### 7. (Architect) Design a lightweight governance process so every deliberate isolation boundary in a production system actually gets both failure directions checked, not just leak prevention.

**Strong answer:** A short checklist attached to each isolation
boundary's own design review, distinct from an ordinary scoping review:
(1) is the isolation goal written down specifically enough to name what
must be withheld and why; (2) does the boundary implementation separate
"opinion" fields from "shared, objective fact" fields explicitly, rather
than stripping an entire step's context as one unit; (3) is the isolated
step run as a genuinely separate call; (4) does an explicit, curated
hand-off contract exist for every shared fact that needs to cross; (5)
is there a trigger to re-verify the boundary when the underlying shared
facts change; (6) has the boundary been tested with both a contamination
probe and a starvation probe, with the starvation probe run
independently rather than assumed satisfied by the contamination probe
passing. Each item should be checkable against the boundary's own code,
the same way this chapter's own `isolation_probes.py` asserts both
probes directly rather than describing them only in a design doc.

**Red flag:** Proposes a checklist that only checks for leaks, or one
that treats "the isolation boundary was reviewed once at launch" as
sufficient without a trigger for re-verification when shared facts
change.

**Follow-up:** "How would this checklist have caught Vesteroak's own hook
failure before it shipped?"

**What this proves:** Designs governance that catches both isolation
failure directions symmetrically, assertable against real code, not a
one-sided leak-prevention checklist.

---

### 8. (Architect) Leadership says: "our new model is much harder to manipulate through anchoring, so do we still need deliberate isolation boundaries between agents?"

**Strong answer:** Yes, for two independent reasons this chapter's own
worked math and live captures both support. First, this chapter's own
security-motivated isolation goal (reducing blast radius) has nothing to
do with anchoring resistance at all — keeping credentials and a
compromised or injected context from reaching a second agent's own tools
is a containment property, not a persuasion-resistance property, and a
harder-to-anchor model doesn't change what a compromised context could
still reach if nothing walls it off. Second, even a model that resists
anchoring perfectly still needs Step 2's own opinion/shared-fact
separation and Step 4's own hand-off contract to get the *right* shared
facts through a boundary at all — Vesteroak's own hook failure was never
about anchoring in the first place; it was a pure starvation failure
that a perfectly anchoring-resistant model would still have reproduced,
because the correct threshold was never in its context to reason from.

**Red flag:** Treats "the model resists anchoring better" as equivalent
to "isolation boundaries are no longer needed," conflating the
anchoring-prevention goal with the blast-radius-reduction and
shared-fact-hand-off goals this chapter also covers.

**Follow-up:** "If the model never anchors on anything, does Vesteroak's
own hook failure still happen?"

**What this proves:** Distinguishes isolation's several independent
goals (anchoring prevention, blast-radius reduction, correct shared-fact
hand-off) rather than treating "anchoring resistance" as a stand-in for
all of them.
