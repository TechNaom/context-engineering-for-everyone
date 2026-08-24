# Castellan Fleet Logistics — Context Engineering System Design Document (Reference Solution)

---

## Component 1: DispatchMind

### 1.1 Job-to-be-done

A dispatcher or driver needs a correct, current answer to "what do I do
right now" during an active incident (closure, weather, mechanical
issue) on a live load — someone is actively waiting on the response
within seconds, not hours.

### 1.2 Multi-step/agentic shape

Genuinely multi-agent, not a single call: a Route Agent (replans the
path), a Compliance Agent (checks HOS regulation against the new plan),
and a Customer-Comms Agent (drafts a delay notice when the SLA threshold
is crossed) — three sub-agents per incident, exactly as walked through
in `../lesson.html`'s own worked example.

### 1.3 Context Budget Ledger (Ch. 1-2)

```python
hard_limit = 6000  # incident_replan request type, one turn

ledger = {
    "line1_system": 380,
    "line2_grounding": 2321,
    "line3_history": 844,
    "line4_memory": 1055,
    "line5_working_space": 1400,
}
```

Line 5 is reserved first (1400 tokens) because an incident replan needs
room for multi-step tool-call reasoning plus a longer generated response
(route options and a customer-message draft). Line 1 is small and fixed
(380 tokens — the same system prompt shape for every incident-replan
turn). The remaining 3820 tokens split 55/20/25 across Lines 2-4 because
an incident leans hardest on live grounding (GPS, weather, HOS chunks,
manifest) rather than conversation history or recalled long-term memory
— the same profile the lesson's own worked example uses, validated
against a measured 480-token worst-case floor for Line 2 (three
contradicting live sources needing simultaneous surfacing).

### 1.4 Short-term memory plan (Ch. 3)

A 350-token verbatim window, newest-turn-first, per active incident
conversation thread. Bounded, explicit pinning (not automatic
summarization) for anything a dispatcher manually flags as load-bearing
mid-incident — e.g. a one-time HOS extension waiver granted verbally and
logged — because Chapter 3's own live-tested finding showed a
summarization call cannot be trusted to preserve an arbitrary pinned
fact unprompted.

### 1.5 Long-term memory plan (Ch. 4)

Scoped strictly per driver ID: prior HOS violation history, endorsement
status, and any standing waivers, retrieved only for the driver on the
active load. Every retrieved record carries an explicit staleness check
against its own stated validity window (e.g. a single-use waiver logged
earlier the same shift is retrieved but flagged stale on a second
incident, never silently treated as still active) — the same mechanic
that resolved this chapter's own worked example's waiver conflict.

### 1.6 Compression and ordering plan (Ch. 5-6)

Turns falling out of the verbatim window are compressed extractively
(bullet-style, not narrative prose) with a fidelity check requiring every
load-bearing fact from the original turns to survive verbatim or
near-verbatim in the summary before it's accepted. The assembled bundle
is then reordered per Chapter 6's recipe: the highest-weight live fact
(the incident alert itself) anchored at the front, the live dispatcher
query placed last, closest to generation, and lower-weight content (the
compressed routine summary) moved into the middle — because DispatchMind's
own incident bundles routinely exceed a few hundred words, squarely in
the range Chapter 6's re-verified Lost-in-the-Middle research still
applies to.

### 1.7 Source assembly and retrieval plan (Ch. 7-8)

Four live source types inventoried per incident: GPS telematics, weather/
closure advisories, the load manifest, and the customer SLA document,
each with an explicit authority rank per claim type (live telematics
outranks a static manifest for a live ETA claim; a weather advisory is
the sole authority for route-risk claims). Any two sources making a
conflicting claim on the same fact are resolved by authority rank before
assembly, not left for the model to referee. HOS regulation text is
retrieved with a 0.5 relevance-score floor and fit to a 100-token budget
at a chunk boundary, with each chunk's own regulation citation ID
preserved for the compliance agent's own response.

### 1.8 Tool context and multi-agent/isolation plan (Ch. 9-11)

