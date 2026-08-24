"""
Chapter 13 Practice Bank: Capstone: Designing a Context Engineering
System

Four short, independent Castellan Fleet Logistics scenarios -- fresh
loads and incidents, none of them the lesson's own I-80 closure or the
exercises' own reefer warning. Each is a few sentences and one recipe
judgment or arithmetic call, covering ground the lesson and exercises
didn't: budget worst-case validation, compression fidelity, source
authority ranking, and tool-result curation.

Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report. Compare against solution.py, which scores a
perfect total.
"""

# Scenario 1 (judgment) -- Load CFL-77120, a routine grocery run with no
# incident: the Line 2 (grounding) budget fits comfortably today because
# nothing unusual is happening. Does a budget fitting comfortably on a
# routine day, by itself, prove the ledger is validated per Chapter 2's
# Step 5?
scenario_1_answer = None  # TODO: "yes" or "no"


# Scenario 2 (production-gear) -- Load CFL-63305: a compressed summary of
# five routine check-in turns is generated. Three load-bearing facts were
# identified before compression. Compute the fidelity check: did all three
# survive in the compressed text?
LOAD_BEARING = ["fuel logged at mile 210", "no HOS violation", "on-time at Elko checkpoint"]
COMPRESSED_SUMMARY = "fuel logged at mile 210; on-time at Elko checkpoint"

scenario_2_survived = None  # TODO: list of LOAD_BEARING facts found in COMPRESSED_SUMMARY
scenario_2_fidelity_ok = None  # TODO: bool -- did ALL load-bearing facts survive?


# Scenario 3 (production-gear) -- Load CFL-40218: two sources both claim a
# value for "current_driver_hos_remaining". Apply the authority ranking
# (lower number wins) to resolve the conflict.
AUTHORITY = {"eld_device_live_feed": 1, "dispatcher_manual_note": 2}
CFL_40218_CLAIMS = [
    {"source": "dispatcher_manual_note", "value": "4h 10m remaining (logged this morning)"},
    {"source": "eld_device_live_feed", "value": "3h 05m remaining (live)"},
]

scenario_3_winner = None  # TODO: the winning claim's "value" string


# Scenario 4 (production-gear) -- Load CFL-51190: a raw weather-tool result
# has 6 fields; this request type only needs 3. Curate it and compute the
# curated token count (word-count proxy).
RAW_WEATHER_RESULT = {
    "condition": "heavy snow",
    "visibility_miles": 0.25,
    "wind_gust_mph": 45,
    "station_id": "KKEMR-4471",
    "raw_radar_blob": "x" * 400,
    "forecast_72h": "..." * 100,
}
NEEDED_FIELDS = ["condition", "visibility_miles", "wind_gust_mph"]

scenario_4_curated = None  # TODO: dict with only NEEDED_FIELDS
scenario_4_curated_tokens = None  # TODO: sum of len(str(v).split()) across curated values


# ===========================================================================
# Scoring -- do not edit below this line
# ===========================================================================

def score_scenario_1():
    return int(scenario_1_answer == "no"), 1


def score_scenario_2():
    expected_survived = [f for f in LOAD_BEARING if f in COMPRESSED_SUMMARY]
    expected_ok = len(expected_survived) == len(LOAD_BEARING)
    correct = 0
    correct += int(scenario_2_survived == expected_survived)
    correct += int(scenario_2_fidelity_ok == expected_ok)
    return correct, 2


def score_scenario_3():
    expected = min(CFL_40218_CLAIMS, key=lambda c: AUTHORITY[c["source"]])["value"]
    return int(scenario_3_winner == expected), 1


def score_scenario_4():
    expected_curated = {k: RAW_WEATHER_RESULT[k] for k in NEEDED_FIELDS}
    expected_tokens = sum(len(str(v).split()) for v in expected_curated.values())
    correct = 0
    correct += int(scenario_4_curated == expected_curated)
    correct += int(scenario_4_curated_tokens == expected_tokens)
    return correct, 2


def main():
    scenarios = [
        ("Scenario 1 -- budget validation judgment", score_scenario_1),
        ("Scenario 2 -- compression fidelity check", score_scenario_2),
        ("Scenario 3 -- source authority resolution", score_scenario_3),
        ("Scenario 4 -- tool-result curation", score_scenario_4),
    ]
    total_correct = 0
    total_possible = 0
    print("Chapter 13 Practice Bank -- Score Report")
    print("=" * 60)
    for label, fn in scenarios:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")


if __name__ == "__main__":
    main()
