"""Jeff Bezos full-body battle sprite with clearer face, 56x56 Game Boy shades."""
import base64
import zlib
PIXELS = "eNrNVtsOQjEMGvD//+x6mc74YEl8cA+aGDmllHK21p8cACRsVEI21MTF/xNJk2SioiBclgjw7tHCERQRxykYOBTMw6FV2Q+QgctS2aFXrykmysctt9wZX7TnzZ01OtugoaO2kraxoc0Qtq976suzWQw7nJZ058jQQ6GJ6ptjTaLgPvtDHE/+VEMsxFaVc1wgURw5dXbuUPCjCj7sj6/TrY5x4H20vHoSjXLpsHSnHFWioAqkOoazc2Y5O8nwJ4+/kq+ze6WJSlcLd7zN+QaGw5opaOTZc3LdJxxdeEbh6NlKypKlGgwxq0PM9UxFy3AWrvn1KKz2wpY053eWrol6Mfj097TBlKW2B/Ljc7lE7yVwhEmafGUGjBw84YC51bKa7ofMiL5HZu/ubPuuyISGG1gbhCvaNInQuJbdmdnvsa8VO3LxFhqDra970udvv7u2PwCN7gVQ"
def jeff_bezos_portrait():
    raw = zlib.decompress(base64.b64decode(PIXELS))
    assert len(raw) == 56 * 56 and set(raw) <= {0, 1, 2, 3}
    return [list(raw[y*56:(y+1)*56]) for y in range(56)]
