"""CR7 full-body celebration sprite, improved face and silhouette.
56x56 pixels, four Game Boy shades.
"""
import base64
import zlib
PIXELS = "eNqtVsu2xCAIM+H//3l4qLW39Q54hkXbRWMwBLS1HwdFA1UUJIJFnMgZkBikqKVpWLJKCKGSAXUcQDiulqeGPQmWcFQyB7OqJwWeJ8pu4QGdJwrlrOJMTSsET2wNq0eNzQpOf+cLoWZxS3vZ9Tubq5CyRBbIoOMCzMPQU/WNZsQZbFxIvxNibo247fG7SzoQiza6Bvf+MJj1jmd30elHUwNwi6PDXPV7hlbJ9upwRVnbuD9wDUELL6jpKe8iNu823odgbz+a2aw5+JSRbW6ef+g8gdeZQYtR3Vm8VX9bVFfHW3tPd8YyC19vyJDuWYfJpqiOxDLBVYDt3JCAxNOUelRq587Ikc6LxdJW2V0TM/6f1r4xkNvWt9UDGdsEUz0E96fTecbZA5Do84/dNGq9LK5bNDyy1Of/Xsdy5Ll6gCSHLadN4LKnptLVrQjzeN7pa4uMTfbv3FFreY5cezWyh9jga30aJs+IhSKEYvoQG8ZEjfD6E5Uz6SZF4bp1d4nfnk7uot4ep3fYI8KDK+w0/AHOJuBRojjje8YHJ5AHcA=="
def cr7_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y * 56:(y + 1) * 56]) for y in range(56)]
