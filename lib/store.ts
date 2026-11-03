"use client";

import { useSyncExternalStore } from "react";
import type { StudyState, Question, Session } from "./types";
import aliases from "../data/source-aliases.json";

const KEY = "cloudbound-study-v1";
// Confirmed personal exam target; saved dates and restored backups are preserved.
const DEFAULT_EXAM_DATE = "2026-11-05";
const EMPTY: StudyState = {
  version: 1,
  examDate: "",
  dailyTarget: 40,
  attempts: [],
  bookmarks: [],
  completedTasks: [],
  sessions: [],
  activeSession: null,
  storageError: "",
};
let current = EMPTY;
let loaded = false;
const listeners = new Set<() => void>();
const sourceAliases: Record<string, string> = aliases;

export function reconcileSourceBookmarks(state: StudyState): StudyState {
  const bookmarks = [
    ...new Set(state.bookmarks.map((id) => sourceAliases[id] ?? id)),
  ];
  return bookmarks.length === state.bookmarks.length &&
    bookmarks.every((id, i) => id === state.bookmarks[i])
    ? state
    : { ...state, bookmarks };
}

function isSession(value: unknown, ids: Set<string>): value is Session {
  if (!value || typeof value !== "object") return false;
  const s = value as Session;
  return (
    typeof s.id === "string" &&
    typeof s.title === "string" &&
    ["practice", "exam"].includes(s.mode) &&
    Array.isArray(s.questionIds) &&
    s.questionIds.length > 0 &&
    s.questionIds.length <= 1000 &&
    new Set(s.questionIds).size === s.questionIds.length &&
    s.questionIds.every((id) => ids.has(id)) &&
    typeof s.answers === "object" &&
    s.answers !== null &&
    Object.values(s.answers).every(
      (a) =>
        Array.isArray(a) &&
        a.every((i) => Number.isInteger(i) && i >= 0 && i < 8),
    ) &&
    Array.isArray(s.checked) &&
    s.checked.every((id) => typeof id === "string") &&
    Array.isArray(s.flagged) &&
    s.flagged.every((id) => typeof id === "string") &&
    typeof s.seconds === "object" &&
    s.seconds !== null &&
    Object.values(s.seconds).every((n) => Number.isFinite(n) && n >= 0) &&
    Number.isInteger(s.index) &&
    s.index >= 0 &&
    s.index < s.questionIds.length &&
    Number.isFinite(s.startedAt) &&
    (s.deadline === null || Number.isFinite(s.deadline)) &&
    (s.completedAt === null || Number.isFinite(s.completedAt))
  );
}
export function validateBackup(value: unknown, bank?: Question[]): StudyState {
  if (!value || typeof value !== "object")
    throw new Error("Choose a Cloudbound JSON backup.");
  const original = value as StudyState;
  const s =
    Array.isArray(original.bookmarks) &&
    original.bookmarks.every((id) => typeof id === "string")
      ? reconcileSourceBookmarks(original)
      : original;
  const ids = new Set(
    bank?.map((q) => q.id) ?? [
      ...(Array.isArray(s.sessions)
        ? s.sessions.flatMap((session) => session.questionIds ?? [])
        : []),
      ...(s.activeSession?.questionIds ?? []),
    ],
  );
  const date =
    /^\d{4}-\d{2}-\d{2}$/.test(s.examDate ?? "") &&
    !Number.isNaN(Date.parse(`${s.examDate}T00:00:00`));
  if (
    s.version !== 1 ||
    !date ||
    !Number.isFinite(s.dailyTarget) ||
    s.dailyTarget < 1 ||
    s.dailyTarget > 500 ||
    !Array.isArray(s.attempts) ||
    !Array.isArray(s.bookmarks) ||
    !s.bookmarks.every((id) => typeof id === "string") ||
    !Array.isArray(s.completedTasks) ||
    !s.completedTasks.every((id) => typeof id === "string") ||
    !Array.isArray(s.sessions) ||
    !s.sessions.every((session) => isSession(session, ids)) ||
    (s.activeSession !== null && !isSession(s.activeSession, ids))
  )
    throw new Error("This backup has missing or invalid study data.");
  if (
    !s.attempts.every(
      (a) =>
        a &&
        typeof a.questionId === "string" &&
        typeof a.sessionId === "string" &&
        typeof a.correct === "boolean" &&
        Number.isFinite(a.at) &&
        Number.isFinite(a.seconds) &&
        a.seconds >= 0 &&
        ["practice", "exam"].includes(a.mode) &&
        Array.isArray(a.selected) &&
        a.selected.every((i) => Number.isInteger(i) && i >= 0 && i < 8),
    )
  )
    throw new Error("This backup contains invalid answer records.");
  if (
    s.uncertain !== undefined &&
    (!Array.isArray(s.uncertain) ||
      !s.uncertain.every(
        (id) => typeof id === "string" && (!bank || ids.has(id)),
      ))
  )
    throw new Error(
      "This backup contains invalid uncertain-question references.",
    );
  if (
    s.mistakes !== undefined &&
    (!s.mistakes ||
      typeof s.mistakes !== "object" ||
      Array.isArray(s.mistakes) ||
      !Object.entries(s.mistakes).every(
        ([id, reason]) =>
          (!bank || ids.has(id)) &&
          ["concept", "services", "requirement", "timing"].includes(reason),
      ))
  )
    throw new Error("This backup contains invalid mistake notes.");
  if (
    s.recall !== undefined &&
    (!s.recall ||
      typeof s.recall !== "object" ||
      Array.isArray(s.recall) ||
      !Object.values(s.recall).every(
        (record) =>
          record &&
          ["again", "known"].includes(record.rating) &&
          Number.isFinite(record.at) &&
          Number.isFinite(record.due) &&
          record.at >= 0 &&
          record.due >= record.at,
      ))
  )
    throw new Error("This backup contains invalid recall records.");
  if (
    bank &&
    (s.attempts.some((a) => !ids.has(a.questionId)) ||
      s.bookmarks.some((id) => !ids.has(id)))
  )
    throw new Error(
      "This backup refers to questions that are not in this question bank.",
    );
  for (const session of [
    ...s.sessions,
    ...(s.activeSession ? [s.activeSession] : []),
  ]) {
    const sessionIds = new Set(session.questionIds);
    if (
      [
        ...session.checked,
        ...session.flagged,
        ...Object.keys(session.answers),
        ...Object.keys(session.seconds),
      ].some((id) => !sessionIds.has(id))
    )
      throw new Error(
        "This backup contains an invalid session question reference.",
      );
    if (
      Object.values(session.answers).some(
        (answer) => new Set(answer).size !== answer.length,
      )
    )
      throw new Error("This backup contains duplicate answer selections.");
    if (bank)
      for (const [id, selected] of Object.entries(session.answers)) {
        const q = bank.find((question) => question.id === id)!;
        if (
          selected.some((index) => index >= q.options.length) ||
          selected.length > q.select
        )
          throw new Error("This backup contains invalid answer selections.");
      }
  }
  if (
    s.activeSession?.completedAt !== undefined &&
    s.activeSession.completedAt !== null
  )
    throw new Error("The saved active session is already complete.");
  if (
    new Set(s.sessions.map((session) => session.id)).size !== s.sessions.length
  )
    throw new Error("This backup contains duplicate completed sessions.");
  return { ...s, storageError: "" };
}
function snapshot() {
  if (!loaded && typeof window !== "undefined") {
    loaded = true;
    current = { ...EMPTY, examDate: DEFAULT_EXAM_DATE };
    try {
      const raw = localStorage.getItem(KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        current = validateBackup(parsed);
        if (
          JSON.stringify(parsed.bookmarks) !== JSON.stringify(current.bookmarks)
        ) {
          try {
            localStorage.setItem(KEY, JSON.stringify(current));
          } catch {
            current = {
              ...current,
              storageError:
                "Merged-source bookmarks were recovered but could not be saved. Export a backup before closing this page.",
            };
          }
        }
      }
    } catch {
      current = {
        ...current,
        storageError:
          "Saved progress could not be loaded. You can restore a backup in Settings.",
      };
    }
  }
  return current;
}
export const getStudy = snapshot;
export function updateStudy(update: (state: StudyState) => StudyState) {
  const next = update(snapshot());
  if (next === current) return;
  current = next;
  try {
    localStorage.setItem(KEY, JSON.stringify({ ...next, storageError: "" }));
  } catch {
    current = {
      ...next,
      storageError:
        "Your browser could not save progress. Export a backup before closing this page.",
    };
  }
  listeners.forEach((listener) => listener());
}
export function useStudy() {
  return useSyncExternalStore(
    (listener) => {
      listeners.add(listener);
      return () => {
        listeners.delete(listener);
      };
    },
    snapshot,
    () => EMPTY,
  );
}
export function resetStudy() {
  updateStudy(() => ({ ...EMPTY, examDate: DEFAULT_EXAM_DATE }));
}
