"""
Chapter 7 Exercises: Multi-Source Context Assembly -- REFERENCE SOLUTION

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

This file fills in every TODO with a correct reference answer and scores
a perfect total when run:

    python3 solution.py
"""

# ===========================================================================
# Exercise 1 -- match each scenario to the right assembly approach.
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

exercise_1_answers = {
    "sources_joined_in_arrival_order_no_overlap_or_conflict_check": "naive_concatenation",
    "exact_duplicate_text_stripped_but_reworded_conflicts_untouched": "string_dedup_only",
    "sources_inventoried_ranked_conflicts_resolved_deduped_then_ordered": "source_assembly_recipe",
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

exercise_2_order = [
    "step_inventory_sources",
    "step_rank_authority",
    "step_detect_conflicts",
    "step_resolve_or_surface",
    "step_deduplicate",
    "step_handoff_to_ordering",
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

exercise_3_answers = {
    "conflict_a": "live_tool_output",
    "conflict_b": "conversation_history_this_session",
    "conflict_c": "system_instructions",
}

# ===========================================================================
# Exercise 4 (production-gear) -- contradiction detection. True = the two
# claims genuinely contradict each other about the same fact; False = the
# claims are a restatement of the same fact, or are about different facts
# entirely.
# ===========================================================================
EXERCISE_4_CLAIM_PAIRS = {
    "prescription_count_conflict": True,
    "warfarin_dose_restatement": False,
    "clinic_hours_vs_pharmacy_hours": False,
    "allergy_status_conflict": True,
    "insurance_provider_restatement": False,
    "refill_quantity_conflict": True,
}

exercise_4_answers = dict(EXERCISE_4_CLAIM_PAIRS)

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


def _highest_authority_instance(instances):
    return max(instances, key=lambda pair: AUTHORITY_RANK[pair[0]])


exercise_5_kept_sources = {
    claim_id: _highest_authority_instance(instances)[0]
    for claim_id, instances in CLAIM_SOURCE_INSTANCES.items()
}
exercise_5_tokens_saved = {
    claim_id: sum(tokens for _, tokens in instances) - _highest_authority_instance(instances)[1]
    for claim_id, instances in CLAIM_SOURCE_INSTANCES.items()
}

# ===========================================================================
# Exercise 6 (production-gear) -- budget check after resolution.
# ===========================================================================
SCRIPTLINE_BUDGET_TOKENS = 900
NAIVE_ASSEMBLY_TOTAL_TOKENS = 1_040

exercise_6_tokens_freed = sum(exercise_5_tokens_saved.values())
exercise_6_resolved_total = NAIVE_ASSEMBLY_TOTAL_TOKENS - exercise_6_tokens_freed
exercise_6_within_budget = exercise_6_resolved_total <= SCRIPTLINE_BUDGET_TOKENS

# ===========================================================================
# Exercise 7 (production-gear) -- naive-vs-recipe regression gate. A
# load-bearing contradiction (the allergy-status conflict) exists in the
# raw assembled sources. Does naive concatenation still contain it
# unresolved? Does the Source Assembly Recipe resolve it? Does the
# resolved result still fit the budget?
# ===========================================================================
exercise_7_naive_contains_contradiction = True
exercise_7_recipe_resolves_contradiction = True
exercise_7_recipe_still_within_budget = True

# ===========================================================================
# Exercise 8 (production-gear) -- escalation decision. For each assembly-
# review outcome, decide the correct next action.
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

exercise_8_answers = {
    "all_contradictions_resolved_by_authority_ranking": "ship_as_is",
    "one_contradiction_no_clear_authority_winner_tie": "resolve_or_escalate",
    "new_source_type_added_no_authority_rank_assigned_yet": "resolve_or_escalate",
}


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

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
    print("Chapter 7 Exercises -- Score Report (REFERENCE SOLUTION)")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    print(
        f"Tokens freed by resolution: {exercise_6_tokens_freed} "
        f"| resolved total: {exercise_6_resolved_total} "
        f"| within {SCRIPTLINE_BUDGET_TOKENS}-token budget: {exercise_6_within_budget}"
    )


if __name__ == "__main__":
    main()
