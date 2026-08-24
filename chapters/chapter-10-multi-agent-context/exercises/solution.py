"""
Chapter 10 Exercises: Context Engineering for Multi-Agent Systems -- REFERENCE SOLUTION

Scenario: Prescott County Emergency Housing Placement Network, a
fictional county emergency-housing agency. Its placement pipeline,
PlacementLine, is a three-step pipeline (Intake Agent, Eligibility Agent,
Match Agent) run by a single orchestrator across a long shift, processing
many households back to back in one session. Chapters 1-9's own recipes
have already run for each step: a correct budget, correct memory
handling, nothing over budget needing compression, no positional risk,
no multi-source contradiction, and (once a step calls a tool) correct
tool-result curation. Your job is this chapter's own new skill: scoping
each step's own context contract, budgeting each step as its own ledger
line, isolating context per household (this pipeline's own unit of
work), and deciding what a sub-agent actually needs from the
orchestrator.

This file fills in every TODO with a correct reference answer and scores
a perfect total when run:

    python3 solution.py
"""

# ===========================================================================
# Exercise 1 -- match each scenario to the right pipeline-context approach.
# ===========================================================================
APPROACHES = {"unscoped_session_history", "scoped_no_unit_isolation", "pipeline_context_recipe"}

EXERCISE_1_SCENARIOS = {
    "every_step_gets_full_shift_history_char_cutoff": (
        "Every step receives the orchestrator's full accumulated history "
        "across every household processed this shift, on every call, "
        "truncated by raw character count wherever the step's own budget "
        "runs out."
    ),
    "steps_scoped_to_current_household_but_no_reset_between_households": (
        "Each step correctly receives only the current household's own "
        "data and the specific prior-step outputs its own contract calls "
        "for, but the orchestrator never resets working context between "
        "one household's placement and the next."
    ),
    "scoped_budgeted_isolated_delegated_handoff": (
        "Each step's own context contract is scoped, each step is "
        "budgeted as its own ledger line, prior steps' outputs are "
        "curated before hand-off, context is isolated at each household "
        "boundary, and each sub-agent receives only its own delegated "
        "sub-task."
    ),
}

exercise_1_answers = {
    "every_step_gets_full_shift_history_char_cutoff": "unscoped_session_history",
    "steps_scoped_to_current_household_but_no_reset_between_households": "scoped_no_unit_isolation",
    "scoped_budgeted_isolated_delegated_handoff": "pipeline_context_recipe",
}

# ===========================================================================
# Exercise 2 -- order the Pipeline/Multi-Agent Context Recipe's six steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_scope_contract": "Define each step's own scoped context contract -- decide exactly which upstream facts and prior-step outputs it needs.",
    "step_curate_handoff": "Pass prior steps' outputs as curated, typed results, never raw reasoning transcripts.",
    "step_budget_ledger_line": "Budget each step's context as its own explicit ledger line item, not one shared pipeline-wide pool.",
    "step_isolate_unit_of_work": "Isolate context per unit of work -- reset or evict the prior unit's working context at each new unit's boundary.",
    "step_delegate_subtask": "Give a sub-agent only its own delegated sub-task, not the orchestrator's full session history.",
    "step_handoff_downstream": "Hand the pipeline's resolved final output downstream as one well-formed record.",
}

exercise_2_order = [
    "step_scope_contract",
    "step_curate_handoff",
    "step_budget_ledger_line",
    "step_isolate_unit_of_work",
    "step_delegate_subtask",
    "step_handoff_downstream",
]

# ===========================================================================
# Exercise 3 (production-gear) -- per-step context budget vs an unscoped,
# ever-growing shift history. PlacementLine has processed 8 households
# already this shift, each leaving ~140 tokens of raw sub-agent output in
# the orchestrator's own accumulated history. The Match Agent's own
# curated inputs for the current household (household 9) total 95 tokens.
# ===========================================================================
PRIOR_HOUSEHOLDS_PROCESSED = 8
RAW_OUTPUT_TOKENS_PER_PRIOR_HOUSEHOLD = 140
HOUSEHOLD_9_CURATED_TOKENS = 95
MATCH_AGENT_BUDGET_TOKENS = 250

