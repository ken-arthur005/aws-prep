import { test } from "node:test";
import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { createHash } from "node:crypto";
import bank from "../data/questions.json";
import manifest from "../data/source-manifest.json";
import november from "../data/november-review.json";
import { REVISION_TOPICS } from "../lib/revision-content";
import {
  questionConcepts,
  RECALL_CARDS,
  revisionPriorities,
  sourceUrl,
  sprintTasks,
} from "../lib/revision";
import { validateBackup } from "../lib/store";
import { createSession, finishSession } from "../lib/study";
import type { Question, StudyState } from "../lib/types";

const questions = bank.questions as Question[];
const copyReview = JSON.parse(
  readFileSync(
    new URL("../data/copy-edit-review.json", import.meta.url),
    "utf8",
  ),
) as {
  reviewedRecords: number;
  editedRecords: number;
  editedFields: number;
  scoringContractSha256: string;
  edits: Record<
    string,
    {
      number: number;
      fields: Record<string, { before: string; after: string }>;
    }
  >;
};
const blank = (): StudyState => ({
  version: 1,
  examDate: "2026-11-05",
  dailyTarget: 40,
  attempts: [],
  bookmarks: [],
  completedTasks: [],
  sessions: [],
  activeSession: null,
  storageError: "",
});

test("every new capture has one real, traceable source URL and a final disposition", () => {
  const sources = new Set<string>();
  for (const q of questions) {
    if (q.sourcePaths) assert.equal(q.sourcePaths.length, q.sources.length);
    for (const source of q.sources) {
      const path = decodeURIComponent(sourceUrl(q, source));
      assert.ok(!sources.has(path), path);
      sources.add(path);
      assert.ok(existsSync(join(process.cwd(), "public", path)), path);
      const entry = manifest.manifest.find((m) => m.path === path);
      assert.equal(entry?.questionId, q.id, path);
    }
  }
  assert.equal(sources.size, bank.sourceCount);
  assert.equal(november.sourceCount, 314);
  assert.equal(november.recordsAdded + november.mergedSources, 314);
  const added = questions.filter((q) => q.batch === "november");
  assert.equal(added.length, november.recordsAdded);
  assert.equal(
    added.filter((q) => q.status === "ready").length,
    november.readyAdded,
  );
  assert.ok(added.every((q) => q.status !== "review"));
});

test("the original question/answer contract remains intact for saved sessions", () => {
  const original = questions.filter((q) => !q.batch);
  assert.equal(original.length, 606);
  const contract = original.map((q) => [
    q.id,
    copyReview.edits[q.id]?.fields.prompt?.before ?? q.prompt,
    q.options.map(
      (value, i) =>
        copyReview.edits[q.id]?.fields[`options.${i}`]?.before ?? value,
    ),
    q.select,
    q.correct,
  ]);
  // Reconstruct pre-copy-edit wording from the ledger; IDs, option positions, and keys remain frozen.
  const digest = createHash("sha256")
    .update(JSON.stringify(contract))
    .digest("hex");
  assert.equal(
    digest,
    "3d7255f83cb0a6fda0344a1269b0d58e215446efc4e02a259bb3ab6132252747",
  );
});

test("copy edits are traceable and preserve the complete scoring contract", () => {
  assert.equal(
    copyReview.reviewedRecords,
    questions.filter((q) => q.status === "ready").length,
  );
  assert.equal(copyReview.editedRecords, Object.keys(copyReview.edits).length);
  let fields = 0;
  for (const [id, record] of Object.entries(copyReview.edits)) {
    const q = questions.find((q) => q.id === id)!;
    assert.ok(q && q.status === "ready");
    for (const [path, edit] of Object.entries(record.fields)) {
      const [field, key] = path.split(".");
      const value = (q as unknown as Record<string, unknown>)[field];
      const actual =
        key === undefined
          ? value
          : Array.isArray(value)
            ? value[Number(key)]
            : (value as Record<string, unknown>)[key];
      assert.equal(actual, edit.after, `${id}:${path}`);
      assert.notEqual(edit.before, edit.after);
      fields++;
    }
  }
  assert.equal(fields, copyReview.editedFields);
  const scoring = questions.map((q) => [
    q.id,
    q.options.length,
    q.select,
    q.correct,
    q.status,
  ]);
  assert.equal(
    createHash("sha256").update(JSON.stringify(scoring)).digest("hex"),
    "d9f600ca3f6c9a74acebcc1cedc3e32b7d4208b99d756ceb566eb2fbdc63816d",
  );
  assert.equal(
    copyReview.scoringContractSha256,
    "d9f600ca3f6c9a74acebcc1cedc3e32b7d4208b99d756ceb566eb2fbdc63816d",
  );
  const cloudhsm = questions.find((q) => q.number === 198)!;
  assert.match(cloudhsm.options[0], /same Region/);
  assert.match(cloudhsm.options[2], /different Region/);
  const firewall = questions.find((q) => q.number === 264)!;
  assert.match(firewall.prompt, /443/);
  assert.match(firewall.options[2], /3306/);
  assert.match(firewall.options[4], /442/); // Preserve the deliberately wrong port.
  assert.match(questions.find((q) => q.number === 1037)!.prompt, /\.NET/);
  assert.equal(
    questions.find((q) => q.number === 178)!.options[0],
    "http://169.254.169.254/latest/meta-data/ami-id",
  );
  assert.equal(
    questions.find((q) => q.number === 952)!.options[0],
    "arn:aws:lambda:aws-region:acct-id:function:helloworld:$LATEST",
  );
});

