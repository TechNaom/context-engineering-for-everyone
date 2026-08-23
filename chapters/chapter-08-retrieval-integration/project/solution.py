"""
Module 4 Project: Build Quartzfield Regional Public Defender
Consortium's BriefLine Retrieval Integration + Source Assembly Pipeline
-- REFERENCE SOLUTION

See README.md for the full spec and task instructions. This is ONE
valid, complete design -- not the only correct one, since the two
write-ups are intentionally open judgment calls. Use it to check your
reasoning's completeness and rigor, not to match numbers exactly.

THIS IS THE CURRICULUM MAP'S OWN L3 INDEPENDENT PROJECT (ships after Ch.
8, per the map's own project ladder), closing Module 4. Per this
course's "no scaffold" convention for L3, this file is a complete
reference design, not a partially-filled template -- starter.py gives
you the same spec with every design decision left to you.
"""

# ---------------------------------------------------------------------------
# PART 1 -- RETRIEVAL INTEGRATION (Chapter 8's own skill)
# ---------------------------------------------------------------------------
# BriefLine's retriever returned five ranked, scored chunks from the
# sentencing-guideline and case-law corpus for a pre-hearing brief.
# Retrieval architecture itself is correct and given -- your job is
# turning this raw ranked output into one well-formed retrieved source.
RELEVANCE_FLOOR = 0.55
PART1_BUDGET_TOKENS = 380

RAW_RANKED_CHUNKS = {
    "chunk_guideline_base_range": {"score": 0.94, "tokens": 160, "doc": "guideline_7B", "seq": 3},
    "chunk_guideline_departure_clause": {"score": 0.89, "tokens": 130, "doc": "guideline_7B", "seq": 4},
    "chunk_prior_case_precedent": {"score": 0.62, "tokens": 120, "doc": "case_precedent_501", "seq": 1},
    "chunk_unrelated_procedural_note": {"score": 0.41, "tokens": 90, "doc": "admin_manual_2", "seq": 9},
    "chunk_unrelated_fee_schedule": {"score": 0.28, "tokens": 70, "doc": "admin_manual_2", "seq": 12},
}

# YOUR DESIGN -- Part 1, Step 1: which chunk keys clear the relevance
# floor?
PART1_SURVIVORS = {
    key for key, meta in RAW_RANKED_CHUNKS.items() if meta["score"] >= RELEVANCE_FLOOR
}

# YOUR DESIGN -- Part 1, Step 2: fit survivors to budget in descending
# score order, stopping BEFORE any chunk that would exceed budget (never
# partially include a chunk). List the kept chunk keys in the order
# kept, and the resulting total.
def _boundary_safe_fit(survivor_keys, chunks, budget):
    ordered = sorted(survivor_keys, key=lambda k: chunks[k]["score"], reverse=True)
    kept = []
    total = 0
    for key in ordered:
        tokens = chunks[key]["tokens"]
        if total + tokens <= budget:
            kept.append(key)
            total += tokens
    return kept, total


PART1_KEPT_CHUNKS, PART1_TOTAL_TOKENS = _boundary_safe_fit(
    PART1_SURVIVORS, RAW_RANKED_CHUNKS, PART1_BUDGET_TOKENS
)

# YOUR DESIGN -- Part 1, Step 3/4: which kept chunks are consecutive
# passages of the same document and should be stitched together? Give
# this as a set of frozensets, each frozenset being one stitched group
# (chunks that share a doc and have consecutive seq numbers).
PART1_STITCHED_GROUPS = {
    frozenset({"chunk_guideline_base_range", "chunk_guideline_departure_clause"}),
}

# YOUR DESIGN -- Part 1, Step 3: provenance for every kept chunk (source
# doc + section reference).
PART1_PROVENANCE = {
    "chunk_guideline_base_range": {"source_doc": "guideline_7B", "section": "Sec. 3 (base range)"},
    "chunk_guideline_departure_clause": {"source_doc": "guideline_7B", "section": "Sec. 4 (departure clause)"},
}

