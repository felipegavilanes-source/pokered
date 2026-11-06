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
state = {"exp_draws": 0, "exp_animations": 0}

def exp_drawn(context):
    context["exp_draws"] += 1

def exp_animated(context):
    context["exp_animations"] += 1

def debug_menu_shown(context):
    context["debug_menu"] = True

state["debug_menu"] = False
p.hook_register(None, "DebugMenu", debug_menu_shown, state)
p.hook_register(None, "DrawBattleExpBar", exp_drawn, state)
p.hook_register(None, "AnimateEXPBar", exp_animated, state)
try:
    p.tick(120)
    # Keep SELECT held while periodically pressing START. We may still be
    # inside the initial Nintendo/Game Freak intro when the test begins;
    # the title only detects a *new* START press in its input loop.
    p.button_press("select")
    for _ in range(220):
        if state["debug_menu"]:
            break
        p.button_press("start")
        p.tick(8)
        p.button_release("start")
        p.tick(18)
    p.button_release("select")
    if not state["debug_menu"]:
        p.screen.image.save("challenge-battle-smoke.png")
        raise SystemExit("FAIL: SELECT+START did not open the debug menu")
    p.tick(100)
    p.button("a")  # FIGHT is the first debug menu entry.
    p.tick(100)
    # The debug battle has a two-stage nickname prompt: first the
    # dialogue, then the YES/NO menu. Repeat B until battle begins.
    for _ in range(120):
        if state["exp_draws"]:
            break
        p.button("b")
        p.tick(60)
    p.tick(120)
    shot = Path("challenge-battle-smoke.png")
    p.screen.image.save(shot)
    print("EXP battle HUD draw calls:", state["exp_draws"])
    print("EXP tilemap window:", p.tilemap_window[10:18, 11])
    _, tilemap = p.symbol_lookup("wTileMap")
    print("EXP WRAM tiles:", [p.memory[tilemap + 11 * 20 + x] for x in range(10, 18)])
    print("Screenshot:", shot)
    if not state["exp_draws"]:
        raise SystemExit("FAIL: EXP bar not reached during debug battle")
    # Force the opponent to 1 HP and defeat it to verify EXP animation,
    # rather than only testing that the empty EXP bar can be rendered.
    _, enemy_hp = p.symbol_lookup("wEnemyMonHP")
    p.memory[enemy_hp] = 0
    p.memory[enemy_hp + 1] = 1
    for _ in range(250):
        if state["exp_animations"]:
            break
        p.button("a")
        p.tick(40)
    print("EXP gain animations:", state["exp_animations"])
    p.tick(120)
    p.screen.image.save("challenge-exp-gain-smoke.png")
    if not state["exp_animations"]:
        raise SystemExit("FAIL: EXP bar did not animate after knocking out a Pokemon")
finally:
    p.stop()
