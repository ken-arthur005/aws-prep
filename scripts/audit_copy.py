"""Local editorial packets for the complete bank; never sends question text to a service."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    bank = json.loads((ROOT / "data/questions.json").read_text(encoding="utf-8"))["questions"]
    packets = []
    for q in bank:
        if q["status"] != "ready":
            continue
        packets.extend([f"\n#{q['number']} {q['id']} | select {q['select']}", q["prompt"]])
        packets.extend(f"{chr(65+i)} {value}" for i,value in enumerate(q["options"]))
    (ROOT / "data/copyedit-packet.txt").write_text("\n".join(packets),encoding="utf-8")
    from copyedit_content import FIELDS
    focused=[]
    for q in bank:
        if q["number"] not in FIELDS: continue
        focused.extend([f"\n#{q['number']} | select {q['select']}",q["prompt"]])
        focused.extend(f"{chr(65+i)} {v}" for i,v in enumerate(q["options"]))
    (ROOT/"data/copyedit-focus.txt").write_text("\n".join(focused),encoding="utf-8")
    remaining={11,148,170,172,180,181,188,190,193,201,247,249,250,271,285,298,303,307,311,326,330,348,352,353,636,649,997,1023}
    context=[]
    for q in bank:
        if q["number"] not in remaining: continue
        context.extend([f"\n#{q['number']}",q["prompt"]])
        context.extend(f"{chr(65+i)} {v}" for i,v in enumerate(q["options"]))
    (ROOT/"data/copyedit-context.txt").write_text("\n".join(context),encoding="utf-8")
    boundaries=[]
    pattern=re.compile(r"[A-Za-z0-9)] (?=(?:In the|After|During|Leadership|Management|Finance|Product|Security|Compliance|Customers|Users|Applications|Developers|Operations|Auditors|Analysts|All|Each|Once|Several|Some|Since)\b)")
    for q in bank:
        if q["status"]!="ready":continue
        for match in pattern.finditer(q["prompt"]):
            boundaries.append(f"#{q['number']} ...{q['prompt'][max(0,match.start()-45):match.end()+85]}...")
    (ROOT/"data/copyedit-boundaries.txt").write_text("\n".join(boundaries),encoding="utf-8")
    spelling = ROOT / "data/copyedit-spelling.json"
    if spelling.exists():
        misses = json.loads(spelling.read_text(encoding="utf-8"))
        candidates = [r for r in misses if re.fullmatch(r"[a-z]+",r["word"]) and r["suggestions"]]
        (ROOT / "data/copyedit-word-candidates.txt").write_text("\n".join(f"{r['word']} {','.join(r['locations'])} -> {','.join(r['suggestions'])}" for r in candidates),encoding="utf-8")
    print({"records":len(bank),"ready":sum(q["status"]=="ready" for q in bank),"promptCharacters":sum(len(q["prompt"]) for q in bank),"optionCharacters":sum(sum(map(len,q["options"])) for q in bank),"explanationCharacters":sum(sum(map(len,q["explanations"])) for q in bank)})

if __name__ == "__main__":
    main()
