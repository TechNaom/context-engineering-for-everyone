"""
Module 3 Project: Build Brackholt County Court Records Office's
ArchiveLine Compression + Ordering Pipeline -- REFERENCE SOLUTION

See README.md for the full spec and task instructions. This is ONE
valid, complete design -- not the only correct one, since the compressed
summary's exact wording, both write-ups, and the specific strategy
justification are intentionally open judgment calls. Use it to check
your reasoning's completeness and rigor, not to match numbers exactly.
"""

# Line budgets for this request type were already allocated via
# Chapter 2's recipe -- given here, not re-derived. This project's own
# job is Chapter 5's compression skill (Part 1) and Chapter 6's ordering
# skill (Part 2), applied together to the same case file, exactly as
# Module 3's own two labs require ("build a summarization pipeline that
# preserves load-bearing facts; reorder a context window to fix a
# lost-in-the-middle failure").
COMPRESSION_TARGET_TOKENS = 600
WINDOW_BUDGET_TOKENS = 3_200

# ---------------------------------------------------------------------------
# PART 1 -- COMPRESSION FIDELITY (Chapter 5's own skill, exercised again
# here because this is Module 3's joint project, not a Chapter 6-only one)
# ---------------------------------------------------------------------------
# An aged-out 3,000-token segment of this session's own docket-review
# conversation has to compress down to the fixed 600-token target above.
# Three load-bearing candidates were flagged before compressing (Chapter
# 5's own Step 2) -- given here as the candidate list you must preserve.
RAW_SEGMENT_TOKENS = 3_000
CANDIDATE_DETAILS = {
    "missing_evidence_log_entry",
    "hearing_continuance_deadline",
    "co_defendant_conflict_note",
}
STRATEGY_OPTIONS = {"extractive", "abstractive"}

# YOUR DESIGN -- Part 1: which candidates actually survive in your
# compressed output (a set of candidate keys), and which strategy you
# chose for each (all three candidates are structured, specific facts
# -- exact wording matters for each -- so extractive is the correct
# choice for all three; the point isn't the choice varying, it's
# choosing on purpose and getting it right for content where exact
# wording matters).
PRODUCED_SUMMARY_CONTENT = {
    "missing_evidence_log_entry",
    "hearing_continuance_deadline",
    "co_defendant_conflict_note",
}

STRATEGY_CHOICES = {
    "missing_evidence_log_entry": "extractive",
    "hearing_continuance_deadline": "extractive",
    "co_defendant_conflict_note": "extractive",
}

PART1_JUSTIFICATION = (
    "All three flagged candidates -- the missing evidence log entry, the "
    "hearing continuance deadline, and the co-defendant conflict note -- "
    "are specific, structured facts (an exact log reference, an exact "
    "date, an exact named conflict) where paraphrase risks changing or "
    "blurring the fact itself, so extractive compression is used for all "
    "three, keeping their exact wording verbatim inside the 600-token "
    "target. All three are confirmed present in PRODUCED_SUMMARY_CONTENT "
    "before this compressed block moves into Part 2 as a single content "
    "block for ordering."
)

# ---------------------------------------------------------------------------
# PART 2 -- CONTEXT ORDERING (this chapter's own new skill)
# ---------------------------------------------------------------------------
# The final assembled pre-hearing-brief window combines Part 1's
# compressed summary with several other already-selected content
# blocks. Every block below is already correctly included (Chapters
# 1-5's own gates already passed) -- this project's Part 2 job is
# deciding WHERE each one goes, exactly as this chapter's own Context
# Ordering Recipe describes.
CONTENT_BLOCKS = {
    "pinned_flight_risk_safety_note": {"weight": "high", "tokens": 80},
    "part1_compressed_summary": {"weight": "high", "tokens": 600},
    "recalled_prior_ruling": {"weight": "low", "tokens": 150},
    "verbatim_window_this_session": {"weight": "low", "tokens": 1_800},
    "routine_administrative_note": {"weight": "low", "tokens": 100},
    "the_query_todays_ask": {"weight": "query", "tokens": 120},
}
POSITION_OPTIONS = {"start_anchor_region", "end_anchor_query_position", "middle"}

