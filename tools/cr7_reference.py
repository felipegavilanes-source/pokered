"""CR7 battle portrait, 56x56 four-shade pixel art.

Adapted from the user's approved reference image, retaining the raised fist,
short spiked hair, face direction, national-team jersey and prominent #7.
This embedded 2-bit palette bitmap is independent of Pillow and source images,
so GitHub Actions reproduces the exact approved portrait with stdlib only.
"""
import base64
import zlib

# 56 x 56 palette indices (0 white, 1 light gray, 2 dark gray, 3 black).
# Base64-encoded zlib stream; decoded pixels are stored row-major.
PIXELS_2BPP_ZLIB = (
    "eNrNVkmCwyAMQ/L//zx4A5NCS26TU9ogy7a80Nq/egC8xzRQhHyL6yBhxwlfcYLsfK+BtEfiwSsv1dGeGcXfAtW9kUx19xIIkSXU"
    "+vM7IQbIgJd6QALUHYayX3pKZ5AQnrc5NQ2o52mOXuOApcTMyl21sNb0tYZizcBsC84fv7pBtQhKaIS4KlN+/sFLP12NwXinvKZP"
    "g0pPeZfPnng7PaoN1wX60JO/aqvU8yT7khV64T/6wNuW7YgL+xhl0TGz5884J0JJNyfqjBvhlMQJy7TgN7olkd0UZsA80KW+kMUF"
    "/3D0M6OqUvibhXfGIcfYiDMaznvogMsxJCWZRAKNkocxC6PIXtexgjBjdNi2O625o5Z1oahkClRk4HZtSw9Ey6nYhQ0nT0vbTd44"
    "3I8IM6LoPRtk7ic+WtB3XP8UbmFBas3YgsBzGEpD1OITFkCbF5jiFIHh7YLPJw9kftbdg1Bhiww/TK1lU7kOkbQdEI4zYK2x/s3C"
    "CMW4YbUtqOfwwPlhy9wWJ2GPi5s21u0zFUdu+FrBBZ1rHnZdtGT1idG8EhkjEaN2Tb9Im+3LSilWwoKx6oebyiFocWEhhFVC41NP"
    "cp9y4MQlNHcMWUOTIYg3xnSzuTFvP1lhui6Gx7KEBysEtes3sqBhwGagUhdApHHgMhmD7gOHxNHGpcwpXUKcb5Q1nXCh6zWwhFgsxJ6HJMwU87uOvj4yM+gEzHnso8iut/Bb47bMhvV+6A9MeAg2"
)

def cr7_portrait():
    pixels = zlib.decompress(base64.b64decode(PIXELS_2BPP_ZLIB))
    if len(pixels) != 56 * 56 or any(value > 3 for value in pixels):
        raise ValueError("CR7 portrait must contain 3136 four-shade pixels")
    return [list(pixels[y * 56:(y + 1) * 56]) for y in range(56)]