exercise_3_naive_tokens = PRIOR_HOUSEHOLDS_PROCESSED * RAW_OUTPUT_TOKENS_PER_PRIOR_HOUSEHOLD + HOUSEHOLD_9_CURATED_TOKENS
exercise_3_scoped_tokens = HOUSEHOLD_9_CURATED_TOKENS
exercise_3_naive_overflows = exercise_3_naive_tokens > MATCH_AGENT_BUDGET_TOKENS
exercise_3_scoped_fits = exercise_3_scoped_tokens <= MATCH_AGENT_BUDGET_TOKENS

# ===========================================================================
# Exercise 4 (production-gear) -- curating a prior step's own output
# before hand-off. The Eligibility Agent's own raw reasoning output has 6
# fields; the Match Agent's own contract only needs 3 of them.
# ===========================================================================
ELIGIBILITY_AGENT_RAW_OUTPUT = {
    "household_id": ("HH-2291", 8),
    "eligible": (True, 4),
    "reasoning_trace": ("Checked income threshold, checked residency, checked prior placements...", 40),
    "priority_tier": ("Tier 2", 6),
    "caseworker_notes": ("Household mentioned preferring ground-floor units", 15),
    "household_size": (3, 4),
}

exercise_4_curated_fields = {"household_id", "eligible", "priority_tier"}

# ===========================================================================
# Exercise 5 (production-gear) -- unit-of-work isolation. Across a working
# context that was never reset, decide which items belong to the CURRENT
# household (HH-2299) and should survive, and which belong to a prior
# household and should be evicted.
# ===========================================================================
WORKING_CONTEXT_ITEMS = {
    "item_1": {"household_id": "HH-2291", "field": "eligible", "value": True},
    "item_2": {"household_id": "HH-2299", "field": "eligible", "value": True},
    "item_3": {"household_id": "HH-2295", "field": "priority_tier", "value": "Tier 1"},
    "item_4": {"household_id": "HH-2299", "field": "priority_tier", "value": "Tier 3"},
}
CURRENT_HOUSEHOLD_ID = "HH-2299"


def _survives_isolation(item, current_id):
    return item["household_id"] == current_id


exercise_5_survives = {k: _survives_isolation(v, CURRENT_HOUSEHOLD_ID) for k, v in WORKING_CONTEXT_ITEMS.items()}

# ===========================================================================
# Exercise 6 (production-gear) -- sub-agent delegation scope. Decide, for
# each candidate payload handed to the Match Agent, whether it is scoped
# correctly (current household's own curated data plus its own delegated
# task) or incorrectly (includes the orchestrator's full session or
# another household's data).
# ===========================================================================
MATCH_AGENT_PAYLOAD_CANDIDATES = {
    "payload_a": {"task": "match_to_available_unit", "household_data": {"id": "HH-2299", "size": 3}, "other_households_included": False},
    "payload_b": {"task": "match_to_available_unit", "household_data": {"id": "HH-2299", "size": 3}, "other_households_included": True},
    "payload_c": {"task": None, "household_data": {"id": "HH-2299", "size": 3}, "other_households_included": False},
}


def _is_correctly_scoped(payload):
    return payload["task"] is not None and payload["other_households_included"] is False


exercise_6_answers = {k: _is_correctly_scoped(v) for k, v in MATCH_AGENT_PAYLOAD_CANDIDATES.items()}

# ===========================================================================
# Exercise 7 (production-gear) -- pipeline-wide ledger, one line per step,
# vs a single shared budget. Three steps, each with its own budget;
# confirm each step's own scoped tokens fit its own line, and compute the
# pipeline-wide total.
# ===========================================================================
STEP_BUDGETS = {"intake_agent": 200, "eligibility_agent": 250, "match_agent": 250}
STEP_SCOPED_TOKENS = {"intake_agent": 60, "eligibility_agent": 75, "match_agent": 95}

exercise_7_fits_per_step = {s: STEP_SCOPED_TOKENS[s] <= STEP_BUDGETS[s] for s in STEP_BUDGETS}
exercise_7_pipeline_total_scoped_tokens = sum(STEP_SCOPED_TOKENS.values())
exercise_7_pipeline_total_budget = sum(STEP_BUDGETS.values())

