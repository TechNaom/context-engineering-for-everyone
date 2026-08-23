"""
Chapter 4 Exercises: Long-Term and Persistent Memory Systems -- REFERENCE SOLUTION

Scenario: Caldermere Home Health Alliance, a fictional home health
agency. Its aide-support assistant, CareLine, works with the same
recurring clients across many separate visits (separate sessions,
sometimes weeks apart) over the life of a care plan. Chapter 2's
recipe already ran for this request type: Line 4 (Recalled Long-Term
Memory) was correctly allocated 1,800 tokens. That number is a given
here, not something to re-derive -- your job is the real write and
retrieval POLICY that decides what gets persisted across visits, what
gets pulled back into Line 4 for a given visit, and what gets excluded
because it's gone stale.

This file fills in every TODO with a correct reference answer and
scores a perfect total when run:

    python3 solution.py
"""

LINE4_BUDGET = 1_800

# Raw fact-store growth across 10 real CareLine visits for one client's
# care plan -- token count of everything disclosed per visit, in order.
# Nothing here is curated yet; this is what an uncurated "write and keep
# everything" store would grow to.
VISIT_TOKENS = [150, 140, 130, 160, 150, 140, 170, 160, 150, 140, 180, 160]

APPROACHES = {"no_persistent_memory_needed", "curated_store_with_staleness_handling", "naive_append_only_log"}

# ===========================================================================
# Exercise 1 -- match each scenario to the right long-term memory approach.
# ===========================================================================
EXERCISE_1_SCENARIOS = {
    "single_visit_no_recurrence": (
        "A client receives exactly one CareLine-supported visit and never "
        "returns -- there is no second session for anything to be recalled "
        "into."
    ),
    "recurring_multi_month_care_plan": (
        "A client has a care plan that runs for months, across dozens of "
        "separate visit sessions. Facts genuinely change over that time -- "
        "medication dosages update, care plans change, old facts become "
        "stale -- and some early facts (a fall risk, a safety concern) must "
        "still be recallable at visit 40, not just visit 2."
    ),
    "log_everything_ever_said_no_curation": (
        "A team appends every fact ever disclosed, in any visit, to one "
        "growing store, and retrieves the entire store into context on "
        "every subsequent visit with no filtering for relevance or "
        "staleness."
    ),
}

# Exercise 1: assign an approach name from APPROACHES to each scenario.
exercise_1_answers = {
    "single_visit_no_recurrence": "no_persistent_memory_needed",
    "recurring_multi_month_care_plan": "curated_store_with_staleness_handling",
    "log_everything_ever_said_no_curation": "naive_append_only_log",
}

# ===========================================================================
# Exercise 2 -- order the Long-Term Memory Policy Recipe's steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_write_criteria": "Decide the write criteria: a bounded, explicit set of fact categories eligible to be persisted at all -- not everything disclosed.",
    "step_storage_shape": "Decide the storage shape: a structured record (subject, category, value, timestamp, status), not a raw transcript dump.",
    "step_retrieval_scope": "Decide the retrieval policy: what scopes a stored memory back into Line 4 for a GIVEN turn -- subject + request-type-relevant categories, never 'load everything.'",
    "step_staleness_handling": "Decide staleness handling: mark superseded/expired records inactive on update, and never retrieve a non-active record into Line 4.",
    "step_bound_line4": "Bound Line 4's own token budget: cap how many facts, and how many tokens, a single turn's retrieval is allowed to pull in.",
    "step_validate_worst_case": "Validate against the longest realistic relationship: the most updates and the most conflicting facts, confirming retrieval never reintroduces stale data and still fits Line 4's budget.",
}

# Exercise 2: the recipe's correct order.
exercise_2_order = [
    "step_write_criteria",
    "step_storage_shape",
    "step_retrieval_scope",
    "step_staleness_handling",
    "step_bound_line4",
    "step_validate_worst_case",
]

# ===========================================================================
# Exercise 3 (production-gear) -- running totals of an UNCURATED store;
# first visit where the raw, uncurated fact total would exceed the
# 1,800-token Line 4 budget (the reason curation is necessary at all).
# ===========================================================================


