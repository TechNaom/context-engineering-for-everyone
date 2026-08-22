"""
Chapter 1 Exercises: The Context Budget -- REFERENCE SOLUTION

See starter.py for the full scenario description (Cobalt Home Security's
GuardLine) and task instructions. This file is the fully filled-in
reference and scores a perfect total when run.
"""

LEDGER_LINES = {
    "L1": "System Instructions",
    "L2": "Grounding Context",
    "L3": "Conversation History",
    "L4": "Recalled Long-Term Memory",
    "L5": "Working Space",
}

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

# Exercise 1: map each failure to its ledger line.
exercise_1_answers = {
    "bloated_system_prompt": "L1",
    "no_kb_eviction": "L2",
    "unbounded_transcript": "L3",
    "no_persistent_recall": "L4",
    "no_output_reservation": "L5",
}

EXERCISE_2_PAIRS = [
    ("No eviction policy on grounding context (L2)", "Conversation history (L3) hits its truncation limit sooner"),
    ("No persistent memory recall (L4)", "A bug in the tool-calling schema validation (unrelated)"),
    ("No output reservation (L5)", "Mid-sentence truncated responses reaching the customer"),
]

# Exercise 2: line dependency reasoning.
# Pair 1: True -- unmanaged L2 growth eats shared budget faster, forcing L3
#   truncation sooner than it would otherwise need to happen.
# Pair 2: False -- missing L4 recall and an unrelated schema-validation bug
#   are independent failures.
# Pair 3: True -- no L5 reservation directly causes truncated mid-response
#   output once the real (tighter) budget is exceeded.
exercise_2_answers = [True, False, True]

EXERCISE_3_FIXES = {
    "add_summarization": "Periodically summarize older turns into a compact running summary, replacing the raw text once a turn ages out of a recent window.",
    "add_kb_reranking": "Re-rank and drop knowledge-base hits that are no longer topically relevant to the current sub-topic.",
    "pin_critical_facts": "Detect certain fact types (equipment model, account tier) and re-fetch them from the account system every turn regardless of transcript state.",
    "trim_system_prompt": "Audit the system prompt and remove rarely-used boilerplate paragraphs.",
}

# Exercise 3: only summarization addresses Conversation History (L3)
# specifically; KB re-ranking is L2, pinning critical facts via re-fetch is
# L4, and trimming the system prompt is L1.
exercise_3_answers = {
    "add_summarization": True,
    "add_kb_reranking": False,
    "pin_critical_facts": False,
    "trim_system_prompt": False,
}

CONTEXT_WINDOW_TOKENS = 8_000
SYSTEM_INSTRUCTIONS_TOKENS = 500
OUTPUT_RESERVATION_TOKENS = 1_200
GROUNDING_CONTEXT_BUDGET_TOKENS = 1_800
TOKENS_PER_TURN = 150

# Exercise 4: context budget arithmetic.
#   history budget = 8000 - 500 - 1200 - 1800 = 4500
#   max full turns = 4500 // 150 = 30
exercise_4_history_budget_tokens = (
    CONTEXT_WINDOW_TOKENS
    - SYSTEM_INSTRUCTIONS_TOKENS
    - OUTPUT_RESERVATION_TOKENS
    - GROUNDING_CONTEXT_BUDGET_TOKENS
)
exercise_4_max_turns = exercise_4_history_budget_tokens // TOKENS_PER_TURN

# Exercise 5: summarize-and-keep-recent is the right eviction policy -- it
# preserves information (compressed) instead of Brackwater's blind
# drop-the-oldest truncation, which guarantees the earliest, potentially
# most load-bearing turns are always the first casualty.
exercise_5_answer = "b"

# Exercise 6: placing the critical fact at the beginning AND again near the
# end/close to the query directly counters the lost-in-the-middle position
# effect -- the two positions research finds most reliable.
exercise_6_answer = "c"

# Exercise 7: a concrete monitor needs both a metric and a threshold --
# "conversation-history token count as a percentage of total budget,
# alerting when it crosses 70%" names both.
exercise_7_monitor = (
    "Track conversation-history token count as a percentage of the total "
    "context budget on every turn, and alert when it exceeds 70% -- this "
    "would have flagged GuardLine's growing risk many turns before the "
    "hard truncation that dropped the equipment-model fact."
)

# Exercise 8: all five lines were considered across Exercises 1-7 above.
exercise_8_considered = {"L1", "L2", "L3", "L4", "L5"}


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
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
    print("Chapter 1 Exercises -- Score Report (REFERENCE SOLUTION)")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    print(f"History budget: {exercise_4_history_budget_tokens} tokens | Max turns: {exercise_4_max_turns}")


if __name__ == "__main__":
    main()
