"""
Chapter 4 Practice Bank: Long-Term and Persistent Memory Systems -- REFERENCE SOLUTION

See README.md for the eight scenarios. This file fills in every TODO
with a correct reference answer and scores a perfect total when run:

    python3 solution.py
"""

# Scenario 1 (judgment) -- Underholt Family Medicine Network: a team's
# Line 4 (Recalled Long-Term Memory) budget was correctly allocated, but
# a patient's care team still sees contradictory facts (an old allergy
# note next to its correction) show up in the same visit. A teammate
# proposes: "let's just raise Line 4's token budget." Does that fix it
# by itself?
scenario_1_answer = "no"

# Scenario 2 (production-gear) -- Presswick Disability Services
# Cooperative: Line 4's budget is 1,200 tokens. Reserve 250 tokens for
# always-retrieved core facts. Average additional retrieved fact is 50
# tokens.
PRESSWICK_LINE4_BUDGET = 1_200
PRESSWICK_CORE_RESERVE = 250
PRESSWICK_AVG_FACT_TOKENS = 50
scenario_2_answer = (PRESSWICK_LINE4_BUDGET - PRESSWICK_CORE_RESERVE) // PRESSWICK_AVG_FACT_TOKENS

# Scenario 3 (judgment) -- Dunmere Memory Care Residences: a team decides
# to write every fact ever disclosed to the persistent store, reasoning
# that "we might need it someday." Is an unbounded write-criteria list a
# sound design?
scenario_3_answer = "no"

# Scenario 4 (production-gear) -- Oxbridge Pediatric Home Care: an
# uncurated store's raw cumulative totals per visit are given below.
# Which visit (1-indexed) first exceeds the 2,000-token Line 4 budget?
OXBRIDGE_LINE4_BUDGET = 2_000
OXBRIDGE_CUMULATIVE = [220, 410, 640, 900, 1_150, 1_430, 1_720, 2_040, 2_300]
scenario_4_answer = next(
    i + 1 for i, total in enumerate(OXBRIDGE_CUMULATIVE) if total > OXBRIDGE_LINE4_BUDGET
)

# Scenario 5 (judgment) -- Wetherby Insurance Trust: a stored fact about
# a client's policy coverage tier is written once and never given an
# expiration, version, or update mechanism, even though coverage tiers
# genuinely change over time. Is that sound design?
scenario_5_answer = "no"

# Scenario 6 (production-gear) -- Camberwell Independent Pharmacy Group:
# a client discloses a documented drug interaction warning relevant to
# every future prescription review. Should this fact be written to the
# persistent store?
scenario_6_answer = True

# Scenario 7 (production-gear) -- Penrose Estate Planning Partners: core
# facts = 180 tokens, scoped facts = 640 tokens, Line 4 budget = 900
# tokens. Does the retrieved package "fit" inside budget, or is it a
# "deficit"?
PENROSE_CORE_TOKENS = 180
PENROSE_SCOPED_TOKENS = 640
PENROSE_LINE4_BUDGET = 900
_penrose_total = PENROSE_CORE_TOKENS + PENROSE_SCOPED_TOKENS
scenario_7_answer = "fits" if _penrose_total <= PENROSE_LINE4_BUDGET else "deficit"

# Scenario 8 (judgment) -- Rushbrook K-12 Special Education Cooperative:
# a team adds real staleness handling (superseded/expired status
# tracking) to a request type that previously had none. Does that alone
# remove the need to still validate the resulting retrieval against the
# worst realistic case (the longest student relationship, the most
# updates)?
scenario_8_answer = "no"


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Underholt Family Medicine Network, judgment)", scenario_1_answer.strip().lower() == "no", 1))

    expected_2 = (PRESSWICK_LINE4_BUDGET - PRESSWICK_CORE_RESERVE) // PRESSWICK_AVG_FACT_TOKENS
    results.append(("Scenario 2 (Presswick Disability Services Cooperative)", scenario_2_answer == expected_2, 1))

    results.append(("Scenario 3 (Dunmere Memory Care Residences, judgment)", scenario_3_answer.strip().lower() == "no", 1))

    expected_4 = next(i + 1 for i, total in enumerate(OXBRIDGE_CUMULATIVE) if total > OXBRIDGE_LINE4_BUDGET)
    results.append(("Scenario 4 (Oxbridge Pediatric Home Care)", scenario_4_answer == expected_4, 1))

    results.append(("Scenario 5 (Wetherby Insurance Trust, judgment)", scenario_5_answer.strip().lower() == "no", 1))

    results.append(("Scenario 6 (Camberwell Independent Pharmacy Group)", scenario_6_answer is True, 1))

    expected_7 = "fits" if _penrose_total <= PENROSE_LINE4_BUDGET else "deficit"
    results.append(("Scenario 7 (Penrose Estate Planning Partners)", scenario_7_answer.strip().lower() == expected_7, 1))

    results.append(("Scenario 8 (Rushbrook K-12 Special Education Cooperative, judgment)", scenario_8_answer.strip().lower() == "no", 1))

    return results


def main():
    print("Chapter 4 Practice Bank -- Score Report (reference solution)")
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
