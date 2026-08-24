"""
Chapter 13 Project -- SOLUTION entry point.

Unlike every prior chapter's `exercises/solution.py` or
`practice/solution.py`, this file's job isn't to hold the reference
response itself -- the L4 "Architecture Challenge" tier's real
deliverable is a written design document
(`solution/SOLUTION_DESIGN_DOCUMENT.md`), not a Python script, per this
chapter's own artifact-shape decision (see `../../quality-audits/
chapter-13-audit.md`'s "L4 artifact-shape decision" section for the full
reasoning, following `ai-engineering-for-everyone` Chapter 13's own
precedent). This file just runs this chapter's structural self-check
against that reference document and confirms it passes -- the same
sanity-check role `solution.py` plays in every other chapter, adapted to
a written-document deliverable.
"""

from self_check import run_self_check

if __name__ == "__main__":
    ok = run_self_check("solution/SOLUTION_DESIGN_DOCUMENT.md")
    print()
    if ok:
        print("solution.py: PASS -- the reference design document passes the full structural self-check.")
    else:
        print("solution.py: FAIL -- the reference design document should never fail its own structural self-check.")
        raise SystemExit(1)
