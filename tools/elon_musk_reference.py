"""Elon Musk full-body trainer battle portrait, four Game Boy shades."""
import base64
import zlib
PIXELS = "eNqtVu0SwjAIg/D+72wLpR+4TdjZP57n0kASmER/P8xvUAIRlKHcUHqKwA4D6kC257nDS3y8eKs4NKZqpRBupbIWWuXj0WDNc+sQNV16hfrR8PSCrzdYw5H7V/MdRlp03fzWqJWHSGFUzXVvzPJSKbK71hCseKRbwwDqICGb0AGDT267R7JKDjIexBmcOI16zlCcJIT0rvqKocEnCZh35cVa4fdqbDGZuHX2/J2DCjV7wcKxe0PwmEQtZrnD9Ybb1YhamOHj5guk+hmmceBoFjSX7snI61EPJGC7yzIV+EBLG2BP3byf/evB6Cnq6wMS52bmN0hjT9rL4inkPITYpFy/4CmhXbwr139GDYeeSA2gsQUbsgspupdfgcdhegXMLcNVHApyEm+Ts89QYg9OlgrhIWEed2qBtDDBsZLt25NZYTgQIEmIlzibV9zyP5sXdMLPBr/LSjl4VVUGePX2CTvm3vTwDvDN9p8/+x+33AmS"
def elon_musk_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y*56:(y+1)*56]) for y in range(56)]
