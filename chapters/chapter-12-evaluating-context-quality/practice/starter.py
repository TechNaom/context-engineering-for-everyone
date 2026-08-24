"""
Chapter 12 Practice Bank: Evaluating Context Quality

See README.md for the eight scenarios. Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report.
"""

# Scenario 1 (judgment) -- Ossbrook Regional Grain Futures Clearinghouse: a
# settlement pipeline confirms its "contract_terms" source is present in an
# assembled bundle before a Settlement Review Agent runs. Does confirming a
# SOURCE category is present, by itself, guarantee the specific required
# fact within it (this contract's own current margin-call threshold) is
# actually present?
scenario_1_answer = None  # TODO: "yes" or "no"

# Scenario 2 (production-gear) -- Colton Regional Home Inspection Licensing
# Board: an Appeals Review case requires 5 specific facts. Compute the
# completeness score (found / total) as a float.
COLTON_REQUIRED_FACTS = {
    "current_inspection_status": {"found": True},
    "prior_variance_granted": {"found": True},
    "code_version_applied": {"found": False},
    "applicant_license_number": {"found": True},
    "appeal_deadline_date": {"found": True},
}

# TODO: compute this by hand.
scenario_2_completeness = 0.0  # TODO

# Scenario 3 (judgment) -- Bramfield Regional Wildfire Evacuation
# Coordination Center: an evacuation-routing bundle fits comfortably inside
# its own token budget with room to spare. Does fitting a token budget, by
# itself, guarantee the bundle's own noise ratio is acceptable?
scenario_3_answer = None  # TODO: "yes" or "no"

# Scenario 4 (production-gear) -- Grendale Regional Court Interpreter
# Certification Board: 180 of a 1200-token bundle are carried over from an
# unrelated interpreter's own file by a stale join. Compute the noise ratio,
# and whether it exceeds a 10% threshold.
GRENDALE_NOISE_TOKENS = 180
GRENDALE_TOTAL_TOKENS = 1200
GRENDALE_THRESHOLD = 0.10

# TODO: compute these two values by hand.
scenario_4_noise_ratio = 0.0  # TODO
scenario_4_exceeds_threshold = None  # TODO

# Scenario 5 (judgment) -- Delmoore Regional Pension Fund Audit Office: an
# Audit Review Agent's own context bundle passes Chapter 11's own
# contamination and starvation probes cleanly (no prior reviewer's own
# opinion leaked in, no required shared fact missing from an isolation
# hand-off). Does passing BOTH of Chapter 11's own probes, by itself,
# guarantee this chapter's own completeness, noise, and positional checks
# also pass?
scenario_5_answer = None  # TODO: "yes" or "no"

# Scenario 6 (production-gear) -- Sennwick Regional Livestock Export Health
# Certification Bureau: a 1800-token bundle. Front bucket ends at 270 (15%),
# back bucket starts at 1530 (last 15%). Bucket each fact's own position.
SENNWICK_FRONT_END = 270
SENNWICK_BACK_START = 1530
SENNWICK_POSITIONS = {
    "current_health_certificate": 900,     # middle
    "export_destination_country": 100,     # front
    "quarantine_status_flag": 1650,        # back
}


def _bucket(position, front_end=SENNWICK_FRONT_END, back_start=SENNWICK_BACK_START):
    if position < front_end:
        return "front"
    if position > back_start:
        return "back"
    return "middle"


# TODO: bucket name for each fact.
scenario_6_answers = {
    "current_health_certificate": None,  # TODO
    "export_destination_country": None,  # TODO
    "quarantine_status_flag": None,  # TODO
}

# Scenario 7 (production-gear) -- Bexmoor Regional Building Code Variance
# Board: evaluate three candidate bundles against the combined context
# quality gate (completeness == 1.0, noise_ratio <= 0.10, no CRITICAL fact
# in the "middle" bucket).
BEXMOOR_CANDIDATES = {
    "bundle_alpha": {"completeness": 1.0, "noise_ratio": 0.08, "critical_fact_bucket": "back"},
    "bundle_beta": {"completeness": 1.0, "noise_ratio": 0.15, "critical_fact_bucket": "front"},
    "bundle_gamma": {"completeness": 0.6, "noise_ratio": 0.02, "critical_fact_bucket": "front"},
}


def _gate_passes(candidate, threshold=0.10):
    return (
        candidate["completeness"] == 1.0
        and candidate["noise_ratio"] <= threshold
        and candidate["critical_fact_bucket"] != "middle"
    )


# TODO: True/False for each -- does this bundle pass the gate?
scenario_7_answers = {
    "bundle_alpha": None,  # TODO
    "bundle_beta": None,  # TODO
    "bundle_gamma": None,  # TODO
}

# Scenario 8 (judgment) -- Warrenfield Regional Small Business Disaster Loan
# Review Panel: a bundle has completeness == 1.0 and noise_ratio == 0.0, but
# its single CRITICAL required fact (current_revenue_loss_percentage) is
# bucketed "middle". Does this bundle pass the combined context quality
# gate?
scenario_8_answer = None  # TODO: "yes" or "no"


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Ossbrook Regional Grain Futures Clearinghouse, judgment)",
                     isinstance(scenario_1_answer, str) and scenario_1_answer.strip().lower() == "no", 1))

    expected_2 = sum(1 for f in COLTON_REQUIRED_FACTS.values() if f["found"]) / len(COLTON_REQUIRED_FACTS)
    results.append(("Scenario 2 (Colton Regional Home Inspection Licensing Board)",
                     abs(scenario_2_completeness - expected_2) < 1e-9, 1))

    results.append(("Scenario 3 (Bramfield Regional Wildfire Evacuation Coordination Center, judgment)",
                     isinstance(scenario_3_answer, str) and scenario_3_answer.strip().lower() == "no", 1))

    expected_4_ratio = GRENDALE_NOISE_TOKENS / GRENDALE_TOTAL_TOKENS
    results.append((
        "Scenario 4 (Grendale Regional Court Interpreter Certification Board)",
        abs(scenario_4_noise_ratio - expected_4_ratio) < 1e-9
        and scenario_4_exceeds_threshold == (expected_4_ratio > GRENDALE_THRESHOLD),
        1,
    ))

    results.append(("Scenario 5 (Delmoore Regional Pension Fund Audit Office, judgment)",
                     isinstance(scenario_5_answer, str) and scenario_5_answer.strip().lower() == "no", 1))

    expected_6 = {k: _bucket(v) for k, v in SENNWICK_POSITIONS.items()}
    correct_6 = sum(1 for k, v in expected_6.items() if scenario_6_answers.get(k) == v)
    results.append(("Scenario 6 (Sennwick Regional Livestock Export Health Certification Bureau)",
                     correct_6 == len(expected_6), 1))

    correct_7 = sum(1 for k, v in BEXMOOR_CANDIDATES.items() if scenario_7_answers.get(k) == _gate_passes(v))
    results.append(("Scenario 7 (Bexmoor Regional Building Code Variance Board)",
                     correct_7 == len(BEXMOOR_CANDIDATES), 1))

    results.append(("Scenario 8 (Warrenfield Regional Small Business Disaster Loan Review Panel, judgment)",
                     isinstance(scenario_8_answer, str) and scenario_8_answer.strip().lower() == "no", 1))

    return results


def main():
    print("Chapter 12 Practice Bank -- Score Report")
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
