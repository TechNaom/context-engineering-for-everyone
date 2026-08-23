"""
Chapter 3 Exercises: Short-Term Conversational Memory -- REFERENCE SOLUTION

Scenario: Quarrowstead Legal Aid Partners, a fictional legal aid
organization. Its internal caseworker assistant, DocketLine, holds
long-running conversations with caseworkers about an active case.
Chapter 2's recipe already ran for this request type: on a
20,000-token context window, Line 3 (Conversation History) was
correctly allocated 6,000 tokens. This chapter's job starts exactly
there -- the budget number is a given, not something to re-derive.
Your job is the eviction/compression POLICY that keeps real
conversation history inside that 6,000-token line without silently
dropping something load-bearing.

This file fills in every TODO with a correct reference answer and
scores a perfect total when run:

    python3 solution.py
"""

LINE3_BUDGET = 6_000

# A real, growing DocketLine case conversation -- token count per turn,
# in order. Turn 2 is where the client discloses a safety concern (see
# Exercise 5/8) -- early in the conversation, exactly the position a
# naive recency-based eviction policy is most likely to drop.
TURN_TOKENS = [420, 380, 510, 340, 460, 500, 610, 590, 480, 530, 600, 580, 450]

POLICIES = {"naive_fifo", "hybrid_pin_summary", "no_policy_needed"}

# ===========================================================================
# Exercise 1 -- match each scenario to the right short-term memory policy.
# ===========================================================================
EXERCISE_1_SCENARIOS = {
    "single_status_lookup": (
        "A caseworker asks DocketLine for one case's current filing status. "
        "One or two turns total, nowhere close to the 6,000-token Line 3 "
        "budget in any realistic conversation."
    ),
    "long_running_case_review": (
        "A caseworker works an active case over many turns across a single "
        "session -- deadlines, safety disclosures, and income changes come "
        "up early and must still matter dozens of turns later, well past "
        "the point where the raw transcript would exceed 6,000 tokens."
    ),
    "fresh_session_no_carryover": (
        "A caseworker starts a brand-new session on a brand-new case; "
        "DocketLine is explicitly configured to discard history at the end "
        "of every session, so conversation history never accumulates "
        "across sessions by design."
    ),
}

# Exercise 1: match each scenario to a policy name.
exercise_1_answers = {
    "single_status_lookup": "no_policy_needed",
    "long_running_case_review": "hybrid_pin_summary",
    "fresh_session_no_carryover": "no_policy_needed",
}

# ===========================================================================
# Exercise 2 -- order the Short-Term Memory Policy Recipe's steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_start_from_budget": "Start from Line 3's already-allocated token budget (Chapter 2's output) -- do not re-derive the number.",
    "step_set_verbatim_window": "Decide the verbatim window: how many of the most recent turns stay raw, uncompressed.",
    "step_set_trigger": "Decide what triggers compression -- a token threshold reached, not necessarily the hard budget itself.",
    "step_compress_not_truncate": "Compress anything falling out of the verbatim window into a running summary instead of blindly discarding it.",
    "step_pin_facts": "Pin load-bearing facts explicitly so they survive compression regardless of how early they occurred.",
    "step_validate_worst_case": "Validate by replaying the worst-case long conversation and confirming pinned facts + summary + verbatim turns fit inside the Line 3 budget.",
}

# Exercise 2: the recipe's correct order.
exercise_2_order = [
    "step_start_from_budget",
    "step_set_verbatim_window",
    "step_set_trigger",
    "step_compress_not_truncate",
    "step_pin_facts",
    "step_validate_worst_case",
]

# ===========================================================================
# Exercise 3 (production-gear) -- running token totals; first turn where
# the raw, uncompressed transcript would exceed the 6,000-token budget.
# ===========================================================================


def _cumulative(turn_tokens):
    running = []
    total = 0
    for t in turn_tokens:
        total += t
        running.append(total)
    return running


_cumulative_totals = _cumulative(TURN_TOKENS)

