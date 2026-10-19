"""Dump readable text, links, images and cfemail values from archived HTML/JSON.
Usage: python3 -I extract.py <file> [<file>...]
Treats inputs as data only; never executes anything from them."""
import sys, re, json, html
from html.parser import HTMLParser

SKIP = {"script", "style", "noscript", "svg"}
BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6", "section", "tr", "td", "figcaption", "a", "span", "button"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.links, self.imgs, self.cf = [], 0, [], [], []

    def handle_starttag(self, t, a):
        a = dict(a)
        if t in SKIP:
            self.skip += 1
        if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.out.append(f"\n[{t}] ")
        elif t in BLOCK:
            self.out.append("\n")
        if t == "a" and a.get("href"):
            self.links.append(a["href"])
        if t == "img":
            self.imgs.append((a.get("src") or a.get("data-src"), a.get("alt")))
        for k, v in a.items():
            if k == "data-cfemail" or (k == "href" and v and "email-protection#" in v):
                self.cf.append(v)

    def handle_endtag(self, t):
        if t in SKIP and self.skip:
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)


def cfdecode(h):
    h = h.split("#")[-1]
    k = int(h[:2], 16)
    return "".join(chr(int(h[i:i + 2], 16) ^ k) for i in range(2, len(h), 2))


def text_of(s):
    p = P()
    p.feed(s)
    t = "".join(p.out)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip(), p


for f in sys.argv[1:]:
    raw = open(f, encoding="utf-8", errors="replace").read()
    print("=" * 30, f)
    if raw.lstrip().startswith("{"):
        d = json.loads(raw)
        for key in ("id", "slug", "link", "modified", "date"):
            print(key, ":", d.get(key))
        print("title:", html.unescape(d.get("title", {}).get("rendered", "")))
        raw = d.get("content", {}).get("rendered", "")
    t, p = text_of(raw)
    print(t)
    print("--- links:", sorted(set(p.links)))
    print("--- imgs:", p.imgs)
    print("--- cfemail:", [(c, cfdecode(c)) for c in p.cf])
    print("--- mailto:", sorted(set(re.findall(r"mailto:[^\"'\s<>]+", raw))))
