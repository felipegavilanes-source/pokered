"""Neymar battle sprite adapted from the user-provided yellow Brazil jersey pixel artwork.
56x56 pixels, four Game Boy shades. Full-body pose preserved.
"""
import base64
import zlib

PIXELS = "eNrNlsuywzAIQxH6/3++POzUd7owyqpetTM5kUCQxOyXDl5RpNOoU0hBQCQDa1CSTLHQQgpKikUwIUogdzPdXaoQB4ebxoHtPwiON4xnDsvt3SfPnjNAJDwIP1p3kqFVw3brZ9/Yvxt04eK+qcH/Y+33+CLjGObVvwyC1jVeMQSWiTE95z5Mh6U5d3CNKIegp9Hg0h/6Dpjvq+cusCcbgxK32b46Z2ytxVQRvq5HH+HhklzFp62gd2k14AoIlNnyGJUKHDKOFELGOu1plrc5ZDRjzvDE6NPHDDuByt055vaoNGcFchTCmrDqajVpON0k9uE89F7fj9Ext9eXFSMlrFD3+ZOeB6EUt6QkLeunwwtuy5nGPdgrjs8vBeuXGNUIyiRd4viYVPR4mBwvzz+X7VOqrt/SdcYYP5xpg0lTubUGn88QE3r54oNTacUXZz95/gCjHwWE"

def neymar_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y * 56:(y + 1) * 56]) for y in range(56)]
