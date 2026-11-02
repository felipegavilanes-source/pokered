"""Full-body Xi Jinping trainer portrait, native 56x56 hand-adjusted facial features, Game Boy DMG 56x56.
Four shades, reproducibly embedded as zlib-compressed palette indices.
"""
import base64
import zlib
PIXELS = "eNrNllmOxCAMRG3X/e882MbQ6fmpamkWogQi8VLGC8TsnzRkC5WKotyhii1mUdDAllrPdUmY4zSe7Pk1MAhLfIrANa51wgAldK8vPOcpl0Au1BWHrkfNd1NSBnZFFLkG2khXsvMO3bUM9f0BMUF9dEKriAFFK5EGZiFJcgGP8OyyfgUTI1bl1Z0d55qcGQUh9piKRc7b5P0Gx2EUT8+Zebl6AyM4nBdQF8MdgbpxRUnusT5CEC8g/GCkoY84cH75NA7WLuxNPkLYsjEZhjGazO1NxQkDW0Ynr/caf5wbb7SHgt4k3uIgHLeHc2GnmLiJ5+2kTFGCmbbjNimjcLHLj4/C5ey3uF21u/w+4DS3WDvTDWSpP7mTN8r/SwwH4UCKOb6qGFgQ579uhuC5b/+Gf92+AEhoBrE="
def xi_jinping_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y*56:(y+1)*56]) for y in range(56)]
