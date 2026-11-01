"""Messi trainer artwork, adapted from the user-approved reference image.
56x56, four Game Boy tones; pixels are stored losslessly as compressed indices.
"""
import base64
import zlib
PIXELS = "eNq9lo2OwjAMg+P4/d/58tPSFo5rwklUwCa0b25nJ6vIH4M2pD2MAdAm7XrAjk2SDkHUPsoOFnIKaJOLtdGpzkQp6pc71RKk+kzzTKUh+NCAPZrmgxl3MMEO5+uLH2UDhOfFvrCJihay9eBiVcwlXucGrpjN9d04X9IhODis8/dlw815D1khnswhy+8w4Y5pBHIDS2pZOisoAd5T7XJWAwOLYvDhR1zN83QsFzIzIwKX3uAcR49ICqedb3oDZkYwvwHy3lSYcphSBcHIcRQBnvRuYLS/zMpkURGUIMKS2T8RWb93p+HbxmmYyHrbnVx4XwJPLrvNp1xFkHpwgXQ5L8TqRDfOy5AlC9MMF/JJ6nClNs9tqLtAVPV2zjH0OSdY8+8AZy/oYdTiw/yVky9w0uUkNxLC7L393VI1z0ePn0f9AjfenB/sBgXSB6Nn97n15qU0tnXbG5uNzTL/x0mXe7mHfAi+/vsDPM4F7g=="
def messi_portrait():
    pixels = zlib.decompress(base64.b64decode(PIXELS))
    assert len(pixels) == 56 * 56
    assert set(pixels) <= {0, 1, 2, 3}
    return [list(pixels[y * 56:(y + 1) * 56]) for y in range(56)]