test("37 shared guides produce uniquely addressed comparison/recall content and valid concept links", () => {
  assert.equal(REVISION_TOPICS.length, 37);
  assert.equal(new Set(REVISION_TOPICS.map((t) => t.id)).size, 37);
  assert.equal(
    new Set(RECALL_CARDS.map((c) => c.id)).size,
    RECALL_CARDS.length,
  );
  const ids = new Set(REVISION_TOPICS.map((t) => t.id));
  for (const topic of REVISION_TOPICS) {
    assert.ok(
      existsSync(
        join(process.cwd(), "public/resources/topic-guides", topic.guide),
      ),
    );
    assert.ok(topic.rules.length >= 3 && topic.choices.length >= 2);
    assert.ok(new URL(topic.reference).protocol === "https:");
  }
  for (const q of questions.filter((q) => q.status === "ready")) {
    assert.ok(questionConcepts(q).length > 0, q.id);
    assert.ok(
      questionConcepts(q).every((t) => ids.has(t.id)),
      q.id,
    );
  }
  for (const card of RECALL_CARDS) assert.ok(ids.has(card.topicId));
  const config = questions.find(
    (q) =>
      q.batch === "november" &&
      q.takeaway.includes("endpoint policy restricts"),
  )!;
  assert.ok(questionConcepts(config).some((t) => t.id === "vpc"));
});

test("uncertain correct answers remain revision evidence while recall does not change exam accuracy", () => {
  const q = questions.find(
    (q) => q.batch === "november" && q.status === "ready",
  )!;
  const session = createSession([q], "exam", "Fresh evidence", 10);
  session.answers[q.id] = q.correct;
  const result = finishSession(
    { ...blank(), activeSession: session, uncertain: [q.id] },
    questions,
  );
  const state = {
    ...result,
    recall: {
      [RECALL_CARDS[0].id]: { rating: "known" as const, at: 1000, due: 2000 },
    },
  };
  assert.equal(state.attempts.length, 1);
  assert.equal(state.attempts[0].correct, true);
  assert.ok(revisionPriorities(questions, state).some((t) => t.uncertain > 0));
  assert.deepEqual(
    validateBackup(JSON.parse(JSON.stringify(state)), questions),
    state,
  );
  const cleared = { ...state, uncertain: [] };
  assert.ok(
    revisionPriorities(questions, cleared).every((t) => t.uncertain === 0),
  );
});

test("unsubmitted mock questions do not feed revision recommendations", () => {
  const q = questions.find((q) => q.status === "ready")!;
  const activeSession = createSession([q], "exam", "No answer hints", 10);
  const state = { ...blank(), activeSession, uncertain: [q.id] };
  assert.ok(
    revisionPriorities(questions, state).every(
      (t) => !t.uncertain && !t.missed,
    ),
  );
});

test("old v1 backups restore without revision fields; malformed new fields cannot replace progress", () => {
  assert.deepEqual(validateBackup(blank(), questions), blank());
  assert.throws(() =>
    validateBackup({ ...blank(), uncertain: ["foreign-id"] }, questions),
  );
  assert.throws(() =>
    validateBackup(
      { ...blank(), recall: { x: { rating: "known", at: 100, due: 50 } } },
      questions,
    ),
  );
  assert.throws(() =>
    validateBackup(
      { ...blank(), mistakes: { [questions[0].id]: "invalid" } },
      questions,
    ),
  );
  const tasks = sprintTasks(0, true);
  assert.equal(tasks[2].count, 10);
  assert.equal(sprintTasks(2, false)[2].count, 65);
});
