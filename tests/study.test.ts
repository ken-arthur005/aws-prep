import { test } from "node:test";
import assert from "node:assert/strict";
import { accuracy, createSession, domainStats, finishSession, firstAttempts, isCorrect, latestAttempts, selectQuestions } from "../lib/study";
import { reconcileSourceBookmarks, validateBackup } from "../lib/store";
import type { Attempt, DomainId, Question, StudyState } from "../lib/types";
import bank from "../data/questions.json";
import raw from "../data/extracted.json";
import textRepairs from "../data/text-repairs.json";
import manifest from "../data/source-manifest.json";

const questions = bank.questions as Question[];
const ready = questions.filter(q => q.status === "ready");
function blank(): StudyState { return { version: 1, examDate: "2026-11-02", dailyTarget: 40, attempts: [], bookmarks: [], completedTasks: [], sessions: [], activeSession: null, storageError: "" }; }
function attempt(id: string, correct: boolean, at: number): Attempt { return { questionId: id, sessionId: "test", selected: [0], correct, seconds: 10, at, mode: "practice" }; }

test("full mocks contain 65 unique study-ready questions at the official approximate weights", () => {
  for (let n = 0; n < 20; n++) {
    const selected = selectQuestions(questions, 65, [], true);
    assert.equal(selected.length, 65);
    assert.equal(new Set(selected.map(q => q.id)).size, 65);
    assert.ok(selected.every(q => q.status === "ready"));
    const counts = Object.fromEntries(["secure", "resilient", "performance", "cost"].map(d => [d, selected.filter(q => q.domain === d).length]));
    assert.deepEqual(counts, { secure: 19, resilient: 17, performance: 16, cost: 13 });
  }
});
test("sparse pools backfill without duplicates and never invent missing questions", () => {
  const pool = ready.filter(q => q.domain === "secure").slice(0, 7);
  assert.equal(selectQuestions(pool, 65, [], true).length, 7);
  assert.equal(new Set(selectQuestions(pool, 65, [], true).map(q => q.id)).size, 7);
});
test("unseen questions are prioritized ahead of recent attempts", () => {
  const pool = ready.slice(0, 20);
  const attempts = pool.slice(0, 10).map(q => attempt(q.id, true, Date.now()));
  assert.ok(selectQuestions(pool, 10, attempts).every(q => !attempts.some(a => a.questionId === q.id)));
});
test("multiple-answer grading requires the exact set, including no extra wrong choices", () => {
  const q = ready.find(q => q.select > 1)!;
  assert.ok(q);
  assert.equal(isCorrect(q, [...q.correct].reverse()), true);
  assert.equal(isCorrect(q, q.correct.slice(1)), false);
  const wrong = q.options.findIndex((_, i) => !q.correct.includes(i));
  assert.equal(isCorrect(q, [...q.correct, wrong]), false);
  assert.equal(isCorrect(q, []), false);
});
test("exam submission scores unanswered questions as wrong and is idempotent", () => {
  const selected = ready.slice(0, 3);
  const session = createSession(selected, "exam", "Test mock", 130);
  session.answers[selected[0].id] = selected[0].correct;
  const state = finishSession({ ...blank(), activeSession: session }, questions, session.startedAt + 100);
  assert.equal(state.attempts.length, 3);
  assert.equal(state.attempts.filter(a => a.correct).length, 1);
  assert.equal(state.sessions.length, 1);
  assert.equal(state.activeSession, null);
  assert.deepEqual(finishSession(state, questions), state);
});
test("practice completion does not count unchecked answers or duplicate checked attempts", () => {
  const selected = ready.slice(0, 2);
  const session = createSession(selected, "practice", "Test practice");
  session.answers[selected[0].id] = selected[0].correct;
  session.checked = [selected[0].id];
  const saved = { ...attempt(selected[0].id, true, Date.now()), sessionId: session.id };
  const state = finishSession({ ...blank(), attempts: [saved], activeSession: session }, questions);
  assert.equal(state.attempts.length, 1);
});
test("first-attempt evidence stays separate from improvement on repeats", () => {
  const q = ready[0];
  const records = [attempt(q.id, true, 3), attempt(q.id, false, 1), attempt(q.id, true, 2)];
  assert.equal(accuracy(firstAttempts(records)), 0);
  assert.equal(latestAttempts(records).get(q.id)?.correct, true);
  assert.equal(domainStats(questions, records).find(d => d.id === q.domain)?.attempted, 1);
});
test("backup round-trip preserves the exam deadline and selected/flagged answers", () => {
  const selected = ready.slice(0, 2);
  const session = createSession(selected, "exam", "Persistent mock", 130);
  session.answers[selected[0].id] = selected[0].correct;
  session.flagged = [selected[0].id];
  const state = { ...blank(), activeSession: session };
  const restored = validateBackup(JSON.parse(JSON.stringify(state)), questions);
  assert.deepEqual(restored, state);
  assert.equal(restored.activeSession!.deadline, session.startedAt + 130 * 60_000);
});
test("malformed/foreign backups cannot replace study state", () => {
  assert.throws(() => validateBackup({ ...blank(), version: 2 }, questions));
  assert.throws(() => validateBackup({ ...blank(), bookmarks: ["unknown-question"] }, questions));
  const session = createSession(ready.slice(0, 2), "exam", "Invalid");
  session.answers[ready[0].id] = [99];
  assert.throws(() => validateBackup({ ...blank(), activeSession: session }, questions));
  assert.throws(() => validateBackup({ ...blank(), attempts: [{ correct: true }] }, questions));
});
test("all shipped ready questions have complete explanations and valid answer indices", () => {
  assert.ok(ready.length >= 65);
  for (const q of ready) {
    assert.ok(q.prompt.length >= 50, q.id);
    assert.ok(q.options.length >= 4 && q.options.length <= 6, q.id);
    assert.equal(q.explanations.length, q.options.length, q.id);
    assert.ok(q.explanations.every(text => text.length >= 40), q.id);
    assert.equal(q.correct.length, q.select, q.id);
    assert.equal(new Set(q.correct).size, q.correct.length, q.id);
    assert.ok(q.correct.every(i => i >= 0 && i < q.options.length), q.id);
    assert.ok(q.readMore.length > 0, q.id);
    assert.ok(q.readMore.every(link => new URL(link.url).protocol === "https:"), q.id);
  }
  assert.equal(new Set(questions.map(q => q.id)).size, questions.length);
  for (const q of questions.filter(q => q.status !== "ready")) assert.equal(q.correct.length, 0);
  const domains = ["secure", "resilient", "performance", "cost"] as DomainId[];
  assert.ok(questions.every(q => domains.includes(q.domain)));
});
test("all 727 screenshot sources are preserved exactly once across records", () => {
  const sources = questions.flatMap(q => q.sources);
  assert.equal(sources.length, 727);
  assert.equal(new Set(sources).size, 727);
});

