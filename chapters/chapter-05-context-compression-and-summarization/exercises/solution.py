"""
Chapter 5 Exercises: Context Compression and Summarization -- REFERENCE SOLUTION

Scenario: Kirkholme Public Transit Safety Board, a fictional transit
safety oversight agency. Its incident-intake assistant, TransitLine,
handles "Vehicle Incident Report" conversations that can run long
before a mechanical or safety pattern emerges across many turns.
Chapter 3's recipe already fired for this request type: a compression
trigger correctly kicks in once a segment exceeds the verbatim window,
and the resulting running summary has a fixed 480-token target. That
target is a given here, not something to re-derive -- your job is the
real compression MECHANICS that decide what survives inside it.

This file fills in every TODO with a correct reference answer and
scores a perfect total when run:

    python3 solution.py
"""

COMPRESSION_TARGET_TOKENS = 480

# ===========================================================================
# Exercise 1 -- match each scenario to the right compression approach.
# ===========================================================================
APPROACHES = {"no_compression_needed", "naive_summarization", "fidelity_checked_pipeline"}

EXERCISE_1_SCENARIOS = {
    "segment_already_under_target": (
        "A TransitLine conversation segment is already under the "
        "480-token target once the trigger fires -- there is nothing "
        "left to shrink."
    ),
    "single_prompt_shrink_as_much_as_possible": (
        "A team calls one prompt -- 'summarize as concisely as "
        "possible' -- with no pre-extraction of load-bearing details "
        "and no check afterward that anything specific survived."
    ),
    "preextraction_bounded_strategy_and_validation": (
        "A team flags load-bearing candidates before compressing, "
        "picks an extractive or abstractive strategy per content type, "
        "compresses against the fixed 480-token target, and validates "
        "every flagged candidate is present before the result ships."
    ),
}

# Exercise 1: assign an approach name from APPROACHES to each scenario.
exercise_1_answers = {
    "segment_already_under_target": "no_compression_needed",
    "single_prompt_shrink_as_much_as_possible": "naive_summarization",
    "preextraction_bounded_strategy_and_validation": "fidelity_checked_pipeline",
}

# ===========================================================================
# Exercise 2 -- order the Compression Fidelity Recipe's steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_identify_exempt": "Identify what's already exempt: anything already pinned (Ch. 3) or already persisted (Ch. 4) is never subject to compression at all.",
    "step_extract_candidates": "Extract load-bearing candidates before compressing: a deterministic pre-pass that flags specific details a compression step must preserve or explicitly justify dropping.",
    "step_choose_strategy": "Choose a strategy matched to content type: extractive for structured/technical content where exact wording matters, abstractive for safe-to-paraphrase narrative content.",
    "step_bound_target": "Bound the target explicitly: a specific length or ratio, never 'as concisely as possible.'",
    "step_run_compression": "Run the compression: execute the chosen strategy against the bounded target.",
    "step_validate_fidelity": "Validate fidelity before shipping: check the output against the candidate list; fail closed (retry, widen, or escalate) if anything flagged is missing.",
}

# Exercise 2: the recipe's correct order.
exercise_2_order = [
    "step_identify_exempt",
    "step_extract_candidates",
    "step_choose_strategy",
    "step_bound_target",
    "step_run_compression",
    "step_validate_fidelity",
]

# ===========================================================================
# Exercise 3 (production-gear) -- compression ratio arithmetic.
# ===========================================================================
RAW_SEGMENT_TOKENS = 2_400

# Exercise 3: tokens that must be cut to hit COMPRESSION_TARGET_TOKENS, and
# the resulting retention percentage (integer, tokens kept / tokens raw * 100).
exercise_3_tokens_to_cut = RAW_SEGMENT_TOKENS - COMPRESSION_TARGET_TOKENS
exercise_3_retention_percentage = COMPRESSION_TARGET_TOKENS * 100 // RAW_SEGMENT_TOKENS

# ===========================================================================
# Exercise 4 (production-gear) -- load-bearing candidate classification.
# ===========================================================================
EXERCISE_4_DETAILS = {
    "bus_route_number_and_mechanical_symptom": True,
    "driver_said_good_morning_to_passenger": False,
    "exact_time_and_location_of_brake_failure_report": True,
    "passenger_thanked_the_driver": False,
    "specific_maintenance_bay_number_referenced": True,
    "weather_was_sunny_during_the_incident": False,
}

# Exercise 4: True if a detail must be flagged as a load-bearing candidate
# before compressing (a specific, technical, or safety-relevant fact a
# diagnosis could depend on); False if it's incidental small talk or
# context with no bearing on the incident's cause.
exercise_4_answers = dict(EXERCISE_4_DETAILS)

# ===========================================================================
# Exercise 5 (production-gear) -- fidelity check.
# ===========================================================================
CANDIDATE_DETAILS = {"route_38", "brake_failure_7_42am", "maintenance_bay_12"}
PRODUCED_SUMMARY_TOKENS = {"route_38", "maintenance_bay_12", "grinding_noise"}

# Exercise 5: which candidates are missing from the produced summary, and
# whether the compression passes its own fidelity-check gate (True only if
# every candidate is present).
exercise_5_missing_candidates = CANDIDATE_DETAILS - PRODUCED_SUMMARY_TOKENS
exercise_5_fidelity_check_passes = len(exercise_5_missing_candidates) == 0

