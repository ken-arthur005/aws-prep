"""Repair reading order only when every meaningful OCR token is preserved.

This never changes option count/order, answer keys or the frozen source extraction.
Editorial corrections in content.py/content_remaining.py take precedence.
"""
from collections import Counter
import json
from pathlib import Path
import re

from parse_questions import parse

root = Path(__file__).resolve().parents[1]
raw = json.loads((root / "data/ocr.json").read_text(encoding="utf-8"))
old = json.loads((root / "data/extracted.json").read_text(encoding="utf-8"))


def tokens(text):
    return Counter(t for t in re.findall(r"\S+", text) if t not in {"O", "o", "○", "©", "✓", "✔"})


repairs = {}
changed_options = 0
for index, (original, ocr) in enumerate(zip(old, raw)):
    assert original["source"] == ocr["source"]
    parsed = parse(ocr)
    change = {}
    if parsed["prompt"] != original["prompt"] and tokens(parsed["prompt"]) == tokens(original["prompt"]):
        change["prompt"] = parsed["prompt"]
    if len(parsed["options"]) == len(original["options"]):
        options = {}
        for i, (before, after) in enumerate(zip(original["options"], parsed["options"])):
            if before != after and tokens(before) == tokens(after):
                options[str(i)] = after
        if options:
            change["option"] = options
            changed_options += len(options)
    if change:
        repairs[str(index)] = change
(root / "data/text-repairs.json").write_text(json.dumps(repairs, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Token-preserving reading-order repairs: {len(repairs)} captures, {changed_options} options")
