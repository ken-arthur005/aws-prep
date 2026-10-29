"""Build the shipped question bank and a traceable source coverage report."""
import json
import re
import textwrap
import hashlib
from difflib import SequenceMatcher
from pathlib import Path
from content import REVIEWS, HOLDS, FIXES, MERGES, DOCS
import content_remaining  # noqa: F401 - applies the second editorial pass

ROOT = Path(__file__).resolve().parents[1]


def normalize(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def tidy(text):
    for pattern, replacement in [(r"\bECO\b", "EC2"), (r"\bSS\b", "S3"), (r"\bS\?\b", "S3"), (r"\bstl\b", "st1"), (r"\bscl\b", "sc1"), (r"\biol\b", "io1"), (r"\bi02\b", "io2"), (r"confguration", "configuration"), (r"encrypt-on", "encryption"), (r"lovAatency", "low-latency"), (r"\bwvwn\.", "www."), (r"AmazonAurora", "Amazon Aurora"), (r"AmazonTranscribe", "Amazon Transcribe")]:
        text = re.sub(pattern, replacement, text)
    return text.strip()


TOPICS = [
    ("secure", "Encryption & key management", r"encrypt|kms|certificate|ssl|tls|cloudhsm", "kms"),
    ("secure", "Identity & access", r"iam|identity|cognito|sts|permission|service control|scp|root user", "iam"),
    ("secure", "Network security", r"security group|network acl|firewall|\bwaf\b|shield|ddos", "vpc"),
    ("resilient", "Disaster recovery", r"rto|rpo|disaster|pilot light|warm standby", "dr"),
    ("resilient", "Messaging & integration", r"sqs|sns|loosely coupled|decoupl|message queue", "sqs"),
    ("cost", "Cost optimization", r"cost.effective|cost.optim|lowest cost|reduce.cost|savings plan|reserved instance|spot instance", "savings"),
    ("performance", "Database architecture", r"database|dynamodb|aurora|rds|mysql|postgres|neptune|documentdb", "rds"),
    ("performance", "DNS & routing", r"route 53|dns|cname|geolocation|routing policy", "routing"),
    ("performance", "Storage architecture", r"s3|\bebs\b|\befs\b|\bfsx\b|storage|glacier|file system", "s3"),
    ("resilient", "Compute & containers", r"ec2|lambda|container|ecs|eks|auto.scal", "as"),
    ("resilient", "Observability", r"cloudwatch|cloudtrail|monitor|logging|metrics|x-ray", "cloudwatch"),
]


def main():
    extracted = json.loads((ROOT / "data/extracted.json").read_text(encoding="utf-8"))
    text_repairs = json.loads((ROOT / "data/text-repairs.json").read_text(encoding="utf-8"))
    order_digest = hashlib.sha256("\n".join(q["source"] for q in extracted).encode()).hexdigest()
    assert order_digest == "63518cd8c46bfbaa86afb3b1ffccafe3e3e63777ace1815dca8e2043c875dc75", "Source order changed: review editorial source indexes before rebuilding."
    for group in json.loads((ROOT / "data/source-groups.json").read_text(encoding="utf-8")):
        parent = group["canonicalIndex"]
        MERGES[parent] = sorted(set(MERGES.get(parent, []) + group["otherIndices"]))
    children = {child for group in MERGES.values() for child in group}
    def descendants(parent, trail=()):
        assert parent not in trail, f"Cyclic source merge: {trail} -> {parent}"
        result = []
        for child in MERGES.get(parent, []):
            result.extend([child, *descendants(child, (*trail, parent))])
        return sorted(set(result))
    roots = {parent: descendants(parent) for parent in MERGES if parent not in children}
    MERGES.clear()
    MERGES.update(roots)
    consumed = {index for sources in MERGES.values() for index in sources}
    bank = []
    keys = {}
    manifest = []
    for index, source in enumerate(extracted):
        if index in consumed:
            continue
        q = {"id": source["id"], "number": index + 1, "prompt": tidy(source["prompt"]), "options": [tidy(o) for o in source["options"]], "select": source["select"], "sources": [source["source"]]}
        repair = text_repairs.get(str(index), {})
        q["prompt"] = tidy(repair.get("prompt", q["prompt"]))
        for position, text in repair.get("option", {}).items():
            q["options"][int(position)] = tidy(text)
        fix = FIXES.get(index, {})
        q["prompt"] = fix.get("prompt", q["prompt"])
        q["select"] = fix.get("select", q["select"])
        q["options"] = fix.get("options", q["options"])
        for option, text in fix.get("option", {}).items():
            if option < len(q["options"]):
                q["options"][option] = text
        q["sources"].extend(extracted[i]["source"] for i in MERGES.get(index, []))
        key = normalize(q["prompt"] + "|" + "|".join(q["options"]))
        duplicate = keys.get(key)
        if duplicate is None and len(q["prompt"]) > 100:
            for existing in bank:
                if len(existing["options"]) != len(q["options"]):
                    continue
                a, b = normalize(q["prompt"]), normalize(existing["prompt"])
                if a[:35] == b[:35] and abs(len(a)-len(b)) < 20 and SequenceMatcher(None, a, b).ratio() > .985 and all(SequenceMatcher(None, normalize(x), normalize(y)).ratio() > .97 for x, y in zip(q["options"], existing["options"])):
                    duplicate = existing
                    break
        if duplicate is not None:
            duplicate["sources"].extend(q["sources"])
            if index in REVIEWS and duplicate["status"] != "ready":
                apply_review(duplicate, REVIEWS[index])
            manifest.append({"sourceIndex": index, "source": source["source"], "questionId": duplicate["id"], "kind": "duplicate"})
            continue
        domain, topic, docs = "resilient", "Architecture tradeoffs", "dr"
        for d, t, pattern, doc in TOPICS:
            if re.search(pattern, q["prompt"], re.I):
                domain, topic, docs = d, t, doc
                break
        q.update({"domain": domain, "topic": topic, "correct": [], "explanations": [], "takeaway": "", "status": "review", "note": "Extracted source material awaiting independent answer and explanation review. Screenshot selections are not an answer key. This item is excluded from scored sessions.", "readMore": links([docs])})
        if not 4 <= len(q["options"]) <= 6 or len(q["prompt"]) < 50:
            q["note"] = "This screenshot is incomplete or its layout needs transcription review. Consult the original source. No answer is inferred and this item is excluded from scored sessions."
        if index in HOLDS:
            hold = HOLDS[index]
            q.update({k: hold[k] for k in ["domain", "topic", "note", "takeaway"]})
            q["readMore"] = links(hold["docs"])
            q["status"] = "legacy"
        if index in REVIEWS:
            apply_review(q, REVIEWS[index])
        q["adapted"] = bool(fix and re.search(r"editorial|clarif", q["note"], re.I))
        q["title"] = fix.get("title", textwrap.shorten(q["takeaway"].split(". ")[0].rstrip("."), width=108, placeholder="…") if q["takeaway"] else q["topic"] + ": " + " ".join(q["prompt"].split()[:13]).rstrip("?.") + "…")
        bank.append(q)
        keys[key] = q
        manifest.append({"sourceIndex": index, "source": source["source"], "questionId": q["id"], "kind": "question"})
    for parent, sources in MERGES.items():
        for source in sources:
            target = next(q for q in bank if extracted[parent]["source"] in q["sources"])
            manifest.append({"sourceIndex": source, "source": extracted[source]["source"], "questionId": target["id"], "kind": "continuation"})
    source_to_id = {source: q["id"] for q in bank for source in q["sources"]}
    pending = [q["number"] for q in bank if q["status"] == "review"]
    assert not pending, f"Editorial review required for records: {pending}"
    aliases = {item["id"]: source_to_id[item["source"]] for item in extracted if item["id"] != source_to_id[item["source"]]}
    assert len(source_to_id) == len(extracted), "A source was lost during merging."
    assert sum(len(q["sources"]) for q in bank) == len(extracted), "A source was assigned more than once."
    output = {"sourceCount": len(extracted), "reviewedAt": "2026-10-29", "aliases": aliases, "questions": bank}
    (ROOT / "data/questions.json").write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    report = {"sources": len(extracted), "uniqueRecords": len(bank), "studyReady": sum(q["status"] == "ready" for q in bank), "flagged": sum(q["status"] == "legacy" for q in bank), "awaitingReview": sum(q["status"] == "review" for q in bank), "manifest": sorted(manifest, key=lambda m: m["sourceIndex"])}
    (ROOT / "data/source-manifest.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (ROOT / "data/source-aliases.json").write_text(json.dumps(aliases, indent=2), encoding="utf-8")
    lines = ["# Editorial review report", "", "Reviewed: 2026-10-29. Original screenshot selections were disregarded.", "", f"- Uploaded screenshots: **{len(extracted)}**", f"- Combined question/source records: **{len(bank)}**", f"- Study-ready, with option-level explanations: **{report['studyReady']}**", f"- Reviewed exclusions: **{report['flagged']}**", f"- Awaiting review: **{report['awaitingReview']}**", "", "All sources are preserved in `source-manifest.json`; merged capture IDs are recorded in `source-aliases.json`.", "Substantive wording corrections are labeled in the app and documented with the question. These are independent study explanations, not an AWS answer key.", "", "## Study-ready pool by domain", ""]
    for domain in ["secure", "resilient", "performance", "cost"]:
        lines.append(f"- {domain}: {sum(q['domain'] == domain and q['status'] == 'ready' for q in bank)}")
    lines.extend(["", "## Reviewed exclusions", "", "These are closed editorial dispositions, not an automatic/background work queue. The source issue and relevant reading are listed below."])
    for q in bank:
        if q["status"] == "legacy":
            lines.extend(["", f"### #{q['number']:03d} — {q['topic']}", "", q["note"], ""])
            lines.extend(f"- Source: `public/questions/{source}`" for source in q["sources"])
            lines.extend(f"- [{link['title']}]({link['url']})" for link in q["readMore"])
    (ROOT / "data/content-review.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "manifest"}, indent=2))
    print("Study-ready domains:", {d: sum(q["domain"] == d and q["status"] == "ready" for q in bank) for d in ["secure", "resilient", "performance", "cost"]})


def links(keys):
    assert all(key in DOCS for key in keys), f"Unknown reference: {keys}"
    return [{"title": DOCS[key][0], "url": DOCS[key][1]} for key in keys]


def apply_review(q, review):
    assert len(review["explanations"]) == len(q["options"]), f"Option count mismatch: {q['number']}: {len(q['options'])} vs {len(review['explanations'])}"
    assert len(review["correct"]) == q["select"], f"Selection count mismatch: {q['number']}"
    assert all(0 <= a < len(q["options"]) for a in review["correct"])
    q.update({key: review[key] for key in ["correct", "domain", "topic", "takeaway", "explanations", "note"]})
    q["readMore"] = links(review["docs"])
    q["status"] = "ready"


main()