Each sub-agent gets its own scoped context contract (Chapter 10 Step 1):
the Route Agent sees the closure alert and a curated route-planning tool
result only (raw telemetry dumps and unused fields dropped at a field
boundary, per Chapter 9); the Compliance Agent sees the retrieved HOS
chunks, the long-term waiver record, and the Route Agent's decision; the
Customer-Comms Agent sees only a curated hand-off fact from the
Compliance Agent (`compliant: true/false` plus a plain-language basis
summary) — never the raw regulation text or the Compliance Agent's own
internal reasoning trace, an explicit isolation boundary (Chapter 11 Step
4) drawn specifically to keep an internal regulatory determination out of
a customer-facing message. Both a contamination probe (does regulation
detail ever leak into a customer message) and a starvation probe (does
the Customer-Comms Agent have everything it needs) are run against this
boundary before shipping, per Chapter 11 Step 6.

### 1.9 Context evaluation gate (Ch. 12)

```python
evaluation_gate = {
    "required_facts": [
        "closure_location",
        "reroute_decision",
        "new_eta",
        "compliance_status",
        "customer_notify_decision",
    ],
    "completeness_threshold": 0.9,
    "noise_ratio_max": 0.15,
    "positional_check": True,
}
```

A 90% completeness bar (not 100%) because a small number of
lower-priority fields — e.g. a secondary fuel-stop recommendation — are
useful but not load-bearing for the core replan-and-notify decision. A
15% noise ceiling matches Chapter 12's own established threshold. The
positional check is required (`True`) because incident bundles routinely
exceed a few hundred words and combine several sources, the exact
condition under which Chapter 6's ordering recipe (and thus Chapter 12's
own positional audit) matters most. Per this chapter's own capstone
finding, the required-fact list explicitly names `compliance_status` and
`customer_notify_decision` as their own resolved-value facts, not just
"HOS regulation cited" or "SLA terms present" — the exact gap this
chapter's own Live Capture 2 found a generic required-fact list can
miss.

---

## Component 2: ComplianceLedger

### 2.1 Job-to-be-done

After a route completes, a compliance officer needs a structured,
regulator-ready report entry assembled from that route's own raw logs —
nobody is waiting on it in real time; it's reviewed on the officer's own
schedule, typically within a business day.

### 2.2 Multi-step/agentic shape

Multi-step, but single-agent, not multi-agent: one pass assembles raw
ELD/HOS logs, any DispatchMind incident records generated during the
route, and the driver's long-term compliance history into one structured
entry. There is no real-time decision loop and no sub-agent delegation —
the "steps" are sequential assembly stages (gather logs, resolve
incident cross-references, structure the entry), not independent agents
each making their own call.

### 2.3 Context Budget Ledger (Ch. 1-2)

```python
hard_limit = 8000  # one completed-route compliance entry, single batch pass

ledger = {
    "line1_system": 250,
    "line2_grounding": 4200,
    "line3_history": 300,
    "line4_memory": 1200,
    "line5_working_space": 2050,
}
```

Line 5 is still reserved first, sized larger than DispatchMind's (2050
tokens) because the generated compliance-report entry itself is long-form
structured prose, not a short reply. Line 1 is smaller (250 tokens — no
conversational persona needed for a batch job). Line 2 dominates (4200
tokens) because the raw ELD/HOS logs and any incident records for an
entire completed route are the actual bulk of this component's own
grounding content, unlike DispatchMind's live, comparatively terse
per-incident sources. Line 3 is small (300 tokens — at most a few review
notes from a prior draft) since this is a single-shot batch assembly,
not a live conversation. Line 4 (1200 tokens) recalls the driver's own
long-term compliance history for cross-referencing.

### 2.4 Short-term memory plan (Ch. 3)

Minimal: at most a prior draft's own reviewer comments, if this entry is
a resubmission after a compliance officer requested a correction. No
verbatim conversation window is needed — there is no live back-and-forth
this component participates in.

### 2.5 Long-term memory plan (Ch. 4)

Scoped per driver, same staleness-aware retrieval mechanic as
DispatchMind's own (Section 1.5) — reused, not redesigned, since the
underlying recipe doesn't change with request volume. The key difference
is retrieval scope: DispatchMind recalls only what's relevant to an
active incident; ComplianceLedger recalls the driver's full compliance
history for the report period being filed.

### 2.6 Compression and ordering plan (Ch. 5-6)

Raw logs are compressed to a bounded fidelity-checked summary only where
they exceed the report's own required detail level (e.g. hundreds of
routine, uneventful log entries collapse to a single "no exceptions"
line, while any flagged entry survives verbatim). Ordering matters less
here than for DispatchMind: this is a single-shot generation reviewed in
full by a human, not a live turn where a buried fact risks going
unnoticed by the model mid-conversation — but the positional audit
(Section 2.9) is still run, because the raw-log bundle is long enough
(often several thousand tokens) that a single decisive flag could still
land in a low-attention position within one generation pass.

