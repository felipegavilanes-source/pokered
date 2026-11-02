"""Donald Trump full-body trainer portrait with improved facial readability.
56x56 pixels, four Game Boy shades. Based on the approved revised artwork.
"""
import base64
import zlib
PIXELS = "eNqtlo2OwzAIgwN+/3c+MJBOd9cWolXaj6Z9NRgn6VpfvpDXFPM3cbzPiNi/Jb7VLdpsvewm/dZSSVTVPnWNSEBI9wuFyZCxGk0SEzfpiLDiASecXZoy4cyMcEZGenqNUiajRwbFzVEMY0Y5ha4TbhjtqBIYBftjEVkE2oqAhyR8ZHSaIMTMAINiplCxhwUHppPinVHYHwHqxfwNeuaQjoTG8pWH6vYJRNgolEuOiL/dhnTbTuN9gxFaktzdMOrXoJSLaIFMFHpnaknwsjKDS3V5alF9kdewfSNbpUPFm72U3WUX3pTEWoj6OImbFrE7iJh5vHZfuRHjbTtLvWzvIp7A6Kq4MsS2HHnnwPXwydE4vHN74sW9ruGY/E7YZdfrcqpYTo/OK87A5HjI8sqXoV5hiilX9ow4zTwPwJ3L2BFHYMYSU8FaUiMQu7jqEN3zYceybw3yeF8zEHUe/ZrK+EkQ/Qb/Gefpo+jZM6zgWBAn3Owx5hsdHnF/rh88bQcp"
def trump_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y * 56:(y + 1) * 56]) for y in range(56)]