# YOUR DESIGN -- Part 2: a position from POSITION_OPTIONS for every block
# key above. The query is fixed by definition at the end anchor nearest
# generation (Step 4); every high-weight, non-query block belongs at the
# start anchor region (Step 2); every low-weight block belongs in the
# middle (Step 3), deliberately, not left to arrival order.
BLOCK_POSITIONS = {
    "pinned_flight_risk_safety_note": "start_anchor_region",
    "part1_compressed_summary": "start_anchor_region",
    "recalled_prior_ruling": "middle",
    "verbatim_window_this_session": "middle",
    "routine_administrative_note": "middle",
    "the_query_todays_ask": "end_anchor_query_position",
}

PART2_JUSTIFICATION = (
    "The pinned flight-risk safety note and Part 1's compressed summary "
    "(which carries all three load-bearing candidates -- the missing "
    "evidence log entry, the continuance deadline, and the conflict "
    "note) are both high-weight per Step 1, so both are placed in the "
    "start anchor region per Step 2, rather than left wherever they "
    "happened to arrive. The query -- today's actual ask -- is placed "
    "at the end anchor nearest generation per Step 4, not buried after "
    "a long undifferentiated block. The recalled prior ruling, the full "
    "verbatim window, and the routine administrative note are all "
    "low-weight and are deliberately placed in the middle per Step 3 -- "
    "not because they don't matter at all, but because the content that "
    "can least afford positional unreliability (the two high-weight "
    "blocks and the active query) has already claimed both anchors, and "
    "the middle is exactly where lower-weight content can safely absorb "
    "that risk instead."
)


# ===========================================================================
# Structural + internal-consistency self-check -- identical to starter.py.
# This plays the role of Chapter 6's own Step 5 positional probe: it
# verifies your placements obey the weight/anchor rules directly, since a
# real live-model probe is exactly what this project's own design
# decisions determine the outcome of.
# ===========================================================================

def check_part1_candidates():
    errors = []
    if not isinstance(PRODUCED_SUMMARY_CONTENT, set):
        errors.append("PRODUCED_SUMMARY_CONTENT must be a set of candidate keys.")
        return errors
    missing = CANDIDATE_DETAILS - PRODUCED_SUMMARY_CONTENT
    if missing:
        errors.append(f"These flagged candidates are missing from PRODUCED_SUMMARY_CONTENT: {sorted(missing)}")
    unknown = PRODUCED_SUMMARY_CONTENT - CANDIDATE_DETAILS
    if unknown:
        errors.append(f"PRODUCED_SUMMARY_CONTENT contains unknown candidate keys: {sorted(unknown)}")
    return errors


def check_part1_strategy():
    errors = []
    if not isinstance(STRATEGY_CHOICES, dict):
        errors.append("STRATEGY_CHOICES must be a dict mapping every candidate to a strategy.")
        return errors
    missing_keys = CANDIDATE_DETAILS - set(STRATEGY_CHOICES.keys())
    if missing_keys:
        errors.append(f"STRATEGY_CHOICES is missing entries for: {sorted(missing_keys)}")
    invalid = {k: v for k, v in STRATEGY_CHOICES.items() if v not in STRATEGY_OPTIONS}
    if invalid:
        errors.append(f"STRATEGY_CHOICES has invalid strategy values: {invalid}")
    # All three given candidates are specific, structured facts where exact
    # wording matters -- extractive is the only correct choice for all three.
    wrong = {k: v for k, v in STRATEGY_CHOICES.items() if k in CANDIDATE_DETAILS and v != "extractive"}
    if wrong:
        errors.append(f"These candidates require extractive compression (exact wording matters): {sorted(wrong)}")
    return errors


