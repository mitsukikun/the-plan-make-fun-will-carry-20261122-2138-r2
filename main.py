import os
from pathlib import Path

ENTRY = "Day 1: spend $25 API credits + $10 domain, find 500 Shopify stores, no blog. Email each a $49 AI SEO audit offer, deliver audits within 24h. Follow up non-replies day 4. At 2% reply, 10 clients pay $490. Reinvest profit in outreach, upsell $99/mo monitoring, target $600 day 30."

assert ENTRY.strip()
assert 1 <= len(ENTRY) <= 280

OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "entry.txt").write_text(ENTRY, encoding="utf-8")
