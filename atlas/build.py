#!/usr/bin/env python3
"""Atlas generator for the craft-n-code repo.

Pure python3 stdlib, no external deps. Reads atlas/manifest.json and emits
atlas/site/<slug>.html per entry plus atlas/site/index.html and site.css.
"""

import html
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATLAS_DIR = os.path.join(REPO_ROOT, "atlas")
MANIFEST_PATH = os.path.join(ATLAS_DIR, "manifest.json")
SITE_DIR = os.path.join(ATLAS_DIR, "site")

CODE_EXTS = {".py", ".js", ".html", ".json", ".sh"}

READING_LADDER = [
    ("Tier 0", ["docs/REPO-TOUR.md"]),
    ("Tier 1", [
        "research/MASTER-DOSSIER.md",
        "research/WINNER-REVERSE-ENGINEERING.md",
        "research/CHEATSHEET-BRIEF.md",
    ]),
    ("Tier 2", [
        "research/2026-TOPIC-PROBABILITY.md",
        "research/IDEA-BANK.md",
        "research/WAVE-SYNTHESIS.md",
    ]),
    ("Tier 3", [
        "research/JUDGE-DOSSIERS.md",
        "research/COMPETITOR-POOL.md",
        "research/2025-FINALS-ROSTER.md",
        "research/REJECTED-LOST-ENTRIES.md",
    ]),
    ("Tier 4", [
        "research/WINNER-EXACT-DEEP-DIVE.md",
        "research/PROBLEM-BANK-SPONSOR-DNA.md",
        "research/EVENT-SITE-FORENSICS-v4.md",
        "research/D3FEST-2022-PROBLEMS.md",
        "research/2024-STATE-QUALIFIER-FORMAT.md",
        "research/RABBITT-AI-DOSSIER.md",
        "research/NEXORA-FORENSICS.md",
        "research/PARTICIPANT-UNIVERSE.md",
        "research/GAP-MAP.md",
    ]),
    ("Tier 5", [
        "scaffold/README.md",
        "docs/CODE-WALKTHROUGH.md",
        "docs/BUILD-SPEC.md",
        "docs/BUILD-SPEC-2.md",
        "scaffold/tests/test_approval.py",
        "scaffold/tests/test_trace.py",
    ]),
]


def slugify(path):
    return path.replace("/", "-").replace(".", "-")


def rel_to_root(path):
    """Relative path from atlas/site/ up to repo root, then down to path."""
    return os.path.join("..", "..", path)


def escape(text):
    return html.escape(text, quote=False)


def inline(text):
    """Render inline markdown: code, bold, links. Text is already escaped."""
    text = re.sub(r"`([^`]+)`", lambda m: "<code>" + m.group(1) + "</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", lambda m: "<strong>" + m.group(1) + "</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  lambda m: '<a href="' + m.group(2) + '">' + m.group(1) + "</a>", text)
    return text


def render_table(lines):
    """lines: list of raw table rows (starting with |). Returns HTML string."""
    rows = []
    for line in lines:
        line = line.strip()
        if line.startswith("|"):
            line = line[1:]
        if line.endswith("|"):
            line = line[:-1]
        cells = [c.strip() for c in line.split("|")]
        rows.append(cells)

    if len(rows) < 2:
        return ""

    header = rows[0]
    body = rows[2:] if re.match(r"^[\s:|-]+$", "|".join(rows[1])) else rows[1:]

    out = ["<table>", "<thead><tr>"]
    for cell in header:
        out.append("<th>" + inline(escape(cell)) + "</th>")
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>")
        for cell in row:
            out.append("<td>" + inline(escape(cell)) + "</td>")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def render_markdown(text):
    """Minimal markdown to HTML. Text is escaped; structure is added."""
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)
    in_code = False
    code_lang = ""
    code_buf = []
    in_list = None
    list_buf = []
    in_blockquote = False
    quote_buf = []
    in_table = False
    table_buf = []

    def flush_list():
        nonlocal in_list, list_buf
        if in_list is None:
            return
        tag = "ol" if in_list == "ordered" else "ul"
        out.append("<" + tag + ">")
        for item in list_buf:
            out.append("<li>" + inline(item) + "</li>")
        out.append("</" + tag + ">")
        in_list = None
        list_buf = []

    def flush_quote():
        nonlocal in_blockquote, quote_buf
        if not in_blockquote:
            return
        out.append("<blockquote>")
        for q in quote_buf:
            out.append("<p>" + inline(q) + "</p>")
        out.append("</blockquote>")
        in_blockquote = False
        quote_buf = []

    def flush_table():
        nonlocal in_table, table_buf
        if not in_table:
            return
        out.append(render_table(table_buf))
        in_table = False
        table_buf = []

    while i < n:
        line = lines[i]

        if in_code:
            if line.strip().startswith("```"):
                out.append("<pre><code class=\"language-" + escape(code_lang) + "\">"
                           + escape("\n".join(code_buf)) + "</code></pre>")
                in_code = False
                code_buf = []
                code_lang = ""
                i += 1
                continue
            code_buf.append(line)
            i += 1
            continue

        stripped = line.strip()

        if stripped.startswith("```"):
            flush_list()
            flush_quote()
            flush_table()
            in_code = True
            code_lang = stripped[3:].strip()
            i += 1
            continue

        if stripped == "":
            flush_list()
            flush_quote()
            flush_table()
            i += 1
            continue

        if stripped.startswith("|"):
            flush_list()
            flush_quote()
            in_table = True
            table_buf.append(line)
            i += 1
            continue

        if in_table:
            flush_table()

        heading = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if heading:
            flush_list()
            flush_quote()
            level = len(heading.group(1))
            out.append("<h" + str(level) + ">" + inline(escape(heading.group(2)))
                       + "</h" + str(level) + ">")
            i += 1
            continue

        if stripped == "---" or stripped == "***" or stripped == "___":
            flush_list()
            flush_quote()
            out.append("<hr>")
            i += 1
            continue

        if stripped.startswith(">"):
            flush_list()
            flush_table()
            if not in_blockquote:
                in_blockquote = True
            quote_buf.append(stripped[1:].strip())
            i += 1
            continue

        if in_blockquote:
            flush_quote()

        ul = re.match(r"^[-*+]\s+(.*)$", stripped)
        if ul:
            flush_quote()
            flush_table()
            if in_list != "unordered":
                flush_list()
                in_list = "unordered"
            list_buf.append(ul.group(1))
            i += 1
            continue

        ol = re.match(r"^\d+[.)]\s+(.*)$", stripped)
        if ol:
            flush_quote()
            flush_table()
            if in_list != "ordered":
                flush_list()
                in_list = "ordered"
            list_buf.append(ol.group(1))
            i += 1
            continue

        flush_list()
        flush_quote()
        flush_table()
        out.append("<p>" + inline(escape(stripped)) + "</p>")
        i += 1

    if in_code:
        out.append("<pre><code class=\"language-" + escape(code_lang) + "\">"
                   + escape("\n".join(code_buf)) + "</code></pre>")
    flush_list()
    flush_quote()
    flush_table()

    return "\n".join(out)


