"""
Chapter 8 Exercises: Retrieval Integration

Scenario: Cobalt Ridge Claims Adjustment Bureau, a fictional insurance
claims adjustment firm. Its claims-review assistant, DossierLine,
retrieves ranked, scored excerpts from a large policy-document and
prior-claim corpus for "Coverage Determination Review" requests.
Chapters 1-7's own recipes have already run for this request type: a
correct budget, correct memory handling, nothing over budget needing
compression, no positional risk, and (once this chapter's own bundle is
ready) no multi-source contradiction left unresolved. Retrieval
architecture itself -- the embedding model, similarity search, ranking
-- is correct and out of scope; your job is this chapter's own new
skill: turning the retriever's raw ranked output into one well-formed
source before it ever reaches Chapter 7's own inventory step.

Fill in each `# TODO`, then run:

    python3 starter.py

to see a score report. Compare against solution.py, which scores a
perfect total.
"""

# ===========================================================================
# Exercise 1 -- match each scenario to the right integration approach.
# Choose from APPROACHES for each key below.
# ===========================================================================
APPROACHES = {"unconditional_top_k", "relevance_floor_only", "retrieval_integration_recipe"}

EXERCISE_1_SCENARIOS = {
    "always_takes_exactly_k_chunks_then_truncates_by_char_count": (
        "The pipeline always includes exactly k ranked chunks regardless "
        "of score, then truncates the assembled text by raw character "
        "count wherever the budget runs out, with no chunk-boundary "
        "awareness."
    ),
    "drops_low_score_chunks_but_still_truncates_and_never_stitches": (
        "Chunks below a minimum score are dropped before selection, but "
        "there is still no boundary-safe budget fit, no provenance "
        "tracking, and no merging of adjacent same-document chunks."
    ),
    "floor_then_boundary_fit_then_provenance_then_stitch_then_handoff": (
        "A relevance floor is applied, surviving chunks are fit to "
        "budget at a chunk boundary, provenance is preserved, adjacent "
        "same-document chunks are stitched together, an empty result is "
        "handled explicitly, and the resolved bundle is handed to "
        "Chapter 7's own Source Assembly Recipe."
    ),
}

# TODO: assign an approach name from APPROACHES to each scenario.
exercise_1_answers = {
    "always_takes_exactly_k_chunks_then_truncates_by_char_count": None,  # TODO
    "drops_low_score_chunks_but_still_truncates_and_never_stitches": None,  # TODO
    "floor_then_boundary_fit_then_provenance_then_stitch_then_handoff": None,  # TODO
}

# ===========================================================================
# Exercise 2 -- order the Retrieval Integration Recipe's six steps.
# ===========================================================================
RECIPE_STEPS = {
    "step_relevance_floor": "Apply a relevance floor before selecting anything -- don't take the top k unconditionally.",
    "step_boundary_safe_fit": "Fit surviving chunks to budget by score, stopping at a chunk boundary rather than truncating mid-sentence.",
    "step_preserve_provenance": "Preserve each surviving chunk's source document, section, and score alongside its text.",
    "step_stitch_adjacent": "Stitch adjacent chunks from the same document back into one contiguous block.",
    "step_handle_empty_result": "Handle a low-confidence or empty result set explicitly, rather than falling back to the top chunk anyway.",
    "step_handoff_to_source_assembly": "Hand the resolved, provenance-tagged bundle to Chapter 7's own Source Assembly Recipe as one source.",
}

# TODO: put the six step keys above in the correct order.
exercise_2_order = [
    # TODO
]

# ===========================================================================
# Exercise 3 (production-gear) -- relevance-floor filtering. Fill in
# exercise_3_survivors with the set of chunk keys that clear the floor.
# ===========================================================================
RELEVANCE_FLOOR = 0.50

EXERCISE_3_CHUNKS = {
    "chunk_policy_exclusion_clause": 0.93,
    "chunk_adjacent_policy_paragraph": 0.85,
    "chunk_prior_claim_precedent": 0.71,
    "chunk_unrelated_regional_bulletin": 0.44,
    "chunk_unrelated_rate_filing": 0.31,
}

# TODO: which chunk keys have a score >= RELEVANCE_FLOOR?
exercise_3_survivors = set()  # TODO

# ===========================================================================
# Exercise 4 (production-gear) -- boundary-safe budget fit. Select
# surviving chunks in descending score order, stopping BEFORE any chunk
# that would push the running total over budget (never partially include
# a chunk). Fill in the list of kept chunk keys, in the order kept, and
# the resulting total token count.
# ===========================================================================
DOSSIERLINE_BUDGET_TOKENS = 420