def _cumulative(tokens):
    running = []
    total = 0
    for t in tokens:
        total += t
        running.append(total)
    return running


_cumulative_totals = _cumulative(VISIT_TOKENS)

# Exercise 3: first 1-indexed visit number whose cumulative raw total
# exceeds LINE4_BUDGET, and the cumulative total at that visit.
exercise_3_first_visit_over_budget = next(
    i + 1 for i, total in enumerate(_cumulative_totals) if total > LINE4_BUDGET
)
exercise_3_cumulative_at_that_visit = _cumulative_totals[exercise_3_first_visit_over_budget - 1]

# ===========================================================================
# Exercise 4 (production-gear) -- retrieval budget sizing.
# ===========================================================================
CORE_RESERVE_TOKENS = 300  # always-retrieved core safety/care-plan facts
AVG_TOKENS_PER_RETRIEVED_FACT = 60

# Exercise 4: tokens left in Line 4's budget after the core reserve, and
# how many additional facts that buys at the average fact size.
exercise_4_remaining_budget = LINE4_BUDGET - CORE_RESERVE_TOKENS
exercise_4_max_additional_facts = exercise_4_remaining_budget // AVG_TOKENS_PER_RETRIEVED_FACT

# ===========================================================================
# Exercise 5 (production-gear) -- write/no-write classification.
# ===========================================================================
EXERCISE_5_FACTS = {
    "client_has_documented_fall_risk": True,
    "client_prefers_morning_visits": False,
    "client_medication_dosage_changed": True,
    "client_liked_aides_choice_of_music": False,
    "client_care_plan_changed_after_hospitalization": True,
    "weather_was_bad_during_the_visit": False,
}

# Exercise 5: write (True) to the persistent store if a fact is
# safety-critical or a real care-plan/clinical change that must still
# matter at a future visit; do not write small talk or facts with no
# bearing on any future visit's decisions.
exercise_5_answers = dict(EXERCISE_5_FACTS)

# ===========================================================================
# Exercise 6 (production-gear) -- staleness resolution: for each subject,
# two stored facts exist with different timestamps. Which one should
# remain ACTIVE (the more recent one), and which becomes SUPERSEDED?
# ===========================================================================
EXERCISE_6_FACT_PAIRS = {
    "medication_dosage": {
        "old": {"id": "lt_dosage_2025_01", "timestamp": "2025-01-10"},
        "new": {"id": "lt_dosage_2025_06", "timestamp": "2025-06-02"},
    },
    "mobility_status": {
        "old": {"id": "lt_mobility_2024_11", "timestamp": "2024-11-20"},
        "new": {"id": "lt_mobility_2025_03", "timestamp": "2025-03-15"},
    },
    "emergency_contact": {
        "old": {"id": "lt_contact_2023_08", "timestamp": "2023-08-01"},
        "new": {"id": "lt_contact_2025_02", "timestamp": "2025-02-14"},
    },
}

# Exercise 6: for each subject, the fact ID that should remain ACTIVE
# (always the more recent timestamp -- the newer record supersedes the
# older one, the older one is marked superseded, never retrieved again).
exercise_6_active_fact_ids = {
    "medication_dosage": "lt_dosage_2025_06",
    "mobility_status": "lt_mobility_2025_03",
    "emergency_contact": "lt_contact_2025_02",
}

# ===========================================================================
# Exercise 7 (production-gear) -- build the retrieved Line 4 package for
# one visit and verify it fits inside the budget.
# ===========================================================================
PACKAGE_CORE_FACTS_TOKENS = 300
PACKAGE_SCOPED_FACTS_TOKENS = 420

exercise_7_total_tokens = PACKAGE_CORE_FACTS_TOKENS + PACKAGE_SCOPED_FACTS_TOKENS
exercise_7_fits_budget = exercise_7_total_tokens <= LINE4_BUDGET
exercise_7_slack_tokens = LINE4_BUDGET - exercise_7_total_tokens