### 2.7 Source assembly and retrieval plan (Ch. 7-8)

Three source types: raw ELD/HOS logs (system of record, highest
authority), DispatchMind's own incident records for the route (secondary,
cross-referenced against the logs), and the driver's long-term compliance
history (context, not authority, for the current filing). Retrieval
integration is lighter here than for DispatchMind — logs are pulled by
route ID, not ranked by a relevance score — but the same relevance-floor
and chunk-boundary-fitting mechanics apply when a route's own log volume
exceeds Line 2's budget.

### 2.8 Tool context and multi-agent/isolation plan (Ch. 9-11)

A single tool call retrieves the route's raw log bundle; its result is
curated to the fields the report template actually requires (driver ID,
route ID, HOS summary, flagged exceptions) before assembly, the same
field-boundary curation Chapter 9 defines. No multi-agent isolation
boundary is needed — there is only one agent, and no customer-facing
output this component ever produces that a compliance determination
needs to be isolated from.

### 2.9 Context evaluation gate (Ch. 12)

```python
evaluation_gate = {
    "required_facts": [
        "route_id",
        "driver_id",
        "hos_summary",
        "incident_flags",
        "compliance_determination",
    ],
    "completeness_threshold": 0.95,
    "noise_ratio_max": 0.10,
    "positional_check": True,
}
```

A stricter 95% completeness bar and a tighter 10% noise ceiling than
DispatchMind's, because a filed compliance-report entry is a regulatory
record — the consequence of a missing or noisy fact here is slower and
harder to correct than DispatchMind's own real-time replan, even though
nobody is waiting on the answer in real time. Positional check remains
`True` for the reason given in Section 2.6: long raw-log bundles still
carry positional risk within a single generation pass, independent of
whether a human later reviews the result.

---

## Part 3: Cross-component synthesis

### 3.1 Why these two components' recipe treatments diverge

The divergence traces to three concrete facts, not labels: DispatchMind
is real-time and user/driver-facing (someone waits seconds for an
answer), which is why its short-term memory, ordering, and isolation
plans are all built around a live, per-incident conversation loop and a
genuine multi-agent boundary; ComplianceLedger is asynchronous and
internal-only, which is why it needs no live verbatim window and no
isolation boundary at all. Both components still need a full-depth
evaluation gate and a full Context Budget Ledger — not because they're
similar in shape, but because both have a real, if different, cost of
being wrong (a bad live replan vs. an incomplete regulatory filing).
DispatchMind's Line 2 dominance reflects live, terse, multi-source
grounding; ComplianceLedger's Line 2 dominance reflects a much larger
volume of a single source type (raw logs). The recipes are the same
eleven in both cases — what changes is which ones run at meaningfully
different intensity, and why.

### 3.2 What would change each component's profile

**DispatchMind:** if Castellan expanded into regions with much sparser
cell coverage, live GPS/weather grounding would become intermittently
unavailable mid-incident — this would force the Long-Term Memory plan
(Section 1.5) to carry more weight as a fallback grounding source when
Line 2's live feeds go stale, and would tighten the staleness-check
mechanic from "flag and surface" to "flag, surface, and explicitly warn
the agent grounding may be out of date."

**ComplianceLedger:** if a regulator began requiring same-day filing
instead of a multi-day review window, this component would need a
review-turnaround SLA for the first time — pushing its own Short-Term
Memory plan (Section 2.4) from "minimal, at most one resubmission's
comments" toward something closer to DispatchMind's own bounded verbatim
window, since a compliance officer would now need to interact with a
draft in near-real time rather than reviewing it on their own schedule.

### 3.3 Shared infrastructure risk

Both components share the same long-term memory store (the driver
compliance-history retrieval mechanic in Sections 1.5/2.5) and the same
tool-result curation library (Chapter 9's field-boundary curation, used
by both the DispatchMind route tool and the ComplianceLedger log-fetch
tool). The real risk: a change to the shared curator's own field-allow
list, made to fix a DispatchMind-specific problem (e.g. adding a new
route-tool field DispatchMind needs), could silently change which fields
ComplianceLedger's own log-fetch tool result includes too, since both
call the same curation function. The guard: the field-allow list itself
must be a per-caller configuration value, not a single shared default —
each component declares its own required-fields list explicitly, and the
shared curator only ever curates against the caller's own declared list,
never a library-wide default either component could silently inherit a
change from.
