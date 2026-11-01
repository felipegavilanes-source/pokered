#!/usr/bin/env python3
"""Messi six-pose Game Boy overworld art adapted from approved pixel sheet.
16x96 grayscale PNG, 4 colors, original PNG generation without Pillow.
"""
import base64
import struct
import zlib
from pathlib import Path
PIXELS = "eNqlU4tuAzEIw+b//3mQqgt2T8m0ntpKJNTgx0U8PZmpNUm5BmZHEnWwa6APpOasg5k0/DmQNSF2QxZAIHKP5/r8wldRA8b969GNdbwtcBHA4HIJMO+Vv+vT91TAOpj0VYDaFUPwal7fzXfJIQLbuJJM/IlQNd4/f6N/9R/uP8Rvtv8KYP6n+Y+pT5Hpv6v/UP+zWsz/AajyBPmd/3HxvwOv/aQBQgTljG/z7wOxcw5ErkRQ91P/Ba+jovkNDcQD/TzST8s7Nd+1gOlj9Onp0xLyur4UONQFZwehgboG/B/848ifZ/4eyKC9bxf+H/LB8M7x3mn4AdGyA74="
COLORS = (255, 170, 85, 0)
def chunk(tag, data):
    return struct.pack(">I",len(data)) + tag + data + struct.pack(">I",zlib.crc32(tag+data)&0xffffffff)
def main():
    indices = zlib.decompress(base64.b64decode(PIXELS))
    assert len(indices) == 16 * 96
    assert set(indices) <= {0,1,2,3}
    scanlines = b"".join(b"\x00"+bytes(COLORS[v] for v in indices[y*16:(y+1)*16]) for y in range(96))
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR",struct.pack(">IIBBBBB",16,96,8,0,0,0,0)) + chunk(b"IDAT",zlib.compress(scanlines,9)) + chunk(b"IEND",b"")
    dest = Path("gfx/sprites/messi.png")
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(png)
    print("Generated",dest)
if __name__ == "__main__":
    main()
