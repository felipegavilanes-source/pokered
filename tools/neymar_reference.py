"""Neymar full-body battle sprite from user-approved grayscale reference.
56x56 pixels, four original Game Boy tones.
"""
import base64
import zlib

PIXELS = "eNq1llluxDAMQ03q/neuFsdJjAFMBajRj2DgV22UrDH+4cC+UX76qDPODtCa1pzpg8Zg/Qwiv1VzTEtAxoiGwVGX6SA7juKZ1VMK+bD34HhK4Z07IzNKhKMH35xaYHoXljydxwAjdzMYv42ZVZDHWnNGduvLa3jizGtsi4uiZyWPgom82JRHeImSmSkdEOGkoi1is/hNUZeDcd3yIxw167TPVWzoKgvQnUxdMg2bpOsILO0FeH1Bs5hm4q8waiBtP9SyUyBnjNTBrES1Am2apwjunGqQxFWLGqSUh+510uthXY41bdocGhzfblrMX1UzL4tsu1kl0CT6lhohcvgo0A2CmfW91J+V3UvxGcNHzr5x+MitrIAtzmq4ZxvUHBSVWb5irRWyMrmeoCi6puhaPewVqrjKYT3MscBo9vKfr5v5opGKOczbN6ekMxy8sWlPKjmf21gtaBL2ahtIjcQaztgkx1OzW012/JC40D/c1tB4Xxr75+H8AdM6B9k="

def neymar_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y * 56:(y + 1) * 56]) for y in range(56)]
