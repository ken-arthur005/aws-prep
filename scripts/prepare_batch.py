"""Parse a separate OCR batch and propose (never approve) cross-bank duplicates."""
import json
import re
from difflib import SequenceMatcher
from itertools import permutations
from pathlib import Path
from parse_questions import parse

ROOT = Path(__file__).resolve().parents[1]

def norm(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())

def main():
    raw = json.loads((ROOT / "data/new-ocr.json").read_text(encoding="utf-8"))
    bank = json.loads((ROOT / "data/questions.json").read_text(encoding="utf-8"))["questions"]
    old = [(q, norm(q["prompt"]), set(re.findall(r"[a-z0-9]+",q["prompt"].lower()))) for q in bank if q.get("batch") != "november"]
    parsed = []
    for i, item in enumerate(raw):
        q = parse(item)
        # Preserve the old filename IDs; collection namespace prevents future source collisions.
        q["id"] = "nov-" + q["id"][2:]
        q["index"] = i
        a = norm(q["prompt"])
        candidates = []
        words = set(re.findall(r"[a-z0-9]+", q["prompt"].lower()))
        likely = sorted(old, key=lambda p: len(words & p[2]) / max(1,len(words | p[2])), reverse=True)[:4]
        for prior, b, _ in likely:
            if not a or min(len(a),len(b)) / max(len(a),len(b)) < .72:
                continue
            score = SequenceMatcher(None, a, b, autojunk=False).ratio()
            if score > .84:
                candidates.append((score, prior))
        if candidates:
            score, prior = max(candidates, key=lambda x:x[0])
            q["candidate"] = {"id": prior["id"], "number": prior["number"], "promptScore": round(score,4)}
            if len(q["options"]) == len(prior["options"]) and 4 <= len(q["options"]) <= 6:
                similarities = [[SequenceMatcher(None,norm(a),norm(b),autojunk=False).ratio() for b in prior["options"]] for a in q["options"]]
                mapping = max(permutations(range(len(q["options"]))),key=lambda p:sum(similarities[j][p[j]] for j in range(len(p))))
                q["candidate"].update({"optionMap":list(mapping), "optionScore":round(min(similarities[j][mapping[j]] for j in range(len(mapping))),4)})
        parsed.append(q)
    (ROOT / "data/new-extracted.json").write_text(json.dumps(parsed,ensure_ascii=False,indent=2),encoding="utf-8")
    lines = []
    for q in parsed:
        lines.extend([f"\n[{q['index']:03}] {q['source']} | select {q['select']} | {q.get('candidate','NEW')}", q["prompt"]])
        lines.extend(f"{chr(65+i)}. {o}" for i,o in enumerate(q["options"]))
    (ROOT / "data/new-review.txt").write_text("\n".join(lines),encoding="utf-8")
    groups = {}
    unique = []
    for q in parsed:
        key = (norm(q["prompt"]), tuple(sorted(norm(o) for o in q["options"])), q["select"])
        if key in groups:
            continue
        groups[key] = q["index"]
        candidate = q.get("candidate", {})
        if candidate.get("promptScore",0) >= .985 and candidate.get("optionScore",0) >= .94:
            continue
        unique.extend([f"\n[{q['index']:03}] {q['source']} | select {q['select']} | {candidate or 'NEW'}",q["prompt"]])
        unique.extend(f"{chr(65+i)}. {o}" for i,o in enumerate(q["options"]))
    (ROOT / "data/new-unique-review.txt").write_text("\n".join(unique),encoding="utf-8")
    print(f"Parsed {len(parsed)}; duplicate candidates {sum('candidate' in q for q in parsed)}; complete option counts {sum(4 <= len(q['options']) <= 6 for q in parsed)}")

if __name__ == "__main__":
    main()
