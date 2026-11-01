#!/usr/bin/env python3
"""Check that Challenge Edition's four trade evolutions work by level.

Run: python3 tools/check_challenge_evolutions.py
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "data/pokemon/evos_moves.asm").read_text(encoding="utf-8")
expected = {
    "Kadabra": (37, "ALAKAZAM"),
    "Machoke": (40, "MACHAMP"),
    "Graveler": (40, "GOLEM"),
    "Haunter": (38, "GENGAR"),
}
errors = []
for name, (level, target) in expected.items():
    match = re.search(
        rf"(?m)^{name}EvosMoves:\s*\n; Evolutions\s*\n(?P<entries>(?:[ \t]*db [^\n]*\n)+)",
        source,
    )
    if not match:
        errors.append(f"{name}: evolution block missing")
        continue
    entries = match.group("entries")
    wanted = f"db EVOLVE_LEVEL, {level}, {target}"
    if wanted not in entries:
        errors.append(f"{name}: expected {wanted}")
    if "EVOLVE_TRADE" in entries:
        errors.append(f"{name}: still requires trading")
if errors:
    print("FAILED: " + "; ".join(errors), file=sys.stderr)
    sys.exit(1)
print("PASS: all four former trade evolutions are available by level")
