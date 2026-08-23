"""
Chapter 2 Exercises: Designing Context Window Budgets -- REFERENCE SOLUTION

See starter.py for the full scenario description (Corravine Freight's
DispatchLine) and task instructions. This file is the fully filled-in
reference and scores a perfect total when run.
"""

RECIPE_STEPS = {
    "step_fix_limit": "Fix the hard context-window limit for the specific model in use.",
    "step_reserve_output": "Reserve Working Space (Line 5) first, sized to this request type's expected response length.",
    "step_fix_system": "Fix Line 1 (System Instructions) as a measured, stable subtraction.",
    "step_split_profile": "Split what's left across Lines 2, 3, and 4 by this request type's real content profile.",
    "step_validate_worst_case": "Validate the allocation against the worst realistic case, not the median case.",
}

REQUEST_TYPE_PROFILES = {
    "short_lookup": {"L2": 0.45, "L3": 0.35, "L4": 0.20},
    "long_recurring": {"L2": 0.35, "L3": 0.40, "L4": 0.25},
    "tool_heavy": {"L2": 0.55, "L3": 0.25, "L4": 0.20},
    "long_document": {"L2": 0.65, "L3": 0.20, "L4": 0.15},
}

EXERCISE_1_REQUEST_TYPES = {
    "quick_status_lookup": (
        "A dispatcher asks for one shipment's current status. One or two "
        "turns, a small amount of tracking-system grounding, almost no "
        "history or persisted memory needed."
    ),
    "multi_leg_route_exception": (
        "A dispatcher works through a shipment with multiple exceptions "
        "across several legs, over many turns, needing a growing "
        "conversation history and a fuller recalled record of prior "
        "exceptions on this shipment."
    ),
    "carrier_tool_dispatch_turn": (
        "DispatchLine calls a carrier API tool to re-route a shipment; "
        "the tool's definition and its returned result dominate the "
        "request, with a short conversation and little persisted memory."
    ),
    "full_manifest_audit": (
        "DispatchLine reviews one large uploaded manifest document line "
        "by line; the document itself dominates the request, with little "
        "conversation history or persisted memory involved."
    ),
}

# Exercise 1: match each request type to its archetype profile.
exercise_1_answers = {
    "quick_status_lookup": "short_lookup",
    "multi_leg_route_exception": "long_recurring",
    "carrier_tool_dispatch_turn": "tool_heavy",
    "full_manifest_audit": "long_document",
}

# Exercise 2: the recipe's correct order -- fix the limit, reserve output,
# fix system instructions, split the profile, then validate worst-case.
exercise_2_order = [
    "step_fix_limit",
    "step_reserve_output",
    "step_fix_system",
    "step_split_profile",
    "step_validate_worst_case",
]

QUICK_LOOKUP_WINDOW = 16_000
QUICK_LOOKUP_OUTPUT = 1_200
QUICK_LOOKUP_SYSTEM = 600

# Exercise 3: 16,000 - 1,200 - 600 = 14,200
exercise_3_remaining_budget = QUICK_LOOKUP_WINDOW - QUICK_LOOKUP_OUTPUT - QUICK_LOOKUP_SYSTEM

# Exercise 4: split 14,200 by the short_lookup profile (45/35/20).
_profile_4 = REQUEST_TYPE_PROFILES["short_lookup"]
exercise_4_L2_tokens = round(exercise_3_remaining_budget * _profile_4["L2"])
exercise_4_L3_tokens = round(exercise_3_remaining_budget * _profile_4["L3"])
exercise_4_L4_tokens = round(exercise_3_remaining_budget * _profile_4["L4"])

MULTI_LEG_REMAINING_BUDGET = 13_900
MULTI_LEG_ALLOCATED = {
    "L2": round(MULTI_LEG_REMAINING_BUDGET * REQUEST_TYPE_PROFILES["long_recurring"]["L2"]),
    "L3": round(MULTI_LEG_REMAINING_BUDGET * REQUEST_TYPE_PROFILES["long_recurring"]["L3"]),
    "L4": round(MULTI_LEG_REMAINING_BUDGET * REQUEST_TYPE_PROFILES["long_recurring"]["L4"]),
}
MULTI_LEG_ACTUAL_WORST_CASE = {"L2": 4_200, "L3": 6_800, "L4": 3_000}

# Exercise 5: allocated (L2=4,865 L3=5,560 L4=3,475) vs actual worst-case
# (L2=4,200 L3=6,800 L4=3,000) -- L2 and L4 have room to spare (surplus),
# L3 is under-provisioned for the true worst case (deficit).
exercise_5_answers = {
    "L2": "surplus",
    "L3": "deficit",
    "L4": "surplus",
}

# Exercise 6: NOT safe. Multi-Leg Route Exception Review's own correctly
# re-derived allocation already runs a deficit on Line 3 for its worst
# case -- reusing Quick Status Lookup's tighter, short-lookup-shaped
# budget (even less generous on history) would only make that deficit
# worse, exactly the mistake TriageLine's team made with Chronic Care
# Check-In in the lesson.
exercise_6_safe_to_reuse = False

