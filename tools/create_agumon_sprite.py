#!/usr/bin/env python3
"""Draw six 16x16 overworld frames for Agumon in the four Game Boy shades.

The silhouettes are hand-pixeled: wide muzzle, reptile eyes, arms, biped feet,
and a visible tail in profile. The overworld expects six frames stacked to 16x96.
"""
import struct
import zlib
from pathlib import Path

# . = background (white); l = light body; m = shadow; # = dark outline.
FRONT = [
"................",
"....##....##....",
"...#ll####ll#...",
"..#llllllllll#..",
".#llllllmlllll#.",
".#ll#llllll#ll#.",
".#ll#llllll#ll#.",
"..#lllmllmlll#..",
"..#llllllllll#..",
"...#l#mmmm#l#...",
"..##llmmmmll##..",
".#l#llmmmmll#l#.",
".##..#llll#..##.",
".....#llll#.....",
"....##l##l##....",
"....###..###....",
]
BACK = [
"................",
"....##....##....",
"...#ll####ll#...",
"..#llllllllll#..",
".#llllllllllll#.",
".#llllmmmmllll#.",
".#lllmmmmmmlll#.",
"..#llmmmmmmll#..",
"...#llllllll#...",
"..##llmmmmll##..",
".#l#llmmmmll#l#.",
".##.#llllll#.##.",
".....#llll#.....",
".....#l##l#.....",
"....##l##l##....",
"....###..###....",
]
SIDE = [
"................",
".....##.........",
"....#ll####.....",
"...#lllllll##...",
"..#llllllllll##.",
"..#lll#llllllll#",
"..#lll#lllllll#.",
"..#lllllllllll#.",
"...#llmmm####l#.",
"...#lllllll###..",
".###llllll#.....",
"#ll#l#llll##....",
".##..#lllll#....",
".....#l#l#l#....",
"....##l#.##l#...",
"....###...###...",
]
PALETTE = {".": 255, "l": 170, "m": 85, "#": 0}

def frame(rows, walking):
    result = [list(row) for row in rows]
    if walking:
        # The head is stable; only arms / feet change during the step.
        if rows is SIDE:
            result[14] = list(".....##.###l#...")
            result[15] = list(".....##..####...")
        else:
            result[14] = list("...##l##.##l#...")
            result[15] = list("...###....####..")
    return result

def chunk(kind, data):
    return (struct.pack(">I", len(data)) + kind + data
            + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff))

def main():
    frames = [frame(FRONT, False), frame(FRONT, True),
              frame(BACK, False), frame(BACK, True),
              frame(SIDE, False), frame(SIDE, True)]
    raw = bytearray()
    for pose in frames:
        if len(pose) != 16:
            raise ValueError("Sprite frame must have 16 rows")
        for row in pose:
            if len(row) != 16:
                raise ValueError("Sprite row must have 16 pixels")
            raw.append(0)  # PNG filter type 0
            raw.extend(PALETTE[pixel] for pixel in row)
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", 16, 96, 8, 0, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))
    path = Path("gfx/sprites/agumon.png")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)
    print("Generated", path, "(six frames)")

if __name__ == "__main__":
    main()
