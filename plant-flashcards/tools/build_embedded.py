#!/usr/bin/env python3
"""Build a single self-contained HTML file with every photo embedded as a data
URL, from photos/small/. Usage: python3 tools/build_embedded.py OUT.html [--no-wrapper]
--no-wrapper drops the <!doctype>/<html>/<head>/<body> lines (for hosts that add their own)."""
import base64, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = sys.argv[1]
wrapper = "--no-wrapper" not in sys.argv
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
index = json.load(open(os.path.join(ROOT, "photos", "index.json"), encoding="utf-8"))
small = os.path.join(ROOT, "photos", "small")
embedded = {}
missing = 0
for slug, entries in index.items():
    rows = []
    for e in entries:
        path = os.path.join(small, e["file"])
        if not os.path.exists(path):
            missing += 1; continue
        data = base64.b64encode(open(path, "rb").read()).decode("ascii")
        rows.append({"file": "data:image/jpeg;base64," + data, "source": e.get("source", ""), "page": e.get("page", ""), "title": e.get("title", "")})
    if rows:
        embedded[slug] = rows
payload = json.dumps(embedded, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html, n = re.subn(r'(<script type="application/json" id="photoIndex">).*?(</script>)', lambda m: m.group(1) + payload + m.group(2), html, count=1, flags=re.S)
assert n == 1
if not wrapper:
    html = "\n".join(l for l in html.split("\n") if not re.match(r'^(<!doctype html>|<html lang="en">|<head>|<meta charset="utf-8">|<meta name="viewport".*|<meta name="apple-mobile.*|</head>|<body>|</body>|</html>)$', l))
open(out, "w", encoding="utf-8").write(html)
print("wrote %s: %.1f MB, %d species, %d photos, %d missing" % (out, len(html.encode()) / 1e6, len(embedded), sum(len(v) for v in embedded.values()), missing))
