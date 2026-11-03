import { test } from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import bank from "../data/questions.json";
import report from "../data/html-review.json";
import extracted from "../data/html-extracted.json";
import equivalents from "../data/question-equivalents.json";
import { canonicalQuestionId, createSession, domainStats, finishSession, firstAttempts, isCorrect, isStudyReady, latestAttempts, selectQuestions, studyAttempts } from "../lib/study";
import { reconcileSourceBookmarks, validateBackup } from "../lib/store";
import { questionConcepts, revisionPriorities } from "../lib/revision";
import type { Attempt, Question, StudyState } from "../lib/types";

const questions = bank.questions as Question[];
const lookup = new Map(questions.map(q => [q.id, q]));
const blank = (): StudyState => ({ version: 1, examDate: "2026-11-05", dailyTarget: 40, attempts: [], bookmarks: [], completedTasks: [], sessions: [], activeSession: null, storageError: "" });
const attempt = (q: Question, at: number): Attempt => ({ questionId: q.id, sessionId: `s-${at}`, selected: [...q.correct], correct: true, seconds: 12, at, mode: "practice" });

test("all 322 supplied HTML records have exactly one closed, checksum-bound disposition", () => {
  const html = readFileSync(new URL("../public/resources/saa-c03-quiz (offline).html", import.meta.url), "utf8");
  const literal = html.match(/const Q=(\[[\s\S]*?\]);\s*const DN=/)![1];
  assert.equal(createHash("sha256").update(literal).digest("hex"), report.checksum);
  assert.equal(extracted.checksum, report.checksum);
  assert.deepEqual(report.records.map(r => r.importId).sort((a, b) => a - b), Array.from({ length: 322 }, (_, i) => i + 1));
  assert.equal(report.records.filter(r => r.disposition === "added").length, report.added);
  assert.equal(report.records.filter(r => r.disposition === "matched").length, report.matched);
  assert.equal(report.records.filter(r => r.disposition === "excluded").length, report.excluded);
  for (const row of report.records) {
    if (row.disposition === "excluded") assert.ok(row.reason && row.reason.length > 40);
    else assert.ok(row.questionId && lookup.has(row.questionId));
  }
});

test("HTML additions are native scored questions with original explanations and no invented image/PDF sources", () => {
  const added = questions.filter(q => q.batch === "html");
  assert.equal(added.length, report.added);
  assert.ok(added.every(isStudyReady));
  assert.equal(selectQuestions(added, 1000, []).length, added.length);
  for (const q of added) {
    const raw = extracted.records.find(r => r.id === q.id)!;
    assert.ok(q.explanations.every(e => e.length >= 40 && e !== raw.suggestedExplanation));
    assert.equal(q.explanations.length, q.options.length);
    assert.equal(q.sources.length, 0);
    assert.equal(q.sourcePaths?.length, 0);
    assert.ok(!/pdf|page\s+\d/i.test(`${q.prompt} ${q.note} ${q.explanations.join(" ")}`));
    assert.ok(questionConcepts(q).length > 0);
    assert.ok(isCorrect(q, q.correct));
  }
  const sixSubnets = lookup.get("html-180")!;
  assert.notDeepEqual(sixSubnets.correct, extracted.records.find(q => q.id === sixSubnets.id)!.suggestedCorrect);
  assert.match(sixSubnets.options[sixSubnets.correct[0]], /six|6/i);
});

test("new sampling and coverage exclude redundant/ambiguous records while historical grading remains valid", () => {
  const ready = questions.filter(isStudyReady);
  assert.equal(ready.length, report.studyReady);
  assert.equal(selectQuestions(questions, 10000, []).length, ready.length);
  assert.equal(domainStats(questions, []).reduce((sum, d) => sum + d.total, 0), ready.length);
  for (const q of questions.filter(q => q.duplicateOf && q.status === "ready")) {
    assert.ok(isStudyReady(lookup.get(q.duplicateOf!)!));
    const session = createSession([q], "exam", "Historical option order", 130);
    session.answers[q.id] = [...q.correct];
    const prior = { ...blank(), activeSession: session };
    assert.deepEqual(validateBackup(JSON.parse(JSON.stringify(prior)), questions).activeSession, session);
    const finished = finishSession(prior, questions);
    assert.equal(finished.attempts[0].questionId, q.id);
    assert.deepEqual(finished.attempts[0].selected, q.correct);
    assert.equal(finished.attempts[0].correct, true);
  }
  for (const q of questions.filter(q => q.studyExcludedReason)) assert.ok(!isStudyReady(q));
});

test("reordered duplicate evidence counts one canonical first attempt without mutating history", () => {
  let reordered = 0;
  for (const [id, mapping] of Object.entries(equivalents.duplicates)) {
    const duplicate = lookup.get(id)!;
    const canonical = lookup.get(mapping.canonicalId)!;
    if (mapping.optionMap.some((n, i) => n !== i)) reordered++;
    assert.deepEqual([...studyAttempts([attempt(duplicate, 1)])[0].selected].sort(), [...canonical.correct].sort());
    const records = [attempt(duplicate, 1), { ...attempt(canonical, 2), correct: false }];
    const before = JSON.stringify(records);
    assert.equal(firstAttempts(records).length, 1);
    assert.equal(firstAttempts(records)[0].questionId, canonical.id);
    assert.equal(latestAttempts(records).get(canonical.id)?.correct, false);
    assert.equal(domainStats(questions, records).reduce((sum, d) => sum + d.attempted, 0), 1);
    assert.equal(JSON.stringify(records), before);
    assert.ok(!selectQuestions([canonical, questions.find(q => isStudyReady(q) && q.id !== canonical.id)!], 1, [attempt(duplicate, 1)]).some(q => q.id === canonical.id));
  }
  assert.ok(reordered > 0, "Exercise non-identity option permutations");
});

test("bookmark, uncertainty and mistake reconciliation preserves sessions and optional v1 fields", () => {
  const [id, mapping] = Object.entries(equivalents.duplicates)[0];
  const duplicate = lookup.get(id)!;
  const prior = { ...blank(), bookmarks: [id, mapping.canonicalId], uncertain: [id], mistakes: { [id]: "concept" as const }, attempts: [attempt(duplicate, 1)], activeSession: createSession([duplicate], "exam", "Retained active session", 130) };
  const result = reconcileSourceBookmarks(prior);
  assert.deepEqual(result.bookmarks, [mapping.canonicalId]);
  assert.deepEqual(result.uncertain, [mapping.canonicalId]);
  assert.deepEqual(result.mistakes, { [mapping.canonicalId]: "concept" });
  assert.equal(result.attempts, prior.attempts);
  assert.equal(result.activeSession, prior.activeSession);
  assert.deepEqual(validateBackup(JSON.parse(JSON.stringify(prior)), questions), result);
  assert.equal(reconcileSourceBookmarks(result), result);
  assert.ok(!("uncertain" in reconcileSourceBookmarks(blank())));
  assert.equal(canonicalQuestionId(id), mapping.canonicalId);
  assert.ok(revisionPriorities(questions, result).every(t => !t.uncertain && !t.missed), "Historical active mock must not leak equivalent-question hints");
});
