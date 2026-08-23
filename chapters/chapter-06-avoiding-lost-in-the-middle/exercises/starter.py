"""
Chapter 6 Exercises: Avoiding Lost-in-the-Middle

Scenario: Calverton Public Defender's Office, a fictional public
defender's office. Its case-file review assistant, DocketLine, handles
"Case File Review" conversations before a hearing -- a real case file
can run long, accumulating a defendant's background, prior filings, a
transcript of plea negotiations, and evidence logs, before the specific
question the attorney actually needs answered ever gets asked. Chapters
1-5's own recipes have already run for this request type: a correct
budget, a correct pin/summary/window shape, a correct long-term recall
policy, and a fidelity-checked compression pipeline. Every fact in the
window is present, unmodified, and within budget -- your job is this
chapter's own new skill: deciding WHERE each already-included fact goes
so the model actually uses it.

Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report. Compare against solution.py, which scores a
perfect total.
"""

# ===========================================================================
# Exercise 1 -- match each scenario to the right ordering approach.
# Choose from APPROACHES for each key below.
# ===========================================================================
APPROACHES = {"arrival_order", "naive_top_load", "weight_ranked_both_anchors"}

EXERCISE_1_SCENARIOS = {
    "content_concatenated_in_whatever_order_it_became_available": (
        "Pinned facts, recalled facts, summary, verbatim window, and "
        "query are concatenated in whatever order they became "
        "available, with no positional review."
    ),
    "everything_important_front_loaded_query_buried_far_from_generation": (
        "Every important fact is moved to the top of the window, but "
        "the query still ends up far from where generation begins, "
        "separated by a long undifferentiated block."
    ),
    "highest_weight_content_and_query_reserved_for_anchors_middle_deliberately_reordered_and_tested": (
        "Content is ranked by load-bearing weight, the highest-weight "
        "facts and the query each get a reserved anchor position, the "
        "middle is deliberately reordered rather than left to arrival "
        "order, and the result is validated with a positional probe."
    ),
}

# TODO: assign an approach name from APPROACHES to each scenario.
exercise_1_answers = {
    "content_concatenated_in_whatever_order_it_became_available": None,  # TODO
    "everything_important_front_loaded_query_buried_far_from_generation": None,  # TODO
    "highest_weight_content_and_query_reserved_for_anchors_middle_deliberately_reordered_and_tested": None,  # TODO
}

# ===========================================================================
# Exercise 2 -- order the Context Ordering Recipe's five steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_rank_by_weight": "Rank what's already inside by load-bearing weight -- not everything correctly included is equally load-bearing.",
    "step_reserve_anchors": "Reserve the anchor positions (start and end) for the highest-weight content -- both research sources agree these are the most reliable positions.",
    "step_reorder_middle": "Reorder the middle deliberately -- don't trust retrieval order, write-timestamp order, or conversation order as a relevance proxy.",
    "step_query_near_end": "Put the query and instructions near the end, after reference material, closest to where generation begins.",
    "step_test_position": "Test position directly with an explicit positional probe; never assume order-invariance, and re-test after any model or context-length change.",
}

# TODO: put the five step keys above in the correct order.
exercise_2_order = [
    # TODO
]

# ===========================================================================
# Exercise 3 (production-gear) -- position-percentile arithmetic.
# ===========================================================================
TOTAL_WINDOW_TOKENS = 3_200
FACT_START_TOKEN = 1_350
FACT_LENGTH_TOKENS = 50
HIGH_RISK_MIDDLE_BAND = (20, 80)  # inclusive percentile range, per the re-verified research

# TODO: the fact's midpoint token offset expressed as an integer percentile
# of TOTAL_WINDOW_TOKENS (using integer division: midpoint * 100 // total),
# and whether that percentile falls inside HIGH_RISK_MIDDLE_BAND (inclusive).
exercise_3_midpoint_percentile = None  # TODO: int
exercise_3_in_high_risk_middle_band = None  # TODO: bool

