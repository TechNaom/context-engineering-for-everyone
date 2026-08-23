"""
Chapter 7 Exercises: Multi-Source Context Assembly

Scenario: Corrinvale Independent Pharmacy Network, a fictional
independent pharmacy chain. Its pharmacist-facing assistant, ScriptLine,
assembles context for "Refill Safety Review" requests from several
sources at once: a retrieved chart-summary document (sometimes stale), a
live tool call to the pharmacy-benefit and EHR systems, the conversation
so far with the patient, and the pharmacy's own system instructions.
Chapters 1-6's own recipes have already run for this request type: a
correct budget, correct short-term/long-term memory handling, nothing
over budget needing compression, and no positional risk. Every source is
individually correct -- your job is this chapter's own new skill:
deciding which sources belong, ranking their authority, detecting and
resolving contradictions between them, and deduplicating restated
content, before Chapter 6's own ordering recipe ever runs.

Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report. Compare against solution.py, which scores a
perfect total.
"""

# ===========================================================================
# Exercise 1 -- match each scenario to the right assembly approach.
# Choose from APPROACHES for each key below.
# ===========================================================================
APPROACHES = {"naive_concatenation", "string_dedup_only", "source_assembly_recipe"}

EXERCISE_1_SCENARIOS = {
    "sources_joined_in_arrival_order_no_overlap_or_conflict_check": (
        "System instructions, retrieved documents, tool output, and "
        "history are joined in whatever order they became available, "
        "with no check for overlap or disagreement between them."
    ),
    "exact_duplicate_text_stripped_but_reworded_conflicts_untouched": (
        "Identical or near-identical strings across sources are removed, "
        "but there is no authority ranking and no check for two sources "
        "disagreeing about the same fact in different words."
    ),
    "sources_inventoried_ranked_conflicts_resolved_deduped_then_ordered": (
        "Every source is inventoried and typed, authority is ranked in "
        "advance per request type, overlapping and contradicting claims "
        "are explicitly detected and resolved, restated content is "
        "deduplicated, and the resolved set is handed to Chapter 6's own "
        "ordering recipe."
    ),
}

# TODO: assign an approach name from APPROACHES to each scenario.
exercise_1_answers = {
    "sources_joined_in_arrival_order_no_overlap_or_conflict_check": None,  # TODO
    "exact_duplicate_text_stripped_but_reworded_conflicts_untouched": None,  # TODO
    "sources_inventoried_ranked_conflicts_resolved_deduped_then_ordered": None,  # TODO
}

# ===========================================================================
# Exercise 2 -- order the Source Assembly Recipe's six steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_inventory_sources": "Inventory every candidate source explicitly -- name each source and its type before assembling anything.",
    "step_rank_authority": "Assign each source type an authority rank for this request type -- decide in advance which source wins when two disagree.",
    "step_detect_conflicts": "Detect overlapping and contradicting claims before assembly, rather than trusting the model to notice them once assembled.",
    "step_resolve_or_surface": "Resolve or explicitly surface each contradiction found, using the authority ranking or flagging it if authority doesn't clearly settle it.",
    "step_deduplicate": "Deduplicate restated content across sources -- the same fact stated twice in different words still wastes budget.",
    "step_handoff_to_ordering": "Hand the resolved, deduplicated set to Chapter 6's own Context Ordering Recipe, rather than re-deriving it.",
}

# TODO: put the six step keys above in the correct order.
exercise_2_order = [
    # TODO
]

# ===========================================================================
# Exercise 3 (production-gear) -- authority-rank conflict resolution.
# ===========================================================================
AUTHORITY_RANK = {
    "system_instructions": 4,
    "live_tool_output": 3,
    "conversation_history_this_session": 2,
    "retrieved_document": 1,
}

EXERCISE_3_CONFLICTS = {
    "conflict_a": {
        "claim": "patient_active_prescription_list",
        "source_x": "retrieved_document",
        "source_y": "live_tool_output",
    },
    "conflict_b": {
        "claim": "new_otc_supplement_disclosed",
        "source_x": "conversation_history_this_session",
        "source_y": "retrieved_document",
    },
    "conflict_c": {
        "claim": "refill_approval_policy_wording",
        "source_x": "retrieved_document",
        "source_y": "system_instructions",
    },
}

# TODO: for each conflict, which source (source_x's or source_y's name)
# wins per AUTHORITY_RANK -- the one with the higher rank.
exercise_3_answers = {
    "conflict_a": None,  # TODO
    "conflict_b": None,  # TODO
    "conflict_c": None,  # TODO
}

