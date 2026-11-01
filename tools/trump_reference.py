"""Donald Trump 56x56 four-shade battle portrait for the Viridian Gym leader.

Derived from the pointing-at-the-player pixel-art reference approved by the
user on 2026-11-01. The image is cropped to a 1024x1024 square, resized to
56x56, contrast-adjusted, and mapped to four Game Boy palette shades.
The original reference is not required at build time; this encoded image
ensures reproducible compilation with Python standard library only.
"""
import base64
import zlib

# Palette indices: 0=white, 1=light gray, 2=dark gray, 3=black.
PIXELS_ZLIB_BASE64 = (
    'eNqdVoGO6yAMa5z//+dHbAdoO3bTm3S6qsPYiU3YdX37RMQVfLh+/wCpz3hA/oiMsTxiY038wFQk0hcb/d8Ca3kQswH/YBwKZ1eu'
    'CR8lRn5DvTtA4JAeX3pz+G6QlnjE0a+M+KABru3EWCLjgyMw06GnCdzpqh3jVfjtycSqrqqIJe9mxhEXshsMy1RHYLXmhEtbxUze'
    'FI/ngRqfOIWSoFjtEX4wV7iH8nMyWWSIhJZRpQrHFyeypaEkjxe1CZy6U7pziC26ASnZVSfbE/ABPgjN6qnkWmU7aRF5DCjjEVo4'
    'Lb/oi7Y74Fi7cT1ZwinI4yEEez1YsOVEDwOT57PkGUQ+i1WZo5X45AMkIvqfQr1r/Yir1TAwLpuwzRe+e9unN9wOwKxpAatwPHFK'
    'ehhHvtWPFcGn61UHPctY3HKxrecpesY6uV/5usLUJzBmHa9p7/1zzjodieSIcC7xNm9Go047C03cJrXH6tODnBYVsMixj0Odu3r7'
    '7CVFzrYmbx+FpI3k3HnwuYfZiuso6dLTGeBf7BeHYGmzar33z3lnerIF99sJc8sX+ywYgZjAUKxzg1FbBzM5OmE+DiPfoczeOn11'
    'psLh6O15PFcKGHTHdwKnnaFqQikR8bpBfW+vOTH+I/vghOY09AuCpH1ThGtvEeObcP2pWtCDnmA4DmCzPdArVsl0iLMbP03Q7jz3'
    'oH3ZBXBH92Cu9sSTWhvK2X15My6gbBs3fyAJrbukd7zSJWiFo78QolfCfLWnzqzuss4DR2WX01/AjMLRm1g3nYaWvHgQGiYT1WZN'
    'BTePvdno9bTRuXNN6NVr8dZ8E2YT1hD27e5MRe5mTanOiwkrLNDFwR9ccQVuNJMLG1CXLkwYXd2DbYHRSieON9W7qDtOAP+Xzs42'
    'nrXh3SCXShyFYu/7C4AHofjKCmm//vPzD7BnDhs='
)

def trump_portrait():
    pixels = zlib.decompress(base64.b64decode(PIXELS_ZLIB_BASE64))
    if len(pixels) != 56 * 56 or any(value > 3 for value in pixels):
        raise ValueError("Trump portrait must be 56x56 with four shades")
    return [list(pixels[y * 56:(y + 1) * 56]) for y in range(56)]
