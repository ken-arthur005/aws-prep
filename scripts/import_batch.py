"""Append reviewed November records without reordering existing IDs or options."""
import hashlib
import json
import re
import textwrap
from pathlib import Path
from content import DOCS
from content_november import REVIEWS, HOLDS, MERGES, CONTINUATIONS, REASONING

ROOT = Path(__file__).resolve().parents[1]
DOCS.update({
    "costtags": ("Cost allocation tags", "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html"),
    "cache": ("ElastiCache overview", "https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html"),
    "snow": ("Snowball Edge availability", "https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html"),
    "polly": ("Polly speech synthesis", "https://docs.aws.amazon.com/polly/latest/dg/what-is.html"),
    "lex": ("Lex conversational interfaces", "https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html"),
    "search": ("OpenSearch service", "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html"),
    "textract": ("Textract document analysis", "https://docs.aws.amazon.com/textract/latest/dg/what-is.html"),
    "kendra": ("Kendra enterprise search", "https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html"),
    "dataexchange": ("AWS Data Exchange", "https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html"),
    "backup": ("AWS Backup", "https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html"),
    "trail": ("CloudTrail trails and supported events", "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html"),
    "discovery": ("Application Discovery availability and alternatives", "https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html"),
    "redshiftshare": ("Redshift cross-account data sharing", "https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html"),
    "optimizer": ("Compute Optimizer recommendations", "https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html"),
    "securityhub": ("Security Hub security controls", "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls.html"),
    "outposts": ("AWS Outposts on-premises infrastructure", "https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html"),
    "cloudhsmstore": ("KMS CloudHSM custom key stores", "https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html"),
    "dx": ("Direct Connect and gateway connectivity", "https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html"),
})
GROUPS = {
    "s3": ("cost", "Object storage classes"), "sse": ("secure", "Storage encryption"),
    "objectlock": ("secure", "Retention & immutability"), "versioning": ("resilient", "Object protection"),
    "sqs": ("resilient", "Messaging & integration"), "sns": ("resilient", "Messaging & integration"),
    "steps": ("resilient", "Workflow orchestration"), "kinesis": ("performance", "Streaming analytics"),
    "rds": ("resilient", "Database connections & availability"), "aurora": ("performance", "Database scaling"),
    "auroraha": ("resilient", "Database availability"), "serverless": ("cost", "Database scaling"),
    "dynamo": ("performance", "NoSQL access patterns"), "cache": ("performance", "Caching & sessions"),
    "cloudfront": ("performance", "Edge delivery"), "routing": ("performance", "DNS & routing"),
    "dns": ("performance", "DNS & routing"), "vpc": ("secure", "Network security"),
    "peering": ("resilient", "Private network connectivity"), "vpn": ("resilient", "Hybrid networking"),
    "nat": ("resilient", "Network egress"), "s3endpoint": ("cost", "Private service access"),
    "endpoint": ("secure", "Private service access"), "kms": ("secure", "Encryption & key management"),
    "kmspolicy": ("secure", "Encryption & key management"), "secrets": ("secure", "Secrets & credentials"),
    "iam": ("secure", "Identity & access"), "scp": ("secure", "Multi-account governance"),
    "ram": ("cost", "Resource sharing"), "orgbilling": ("cost", "Multi-account governance"),
    "costtags": ("cost", "Cost attribution"), "as": ("resilient", "Compute scaling"),
    "tracking": ("resilient", "Compute scaling"), "hooks": ("resilient", "Compute lifecycle"),
    "ebs": ("performance", "Block storage"), "efs": ("performance", "Shared file storage"),
    "fsxwindows": ("performance", "Windows file storage"), "gateway": ("cost", "Hybrid storage"),
    "datasync": ("performance", "Data movement"), "dms": ("resilient", "Database migration"),
    "eks": ("resilient", "Containers & orchestration"), "ecs": ("resilient", "Containers & orchestration"),
    "fargate": ("cost", "Containers & orchestration"), "lambda": ("performance", "Serverless compute"),
    "waf": ("secure", "Network & application protection"), "macie": ("secure", "Sensitive data discovery"),
    "trail": ("secure", "Audit & observability"), "cloudwatch": ("resilient", "Observability"),
    "xray": ("resilient", "Observability"), "ssm": ("secure", "Fleet management"),
    "acm": ("secure", "TLS & certificates"), "cfnfull": ("resilient", "Infrastructure automation"),
    "cfnoutputs": ("resilient", "Infrastructure automation"), "spot": ("cost", "Compute purchasing"),
    "backup": ("resilient", "Backup & recovery"), "dr": ("resilient", "Disaster recovery"),
    "cloudhsmstore": ("secure", "Encryption & key management"), "dx": ("resilient", "Hybrid networking"),
}

