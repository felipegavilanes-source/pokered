#!/usr/bin/env python3
"""Build Agumon's six-frame 16x16 overworld sprite from the user-provided sheet.

The user supplied a 6-column sprite sheet on 2026-11-01. Frames are sampled
from its first two columns of front, back and side poses, reduced to 16x16,
mapped to four Game Boy shades, and lightly corrected at the top of the head.

The resulting exact palette pixels are embedded here (zlib/base64) so both
Linux and macOS GitHub Actions can reproduce the image without Pillow.
The frame order is: front, front walk, back, back walk, side, side walk.
"""
import base64
import hashlib
import struct
import zlib
from pathlib import Path

# 16x96 row-major palette indices: 0=white, 1=light, 2=dark, 3=black.
PIXELS_ZLIB_BASE64 = (
    "eNq1lFt2wzAIRGFm/3vuCBkJbCvtR4rjnIMewB0hm8kYZmlOlxUfw/V0QQ3oyQVyObasDUTfT8hKfOvpRjaUDR7rAc/pKEf/"
    "rD6Wr9B6x5PRNaN31yNf9ZZ8EBPY6/nA7y/8siO/v/Cv5V/n9yc/bvxo/PiFf+YrPFOPk48oX7+tz0MAzd/5j/kYaqyAUmPO"
    "o/EvQRR8FMR1Ah6KyMM+MWM/zzFvX+K35PfD/jnwZ37r/Nd1Kvzo/KoE0Q+rITwEqAWPUSsCvPCbHfqXkar0p8+MfnWop2Hn"
    "B0tHXwBg598ZUdWcDeq9nurH2W6xefs8qV9Yk1lcjRrPvOG+8+PBj3/jZ+cfl7Uej1XeLMi7Gty3L/gLL8aQd2Dk+h+8qQW7"
)
EXPECTED_SHA256 = "4628861514aa7db8e7cd6fa566232f22e74d26775a6cd4ffd45e111af3542b76"
PALETTE = (255, 170, 85, 0)

def chunk(kind, payload):
    return (struct.pack(">I", len(payload)) + kind + payload
            + struct.pack(">I", zlib.crc32(kind + payload) & 0xffffffff))

def main():
    indices = zlib.decompress(base64.b64decode(PIXELS_ZLIB_BASE64))
    if len(indices) != 16 * 96 or any(index > 3 for index in indices):
        raise ValueError("Agumon sprite must have six 16x16 four-shade frames")
    if hashlib.sha256(indices).hexdigest() != EXPECTED_SHA256:
        raise ValueError("Agumon sprite differs from the approved source sheet")
    raw = bytearray()
    for y in range(96):
        raw.append(0)  # PNG scanline filter None
        raw.extend(PALETTE[i] for i in indices[y * 16:(y + 1) * 16])
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", 16, 96, 8, 0, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))
    path = Path("gfx/sprites/agumon.png")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)
    print("Generated", path, "from user-supplied Agumon sprite sheet (six frames)")

if __name__ == "__main__":
    main()
