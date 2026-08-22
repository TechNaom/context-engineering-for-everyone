"""
Chapter 1 Exercises: The Context Budget

Scenario for these exercises (deliberately different from the lesson's
Brackwater/SignalDesk hook, so you apply the framework fresh, not just
recall the lesson's answers):

    Cobalt Home Security is a fictional home-security company. Its
    customer chat assistant, GuardLine, walks customers through alarm
    troubleshooting, pulls relevant knowledge-base articles, and can
    call a tool to check a customer's account and equipment record.
    GuardLine calls a hosted model API for every turn, at real
    per-token cost, inside a real, fixed context-window limit.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
There's no hidden grading server -- the answer key lives in this file,
the same way the lesson's own walkthrough table is fully worked out for
you to check your reasoning against.
"""

LEDGER_LINES = {
    "L1": "System Instructions",
    "L2": "Grounding Context",
    "L3": "Conversation History",
    "L4": "Recalled Long-Term Memory",
    "L5": "Working Space",
}

# ---------------------------------------------------------------------------
# Exercise 1 -- Map five GuardLine failure descriptions to the single ledger
# line that best explains each one. Use the line IDs above (e.g. "L1").
# ---------------------------------------------------------------------------
EXERCISE_1_FAILURES = {
    "bloated_system_prompt": (
        "GuardLine's system prompt has grown to include six paragraphs of "
        "legal boilerplate and rarely-needed edge-case instructions "
        "appended over time, consuming a large fixed share of the budget "
        "on every single request regardless of need."
    ),
    "no_kb_eviction": (
        "GuardLine keeps every knowledge-base article it has ever "
        "retrieved in a session inside the request, even ones about "
        "topics the conversation moved past ten turns ago."
    ),
    "unbounded_transcript": (
        "The full raw conversation transcript is sent every turn with no "
        "summarization and no cap, so a long session eventually exceeds "
        "the window and the oldest turns are blindly cut."
    ),
    "no_persistent_recall": (
        "A customer's stated equipment model number, mentioned once early "
        "in a long session, is never re-fetched from the account system "
        "on later turns, relying only on it surviving in the raw "
        "transcript."
    ),
    "no_output_reservation": (
        "GuardLine's budget calculation only accounts for input content; "
        "it doesn't reserve any room for its own response, so long "
        "answers get cut off mid-sentence when the budget is already "
        "nearly full."
    ),
}

# TODO 1: fill in the ledger line ID (e.g. "L1") that best explains each
# failure above.
exercise_1_answers = {
    "bloated_system_prompt": "",    # TODO
    "no_kb_eviction": "",           # TODO
    "unbounded_transcript": "",     # TODO
    "no_persistent_recall": "",     # TODO
    "no_output_reservation": "",    # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 -- Line dependency. For each pair below, decide whether the
# FIRST condition would make the SECOND outcome more likely (True) or the
# two are independent (False).
# ---------------------------------------------------------------------------
EXERCISE_2_PAIRS = [
    ("No eviction policy on grounding context (L2)", "Conversation history (L3) hits its truncation limit sooner"),
    ("No persistent memory recall (L4)", "A bug in the tool-calling schema validation (unrelated)"),
    ("No output reservation (L5)", "Mid-sentence truncated responses reaching the customer"),
]

# TODO 2: fill in True/False for each pair above, in order.
exercise_2_answers = [
    None,  # TODO -- unmanaged L2 growth and earlier L3 truncation
    None,  # TODO -- missing L4 recall and an unrelated schema bug
    None,  # TODO -- no L5 reservation and truncated responses
]

# ---------------------------------------------------------------------------
# Exercise 3 (production-gear: memory) -- Given four candidate fixes for
# GuardLine, mark which ones actually address the Conversation History (L3)
# line specifically (True) versus which address a different ledger line
# entirely (False).
# ---------------------------------------------------------------------------
EXERCISE_3_FIXES = {
    "add_summarization": "Periodically summarize older turns into a compact running summary, replacing the raw text once a turn ages out of a recent window.",
    "add_kb_reranking": "Re-rank and drop knowledge-base hits that are no longer topically relevant to the current sub-topic.",
    "pin_critical_facts": "Detect certain fact types (equipment model, account tier) and re-fetch them from the account system every turn regardless of transcript state.",
    "trim_system_prompt": "Audit the system prompt and remove rarely-used boilerplate paragraphs.",
}

# TODO 3: fill in True/False for each fix above -- does it address L3
# (Conversation History) specifically?
exercise_3_answers = {
    "add_summarization": None,   # TODO
    "add_kb_reranking": None,    # TODO
    "pin_critical_facts": None,  # TODO
    "trim_system_prompt": None,  # TODO
}

# ---------------------------------------------------------------------------
# Exercise 4 (production-gear: budget arithmetic) -- GuardLine's model has an
# 8,000-token context window. System instructions use a fixed 500 tokens.
# GuardLine reserves 1,200 tokens for its own output (Line 5), and budgets
# 1,800 tokens for grounding context (Line 2). Every remaining token goes to
# conversation history (Line 3). Each turn (one user message + one assistant
# reply) averages 150 tokens. Compute:
#   (a) the token budget remaining for conversation history (an integer)
#   (b) the maximum number of FULL turns that fit in that budget before
#       compression must kick in (integer, rounded down)
# ---------------------------------------------------------------------------
CONTEXT_WINDOW_TOKENS = 8_000
SYSTEM_INSTRUCTIONS_TOKENS = 500
OUTPUT_RESERVATION_TOKENS = 1_200
GROUNDING_CONTEXT_BUDGET_TOKENS = 1_800
TOKENS_PER_TURN = 150

exercise_4_history_budget_tokens = None  # TODO: integer
exercise_4_max_turns = None              # TODO: integer, rounded down

# ---------------------------------------------------------------------------
# Exercise 5 (production-gear: memory policy) -- GuardLine's conversation
# history is about to exceed its budget. Pick the ONE eviction policy below
# that is the most appropriate first fix (write the option's key, e.g. "b").
#   a. Drop the oldest turns blindly, keeping only what fits under the cap.
#   b. Summarize turns older than the most recent N into a compact running
#      summary, and keep the most recent N turns verbatim.
#   c. Send the full transcript anyway and let the API return an error.
#   d. Randomly sample which turns to keep, to avoid any systematic bias.
# ---------------------------------------------------------------------------
exercise_5_answer = ""  # TODO: "a", "b", "c", or "d"

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: ordering) -- GuardLine's context for a given
# turn includes one critical fact (the customer's equipment model) buried
# among a lot of routine troubleshooting chatter. Per this chapter's
# lost-in-the-middle finding, where should the critical fact be placed in
# the assembled context to make the model most likely to actually use it?
# Pick the ONE option below (write the option's key).
#   a. Only at the very beginning of the context, and nowhere else.
#   b. Exactly in the middle of the context, where it's "centrally located."
#   c. At the beginning AND again near the end, close to the current query.
#   d. Position doesn't matter as long as the fact is included somewhere.
# ---------------------------------------------------------------------------
exercise_6_answer = ""  # TODO: "a", "b", "c", or "d"