def render_code(text, path):
    lang = os.path.splitext(path)[1].lstrip(".")
    return "<pre><code class=\"language-" + escape(lang) + "\">" + escape(text) + "</code></pre>"


def render_content(path, text):
    ext = os.path.splitext(path)[1]
    if ext in CODE_EXTS:
        return render_code(text, path)
    return render_markdown(text)


def page_html(path, blurb, body):
    open_link = rel_to_root(path)
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{path}</title>
<link rel="stylesheet" href="site.css">
</head>
<body>
<header class="page-head">
  <a class="back" href="index.html">&larr; BACK TO INDEX</a>
  <h1>{path}</h1>
  <p class="blurb">{blurb}</p>
  <a class="open" href="{open_link}" target="_blank" rel="noopener">OPEN FILE</a>
</header>
<main class="content">
{body}
</main>
</body>
</html>
""".format(path=escape(path), blurb=escape(blurb), open_link=escape(open_link), body=body)


def ladder_html():
    out = ['<div class="ladder">']
    for tier, paths in READING_LADDER:
        out.append('<div class="tier"><h3>' + escape(tier) + "</h3><ul>")
        for p in paths:
            slug = slugify(p)
            out.append('<li><a href="' + slug + '.html">' + escape(p) + "</a></li>")
        out.append("</ul></div>")
    out.append("</div>")
    return "".join(out)


def index_html(manifest, total_chars, file_count):
    sections = []
    for section in manifest["sections"]:
        cards = []
        for entry in section["entries"]:
            slug = slugify(entry["path"])
            open_link = rel_to_root(entry["path"])
            cards.append(
                '<div class="card"><div class="card-path">' + escape(entry["path"])
                + '</div><div class="card-blurb">' + escape(entry["blurb"])
                + '</div><div class="card-links"><a href="' + slug + '.html">PAGE</a>'
                + ' <a href="' + escape(open_link) + '" target="_blank" rel="noopener">OPEN FILE</a>'
                + "</div></div>"
            )
        sections.append(
            '<section><h2>' + escape(section["name"]) + "</h2>" + "".join(cards) + "</section>"
        )

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="site.css">
</head>
<body>
<header class="index-head">
  <h1>{title}</h1>
  <p class="subtitle">{subtitle}</p>
</header>
<section class="ladder-section">
  <h2>READING LADDER</h2>
  {ladder}
</section>
{sections}
<footer class="foot">
  {file_count} files, {total_chars} source chars
</footer>
</body>
</html>
""".format(
        title=escape(manifest["title"]),
        subtitle=escape(manifest["subtitle"]),
        ladder=ladder_html(),
        sections="".join(sections),
        file_count=file_count,
        total_chars=total_chars,
    )