MANIFEST_AUDIT_WINDOW = 32_000
MANIFEST_AUDIT_OUTPUT = 2_000
MANIFEST_AUDIT_SYSTEM = 1_000

# Exercise 7: 32,000 - 2,000 - 1,000 = 29,000, split by long_document (65/20/15).
exercise_7_remaining_budget = MANIFEST_AUDIT_WINDOW - MANIFEST_AUDIT_OUTPUT - MANIFEST_AUDIT_SYSTEM
_profile_7 = REQUEST_TYPE_PROFILES["long_document"]
exercise_7_L2_tokens = round(exercise_7_remaining_budget * _profile_7["L2"])
exercise_7_L3_tokens = round(exercise_7_remaining_budget * _profile_7["L3"])
exercise_7_L4_tokens = round(exercise_7_remaining_budget * _profile_7["L4"])

# Exercise 8: all 5 recipe steps were applied across Exercises 1-7 above.
exercise_8_considered = {
    "step_fix_limit",
    "step_reserve_output",
    "step_fix_system",
    "step_split_profile",
    "step_validate_worst_case",
}


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "quick_status_lookup": "short_lookup",
        "multi_leg_route_exception": "long_recurring",
        "carrier_tool_dispatch_turn": "tool_heavy",
        "full_manifest_audit": "long_document",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_fix_limit",
        "step_reserve_output",
        "step_fix_system",
        "step_split_profile",
        "step_validate_worst_case",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    expected = QUICK_LOOKUP_WINDOW - QUICK_LOOKUP_OUTPUT - QUICK_LOOKUP_SYSTEM
    correct = 1 if exercise_3_remaining_budget == expected else 0
    return correct, 1


def score_exercise_4():
    remaining = QUICK_LOOKUP_WINDOW - QUICK_LOOKUP_OUTPUT - QUICK_LOOKUP_SYSTEM
    profile = REQUEST_TYPE_PROFILES["short_lookup"]
    expected_L2 = round(remaining * profile["L2"])
    expected_L3 = round(remaining * profile["L3"])
    expected_L4 = round(remaining * profile["L4"])
    correct = 0
    correct += int(exercise_4_L2_tokens == expected_L2)
    correct += int(exercise_4_L3_tokens == expected_L3)
    correct += int(exercise_4_L4_tokens == expected_L4)
    return correct, 3


def score_exercise_5():
    key = {}
    for line, allocated in MULTI_LEG_ALLOCATED.items():
        actual = MULTI_LEG_ACTUAL_WORST_CASE[line]
        key[line] = "surplus" if allocated > actual else "deficit"
    correct = sum(
        1 for line, expected in key.items()
        if exercise_5_answers.get(line, "").strip().lower() == expected
    )
    return correct, len(key)


def score_exercise_6():
    correct = 1 if exercise_6_safe_to_reuse is False else 0
    return correct, 1


def score_exercise_7():
    remaining = MANIFEST_AUDIT_WINDOW - MANIFEST_AUDIT_OUTPUT - MANIFEST_AUDIT_SYSTEM
    profile = REQUEST_TYPE_PROFILES["long_document"]
    expected_L2 = round(remaining * profile["L2"])
    expected_L3 = round(remaining * profile["L3"])
    expected_L4 = round(remaining * profile["L4"])
    correct = 0
    correct += int(exercise_7_remaining_budget == remaining)
    correct += int(exercise_7_L2_tokens == expected_L2)
    correct += int(exercise_7_L3_tokens == expected_L3)
    correct += int(exercise_7_L4_tokens == expected_L4)
    return correct, 4


def score_exercise_8():
    all_five = set(RECIPE_STEPS.keys())
    correct = len(all_five & exercise_8_considered)
    return correct, len(all_five)


def main():
    exercises = [
        ("Exercise 1 -- match request types to profiles", score_exercise_1),
        ("Exercise 2 -- order the allocation recipe steps", score_exercise_2),
        ("Exercise 3 -- reserve output + system, compute remaining budget", score_exercise_3),
        ("Exercise 4 -- profile-split arithmetic", score_exercise_4),
        ("Exercise 5 -- worst-case validation (surplus/deficit)", score_exercise_5),
        ("Exercise 6 -- reuse-safety judgment", score_exercise_6),
        ("Exercise 7 -- design a new allocation from scratch", score_exercise_7),
        ("Exercise 8 -- recipe completeness gate", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 2 Exercises -- Score Report (REFERENCE SOLUTION)")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    print(
        f"Quick Status Lookup: remaining={exercise_3_remaining_budget}, "
        f"L2={exercise_4_L2_tokens} L3={exercise_4_L3_tokens} L4={exercise_4_L4_tokens}"
    )
    print(
        f"Full Manifest Audit: remaining={exercise_7_remaining_budget}, "
        f"L2={exercise_7_L2_tokens} L3={exercise_7_L3_tokens} L4={exercise_7_L4_tokens}"
    )


if __name__ == "__main__":
    main()
