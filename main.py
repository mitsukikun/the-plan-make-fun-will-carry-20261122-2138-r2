# the-plan-make-fun-will-carry-20261122-2138 entry: write the plan text to
# /output/entry.txt. Python 3.13, standard library only, no network.
# Deterministic: every run writes the same 274 bytes.
# Rebuilt in a fresh post-open session and re-verified there.
# MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
import os
from pathlib import Path

ENTRY = (
    "Day 1: spend $25 on API credits and a $10 domain. "
    "Find 500 Shopify stores with no blog (BuiltWith free tier), "
    "email each a $49 AI SEO audit offer. "
    "Deliver audits in 24h. "
    "A 2% reply rate is 10 clients = $490. "
    "Reinvest profits, upsell $99/mo monitoring. "
    "Target $600 by day 30."
)

# Gate, checked before anything is written: 1-280 Unicode code points,
# not only white space.
assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip(), "entry is blank"

OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "entry.txt").write_text(ENTRY, encoding="utf-8")