CSS = """/* Atlas site stylesheet */
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #0d1117;
  color: #c9d1d9;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.6;
}
a { color: #58a6ff; text-decoration: none; }
a:hover { text-decoration: underline; }
header.index-head, header.page-head {
  padding: 2rem 2rem 1rem;
  border-bottom: 1px solid #21262d;
  background: #161b22;
}
header.index-head h1, header.page-head h1 { margin: 0 0 0.5rem; color: #f0f6fc; }
.subtitle { color: #8b949e; max-width: 60rem; }
.back { display: inline-block; margin-bottom: 1rem; font-size: 0.9rem; }
.open {
  display: inline-block;
  margin-top: 0.5rem;
  padding: 0.4rem 0.9rem;
  border: 1px solid #58a6ff;
  border-radius: 6px;
  color: #58a6ff;
}
.open:hover { background: #1f6feb; color: #fff; text-decoration: none; }
main.content, section { padding: 1.5rem 2rem; max-width: 70rem; }
section { border-bottom: 1px solid #21262d; }
h2 { color: #f0f6fc; border-bottom: 1px solid #21262d; padding-bottom: 0.3rem; }
h3 { color: #f0f6fc; }
.card {
  border: 1px solid #21262d;
  border-radius: 8px;
  padding: 0.9rem 1rem;
  margin: 0.7rem 0;
  background: #161b22;
}
.card-path { font-weight: 600; color: #f0f6fc; font-family: ui-monospace, monospace; }
.card-blurb { color: #8b949e; margin: 0.3rem 0; }
.card-links a { margin-right: 1rem; font-size: 0.9rem; }
.ladder { display: flex; flex-wrap: wrap; gap: 1rem; }
.tier { border: 1px solid #21262d; border-radius: 8px; padding: 0.8rem 1rem; background: #161b22; min-width: 16rem; }
.tier h3 { margin: 0 0 0.5rem; }
.tier ul { margin: 0; padding-left: 1.2rem; }
.tier li { margin: 0.2rem 0; }
.content h1, .content h2, .content h3, .content h4 { color: #f0f6fc; }
.content p { margin: 0.6rem 0; }
.content ul, .content ol { padding-left: 1.5rem; }
.content li { margin: 0.2rem 0; }
.content blockquote {
  margin: 0.6rem 0;
  padding: 0.2rem 1rem;
  border-left: 4px solid #30363d;
  color: #8b949e;
}
.content hr { border: 0; border-top: 1px solid #30363d; margin: 1.2rem 0; }
.content code {
  background: #21262d;
  padding: 0.1rem 0.35rem;
  border-radius: 4px;
  font-family: ui-monospace, monospace;
  font-size: 0.9em;
}
.content pre {
  background: #161b22;
  border: 1px solid #21262d;
  border-radius: 8px;
  padding: 1rem;
  overflow-x: auto;
}
.content pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 0.8rem 0; width: 100%; }
th, td { border: 1px solid #30363d; padding: 0.4rem 0.7rem; text-align: left; }
th { background: #21262d; color: #f0f6fc; }
.foot { padding: 1.5rem 2rem; color: #8b949e; font-size: 0.9rem; }
"""


def build(manifest_path=MANIFEST_PATH, site_dir=SITE_DIR, repo_root=REPO_ROOT):
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    os.makedirs(site_dir, exist_ok=True)

    with open(os.path.join(site_dir, "site.css"), "w", encoding="utf-8") as f:
        f.write(CSS)

    total_chars = 0
    file_count = 0

    seen = set()
    for section in manifest["sections"]:
        for entry in section["entries"]:
            path = entry["path"]
            full = os.path.join(repo_root, path)
            with open(full, "r", encoding="utf-8") as f:
                text = f.read()
            total_chars += len(text)
            file_count += 1
            body = render_content(path, text)
            slug = slugify(path)
            seen.add(path)
            with open(os.path.join(site_dir, slug + ".html"), "w", encoding="utf-8") as f:
                f.write(page_html(path, entry["blurb"], body))

    for _, paths in READING_LADDER:
        for path in paths:
            if path in seen:
                continue
            full = os.path.join(repo_root, path)
            if not os.path.exists(full):
                print("WARNING: skipping missing ladder file: " + path, file=sys.stderr)
                continue
            with open(full, "r", encoding="utf-8") as f:
                text = f.read()
            total_chars += len(text)
            file_count += 1
            body = render_content(path, text)
            slug = slugify(path)
            with open(os.path.join(site_dir, slug + ".html"), "w", encoding="utf-8") as f:
                f.write(page_html(path, "Reading ladder entry", body))

    with open(os.path.join(site_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html(manifest, total_chars, file_count))

    return file_count, total_chars


def main():
    count, chars = build()
    print("Built {} files, {} source chars -> {}".format(count, chars, SITE_DIR))


if __name__ == "__main__":
    main()
