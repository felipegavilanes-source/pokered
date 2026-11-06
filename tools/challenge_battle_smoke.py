#!/usr/bin/env python3
"""Headless debug battle: assert that the player battle EXP bar actually renders."""
from pathlib import Path
from pyboy import PyBoy

rom = Path("pokeblue_debug.gbc")
sym = Path("pokeblue_debug.sym")
if not rom.exists() or not sym.exists():
    raise SystemExit("Missing debug ROM or symbols")
p = PyBoy(str(rom), symbols=str(sym), window="null", sound_emulated=False)
p.set_emulation_speed(0)
state = {"exp_draws": 0}

def exp_drawn(context):
    context["exp_draws"] += 1

def debug_menu_shown(context):
    context["debug_menu"] = True

state["debug_menu"] = False
p.hook_register(None, "DebugMenu", debug_menu_shown, state)
p.hook_register(None, "DrawBattleExpBar", exp_drawn, state)
try:
    p.tick(120)
    # Holding START+SELECT on the title enters the debug menu;
    # UP+SELECT+B would instead clear the save file.
    p.button_press("start")
    p.button_press("select")
    for _ in range(120):
        if state["debug_menu"]:
            break
        p.tick(30)
    p.button_release("start")
    p.button_release("select")
    if not state["debug_menu"]:
        raise SystemExit("FAIL: START+SELECT did not open the debug menu")
    p.tick(100)
    p.button("a")  # FIGHT is the first debug menu entry.
    for i in range(120):
        if state["exp_draws"]:
            break
        p.tick(60)
    p.tick(120)
    shot = Path("challenge-battle-smoke.png")
    p.screen.image.save(shot)
    print("EXP battle HUD draw calls:", state["exp_draws"])
    print("Screenshot:", shot)
    if not state["exp_draws"]:
        raise SystemExit("FAIL: EXP bar not reached during debug battle")
finally:
    p.stop()
