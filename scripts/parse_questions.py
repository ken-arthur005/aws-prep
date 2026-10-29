"""Convert coordinate-preserving OCR into a reviewable question bank."""
import hashlib
import json
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def clean(text):
    text = text.replace("•", " ").replace("’", "'").replace("—", "-")
    for a, b in [("53", "S3"), ("EC 2", "EC2"), ("I AM", "IAM"), ("S QL", "SQL")]:
        if a != "53":
            text = text.replace(a, b)
    text = re.sub(r"\b(?:Amazon|amazon) 53\b", "Amazon S3", text)
    return re.sub(r"\s+", " ", text).strip()


def rows(words):
    buckets = []
    for word in sorted(words, key=lambda w: (w["y"], w["x"])):
        if not buckets or abs(word["y"] - buckets[-1][0]) > 9:
            buckets.append([word["y"], []])
        buckets[-1][1].append(word)
    return [(y, clean(" ".join(w["text"] for w in sorted(ws, key=lambda w: w["x"])))) for y, ws in buckets]


def parse(item):
    words = [w for line in item["lines"] for w in line["words"]]
    side = any("Description" == line["text"].strip() for line in item["lines"]) and item.get("width", 0) > 1050
    options = []
    prompt = []
    if side:
        with Image.open(ROOT / "public" / "questions" / item["source"]) as image:
            image = image.convert("RGB")
            width, height = image.size
            counts = []
            for x in range(int(width * .28), int(width * .65)):
                score = sum(1 for y in range(12, height - 8, 4) if (lambda p: 215 < p[0] < 250 and abs(p[0] - p[1]) < 15 and p[2] >= p[0])(image.getpixel((x, y))))
                counts.append((score, x))
            divider = max(counts)[1]
        prompt = [t for _, t in rows([w for w in words if w["x"] < divider - 5]) if t != "Description"]
        previous = None
        for y, text in rows([w for w in words if w["x"] > divider + 15]):
            text = re.sub(r"^[O0©◯✓✔]\s+", "", text)
            if previous is None or y - previous > 27:
                options.append(text)
            else:
                options[-1] += " " + text
            previous = y
    else:
        candidates = [w for w in words if re.fullmatch(r"[A-F][.):]?", w["text"]) and w["x"] < item.get("width", 1000) * .28]
        clusters = []
        for candidate in candidates:
            group = next((g for g in clusters if abs(g[0]["x"] - candidate["x"]) < 14), None)
            if group is None:
                clusters.append([candidate])
            else:
                group.append(candidate)
        labels = max(clusters, key=lambda g: len(set(w["text"][0] for w in g)), default=[])
        labels = sorted(labels, key=lambda w: w["y"]) if len(set(w["text"][0] for w in labels)) >= 2 else []
        if labels:
            labelx = sum(w["x"] for w in labels) / len(labels)
            useful = [w for w in words if not (re.fullmatch(r"[A-F][.):]?", w["text"]) and abs(w["x"] - labelx) < 15) and not (re.fullmatch(r"[oO0©@()]+|[C(]\)", w["text"]) and w["x"] < labelx + 15)]
            text_rows = rows(useful)
            option_rows = []
            for y, text in text_rows:
                row_words = [w for w in useful if abs(w["y"] - y) <= 9]
                if row_words and min(w["x"] for w in row_words) > labelx + 15:
                    option_rows.append((y, text))
            start = option_rows[0][0] if option_rows else labels[0]["y"]
            prompt = [t for y, t in text_rows if y < start - 8 and not re.match(r"^(Question \d+|Domain:|Description$)", t)]
            previous = None
            for y, text in option_rows:
                if previous is None or y - previous > 36:
                    options.append(text)
                else:
                    options[-1] += " " + text
                previous = y
        else:
            prompt = [t for _, t in rows(words) if not re.match(r"^(Question \d+|Domain:|Description$|[oO0]$)", t)]
    prompt = clean(" ".join(prompt))
    options = [clean(re.sub(r"^[O0©◯✓✔]\s+", "", o)) for o in options]
    select = re.search(r"(?:select|choose)\s+(two|three|four|2|3|4)", prompt, re.I)
    count = {"two": 2, "three": 3, "four": 4, "2": 2, "3": 3, "4": 4}.get(select[1].lower(), 1) if select else 1
    return {"id": "q-" + hashlib.sha256(item["source"].encode()).hexdigest()[:10], "source": item["source"], "prompt": prompt, "options": options, "select": count, "layout": "side" if side else "stacked"}


def main():
    raw = json.loads((ROOT / "data" / "ocr.json").read_text(encoding="utf-8"))
    parsed = [parse(item) for item in raw]
    (ROOT / "data" / "extracted.json").write_text(json.dumps(parsed, ensure_ascii=False, indent=2), encoding="utf-8")
    review = []
    for i, question in enumerate(parsed):
        review.append(f"\n[{i:03d}] {question['source']} | {question['id']} | select {question['select']}")
        review.append(question["prompt"])
        review.extend(f"{chr(65+j)}. {option}" for j, option in enumerate(question["options"]))
    (ROOT / "data" / "review.txt").write_text("\n".join(review), encoding="utf-8")
    print(f"Parsed {len(parsed)} screenshots; {sum(4 <= len(q['options']) <= 6 for q in parsed)} have 4-6 options")


main()
