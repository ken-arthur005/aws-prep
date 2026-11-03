"""Native HTML-question import using closed editorial decisions, never the supplied key."""
import hashlib
import json
import re
import textwrap
from pathlib import Path
from content_html import REVIEWS, HOLDS, MATCHES, PRIMARY, STUDY_EXCLUSIONS, BANK_DUPLICATES, RECOVERED_SOURCES
from prepare_html import option_match

ROOT=Path(__file__).resolve().parents[1]
CHECKSUM="b2bf0714eb026874be87b5b87bcdeff6aecb40c36ad5400a37a71b4c6e493e75"

def extend_html(bank):
    extracted=json.loads((ROOT/"data/html-extracted.json").read_text(encoding="utf-8"))
    actual=(ROOT/"public/resources/saa-c03-quiz (offline).html").read_text(encoding="utf-8")
    literal=re.search(r"const Q=(\[[\s\S]*?\]);\s*const DN=",actual)[1]
    assert extracted["checksum"]==CHECKSUM==hashlib.sha256(literal.encode()).hexdigest(),"HTML changed: re-review before import"
    records=extracted["records"]
    assert {r["importId"] for r in records}==set(range(1,323))
    decisions=set(REVIEWS)|set(HOLDS)|set(MATCHES)
    assert decisions==set(range(1,323)),f"Unreviewed or invalid import IDs: {set(range(1,323))^decisions}"
    assert not(set(REVIEWS)&set(HOLDS) or set(REVIEWS)&set(MATCHES) or set(HOLDS)&set(MATCHES))
    for item in records:
        i=item["importId"]
        if i not in REVIEWS:continue
        review=REVIEWS[i]
        assert len(review["correct"])==item["select"] and len(review["options"])==len(item["options"]),i
        assert len(review["explanations"])==len(review["options"]) and all(len(e)>=40 for e in review["explanations"]),i
        assert len(set(review["correct"]))==len(review["correct"]) and all(0<=n<len(review["options"]) for n in review["correct"]),i
        bank.append({"id":item["id"],"number":1041+i,"title":textwrap.shorten(review["takeaway"],width=106,placeholder="…"),"prompt":review["prompt"],"options":review["options"],"select":item["select"],"correct":review["correct"],"explanations":review["explanations"],"takeaway":review["takeaway"],"domain":review["domain"],"topic":review["topic"],"sources":[],"sourcePaths":[],"status":"ready","note":review["note"],"adapted":bool(review["note"]),"batch":"html","readMore":[{"title":PRIMARY[k][0],"url":PRIMARY[k][1]} for k in review["refs"]]})
    return records

def finalize_study_pool(bank, records, aliases):
    by_number={q["number"]:q for q in bank}
    by_id={q["id"]:q for q in bank}
    equivalents={}
    for canonical_n,duplicate_n in BANK_DUPLICATES:
        canonical,duplicate=by_number[canonical_n],by_number[duplicate_n]
        assert canonical["status"]==duplicate["status"]=="ready"
        mapping=option_match(duplicate["options"],canonical["options"])["optionMap"]
        assert {mapping[n] for n in duplicate["correct"]}==set(canonical["correct"]),(canonical_n,duplicate_n,"incompatible keys")
        duplicate["duplicateOf"]=canonical["id"]
        equivalents[duplicate["id"]]={"canonicalId":canonical["id"],"optionMap":mapping}
        aliases[duplicate["id"]]=canonical["id"]
    for number,reason in STUDY_EXCLUSIONS.items():
        by_number[number]["studyExcludedReason"]=reason
    for number,target in RECOVERED_SOURCES.items():
        assert by_number[number]["status"]!="ready" and target in by_id
        by_number[number]["duplicateOf"]=target
        aliases[by_number[number]["id"]]=target
    def canonical_id(id):
        seen=set()
        while by_id[id].get("duplicateOf"):
            assert id not in seen,"Cyclic study duplicate"
            seen.add(id);id=by_id[id]["duplicateOf"]
        return id
    # Flatten bookmark aliases, including old source captures whose canonical record
    # is now a retained history duplicate. Historical session answers are not mutated.
    for old,target in list(aliases.items()):aliases[old]=canonical_id(target)
    report_rows=[]
    for item in records:
        i=item["importId"]
        if i in REVIEWS:
            report_rows.append({"importId":i,"disposition":"added","questionId":item["id"],"answerIndependentlyReviewed":True,"sameAnswerPositionsAsSupplied":item["suggestedCorrect"]==REVIEWS[i]["correct"]})
        elif i in HOLDS:
            report_rows.append({"importId":i,"disposition":"excluded","reason":HOLDS[i]})
        else:
            target=MATCHES[i]
            q=by_number[target] if isinstance(target,int) else by_id[target]
            target_id=canonical_id(q["id"])
            target_q=by_id[target_id]
            aliases[item["id"]]=target_id
            report_rows.append({"importId":i,"disposition":"matched","questionId":target_id,"studyEligible":target_q["status"]=="ready" and not target_q.get("studyExcludedReason")})
    active=[q for q in bank if q["status"]=="ready" and not q.get("duplicateOf") and not q.get("studyExcludedReason")]
    exact=set()
    for q in active:
        key=(re.sub(r"[^a-z0-9]","",q["prompt"].lower()),tuple(sorted(re.sub(r"[^a-z0-9]","",o.lower()) for o in q["options"])),q["select"])
        assert key not in exact,f"Exact study duplicate remains: {q['id']}"
        exact.add(key)
    excluded=[q["id"] for q in bank if q["status"]!="ready" or q.get("studyExcludedReason")]
    (ROOT/"data/question-equivalents.json").write_text(json.dumps({"duplicates":equivalents,"excludedIds":excluded},indent=2)+"\n",encoding="utf-8")
    summary={"sourceRecords":322,"added":len(REVIEWS),"matched":len(MATCHES),"excluded":len(HOLDS),"retainedHistoryDuplicates":sum(bool(q.get("duplicateOf")) for q in bank),"additionalStudyExclusions":len(STUDY_EXCLUSIONS),"studyReady":len(active),"checksum":CHECKSUM,"records":report_rows}
    (ROOT/"data/html-review.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    print("Native HTML integration:",{k:v for k,v in summary.items() if k!="records"})
    return summary
