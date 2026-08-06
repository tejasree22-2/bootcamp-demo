#!/usr/bin/env python3
"""
update.py — Scans participants/*/info.json and injects participant cards
into the main index.html between the PARTICIPANTS_START / PARTICIPANTS_END markers.
Also appends a new run section to run-history.html showing newly merged students.

Usage:
    python update.py
"""

import os
import json
import re
from html import escape
from datetime import datetime, timezone, timedelta

PARTICIPANTS_DIR = os.path.join(os.path.dirname(__file__), "participants")
MAIN_HTML = os.path.join(os.path.dirname(__file__), "index.html")
HISTORY_HTML = os.path.join(os.path.dirname(__file__), "run-history.html")

START_MARKER = "<!-- PARTICIPANTS_START -->"
END_MARKER = "<!-- PARTICIPANTS_END -->"

RUNS_START = "<!-- RUNS_START -->"
RUNS_END = "<!-- RUNS_END -->"


def initials(name):
    parts = name.strip().split()
    return "".join(w[0] for w in parts if w)[:2].upper()


def make_card(folder, info):
    name = escape(info.get("name", folder))
    roll_no = escape(str(info.get("roll_no", "")))
    photo_raw = info.get("photo", "")
    photo = escape(photo_raw) if photo_raw.startswith("https://") else ""
    href = f"participants/{folder}/index.html"

    if photo:
        avatar_html = (
            f'<div class="card-avatar">'
            f'<img src="{photo}" alt="{name}" loading="lazy" '
            f'onerror="this.parentElement.textContent=&quot;{initials(name)}&quot;">'
            f'</div>'
        )
    else:
        avatar_html = f'<div class="card-avatar">{initials(name)}</div>'

    return (
        f'<a class="card" href="{href}">\n'
        f'  {avatar_html}\n'
        f'  <div class="card-name">{name}</div>\n'
        f'  <div class="card-roll">{roll_no}</div>\n'
        f'  <div class="card-arrow">View Profile &rarr;</div>\n'
        f'</a>'
    )


def get_existing_folders(html):
    """Extract participant folder names already listed in index.html."""
    return set(re.findall(r'href="participants/([^/]+)/index\.html"', html))


def get_run_count(history_html):
    """Count how many runs have been recorded in run-history.html."""
    return len(re.findall(r'class="run-block"', history_html))


def make_run_block(run_number, timestamp, new_entries):
    rows = ""
    if new_entries:
        for folder, info in new_entries:
            name = escape(info.get("name", folder))
            roll_no = escape(str(info.get("roll_no", "?")))
            href = f"participants/{folder}/index.html"
            rows += (
                f'        <tr>'
                f'<td><a href="{href}">{roll_no}</a></td>'
                f'<td>{name}</td>'
                f'</tr>\n'
            )
        table = (
            f'      <table>\n'
            f'        <thead><tr><th>Roll No</th><th>Name</th></tr></thead>\n'
            f'        <tbody>\n{rows}        </tbody>\n'
            f'      </table>\n'
        )
    else:
        table = '      <p class="no-new">No new participants this run.</p>\n'

    count_label = f"{len(new_entries)} new student{'s' if len(new_entries) != 1 else ''}"

    return (
        f'    <div class="run-block">\n'
        f'      <div class="run-header">\n'
        f'        <span class="run-title">Run #{run_number}</span>\n'
        f'        <span class="run-meta">{timestamp} &mdash; {count_label}</span>\n'
        f'      </div>\n'
        f'{table}'
        f'    </div>\n'
    )


def init_history_file():
    """Create run-history.html if it doesn't exist."""
    content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Run History — Bootcamp Participants</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f4f6f9; color: #1a1a2e; padding: 2rem; }
    h1 { font-size: 1.6rem; margin-bottom: 0.4rem; }
    .subtitle { color: #555; margin-bottom: 2rem; font-size: 0.95rem; }
    .run-block {
      background: #fff;
      border: 1px solid #e0e0e0;
      border-radius: 10px;
      margin-bottom: 1.5rem;
      overflow: hidden;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .run-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.9rem 1.2rem;
      background: #1a1a2e;
      color: #fff;
    }
    .run-title { font-weight: 700; font-size: 1rem; }
    .run-meta { font-size: 0.82rem; opacity: 0.75; }
    table { width: 100%; border-collapse: collapse; }
    thead { background: #f0f2f5; }
    th, td { padding: 0.65rem 1.2rem; text-align: left; font-size: 0.9rem; border-bottom: 1px solid #eee; }
    td a { color: #4f46e5; text-decoration: none; font-weight: 600; }
    td a:hover { text-decoration: underline; }
    .no-new { padding: 0.8rem 1.2rem; color: #888; font-size: 0.9rem; }
  </style>
</head>
<body>
  <h1>Run History</h1>
  <p class="subtitle">Each section shows students whose pull requests were merged since the previous run.</p>

<!-- RUNS_START -->
<!-- RUNS_END -->

</body>
</html>
"""
    with open(HISTORY_HTML, "w", encoding="utf-8") as f:
        f.write(content)
    print("  Created run-history.html")


def append_run(new_entries):
    """Append a new run block to run-history.html."""
    if not os.path.isfile(HISTORY_HTML):
        init_history_file()

    with open(HISTORY_HTML, encoding="utf-8") as f:
        history = f.read()

    run_number = get_run_count(history) + 1
    IST = timezone(timedelta(hours=5, minutes=30))
    timestamp = datetime.now(IST).strftime("%Y-%m-%d %I:%M %p IST")
    block = make_run_block(run_number, timestamp, new_entries)

    updated = history.replace(
        RUNS_END,
        f"{block}{RUNS_END}"
    )

    with open(HISTORY_HTML, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"  Run #{run_number} appended to run-history.html — {len(new_entries)} new student(s)")


def main():
    if not os.path.isdir(PARTICIPANTS_DIR):
        print(f"ERROR: participants/ directory not found at {PARTICIPANTS_DIR}")
        return

    with open(MAIN_HTML, encoding="utf-8") as f:
        html = f.read()

    existing_folders = get_existing_folders(html)

    entries = []
    new_entries = []

    for folder in sorted(os.listdir(PARTICIPANTS_DIR)):
        folder_path = os.path.join(PARTICIPANTS_DIR, folder)
        info_path = os.path.join(folder_path, "info.json")

        if not os.path.isdir(folder_path):
            continue
        if not os.path.isfile(info_path):
            continue

        try:
            with open(info_path, encoding="utf-8") as f:
                info = json.load(f)
            entries.append((folder, info))
            if folder not in existing_folders:
                new_entries.append((folder, info))
            print(f"  Found: {folder}  →  {info.get('name', '?')} ({info.get('roll_no', '?')})")
        except json.JSONDecodeError as e:
            print(f"  SKIP {folder}: invalid info.json — {e}")

    if not entries:
        cards_html = '    <div class="empty">No participants yet.</div>'
    else:
        cards_html = "\n".join(make_card(f, i) for f, i in entries)

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL,
    )

    if not pattern.search(html):
        print("ERROR: Could not find PARTICIPANTS_START / PARTICIPANTS_END markers in index.html")
        return

    new_html = pattern.sub(
        f"{START_MARKER}\n{cards_html}\n{END_MARKER}",
        html,
    )

    with open(MAIN_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"\nDone! {len(entries)} participant(s) written to index.html")

    # Append run to history
    append_run(new_entries)


if __name__ == "__main__":
    main()
