#!/usr/bin/env python3
"""Generate a recognizable four-shade Agumon-inspired 16x16 overworld sprite.
Gen 1 stores six 16x16 poses (down, up, side; two frames each) in a 16x96 PNG.
"""
import struct
import zlib
from pathlib import Path

# Pixel art: . transparent/white, o light orange, O mid orange, # outline.
# Four shades are mapped to Game Boy DMG palette.
FRONT = [
"................",
".....######.....",
"...##OOOOOO##...",
"..#OOooooooOO#..",
".#OOooOOOOooOO#.",
".#OO#OooooO#OO#.",
"#OOO#oooooo#OOO#",
"#OOOoo#oo#ooOOO#",
"#OOOooo##oooOOO#",
".#OOoo####ooOO#.",
"..#OOooOOooOO#..",
"...##OOOOOO##...",
"..#OO#OOOO#OO#..",
"..#OO#....#OO#..",
"...##......##...",
"................",
]
BACK = [
"................",
".....######.....",
"...##OOOOOO##...",
"..#OOOOOOOOOO#..",
".#OOOOOOOOOOOO#.",
".#OOOOOOOOOOOO#.",
"#OOOOOOOOOOOOOO#",
"#OOOOOOOOOOOOOO#",
"#OOOOOOOOOOOOOO#",
".#OOOooooooOOO#.",
"..#OOooooooOO#..",
"...##OOOOOO##...",
"..#OO#OOOO#OO#..",
"..#OO#....#OO#..",
"...##......##...",
"................",
]
SIDE = [
"................",
"......#####.....",
"....##OOOOO##...",
"...#OOOOOOOO#...",
"..#OOOooooOO##..",
".#OOO#oooo#OOO#.",
".#OOO#oooooOOO#.",
".#OOOoooo##OOO#.",
"..#OOOooo#OOO#..",
"...#OOOooOO##...",
"....##OOOO##....",
"...#OO#OO#OO#...",
"..#OO#....#OO#..",
"..#OO#....#OO#..",
"...##......##...",
"................",
]
PALETTE = {".": 255, "o": 170, "O": 85, "#": 0}

def make_frame(base, walking=False):
    rows = [list(row) for row in base]
    if walking:
        # Alternate legs for an unmistakable two-frame walking cycle.
        for y in (12, 13, 14):
            rows[y][3], rows[y][4] = rows[y][4], rows[y][3]
            rows[y][11], rows[y][12] = rows[y][12], rows[y][11]
        rows[14][4] = "O"
        rows[14][11] = "O"
    return rows

def chunk(kind, data):
    return (struct.pack(">I", len(data)) + kind + data +
            struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff))

def main():
    frames = [make_frame(FRONT), make_frame(FRONT, True),
              make_frame(BACK), make_frame(BACK, True),
              make_frame(SIDE), make_frame(SIDE, True)]
    raw = bytearray()
    for frame in frames:
        for row in frame:
            if len(row) != 16:
                raise ValueError("Each sprite row must be 16 pixels")
            raw.append(0)  # PNG filter type 0
            raw.extend(PALETTE[c] for c in row)
    ihdr = struct.pack(">IIBBBBB", 16, 96, 8, 0, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) +
           chunk(b"IDAT", zlib.compress(bytes(raw), 9)) +
           chunk(b"IEND", b""))
    output = Path("gfx/sprites/agumon.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(png)
    print("Generated", output)

if __name__ == "__main__":
    main()
