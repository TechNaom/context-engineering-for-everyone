"""
Chapter 12 Exercises: Evaluating Context Quality -- REFERENCE SOLUTION

Scenario: Merrivale County Emergency Housing Placement Network, a
fictional county agency. Its placement pipeline, PlacementGuard,
assembles context for a Housing Placement Agent from four sources:
applicant_intake, shelter_availability, medical_needs_flags, and
prior_placement_notes -- every one of them correctly budgeted, fresh,
retrieved, and isolated per Chapters 1-11's own recipes.

This file fills in every TODO with a correct reference answer and scores
a perfect total when run:

    python3 solution.py
"""

# ===========================================================================
# Exercise 1 -- match each scenario to the right evaluation approach.
# ===========================================================================
APPROACHES = {"no_evaluation", "proxy_only_evaluation", "context_evaluation_recipe"}

EXERCISE_1_SCENARIOS = {
    "bundle_shipped_straight_from_assembly": (
        "PlacementGuard sends the assembled bundle straight to the model "
        "once every Chapter 1-11 per-step check passes -- no check runs "
        "on the finished bundle itself."
    ),
    "bundle_checked_for_source_presence_only": (
        "PlacementGuard confirms all four expected sources (applicant_intake, "
        "shelter_availability, medical_needs_flags, prior_placement_notes) "
        "are present in the bundle, and reports the bundle complete on "
        "that basis alone."
    ),
    "bundle_checked_fact_by_fact_with_a_gate": (
        "PlacementGuard scores completeness against a specific list of "
        "required facts for this case, computes a real noise ratio, "
        "audits where each required fact landed, and combines all three "
        "into a single pass/fail gate before the call."
    ),
}

exercise_1_answers = {
    "bundle_shipped_straight_from_assembly": "no_evaluation",
    "bundle_checked_for_source_presence_only": "proxy_only_evaluation",
    "bundle_checked_fact_by_fact_with_a_gate": "context_evaluation_recipe",
}

# ===========================================================================
# Exercise 2 -- order the Context Evaluation Recipe's six steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_define_facts": "Define completeness at the fact level, per case, before assembly.",
    "step_score_completeness": "Score completeness against that required-fact list, not source presence.",
    "step_score_noise": "Score relevance as a noise ratio, not a token count.",
    "step_positional_audit": "Audit where each required fact actually landed in the assembled sequence.",
    "step_combined_gate": "Combine completeness, noise ratio, and positional risk into one pre-call gate.",
    "step_reverify": "Re-run the evaluation whenever the assembly pipeline itself changes.",
}

exercise_2_order = [
    "step_define_facts",
    "step_score_completeness",
    "step_score_noise",
    "step_positional_audit",
    "step_combined_gate",
    "step_reverify",
]

# ===========================================================================
# Exercise 3 (production-gear) -- completeness score.
# ===========================================================================
CASE_MC5521_REQUIRED_FACTS = {
    "current_medical_accommodation_need": {"priority": "critical", "found": True},
    "household_size": {"priority": "standard", "found": True},
    "prior_no_show_flag": {"priority": "standard", "found": False},
    "eligible_shelter_capacity": {"priority": "standard", "found": True},
}


def completeness_score(required_facts):
    found = sum(1 for f in required_facts.values() if f["found"])
    return found / len(required_facts)


exercise_3_completeness = completeness_score(CASE_MC5521_REQUIRED_FACTS)

# ===========================================================================
# Exercise 4 (production-gear) -- noise ratio.
# ===========================================================================
NOISE_TOKENS = 300
BUNDLE_TOTAL_TOKENS = 2500
NOISE_THRESHOLD = 0.10


def noise_ratio(noise_tokens, total_tokens):
    return noise_tokens / total_tokens


exercise_4_noise_ratio = noise_ratio(NOISE_TOKENS, BUNDLE_TOTAL_TOKENS)
exercise_4_exceeds_threshold = exercise_4_noise_ratio > NOISE_THRESHOLD

# ===========================================================================
# Exercise 5 (production-gear) -- positional audit.
# ===========================================================================
FRONT_BUCKET_END = 375
BACK_BUCKET_START = 2125
FACT_POSITIONS = {
    "current_medical_accommodation_need": 1400,   # middle
    "household_size": 120,                        # front
    "eligible_shelter_capacity": 2300,             # back
}


def position_bucket(position, front_end=FRONT_BUCKET_END, back_start=BACK_BUCKET_START):
    if position < front_end:
        return "front"
    if position > back_start:
        return "back"
    return "middle"


exercise_5_answers = {k: position_bucket(v) for k, v in FACT_POSITIONS.items()}

# ===========================================================================
# Exercise 6 (production-gear) -- combined context quality gate.
# ===========================================================================
GATE_CANDIDATES = {
    "bundle_p": {"completeness": 1.0, "noise_ratio": 0.05, "critical_fact_bucket": "front"},
    "bundle_q": {"completeness": 0.8, "noise_ratio": 0.05, "critical_fact_bucket": "front"},
    "bundle_r": {"completeness": 1.0, "noise_ratio": 0.05, "critical_fact_bucket": "middle"},
}