# ===========================================================================
# Exercise 4 (production-gear) -- load-bearing weight classification.
# ===========================================================================
EXERCISE_4_DETAILS = {
    "exculpatory_alibi_witness_statement": True,
    "courthouse_parking_validation_info": False,
    "prior_conviction_wrongly_attributed_to_client": True,
    "clerk_office_hours_note": False,
    "chain_of_custody_gap_in_evidence_log": True,
    "defendant_mentioned_liking_coffee": False,
}

# TODO: for each detail key below, decide True (high load-bearing weight --
# must be placed at an anchor) or False (low weight -- can sit in the middle).
exercise_4_answers = {
    "exculpatory_alibi_witness_statement": None,  # TODO
    "courthouse_parking_validation_info": None,  # TODO
    "prior_conviction_wrongly_attributed_to_client": None,  # TODO
    "clerk_office_hours_note": None,  # TODO
    "chain_of_custody_gap_in_evidence_log": None,  # TODO
    "defendant_mentioned_liking_coffee": None,  # TODO
}

# ===========================================================================
# Exercise 5 (production-gear) -- positional probe: anchor-required facts.
# ===========================================================================
ANCHOR_REQUIRED_FACTS = {
    "exculpatory_alibi_witness_statement",
    "chain_of_custody_gap_in_evidence_log",
    "prior_conviction_wrongly_attributed_to_client",
}
ACTUAL_ANCHOR_PLACEMENTS = {
    "exculpatory_alibi_witness_statement",
    "chain_of_custody_gap_in_evidence_log",
}

# TODO: which anchor-required facts (a set) are missing from
# ACTUAL_ANCHOR_PLACEMENTS, and whether the placement passes its own
# positional-probe gate (a bool, True only if none are missing).
exercise_5_missing_from_anchors = None  # TODO: set
exercise_5_placement_passes = None  # TODO: bool

# ===========================================================================
# Exercise 6 (production-gear) -- query/instruction anchor classification.
# True = belongs at the end anchor nearest generation (the active
# query/instruction); False = reference/history material that belongs
# elsewhere in the window.
# ===========================================================================
EXERCISE_6_CONTENT = {
    "the_current_hearing_question_the_model_must_answer_now": True,
    "a_120_turn_transcript_of_prior_plea_negotiations": False,
    "the_specific_instruction_asking_for_a_recommendation_today": True,
    "a_reference_copy_of_the_original_police_report": False,
    "the_final_ask_summarize_contraindications_for_todays_filing": True,
    "background_biography_of_the_defendant": False,
}

# TODO: for each content type below, decide True (belongs at the end anchor
# nearest generation) or False (belongs elsewhere in the window).
exercise_6_answers = {
    "the_current_hearing_question_the_model_must_answer_now": None,  # TODO
    "a_120_turn_transcript_of_prior_plea_negotiations": None,  # TODO
    "the_specific_instruction_asking_for_a_recommendation_today": None,  # TODO
    "a_reference_copy_of_the_original_police_report": None,  # TODO
    "the_final_ask_summarize_contraindications_for_todays_filing": None,  # TODO
    "background_biography_of_the_defendant": None,  # TODO
}

# ===========================================================================
# Exercise 7 (production-gear) -- arrival-order-vs-weight-ranked regression
# gate. A load-bearing detail (the chain-of-custody gap) exists in the raw
# case file. Does arrival order bury it in the middle? Does weight-ranked
# placement surface it at an anchor? Would the weight-ranked pipeline's own
# positional probe (Step 5) flag a failure if it were still buried?
# ===========================================================================
exercise_7_arrival_order_buries_detail = None  # TODO: bool
exercise_7_weight_ranked_surfaces_detail = None  # TODO: bool
exercise_7_weight_ranked_would_flag_if_still_buried = None  # TODO: bool

# ===========================================================================
# Exercise 8 (production-gear) -- retest/escalation decision. For each
# positional-probe outcome, decide the correct next action from
# POSITION_OPTIONS.
# ===========================================================================
POSITION_OPTIONS = {"ship_as_is", "retest_or_reposition"}

