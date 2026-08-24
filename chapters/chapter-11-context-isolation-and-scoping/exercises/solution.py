"""
Chapter 11 Exercises: Context Isolation and Scoping -- REFERENCE SOLUTION

Scenario: Calloway County Child Welfare Case Review Network, a fictional
county child-welfare agency. Its case pipeline, CaseShield, has two
stages: a Primary Caseworker Agent makes an initial risk assessment, and
-- required by county policy, to preserve a genuinely independent second
read -- a Second-Opinion Reviewer Agent reviews the same case separately.
The Second-Opinion Reviewer must never see the Primary Caseworker's own
risk score, narrative reasoning, or recommendation. It SHOULD still
receive the shared, objective Risk Assessment Rubric version both stages
are required to apply, and the case's own identifying facts.

This file fills in every TODO with a correct reference answer and scores
a perfect total when run:

    python3 solution.py
"""

# ===========================================================================
# Exercise 1 -- match each scenario to the right isolation approach.
# ===========================================================================
APPROACHES = {"no_isolation", "isolation_drawn_too_broadly", "context_isolation_recipe"}

EXERCISE_1_SCENARIOS = {
    "second_opinion_sees_full_primary_transcript": (
        "The Second-Opinion Reviewer Agent receives the Primary "
        "Caseworker Agent's own full risk score, narrative reasoning, "
        "and recommendation alongside the case facts."
    ),
    "second_opinion_gets_nothing_from_primary_stage_at_all": (
        "The Second-Opinion Reviewer Agent receives none of the Primary "
        "Caseworker stage's context at all, including the shared, "
        "current Risk Assessment Rubric version both stages are "
        "required to apply."
    ),
    "second_opinion_isolated_from_opinion_but_given_shared_rubric": (
        "The Second-Opinion Reviewer Agent never sees the Primary "
        "Caseworker's own score, reasoning, or recommendation, but does "
        "receive the current Risk Assessment Rubric version through an "
        "explicit hand-off contract."
    ),
}

exercise_1_answers = {
    "second_opinion_sees_full_primary_transcript": "no_isolation",
    "second_opinion_gets_nothing_from_primary_stage_at_all": "isolation_drawn_too_broadly",
    "second_opinion_isolated_from_opinion_but_given_shared_rubric": "context_isolation_recipe",
}

# ===========================================================================
# Exercise 2 -- order the Context Isolation Recipe's six steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_name_goal": "Name the isolation goal, specifically -- what must be withheld and why.",
    "step_draw_boundary": "Draw the boundary around the prior agent's own opinion, not the whole step's context.",
    "step_separate_call": "Implement isolation as a genuinely separate call, not a filter on a shared history.",
    "step_handoff_contract": "Cross the boundary only through an explicit, curated hand-off contract.",
    "step_reverify": "Re-verify the boundary whenever the shared grounding it depends on changes.",
    "step_two_probes": "Test isolation with both a contamination probe and a starvation probe.",
}

exercise_2_order = [
    "step_name_goal",
    "step_draw_boundary",
    "step_separate_call",
    "step_handoff_contract",
    "step_reverify",
    "step_two_probes",
]

# ===========================================================================
# Exercise 3 (production-gear) -- per-approach budget and correctness check.
# ===========================================================================
SYSTEM_INSTRUCTIONS_TOKENS = 120
CASE_FACTS_TOKENS = 180
RESERVED_OUTPUT_TOKENS = 90
SHARED_RUBRIC_TOKENS = 60
PRIMARY_RAW_OUTPUT_TOKENS = 150
SECOND_OPINION_BUDGET_TOKENS = 450

exercise_3_no_isolation_tokens = SYSTEM_INSTRUCTIONS_TOKENS + CASE_FACTS_TOKENS + RESERVED_OUTPUT_TOKENS + SHARED_RUBRIC_TOKENS + PRIMARY_RAW_OUTPUT_TOKENS
exercise_3_too_broad_tokens = SYSTEM_INSTRUCTIONS_TOKENS + CASE_FACTS_TOKENS + RESERVED_OUTPUT_TOKENS
exercise_3_recipe_tokens = SYSTEM_INSTRUCTIONS_TOKENS + CASE_FACTS_TOKENS + RESERVED_OUTPUT_TOKENS + SHARED_RUBRIC_TOKENS

# ===========================================================================
# Exercise 4 (production-gear) -- separating opinion from shared fact.
# ===========================================================================
PRIMARY_CASEWORKER_RAW_OUTPUT = {
    "risk_score": "high",
    "narrative_reasoning": "Household shows three of five risk indicators on the current rubric...",
    "recommendation": "escalate_to_supervisor",
    "rubric_version_applied": "v4.2",
    "case_id": "CW-3391",
}

exercise_4_opinion_fields = {"risk_score", "narrative_reasoning", "recommendation"}
exercise_4_shared_fields = {"rubric_version_applied", "case_id"}

# ===========================================================================
# Exercise 5 (production-gear) -- build the Step 4 curated hand-off
# contract.
# ===========================================================================
SHARED_RUBRIC_DATA = {"rubric_version": "v4.2", "updated_months_ago": 1, "tokens": 60}


def build_handoff_contract(rubric_data):
    return {
        "rubric_version": rubric_data["rubric_version"],
        "updated_months_ago": rubric_data["updated_months_ago"],
        "source": "shared_rubric",
    }


exercise_5_handoff = build_handoff_contract(SHARED_RUBRIC_DATA)

