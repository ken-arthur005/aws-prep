"""Propose within-bank duplicates for editorial review, including reordered options."""
import json
import argparse
from pathlib import Path
from prepare_html import norm, words, ratio, option_match

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study-pool",action="store_true",help="Audit the final eligible pool, including native HTML additions")
    parser.add_argument("--min-overlap",type=float,default=.62)
    parser.add_argument("--min-prompt",type=float,default=.88)
    parser.add_argument("--min-option",type=float,default=.72)
    args=parser.parse_args()
    bank=json.loads((ROOT/"data/questions.json").read_text(encoding="utf-8"))["questions"]
    ready=[q for q in bank if q["status"]=="ready" and (not q.get("duplicateOf") and not q.get("studyExcludedReason") if args.study_pool else q.get("batch")!="html")]
    tokens={q["id"]:words(q["prompt"]) for q in ready}
    rows=[]
    for i,a in enumerate(ready):
        for b in ready[i+1:]:
            if len(a["options"])!=len(b["options"]) or a["select"]!=b["select"]:continue
            aw,bw=tokens[a["id"]],tokens[b["id"]]
            overlap=len(aw&bw)/max(1,len(aw|bw))
            if overlap<args.min_overlap:continue
            score=ratio(a["prompt"],b["prompt"])
            if score<args.min_prompt:continue
            align=option_match(b["options"],a["options"])
            if align["optionScore"]<args.min_option:continue
            rows.append({"canonical":a["id"],"duplicate":b["id"],"numbers":[a["number"],b["number"]],"promptScore":round(score,4),**align,"keysAgree":set(align["optionMap"][n] for n in b["correct"])==set(a["correct"]),"prompt":a["prompt"],"otherPrompt":b["prompt"]})
    (ROOT/"data/bank-duplicate-candidates.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (ROOT/"data/bank-duplicate-review.txt").write_text("\n".join(f"{r['numbers']} p={r['promptScore']} o={r['optionScore']} keys={r['keysAgree']} | {r['prompt']}\n  Other: {r['otherPrompt']}" for r in rows),encoding="utf-8")
    print(f"{len(rows)} within-bank pairs require review")

if __name__=="__main__":main()
