"""Donald Trump 56x56 four-tone battle portrait for the Viridian Gym leader.

Created in the same high-contrast, GBA-inspired pixel-art style as the
approved CR7 reference: swept blond hair, suit and tie, raised fist.
The ROM is a Gen 1 Pokémon Blue hack; portraits use 4 grayscale shades.
The embedded pixel array is self-contained so CI does not need Pillow.
"""
import base64
import zlib

# 0=white, 1=light gray, 2=dark gray, 3=black.
PIXELS_ZLIB_BASE64 = (
    "eNq1VtG2pDAIK+T//3lLCNhWd3Uedo5zvLeaAgmhM8b/+pjZ7xh3x/zaTxgUxH6AmneCRuTXBBsTJc4vPsCWtAISwceHTGNvE5nz"
    "mrvMy94zTTIs2ZyxEPfxioMzJtnUZ5br+BDNIkbzmcwa7F0BQCgr2DulEwQw6Ag5gpuk9YXSmWPC2DGJigLNPyQ6MeTGhAyW3iQk"
    "98gUU/kZUMn/E2a5uZWLJD/8BRc7m8KVEvPvFwlnmogayxGMxru/ujXVoCsCrcTvbnIsybMQw5YpQpxbQHZi82zElSFqr6H4h3HW"
    "RkrdV8GMSp64fB5llCXEYS1Y7nPyifL2guP+xWhsPP/DWV21PtZ4NV5ytk1Nn9NM1+0rtR44P/1wsduEXTtT9KlJqIAnnK2EzTtd"
    "4LR9pGGBe2RzCuu9IziMwke8hx9u3YLN5ZUxOwRVGtm0J1YMm03AWZbAv6ggiQ53CZi+CNzxvGeJn8Mpm1bjDKdpnfU+wEaSqZ45"
    "Z0RkHS/gWGUL6Ahkmv7QY7dZRfJlRQb1gQcRvM8SNmL2ojLnkp2JktzZMLyos8ZtnEV6M2UFdjYzltHOOntcOJQgPk7mZk8wVjSH"
    "X5+MyDgqb/g2dj0PLNbkG1DUqEmjQX0B8pVsxQ2pgBREx60avHG1d3nau0AJz+fJVneNaW/tr6nVkTnvKaHzCM6sdxz4XdOUhoGi"
    "6V3vmeorDEnFictoNHau08YVDl3oWmC0beEqRrLUjBQQe6KWOLBjinOoOXABu8k6UdJCk8r9+XCt7h6wcLRN6JTjCwrXIS/5O9F0"
    "EnLiiXTiLhiw4Da4cFVJk37H7fmywKtorH184taAskQ9wPWDz6yb+lqqgZZDzcqg5n8AUI4MdA=="
)

def trump_portrait():
    pixels = zlib.decompress(base64.b64decode(PIXELS_ZLIB_BASE64))
    if len(pixels) != 56 * 56 or any(value > 3 for value in pixels):
        raise ValueError("Trump portrait must be 56x56 with four shades")
    return [list(pixels[y * 56:(y + 1) * 56]) for y in range(56)]
