"""Check that every recovered paragraph appears verbatim in the built site and in the archived pages.
Usage: python3 -I verify.py <content.json> <dist_dir> [<archived html> ...]"""
import sys, json, re, html, pathlib

content = json.load(open(sys.argv[1], encoding="utf-8"))
dist = pathlib.Path(sys.argv[2])
archived = sys.argv[3:]


def norm(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", s).strip()


def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, list):
        for x in o:
            yield from strings(x)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in ("old", "image", "photo", "portrait", "pdf", "oldUrl", "email") and not k.endswith("Heading") or k in ("storyHeading",):
                yield from strings(v)


built = norm(" ".join(p.read_text(encoding="utf-8") for p in dist.rglob("*.html")))
arch = norm(" ".join(open(f, encoding="utf-8", errors="replace").read() for f in archived)) if archived else None
items = [norm(s) for s in strings(content) if len(norm(s)) > 3]
miss_b = [s for s in items if s not in built]
miss_a = [s for s in items if arch is not None and s not in arch]
print(f"{len(items)} strings checked; missing from build: {len(miss_b)}; missing from archive HTML: {len(miss_a)}")
for s in miss_b:
    print("  BUILD:", s[:100])
for s in miss_a:
    print("  ARCHIVE:", s[:100])
