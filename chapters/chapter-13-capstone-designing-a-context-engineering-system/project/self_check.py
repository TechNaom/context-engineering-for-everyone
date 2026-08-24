"""
Chapter 13 Project: Structural self-check for a filled-in
DESIGN_DOCUMENT_TEMPLATE.md.

This is NOT a scored exercise in the way Chapters 1-12's own exercises
and practice banks were. The L4 "Architecture Challenge" project tier
gives a business problem only, with no scaffold -- most of what you
produce (the job-to-be-done sentences, the multi-step/agentic shape
assessment, and the six Chapter 3-4/5-6/7-8/9-11/12 plans per component)
is a real written design document that has to be graded qualitatively,
against RUBRIC.md, the same way a real architecture-review document
would be -- not by a script.

What THIS script checks, mechanically, because it genuinely can:
  1. Every required section header is present in your filled-in document
     (nothing silently deleted).
  2. Every `ledger`/`hard_limit` and `evaluation_gate` code block is
     present and parses as real Python (not left as a TODO placeholder).
  3. Each component's Context Budget Ledger (Chapter 1-2) is
     ARITHMETICALLY VALID: all five lines are non-negative integers,
     Line 5 (Working Space) is actually reserved (> 0), and the five
     lines sum to no more than the declared hard_limit -- the same
     validation Chapter 2's own Budget Allocation Recipe Step 5 performs.
  4. Each component's evaluation gate (Chapter 12) has real, in-range
     values: completeness_threshold and noise_ratio_max are floats in
     [0.0, 1.0], positional_check is a bool, and required_facts is a
     non-empty list of at least 3 items.

It does NOT grade whether your job-to-be-done sentence is well-written,
whether your multi-step/agentic assessment is correct, or whether your
Chapter 3-11 plans are any good -- that's RUBRIC.md's job, and a human
reader's (including your own, comparing against
solution/SOLUTION_DESIGN_DOCUMENT.md).

Usage:
    python3 self_check.py                                   # checks solution/SOLUTION_DESIGN_DOCUMENT.md
    python3 self_check.py path/to/your_filled_document.md    # checks your own file
"""

import ast
import re
import sys

REQUIRED_SECTIONS = [
    "1.1 Job-to-be-done", "1.2 Multi-step/agentic shape",
    "1.3 Context Budget Ledger", "1.4 Short-term memory plan",
    "1.5 Long-term memory plan", "1.6 Compression and ordering plan",
    "1.7 Source assembly and retrieval plan",
    "1.8 Tool context and multi-agent/isolation plan",
    "1.9 Context evaluation gate",
    "2.1 Job-to-be-done", "2.2 Multi-step/agentic shape",
    "2.3 Context Budget Ledger", "2.4 Short-term memory plan",
    "2.5 Long-term memory plan", "2.6 Compression and ordering plan",
    "2.7 Source assembly and retrieval plan",
    "2.8 Tool context and multi-agent/isolation plan",
    "2.9 Context evaluation gate",
    "3.1 Why these two components' recipe treatments diverge",
    "3.2 What would change each component's profile",
    "3.3 Shared infrastructure risk",
]

REQUIRED_LEDGER_KEYS = {
    "line1_system", "line2_grounding", "line3_history",
    "line4_memory", "line5_working_space",
}
REQUIRED_GATE_KEYS = {
    "required_facts", "completeness_threshold", "noise_ratio_max", "positional_check",
}


def extract_code_blocks(markdown_text):
    """Returns every fenced ```python ... ``` block's raw text, in order."""
    return re.findall(r"```python\n(.*?)```", markdown_text, re.S)


def parse_assignment(block_text, var_name):
    """Finds `var_name = <literal>` inside a code block and safely parses
    it as a Python literal. Returns None if not found or not a valid
    literal (a bare `None` placeholder is a valid literal -- that's fine,
    it just means the field isn't filled in yet)."""
    m = re.search(rf"{var_name}\s*=\s*([^\n]+(?:\n(?!\w+\s*=).*)*)", block_text, re.S)
    if not m:
        return None
    candidate = m.group(1).strip()
    # Trim trailing content that belongs to a later assignment in the
    # same block (parse_dict handles multi-line dict literals fully).
    try:
        return ast.literal_eval(candidate)
    except (ValueError, SyntaxError):
        # try to isolate just a `{...}` or scalar at the start
        m2 = re.match(r"(\{.*?\}|[-\d.]+|True|False|None|\"[^\"]*\")", candidate, re.S)
        if not m2:
            return None
        try:
            return ast.literal_eval(m2.group(1))
        except (ValueError, SyntaxError):
            return None


def check_sections_present(text):
    return [s for s in REQUIRED_SECTIONS if s not in text]


