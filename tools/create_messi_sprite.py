#!/usr/bin/env python3
"""Six 16x16 Messi overworld poses (front, back, side; each with walk frame).

Four Gen 1-compatible tones: cropped dark hair, full beard and jersey stripes.
Route 9 has its own sprite set so talking to the NPC never swaps his graphics.
"""
import struct
import zlib
from pathlib import Path

FRONT = [
"................",
".....#####......",
"....#MMMMM#.....",
"...#MlllllM#....",
"...#l#lll#l#....",
"...#lllllll#....",
"...#M#####M#....",
"....#MMMMM#.....",
"...##lllll##....",
"..#l#lMlMl#l#...",
"..#l#lllll#l#...",
"...##lMlMl##....",
".....#MMM#......",
".....#M#M#......",
"....##.#.##.....",
"....##...##.....",
]
BACK = [
"................",
".....#####......",
"....#MMMMM#.....",
"...#MMMMMMM#....",
"...#MMMMMMM#....",
"...#MMMMMMM#....",
"....#MMMMM#.....",
"....#MMMMM#.....",
"...##lllll##....",
"..#l#lMlMl#l#...",
"..#l#lllll#l#...",
"...##lMlMl##....",
".....#MMM#......",
".....#M#M#......",
"....##.#.##.....",
"....##...##.....",
]
SIDE = [
"................",
".....#####......",
"....#MMMMM#.....",
"...#Mlllll#.....",
"...#l#llll##....",
"...#lllllll#....",
"...#MM####l#....",
"....#MMMM##.....",
"....#lMMM#......",
"...##llll##.....",
"..#l#lMlMl#.....",
"..##.lMlMl#.....",
".....#MMM#......",
".....#M#M#......",
"....##.#.##.....",
"....##...##.....",
]
PALETTE = {".": 255, "l": 170, "M": 85, "#": 0}

def pose(rows, walking=False):
    image = rows.copy()
    if walking:
        image[13] = "....##M#M##....."
        image[14] = "...##..#..##...."
        image[15] = "...##.....##...."
    return image

def chunk(tag, data):
    return (struct.pack(">I", len(data)) + tag + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))

def main():
    frames = [pose(FRONT), pose(FRONT, True),
              pose(BACK), pose(BACK, True),
              pose(SIDE), pose(SIDE, True)]
    png_rows = bytearray()
    for i, frame in enumerate(frames):
        if len(frame) != 16:
            raise ValueError(f"Messi frame {i} is not 16 pixels high")
        for y, row in enumerate(frame):
            if len(row) != 16:
                raise ValueError(f"Messi frame {i} line {y} must have 16 pixels")
            png_rows.append(0)
            png_rows.extend(PALETTE[c] for c in row)
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", 16, 96, 8, 0, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(png_rows, 9))
           + chunk(b"IEND", b""))
    output = Path("gfx/sprites/messi.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(png)
    print("Generated", output, "(six 16x16 frames)")

if __name__ == "__main__":
    main()
