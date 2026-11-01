#!/usr/bin/env python3
"""Regression checks for Challenge Edition's custom overworld and trainer graphics.

Run after "make": no external packages or emulator required.
"""
from pathlib import Path
import re
import hashlib
import struct
import zlib

ROOT = Path(__file__).resolve().parent.parent
PORTRAITS = {
    "CHIEF": ("neymar", "NeymarPic"),
    "GIOVANNI": ("trump", "TrumpPic"),
    "BLAINE": ("xi_jinping", "XiJinpingPic"),
    "MESSI": ("messi", "MessiPic"),
    "CR7": ("cr7", "CR7Pic"),
    "ELON_MUSK": ("elon_musk", "ElonMuskPic"),
    "JEFF_BEZOS": ("jeff_bezos", "JeffBezosPic"),
    "BILL_GATES": ("bill_gates", "BillGatesPic"),
    "STEVE_JOBS": ("steve_jobs", "SteveJobsPic"),
    "KIM_JONG_UN": ("kim_jong_un", "KimJongUnPic"),
    "MADURO": ("maduro", "MaduroPic"),
    "CHE_GUEVARA": ("che_guevara", "CheGuevaraPic"),
    "PUTIN": ("putin", "PutinPic"),
}
DMG_SHADES = {0, 85, 170, 255}


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def check_png(path, width, height):
    payload = (ROOT / path).read_bytes()
    assert payload.startswith(b"\x89PNG\r\n\x1a\n"), f"{path}: PNG signature invalid"
    offset = 8
    compressed = bytearray()
    dimensions = None
    while offset < len(payload):
        assert offset + 12 <= len(payload), f"{path}: truncated PNG chunk"
        size = int.from_bytes(payload[offset:offset + 4], "big")
        kind = payload[offset + 4:offset + 8]
        end = offset + 12 + size
        assert end <= len(payload), f"{path}: truncated {kind!r}"
        data = payload[offset + 8:offset + 8 + size]
        expected_crc = int.from_bytes(payload[offset + 8 + size:end], "big")
        assert zlib.crc32(kind + data) & 0xffffffff == expected_crc, f"{path}: bad CRC"
        if kind == b"IHDR":
            dimensions = struct.unpack(">IIBBBBB", data)
        elif kind == b"IDAT":
            compressed.extend(data)
        elif kind == b"IEND":
            break
        offset = end
    assert dimensions == (width, height, 8, 0, 0, 0, 0), (
        f"{path}: expected {width}x{height} 8-bit grayscale, got {dimensions}"
    )
    raw = zlib.decompress(compressed)
    assert len(raw) == (width + 1) * height, f"{path}: bad pixel data size"
    for row in range(height):
        offset = row * (width + 1)
        assert raw[offset] == 0, f"{path}: unsupported PNG filter"
        assert set(raw[offset + 1:offset + width + 1]) <= DMG_SHADES, (
            f"{path}: colors outside four Game Boy shades"
        )