# Exercise 3: first 1-indexed turn number whose cumulative total exceeds
# LINE3_BUDGET, and the cumulative total at that turn.
exercise_3_first_turn_over_budget = next(
    i + 1 for i, total in enumerate(_cumulative_totals) if total > LINE3_BUDGET
)
exercise_3_cumulative_at_that_turn = _cumulative_totals[exercise_3_first_turn_over_budget - 1]

# ===========================================================================
# Exercise 4 (production-gear) -- verbatim window sizing.
# ===========================================================================
PINNED_FACTS_RESERVE = 500
SUMMARY_RESERVE = 1500
AVG_TOKENS_PER_TURN = 500

# Exercise 4: tokens left for verbatim turns, and how many recent turns
# that buys at the average per-turn size.
exercise_4_verbatim_budget = LINE3_BUDGET - PINNED_FACTS_RESERVE - SUMMARY_RESERVE
exercise_4_max_verbatim_turns = exercise_4_verbatim_budget // AVG_TOKENS_PER_TURN

# ===========================================================================
# Exercise 5 (production-gear) -- pin/no-pin classification.
# ===========================================================================
EXERCISE_5_FACTS = {
    "client_has_pending_eviction_deadline_in_9_days": True,
    "client_prefers_email_over_phone": False,
    "client_disclosed_domestic_violence_safety_concern": True,
    "client_mentioned_liking_the_caseworkers_coffee_order": False,
    "client_income_changed_affecting_case_eligibility": True,
    "weather_was_bad_during_the_intake_call": False,
}

# Exercise 5: pin (True) if a fact is safety-critical, deadline-critical,
# or would change the case's outcome/eligibility if it were forgotten;
# do not pin small talk or facts already recorded elsewhere in the case
# file with no bearing on the model's next answer.
exercise_5_answers = dict(EXERCISE_5_FACTS)

# ===========================================================================
# Exercise 6 (production-gear) -- compression trigger check.
# ===========================================================================
TRIGGER_THRESHOLD = 4_500  # deliberately earlier than the 6,000 hard budget

# Exercise 6: first turn whose cumulative total reaches or exceeds the
# trigger threshold (compression should start here, before the hard
# budget is actually hit).
exercise_6_trigger_turn = next(
    i + 1 for i, total in enumerate(_cumulative_totals) if total >= TRIGGER_THRESHOLD
)

# ===========================================================================
# Exercise 7 (production-gear) -- build the final short-term memory
# package and verify it fits inside the Line 3 budget.
# ===========================================================================
PACKAGE_PINNED_FACTS_TOKENS = 480
PACKAGE_SUMMARY_TOKENS = 1_400
PACKAGE_VERBATIM_TOKENS = 3_800

exercise_7_total_tokens = (
    PACKAGE_PINNED_FACTS_TOKENS + PACKAGE_SUMMARY_TOKENS + PACKAGE_VERBATIM_TOKENS
)
exercise_7_fits_budget = exercise_7_total_tokens <= LINE3_BUDGET
exercise_7_slack_tokens = LINE3_BUDGET - exercise_7_total_tokens

# ===========================================================================
# Exercise 8 (production-gear) -- naive-FIFO-vs-hybrid regression gate.
# ===========================================================================
PINNED_FACT_TURN = 2  # the safety disclosure happened at turn 2
NAIVE_VERBATIM_WINDOW_TURNS = 8  # how many of the most recent turns fit under naive FIFO

