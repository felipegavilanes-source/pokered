#!/usr/bin/env python3
"""Regression checks: original characters, three starters, harder battles."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

const = read("constants/pokemon_constants.asm")
for value in ("STARTER1 EQU MAGIKARP", "STARTER2 EQU TANGELA", "STARTER3 EQU ZUBAT"):
    assert value in const, value
assert "db SPLASH, TACKLE, NO_MOVE, NO_MOVE" in read("data/pokemon/base_stats/magikarp.asm")
for route, species in (("Route24", "BULBASAUR"), ("Route25", "CHARMANDER"), ("Route6", "SQUIRTLE")):
    assert species in read("data/wild/maps/" + route + ".asm")
oak = read("text/OaksLab.asm")
for species in ("MAGIKARP", "TANGELA", "ZUBAT"):
    assert species in oak
parties = read("data/trainers/parties.asm")
assert "BrockData:" in parties and "db $FF, 20, GEODUDE" in parties
assert "Rival1Data:" in parties and "db 5, TANGELA, 0" in parties and "db 5, ZUBAT, 0" in parties
assert "Rival2Data:" in parties and "Rival3Data:" in parties
engine = read("engine/battle/trainer_ai.asm")
assert "AIMoveChoiceModification5:" in engine and "Rival1AI:" in engine and "SabrinaAI:" in engine
classes = read("constants/trainer_constants.asm")
for name in ("MESSI", "CR7", "ELON_MUSK", "JEFF_BEZOS", "BILL_GATES", "STEVE_JOBS", "KIM_JONG_UN", "MADURO", "CHE_GUEVARA", "PUTIN"):
    assert "trainer_const " + name not in classes
    assert re.search(r"\\b" + name + r"\\b", read("data/trainers/ai_pointers.asm")) is None
names = read("data/trainers/names.asm")
assert 'li "GIOVANNI"' in names and 'li "BLAINE"' in names and 'li "CHIEF"' in names
assert "AgumonSprite" not in read("gfx/sprites.asm")
assert "Challenge Trainer Pics" not in read("gfx/pics.asm")
print("OK: original characters; custom starters and harder trainers/AI retained")