def check_part2_anchor_assignment():
    errors = []
    if not isinstance(BLOCK_POSITIONS, dict):
        errors.append("BLOCK_POSITIONS must be a dict mapping every block key to a position.")
        return errors

    missing_keys = set(CONTENT_BLOCKS.keys()) - set(BLOCK_POSITIONS.keys())
    if missing_keys:
        errors.append(f"BLOCK_POSITIONS is missing entries for: {sorted(missing_keys)}")

    invalid = {k: v for k, v in BLOCK_POSITIONS.items() if v not in POSITION_OPTIONS}
    if invalid:
        errors.append(f"BLOCK_POSITIONS has invalid position values: {invalid}")

    # The query must sit at the end anchor position -- fixed by Step 4.
    query_pos = BLOCK_POSITIONS.get("the_query_todays_ask")
    if query_pos != "end_anchor_query_position":
        errors.append("the_query_todays_ask MUST be placed at end_anchor_query_position.")

    # Every high-weight, non-query block MUST be at the start anchor region.
    high_weight_blocks = {
        k for k, v in CONTENT_BLOCKS.items()
        if v["weight"] == "high"
    }
    misplaced_high = {
        k for k in high_weight_blocks
        if BLOCK_POSITIONS.get(k) != "start_anchor_region"
    }
    if misplaced_high:
        errors.append(f"These high-weight blocks MUST be at start_anchor_region: {sorted(misplaced_high)}")

    return errors


def check_part2_middle_placement():
    errors = []
    if not isinstance(BLOCK_POSITIONS, dict):
        return errors  # already reported above

    # Low-weight blocks must NOT occupy an anchor position -- anchors are
    # reserved for the highest-weight content and the active query.
    low_weight_blocks = {
        k for k, v in CONTENT_BLOCKS.items()
        if v["weight"] == "low"
    }
    wrongly_anchored = {
        k for k in low_weight_blocks
        if BLOCK_POSITIONS.get(k) in {"start_anchor_region", "end_anchor_query_position"}
    }
    if wrongly_anchored:
        errors.append(f"These low-weight blocks must NOT occupy an anchor position: {sorted(wrongly_anchored)}")

    return errors


def check_window_budget():
    errors = []
    total = sum(v["tokens"] for v in CONTENT_BLOCKS.values())
    if total > WINDOW_BUDGET_TOKENS:
        errors.append(
            f"Assembled window total ({total} tokens) exceeds the "
            f"{WINDOW_BUDGET_TOKENS}-token budget by {total - WINDOW_BUDGET_TOKENS} tokens."
        )
    return errors


def check_writeups():
    errors = []
    if len(PART1_JUSTIFICATION.strip()) < 40:
        errors.append("PART1_JUSTIFICATION should be a real 2-4 sentence explanation (40+ characters)")
    if len(PART2_JUSTIFICATION.strip()) < 40:
        errors.append("PART2_JUSTIFICATION should be a real 2-4 sentence explanation (40+ characters)")
    return errors


def main():
    print("Module 3 Project -- Self-Check (reference solution)")
    print("=" * 60)
    p1_candidate_errors = check_part1_candidates()
    p1_strategy_errors = check_part1_strategy()
    p2_anchor_errors = check_part2_anchor_assignment()
    p2_middle_errors = check_part2_middle_placement()
    budget_errors = check_window_budget()
    writeup_errors = check_writeups()
    all_errors = (
        p1_candidate_errors + p1_strategy_errors + p2_anchor_errors
        + p2_middle_errors + budget_errors + writeup_errors
    )

    total_tokens = sum(v["tokens"] for v in CONTENT_BLOCKS.values())
    print("-- Part 1: Compression Fidelity (Chapter 5's own skill) --")
    print(f"Candidates preserved: {sorted(PRODUCED_SUMMARY_CONTENT)}")
    print(f"Strategy choices: {STRATEGY_CHOICES}")
    print("-- Part 2: Context Ordering (this chapter's own skill) --")
    for block, pos in BLOCK_POSITIONS.items():
        print(f"  {block} ({CONTENT_BLOCKS[block]['weight']}, {CONTENT_BLOCKS[block]['tokens']}t) -> {pos}")
    print(f"Assembled window total: {total_tokens} / {WINDOW_BUDGET_TOKENS} tokens")

    if not all_errors:
        print("\nPASS -- Part 1's candidates and strategy are correct, and Part 2's anchor")
        print("assignment and middle placement obey every weight/position rule, with the")
        print("assembled window fitting its budget.")
        print("Now compare your reasoning (not just structure) against solution.py, and")
        print("check your work against RUBRIC.md before considering this project done.")
    else:
        print(f"\n{len(all_errors)} issue(s) found:")
        for e in all_errors:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
