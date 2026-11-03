"""Extract only the JSON literal from the supplied quiz; never execute its scripts.

Matching is a review aid. Raw screenshot variants and the copy-edit ledger help
recognise OCR differences; no similarity score approves an answer or a merge.
"""
import hashlib
import itertools
import json
import re
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "public/resources/saa-c03-quiz (offline).html"

def norm(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())

def words(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def ratio(a, b):
    return SequenceMatcher(None, norm(a), norm(b), autojunk=False).ratio()

def option_match(a, b):
    if len(a) != len(b): return None
    scores = [[ratio(x,y) for y in b] for x in a]
    mapping = max(itertools.permutations(range(len(a))), key=lambda m:sum(scores[i][m[i]] for i in range(len(m))))
    return {"optionMap":list(mapping), "optionScore":round(min(scores[i][mapping[i]] for i in range(len(mapping))),4), "optionMean":round(sum(scores[i][mapping[i]] for i in range(len(mapping)))/len(mapping),4)}

def main():
    html = HTML.read_text(encoding="utf-8")
    match = re.search(r"const Q=(\[[\s\S]*?\]);\s*const DN=", html)
    assert match, "Question JSON literal not found"
    raw = json.loads(match[1])
    assert len(raw)==322 and len({q["id"] for q in raw})==322
    digest = hashlib.sha256(match[1].encode()).hexdigest()
    extracted=[]
    for item in raw:
        assert item["n"]==len(item["a"]) and len(set(item["a"]))==len(item["a"])
        assert all(isinstance(i,int) and 0<=i<len(item["o"]) for i in item["a"])
        extracted.append({"id":f"html-{item['id']:03}", "importId":item["id"], "prompt":item["q"], "options":item["o"], "select":item["n"], "suggestedCorrect":item["a"], "suggestedExplanation":item["e"], "suggestedDomain":item["d"]})
    (ROOT/"data/html-extracted.json").write_text(json.dumps({"checksum":digest,"records":extracted},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    bank=json.loads((ROOT/"data/questions.json").read_text(encoding="utf-8"))["questions"]
    bank=[q for q in bank if q.get("batch")!="html"]
    lookup={q["id"]:q for q in bank}
    source_targets={source:q["id"] for q in bank for source in q["sources"]}
    ledger=json.loads((ROOT/"data/copy-edit-review.json").read_text(encoding="utf-8"))["edits"]
    variants=[]
    for q in bank:
        variants.append((q["id"],q["prompt"],q["options"]))
        edits=ledger.get(q["id"],{}).get("fields",{})
        variants.append((q["id"],edits.get("prompt",{}).get("before",q["prompt"]),[edits.get(f"options.{i}",{}).get("before",v) for i,v in enumerate(q["options"])]))
    for name in ["extracted.json","new-extracted.json"]:
        for q in json.loads((ROOT/"data"/name).read_text(encoding="utf-8")):
            target=source_targets.get(q["source"])
            if target and len(q["options"])>=3:variants.append((target,q["prompt"],q["options"]))
    variants=[(id,prompt,options,words(prompt+" "+" ".join(options))) for id,prompt,options in variants]
    reports=[]
    for i,q in enumerate(extracted):
        tokens=words(q["prompt"]+" "+" ".join(q["options"]))
        likely=sorted(variants,key=lambda v:len(tokens&v[3])/max(1,len(tokens|v[3])),reverse=True)[:8]
        matches={}
        for id,prompt,options,_ in likely:
            align=option_match(q["options"],options)
            if not align:continue
            p=ratio(q["prompt"],prompt)
            candidate={"id":id,"number":lookup[id]["number"],"status":lookup[id]["status"],"promptScore":round(p,4),**align}
            candidate["score"]=round(.55*p+.45*align["optionMean"],4)
            if id not in matches or candidate["score"]>matches[id]["score"]:matches[id]=candidate
        candidates=sorted(matches.values(),key=lambda m:m["score"],reverse=True)[:3]
        reports.append({"importId":q["importId"],"candidates":candidates})
        if (i+1)%50==0:print(f"Matched {i+1}/{len(extracted)}",flush=True)
    (ROOT/"data/html-match-candidates.json").write_text(json.dumps(reports,indent=2)+"\n",encoding="utf-8")
    lines=[]
    for q,r in zip(extracted,reports):
        lines.extend([f"\nHTML {q['importId']:03} | select {q['select']} | {r['candidates']}",q["prompt"]])
        lines.extend(f"{chr(65+i)}. {o}" for i,o in enumerate(q["options"]))
        lines.extend(["Provisional AI key: "+str(q["suggestedCorrect"]),q["suggestedExplanation"]])
    (ROOT/"data/html-review-packet.txt").write_text("\n".join(lines),encoding="utf-8")
    weaker=[]
    summary=[]
    for q,r in zip(extracted,reports):
        best=r["candidates"][0] if r["candidates"] else {}
        strong=best.get("promptScore",0)>=.9 and best.get("optionScore",0)>=.8
        summary.append(f"{q['importId']:03} {'MATCH' if strong else 'REVIEW'} -> {best.get('number')} p={best.get('promptScore')} o={best.get('optionScore')} | {q['prompt'][:100]}")
        if not strong:
            weaker.extend([f"\nHTML {q['importId']:03} | select {q['select']} | {r['candidates']}",q["prompt"]])
            weaker.extend(f"{chr(65+i)}. {o}" for i,o in enumerate(q["options"]))
            weaker.extend(["Provisional AI key: "+str(q["suggestedCorrect"]),q["suggestedExplanation"]])
    (ROOT/"data/html-review-weaker.txt").write_text("\n".join(weaker),encoding="utf-8")
    (ROOT/"data/html-review-summary.txt").write_text("\n".join(summary),encoding="utf-8")
    print("HTML checksum:",digest)
    print("Strong matching proposals:",sum(bool(r["candidates"]) and r["candidates"][0]["promptScore"]>=.9 and r["candidates"][0]["optionScore"]>=.8 for r in reports))

if __name__=="__main__":main()