def norm(value):
    return re.sub(r"[^a-z0-9]", "", value.lower())

def key(q):
    return norm(q["prompt"]), tuple(sorted(norm(o) for o in q["options"])), q["select"]

def text(value):
    for pattern, replacement in [(r"\bSS\b", "S3"), (r"\bStl\b", "st1"), (r"\bscl\b", "sc1"), (r"\biol\b", "io1"), (r"\bi02\b", "io2"), (r"\bOpenAPl\b", "OpenAPI")]:
        value = re.sub(pattern, replacement, value, flags=re.I)
    return value

def extend_bank(bank, manifest, aliases):
    extracted = json.loads((ROOT / "data/new-extracted.json").read_text(encoding="utf-8"))
    assert len(extracted) == 314, "Review collection changes before applying indexed November decisions"
    digest = hashlib.sha256("\n".join(q["source"] for q in extracted).encode()).hexdigest()
    assert digest == "1b0efe8dba15a993733bc6cbaf4e273d31593fc4a4212fe7c52d0950a133c37f", "November source order changed; re-review indexed decisions"
    print("November order checksum:", digest)
    actual = sorted(p.name for p in (ROOT / "public/new set").glob("*.png"))
    assert [q["source"] for q in extracted] == actual
    lookup = {q["id"]:q for q in bank}
    originals = {key(q):q for q in bank}
    seen, assigned, new_records = {}, {}, []
    def source(q, item, kind):
        if "sourcePaths" not in q:
            q["sourcePaths"] = ["/questions/" + s for s in q["sources"]]
        q["sources"].append(item["source"])
        q["sourcePaths"].append("/new set/" + item["source"])
        manifest.append({"sourceIndex":727+item["index"], "source":item["source"], "path":"/new set/"+item["source"], "collection":"november", "questionId":q["id"], "kind":kind})
        assigned[item["index"]] = q
        if item["id"] != q["id"]:
            aliases[item["id"]] = q["id"]
    for item in extracted:
        i = item["index"]
        if i in CONTINUATIONS:
            continue
        candidate = item.get("candidate", {})
        prior = seen.get(key(item)) or originals.get(key(item))
        if i in MERGES:
            prior = lookup[MERGES[i]]
        elif not prior and candidate.get("promptScore",0) >= .985 and candidate.get("optionScore",0) >= .94:
            prior = lookup.get(candidate["id"])
        if prior:
            source(prior,item,"duplicate")
            seen[key(item)] = prior
            continue
        assert i in REVIEWS or i in HOLDS, f"Independent editorial decision required for November index {i}: {item['source']}"
        review = REVIEWS.get(i) or HOLDS[i]
        doc = review["docs"][0]
        assert doc in DOCS, f"Unknown reference {doc}"
        domain, topic = GROUPS.get(doc,("performance","Specialised service selection"))
        q = {"id":item["id"], "number":728+i, "prompt":review.get("prompt") or text(item["prompt"]), "options":review.get("options") or [text(o) for o in item["options"]], "select":item["select"], "sources":[], "sourcePaths":[], "domain":review.get("domain") or domain, "topic":topic, "correct":review.get("correct",[]), "explanations":review.get("explanations",[]), "takeaway":review.get("takeaway",""), "status":"ready" if i in REVIEWS else "legacy", "note":review["note"], "batch":"november", "adapted":bool(review.get("prompt") or review.get("options")), "readMore":[{"title":DOCS[d][0],"url":DOCS[d][1]} for d in review["docs"]]}
        q["title"] = textwrap.shorten(q["takeaway"],width=106,placeholder="…").rstrip(".") if q["takeaway"] else topic + ": reviewed source exclusion"
        if i in REASONING:
            q["reasoning"] = REASONING[i]
        if q["status"] == "ready":
            assert len(q["correct"]) == q["select"] and len(q["explanations"]) == len(q["options"]), (i,len(q["options"]),len(q["explanations"]))
            assert 3 <= len(q["options"]) <= 6 and all(len(e)>=40 for e in q["explanations"]), i
            assert all(0 <= a < len(q["options"]) for a in q["correct"]), i
        source(q,item,"question")
        seen[key(item)] = q
        lookup[q["id"]] = q
        bank.append(q)
        new_records.append(q)
    for i, parent in CONTINUATIONS.items():
        source(assigned[parent],extracted[i],"continuation")
    assert len(assigned) == 314
    assert set(REVIEWS).isdisjoint(HOLDS)
    report = {"collection":"november", "sourceCount":314, "recordsAdded":len(new_records), "readyAdded":sum(q["status"]=="ready" for q in new_records), "excludedAdded":sum(q["status"]=="legacy" for q in new_records), "mergedSources":314-len(new_records), "orderChecksum":digest}
    print(json.dumps(report,indent=2))
    (ROOT / "data/november-review.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    return report