# ===========================================================================
# Exercise 8 (production-gear) -- downstream handoff typing. A pipeline's
# final resolved output is ready to hand downstream only if it is typed,
# curated, and scoped to exactly one household (not a mixed multi-household
# record).
# ===========================================================================
EXERCISE_8_CANDIDATES = {
    "record_a": {"type": "placement_recommendation", "curated": True, "household_count": 1},
    "record_b": {"type": "placement_recommendation", "curated": False, "household_count": 1},
    "record_c": {"type": None, "curated": True, "household_count": 1},
    "record_d": {"type": "placement_recommendation", "curated": True, "household_count": 2},
}


def _is_ready_for_downstream_handoff(record):
    return record["type"] == "placement_recommendation" and record["curated"] is True and record["household_count"] == 1


exercise_8_answers = {k: _is_ready_for_downstream_handoff(v) for k, v in EXERCISE_8_CANDIDATES.items()}


# ===========================================================================
# Scoring harness -- identical to starter.py, included so this file is
# runnable standalone.
# ===========================================================================

def score_exercise_1():
    key = {
        "every_step_gets_full_shift_history_char_cutoff": "unscoped_session_history",
        "steps_scoped_to_current_household_but_no_reset_between_households": "scoped_no_unit_isolation",
        "scoped_budgeted_isolated_delegated_handoff": "pipeline_context_recipe",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_scope_contract", "step_curate_handoff", "step_budget_ledger_line",
        "step_isolate_unit_of_work", "step_delegate_subtask", "step_handoff_downstream",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    expected_naive = PRIOR_HOUSEHOLDS_PROCESSED * RAW_OUTPUT_TOKENS_PER_PRIOR_HOUSEHOLD + HOUSEHOLD_9_CURATED_TOKENS
    expected_scoped = HOUSEHOLD_9_CURATED_TOKENS
    correct = 0
    correct += int(exercise_3_naive_tokens == expected_naive)
    correct += int(exercise_3_scoped_tokens == expected_scoped)
    correct += int(exercise_3_naive_overflows == (expected_naive > MATCH_AGENT_BUDGET_TOKENS))
    correct += int(exercise_3_scoped_fits == (expected_scoped <= MATCH_AGENT_BUDGET_TOKENS))
    return correct, 4


def score_exercise_4():
    expected = {"household_id", "eligible", "priority_tier"}
    correct = int(exercise_4_curated_fields == expected)
    return correct, 1


def score_exercise_5():
    correct = sum(
        1 for k, v in WORKING_CONTEXT_ITEMS.items()
        if exercise_5_survives.get(k) == _survives_isolation(v, CURRENT_HOUSEHOLD_ID)
    )
    return correct, len(WORKING_CONTEXT_ITEMS)


def score_exercise_6():
    correct = sum(
        1 for k, v in MATCH_AGENT_PAYLOAD_CANDIDATES.items()
        if exercise_6_answers.get(k) == _is_correctly_scoped(v)
    )
    return correct, len(MATCH_AGENT_PAYLOAD_CANDIDATES)


def score_exercise_7():
    expected_fits = {s: STEP_SCOPED_TOKENS[s] <= STEP_BUDGETS[s] for s in STEP_BUDGETS}
    correct = 0
    correct += sum(1 for s in STEP_BUDGETS if exercise_7_fits_per_step.get(s) == expected_fits[s])
    correct += int(exercise_7_pipeline_total_scoped_tokens == sum(STEP_SCOPED_TOKENS.values()))
    correct += int(exercise_7_pipeline_total_budget == sum(STEP_BUDGETS.values()))
    return correct, len(STEP_BUDGETS) + 2


def score_exercise_8():
    correct = sum(
        1 for k, v in EXERCISE_8_CANDIDATES.items()
        if exercise_8_answers.get(k) == _is_ready_for_downstream_handoff(v)
    )
    return correct, len(EXERCISE_8_CANDIDATES)


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to pipeline-context approaches", score_exercise_1),
        ("Exercise 2 -- order the Pipeline/Multi-Agent Context Recipe", score_exercise_2),
        ("Exercise 3 -- per-step budget vs unscoped shift history", score_exercise_3),
        ("Exercise 4 -- curating a prior step's own output", score_exercise_4),
        ("Exercise 5 -- unit-of-work isolation", score_exercise_5),
        ("Exercise 6 -- sub-agent delegation scope", score_exercise_6),
        ("Exercise 7 -- pipeline-wide ledger, one line per step", score_exercise_7),
        ("Exercise 8 -- downstream handoff typing", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 10 Exercises -- Score Report (REFERENCE SOLUTION)")
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
