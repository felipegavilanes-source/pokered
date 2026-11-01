"""Donald Trump full-body battle portrait from the latest user-provided image.
56x56 pixels, four Game Boy shades.
"""
import base64
import zlib
PIXELS = "eNrVlssWAyEIQyX5/3+ugPjoOZ0Bd3XVhddECHZa+/slum6oG3Lur4Gyy1ZthtlqTfx2aFdczahgAyuCCDFBuemuWeeMwh1HFHOGkKvlBSQUElZQQLezAwqDSbCLdKbXs+v6CVm5btM64FhS0CzCOXEQmZLAijJsjiVvU2cFDM4ZvgiKboZjtJhFXZ9BmdjiDOOTU1UzBTouURN68/FQRtvZr+XXG1XpTVDwZy88V+tXYPRq/RwomUd6xtzdMCh4mETZOxgdH6fhPd+zZzvXEtwG2RExI28pHcM3eDL7cstKiYYgP/FTjbpakeNxv+TA70UtPEu2/WxEWq+1siBXnkuCGAMQGa0YpcSTWHl5GXlmSZCceSbyghYU2WOeu92RL2Zv+NU1WaaL/4X6Ml594pWm6ShvZZxOp7dGb79i//Lj+wNVwgVX"
def trump_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y * 56:(y + 1) * 56]) for y in range(56)]