# Exercise 8: does plain recency-based (FIFO) eviction, keeping only the
# most recent NAIVE_VERBATIM_WINDOW_TURNS turns, still contain the turn
# where the pinned fact was disclosed? Does the hybrid policy (which
# pins the fact explicitly, independent of position) retain it?
_total_turns = len(TURN_TOKENS)
_oldest_kept_turn_under_naive = _total_turns - NAIVE_VERBATIM_WINDOW_TURNS + 1
exercise_8_naive_retains_pinned_fact = PINNED_FACT_TURN >= _oldest_kept_turn_under_naive
exercise_8_hybrid_retains_pinned_fact = True  # pinning is defined to be position-independent


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "single_status_lookup": "no_policy_needed",
        "long_running_case_review": "hybrid_pin_summary",
        "fresh_session_no_carryover": "no_policy_needed",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_start_from_budget",
        "step_set_verbatim_window",
        "step_set_trigger",
        "step_compress_not_truncate",
        "step_pin_facts",
        "step_validate_worst_case",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    totals = _cumulative(TURN_TOKENS)
    expected_turn = next(i + 1 for i, total in enumerate(totals) if total > LINE3_BUDGET)
    expected_cum = totals[expected_turn - 1]
    correct = 0
    correct += int(exercise_3_first_turn_over_budget == expected_turn)
    correct += int(exercise_3_cumulative_at_that_turn == expected_cum)
    return correct, 2


def score_exercise_4():
    expected_budget = LINE3_BUDGET - PINNED_FACTS_RESERVE - SUMMARY_RESERVE
    expected_turns = expected_budget // AVG_TOKENS_PER_TURN
    correct = 0
    correct += int(exercise_4_verbatim_budget == expected_budget)
    correct += int(exercise_4_max_verbatim_turns == expected_turns)
    return correct, 2


def score_exercise_5():
    correct = sum(
        1 for k, v in EXERCISE_5_FACTS.items() if exercise_5_answers.get(k) == v
    )
    return correct, len(EXERCISE_5_FACTS)


def score_exercise_6():
    totals = _cumulative(TURN_TOKENS)
    expected = next(i + 1 for i, total in enumerate(totals) if total >= TRIGGER_THRESHOLD)
    correct = 1 if exercise_6_trigger_turn == expected else 0
    return correct, 1


def score_exercise_7():
    expected_total = PACKAGE_PINNED_FACTS_TOKENS + PACKAGE_SUMMARY_TOKENS + PACKAGE_VERBATIM_TOKENS
    expected_fits = expected_total <= LINE3_BUDGET
    expected_slack = LINE3_BUDGET - expected_total
    correct = 0
    correct += int(exercise_7_total_tokens == expected_total)
    correct += int(exercise_7_fits_budget == expected_fits)
    correct += int(exercise_7_slack_tokens == expected_slack)
    return correct, 3


def score_exercise_8():
    oldest_kept = _total_turns - NAIVE_VERBATIM_WINDOW_TURNS + 1
    expected_naive = PINNED_FACT_TURN >= oldest_kept
    correct = 0
    correct += int(exercise_8_naive_retains_pinned_fact == expected_naive)
    correct += int(exercise_8_hybrid_retains_pinned_fact is True)
    # The whole point of this gate: hybrid must retain what naive drops.
    correct += int(
        exercise_8_hybrid_retains_pinned_fact is True
        and exercise_8_naive_retains_pinned_fact is False
    )
    return correct, 3


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to short-term memory policies", score_exercise_1),
        ("Exercise 2 -- order the Short-Term Memory Policy Recipe", score_exercise_2),
        ("Exercise 3 -- running totals, first turn over budget", score_exercise_3),
        ("Exercise 4 -- verbatim window sizing", score_exercise_4),
        ("Exercise 5 -- pin/no-pin classification", score_exercise_5),
        ("Exercise 6 -- compression trigger check", score_exercise_6),
        ("Exercise 7 -- build and validate the final memory package", score_exercise_7),
        ("Exercise 8 -- naive-vs-hybrid regression gate", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 3 Exercises -- Score Report (REFERENCE SOLUTION)")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    print(
        f"First turn over 6,000-token budget: turn {exercise_3_first_turn_over_budget} "
        f"(cumulative {exercise_3_cumulative_at_that_turn})"
    )
    print(
        f"Naive FIFO retains the turn-2 safety disclosure: {exercise_8_naive_retains_pinned_fact} "
        f"| Hybrid retains it: {exercise_8_hybrid_retains_pinned_fact}"
    )


if __name__ == "__main__":
    main()
