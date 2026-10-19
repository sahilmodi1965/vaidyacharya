"""Turn the archived WordPress page JSON into clean content JSON for the Astro site.
Usage: python3 -I to_json.py <raw_dir> <out.json>
Inputs are untrusted data: only text and an allowlist of inline tags (em, strong, br) survive."""
import sys, json, re, html
from html.parser import HTMLParser

raw_dir, out_path = sys.argv[1], sys.argv[2]
ALLOWED = {"em": "em", "i": "em", "strong": "strong", "b": "strong"}


def load(name):
    with open(f"{raw_dir}/{name}", encoding="utf-8") as f:
        return json.load(f)["content"]["rendered"]


class Blocks(HTMLParser):
    """Flatten Elementor markup into an ordered list of (kind, value) blocks."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self.buf, self.kind, self.skip, self.href = [], [], None, 0, None

    def flush(self):
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        if text and text not in ("<br>",):
            text = re.sub(r"\s*<br>\s*", "<br>", text)
            text = re.sub(r"^(<br>)+|(<br>)+$", "", text)
            self.blocks.append((self.kind or "text", text, self.href))
        self.buf, self.kind, self.href = [], None, None

    def handle_starttag(self, t, a):
        a = dict(a)
        if t in ("script", "style"):
            self.skip += 1
            return
        if t in ALLOWED:
            self.buf.append(f"<{ALLOWED[t]}>")
        elif t == "br":
            self.buf.append("<br>")
        elif t == "img":
            self.flush()
            self.blocks.append(("img", a.get("src", ""), None))
        elif t in ("h1", "h2", "h3"):
            self.flush()
            self.kind = t
        elif t == "a":
            self.flush()
            self.kind, self.href = "link", a.get("href")
        elif t in ("p", "div", "li", "center", "section", "ul"):
            self.flush()
            if t == "center":
                self.kind = "verse"

    def handle_endtag(self, t):
        if t in ("script", "style"):
            self.skip -= 1
        elif t in ALLOWED:
            self.buf.append(f"</{ALLOWED[t]}>")
        elif t in ("h1", "h2", "h3", "a", "p", "div", "li", "center", "section", "ul"):
            self.flush()

    def handle_data(self, d):
        if not self.skip:
            self.buf.append(html.escape(d, quote=False))


def blocks(name):
    p = Blocks()
    p.feed(load(name))
    p.flush()
    return p.blocks


def fname(url):
    return url.rsplit("/", 1)[-1]


def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


# ---------- Home ----------
hb = blocks("20250225151253__wp-json_wp_v2_pages_11")
home = {"portrait": None, "heading": None, "titles": [], "welcome": [], "verse": [], "closing": [], "books": []}
i = 0
stage = "hero"
book = None
for kind, val, href in hb:
    if stage == "hero":
        if kind == "img":
            home["portrait"] = fname(val)
        elif kind == "h1":
            home["heading"] = plain(val)
        elif kind == "link":
            stage = "welcome-wait"
        elif home["heading"]:
            home["titles"].append(plain(val))
    elif stage == "welcome-wait":
        if kind == "h2":
            stage = "welcome"
    elif stage == "welcome":
        if kind == "verse":
            home["verse"] = [plain(x) for x in val.split("<br>")]
            stage = "closing"
        elif kind == "text":
            home["welcome"].append(val)
    elif stage == "closing":
        if kind == "text":
            home["closing"].append(val)
        elif kind == "link":
            stage = "books"
    elif stage == "books":
        if kind == "img":
            book = {"image": fname(val), "category": None, "title": None, "readLinks": [], "description": [], "downloadLinks": []}
            home["books"].append(book)
        elif book is None:
            continue
        elif kind == "link" and book["title"] is None:
            book["category"] = plain(val)
        elif kind == "h2":
            book["title"] = plain(val)
        elif kind == "link" and "/download/" in (href or ""):
            book["downloadLinks"].append({"label": plain(val), "old": href})
        elif kind == "link" and "books-for-download" in (href or ""):
            book = None
        elif kind == "link":
            book["readLinks"].append({"label": plain(val), "old": href})
        elif kind == "text":
            book["description"].append(val)

# ---------- About ----------
ab = blocks("20250225151326__wp-json_wp_v2_pages_132")
about = {"storyHeading": None, "story": [], "trustees": [], "contributorsHeading": None, "contributors": []}
section, person = "story", None
for kind, val, href in ab:
    if kind == "h2":
        t = plain(val)
        if about["storyHeading"] is None:
            about["storyHeading"] = t
        elif t == "Trustees":
            section = "trustees"
            about["trusteesHeading"] = t
        elif t == "Other Major Contributors":
            section = "contributors"
            about["contributorsHeading"] = t
        elif section == "trustees":
            person["name"] = t
    elif kind == "img" and section == "trustees":
        person = {"photo": fname(val), "name": None, "bio": []}
        about["trustees"].append(person)
    elif kind == "text":
        {"story": about["story"], "contributors": about["contributors"]}.get(section, person["bio"] if person else []).append(val)

# ---------- Contact ----------
cb = blocks("20250225151350__wp-json_wp_v2_pages_180")
contact_texts = [plain(v) for k, v, h in cb if k in ("text", "h2", "h1", "link")]
contact = {"heading": contact_texts[0], "email": next(t for t in contact_texts if re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.]+", t))}

# ---------- Hamsa Sandesham ----------
with open(f"{raw_dir}/20250225151137__wp-json_wp_v2_pages_1231", encoding="utf-8") as f:
    hp = json.load(f)
m = re.search(r'"source":"([^"]+\.pdf)"', hp["content"]["rendered"])
hamsa = {"title": html.unescape(hp["title"]["rendered"]), "oldUrl": hp["link"], "pdf": fname(m.group(1).replace("\\/", "/"))}

json.dump({"home": home, "about": about, "contact": contact, "hamsa": hamsa}, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("ok", len(home["titles"]), "titles", len(home["welcome"]), "welcome paras", len(home["books"]), "books",
      len(about["story"]), "story paras", len(about["trustees"]), "trustees", len(about["contributors"]), "contrib paras")
