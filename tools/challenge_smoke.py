#!/usr/bin/env python3
"""Boot Pokemon Blue Challenge Edition in a headless emulator and visit the protagonist selector."""
from pathlib import Path
from pyboy import PyBoy

ROM = Path("pokeblue.gbc")
SYMBOLS = Path("pokeblue.sym")
SHOT = Path("challenge-selector-smoke.png")
if not ROM.exists() or not SYMBOLS.exists():
    raise SystemExit("Missing ROM or symbol file")
pyboy = PyBoy(str(ROM), window="null", symbols=str(SYMBOLS), sound_emulated=False)
pyboy.set_emulation_speed(0)
seen = {"selector": False, "exp": 0}

def on_selector(context):
    context["selector"] = True

def on_exp(context):
    context["exp"] += 1

pyboy.hook_register(None, "ChoosePlayerSprite", on_selector, seen)
pyboy.hook_register(None, "DrawBattleExpBar", on_exp, seen)
try:
    pyboy.tick(240)
    pyboy.button("start")
    pyboy.tick(50)
    pyboy.button("a")
    pyboy.tick(70)
    # Advance the dialogue. Exit as soon as the selector is reached.
    for n in range(1100):
        if seen["selector"]:
            break
        pyboy.button("a")
        pyboy.tick(12)
    if not seen["selector"]:
        pyboy.screen.image.save(SHOT)
        raise SystemExit("FAIL: intro did not reach the protagonist selector")
    # The routine begins with a white fade; capture the actual rendered menu.
    pyboy.button_release("a")
    pyboy.tick(120)
    pyboy.screen.image.save(SHOT)
    _, choice_addr = pyboy.symbol_lookup("wUnusedPlayerDataByte")
    print("Character selection screen:", SHOT)
    pyboy.button("down")  # Choose Blue (index 1).
    pyboy.tick(15)
    pyboy.button("a")
    pyboy.tick(90)
    choice = pyboy.memory[choice_addr]
    print("ROM:", pyboy.cartridge_title)
    print("Reached character selector:", seen["selector"])
    print("Selected character id (expect Blue=1):", choice)
    print("EXP bar draws:", seen["exp"])
    if choice != 1:
        raise SystemExit("FAIL: selector did not store Blue as character id 1")
finally:
    pyboy.stop()
