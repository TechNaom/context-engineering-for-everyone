"""
Chapter 8 Practice Bank: Retrieval Integration -- REFERENCE SOLUTION

See README.md for the eight scenarios. This file fills in every TODO
with a correct reference answer and scores a perfect total when run:

    python3 solution.py
"""

# Scenario 1 (judgment) -- Harborlight Maritime Archive Society: a
# retrieval pipeline always takes the top 5 ranked chunks regardless of
# their score, then appends them all. Does taking a fixed top-k
# guarantee every included chunk is actually relevant?
scenario_1_answer = "no"

# Scenario 2 (production-gear) -- Aspenfield Community College Library:
# given four scored chunks and a relevance floor of 0.55, which survive?
ASPENFIELD_FLOOR = 0.55
ASPENFIELD_CHUNKS = {
    "chunk_catalog_policy": 0.79,
    "chunk_circulation_rule": 0.61,
    "chunk_unrelated_budget_memo": 0.38,
    "chunk_unrelated_staffing_note": 0.22,
}
scenario_2_survivors = {
    key for key, score in ASPENFIELD_CHUNKS.items() if score >= ASPENFIELD_FLOOR
}

# Scenario 3 (judgment) -- Beacon Crest Genealogy Society: a pipeline
# drops every chunk below a relevance floor, but still truncates the
# surviving chunks by raw character count wherever the token budget
# happens to run out. Does relevance-floor filtering alone guarantee no
# chunk gets cut off mid-sentence?
scenario_3_answer = "no"

# Scenario 4 (production-gear) -- Slatebrook Patent Research Group:
# select surviving chunks in descending score order, stopping BEFORE any
# chunk that would push the running total over the 300-token budget.
SLATEBROOK_BUDGET_TOKENS = 300
SLATEBROOK_SURVIVORS = {
    "chunk_prior_art_reference": (0.90, 170),
    "chunk_claim_construction_note": (0.77, 110),
    "chunk_related_filing_summary": (0.60, 90),
}


def _boundary_safe_fit(chunks, budget):
    ordered = sorted(chunks.items(), key=lambda kv: kv[1][0], reverse=True)
    kept = []
    total = 0
    for key, (score, tokens) in ordered:
        if total + tokens <= budget:
            kept.append(key)
            total += tokens
    return kept, total


scenario_4_kept_chunks, scenario_4_total_tokens = _boundary_safe_fit(
    SLATEBROOK_SURVIVORS, SLATEBROOK_BUDGET_TOKENS
)

# Scenario 5 (judgment) -- Timberline Structural Engineering Archive:
# two surviving chunks are both individually accurate, correctly scored,
# and correctly included -- but they are the same load-bearing
# paragraph of the same inspection report, split at a mechanical chunk
# boundary and left as two separate, un-stitched blocks. Does individual
# per-chunk accuracy guarantee the reader experiences them as one
# coherent passage?
scenario_5_answer = "no"

# Scenario 6 (production-gear) -- Garnet Valley Genetic Testing
# Registry: should each pair be stitched (same document, consecutive
# sequence positions)?
GARNET_VALLEY_PAIRS = {
    "pair_x": {"doc_a": "protocol_report_88", "seq_a": 11, "doc_b": "protocol_report_88", "seq_b": 12},
    "pair_y": {"doc_a": "protocol_report_88", "seq_a": 11, "doc_b": "consent_form_14", "seq_b": 2},
}


def _should_stitch(pair):
    return pair["doc_a"] == pair["doc_b"] and abs(pair["seq_a"] - pair["seq_b"]) == 1


scenario_6_answers = {key: _should_stitch(pair) for key, pair in GARNET_VALLEY_PAIRS.items()}

# Scenario 7 (production-gear) -- Poplar Crossing School District
# Archive: a load-bearing IEP-accommodation clause (the continuation of
# the top-scored chunk) is at risk of mid-clause truncation under a
# naive character-count cutoff over a 260-token budget. The recipe's own
# boundary-safe fit keeps both the top chunk (150 tokens) and the
# accommodation-clause continuation (100 tokens), totaling 250 tokens.
# Does naive concatenation leave the clause unresolved/truncated? Does
# the recipe preserve it? Does the resolved total still fit budget?
POPLAR_CROSSING_BUDGET_TOKENS = 260
POPLAR_CROSSING_NAIVE_TOTAL_TOKENS = 310  # 150 + 100 + 60 (unrelated) all concatenated
POPLAR_CROSSING_RECIPE_RESOLVED_TOTAL_TOKENS = 250  # 150 + 100, unrelated chunk dropped at the floor

scenario_7_naive_truncates_load_bearing_clause = True
scenario_7_recipe_preserves_load_bearing_clause = True
scenario_7_resolved_total = POPLAR_CROSSING_RECIPE_RESOLVED_TOTAL_TOKENS
scenario_7_within_budget = scenario_7_resolved_total <= POPLAR_CROSSING_BUDGET_TOKENS

# Scenario 8 (judgment) -- Otterbend Wildlife Research Station: every
# chunk the retriever returned for a highly specific query scores below
# the relevance floor. Is it safe to proceed with the highest-scoring
# chunk anyway since it's the "best available" result, or should the
# pipeline surface that no sufficiently relevant result was found?
scenario_8_answer = "surface_no_relevant_result"


# ===========================================================================
# Scoring harness -- identical to starter.py.
# ===========================================================================

def score():
    results = []

    results.append(("Scenario 1 (Harborlight Maritime Archive Society, judgment)", scenario_1_answer.strip().lower() == "no", 1))

    expected_2 = {key for key, score_ in ASPENFIELD_CHUNKS.items() if score_ >= ASPENFIELD_FLOOR}
    results.append(("Scenario 2 (Aspenfield Community College Library)", scenario_2_survivors == expected_2, 1))

    results.append(("Scenario 3 (Beacon Crest Genealogy Society, judgment)", scenario_3_answer.strip().lower() == "no", 1))

    expected_4_kept, expected_4_total = _boundary_safe_fit(SLATEBROOK_SURVIVORS, SLATEBROOK_BUDGET_TOKENS)
    results.append((
        "Scenario 4 (Slatebrook Patent Research Group)",
        scenario_4_kept_chunks == expected_4_kept and scenario_4_total_tokens == expected_4_total,
        1,
    ))

    results.append(("Scenario 5 (Timberline Structural Engineering Archive, judgment)", scenario_5_answer.strip().lower() == "no", 1))

    correct_6 = sum(1 for k, pair in GARNET_VALLEY_PAIRS.items() if scenario_6_answers.get(k) == _should_stitch(pair))
    results.append(("Scenario 6 (Garnet Valley Genetic Testing Registry)", correct_6 == len(GARNET_VALLEY_PAIRS), 1))

    results.append((
        "Scenario 7 (Poplar Crossing School District Archive)",
        scenario_7_naive_truncates_load_bearing_clause is True
        and scenario_7_recipe_preserves_load_bearing_clause is True
        and scenario_7_resolved_total == POPLAR_CROSSING_RECIPE_RESOLVED_TOTAL_TOKENS
        and scenario_7_within_budget is True,
        1,
    ))

    results.append(("Scenario 8 (Otterbend Wildlife Research Station, judgment)", scenario_8_answer.strip().lower() == "surface_no_relevant_result", 1))

    return results


def main():
    print("Chapter 8 Practice Bank -- Score Report (reference solution)")
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
