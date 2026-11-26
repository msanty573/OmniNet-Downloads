"""Rebuild src/mjsnet/assets/oui.tsv.gz, the MAC-address maker list.

Source: the IEEE registers (MA-L, MA-M, MA-S) as JSON from
https://github.com/silverwind/oui-data (BSD-2-Clause, packaging/licenses/oui-data-LICENSE.txt),
rebuilt from IEEE's files daily. Run before each release:
    .venv/bin/python packaging/make_oui.py
The monthly "Maker list" workflow in the downloads repo runs a copy (tools/make_oui.py)
with an output path, publishing oui.tsv.gz + oui.json for the apps' monthly refresh:
    python3 make_oui.py OUT_DIR
The .gz is byte-for-byte repeatable (no timestamp), so an unchanged list has the same sha256.
"""

from __future__ import annotations

import datetime
import gzip
import hashlib
import io
import json
import sys
import urllib.request
from pathlib import Path

URL = "https://raw.githubusercontent.com/silverwind/oui-data/master/index.json"
OUT = Path(__file__).resolve().parent.parent / "src" / "mjsnet" / "assets" / "oui.tsv.gz"


def main(out: Path = OUT, info: bool = False) -> None:
    req = urllib.request.Request(URL, headers={"User-Agent": "mjsnet-build"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    rows = {}
    for prefix, text in data.items():
        name = " ".join(text.split("\n")[0].split())      # first line = organisation
        if name:
            rows[prefix.upper()] = name
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", compresslevel=9, mtime=0) as gz:
        gz.write("".join(f"{k}\t{name_fix(rows[k])}\n" for k in sorted(rows)).encode("utf-8"))
    blob = buf.getvalue()
    out.write_bytes(blob)
    print(f"Wrote {out.name}: {len(rows):,} prefixes, {len(blob) // 1024} KB")
    if info:
        meta = {"count": len(rows), "sha256": hashlib.sha256(blob).hexdigest(), "size": len(blob),
                "built": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")}
        (out.parent / "oui.json").write_text(json.dumps(meta, indent=1) + "\n", encoding="utf-8")


def name_fix(name: str) -> str:
    return name.replace("\t", " ")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        d = Path(sys.argv[1])
        d.mkdir(parents=True, exist_ok=True)
        main(d / "oui.tsv.gz", info=True)
    else:
        main()