def main():
    # Outdoor cities use fixed 11-slot sprite lists. Pallet needs its own slot.
    sets = read("data/maps/sprite_sets.asm")
    const = read("constants/sprite_set_constants.asm")
    objects = read("data/maps/objects/PalletTown.asm")
    pointers = read("data/sprites/sprites.asm")
    assert "const SPRITESET_PALLET_AGUMON" in const
    assert re.search(r"db SPRITESET_PALLET_AGUMON\s*;\s*PALLET_TOWN", sets)
    own_set = re.split(r"(?m)^; SPRITESET_", sets.split("; SPRITESET_PALLET_AGUMON (", 1)[1], maxsplit=1)[0]
    entries = re.findall(r"^\s*db\s+(SPRITE_\w+)", own_set, re.M)
    assert len(entries) == 11, f"Pallet set must have 11 sprites; got {len(entries)}"
    assert entries[5] == "SPRITE_UNUSED_SCIENTIST", "Agumon needs a dedicated VRAM slot"
    assert "SPRITE_UNUSED_SCIENTIST, STAY, DOWN, TEXT_PALLETTOWN_AGUMON" in objects
    assert "overworld_sprite AgumonSprite, 12" in pointers

    check_png("gfx/sprites/agumon.png", 16, 96)  # six 16x16 frames
    # The artwork is sampled from the user-provided six-pose sprite sheet.
    from create_agumon_sprite import PIXELS_ZLIB_BASE64, EXPECTED_SHA256
    import base64
    pixels = zlib.decompress(base64.b64decode(PIXELS_ZLIB_BASE64))
    assert len(pixels) == 16 * 96
    assert hashlib.sha256(pixels).hexdigest() == EXPECTED_SHA256
    assert set(pixels) == {0, 1, 2, 3}
    frames = [pixels[i * 256:(i + 1) * 256] for i in range(6)]
    assert len(set(frames)) == 6, "Each Agumon walk/direction pose must be distinct"
    assert "AgumonSprite::" in read("gfx/sprites.asm")

    assert (ROOT / "gfx/sprites/agumon.2bpp").stat().st_size == 24 * 16, (
        "Agumon's complete six frames must occupy 24 Game Boy tiles"
    )

    # Neymar and Messi use stock overworld graphics; battle portraits stay custom.
    forest = read("data/maps/objects/ViridianForest.asm")
    route9 = read("data/maps/objects/Route9.asm")
    route15 = read("data/maps/objects/Route15.asm")
    sprite_constants = read("constants/sprite_constants.asm")
    sprite_gfx = read("gfx/sprites.asm")
    linker = read("layout.link")
    generator = read("tools/generate_football_trainer.py")
    map_sets = read("data/maps/sprite_sets.asm")
    set_constants = read("constants/sprite_set_constants.asm")
    assert "SPRITE_YOUNGSTER, STAY, LEFT, TEXT_VIRIDIANFOREST_YOUNGSTER4, OPP_CHIEF" in forest
    assert "SPRITE_COOLTRAINER_M, STAY, LEFT, TEXT_ROUTE9_COOLTRAINER_M1, OPP_MESSI" in route9
    assert "db SPRITESET_PEWTER_CERULEAN ; ROUTE_9" in map_sets
    assert "return neymar_portrait()" in generator
    assert "return messi_portrait()" in generator
    assert "from cr7_reference import cr7_portrait" in generator
    assert "return cr7_portrait()" in generator
    assert "from trump_reference import trump_portrait" in generator
    assert "return trump_portrait()" in generator
    from trump_reference import trump_portrait
    trump_pixels = trump_portrait()
    assert len(trump_pixels) == 56 and all(len(row) == 56 for row in trump_pixels)
    assert set(value for row in trump_pixels for value in row) == {0, 1, 2, 3}
    assert hashlib.sha256(bytes(v for row in trump_pixels for v in row)).hexdigest() == (
        "5bcfe140ed2c063cc68819001a0536e30954e05a43ac1f02922bcc21a3b2f9a2"
    ), "Trump battle portrait must match the approved pointing pose"

    assert "pic_money TrumpPic,        9900" in read("data/trainers/pic_pointers_money.asm")

    from cr7_reference import cr7_portrait
    cr7_pixels = cr7_portrait()
    assert len(cr7_pixels) == 56 and all(len(row) == 56 for row in cr7_pixels)
    assert set(value for row in cr7_pixels for value in row) == {0, 1, 2, 3}


    # CR7 now uses the original Cooltrainer M NPC and Route 15 sprite set.
    assert "SPRITE_COOLTRAINER_M, STAY, UP, TEXT_ROUTE15_COOLTRAINER_M1, OPP_CR7" in route15
    assert "SPRITESET_SILENCE_BRIDGE  ; SPLITSET_ROUTE_15" in map_sets
    assert "SPRITESET_ROUTE15_CR7" not in set_constants
    assert "DEF SPRITE_CR7" not in sprite_constants
    assert "overworld_sprite GuardSprite, 12" in pointers
    assert "CR7Sprite::" not in sprite_gfx
    # The battle portrait remains CR7Pic and is tested with the other trainers.

    # Each custom trainer uses the correct portrait pointer and graphics bank.
    pictures = read("gfx/pics.asm")
    money = read("data/trainers/pic_pointers_money.asm")
    constants = read("constants/trainer_constants.asm")
    loader = read("engine/battle/core.asm")
    assert 'SECTION "Challenge Trainer Pics", ROMX' in pictures
    assert 'BANK("Challenge Trainer Pics")' in loader
    for trainer_class in ("CHIEF", "GIOVANNI", "BLAINE", "MESSI"):
        assert f"cp {trainer_class}" in loader, f"{trainer_class}: bank dispatch missing"
    classes = re.findall(r"^\s*trainer_const\s+(\w+)", constants, re.M)
    pic_entries = re.findall(r"^\s*pic_money\s+(\w+)\s*,", money, re.M)
    assert len(pic_entries) == len(classes) - 1, (
        f"Trainer picture pointers {len(pic_entries)} != trainer classes {len(classes) - 1}"
    )
    for trainer_class, (stem, symbol) in PORTRAITS.items():
        assert trainer_class in classes, f"{trainer_class}: trainer class missing"
        assert pic_entries[classes.index(trainer_class) - 1] == symbol, (
            f"{trainer_class}: wrong portrait pointer"
        )
        assert f'{symbol}:: INCBIN "gfx/trainers/{stem}.pic"' in pictures
        check_png(f"gfx/trainers/{stem}.png", 56, 56)
        assert (ROOT / f"gfx/trainers/{stem}.pic").stat().st_size > 0

    print("OK: Pallet Town Agumon sprite set, 6 animation frames, "
          "13 custom trainer portraits, Neymar/Messi overworld, Route 9 graphics, trainer class pointers and picture banks.")


if __name__ == "__main__":
    main()