# ===========================================================================
# Exercise 6 (production-gear) -- extractive vs. abstractive strategy
# selection. True = extractive is the right choice (exact wording matters);
# False = abstractive is fine (safe to paraphrase).
# ===========================================================================
EXERCISE_6_CONTENT = {
    "structured_incident_report_with_ids_and_timestamps": True,
    "casual_smalltalk_about_the_weekend": False,
    "technical_diagnostic_sequence_with_specific_readings": True,
    "general_narrative_complaint_with_no_specific_numbers": False,
    "list_of_exact_part_numbers_and_serials": True,
    "customer_expressing_frustration_with_wait_time": False,
}

exercise_6_answers = dict(EXERCISE_6_CONTENT)

# ===========================================================================
# Exercise 7 (production-gear) -- naive-vs-fidelity-checked regression gate.
# A load-bearing technical detail (a specific error code) exists in the raw
# segment. Does naive "shrink as much as possible" compression drop it? Does
# the fidelity-checked pipeline retain it? Would the fidelity-checked
# pipeline's own validation flag a failure if the detail HAD been dropped?
# ===========================================================================
exercise_7_naive_drops_detail = True  # naive compression has no candidate list to protect it
exercise_7_fidelity_checked_retains_detail = True  # flagged as a candidate, preserved via extractive strategy
exercise_7_fidelity_checked_would_flag_if_dropped = True  # Step 6 checks the candidate list either way

# ===========================================================================
# Exercise 8 (production-gear) -- escalation decision. For each fidelity
# check outcome, decide the correct next action.
# ===========================================================================
ESCALATION_OPTIONS = {"ship_as_is", "retry_or_escalate"}

EXERCISE_8_SCENARIOS = {
    "fidelity_check_passes_all_candidates_present": (
        "All flagged candidates are present in the compressed output."
    ),
    "fidelity_check_fails_one_candidate_missing": (
        "One flagged candidate (a specific error code) is missing from "
        "the compressed output."
    ),
    "target_impossible_to_hit_without_losing_a_candidate": (
        "Every extractive strategy tried still exceeds the 480-token "
        "target unless a flagged candidate is cut."
    ),
}

# Exercise 8: an action from ESCALATION_OPTIONS for each scenario.
exercise_8_answers = {
    "fidelity_check_passes_all_candidates_present": "ship_as_is",
    "fidelity_check_fails_one_candidate_missing": "retry_or_escalate",
    "target_impossible_to_hit_without_losing_a_candidate": "retry_or_escalate",
}


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "segment_already_under_target": "no_compression_needed",
        "single_prompt_shrink_as_much_as_possible": "naive_summarization",
        "preextraction_bounded_strategy_and_validation": "fidelity_checked_pipeline",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_identify_exempt",
        "step_extract_candidates",
        "step_choose_strategy",
        "step_bound_target",
        "step_run_compression",
        "step_validate_fidelity",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    expected_cut = RAW_SEGMENT_TOKENS - COMPRESSION_TARGET_TOKENS
    expected_pct = COMPRESSION_TARGET_TOKENS * 100 // RAW_SEGMENT_TOKENS
    correct = 0
    correct += int(exercise_3_tokens_to_cut == expected_cut)
    correct += int(exercise_3_retention_percentage == expected_pct)
    return correct, 2


def score_exercise_4():
    correct = sum(
        1 for k, v in EXERCISE_4_DETAILS.items() if exercise_4_answers.get(k) == v
    )
    return correct, len(EXERCISE_4_DETAILS)


def score_exercise_5():
    expected_missing = CANDIDATE_DETAILS - PRODUCED_SUMMARY_TOKENS
    expected_passes = len(expected_missing) == 0
    correct = 0
    correct += int(exercise_5_missing_candidates == expected_missing)
    correct += int(exercise_5_fidelity_check_passes == expected_passes)
    return correct, 2


def score_exercise_6():
    correct = sum(
        1 for k, v in EXERCISE_6_CONTENT.items() if exercise_6_answers.get(k) == v
    )
    return correct, len(EXERCISE_6_CONTENT)


def score_exercise_7():
    correct = 0
    correct += int(exercise_7_naive_drops_detail is True)
    correct += int(exercise_7_fidelity_checked_retains_detail is True)
    correct += int(exercise_7_fidelity_checked_would_flag_if_dropped is True)
    return correct, 3


def score_exercise_8():
    key = {
        "fidelity_check_passes_all_candidates_present": "ship_as_is",
        "fidelity_check_fails_one_candidate_missing": "retry_or_escalate",
        "target_impossible_to_hit_without_losing_a_candidate": "retry_or_escalate",
    }
    correct = sum(1 for k, v in key.items() if exercise_8_answers.get(k) == v)
    return correct, len(key)


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to compression approaches", score_exercise_1),
        ("Exercise 2 -- order the Compression Fidelity Recipe", score_exercise_2),
        ("Exercise 3 -- compression ratio arithmetic", score_exercise_3),
        ("Exercise 4 -- load-bearing candidate classification", score_exercise_4),
        ("Exercise 5 -- fidelity check", score_exercise_5),
        ("Exercise 6 -- extractive vs. abstractive strategy selection", score_exercise_6),
        ("Exercise 7 -- naive-vs-fidelity-checked regression gate", score_exercise_7),
        ("Exercise 8 -- escalation decision", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 5 Exercises -- Score Report (REFERENCE SOLUTION)")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    print(
        f"Retention at the {COMPRESSION_TARGET_TOKENS}-token target from a "
        f"{RAW_SEGMENT_TOKENS}-token raw segment: {exercise_3_retention_percentage}% "
        f"({exercise_3_tokens_to_cut} tokens cut)"
    )
    print(
        f"Fidelity check missing candidates: {sorted(exercise_5_missing_candidates)} "
        f"| passes: {exercise_5_fidelity_check_passes}"
    )


if __name__ == "__main__":
    main()
