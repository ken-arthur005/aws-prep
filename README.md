# Cloudbound v2 — AWS SAA-C03 study basecamp

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
- A date-aware study checklist, editable exam date and daily question target.
- Browser-local progress with JSON export/import and validation before confirmed restore.
- **Revision desk:** 37 curated plain-English guides with analogies, service comparisons, constraints, worked scenarios, and direct concept practice.
- **Understand / Compare / Quick recall / Last lap:** four views over shared editorial content, with multiword search and printable final-review sheets.
- **Guessed / unsure** markers and optional mistake reasons. Correct guesses remain reviewable until explicitly cleared.
- Concept recommendations from latest misses and uncertainty, including deep links such as `#revision/rds/compare`.
- Self-rated recall with ten-minute / twelve-hour revisit intervals, stored separately from question/mock accuracy.
- New-November-only practice and source-aware original screenshot links.
- An exam-date-aware sprint with four milestones, rather than four mandatory calendar days. New profiles default to the confirmed **5 November 2026** exam; existing dates are preserved.

AWS's passing score of **720** is scaled; the app deliberately does not equate it to 72% raw accuracy or predict a pass.

## Content coverage and quality

All **1,041 uploaded PNG screenshots** have an editorial disposition, with original source links preserved. After combining duplicate and split captures there are **798 question/source records**:

- **705 study-ready questions** have independently prepared answers, a rationale for every option, key takeaways, internal revision links, and AWS references.
- **93 reviewed exclusions** have specific notes documenting obsolete service eligibility, contradictory/missing answers, unreadable crops or non-question material. They remain inspectable and do not enter scored sessions.
- **0 awaiting review.** The bank builder and tests reject an unexplained return to the review backlog.

The screenshot's chosen answers, checkmarks and highlights are never used as an answer key. Some material is materially outdated: the S3 object-size limit changed, and CloudTrail Lake closed to new customers on May 31, 2026. The source-quality notes explain affected records.

The editorial pass is complete for this uploaded collection. Source-faithful transcription repairs and explicitly labeled study variants recover useful material; substantive corrections are described in each question's notes and marked **Updated source**. Original screenshots remain available for comparison. These are independent study explanations, not an official AWS answer key or a guarantee every source scenario is deployment-ready.

The question pool has 209 Secure, 210 Resilient, 193 High-performing and 93 Cost-optimized questions. Full mocks still sample approximately the official domain weights, rather than copying these pool proportions.

### November import

The **314 captures in `public/new set/`** add **171 study-ready questions** and **21 documented exclusions**. Another **122 captures** are duplicate/continuation evidence attached to canonical records. Original question IDs, option orders, selection counts, prompts, and answer sets remain frozen; a regression checksum protects the pre-v2 saved-session contract.

Some complete new screenshots genuinely have three options; those are preserved rather than inventing a fourth. Substantive corrections and study variants are explicitly labelled. Historical Pinpoint journeys, unavailable new-customer services, unsupported network transit, and genuinely underspecified questions do not enter scored mocks.

### Revision editorial approach

