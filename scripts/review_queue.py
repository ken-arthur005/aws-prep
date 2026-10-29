"""Produce bounded editorial worksheets without losing any question text."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
bank = json.loads((ROOT / "data/questions.json").read_text(encoding="utf-8"))
out = ROOT / "data/review-queue"
out.mkdir(exist_ok=True)
for stale in [*out.glob("review-*.txt"), *out.glob("legacy-*.txt")]:
    stale.unlink()
for status in ["review", "legacy"]:
    questions = [q for q in bank["questions"] if q["status"] == status]
    for start in range(0, len(questions), 40):
        lines = []
        for q in questions[start:start+40]:
            lines += [f"\n[{q['number']-1:03d}] {q['id']} | choose {q['select']} | {q['sources'][0]}", q["prompt"]]
            lines.extend(f"{chr(65+i)}. {text}" for i, text in enumerate(q["options"]))
            if status == "legacy":
                lines.append("Previous exclusion: " + q["note"])
        (out / f"{status}-{start//40+1:02d}.txt").write_text("\n".join(lines), encoding="utf-8")
    print(status, len(questions), "records", (len(questions)+39)//40, "worksheets")
sources = json.loads((ROOT / "data/extracted.json").read_text(encoding="utf-8"))
print("Source-order SHA256:", hashlib.sha256("\n".join(q["source"] for q in sources).encode()).hexdigest())
groups = ROOT / "data/source-groups.json"
if not groups.exists():
    source_indices = {q["source"]: i for i, q in enumerate(sources)}
    recorded = [{"canonicalIndex": q["number"]-1, "otherIndices": [source_indices[name] for name in q["sources"] if source_indices[name] != q["number"]-1]} for q in bank["questions"] if len(q["sources"]) > 1]
    groups.write_text(json.dumps(recorded, indent=2), encoding="utf-8")
    print("Recorded", len(recorded), "already-established duplicate/continuation groups")
for q in bank["questions"]:
    if q["status"] == "legacy" and (len(q["note"]) < 100 or not q["readMore"]):
        print("Incomplete exclusion note/reference", q["number"]-1, len(q["note"]), q["readMore"])
    if q["status"] == "ready":
        for i, explanation in enumerate(q["explanations"]):
            if len(explanation) < 40:
                print("Short rationale", q["number"]-1, chr(65+i), explanation)