# ===========================================================================
# Exercise 4 (production-gear) -- contradiction detection. True = the two
# claims genuinely contradict each other about the same fact; False = the
# claims are a restatement of the same fact, or are about different facts
# entirely.
#
#   prescription_count_conflict: an older chart summary says the patient
#     has 2 active prescriptions; a live EHR pull says 4 active
#     prescriptions -- different counts for the same fact.
#   warfarin_dose_restatement: both sources say the patient takes 5mg
#     warfarin daily -- same claim, different wording.
#   clinic_hours_vs_pharmacy_hours: one source states clinic hours, the
#     other states pharmacy-counter hours -- different facts entirely.
#   allergy_status_conflict: a retrieved chart says no known drug
#     allergies; a live EHR flag says a penicillin allergy was documented
#     last month -- a genuine, high-stakes contradiction.
#   insurance_provider_restatement: both sources name the same insurance
#     provider, just formatted differently.
#   refill_quantity_conflict: a prior-authorization document says a
#     30-day supply was approved; a live pharmacy-benefit tool says a
#     90-day supply was approved -- a genuine conflict on quantity.
# ===========================================================================
EXERCISE_4_CLAIM_PAIRS = {
    "prescription_count_conflict": True,
    "warfarin_dose_restatement": False,
    "clinic_hours_vs_pharmacy_hours": False,
    "allergy_status_conflict": True,
    "insurance_provider_restatement": False,
    "refill_quantity_conflict": True,
}

# TODO: for each key below, decide True (genuine contradiction) or False
# (restatement, or unrelated facts).
exercise_4_answers = {
    "prescription_count_conflict": None,  # TODO
    "warfarin_dose_restatement": None,  # TODO
    "clinic_hours_vs_pharmacy_hours": None,  # TODO
    "allergy_status_conflict": None,  # TODO
    "insurance_provider_restatement": None,  # TODO
    "refill_quantity_conflict": None,  # TODO
}

# ===========================================================================
# Exercise 5 (production-gear) -- deduplication arithmetic. For each claim,
# multiple sources assert the same fact at different token costs. Keep only
# the highest-authority instance; compute the tokens saved by dropping the
# rest.
# ===========================================================================
CLAIM_SOURCE_INSTANCES = {
    "patient_active_prescription_list": [
        ("retrieved_document", 140),
        ("live_tool_output", 35),
    ],
    "allergy_status": [
        ("retrieved_document", 60),
        ("live_tool_output", 25),
        ("conversation_history_this_session", 20),
    ],
    "pharmacy_hours": [
        ("system_instructions", 15),
    ],
}

# TODO: for each claim_id, which source name (per AUTHORITY_RANK) should be
# kept, and how many tokens are saved by dropping the other instance(s)
# (sum of all instance token costs, minus the kept instance's own cost)?
exercise_5_kept_sources = {
    "patient_active_prescription_list": None,  # TODO: str
    "allergy_status": None,  # TODO: str
    "pharmacy_hours": None,  # TODO: str
}
exercise_5_tokens_saved = {
    "patient_active_prescription_list": None,  # TODO: int
    "allergy_status": None,  # TODO: int
    "pharmacy_hours": None,  # TODO: int
}

# ===========================================================================
# Exercise 6 (production-gear) -- budget check after resolution.
# ===========================================================================
SCRIPTLINE_BUDGET_TOKENS = 900
NAIVE_ASSEMBLY_TOTAL_TOKENS = 1_040

# TODO: total tokens freed (sum of exercise_5_tokens_saved's values), the
# resolved total (NAIVE_ASSEMBLY_TOTAL_TOKENS minus tokens freed), and
# whether that resolved total fits within SCRIPTLINE_BUDGET_TOKENS.
exercise_6_tokens_freed = None  # TODO: int
exercise_6_resolved_total = None  # TODO: int
exercise_6_within_budget = None  # TODO: bool

# ===========================================================================
# Exercise 7 (production-gear) -- naive-vs-recipe regression gate. A
# load-bearing contradiction (the allergy-status conflict) exists in the
# raw assembled sources. Does naive concatenation still contain it
# unresolved? Does the Source Assembly Recipe resolve it? Does the
# resolved result still fit the budget?
# ===========================================================================
exercise_7_naive_contains_contradiction = None  # TODO: bool
exercise_7_recipe_resolves_contradiction = None  # TODO: bool
exercise_7_recipe_still_within_budget = None  # TODO: bool

# ===========================================================================
# Exercise 8 (production-gear) -- escalation decision. For each assembly-
# review outcome, decide the correct next action from RESOLUTION_OPTIONS.
# ===========================================================================
RESOLUTION_OPTIONS = {"ship_as_is", "resolve_or_escalate"}

