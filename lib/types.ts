export type DomainId = "secure" | "resilient" | "performance" | "cost";
export type Question = {
  id: string;
  number: number;
  title: string;
  prompt: string;
  options: string[];
  select: number;
  correct: number[];
  explanations: string[];
  takeaway: string;
  domain: DomainId;
  topic: string;
  sources: string[];
  sourcePaths?: string[];
  batch?: string;
  reasoning?: {
    ask: string;
    requirements: string[];
    why: string;
    alternative: string;
    alternativeWhen: string;
  };
  status: "ready" | "review" | "legacy";
  note: string;
  adapted?: boolean;
  readMore: { title: string; url: string }[];
};
export type Attempt = {
  questionId: string;
  sessionId: string;
  selected: number[];
  correct: boolean;
  seconds: number;
  at: number;
  mode: "practice" | "exam";
};
export type Session = {
  id: string;
  mode: "practice" | "exam";
  title: string;
  questionIds: string[];
  answers: Record<string, number[]>;
  checked: string[];
  flagged: string[];
  seconds: Record<string, number>;
  index: number;
  startedAt: number;
  deadline: number | null;
  completedAt: number | null;
};
export type StudyState = {
  version: 1;
  examDate: string;
  dailyTarget: number;
  attempts: Attempt[];
  bookmarks: string[];
  completedTasks: string[];
  sessions: Session[];
  activeSession: Session | null;
  storageError: string;
  uncertain?: string[];
  mistakes?: Record<string, "concept" | "services" | "requirement" | "timing">;
  recall?: Record<
    string,
    { rating: "again" | "known"; at: number; due: number }
  >;
};
export type Tab =
  | "dashboard"
  | "practice"
  | "exams"
  | "analytics"
  | "review"
  | "revision"
  | "library"
  | "settings";
