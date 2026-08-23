"""
Chapter 4 Exercises: Long-Term and Persistent Memory Systems

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

Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report. Compare against solution.py, which scores a
perfect total.
"""

LINE4_BUDGET = 1_800

# Raw fact-store growth across 12 real CareLine visits for one client's
# care plan -- token count of everything disclosed per visit, in order.
# Nothing here is curated yet; this is what an uncurated "write and keep
# everything" store would grow to.
VISIT_TOKENS = [150, 140, 130, 160, 150, 140, 170, 160, 150, 140, 180, 160]

APPROACHES = {"no_persistent_memory_needed", "curated_store_with_staleness_handling", "naive_append_only_log"}

# ===========================================================================
# Exercise 1 -- match each scenario to the right long-term memory approach.
# Choose from APPROACHES for each key below.
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

# TODO: assign an approach name from APPROACHES to each scenario.
exercise_1_answers = {
    "single_visit_no_recurrence": None,  # TODO
    "recurring_multi_month_care_plan": None,  # TODO
    "log_everything_ever_said_no_curation": None,  # TODO
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

# TODO: put the six step keys above in the correct order.
exercise_2_order = [
    # TODO
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

# TODO: first 1-indexed visit number whose cumulative raw total exceeds
# LINE4_BUDGET, and the cumulative total at that visit.
exercise_3_first_visit_over_budget = None  # TODO: int
exercise_3_cumulative_at_that_visit = None  # TODO: int

# ===========================================================================
# Exercise 4 (production-gear) -- retrieval budget sizing.
# ===========================================================================
CORE_RESERVE_TOKENS = 300  # always-retrieved core safety/care-plan facts
AVG_TOKENS_PER_RETRIEVED_FACT = 60

# TODO: tokens left in Line 4's budget after the core reserve, and how
# many additional facts that buys at the average fact size (integer
# division).
exercise_4_remaining_budget = None  # TODO: int
exercise_4_max_additional_facts = None  # TODO: int

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

# TODO: for each fact key below, decide True (write to the persistent
# store) or False (don't). Write a fact if it's safety-critical or a real
# care-plan/clinical change that must still matter at a future visit. Do
# not write small talk or facts with no bearing on any future visit.
exercise_5_answers = {
    "client_has_documented_fall_risk": None,  # TODO
    "client_prefers_morning_visits": None,  # TODO
    "client_medication_dosage_changed": None,  # TODO
    "client_liked_aides_choice_of_music": None,  # TODO
    "client_care_plan_changed_after_hospitalization": None,  # TODO
    "weather_was_bad_during_the_visit": None,  # TODO
}

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

# TODO: for each subject, the fact ID (a string) that should remain
# ACTIVE -- always the more recent timestamp.
exercise_6_active_fact_ids = {
    "medication_dosage": None,  # TODO
    "mobility_status": None,  # TODO
    "emergency_contact": None,  # TODO
}

# ===========================================================================
# Exercise 7 (production-gear) -- build the retrieved Line 4 package for
# one visit and verify it fits inside the budget.
# ===========================================================================
PACKAGE_CORE_FACTS_TOKENS = 300
PACKAGE_SCOPED_FACTS_TOKENS = 420

# TODO: sum the two package components; whether the total fits inside
# LINE4_BUDGET; and how much slack (budget minus total) remains.
exercise_7_total_tokens = None  # TODO: int
exercise_7_fits_budget = None  # TODO: bool
exercise_7_slack_tokens = None  # TODO: int

# ===========================================================================
# Exercise 8 (production-gear) -- naive-append-vs-curated regression gate.
# A superseded medication-dosage fact and its active replacement both
# exist in the store. Does naive "retrieve everything ever stored"
# incorrectly retrieve the superseded (outdated, contradictory) fact
# alongside its replacement? Does the curated policy correctly exclude it?
# ===========================================================================
SUPERSEDED_FACT_STATUS = "superseded"
CURRENT_FACT_STATUS = "active"

# TODO: does the naive "retrieve everything ever stored" policy retrieve
# a superseded fact? Does the curated policy (filters on status=="active")
# retrieve a superseded fact? Does the curated policy still retrieve the
# current, active replacement?
exercise_8_naive_retrieves_superseded = None  # TODO: bool
exercise_8_curated_retrieves_superseded = None  # TODO: bool
exercise_8_curated_retrieves_current = None  # TODO: bool


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
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
    print("Chapter 4 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every task correctly completed.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
