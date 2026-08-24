"""
Chapter 11 Practice Bank: Context Isolation and Scoping

See README.md for the eight scenarios. Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report.
"""

# Scenario 1 (judgment) -- Brightfen Regional Utility Outage Response
# Cooperative: a dispatch pipeline deliberately isolates its Root-Cause
# Review Agent from the original Dispatch Agent's own outage
# classification, to get a genuinely independent second read. Does that
# isolation, by itself, guarantee the Root-Cause Review Agent still
# receives the shared, current outage-classification rubric it needs?
scenario_1_answer = None  # TODO: "yes" or "no"

# Scenario 2 (production-gear) -- Norwick Regional Medical Second-Opinion
# Network: a Second-Opinion Agent's own budget is 250 tokens: 150 tokens
# of case facts plus either the First Opinion Agent's own 130-token raw
# reasoning (no isolation) or a 40-token shared clinical-guideline
# hand-off (the recipe). Compute the naive (no-isolation) total and
# whether it overflows, and the scoped (recipe) total and whether it
# fits.
NORWICK_CASE_FACTS_TOKENS = 150
NORWICK_PRIOR_OPINION_RAW_TOKENS = 130
NORWICK_SHARED_GUIDELINE_TOKENS = 40
NORWICK_BUDGET = 250

# TODO: compute these four values by hand.
scenario_2_naive_tokens = 0  # TODO
scenario_2_naive_overflows = None  # TODO
scenario_2_scoped_tokens = 0  # TODO
scenario_2_scoped_fits = None  # TODO

# Scenario 3 (judgment) -- Marrenfield Regional Crop Insurance Claims
# Bureau: isolating the Adjuster Review Agent from the initial Claims
# Agent's own damage estimate is the right call to prevent anchoring. Is
# it sufficient to implement that by deleting the initial agent's ENTIRE
# output from context, if the shared, current per-acre payout schedule
# also gets deleted along with it?
scenario_3_answer = None  # TODO: "yes" or "no"

# Scenario 4 (production-gear) -- Coalport Regional Ferry Safety
# Inspection Authority: curate a vessel Inspector's own 5-field raw
# output down to the fields safe to hand off to an independent
# Re-Inspection Agent. Fields: vessel_id, inspector_findings_narrative,
# pass_fail_recommendation, safety_code_version_applied, inspection_date.
# The narrative and recommendation are the inspector's own opinion; the
# rest are objective, shared facts.
COALPORT_RAW_OUTPUT = {
    "vessel_id": "CP-771",
    "inspector_findings_narrative": "Observed corrosion on port-side hull plating near waterline...",
    "pass_fail_recommendation": "fail",
    "safety_code_version_applied": "2026-rev-3",
    "inspection_date": "2026-07-14",
}
COALPORT_SAFE_TO_HANDOFF_FIELDS = {"vessel_id", "safety_code_version_applied", "inspection_date"}

# TODO: the set of field keys safe to hand off to the Re-Inspection Agent.
scenario_4_handoff_fields = set()  # TODO

# Scenario 5 (judgment) -- Sallowbrook Regional Land Trust Conservation
# Board: a grant review pipeline isolates its Appeals Panel from the
# original Review Committee's own vote tally and comments. Does that
# alone guarantee the Appeals Panel still has access to the current,
# correct acreage-eligibility formula used by both stages?
scenario_5_answer = None  # TODO: "yes" or "no"

# Scenario 6 (production-gear) -- Vantree Regional Air Quality Monitoring
# Network: classify each candidate payload handed to an isolated Review
# Agent as "compliant" (no prior reviewer opinion present, no shared
# facts missing), "contamination_fail" (opinion present), or
# "starvation_fail" (a required shared fact -- current_aqi_threshold --
# is missing).
VANTREE_PAYLOADS = {
    "payload_p": {"has_prior_reviewer_opinion": False, "missing_shared_facts": []},
    "payload_q": {"has_prior_reviewer_opinion": True, "missing_shared_facts": []},
    "payload_r": {"has_prior_reviewer_opinion": False, "missing_shared_facts": ["current_aqi_threshold"]},
}


def _classify_vantree(payload):
    if payload["has_prior_reviewer_opinion"]:
        return "contamination_fail"
    if payload["missing_shared_facts"]:
        return "starvation_fail"
    return "compliant"


# TODO: classification string for each payload.
scenario_6_answers = {
    "payload_p": None,  # TODO
    "payload_q": None,  # TODO
    "payload_r": None,  # TODO
}