PART1_JUSTIFICATION = (
    "The 0.55 relevance floor correctly excludes both unrelated admin_manual_2 "
    "chunks (0.41 and 0.28), leaving three genuine candidates. The boundary-safe "
    "fit takes the two highest-scored chunks (0.94 base range, 160 tokens; 0.89 "
    "departure clause, 130 tokens = 290 tokens) and correctly stops before the "
    "120-token precedent chunk, which would push the running total to 410, over "
    "the 380-token budget -- no chunk is ever partially included. The base range "
    "and departure clause chunks are consecutive paragraphs (seq 3 and 4) of the "
    "same guideline_7B document, so they are stitched into one 290-token "
    "contiguous excerpt rather than left as two separate blocks, and both carry "
    "explicit provenance so the resulting source can be cited and correctly "
    "authority-ranked in Part 2."
)

# ---------------------------------------------------------------------------
# PART 2 -- SOURCE ASSEMBLY (Chapter 7's own skill)
# ---------------------------------------------------------------------------
# Part 1's stitched, provenance-tagged output becomes ONE inventoried
# source below (type "retrieved_document"). It joins three other
# already-correctly-produced sources for the same pre-hearing brief
# request. Authority ranking for this request type is given, fixed by
# Chapter 7's own recipe -- not re-derived here.
AUTHORITY_RANK = {
    "system_instructions": 4,
    "live_tool_output": 3,
    "conversation_history": 2,
    "retrieved_document": 1,
}
WINDOW_BUDGET_TOKENS = 500

CANDIDATE_SOURCES = {
    "part1_retrieved_document": {
        "type": "retrieved_document",
        "tokens": PART1_TOTAL_TOKENS,  # 290, from Part 1's own resolved output
        "claims": {"sentencing_departure_availability"},
    },
    "live_docket_status_check": {
        "type": "live_tool_output",
        "tokens": 45,
        "claims": {"sentencing_departure_availability"},  # CONTRADICTS the retrieved doc
    },
    "conversation_history_this_session": {
        "type": "conversation_history",
        "tokens": 80,
        "claims": {"defendant_statement_context"},
    },
    "office_practice_standard": {
        "type": "system_instructions",
        "tokens": 60,
        "claims": {"brief_formatting_requirement"},
    },
}

# The retrieved guideline_7B departure clause (three weeks old in the
# corpus) states the departure exception applies; the live docket-status
# tool call reports the exception was superseded by a statute change
# last month, in this jurisdiction, as of today. Both sources speak to
# the SAME claim (sentencing_departure_availability) and disagree.

# YOUR DESIGN -- Part 2, Step 3: was a genuine contradiction detected?
PART2_CONTRADICTION_DETECTED = True

# YOUR DESIGN -- Part 2, Step 2/4: per AUTHORITY_RANK, which source
# governs the contested claim?
def _resolve_claim_conflict(source_a, source_b, sources):
    rank_a = AUTHORITY_RANK[sources[source_a]["type"]]
    rank_b = AUTHORITY_RANK[sources[source_b]["type"]]
    return source_a if rank_a > rank_b else source_b


PART2_WINNING_SOURCE = _resolve_claim_conflict(
    "part1_retrieved_document", "live_docket_status_check", CANDIDATE_SOURCES
)

# YOUR DESIGN -- Part 2, Step 5/6: which source keys remain in the final
# assembled window? (No restated duplicate content exists between these
# four sources, so nothing needs deduplicating this time -- the
# retrieved document's OTHER content, e.g. the base sentencing range, is
# still valid and kept; only its specific departure-availability claim
# is now understood to be superseded, not the whole block.)
PART2_SOURCES_RETAINED = {
    "part1_retrieved_document",
    "live_docket_status_check",
    "conversation_history_this_session",
    "office_practice_standard",
}