# ---------------------------------------------------------------------------
# Exercise 7 (production-gear: context-health monitoring) -- Name ONE
# concrete monitor (a specific metric plus a specific threshold or
# comparison) that would have caught GuardLine's conversation-history budget
# growing dangerously large BEFORE it caused a truncation-driven incident,
# not after. Must mention both a metric AND a threshold/comparison to pass.
# ---------------------------------------------------------------------------
exercise_7_monitor = ""  # TODO: one concrete sentence

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: completeness gate) -- Before a context-
# engineered feature ships, a real team checks that every one of the 5
# ledger lines was at least considered (even if the answer for one is "not
# applicable here, because..."). Fill in exercise_8_considered with all 5
# line IDs you considered while working through Exercises 1-7 above.
# ---------------------------------------------------------------------------
exercise_8_considered = set()  # TODO: add all 5 "L1".."L5" IDs


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_exercise_1():
    key = {
        "bloated_system_prompt": "L1",
        "no_kb_eviction": "L2",
        "unbounded_transcript": "L3",
        "no_persistent_recall": "L4",
        "no_output_reservation": "L5",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [True, False, True]
    correct = sum(
        1 for i, v in enumerate(key)
        if i < len(exercise_2_answers) and exercise_2_answers[i] is v
    )
    return correct, len(key)


def score_exercise_3():
    key = {
        "add_summarization": True,
        "add_kb_reranking": False,
        "pin_critical_facts": False,
        "trim_system_prompt": False,
    }
    correct = sum(1 for k, v in key.items() if exercise_3_answers.get(k) is v)
    return correct, len(key)


def score_exercise_4():
    correct = 0
    total = 2
    expected_history_budget = (
        CONTEXT_WINDOW_TOKENS
        - SYSTEM_INSTRUCTIONS_TOKENS
        - OUTPUT_RESERVATION_TOKENS
        - GROUNDING_CONTEXT_BUDGET_TOKENS
    )
    expected_max_turns = expected_history_budget // TOKENS_PER_TURN
    if exercise_4_history_budget_tokens == expected_history_budget:
        correct += 1
    if exercise_4_max_turns == expected_max_turns:
        correct += 1
    return correct, total


def score_exercise_5():
    correct = 1 if exercise_5_answer.strip().lower() == "b" else 0
    return correct, 1


def score_exercise_6():
    correct = 1 if exercise_6_answer.strip().lower() == "c" else 0
    return correct, 1


def score_exercise_7():
    text = exercise_7_monitor.lower()
    metric_words = ["token", "budget", "%", "percent", "history", "context", "size", "length"]
    threshold_words = ["threshold", "alert", "exceed", "%", "percent", "trailing", "average", "cap", "limit", "rolling"]
    has_metric = any(w in text for w in metric_words)
    has_threshold = any(w in text for w in threshold_words)
    correct = int(has_metric) + int(has_threshold)
    return correct, 2


def score_exercise_8():
    all_five = set(LEDGER_LINES.keys())
    correct = len(all_five & exercise_8_considered)
    return correct, len(all_five)


def main():
    exercises = [
        ("Exercise 1 -- map failures to ledger lines", score_exercise_1),
        ("Exercise 2 -- ledger line dependency reasoning", score_exercise_2),
        ("Exercise 3 -- evaluate which fixes address Conversation History", score_exercise_3),
        ("Exercise 4 -- context budget arithmetic", score_exercise_4),
        ("Exercise 5 -- memory eviction policy selection", score_exercise_5),
        ("Exercise 6 -- lost-in-the-middle ordering decision", score_exercise_6),
        ("Exercise 7 -- context-health monitor design", score_exercise_7),
        ("Exercise 8 -- full-ledger completeness check", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 1 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every failure correctly mapped to the ledger.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
