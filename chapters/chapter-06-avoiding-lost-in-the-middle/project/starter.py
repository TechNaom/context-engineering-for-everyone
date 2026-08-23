"""
Module 3 Project: Build Brackholt County Court Records Office's
ArchiveLine Compression + Ordering Pipeline

Brackholt County Court Records Office is a fictional court records
office. Its docket-review assistant, ArchiveLine, helps a public
defender review an active case file before a hearing -- assembling a
pre-hearing brief from this session's own long conversation plus
already-selected reference content. This is Module 3's own closing
project, drawing on BOTH chapters this module built: Chapter 5's
Compression Fidelity Recipe (Part 1) and this chapter's own Context
Ordering Recipe (Part 2) -- not just this chapter's material in
isolation, per the curriculum map's own Module 3 labs ("build a
summarization pipeline that preserves load-bearing facts; reorder a
context window to fix a lost-in-the-middle failure").

A note on this project's tier: the curriculum map's own four-tier
project ladder (L1 after Ch. 2, L2 after Ch. 4, L3 after Ch. 8, L4 the
Ch. 13 capstone) does not assign a numbered tier to Module 3 -- it
jumps directly from L2 (Ch. 4) to L3 (Ch. 8). This project is the
course's own separate "one project per module" convention (confirmed in
Chapter 4's session) filling that gap, not a claim to be the literal L3
tier early. See `quality-audits/chapter-06-audit.md` for the full
reasoning. In scaffold terms it sits between L2's partial scaffold and
L3's no-scaffold: a full spec is given, like L2, but you design both
halves (compression AND ordering) together with no part solved for you.

THE SYSTEM
----------
An aged-out 3,000-token segment of this session's own docket-review
conversation must compress to a fixed 600-token target (Chapter 5's own
skill). The compressed result then becomes one content block inside a
larger, already-assembled 3,200-token-budget pre-hearing-brief window,
alongside several other already-correctly-included blocks -- and this
chapter's own skill (Part 2) decides where each block belongs.

PART 1 -- COMPRESSION FIDELITY (Chapter 5's own skill, reused here)
--------------------------------------------------------------------
  Raw segment (fixed, given):            3,000 tokens
  Compression target (fixed, given):       600 tokens
  3 load-bearing candidates already flagged (Chapter 5's own Step 2) --
  see CANDIDATE_DETAILS below. All three must survive compression.

PART 2 -- CONTEXT ORDERING (this chapter's own new skill)
--------------------------------------------------------------------
  Assembled window budget (fixed, given): 3,200 tokens
  6 content blocks, each already correctly selected (Chapters 1-5's own
  gates already passed) -- see CONTENT_BLOCKS below. Each is tagged
  "high" weight, "low" weight, or "query" (there is exactly one query
  block). The query MUST sit at end_anchor_query_position (Step 4).
  Every "high" weight block MUST sit at start_anchor_region (Step 2).
  Every "low" weight block must NOT occupy either anchor position
  (Step 3 -- the middle is exactly where lower-weight content belongs).

YOUR TASK
---------
1. Fill in PRODUCED_SUMMARY_CONTENT (a set) and STRATEGY_CHOICES (a
   dict) for Part 1: which candidates survive your compression, and
   which strategy (extractive/abstractive) you chose for each. All
   three given candidates are specific, structured facts -- decide for
   yourself whether that means extractive or abstractive is correct,
   and be prepared to defend it in PART1_JUSTIFICATION.
2. Fill in BLOCK_POSITIONS for Part 2: a position from POSITION_OPTIONS
   for every block in CONTENT_BLOCKS, obeying the anchor/middle rules
   above.
3. Fill in PART1_JUSTIFICATION and PART2_JUSTIFICATION: 2-4 real
   sentences each, defending your Part 1 and Part 2 choices separately.

Fill in every TODO, then run:

    python3 starter.py

to see a self-check. Like Chapter 4's own project, most of this one IS
mechanically checkable against your own numbers (candidate presence and
strategy correctness for Part 1; anchor/middle placement correctness
and budget fit for Part 2) -- only the QUALITY of your two write-ups is
open-ended. Compare your full reasoning against solution.py, then
self-grade against RUBRIC.md.
"""

COMPRESSION_TARGET_TOKENS = 600
WINDOW_BUDGET_TOKENS = 3_200

# ---------------------------------------------------------------------------
# PART 1 -- COMPRESSION FIDELITY
# ---------------------------------------------------------------------------
RAW_SEGMENT_TOKENS = 3_000
CANDIDATE_DETAILS = {
    "missing_evidence_log_entry",
    "hearing_continuance_deadline",
    "co_defendant_conflict_note",
}
STRATEGY_OPTIONS = {"extractive", "abstractive"}

# TODO (Part 1): which candidates survive in your compressed output.
PRODUCED_SUMMARY_CONTENT = {
    # TODO
}

# TODO (Part 1): a strategy from STRATEGY_OPTIONS for each candidate.
STRATEGY_CHOICES = {
    "missing_evidence_log_entry": None,  # TODO
    "hearing_continuance_deadline": None,  # TODO
    "co_defendant_conflict_note": None,  # TODO
}

# TODO: 2-4 sentences defending your Part 1 candidate/strategy choices.
PART1_JUSTIFICATION = ""

# ---------------------------------------------------------------------------
# PART 2 -- CONTEXT ORDERING
# ---------------------------------------------------------------------------
CONTENT_BLOCKS = {
    "pinned_flight_risk_safety_note": {"weight": "high", "tokens": 80},
    "part1_compressed_summary": {"weight": "high", "tokens": 600},
    "recalled_prior_ruling": {"weight": "low", "tokens": 150},
    "verbatim_window_this_session": {"weight": "low", "tokens": 1_800},
    "routine_administrative_note": {"weight": "low", "tokens": 100},
    "the_query_todays_ask": {"weight": "query", "tokens": 120},
}
POSITION_OPTIONS = {"start_anchor_region", "end_anchor_query_position", "middle"}

# TODO (Part 2): a position from POSITION_OPTIONS for every block key
# above.
BLOCK_POSITIONS = {
    "pinned_flight_risk_safety_note": None,  # TODO
    "part1_compressed_summary": None,  # TODO
    "recalled_prior_ruling": None,  # TODO
    "verbatim_window_this_session": None,  # TODO
    "routine_administrative_note": None,  # TODO
    "the_query_todays_ask": None,  # TODO
}

# TODO: 2-4 sentences defending your Part 2 placement choices.
PART2_JUSTIFICATION = ""


# ===========================================================================
# Structural + internal-consistency self-check -- do not need to edit
# anything below this line.
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

    query_pos = BLOCK_POSITIONS.get("the_query_todays_ask")
    if query_pos != "end_anchor_query_position":
        errors.append("the_query_todays_ask MUST be placed at end_anchor_query_position.")

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
        return errors

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
    print("Module 3 Project -- Self-Check")
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
        print("\nFix the issues above and re-run this file.")


if __name__ == "__main__":
    main()