PART2_ASSEMBLED_TOTAL_TOKENS = sum(
    CANDIDATE_SOURCES[key]["tokens"] for key in PART2_SOURCES_RETAINED
)
PART2_WITHIN_BUDGET = PART2_ASSEMBLED_TOTAL_TOKENS <= WINDOW_BUDGET_TOKENS

PART2_JUSTIFICATION = (
    "part1_retrieved_document and live_docket_status_check both make a claim "
    "about sentencing_departure_availability, and they disagree -- the retrieved "
    "guideline commentary says the departure exception applies, the live docket "
    "status check says it was superseded by statute last month. Per the "
    "authority ranking, live_tool_output (rank 3) outranks retrieved_document "
    "(rank 1) for a time-sensitive status claim, so live_docket_status_check "
    "governs; the retrieved document's own general sentencing-range content is "
    "still valid and kept in the window, but its specific departure claim is now "
    "understood as superseded, not silently presented as current. All four "
    "sources remain in the assembled window (no restated duplicate content "
    "exists to deduplicate this time), totaling 475 of the 500-token budget, "
    "leaving 25 tokens of headroom. This resolved, provenance-tagged set is now "
    "ready to hand to Chapter 6's own Context Ordering Recipe, exactly as "
    "Chapter 7's Step 6 and this chapter's own Step 6 both describe."
)


# ===========================================================================
# Structural + internal-consistency self-check -- identical to
# starter.py. Plays the role of both chapters' own deterministic
# verification steps: Chapter 8's boundary/provenance/stitch rules for
# Part 1, and Chapter 7's contradiction-detection/resolution rules for
# Part 2.
# ===========================================================================

def check_part1_floor():
    errors = []
    expected = {key for key, meta in RAW_RANKED_CHUNKS.items() if meta["score"] >= RELEVANCE_FLOOR}
    if not isinstance(PART1_SURVIVORS, set):
        errors.append("PART1_SURVIVORS must be a set of chunk keys.")
        return errors
    if PART1_SURVIVORS != expected:
        errors.append(f"PART1_SURVIVORS should be {sorted(expected)}, got {sorted(PART1_SURVIVORS)}.")
    return errors


def check_part1_fit():
    errors = []
    expected_kept, expected_total = _boundary_safe_fit(PART1_SURVIVORS, RAW_RANKED_CHUNKS, PART1_BUDGET_TOKENS)
    if PART1_KEPT_CHUNKS != expected_kept:
        errors.append(f"PART1_KEPT_CHUNKS should be {expected_kept}, got {PART1_KEPT_CHUNKS}.")
    if PART1_TOTAL_TOKENS != expected_total:
        errors.append(f"PART1_TOTAL_TOKENS should be {expected_total}, got {PART1_TOTAL_TOKENS}.")
    if PART1_TOTAL_TOKENS > PART1_BUDGET_TOKENS:
        errors.append(f"PART1_TOTAL_TOKENS ({PART1_TOTAL_TOKENS}) exceeds the {PART1_BUDGET_TOKENS}-token budget.")
    return errors


def check_part1_stitch():
    errors = []
    expected_group = frozenset({"chunk_guideline_base_range", "chunk_guideline_departure_clause"})
    if expected_group not in PART1_STITCHED_GROUPS:
        errors.append(
            "PART1_STITCHED_GROUPS must include the base-range/departure-clause "
            "group -- they are consecutive paragraphs (seq 3, 4) of guideline_7B."
        )
    return errors


def check_part1_provenance():
    errors = []
    for key in PART1_KEPT_CHUNKS:
        meta = PART1_PROVENANCE.get(key)
        if not meta or not meta.get("source_doc") or not meta.get("section"):
            errors.append(f"PART1_PROVENANCE is missing complete source_doc/section for kept chunk: {key}")
    return errors


def check_part2_contradiction():
    errors = []
    if PART2_CONTRADICTION_DETECTED is not True:
        errors.append(
            "PART2_CONTRADICTION_DETECTED must be True -- part1_retrieved_document "
            "and live_docket_status_check both claim sentencing_departure_availability "
            "and disagree."
        )
    return errors


