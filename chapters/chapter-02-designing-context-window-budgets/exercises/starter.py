"""
Chapter 2 Exercises: Designing Context Window Budgets

Scenario for these exercises (deliberately different from the lesson's
Vantry Health Network/TriageLine hook, so you apply the recipe fresh,
not just recall the lesson's numbers):

    Corravine Freight is a fictional freight-dispatch company. Its
    internal dispatcher assistant, DispatchLine, serves several
    distinct request types on the same 16,000-token-context-window
    model -- a quick status lookup, a multi-leg route exception
    review, a carrier tool-dispatch turn, and a full manifest audit.
    Each request type has a genuinely different content shape, and
    each one needs its own derived budget allocation before it ships,
    per this chapter's five-step recipe.

Fill in every TODO below, then run this file:

    python3 starter.py

to see your score. Compare against solution.py for reference answers.
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

# ---------------------------------------------------------------------------
# Exercise 1 -- Match each DispatchLine request type to the archetype
# profile (a key in REQUEST_TYPE_PROFILES above) that best fits its shape.
# ---------------------------------------------------------------------------
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

# TODO 1: fill in the archetype key (e.g. "short_lookup") for each request
# type above.
exercise_1_answers = {
    "quick_status_lookup": "",           # TODO
    "multi_leg_route_exception": "",     # TODO
    "carrier_tool_dispatch_turn": "",    # TODO
    "full_manifest_audit": "",           # TODO
}

# ---------------------------------------------------------------------------
# Exercise 2 -- Put the five allocation-recipe steps (the keys of
# RECIPE_STEPS above) in the correct order, first to last.
# ---------------------------------------------------------------------------
exercise_2_order = []  # TODO: list of 5 step keys, in the correct order

# ---------------------------------------------------------------------------
# Exercise 3 (production-gear: budget arithmetic) -- Quick Status Lookup
# runs on a 16,000-token context window. Reserve 1,200 tokens for output
# (Line 5) and 600 tokens for system instructions (Line 1). Compute the
# remaining budget available to split across Lines 2, 3, and 4.
# ---------------------------------------------------------------------------
QUICK_LOOKUP_WINDOW = 16_000
QUICK_LOOKUP_OUTPUT = 1_200
QUICK_LOOKUP_SYSTEM = 600

exercise_3_remaining_budget = None  # TODO: integer

# ---------------------------------------------------------------------------
# Exercise 4 (production-gear: profile-split arithmetic) -- Split Exercise
# 3's remaining budget across Lines 2, 3, and 4 using the "short_lookup"
# profile's percentages from REQUEST_TYPE_PROFILES. Round each result to the
# nearest integer.
# ---------------------------------------------------------------------------
exercise_4_L2_tokens = None  # TODO: integer
exercise_4_L3_tokens = None  # TODO: integer
exercise_4_L4_tokens = None  # TODO: integer

# ---------------------------------------------------------------------------
# Exercise 5 (production-gear: worst-case validation) -- Multi-Leg Route
# Exception Review runs on the same 16,000-token window, with 1,500 tokens
# reserved for output and 600 for system instructions (remaining budget:
# 13,900 tokens), split using the "long_recurring" profile. Given the
# ALLOCATED tokens below (already computed for you) and the ACTUAL worst-case
# need for each line, mark each line "surplus" (allocated > actual need) or
# "deficit" (allocated < actual need).
# ---------------------------------------------------------------------------
MULTI_LEG_REMAINING_BUDGET = 13_900
MULTI_LEG_ALLOCATED = {
    "L2": round(MULTI_LEG_REMAINING_BUDGET * REQUEST_TYPE_PROFILES["long_recurring"]["L2"]),
    "L3": round(MULTI_LEG_REMAINING_BUDGET * REQUEST_TYPE_PROFILES["long_recurring"]["L3"]),
    "L4": round(MULTI_LEG_REMAINING_BUDGET * REQUEST_TYPE_PROFILES["long_recurring"]["L4"]),
}
MULTI_LEG_ACTUAL_WORST_CASE = {"L2": 4_200, "L3": 6_800, "L4": 3_000}

exercise_5_answers = {
    "L2": "",  # TODO: "surplus" or "deficit"
    "L3": "",  # TODO: "surplus" or "deficit"
    "L4": "",  # TODO: "surplus" or "deficit"
}

# ---------------------------------------------------------------------------
# Exercise 6 (production-gear: reuse-safety judgment) -- A teammate proposes
# reusing Quick Status Lookup's exact budget allocation (Exercises 3-4) for
# Multi-Leg Route Exception Review, since both run on the identical
# 16,000-token model. Given Exercise 5's own deficit/surplus findings for
# the CORRECTLY re-derived Multi-Leg allocation, is reusing Quick Status
# Lookup's budget (a DIFFERENT, tighter profile) for Multi-Leg safe?
# ---------------------------------------------------------------------------
exercise_6_safe_to_reuse = None  # TODO: True or False

# ---------------------------------------------------------------------------
# Exercise 7 (production-gear: design from scratch) -- Full Manifest Audit
# is a new request type on a larger, 32,000-token-window model. Reserve
# 2,000 tokens for output and 1,000 for system instructions. Using the
# "long_document" profile, compute the remaining budget and the token
# allocation for Lines 2, 3, and 4 (round to the nearest integer).
# ---------------------------------------------------------------------------
MANIFEST_AUDIT_WINDOW = 32_000
MANIFEST_AUDIT_OUTPUT = 2_000
MANIFEST_AUDIT_SYSTEM = 1_000

exercise_7_remaining_budget = None  # TODO: integer
exercise_7_L2_tokens = None         # TODO: integer
exercise_7_L3_tokens = None         # TODO: integer
exercise_7_L4_tokens = None         # TODO: integer

# ---------------------------------------------------------------------------
# Exercise 8 (production-gear: recipe completeness gate) -- Before a new
# request type's budget ships, a real team checks that all 5 recipe steps
# were actually followed for it, not just guessed at. Fill in
# exercise_8_considered with all 5 step keys (from RECIPE_STEPS above) you
# applied while working through Exercises 1-7.
# ---------------------------------------------------------------------------
exercise_8_considered = set()  # TODO: add all 5 step keys


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
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
    print("Chapter 2 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every allocation correctly derived.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
