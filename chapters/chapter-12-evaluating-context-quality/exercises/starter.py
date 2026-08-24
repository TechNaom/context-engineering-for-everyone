"""
Chapter 12 Exercises: Evaluating Context Quality

Scenario: Merrivale County Emergency Housing Placement Network, a
fictional county agency. Its placement pipeline, PlacementGuard,
assembles context for a Housing Placement Agent from four sources:
applicant_intake, shelter_availability, medical_needs_flags, and
prior_placement_notes -- every one of them correctly budgeted, fresh,
retrieved, and isolated per Chapters 1-11's own recipes. Your job is
this chapter's own new skill: checking the FINISHED bundle itself for
completeness, noise, and positional risk, rather than trusting that a
correctly-run assembly pipeline guarantees a good result.

Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report. Compare against solution.py, which scores a
perfect total.
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

# TODO: assign an approach name from APPROACHES to each scenario.
exercise_1_answers = {
    "bundle_shipped_straight_from_assembly": None,  # TODO
    "bundle_checked_for_source_presence_only": None,  # TODO
    "bundle_checked_fact_by_fact_with_a_gate": None,  # TODO
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

# TODO: put the six step keys above in the correct order.
exercise_2_order = [
    # TODO
]

# ===========================================================================
# Exercise 3 (production-gear) -- completeness score. Case MC-5521 requires
# four facts. Compute the completeness score (found / total) as a float.
# ===========================================================================
CASE_MC5521_REQUIRED_FACTS = {
    "current_medical_accommodation_need": {"priority": "critical", "found": True},
    "household_size": {"priority": "standard", "found": True},
    "prior_no_show_flag": {"priority": "standard", "found": False},
    "eligible_shelter_capacity": {"priority": "standard", "found": True},
}


def completeness_score(required_facts):
    # TODO: return found / total as a float.
    return 0.0  # TODO


exercise_3_completeness = completeness_score(CASE_MC5521_REQUIRED_FACTS)

# ===========================================================================
# Exercise 4 (production-gear) -- noise ratio. prior_placement_notes
# contains 300 tokens carried over from a DIFFERENT applicant's own case
# by a stale join, out of a 2500-token total bundle. Compute the noise
# ratio, and whether it exceeds a 10% threshold.
# ===========================================================================
NOISE_TOKENS = 300
BUNDLE_TOTAL_TOKENS = 2500
NOISE_THRESHOLD = 0.10


def noise_ratio(noise_tokens, total_tokens):
    # TODO: return noise_tokens / total_tokens as a float.
    return 0.0  # TODO


exercise_4_noise_ratio = noise_ratio(NOISE_TOKENS, BUNDLE_TOTAL_TOKENS)
# TODO: True if exercise_4_noise_ratio exceeds NOISE_THRESHOLD.
exercise_4_exceeds_threshold = None  # TODO

# ===========================================================================
# Exercise 5 (production-gear) -- positional audit. The bundle is 2500
# tokens; front bucket is the first 15% (< 375), back bucket is the last
# 15% (> 2125), everything else is middle. Classify each fact's position.
# ===========================================================================
FRONT_BUCKET_END = 375
BACK_BUCKET_START = 2125
FACT_POSITIONS = {
    "current_medical_accommodation_need": 1400,   # middle
    "household_size": 120,                        # front
    "eligible_shelter_capacity": 2300,             # back
}


def position_bucket(position, front_end=FRONT_BUCKET_END, back_start=BACK_BUCKET_START):
    # TODO: return "front", "middle", or "back".
    return ""  # TODO


# TODO: bucket name for each fact.
exercise_5_answers = {
    "current_medical_accommodation_need": None,  # TODO
    "household_size": None,  # TODO
    "eligible_shelter_capacity": None,  # TODO
}

# ===========================================================================
# Exercise 6 (production-gear) -- combined context quality gate. A gate
# passes only if completeness == 1.0, noise_ratio <= 0.10, and no CRITICAL
# fact is bucketed "middle". Evaluate three candidate bundles.
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


# TODO: True/False for each -- does this bundle pass the gate?
exercise_6_answers = {
    "bundle_p": None,  # TODO
    "bundle_q": None,  # TODO
    "bundle_r": None,  # TODO
}

# ===========================================================================
# Exercise 7 (production-gear) -- fix-simulation arithmetic. Starting from
# a 2500-token bundle with 300 noise tokens: the fix removes all 300 noise
# tokens, adds a 90-token missing fact, and adds a 60-token promoted-summary
# section for the critical fact. Compute the resulting total and confirm it
# both fits a 2400-token ceiling and eliminates all noise.
# ===========================================================================
BEFORE_TOTAL = 2500
NOISE_REMOVED = 300
FACT_ADDED_TOKENS = 90
SUMMARY_ADDED_TOKENS = 60
AFTER_CEILING = 2400

# TODO: compute the after-fix total.
exercise_7_after_total = 0  # TODO
# TODO: True if exercise_7_after_total <= AFTER_CEILING.
exercise_7_fits_ceiling = None  # TODO

# ===========================================================================
# Exercise 8 (production-gear) -- combine completeness and quality (noise +
# position together) into a single classification: "compliant" (both ok),
# "completeness_fail" (completeness < 1.0 only), "quality_fail" (noise or
# position bad, completeness fine), or "both_fail" (both bad).
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


# TODO: classification string for each bundle.
exercise_8_answers = {
    "final_bundle_w": None,  # TODO
    "final_bundle_x": None,  # TODO
    "final_bundle_y": None,  # TODO
    "final_bundle_z": None,  # TODO
}


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
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
    print("Chapter 12 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every exercise correctly reasoned.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
