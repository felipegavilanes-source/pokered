#!/usr/bin/env python3
"""Install the original 151 Pokemon battle sprites from pinned pret/pokeyellow.

Run before 'make'. Both front and back PNGs are replaced; gameplay data is untouched.
The pinned upstream commit keeps CI builds reproducible.
"""
from pathlib import Path
from io import BytesIO
import shutil
import tarfile
import urllib.request

YELLOW_COMMIT = "b452f2ab07185075140061c5084ab866d5e4a794"
URL = f"https://codeload.github.com/pret/pokeyellow/tar.gz/{YELLOW_COMMIT}"
ROOT = Path(__file__).resolve().parents[1]
FRONT = ROOT / "gfx/pokemon/front"
BACK = ROOT / "gfx/pokemon/back"

def main():
    expected = {p.name for p in BACK.glob("*.png")}
    if len(expected) != 151:
        raise RuntimeError(f"Expected 151 Pokemon back sprites, found {len(expected)}")
    if not expected.issubset({p.name for p in FRONT.glob("*.png")}):
        raise RuntimeError("Pokemon front/back sprite lists differ")

    request = urllib.request.Request(URL, headers={"User-Agent": "pokered-yellow-sprite-import"})
    with urllib.request.urlopen(request, timeout=90) as response:
        archive = tarfile.open(fileobj=BytesIO(response.read()), mode="r:gz")

    for kind, names in (("front", expected), ("back", expected)):
        members = {Path(m.name).name: m for m in archive.getmembers()
                   if m.isfile() and "/gfx/pokemon/" + kind + "/" in m.name
                   and m.name.endswith(".png")}
        missing = names - members.keys()
        if missing:
            raise RuntimeError(f"Missing Yellow {kind} sprites: {sorted(missing)}")
        destination = FRONT if kind == "front" else BACK
        for name in sorted(names):
            with archive.extractfile(members[name]) as src, (destination / name).open("wb") as dst:
                shutil.copyfileobj(src, dst)
        print(f"Installed {len(names)} Pokemon Yellow {kind} sprites")

if __name__ == "__main__":
    main()