EXERCISE_4_SURVIVORS_WITH_TOKENS = {
    "chunk_policy_exclusion_clause": (0.93, 190),
    "chunk_adjacent_policy_paragraph": (0.85, 140),
    "chunk_prior_claim_precedent": (0.71, 150),
}

# TODO: fill these in by hand-computing the boundary-safe fit.
exercise_4_kept_chunks = []  # TODO
exercise_4_total_tokens = 0  # TODO

# ===========================================================================
# Exercise 5 (production-gear) -- provenance completeness check. A chunk
# is provenance-complete only if it carries a non-empty source document
# id, section reference, AND score. True = complete; False = missing at
# least one required field.
# ===========================================================================
EXERCISE_5_CHUNK_METADATA = {
    "chunk_a": {"source_doc": "policy_4471", "section": "Sec. 3.2", "score": 0.88},
    "chunk_b": {"source_doc": "policy_4471", "section": "", "score": 0.81},
    "chunk_c": {"source_doc": "", "section": "Sec. 1.1", "score": 0.76},
    "chunk_d": {"source_doc": "claim_precedent_209", "section": "Sec. 2.0", "score": 0.65},
}

# TODO: True/False for each chunk key.
exercise_5_answers = {
    "chunk_a": None,  # TODO
    "chunk_b": None,  # TODO
    "chunk_c": None,  # TODO
    "chunk_d": None,  # TODO
}

# ===========================================================================
# Exercise 6 (production-gear) -- adjacent-chunk stitching. Two chunks
# should be stitched if they share the same source document AND their
# sequence positions are consecutive (differ by exactly 1).
# ===========================================================================
EXERCISE_6_CHUNK_PAIRS = {
    "pair_1": {"doc_a": "policy_4471", "seq_a": 4, "doc_b": "policy_4471", "seq_b": 5},
    "pair_2": {"doc_a": "policy_4471", "seq_a": 4, "doc_b": "policy_4471", "seq_b": 9},
    "pair_3": {"doc_a": "policy_4471", "seq_a": 2, "doc_b": "claim_precedent_209", "seq_b": 3},
    "pair_4": {"doc_a": "claim_precedent_209", "seq_a": 7, "doc_b": "claim_precedent_209", "seq_b": 8},
}

# TODO: True/False -- should this pair be stitched?
exercise_6_answers = {
    "pair_1": None,  # TODO
    "pair_2": None,  # TODO
    "pair_3": None,  # TODO
    "pair_4": None,  # TODO
}

# ===========================================================================
# Exercise 7 (production-gear) -- naive-vs-recipe regression gate. A
# load-bearing exclusion clause (chunk_adjacent_policy_paragraph, the
# continuation of chunk_policy_exclusion_clause) is at risk of mid-clause
# truncation under a naive character-count cutoff. Does the naive
# pipeline drop it? Does the recipe preserve it while staying in budget?
# ===========================================================================
NAIVE_RAW_CONCAT_TOKENS = 480  # all 3 survivors concatenated, no boundary awareness
NAIVE_CUTOFF_TOKENS = 420  # same budget, applied by raw count -> cuts the 3rd chunk mid-sentence

# TODO: True/False for each.
exercise_7_naive_drops_load_bearing_clause = None  # TODO
exercise_7_recipe_preserves_load_bearing_clause = None  # TODO (use your Exercise 4 answer)
exercise_7_recipe_within_budget = None  # TODO (use your Exercise 4 answer)

# ===========================================================================
# Exercise 8 (production-gear) -- empty/low-confidence result decision.
# For each retrieval outcome, decide the correct next action.
# ===========================================================================
RESOLUTION_OPTIONS = {"proceed_with_bundle", "surface_no_relevant_result"}

EXERCISE_8_SCENARIOS = {
    "two_chunks_clear_the_floor_with_room_to_spare": (
        "Two chunks clear the 0.50 relevance floor and fit comfortably "
        "inside budget."
    ),
    "every_chunk_scores_below_the_floor": (
        "All five retrieved chunks score below the 0.50 relevance floor "
        "-- nothing genuinely relevant was found."
    ),
    "highest_scoring_chunk_is_0_38_no_chunk_clears_the_floor": (
        "The highest-scoring retrieved chunk is 0.38; no chunk clears "
        "the floor, but it is tempting to include it anyway since it is "
        "the 'best available' result."
    ),
}

# TODO: a resolution from RESOLUTION_OPTIONS for each scenario.
exercise_8_answers = {
    "two_chunks_clear_the_floor_with_room_to_spare": None,  # TODO
    "every_chunk_scores_below_the_floor": None,  # TODO
    "highest_scoring_chunk_is_0_38_no_chunk_clears_the_floor": None,  # TODO
}


