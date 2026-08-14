#!/usr/bin/env python3
"""Tests for atlas/build.py. Plain python3, no external deps.

Runs the build against a temp copy of the manifest with a crafted file
containing a script tag and a table, then asserts escaping, table
rendering, page generation, source presence, and OPEN FILE targets.
"""

import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as atlas

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATLAS_DIR = os.path.join(REPO_ROOT, "atlas")


def make_manifest(tmp):
    manifest = {
        "title": "Test Atlas",
        "subtitle": "Test subtitle",
        "sections": [
            {
                "name": "Test Section",
                "entries": [
                    {"path": "docs/note.md", "blurb": "A note with a table and script"},
                    {"path": "scaffold/code.py", "blurb": "A code file"},
                ],
            }
        ],
    }
    mpath = os.path.join(tmp, "manifest.json")
    with open(mpath, "w", encoding="utf-8") as f:
        json.dump(manifest, f)

    note = os.path.join(tmp, "docs", "note.md")
    os.makedirs(os.path.dirname(note), exist_ok=True)
    with open(note, "w", encoding="utf-8") as f:
        f.write(
            "A plain paragraph that survives rendering.\n\n"
            "# Heading\n\n"
            "<script>alert(1)</script>\n\n"
            "| A | B |\n|---|---|\n| x | **y** |\n"
        )

    code = os.path.join(tmp, "scaffold", "code.py")
    os.makedirs(os.path.dirname(code), exist_ok=True)
    with open(code, "w", encoding="utf-8") as f:
        f.write("def hello():\n    return '<b>hi</b>'\n")

    for _, paths in atlas.READING_LADDER:
        for rel in paths:
            src = os.path.join(REPO_ROOT, rel)
            if not os.path.exists(src):
                continue
            dst = os.path.join(tmp, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)

    return mpath


def main():
    tmp = tempfile.mkdtemp(prefix="atlas-test-")
    try:
        mpath = make_manifest(tmp)
        site = os.path.join(tmp, "atlas", "site")
        atlas.build(manifest_path=mpath, site_dir=site, repo_root=tmp)

        with open(os.path.join(site, "docs-note-md.html"), "r", encoding="utf-8") as f:
            note_html = f.read()

        assert "<script>alert(1)</script>" not in note_html, "script tag not escaped"
        assert "&lt;script&gt;alert(1)&lt;/script&gt;" in note_html, "escaped script missing"
        assert "<table>" in note_html, "table not rendered"
        assert "<th>A</th>" in note_html, "table header missing"
        assert "<strong>y</strong>" in note_html, "bold inside cell missing"

        with open(os.path.join(site, "scaffold-code-py.html"), "r", encoding="utf-8") as f:
            code_html = f.read()
        assert "&lt;b&gt;hi&lt;/b&gt;" in code_html, "code block not escaped"

        for slug in ("docs-note-md", "scaffold-code-py"):
            page = os.path.join(site, slug + ".html")
            assert os.path.exists(page), "page missing: " + slug
            with open(page, "r", encoding="utf-8") as f:
                content = f.read()
            src = "def hello():" if slug == "scaffold-code-py" else "A plain paragraph that survives"
            assert src[:40] in content, "source head not present in " + slug

        for entry in ("docs/note.md", "scaffold/code.py"):
            target = os.path.join(site, "..", "..", entry)
            assert os.path.exists(target), "OPEN FILE target missing: " + entry

        assert os.path.exists(os.path.join(site, "index.html")), "index missing"
        assert os.path.exists(os.path.join(site, "site.css")), "css missing"

        print("ALL TESTS PASSED")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