EXERCISE_8_SCENARIOS = {
    "all_contradictions_resolved_by_authority_ranking": (
        "Every contradiction Step 3 found was cleanly resolved by Step "
        "2's pre-assigned authority ranking, with no ties."
    ),
    "one_contradiction_no_clear_authority_winner_tie": (
        "One contradiction was found where both sources share the same "
        "authority rank, and the ranking gives no clear winner."
    ),
    "new_source_type_added_no_authority_rank_assigned_yet": (
        "A new source type was added to the pipeline, but Step 2's "
        "authority ranking was never updated to include it."
    ),
}

# TODO: an action from RESOLUTION_OPTIONS for each scenario.
exercise_8_answers = {
    "all_contradictions_resolved_by_authority_ranking": None,  # TODO
    "one_contradiction_no_clear_authority_winner_tie": None,  # TODO
    "new_source_type_added_no_authority_rank_assigned_yet": None,  # TODO
}


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def _highest_authority_instance(instances):
    return max(instances, key=lambda pair: AUTHORITY_RANK[pair[0]])


def score_exercise_1():
    key = {
        "sources_joined_in_arrival_order_no_overlap_or_conflict_check": "naive_concatenation",
        "exact_duplicate_text_stripped_but_reworded_conflicts_untouched": "string_dedup_only",
        "sources_inventoried_ranked_conflicts_resolved_deduped_then_ordered": "source_assembly_recipe",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_inventory_sources",
        "step_rank_authority",
        "step_detect_conflicts",
        "step_resolve_or_surface",
        "step_deduplicate",
        "step_handoff_to_ordering",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    correct = 0
    for key, conflict in EXERCISE_3_CONFLICTS.items():
        x, y = conflict["source_x"], conflict["source_y"]
        expected = x if AUTHORITY_RANK[x] > AUTHORITY_RANK[y] else y
        correct += int(exercise_3_answers.get(key) == expected)
    return correct, len(EXERCISE_3_CONFLICTS)


def score_exercise_4():
    correct = sum(
        1 for k, v in EXERCISE_4_CLAIM_PAIRS.items() if exercise_4_answers.get(k) == v
    )
    return correct, len(EXERCISE_4_CLAIM_PAIRS)


def score_exercise_5():
    correct = 0
    total = 0
    for claim_id, instances in CLAIM_SOURCE_INSTANCES.items():
        expected_kept = _highest_authority_instance(instances)[0]
        expected_saved = sum(t for _, t in instances) - _highest_authority_instance(instances)[1]
        correct += int(exercise_5_kept_sources.get(claim_id) == expected_kept)
        correct += int(exercise_5_tokens_saved.get(claim_id) == expected_saved)
        total += 2
    return correct, total


def score_exercise_6():
    expected_freed = sum(
        sum(t for _, t in instances) - _highest_authority_instance(instances)[1]
        for instances in CLAIM_SOURCE_INSTANCES.values()
    )
    expected_resolved = NAIVE_ASSEMBLY_TOTAL_TOKENS - expected_freed
    expected_within = expected_resolved <= SCRIPTLINE_BUDGET_TOKENS
    correct = 0
    correct += int(exercise_6_tokens_freed == expected_freed)
    correct += int(exercise_6_resolved_total == expected_resolved)
    correct += int(exercise_6_within_budget == expected_within)
    return correct, 3


def score_exercise_7():
    correct = 0
    correct += int(exercise_7_naive_contains_contradiction is True)
    correct += int(exercise_7_recipe_resolves_contradiction is True)
    correct += int(exercise_7_recipe_still_within_budget is True)
    return correct, 3


def score_exercise_8():
    key = {
        "all_contradictions_resolved_by_authority_ranking": "ship_as_is",
        "one_contradiction_no_clear_authority_winner_tie": "resolve_or_escalate",
        "new_source_type_added_no_authority_rank_assigned_yet": "resolve_or_escalate",
    }
    correct = sum(1 for k, v in key.items() if exercise_8_answers.get(k) == v)
    return correct, len(key)


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to assembly approaches", score_exercise_1),
        ("Exercise 2 -- order the Source Assembly Recipe", score_exercise_2),
        ("Exercise 3 -- authority-rank conflict resolution", score_exercise_3),
        ("Exercise 4 -- contradiction detection", score_exercise_4),
        ("Exercise 5 -- deduplication arithmetic", score_exercise_5),
        ("Exercise 6 -- budget check after resolution", score_exercise_6),
        ("Exercise 7 -- naive-vs-recipe regression gate", score_exercise_7),
        ("Exercise 8 -- escalation decision", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 7 Exercises -- Score Report")
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
