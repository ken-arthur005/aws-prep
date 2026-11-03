import { REVISION_TOPICS, type RevisionTopic } from "./revision-content";
import { latestAttempts } from "./study";
import type { Question, StudyState } from "./types";

const fallback: Record<string, string> = {
  "Identity & access": "iam",
  "Encryption & key management": "keys",
  "Network security": "security",
  "Disaster recovery": "dr",
  "Messaging & integration": "messaging",
  "Cost optimization": "cost-tools",
  "Database architecture": "rds",
  "DNS & routing": "dns",
  "Storage architecture": "s3",
  "Compute & containers": "containers",
  Observability: "observability",
  "Audit & observability": "observability",
};
const conceptCache = new WeakMap<Question, RevisionTopic[]>();
export function questionConcepts(q: Question) {
  const cached = conceptCache.get(q);
  if (cached) return cached;
  // Correct-option and takeaway text outweigh distracting service names in the scenario.
  const core =
    `${q.takeaway} ${q.correct.map((i) => q.options[i]).join(" ")}`.toLowerCase();
  const prompt = `${q.topic} ${q.prompt}`.toLowerCase();
  const contains = (text: string, keyword: string) =>
    new RegExp(
      `(^|[^a-z0-9])${keyword.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}([^a-z0-9]|$)`,
      "i",
    ).test(text);
  const ranked = REVISION_TOPICS.filter((t) => t.id !== "exam-technique")
    .map((t) => ({
      topic: t,
      score: t.keywords.reduce(
        (score, word) =>
          score +
          (contains(core, word) ? 4 : 0) +
          (contains(prompt, word) ? 1 : 0),
        0,
      ),
    }))
    .filter((t) => t.score > 0)
    .sort((a, b) => b.score - a.score);
  const concepts = ranked.length
    ? ranked.slice(0, 3).map((t) => t.topic)
    : [
        REVISION_TOPICS.find(
          (t) => t.id === (fallback[q.topic] ?? "architecture"),
        )!,
      ];
  conceptCache.set(q, concepts);
  return concepts;
}

export const RECALL_CARDS = REVISION_TOPICS.flatMap((topic) => [
  {
    id: `${topic.id}:scenario`,
    topicId: topic.id,
    prompt: topic.scenario.prompt,
    answer: topic.scenario.answer,
    why: topic.scenario.why,
    contrast: topic.scenario.instead,
  },
  ...topic.choices.map((choice, i) => ({
    id: `${topic.id}:choice:${i}`,
    topicId: topic.id,
    prompt: `Which tool or pattern fits? ${choice.when}`,
    answer: choice.service,
    why: choice.watch,
    contrast: topic.rules[0],
  })),
]);

export function revisionPriorities(bank: Question[], state: StudyState) {
  const latest = latestAttempts(state.attempts);
  const uncertain = new Set(state.uncertain ?? []);
  const evidence = new Map(
    REVISION_TOPICS.map((t) => [t.id, { missed: 0, uncertain: 0, seen: 0 }]),
  );
  for (const q of bank.filter((q) => q.status === "ready")) {
    if (
      state.activeSession?.mode === "exam" &&
      state.activeSession.questionIds.includes(q.id)
    )
      continue;
    const attempt = latest.get(q.id);
    if (!attempt && !uncertain.has(q.id)) continue;
    for (const t of questionConcepts(q)) {
      const row = evidence.get(t.id)!;
      if (attempt) row.seen++;
      if (attempt && !attempt.correct) row.missed++;
      if (uncertain.has(q.id)) row.uncertain++;
    }
  }
  return REVISION_TOPICS.map((topic) => ({
    topic,
    ...evidence.get(topic.id)!,
  })).sort(
    (a, b) =>
      b.missed * 2 + b.uncertain - (a.missed * 2 + a.uncertain) ||
      b.seen - a.seen,
  );
}

export function sourceUrl(q: Question, source: string) {
  const path = q.sourcePaths?.[q.sources.indexOf(source)];
  return path
    ? path.split("/").map(encodeURIComponent).join("/")
    : `/questions/${encodeURIComponent(source)}`;
}

export function objective(q: Question) {
  const text = q.prompt.toLowerCase();
  if (
    /least operational|minimum operational|minimizing.{0,30}overhead|minimal.{0,20}management/.test(
      text,
    )
  )
    return "First meet every requirement; then prefer the supported solution with the least management work.";
  if (
    /cost.effective|cost.optim|lowest cost|minimi[sz].{0,25}cost|reduce.{0,15}cost/.test(
      text,
    )
  )
    return "Eliminate designs that miss a requirement; compare the total cost of the remaining valid designs.";
  if (/rpo|rto|disaster|highly available|high availability/.test(text))
    return "Identify the failure scope and recovery objectives. Availability, data loss, and restore time are different constraints.";
  return "Check the required protocol, access pattern, security, and failure scope before matching a service name.";
}

export function sprintTasks(remaining: number, hasAttempts: boolean) {
  return [
    {
      title: hasAttempts
        ? "Check your fresh-question evidence"
        : "Find your starting point",
      detail: "20–25 mixed questions. Review wrong and uncertain answers.",
      action: "Take a diagnostic",
      count: 25,
    },
    {
      title: "Repair the biggest distinctions",
      detail:
        "Read the relevant comparison, explain it aloud, then practise related scenarios.",
      action: "Train weak areas",
      count: 20,
    },
    {
      title:
        remaining === 0
          ? "Reinforce your reasoning"
          : "Give exam day a dress rehearsal",
      detail:
        remaining === 0
          ? "A short mixed set with careful review; leave room for breaks."
          : "65 questions, 130 minutes. Leave substantial time to review uncertain choices.",
      action: remaining === 0 ? "Short practice" : "Take a full mock",
      count: remaining === 0 ? 10 : 65,
    },
    {
      title: "Last lap: retrieve, then check",
      detail:
        "Pocket cards, remaining mistakes, and a short recall check. Rest before the exam.",
      action: "Review & reinforce",
      count: 10,
    },
  ];
}