# Scenario 7 (production-gear) -- Kesterly Regional Public Records
# Redaction Service: a three-step pipeline (Intake Agent, Redaction
# Review Agent [isolated from Intake's own drafting notes], Release
# Agent), each with its own ledger line. Confirm each step's own scoped
# tokens fit its own budget, and compute the pipeline-wide total scoped
# tokens and total budget.
KESTERLY_STEP_BUDGETS = {"intake_agent": 150, "redaction_review_agent": 300, "release_agent": 200}
KESTERLY_STEP_SCOPED_TOKENS = {"intake_agent": 70, "redaction_review_agent": 210, "release_agent": 130}

# TODO: fill these in by hand.
scenario_7_fits_per_step = {
    "intake_agent": None,  # TODO
    "redaction_review_agent": None,  # TODO
    "release_agent": None,  # TODO
}
scenario_7_pipeline_total_scoped = 0  # TODO
scenario_7_pipeline_total_budget = 0  # TODO

# Scenario 8 (judgment) -- Wolvercote Regional Peer Review Grant Panel:
# two independent grant reviewers are each isolated from the other's own
# score and comments, per policy, to preserve genuinely independent
# scoring. Does that isolation mean neither reviewer should receive the
# shared, objective grant-category funding cap they both need to apply
# consistently?
scenario_8_answer = None  # TODO: "yes" or "no"


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Brightfen Regional Utility Outage Response Cooperative, judgment)",
                     isinstance(scenario_1_answer, str) and scenario_1_answer.strip().lower() == "no", 1))

    expected_2_naive = NORWICK_CASE_FACTS_TOKENS + NORWICK_PRIOR_OPINION_RAW_TOKENS
    expected_2_scoped = NORWICK_CASE_FACTS_TOKENS + NORWICK_SHARED_GUIDELINE_TOKENS
    results.append((
        "Scenario 2 (Norwick Regional Medical Second-Opinion Network)",
        scenario_2_naive_tokens == expected_2_naive
        and scenario_2_naive_overflows == (expected_2_naive > NORWICK_BUDGET)
        and scenario_2_scoped_tokens == expected_2_scoped
        and scenario_2_scoped_fits == (expected_2_scoped <= NORWICK_BUDGET),
        1,
    ))

    results.append(("Scenario 3 (Marrenfield Regional Crop Insurance Claims Bureau, judgment)",
                     isinstance(scenario_3_answer, str) and scenario_3_answer.strip().lower() == "no", 1))

    results.append(("Scenario 4 (Coalport Regional Ferry Safety Inspection Authority)",
                     scenario_4_handoff_fields == COALPORT_SAFE_TO_HANDOFF_FIELDS, 1))

    results.append(("Scenario 5 (Sallowbrook Regional Land Trust Conservation Board, judgment)",
                     isinstance(scenario_5_answer, str) and scenario_5_answer.strip().lower() == "no", 1))

    correct_6 = sum(1 for k, v in VANTREE_PAYLOADS.items() if scenario_6_answers.get(k) == _classify_vantree(v))
    results.append(("Scenario 6 (Vantree Regional Air Quality Monitoring Network)", correct_6 == len(VANTREE_PAYLOADS), 1))

    expected_fits_7 = {s: KESTERLY_STEP_SCOPED_TOKENS[s] <= KESTERLY_STEP_BUDGETS[s] for s in KESTERLY_STEP_BUDGETS}
    results.append((
        "Scenario 7 (Kesterly Regional Public Records Redaction Service)",
        scenario_7_fits_per_step == expected_fits_7
        and scenario_7_pipeline_total_scoped == sum(KESTERLY_STEP_SCOPED_TOKENS.values())
        and scenario_7_pipeline_total_budget == sum(KESTERLY_STEP_BUDGETS.values()),
        1,
    ))

    results.append(("Scenario 8 (Wolvercote Regional Peer Review Grant Panel, judgment)",
                     isinstance(scenario_8_answer, str) and scenario_8_answer.strip().lower() == "no", 1))

    return results


def main():
    print("Chapter 11 Practice Bank -- Score Report")
    print("=" * 60)
    results = score()
    total_correct = 0
    total_possible = 0
    for label, correct, possible in results:
        total_correct += int(correct) * possible
        total_possible += possible
        mark = "PASS" if correct else "FAIL"
        print(f"{label}: {mark}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every scenario correctly reasoned.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
