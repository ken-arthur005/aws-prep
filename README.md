# Cloudbound — AWS SAA-C03 study basecamp

A personal, responsive exam-preparation app built with Next.js 16 and React 19. The design combines warm paper, comic-book outlines, a friendly cloud illustration, and a distraction-light question screen.

## Run

```sh
pnpm install
pnpm dev
```

Open http://localhost:3000. No account, database, API key or live AI service is required for studying.

```sh
pnpm test          # scoring, sampling, persistence contracts, content/source integrity
pnpm lint
pnpm build
pnpm start        # serve the production build
```

## Study features

- Domain/topic practice, unseen-first selection, optional timers, bookmarks and flags.
- Full **65-question / 130-minute** mock exams and configurable mini mocks.
- Approximate official domain weighting: Secure 30%, Resilient 26%, High-performing 24%, Cost-optimized 20%.
- Multi-response exact-set scoring; unanswered exam questions are incorrect.
- Immediate practice explanations; exam explanations only after submission.
- Persistent exam deadlines: refreshing or leaving the question screen does not reset/pause the countdown. An expired session submits on the next active page check.
- First-attempt accuracy, repeat attempts, coverage, domain/topic weaknesses, answer timing, and session trends calculated from real records.
- A four-day study checklist, editable exam date and daily question target.
- Browser-local progress with JSON export/import and validation before confirmed restore.

AWS's passing score of **720** is scaled; the app deliberately does not equate it to 72% raw accuracy or predict a pass.

## Content coverage and quality

All **727 uploaded PNG screenshots** are represented, with original source links preserved. The initial extraction/deduplication produces **635 question/source records**:

- **198 study-ready questions** have independently prepared answers, a rationale for every option, key takeaways and AWS reading links.
- **74 source records are explicitly flagged** for obsolete information, ambiguous/contradictory premises, missing options or non-question material.
- **363 extracted records still await editorial answer/explanation review.** They remain inspectable in the library and are excluded from scored practice and exams. They must not be treated as reviewed or silently assigned an answer.

The screenshot's chosen answers, checkmarks and highlights are never used as an answer key. Some material is materially outdated: the S3 object-size limit changed, and CloudTrail Lake closed to new customers on May 31, 2026. The source-quality notes explain affected records.

The shipped app is usable now, but the editorial review of the entire extracted pool is **not complete**. The library and counts expose that distinction.

### Source of truth

- `data/questions.json`: shipped question bank, explanations, status and citations.
- `data/source-manifest.json`: mapping of every screenshot to its question/source record, including duplicates and continuations.
- `data/extracted.json`: coordinate-parser output retained for editorial review/rebuilding.
- `scripts/content.py`: explicit editorial answer decisions, corrections and quality flags. Indexes reference the existing, sorted 727-source extraction; review the source order before importing a different collection.
- `scripts/build_bank.py`: deterministic bank generation, deduplication and invariant checks.

Rebuild after an editorial change:

```sh
pnpm content:build
pnpm test
```

### Re-extract screenshots (Windows only)

The app itself does not run OCR. Initial extraction was performed locally with Windows OCR, without sending images to an external service.

1. Use Python 3.12, an English Windows OCR language pack, Pillow, and PyWinRT packages for `Windows.Media.Ocr`, `Windows.Graphics.Imaging`, `Windows.Storage`, `Windows.Globalization`, `Windows.Foundation`, and `Windows.Storage.Streams`.
2. Run `python scripts/extract_questions.py`. This writes resumable, coordinate-preserving `data/ocr.json`.
3. Run `python scripts/parse_questions.py` to generate `data/extracted.json` and a human-readable `data/review.txt`.
4. Review extraction accuracy, source order, duplicate/continuation mappings and all editorial decisions before rebuilding. Adding/reordering source files without updating the editorial mapping can invalidate answer associations.

OCR raw output/logs and browser-check artifacts are ignored by Git. The original screenshot files are preserved.

## Architecture

- `app/page.tsx`: server-rendered bank entry point.
- `components/study-app.tsx`: dashboard, practice, mocks, library, results, analytics and settings.
- `components/cloud.tsx`: original inline SVG study companion.
- `lib/study.ts`: sampling, exact-set grading, statistics and session completion.
- `lib/store.ts`: versioned localStorage persistence and backup validation via a React external store.
- `tests/study.test.ts`: meaningful regression tests for exam behavior and content invariants.

Progress is specific to the browser/device until exported and imported elsewhere. Settings includes an explicit reset confirmation. Backup restoration replaces the current local study state only after confirmation.

## Primary exam references

- [Official AWS exam overview](https://aws.amazon.com/certification/certified-solutions-architect-associate/)
- [Official SAA-C03 exam guide and domain breakdown](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html)
- [Current S3 multipart/object limits](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html)
- [CloudTrail Lake availability notice](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html)

Question-specific reading links are included with the individual explanations.
