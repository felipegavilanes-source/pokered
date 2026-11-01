#!/usr/bin/env python3
"""Draw a six-frame Neymar overworld sprite in the Pokémon Gen 1 format.

16 pixels wide, 96 pixels tall, four grayscale tones, two poses per direction.
The original screenshot mockup has a much larger character than Gen 1 permits;
this is its small-scale equivalent: high hair, beard, jersey and raised arms.
"""
from pathlib import Path
import struct
import zlib

FRONT = [
"......###.......",
".....#MM###.....",
"....##MMM##.....",
"....#lllll#.....",
"....#M#l#M#.....",
"....#lllll#.....",
".....#MMM#......",
"....##MMM##.....",
"..##.#lll#.##...",
"..#l##lll##l#...",
"..##.#lll#.##...",
".....#lMl#......",
".....#MMM#......",
".....#M#M#......",
".....#.#.#......",
"....##.###......",
]
BACK = [
"......###.......",
".....#MM###.....",
"....##MMM##.....",
"....#MMMMM#.....",
"....#MMMMM#.....",
"....#MMMMM#.....",
".....#MMM#......",
"....##lll##.....",
"..##.#lll#.##...",
"..#l##lMl##l#...",
"..##.#lll#.##...",
".....#lll#......",
".....#MMM#......",
".....#M#M#......",
".....#.#.#......",
"....##.###......",
]
SIDE = [
"......###.......",
".....#MM##......",
"....##MMM#......",
"....#llll##.....",
"....#Ml#ll#.....",
"....#llll##.....",
".....#MM##......",
".....#MM#.......",
"..##.#ll##......",
"..#l##lll#......",
"..##.#lll#......",
".....#lll#......",
".....#MMM#......",
".....#M#M#......",
".....#.#.#......",
"....##.###......",
]
PALETTE = {".": 255, "l": 170, "M": 85, "#": 0}

def pose(base, walking=False):
    rows = base.copy()
    if walking:
        # Keep head static, alternate legs during the walking animation.
        rows[13] = ".....#M#M#......"
        rows[14] = "....##..#.#....."
        rows[15] = "....##..###....."
    return rows

def chunk(tag, payload):
    return (struct.pack(">I", len(payload)) + tag + payload
            + struct.pack(">I", zlib.crc32(tag + payload) & 0xffffffff))

def main():
    frames = [pose(FRONT), pose(FRONT, True),
              pose(BACK), pose(BACK, True),
              pose(SIDE), pose(SIDE, True)]
    buf = bytearray()
    for index, frame in enumerate(frames):
        if len(frame) != 16:
            raise ValueError(f"Frame {index} is not 16 pixels high")
        for y, line in enumerate(frame):
            if len(line) != 16:
                raise ValueError(f"Frame {index}, row {y} is {len(line)} pixels wide")
            buf.append(0)
            buf.extend(PALETTE[ch] for ch in line)
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", 16, 96, 8, 0, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(buf, 9))
           + chunk(b"IEND", b""))
    path = Path("gfx/sprites/neymar.png")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)
    print("Generated", path)

if __name__ == "__main__":
    main()