# ===========================================================================
# Exercise 6 (production-gear) -- contamination probe.
# ===========================================================================
CONTAMINATION_CANDIDATES = {
    "bundle_1": {"case_id": "CW-3391", "rubric_version": "v4.2"},
    "bundle_2": {"case_id": "CW-3391", "rubric_version": "v4.2", "risk_score": "high"},
    "bundle_3": {"case_id": "CW-3391", "recommendation": "escalate_to_supervisor"},
}


def _is_contaminated(bundle):
    return "risk_score" in bundle or "narrative_reasoning" in bundle or "recommendation" in bundle


exercise_6_answers = {k: _is_contaminated(v) for k, v in CONTAMINATION_CANDIDATES.items()}

# ===========================================================================
# Exercise 7 (production-gear) -- starvation probe.
# ===========================================================================
REQUIRED_SHARED_FACTS = {"rubric_version"}
STARVATION_CANDIDATES = {
    "bundle_a": {"case_id": "CW-3391", "rubric_version": "v4.2"},
    "bundle_b": {"case_id": "CW-3391"},
    "bundle_c": {"rubric_version": "v4.2"},
}


def _is_starved(bundle, required=REQUIRED_SHARED_FACTS):
    return not required.issubset(bundle.keys())


exercise_7_answers = {k: _is_starved(v) for k, v in STARVATION_CANDIDATES.items()}

# ===========================================================================
# Exercise 8 (production-gear) -- combined 2x2 classification.
# ===========================================================================
EXERCISE_8_CANDIDATES = {
    "final_bundle_w": {"case_id": "CW-3391", "rubric_version": "v4.2"},
    "final_bundle_x": {"case_id": "CW-3391", "rubric_version": "v4.2", "risk_score": "high"},
    "final_bundle_y": {"case_id": "CW-3391"},
    "final_bundle_z": {"case_id": "CW-3391", "risk_score": "high"},
}


def _classify(bundle):
    contaminated = _is_contaminated(bundle)
    starved = _is_starved(bundle)
    if contaminated and starved:
        return "both_fail"
    if contaminated:
        return "contamination_fail"
    if starved:
        return "starvation_fail"
    return "compliant"


exercise_8_answers = {k: _classify(v) for k, v in EXERCISE_8_CANDIDATES.items()}


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "second_opinion_sees_full_primary_transcript": "no_isolation",
        "second_opinion_gets_nothing_from_primary_stage_at_all": "isolation_drawn_too_broadly",
        "second_opinion_isolated_from_opinion_but_given_shared_rubric": "context_isolation_recipe",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_name_goal", "step_draw_boundary", "step_separate_call",
        "step_handoff_contract", "step_reverify", "step_two_probes",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    expected_no_isolation = SYSTEM_INSTRUCTIONS_TOKENS + CASE_FACTS_TOKENS + RESERVED_OUTPUT_TOKENS + SHARED_RUBRIC_TOKENS + PRIMARY_RAW_OUTPUT_TOKENS
    expected_too_broad = SYSTEM_INSTRUCTIONS_TOKENS + CASE_FACTS_TOKENS + RESERVED_OUTPUT_TOKENS
    expected_recipe = SYSTEM_INSTRUCTIONS_TOKENS + CASE_FACTS_TOKENS + RESERVED_OUTPUT_TOKENS + SHARED_RUBRIC_TOKENS
    correct = 0
    correct += int(exercise_3_no_isolation_tokens == expected_no_isolation)
    correct += int(exercise_3_too_broad_tokens == expected_too_broad)
    correct += int(exercise_3_recipe_tokens == expected_recipe)
    return correct, 3


def score_exercise_4():
    expected_opinion = {"risk_score", "narrative_reasoning", "recommendation"}
    expected_shared = {"rubric_version_applied", "case_id"}
    correct = int(exercise_4_opinion_fields == expected_opinion) + int(exercise_4_shared_fields == expected_shared)
    return correct, 2


def score_exercise_5():
    expected = {"rubric_version": "v4.2", "updated_months_ago": 1, "source": "shared_rubric"}
    correct = int(exercise_5_handoff == expected)
    return correct, 1


def score_exercise_6():
    correct = sum(1 for k, v in CONTAMINATION_CANDIDATES.items() if exercise_6_answers.get(k) == _is_contaminated(v))
    return correct, len(CONTAMINATION_CANDIDATES)


def score_exercise_7():
    correct = sum(1 for k, v in STARVATION_CANDIDATES.items() if exercise_7_answers.get(k) == _is_starved(v))
    return correct, len(STARVATION_CANDIDATES)


def score_exercise_8():
    correct = sum(1 for k, v in EXERCISE_8_CANDIDATES.items() if exercise_8_answers.get(k) == _classify(v))
    return correct, len(EXERCISE_8_CANDIDATES)


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to isolation approaches", score_exercise_1),
        ("Exercise 2 -- order the Context Isolation Recipe", score_exercise_2),
        ("Exercise 3 -- per-approach budget and correctness", score_exercise_3),
        ("Exercise 4 -- separating opinion from shared fact", score_exercise_4),
        ("Exercise 5 -- build the Step 4 hand-off contract", score_exercise_5),
        ("Exercise 6 -- contamination probe", score_exercise_6),
        ("Exercise 7 -- starvation probe", score_exercise_7),
        ("Exercise 8 -- combined 2x2 classification", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 11 Exercises -- Score Report (REFERENCE SOLUTION)")
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