# ===========================================================================
# Exercise 8 (production-gear) -- naive-append-vs-curated regression gate.
# A superseded medication-dosage fact and its active replacement both
# exist in the store. Does naive "retrieve everything ever stored"
# incorrectly retrieve the superseded (outdated, contradictory) fact
# alongside its replacement? Does the curated policy correctly exclude it?
# ===========================================================================
SUPERSEDED_FACT_STATUS = "superseded"
CURRENT_FACT_STATUS = "active"

exercise_8_naive_retrieves_superseded = True  # naive policy retrieves EVERY stored fact, by definition
exercise_8_curated_retrieves_superseded = False  # curated policy filters status != "active"
exercise_8_curated_retrieves_current = True  # the active replacement is still retrieved


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "single_visit_no_recurrence": "no_persistent_memory_needed",
        "recurring_multi_month_care_plan": "curated_store_with_staleness_handling",
        "log_everything_ever_said_no_curation": "naive_append_only_log",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_write_criteria",
        "step_storage_shape",
        "step_retrieval_scope",
        "step_staleness_handling",
        "step_bound_line4",
        "step_validate_worst_case",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    totals = _cumulative(VISIT_TOKENS)
    expected_visit = next(i + 1 for i, total in enumerate(totals) if total > LINE4_BUDGET)
    expected_cum = totals[expected_visit - 1]
    correct = 0
    correct += int(exercise_3_first_visit_over_budget == expected_visit)
    correct += int(exercise_3_cumulative_at_that_visit == expected_cum)
    return correct, 2


def score_exercise_4():
    expected_remaining = LINE4_BUDGET - CORE_RESERVE_TOKENS
    expected_facts = expected_remaining // AVG_TOKENS_PER_RETRIEVED_FACT
    correct = 0
    correct += int(exercise_4_remaining_budget == expected_remaining)
    correct += int(exercise_4_max_additional_facts == expected_facts)
    return correct, 2


def score_exercise_5():
    correct = sum(
        1 for k, v in EXERCISE_5_FACTS.items() if exercise_5_answers.get(k) == v
    )
    return correct, len(EXERCISE_5_FACTS)


def score_exercise_6():
    correct = sum(
        1 for k, v in EXERCISE_6_FACT_PAIRS.items()
        if exercise_6_active_fact_ids.get(k) == v["new"]["id"]
    )
    return correct, len(EXERCISE_6_FACT_PAIRS)


def score_exercise_7():
    expected_total = PACKAGE_CORE_FACTS_TOKENS + PACKAGE_SCOPED_FACTS_TOKENS
    expected_fits = expected_total <= LINE4_BUDGET
    expected_slack = LINE4_BUDGET - expected_total
    correct = 0
    correct += int(exercise_7_total_tokens == expected_total)
    correct += int(exercise_7_fits_budget == expected_fits)
    correct += int(exercise_7_slack_tokens == expected_slack)
    return correct, 3


def score_exercise_8():
    correct = 0
    correct += int(exercise_8_naive_retrieves_superseded is True)
    correct += int(exercise_8_curated_retrieves_superseded is False)
    correct += int(exercise_8_curated_retrieves_current is True)
    return correct, 3


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to long-term memory approaches", score_exercise_1),
        ("Exercise 2 -- order the Long-Term Memory Policy Recipe", score_exercise_2),
        ("Exercise 3 -- uncurated growth, first visit over budget", score_exercise_3),
        ("Exercise 4 -- retrieval budget sizing", score_exercise_4),
        ("Exercise 5 -- write/no-write classification", score_exercise_5),
        ("Exercise 6 -- staleness resolution", score_exercise_6),
        ("Exercise 7 -- build and validate the retrieved Line 4 package", score_exercise_7),
        ("Exercise 8 -- naive-append-vs-curated regression gate", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 4 Exercises -- Score Report (REFERENCE SOLUTION)")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    print(
        f"First visit an uncurated store exceeds the {LINE4_BUDGET}-token Line 4 budget: "
        f"visit {exercise_3_first_visit_over_budget} (cumulative {exercise_3_cumulative_at_that_visit})"
    )
    print(
        f"Naive append-only retrieves the superseded dosage fact: {exercise_8_naive_retrieves_superseded} "
        f"| Curated retrieves it: {exercise_8_curated_retrieves_superseded}"
    )


if __name__ == "__main__":
    main()
