"""
Module 4 Project: Build Quartzfield Regional Public Defender
Consortium's BriefLine Retrieval Integration + Source Assembly Pipeline

THIS IS THE CURRICULUM MAP'S OWN L3 INDEPENDENT PROJECT (ships after Ch.
8), closing Module 4. "Independent" means no scaffold: unlike Chapter
4's L2 project, this file gives you the full spec and the data, but no
partially-filled template or step-by-step hints beyond the spec itself
-- you design both parts from scratch, the same way Module 4's own two
labs are stated as a pair in the curriculum map ("take a retriever's
ranked output and produce well-formed context from it" + "assemble
context from 3+ real sources for one request").

Quartzfield Regional Public Defender Consortium is a fictional public
defender's office. Its pre-hearing brief assistant, BriefLine, prepares
a sentencing brief by (1) turning a retriever's raw ranked chunk list
into one well-formed source (Chapter 8's own Retrieval Integration
Recipe), then (2) combining that source with three other
already-correctly-produced sources for the same request, resolving a
genuine contradiction between two of them (Chapter 7's own Source
Assembly Recipe). Neither chapter's recipe is re-derived here -- this
project tests whether you can apply both, in sequence, to one real
pipeline, exactly as the module's own two labs require together.

YOUR TASK
---------
PART 1 (Chapter 8's own skill): given RAW_RANKED_CHUNKS below, apply a
relevance floor, fit survivors to budget at a chunk boundary (never
partially including a chunk), identify which surviving chunks should be
stitched together (same document, consecutive seq numbers), and attach
provenance to every kept chunk.

PART 2 (Chapter 7's own skill): given CANDIDATE_SOURCES below (which
includes Part 1's own resolved output as one source), detect the
contradiction between two sources making the same claim, resolve it
using the given AUTHORITY_RANK, and confirm the retained set fits the
window budget.

Fill in every TODO, then run:

    python3 starter.py

Like Chapter 6's own project, most of this one IS mechanically checkable
against your own numbers -- only the QUALITY of your two write-ups is
open-ended. Compare your full reasoning against solution.py, then
self-grade against RUBRIC.md.
"""

# ---------------------------------------------------------------------------
# PART 1 -- RETRIEVAL INTEGRATION
# ---------------------------------------------------------------------------
RELEVANCE_FLOOR = 0.55
PART1_BUDGET_TOKENS = 380

RAW_RANKED_CHUNKS = {
    "chunk_guideline_base_range": {"score": 0.94, "tokens": 160, "doc": "guideline_7B", "seq": 3},
    "chunk_guideline_departure_clause": {"score": 0.89, "tokens": 130, "doc": "guideline_7B", "seq": 4},
    "chunk_prior_case_precedent": {"score": 0.62, "tokens": 120, "doc": "case_precedent_501", "seq": 1},
    "chunk_unrelated_procedural_note": {"score": 0.41, "tokens": 90, "doc": "admin_manual_2", "seq": 9},
    "chunk_unrelated_fee_schedule": {"score": 0.28, "tokens": 70, "doc": "admin_manual_2", "seq": 12},
}

# TODO (Part 1, Step 1): which chunk keys clear RELEVANCE_FLOOR?
PART1_SURVIVORS = set()  # TODO

# TODO (Part 1, Step 2): fit your survivors to PART1_BUDGET_TOKENS in
# descending score order, stopping BEFORE any chunk that would exceed
# budget. List the kept chunk keys (in order kept) and the total tokens.
PART1_KEPT_CHUNKS = []  # TODO
PART1_TOTAL_TOKENS = 0  # TODO

# TODO (Part 1, Step 4): which kept chunks are consecutive passages of
# the same document and should be stitched? A set of frozensets, one per
# stitched group.
PART1_STITCHED_GROUPS = set()  # TODO

# TODO (Part 1, Step 3): provenance (source_doc + section) for every
# chunk key in PART1_KEPT_CHUNKS.
PART1_PROVENANCE = {
    # TODO -- one entry per kept chunk, e.g.:
    # "chunk_guideline_base_range": {"source_doc": "guideline_7B", "section": "Sec. 3 (base range)"},
}

# TODO: 2-4 sentences defending your Part 1 floor/fit/stitch/provenance
# choices.
PART1_JUSTIFICATION = ""

# ---------------------------------------------------------------------------
# PART 2 -- SOURCE ASSEMBLY
# ---------------------------------------------------------------------------
AUTHORITY_RANK = {
    "system_instructions": 4,
    "live_tool_output": 3,
    "conversation_history": 2,
    "retrieved_document": 1,
}
WINDOW_BUDGET_TOKENS = 500

# NOTE: "tokens" for part1_retrieved_document should be YOUR OWN
# PART1_TOTAL_TOKENS result, not a fresh number -- Part 1's output feeds
# Part 2 directly, exactly as the Retrieval Integration Recipe's own
# Step 6 describes.
CANDIDATE_SOURCES = {
    "part1_retrieved_document": {
        "type": "retrieved_document",
        "tokens": None,  # TODO -- use your own PART1_TOTAL_TOKENS
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

# TODO (Part 2, Step 3): was a genuine contradiction detected between
# part1_retrieved_document and live_docket_status_check?
PART2_CONTRADICTION_DETECTED = None  # TODO

# TODO (Part 2, Step 2/4): per AUTHORITY_RANK, which source key governs
# the contested sentencing_departure_availability claim?
PART2_WINNING_SOURCE = None  # TODO

# TODO (Part 2, Step 5/6): which source keys remain in the final
# assembled window? (Think about whether any source needs to be fully
# dropped, or just have one specific claim flagged as superseded.)
PART2_SOURCES_RETAINED = set()  # TODO

# TODO: compute from your own PART2_SOURCES_RETAINED.
PART2_ASSEMBLED_TOTAL_TOKENS = 0  # TODO
PART2_WITHIN_BUDGET = None  # TODO

# TODO: 2-4 sentences defending your Part 2 contradiction/resolution/
# budget choices.
PART2_JUSTIFICATION = ""


# ===========================================================================
# Structural + internal-consistency self-check -- do not need to edit
# anything below this line.
# ===========================================================================

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


def _resolve_claim_conflict(source_a, source_b, sources):
    rank_a = AUTHORITY_RANK[sources[source_a]["type"]]
    rank_b = AUTHORITY_RANK[sources[source_b]["type"]]
    return source_a if rank_a > rank_b else source_b


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
    try:
        expected_total = sum(CANDIDATE_SOURCES[key]["tokens"] for key in PART2_SOURCES_RETAINED)
    except TypeError:
        errors.append("CANDIDATE_SOURCES['part1_retrieved_document']['tokens'] is still None -- fill it in from your own PART1_TOTAL_TOKENS.")
        return errors
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
    print("Module 4 Project (L3 Independent) -- Self-Check")
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
        print("\nFix the issues above and re-run this file.")


if __name__ == "__main__":
    main()
