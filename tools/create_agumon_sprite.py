#!/usr/bin/env python3
"""Generate a 16x96, four-shade Game Boy overworld sprite for Agumon.
Six 16x16 frames: down x2, up x2, sideways x2.
No external Python packages required.
"""
import struct
import zlib
from pathlib import Path

FRONT = [
"................",".....###........","...##...##......","..#.......#.....",
".#.........#....",".#....##....#...","#.....##.....#..","#............#..",
"#...##.......#..",".#..##......#...","..#......###....",
"...##....#..#...","....#....#..#...","....#....#..#...",
"...##....####...","................",
]
BACK = [
"................",".....######.....","...##......##...","..#..........#..",
".#............#.",".#............#.","#..............#","#..............#",
"#..............#",".#............#.","..#..........#..",
"...#........#...","....#......#....","...##......##...",
"...##......##...","................",
]
SIDE = [
"................","......###.......","....##...##.....","...#.......##...",
"..#..........#..","..#...##......#.","..#...##......#.",
"..#...........#.","...#....##....#.","....#...##...#..",
".....##.....#...",".....#.....##...",".....#.....#....",
"....##....##....","....##....##....","................",
]

def chunk(kind, payload):
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xffffffff)

def main():
    rows = []
    for frame in (FRONT, FRONT, BACK, BACK, SIDE, SIDE):
        for y, line in enumerate(frame):
            pixels = [3 if ch == "#" else 0 for ch in line]
            if frame is FRONT and y == 6:
                pixels[7] = pixels[8] = 0
            rows.append(bytes([0] + pixels))
    raw = b"".join(rows)
    png = (b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", 16, 96, 8, 0, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b""))
    path = Path("gfx/sprites/agumon.png")
    path.write_bytes(png)
    print("Generated", path)

if __name__ == "__main__":
    main()
