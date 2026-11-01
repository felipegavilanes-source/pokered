"""Full-body Messi battle portrait adapted from the latest user-provided reference.
56x56 pixels, four Game Boy shades; stored losslessly as compressed indices.
"""
import base64
import zlib
PIXELS = "eNqtluuywyAIhN3l/d+54ZaY6RyEM/VH2mn9grILutaPB23MKTFOMKEgTk1BD2awyCSczs/BSbxcp4KYrHMLPeG2DMm/OI44QidDx0AJaEJoKgID00CnY8UDE84+Vqx1xME5DuIt3RJNOHCi3/J8XAiFs4K40gmNJrP6uxS41sdhOLVJVhImVNYR1ddNFJEPdTT0a88x8PerReEG6FnNp0Y/U589BqrDmbncYfdzsRdOJ+cD98+HcLB0BMcIy3M4n+sFlNwpoFY3CNxZjNinqjePSCgRnEqJWgqTWV6c/YRDRsW0BjcdrBZPG+TfXNUujOH65lBz5mhki3g4V7VUTwltm+kUf0catTALQ7lHReQfpTedg4/gWFvblmn9Xaxs/fj0d5QcPTPbYWuwnYfFOiGuwhfn/bRuLVtXSu7cEHUjulS5t+hc53AhIykrI7b7YMyOnLJ9qCyEvWjrbnfrzJ51iT539yGw1QMzp3FyPs5rx8sGbQGbnGu/Hbw9HeLC+rr1onWIcXNV3gtxXuSbS/B8dWE2tKdTgaNrdjU+YE0F9g=="
def messi_portrait():
    pixels = zlib.decompress(base64.b64decode(PIXELS))
    assert len(pixels) == 56 * 56
    assert set(pixels) <= {0, 1, 2, 3}
    return [list(pixels[y * 56:(y + 1) * 56]) for y in range(56)]
