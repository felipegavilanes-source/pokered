"""Full-body Xi Jinping trainer portrait, custom-pixel-refined face, Game Boy DMG 56x56.
Four shades, reproducibly embedded as zlib-compressed palette indices.
"""
import base64
import zlib
PIXELS = "eNrNlksOAzEIQ2P7/nfuAElTzWxw2kWRRt3kFTCfZIx/MVzmUyzzMVwUQBdTGkUnVihcARmqAVLrD7wcU8r8ImAYcUoXlwkaXAgJZflCnH56GHVYmaDDoUoXP/C5qY4jZ4KlaJ/jdBMwrTYbKeNVB9rTEJXz+zpqOGi7i8RgpjfHADWD3fqBy0IVtckn1gK3uxXsFxyNMLd1io958EbihFMjQd45pa7oNebdXyNOPbjYTp3V+ZClt9EeYbK5CLO/ElZFKbexaV1mpxxP/a3cNA3WUuK8N+lxpan6ZUhdNDtT/oIRMDvA5LJXw631comsTjjuYexzKq4C9fxhczBk0ebkcByuvw8xJsemu73A1pLqXe18j3iNQ+cSrOFZB7mGyX8d4+y5/HN7AfP8BlE="
def xi_jinping_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y*56:(y+1)*56]) for y in range(56)]