`lib/revision-content.ts` contains original concise summaries informed by the supplied resources. It is the shared source for guides, comparisons, pocket cards, and recall. Community source: [RonitSachdev — AWS SAA-C03 Guides](https://github.com/RonitSachdev/aws-saa-c03-guides), under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The summaries shorten/reorganise the material, add examples, and correct outdated details; in-app source notes retain attribution and identify the guide used. The original resource files remain available for inspection.

The revision summaries correct outdated shortcuts including SQS's former 256 KB limit, the old gp3 16,000 IOPS ceiling, creation-only Object Lock, blanket non-readable RDS Multi-AZ claims, the absolute 29-second API Gateway timeout, and outdated KMS validation/certificate-export claims. Primary references support these corrections. Source material is not automatically treated as a verified answer key.

### Source of truth

- `data/questions.json`: shipped question bank, explanations, status and citations.
- `data/source-manifest.json`: mapping of every screenshot to its question/source record, including duplicates and continuations.
- `data/content-review.md`: generated coverage summary and the documented reason/reference for every excluded record.
- `data/source-groups.json`: established duplicate/continuation groups, retained so editing one capture does not resurrect an unanswered duplicate.
- `data/text-repairs.json`: token-preserving OCR reading-order repairs for 1,037 options across 281 captures. Radio-button glyphs no longer split capitalized words away from their sentences.
- `data/extracted.json`: coordinate-parser output retained for editorial review/rebuilding.
- `scripts/content.py`: explicit editorial answer decisions, corrections and quality flags. Indexes reference the existing, sorted 727-source extraction; review the source order before importing a different collection.
- `scripts/content_remaining.py`: completed second pass, explicit option-order remaps and re-review of earlier exclusions.
- `scripts/build_bank.py`: deterministic bank generation, source-order checksum protection, duplicate flattening, alias generation and invariant checks. Bookmark aliases preserve saved references to merged unscored source captures.
- `data/new-extracted.json`: coordinate-parser output for the separate November collection, including duplicate candidates and source indices.
- `scripts/content_november.py`: explicit independent November answer decisions, option rationales, corrections, exclusions, and reviewed merge overrides.
- `scripts/import_batch.py`: adds reviewed November records/source paths without changing the old question/answer contract.
- `data/november-review.json`: generated collection counts and source-order checksum.

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
4. Optionally run `python scripts/reflow_ocr.py` to recover reading order only where the meaningful token multiset and option position are preserved.
5. Review extraction accuracy, source order, duplicate/continuation mappings and all editorial decisions before rebuilding. The frozen source checksum prevents applying old indexed reviews to a reordered collection.

OCR raw output/logs and browser-check artifacts are ignored by Git. The original screenshot files are preserved.

The November batch can be re-extracted with offline Windows OCR **without PyWinRT or Pillow**:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/extract_batch.ps1
python scripts/prepare_batch.py
python scripts/build_bank.py
```

This preserves coordinates and detects the two-column divider. Parsing supports side-by-side and stacked layouts, including narrow captures. `prepare_batch.py` proposes duplicate candidates; independent decisions and the frozen collection order remain required before a bank rebuild. Raw OCR/review packets are local intermediates; the reviewed extraction is shipped.

## Architecture

- `app/page.tsx`: server-rendered bank entry point.
- `components/study-app.tsx`: dashboard, practice, mocks, library, results, analytics and settings.
- `components/cloud.tsx`: original inline SVG study companion.
- `lib/study.ts`: sampling, exact-set grading, statistics and session completion.
- `lib/store.ts`: versioned localStorage persistence and backup validation via a React external store.
- `components/revision-desk.tsx`: guide reader, comparisons, self-check recall, printable review, and concept connections.
- `lib/revision.ts`: question-to-concept matching, revision priorities, source URLs, and date-aware sprint milestones.
- `lib/revision-content.ts`: shared editorial revision material, including primary references and counterfactual examples.
- `tests/study.test.ts`: meaningful regression tests for exam behavior and content invariants.
- `tests/revision.test.ts`: full source traceability, original contract checksum, revision graph integrity, uncertainty/recall persistence, old backups, and mock recommendation boundaries.

An optional real-browser regression script is included at `scripts/check_ui.mjs`. Install Playwright and Chromium in a development environment and build the app. Run a production server on port 3100, or set `UI_START_SERVER=1` to have the script start and stop its own preview, then run `node scripts/check_ui.mjs`. `PLAYWRIGHT_MODULE` may point to an external Playwright installation; `UI_ARTIFACTS` optionally names an existing screenshot directory. It checks desktop/mobile revision, multiword search, recall, print layout, new-question practice, uncertainty review, saved progress, and mock deadline/explanation boundaries.

Progress is specific to the browser/device until exported and imported elsewhere. Settings includes an explicit reset confirmation. Backup restoration replaces the current local study state only after confirmation.

The storage key/schema remain `cloudbound-study-v1` / version 1. Revision fields are additive and optional so existing backups remain valid. Recall self-ratings never create scored question attempts. Unsubmitted mock questions are excluded from concept-priority evidence, and their explanations remain hidden until submission.

## Primary exam references

- [Official AWS exam overview](https://aws.amazon.com/certification/certified-solutions-architect-associate/)
- [Official SAA-C03 exam guide and domain breakdown](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html)
- [Current S3 multipart/object limits](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html)
- [CloudTrail Lake availability notice](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html)

Question-specific reading links are included with the individual explanations.