def _gate_passes(candidate):
    return (
        candidate["completeness"] == 1.0
        and candidate["noise_ratio"] <= NOISE_THRESHOLD
        and candidate["critical_fact_bucket"] != "middle"
    )


exercise_6_answers = {k: _gate_passes(v) for k, v in GATE_CANDIDATES.items()}

# ===========================================================================
# Exercise 7 (production-gear) -- fix-simulation arithmetic.
# ===========================================================================
BEFORE_TOTAL = 2500
NOISE_REMOVED = 300
FACT_ADDED_TOKENS = 90
SUMMARY_ADDED_TOKENS = 60
AFTER_CEILING = 2400

exercise_7_after_total = BEFORE_TOTAL - NOISE_REMOVED + FACT_ADDED_TOKENS + SUMMARY_ADDED_TOKENS
exercise_7_fits_ceiling = exercise_7_after_total <= AFTER_CEILING

# ===========================================================================
# Exercise 8 (production-gear) -- combined completeness/quality classification.
# ===========================================================================
EXERCISE_8_CANDIDATES = {
    "final_bundle_w": {"completeness": 1.0, "noise_ratio": 0.03, "critical_fact_bucket": "back"},
    "final_bundle_x": {"completeness": 0.75, "noise_ratio": 0.03, "critical_fact_bucket": "back"},
    "final_bundle_y": {"completeness": 1.0, "noise_ratio": 0.20, "critical_fact_bucket": "middle"},
    "final_bundle_z": {"completeness": 0.5, "noise_ratio": 0.25, "critical_fact_bucket": "middle"},
}


def _quality_ok(candidate):
    return candidate["noise_ratio"] <= NOISE_THRESHOLD and candidate["critical_fact_bucket"] != "middle"


def _classify(candidate):
    completeness_ok = candidate["completeness"] == 1.0
    quality_ok = _quality_ok(candidate)
    if completeness_ok and quality_ok:
        return "compliant"
    if not completeness_ok and quality_ok:
        return "completeness_fail"
    if completeness_ok and not quality_ok:
        return "quality_fail"
    return "both_fail"


exercise_8_answers = {k: _classify(v) for k, v in EXERCISE_8_CANDIDATES.items()}


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "bundle_shipped_straight_from_assembly": "no_evaluation",
        "bundle_checked_for_source_presence_only": "proxy_only_evaluation",
        "bundle_checked_fact_by_fact_with_a_gate": "context_evaluation_recipe",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_define_facts", "step_score_completeness", "step_score_noise",
        "step_positional_audit", "step_combined_gate", "step_reverify",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    expected = 3 / 4
    correct = int(abs(exercise_3_completeness - expected) < 1e-9)
    return correct, 1


def score_exercise_4():
    expected_ratio = NOISE_TOKENS / BUNDLE_TOTAL_TOKENS
    correct = 0
    correct += int(abs(exercise_4_noise_ratio - expected_ratio) < 1e-9)
    correct += int(exercise_4_exceeds_threshold == (expected_ratio > NOISE_THRESHOLD))
    return correct, 2


def score_exercise_5():
    expected = {
        "current_medical_accommodation_need": "middle",
        "household_size": "front",
        "eligible_shelter_capacity": "back",
    }
    correct = sum(1 for k, v in expected.items() if exercise_5_answers.get(k) == v)
    return correct, len(expected)


def score_exercise_6():
    correct = sum(1 for k, v in GATE_CANDIDATES.items() if exercise_6_answers.get(k) == _gate_passes(v))
    return correct, len(GATE_CANDIDATES)


def score_exercise_7():
    expected_total = BEFORE_TOTAL - NOISE_REMOVED + FACT_ADDED_TOKENS + SUMMARY_ADDED_TOKENS
    correct = 0
    correct += int(exercise_7_after_total == expected_total)
    correct += int(exercise_7_fits_ceiling == (expected_total <= AFTER_CEILING))
    return correct, 2


def score_exercise_8():
    correct = sum(1 for k, v in EXERCISE_8_CANDIDATES.items() if exercise_8_answers.get(k) == _classify(v))
    return correct, len(EXERCISE_8_CANDIDATES)


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to evaluation approaches", score_exercise_1),
        ("Exercise 2 -- order the Context Evaluation Recipe", score_exercise_2),
        ("Exercise 3 -- completeness score", score_exercise_3),
        ("Exercise 4 -- noise ratio", score_exercise_4),
        ("Exercise 5 -- positional audit", score_exercise_5),
        ("Exercise 6 -- combined context quality gate", score_exercise_6),
        ("Exercise 7 -- fix-simulation arithmetic", score_exercise_7),
        ("Exercise 8 -- combined completeness/quality classification", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 12 Exercises -- Score Report (REFERENCE SOLUTION)")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")


if __name__ == "__main__":
    main()