# ===========================================================================
# Scoring harness -- do not need to edit anything below this line.
# ===========================================================================

def _boundary_safe_fit(chunks_with_scores_tokens, budget):
    ordered = sorted(chunks_with_scores_tokens.items(), key=lambda kv: kv[1][0], reverse=True)
    kept = []
    running_total = 0
    for key, (score, tokens) in ordered:
        if running_total + tokens <= budget:
            kept.append(key)
            running_total += tokens
    return kept, running_total


def _is_provenance_complete(meta):
    return bool(meta.get("source_doc")) and bool(meta.get("section")) and meta.get("score") is not None


def _should_stitch(pair):
    return pair["doc_a"] == pair["doc_b"] and abs(pair["seq_a"] - pair["seq_b"]) == 1


def score_exercise_1():
    key = {
        "always_takes_exactly_k_chunks_then_truncates_by_char_count": "unconditional_top_k",
        "drops_low_score_chunks_but_still_truncates_and_never_stitches": "relevance_floor_only",
        "floor_then_boundary_fit_then_provenance_then_stitch_then_handoff": "retrieval_integration_recipe",
    }
    correct = sum(1 for k, v in key.items() if exercise_1_answers.get(k) == v)
    return correct, len(key)


def score_exercise_2():
    key = [
        "step_relevance_floor",
        "step_boundary_safe_fit",
        "step_preserve_provenance",
        "step_stitch_adjacent",
        "step_handle_empty_result",
        "step_handoff_to_source_assembly",
    ]
    correct = 1 if exercise_2_order == key else 0
    return correct, 1


def score_exercise_3():
    expected = {key for key, score in EXERCISE_3_CHUNKS.items() if score >= RELEVANCE_FLOOR}
    correct = int(exercise_3_survivors == expected)
    return correct, 1


def score_exercise_4():
    expected_kept, expected_total = _boundary_safe_fit(EXERCISE_4_SURVIVORS_WITH_TOKENS, DOSSIERLINE_BUDGET_TOKENS)
    correct = 0
    correct += int(exercise_4_kept_chunks == expected_kept)
    correct += int(exercise_4_total_tokens == expected_total)
    return correct, 2


def score_exercise_5():
    correct = sum(
        1 for k, meta in EXERCISE_5_CHUNK_METADATA.items()
        if exercise_5_answers.get(k) == _is_provenance_complete(meta)
    )
    return correct, len(EXERCISE_5_CHUNK_METADATA)


def score_exercise_6():
    correct = sum(
        1 for k, pair in EXERCISE_6_CHUNK_PAIRS.items()
        if exercise_6_answers.get(k) == _should_stitch(pair)
    )
    return correct, len(EXERCISE_6_CHUNK_PAIRS)


def score_exercise_7():
    correct = 0
    correct += int(exercise_7_naive_drops_load_bearing_clause is True)
    correct += int(exercise_7_recipe_preserves_load_bearing_clause is True)
    correct += int(exercise_7_recipe_within_budget is True)
    return correct, 3


def score_exercise_8():
    key = {
        "two_chunks_clear_the_floor_with_room_to_spare": "proceed_with_bundle",
        "every_chunk_scores_below_the_floor": "surface_no_relevant_result",
        "highest_scoring_chunk_is_0_38_no_chunk_clears_the_floor": "surface_no_relevant_result",
    }
    correct = sum(1 for k, v in key.items() if exercise_8_answers.get(k) == v)
    return correct, len(key)


def main():
    exercises = [
        ("Exercise 1 -- match scenarios to integration approaches", score_exercise_1),
        ("Exercise 2 -- order the Retrieval Integration Recipe", score_exercise_2),
        ("Exercise 3 -- relevance-floor filtering", score_exercise_3),
        ("Exercise 4 -- boundary-safe budget fit", score_exercise_4),
        ("Exercise 5 -- provenance completeness check", score_exercise_5),
        ("Exercise 6 -- adjacent-chunk stitching", score_exercise_6),
        ("Exercise 7 -- naive-vs-recipe regression gate", score_exercise_7),
        ("Exercise 8 -- empty/low-confidence result decision", score_exercise_8),
    ]

    total_correct = 0
    total_possible = 0
    print("Chapter 8 Exercises -- Score Report")
    print("=" * 60)
    for label, fn in exercises:
        correct, possible = fn()
        total_correct += correct
        total_possible += possible
        print(f"{label}: {correct}/{possible}")
    print("=" * 60)
    print(f"TOTAL: {total_correct}/{total_possible}")
    if total_possible and total_correct == total_possible:
        print("Perfect score -- every exercise correctly reasoned.")
    else:
        print("Keep going -- fill in the remaining TODOs and re-run this file.")


if __name__ == "__main__":
    main()