def validate_ledger(hard_limit, ledger):
    issues = []
    if hard_limit is None or not isinstance(hard_limit, int):
        issues.append("hard_limit missing or not an int")
        return issues
    if ledger is None:
        issues.append("ledger block missing or unparseable")
        return issues
    if set(ledger.keys()) != REQUIRED_LEDGER_KEYS:
        issues.append(f"ledger keys don't match the required set: {sorted(ledger.keys())}")
        return issues
    if any(v is None for v in ledger.values()):
        issues.append("ledger still has a None placeholder -- fill in every line")
        return issues
    if any(not isinstance(v, int) or v < 0 for v in ledger.values()):
        issues.append("every ledger line must be a non-negative int")
        return issues
    if ledger["line5_working_space"] <= 0:
        issues.append("Line 5 (Working Space) must be reserved (> 0) -- Ch. 2 Step 2")
    total = sum(ledger.values())
    if total > hard_limit:
        issues.append(f"ledger totals {total} tokens, over the declared hard_limit of {hard_limit}")
    return issues


def validate_gate(gate):
    issues = []
    if gate is None:
        issues.append("evaluation_gate block missing or unparseable")
        return issues
    if set(gate.keys()) != REQUIRED_GATE_KEYS:
        issues.append(f"evaluation_gate keys don't match the required set: {sorted(gate.keys())}")
        return issues
    if any(v is None for v in gate.values()):
        issues.append("evaluation_gate still has a None placeholder -- fill in every field")
        return issues
    rf = gate["required_facts"]
    if not isinstance(rf, list) or len(rf) < 3:
        issues.append("required_facts must be a list of at least 3 items")
    ct = gate["completeness_threshold"]
    if not isinstance(ct, (int, float)) or not (0.0 <= ct <= 1.0):
        issues.append("completeness_threshold must be a number in [0.0, 1.0]")
    nr = gate["noise_ratio_max"]
    if not isinstance(nr, (int, float)) or not (0.0 <= nr <= 1.0):
        issues.append("noise_ratio_max must be a number in [0.0, 1.0]")
    if not isinstance(gate["positional_check"], bool):
        issues.append("positional_check must be a bool")
    return issues


def check_component(code_blocks, component_index, label):
    """component_index: 0 for DispatchMind's pair of blocks, 1 for
    ComplianceLedger's."""
    ledger_block = code_blocks[component_index * 2] if len(code_blocks) > component_index * 2 else None
    gate_block = code_blocks[component_index * 2 + 1] if len(code_blocks) > component_index * 2 + 1 else None

    hard_limit = parse_assignment(ledger_block, "hard_limit") if ledger_block else None
    ledger = parse_assignment(ledger_block, "ledger") if ledger_block else None
    gate = parse_assignment(gate_block, "evaluation_gate") if gate_block else None

    ledger_issues = validate_ledger(hard_limit, ledger)
    gate_issues = validate_gate(gate)
    return ledger_issues, gate_issues, hard_limit, ledger, gate


def run_self_check(path):
    with open(path) as f:
        text = f.read()

    print(f"Chapter 13 Project -- Structural Self-Check for {path}")
    print("=" * 70)

    missing_sections = check_sections_present(text)
    if missing_sections:
        print(f"MISSING SECTIONS ({len(missing_sections)}):")
        for s in missing_sections:
            print(f"  - {s}")
    else:
        print(f"All {len(REQUIRED_SECTIONS)} required section headers present: PASS")

    code_blocks = extract_code_blocks(text)
    print(f"\nFound {len(code_blocks)} python code block(s) (expected at least 4: ledger+gate x2 components).")

    total_checks = 0
    total_pass = 0

    for idx, label in enumerate(["DispatchMind (Component 1)", "ComplianceLedger (Component 2)"]):
        ledger_issues, gate_issues, hard_limit, ledger, gate = check_component(code_blocks, idx, label)
        total_checks += 1
        issues = ledger_issues + gate_issues
        if not issues:
            total_pass += 1
            spare = hard_limit - sum(ledger.values())
            print(f"\n{label}: PASS")
            print(f"  ledger: {ledger} (hard_limit={hard_limit}, spare={spare})")
            print(f"  evaluation_gate: {gate}")
        else:
            print(f"\n{label}: FAIL")
            for issue in issues:
                print(f"  - {issue}")

    print("\n" + "=" * 70)
    sections_ok = len(missing_sections) == 0
    print(f"Sections: {'PASS' if sections_ok else 'FAIL'} ({len(REQUIRED_SECTIONS) - len(missing_sections)}/{len(REQUIRED_SECTIONS)})")
    print(f"Ledger + evaluation-gate arithmetic: {total_pass}/{total_checks} components correct")
    print("\nThis structural check covers what's objectively checkable. The rest of")
    print("this document -- the job-to-be-done sentences, the multi-step/agentic")
    print("assessments, and the eleven-recipe treatment plans per component -- needs")
    print("a real, qualitative read against RUBRIC.md. A perfect structural score")
    print("here is a necessary floor, not a passing grade on its own.")

    return sections_ok and total_pass == total_checks


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "solution/SOLUTION_DESIGN_DOCUMENT.md"
    ok = run_self_check(target)
    sys.exit(0 if ok else 1)