EXERCISE_8_SCENARIOS = {
    "positional_probe_passes_all_high_weight_facts_at_anchors": (
        "Every high-weight fact identified in Step 1 is confirmed at an "
        "anchor position by the Step 5 probe."
    ),
    "positional_probe_fails_one_high_weight_fact_still_in_middle": (
        "One high-weight fact (a chain-of-custody gap) is still found "
        "in the middle band by the Step 5 probe."
    ),
    "model_swapped_to_a_different_family_since_last_probe": (
        "The underlying model was swapped to a different model family "
        "since the last positional probe was run, but placements were "
        "never re-tested against the new model."
    ),
}

# TODO: an action from POSITION_OPTIONS for each scenario.
exercise_8_answers = {
    "positional_probe_passes_all_high_weight_facts_at_anchors": None,  # TODO
    "positional_probe_fails_one_high_weight_fact_still_in_middle": None,  # TODO
    "model_swapped_to_a_different_family_since_last_probe": None,  # TODO
}


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score_exercise_1():
    key = {
        "content_concatenated_in_whatever_order_it_became_available": "arrival_order",
        "everything_important_front_loaded_query_buried_far_from_generation": "naive_top_load",
        "highest_weight_content_and_query_reserved_for_anchors_middle_deliberately_reordered_and_tested": "weight_ranked_both_anchors",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_rank_by_weight",
        "step_reserve_anchors",
        "step_reorder_middle",
        "step_query_near_end",
        "step_test_position",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    expected_pct = (FACT_START_TOKEN + FACT_LENGTH_TOKENS // 2) * 100 // TOTAL_WINDOW_TOKENS
    expected_band = HIGH_RISK_MIDDLE_BAND[0] <= expected_pct <= HIGH_RISK_MIDDLE_BAND[1]
    correct = 0
    correct += int(exercise_3_midpoint_percentile == expected_pct)
    correct += int(exercise_3_in_high_risk_middle_band == expected_band)
    return correct, 2


def score_exercise_4():
    correct = sum(
        1 for k, v in EXERCISE_4_DETAILS.items() if exercise_4_answers.get(k) == v
    )
    return correct, len(EXERCISE_4_DETAILS)


def score_exercise_5():
    expected_missing = ANCHOR_REQUIRED_FACTS - ACTUAL_ANCHOR_PLACEMENTS
    expected_passes = len(expected_missing) == 0
    correct = 0
    correct += int(exercise_5_missing_from_anchors == expected_missing)
    correct += int(exercise_5_placement_passes == expected_passes)
    return correct, 2


def score_exercise_6():
    correct = sum(
        1 for k, v in EXERCISE_6_CONTENT.items() if exercise_6_answers.get(k) == v
    )
    return correct, len(EXERCISE_6_CONTENT)


def score_exercise_7():
    correct = 0
    correct += int(exercise_7_arrival_order_buries_detail is True)
    correct += int(exercise_7_weight_ranked_surfaces_detail is True)
    correct += int(exercise_7_weight_ranked_would_flag_if_still_buried is True)
    return correct, 3


def score_exercise_8():
    key = {
        "positional_probe_passes_all_high_weight_facts_at_anchors": "ship_as_is",
        "positional_probe_fails_one_high_weight_fact_still_in_middle": "retest_or_reposition",
        "model_swapped_to_a_different_family_since_last_probe": "retest_or_reposition",
    }
    correct = sum(1 for k, v in key.items() if exercise_8_answers.get(k) == v)
    return correct, len(key)


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to ordering approaches", score_exercise_1),
        ("Exercise 2 -- order the Context Ordering Recipe", score_exercise_2),
        ("Exercise 3 -- position-percentile arithmetic", score_exercise_3),
        ("Exercise 4 -- load-bearing weight classification", score_exercise_4),
        ("Exercise 5 -- positional probe: anchor-required facts", score_exercise_5),
        ("Exercise 6 -- query/instruction anchor classification", score_exercise_6),
        ("Exercise 7 -- arrival-order-vs-weight-ranked regression gate", score_exercise_7),
        ("Exercise 8 -- retest/escalation decision", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 6 Exercises -- Score Report")
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