test("editorial backlog cannot silently return or enter a scored mock", () => {
  assert.equal(questions.filter(q => q.status === "review").length, 0);
  const excluded = questions.filter(q => q.status === "legacy");
  assert.ok(excluded.length > 0);
  assert.ok(excluded.every(q => q.note.length >= 100 && q.readMore.length > 0));
  assert.ok(selectQuestions(questions, 65, [], true).every(q => q.explanations.length === q.options.length));
});

test("bookmarks from merged unscored captures resolve without resetting progress", () => {
  const [oldId, canonical] = Object.entries(bank.aliases)[0];
  const prior = { ...blank(), bookmarks: [oldId, canonical], attempts: [attempt(ready[0].id, true, 1)] };
  const updated = reconcileSourceBookmarks(prior);
  assert.deepEqual(updated.bookmarks, [canonical]);
  assert.equal(updated.attempts, prior.attempts);
  assert.equal(updated.examDate, prior.examDate);
  assert.deepEqual(validateBackup(JSON.parse(JSON.stringify(prior)), questions).bookmarks, [canonical]);
});

test("reading-order repairs preserve meaningful tokens and the original option positions", () => {
  const tokens = (text: string) => text.match(/\S+/g)?.filter(token => !["O", "o", "○", "©", "✓", "✔"].includes(token)).sort() ?? [];
  const repairs = textRepairs as Record<string, { prompt?: string; option?: Record<string, string> }>;
  for (const [index, change] of Object.entries(repairs)) {
    const original = raw[Number(index)];
    if (change.prompt) assert.deepEqual(tokens(change.prompt), tokens(original.prompt), index);
    for (const [position, text] of Object.entries(change.option ?? {})) {
      assert.ok(Number(position) < original.options.length);
      assert.deepEqual(tokens(text), tokens(original.options[Number(position)]), `${index}/${position}`);
    }
  }
});

test("coverage reports and bookmark aliases agree with the shipped bank", () => {
  assert.equal(manifest.studyReady, ready.length);
  assert.equal(manifest.uniqueRecords, questions.length);
  assert.equal(manifest.awaitingReview, 0);
  assert.equal(manifest.manifest.length, bank.sourceCount);
  const ids = new Set(questions.map(q => q.id));
  for (const [source, target] of Object.entries(bank.aliases)) {
    assert.notEqual(source, target);
    assert.ok(ids.has(target));
    assert.equal((bank.aliases as Record<string, string>)[target], undefined);
  }
});