def check_part2_resolution():
    errors = []
    expected_winner = _resolve_claim_conflict("part1_retrieved_document", "live_docket_status_check", CANDIDATE_SOURCES)
    if PART2_WINNING_SOURCE != expected_winner:
        errors.append(f"PART2_WINNING_SOURCE should be '{expected_winner}' (higher authority rank), got '{PART2_WINNING_SOURCE}'.")
    return errors


def check_part2_budget():
    errors = []
    if not isinstance(PART2_SOURCES_RETAINED, set):
        errors.append("PART2_SOURCES_RETAINED must be a set of source keys.")
        return errors
    missing = set(CANDIDATE_SOURCES.keys()) - PART2_SOURCES_RETAINED
    if missing:
        errors.append(f"PART2_SOURCES_RETAINED is missing sources that should be kept (no dedup needed here): {sorted(missing)}")
    expected_total = sum(CANDIDATE_SOURCES[key]["tokens"] for key in PART2_SOURCES_RETAINED)
    if PART2_ASSEMBLED_TOTAL_TOKENS != expected_total:
        errors.append(f"PART2_ASSEMBLED_TOTAL_TOKENS should be {expected_total}, got {PART2_ASSEMBLED_TOTAL_TOKENS}.")
    if PART2_ASSEMBLED_TOTAL_TOKENS > WINDOW_BUDGET_TOKENS:
        errors.append(f"PART2_ASSEMBLED_TOTAL_TOKENS ({PART2_ASSEMBLED_TOTAL_TOKENS}) exceeds the {WINDOW_BUDGET_TOKENS}-token budget.")
    if PART2_WITHIN_BUDGET != (PART2_ASSEMBLED_TOTAL_TOKENS <= WINDOW_BUDGET_TOKENS):
        errors.append("PART2_WITHIN_BUDGET does not match the actual budget comparison.")
    return errors


def check_writeups():
    errors = []
    if len(PART1_JUSTIFICATION.strip()) < 40:
        errors.append("PART1_JUSTIFICATION should be a real 2-4 sentence explanation (40+ characters)")
    if len(PART2_JUSTIFICATION.strip()) < 40:
        errors.append("PART2_JUSTIFICATION should be a real 2-4 sentence explanation (40+ characters)")
    return errors


def main():
    print("Module 4 Project (L3 Independent) -- Self-Check (reference solution)")
    print("=" * 70)
    all_errors = (
        check_part1_floor() + check_part1_fit() + check_part1_stitch()
        + check_part1_provenance() + check_part2_contradiction()
        + check_part2_resolution() + check_part2_budget() + check_writeups()
    )

    print("-- Part 1: Retrieval Integration (Chapter 8's own skill) --")
    print(f"Survivors past relevance floor: {sorted(PART1_SURVIVORS)}")
    print(f"Boundary-safe kept chunks: {PART1_KEPT_CHUNKS} ({PART1_TOTAL_TOKENS}/{PART1_BUDGET_TOKENS} tokens)")
    print(f"Stitched groups: {[sorted(g) for g in PART1_STITCHED_GROUPS]}")
    print("-- Part 2: Source Assembly (Chapter 7's own skill) --")
    print(f"Contradiction detected: {PART2_CONTRADICTION_DETECTED}")
    print(f"Winning source for the contested claim: {PART2_WINNING_SOURCE}")
    print(f"Assembled window total: {PART2_ASSEMBLED_TOTAL_TOKENS}/{WINDOW_BUDGET_TOKENS} tokens (within budget: {PART2_WITHIN_BUDGET})")

    if not all_errors:
        print("\nPASS -- Part 1's relevance floor, boundary-safe fit, stitching, and")
        print("provenance are all correct, and Part 2's contradiction detection,")
        print("authority-based resolution, and budget fit are all correct.")
        print("Now compare your reasoning (not just structure) against solution.py, and")
        print("check your work against RUBRIC.md before considering this project done.")
    else:
        print(f"\n{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
