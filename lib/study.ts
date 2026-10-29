import type { Attempt, DomainId, Question, Session, StudyState } from "./types";

export const DOMAINS: { id: DomainId; name: string; short: string; weight: number; color: string; description: string }[] = [
  { id: "secure", name: "Design Secure Architectures", short: "Secure", weight: 30, color: "mint", description: "IAM, encryption, network protection & data security" },
  { id: "resilient", name: "Design Resilient Architectures", short: "Resilient", weight: 26, color: "blue", description: "High availability, recovery & loosely coupled systems" },
  { id: "performance", name: "Design High-Performing Architectures", short: "High-performing", weight: 24, color: "peach", description: "Scalable compute, storage, databases & networks" },
  { id: "cost", name: "Design Cost-Optimized Architectures", short: "Cost-optimized", weight: 20, color: "yellow", description: "Right-size resources & make smarter tradeoffs" },
];
export const EXAM_GUIDE = "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html";

export function isCorrect(question: Question, selected: number[] = []) {
  return question.correct.length > 0 && selected.length === question.correct.length && question.correct.every(i => selected.includes(i));
}
export function percent(right: number, total: number) { return total ? Math.round(right / total * 100) : 0; }
export function accuracy(attempts: Attempt[]) { return percent(attempts.filter(a => a.correct).length, attempts.length); }
export function firstAttempts(attempts: Attempt[]) {
  const seen = new Set<string>();
  return [...attempts].sort((a, b) => a.at - b.at).filter(a => { if (seen.has(a.questionId)) return false; seen.add(a.questionId); return true; });
}
export function latestAttempts(attempts: Attempt[]) {
  const latest = new Map<string, Attempt>();
  for (const a of [...attempts].sort((a, b) => a.at - b.at)) latest.set(a.questionId, a);
  return latest;
}
export function shuffle<T>(items: T[]): T[] {
  const result = [...items];
  for (let i = result.length - 1; i > 0; i--) {
    const array = new Uint32Array(1);
    const value = typeof crypto !== "undefined" ? crypto.getRandomValues(array)[0] / 4294967296 : Math.random();
    const j = Math.floor(value * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}
export function selectQuestions(pool: Question[], count: number, attempts: Attempt[], weighted = false) {
  const eligible = pool.filter(q => q.status === "ready");
  const recent = new Map<string, number>();
  for (const a of attempts) recent.set(a.questionId, Math.max(recent.get(a.questionId) ?? 0, a.at));
  const prioritize = (items: Question[]) => shuffle(items).sort((a, b) => (recent.get(a.id) ?? 0) - (recent.get(b.id) ?? 0));
  if (!weighted) return prioritize(eligible).slice(0, count);
  const total = Math.min(count, eligible.length);
  const quotas = DOMAINS.map(d => ({ id: d.id, n: Math.floor(total * d.weight / 100), remainder: total * d.weight / 100 % 1 }));
  let remaining = total - quotas.reduce((sum, q) => sum + q.n, 0);
  for (const q of [...quotas].sort((a, b) => b.remainder - a.remainder)) if (remaining-- > 0) q.n++;
  const picked = quotas.flatMap(q => prioritize(eligible.filter(item => item.domain === q.id)).slice(0, q.n));
  const used = new Set(picked.map(q => q.id));
  picked.push(...prioritize(eligible.filter(q => !used.has(q.id))).slice(0, total - picked.length));
  return shuffle(picked);
}
export function createSession(questions: Question[], mode: Session["mode"], title: string, minutes?: number): Session {
  const startedAt = Date.now();
  return { id: crypto.randomUUID(), mode, title, questionIds: questions.map(q => q.id), answers: {}, checked: [], flagged: [], seconds: {}, index: 0, startedAt, deadline: minutes ? startedAt + minutes * 60_000 : null, completedAt: null };
}
export function finishSession(state: StudyState, bank: Question[], at = Date.now()): StudyState {
  const session = state.activeSession;
  if (!session || state.sessions.some(s => s.id === session.id)) return state;
  const completed = { ...session, completedAt: at };
  const lookup = new Map(bank.map(q => [q.id, q]));
  const existing = new Set(state.attempts.filter(a => a.sessionId === session.id).map(a => a.questionId));
  const additions: Attempt[] = session.questionIds.flatMap(id => {
    const question = lookup.get(id);
    if (!question || existing.has(id) || (session.mode === "practice" && !session.checked.includes(id))) return [];
    return [{ questionId: id, sessionId: session.id, selected: session.answers[id] ?? [], correct: isCorrect(question, session.answers[id]), seconds: session.seconds[id] ?? 0, at, mode: session.mode }];
  });
  return { ...state, activeSession: null, sessions: [...state.sessions, completed], attempts: [...state.attempts, ...additions] };
}
export function formatTime(seconds: number) {
  const s = Math.max(0, Math.floor(seconds));
  return `${Math.floor(s / 60).toString().padStart(2, "0")}:${(s % 60).toString().padStart(2, "0")}`;
}
export function localDate(date = new Date()) { return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`; }
export function daysUntil(date: string) {
  if (!date) return 4;
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const target = new Date(`${date}T00:00:00`);
  return Math.max(0, Math.ceil((target.getTime() - today.getTime()) / 86400000));
}
export function domainStats(bank: Question[], attempts: Attempt[]) {
  const first = firstAttempts(attempts);
  return DOMAINS.map(domain => {
    const ids = new Set(bank.filter(q => q.domain === domain.id && q.status === "ready").map(q => q.id));
    const records = attempts.filter(a => ids.has(a.questionId));
    const initial = first.filter(a => ids.has(a.questionId));
    return { ...domain, total: ids.size, attempted: initial.length, accuracy: accuracy(records), firstAccuracy: accuracy(initial), attempts: records.length, priority: domain.weight * (1 - (initial.filter(a => a.correct).length + 1) / (initial.length + 2)) };
  });
}
