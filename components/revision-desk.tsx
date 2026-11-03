"use client";

import { useEffect, useMemo, useState } from "react";
import {
  ArrowRight,
  BookOpen,
  Check,
  ChevronRight,
  Clock3,
  Lightbulb,
  Printer,
  RotateCcw,
  Search,
  Sparkles,
  Target,
} from "lucide-react";
import {
  REVISION_REVIEWED,
  REVISION_TOPICS,
  type RevisionTopic,
} from "@/lib/revision-content";
import {
  objective,
  questionConcepts,
  RECALL_CARDS,
  revisionPriorities,
} from "@/lib/revision";
import { updateStudy } from "@/lib/store";
import { DOMAINS } from "@/lib/study";
import type { Question, StudyState } from "@/lib/types";

type Mode = "understand" | "compare" | "recall" | "last-lap";
const MODES: { id: Mode; label: string; description: string }[] = [
  {
    id: "understand",
    label: "Understand",
    description: "Build the mental model",
  },
  { id: "compare", label: "Compare", description: "Choose between services" },
  {
    id: "recall",
    label: "Quick recall",
    description: "Retrieve before revealing",
  },
  { id: "last-lap", label: "Last lap", description: "Your final-review sheet" },
];

export function RevisionDesk({
  questions,
  state,
  start,
  now,
}: {
  questions: Question[];
  state: StudyState;
  start: (pool: Question[], title: string) => void;
  now: number;
}) {
  const [mode, setMode] = useState<Mode>("understand");
  const [topicId, setTopicId] = useState("vpc");
  const [search, setSearch] = useState("");
  const [scope, setScope] = useState("weak");
  const priorities = useMemo(
    () => revisionPriorities(questions, state),
    [questions, state],
  );
  const weak = priorities.filter((t) => t.missed || t.uncertain);
  useEffect(() => {
    const readHash = () => {
      const [, id, requestedMode] = window.location.hash.slice(1).split("/");
      if (REVISION_TOPICS.some((t) => t.id === id)) setTopicId(id);
      if (MODES.some((m) => m.id === requestedMode))
        setMode(requestedMode as Mode);
    };
    queueMicrotask(readHash);
    window.addEventListener("hashchange", readHash);
    return () => window.removeEventListener("hashchange", readHash);
  }, []);
  const topic = REVISION_TOPICS.find((t) => t.id === topicId)!;
  const matching = REVISION_TOPICS.filter((t) => {
    const haystack =
      `${t.title} ${t.idea} ${t.keywords.join(" ")} ${t.choices.map((c) => `${c.service} ${c.when} ${c.watch}`).join(" ")}`.toLowerCase();
    return search
      .toLowerCase()
      .trim()
      .split(/\s+/)
      .every((word) => haystack.includes(word));
  });
  const poolFor = (id: string) =>
    questions.filter(
      (q) =>
        q.status === "ready" && questionConcepts(q).some((t) => t.id === id),
    );
  const pool = poolFor(topic.id);
  const recallTopics =
    scope === "all"
      ? REVISION_TOPICS.map((t) => t.id)
      : scope === "weak"
        ? weak.length
          ? weak.map((t) => t.topic.id)
          : ["vpc", "s3", "rds", "messaging", "iam", "exam-technique"]
        : [scope];
  function open(id: string, next = mode) {
    setTopicId(id);
    setMode(next);
    window.history.replaceState(null, "", `#revision/${id}/${next}`);
  }
  return (
    <div className="revision-desk">
      <div className="page-heading">
        <div>
          <div className="eyebrow">LESS SCROLLING. MORE LIGHTBULBS.</div>
          <h1>Your revision desk.</h1>
          <p>
            Understand the idea. Compare the tradeoff. Close the notes and
            retrieve it.
          </p>
        </div>
        <span className="revision-stamp">
          <BookOpen size={18} />
          {REVISION_TOPICS.length} curated guides
        </span>
      </div>
      <div className="revision-modes" aria-label="Revision views">
        {MODES.map((m) => (
          <button
            key={m.id}
            className={mode === m.id ? "selected" : ""}
            aria-pressed={mode === m.id}
            onClick={() => open(topicId, m.id)}
          >
            <strong>{m.label}</strong>
            <small>{m.description}</small>
          </button>
        ))}
      </div>
      {weak.length > 0 && (
        <section className="revision-recommendation">
          <Target size={23} />
          <div>
            <strong>Your next useful distinction</strong>
            <p>
              {weak[0].topic.title} · {weak[0].missed} latest misses ·{" "}
              {weak[0].uncertain} marked unsure. Topic signals can overlap.
            </p>
          </div>
          <button
            className="button small"
            onClick={() => open(weak[0].topic.id, "compare")}
          >
            Repair this <ArrowRight size={15} />
          </button>
        </section>
      )}
      {mode === "recall" ? (
        <>
          <div className="recall-heading">
            <div>
              <h2>Say your answer before you peek.</h2>
              <p>
                These are concept checks. Their results are separate from
                practice and mock accuracy.
              </p>
            </div>
            <label>
              Recall stack
              <select value={scope} onChange={(e) => setScope(e.target.value)}>
                <option value="weak">
                  {weak.length
                    ? "My weak & uncertain concepts"
                    : "Core exam distinctions"}
                </option>
                <option value="all">All concepts</option>
                {REVISION_TOPICS.map((t) => (
                  <option key={t.id} value={t.id}>
                    {t.title}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <Recall
            key={scope + recallTopics.join(",")}
            topicIds={recallTopics}
            state={state}
            now={now}
            open={(id) => open(id, "understand")}
          />
        </>
      ) : mode === "last-lap" ? (
        <LastLap
          topics={[
            ...new Set([
              ...weak.slice(0, 6).map((t) => t.topic.id),
              "exam-technique",
              "vpc",
              "network-links",
              "s3",
              "block-file",
              "rds",
              "dynamodb",
              "messaging",
              "edge",
              "observability",
              "security",
              "dr",
              "keys",
              "secrets",
              "containers",
            ]),
          ].map((id) => REVISION_TOPICS.find((t) => t.id === id)!)}
          open={(id) => open(id, "compare")}
        />
      ) : (
        <div className="revision-layout">
          <aside className="revision-index">
            <label className="search-input">
              <Search size={17} />
              <span className="sr-only">Search revision guides</span>
              <input
                placeholder="S3, private access, failover…"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
            </label>
            <p className="quiet-note">
              {matching.length} guides · search concepts and scenarios
            </p>
            <div className="revision-topic-list">
              {matching.map((t) => (
                <button
                  key={t.id}
                  aria-current={t.id === topic.id ? "page" : undefined}
                  className={t.id === topic.id ? "selected" : ""}
                  onClick={() => open(t.id)}
                >
                  <span>{t.title}</span>
                  <ChevronRight size={14} />
                </button>
              ))}
              {!matching.length && (
                <p>No guides match. Try a service or a broader phrase.</p>
              )}
            </div>
          </aside>
          <article className="revision-article" key={topic.id + mode}>
            <div className="revision-article-meta">
              <span
                className={`chip ${DOMAINS.find((d) => d.id === topic.domain)!.color}`}
              >
                {DOMAINS.find((d) => d.id === topic.domain)!.short}
              </span>
              <span>Reviewed {REVISION_REVIEWED} · ~3 min</span>
            </div>
            <h2>{topic.title}</h2>
            {mode === "understand" && (
              <>
                <section className="revision-idea">
                  <span className="eyebrow">THE IDEA IN 30 SECONDS</span>
                  <p>{topic.idea}</p>
                </section>
                <div className="revision-analogy">
                  <Lightbulb size={22} />
                  <p>{topic.analogy}</p>
                </div>
              </>
            )}
            <h3>
              {mode === "compare"
                ? "What makes the answer change?"
                : "Choose by the requirement."}
            </h3>
            <Comparison topic={topic} />
            <section className="revision-rules">
              <h3>Constraints worth remembering.</h3>
              <ul>
                {topic.rules.map((rule) => (
                  <li key={rule}>{rule}</li>
                ))}
              </ul>
            </section>
            <section className="worked-scenario">
              <span className="eyebrow">A WORKED CONNECTION</span>
              <h3>{topic.scenario.prompt}</h3>
              <p>
                <strong>The fit:</strong> {topic.scenario.answer}
              </p>
              <p>
                <strong>Why:</strong> {topic.scenario.why}
              </p>
              <p>
                <strong>When the answer changes:</strong>{" "}
                {topic.scenario.instead}
              </p>
            </section>
            <div className="revision-next">
              <div>
                <strong>Now close the notes.</strong>
                <p>
                  Explain the distinction in your own words, then try a fresh
                  scenario.
                </p>
              </div>
              <div className="button-row">
                <button
                  className="button"
                  onClick={() => {
                    setScope(topic.id);
                    open(topic.id, "recall");
                  }}
                >
                  Test my recall <Sparkles size={16} />
                </button>
                <button
                  className="button primary"
                  disabled={!pool.length || !!state.activeSession}
                  onClick={() => start(pool, topic.title)}
                >
                  Practise this concept <ArrowRight size={16} />
                </button>
              </div>
              <small>
                {pool.length} linked study-ready questions · unseen questions
                prioritised
              </small>
            </div>
            <details className="revision-references">
              <summary>Sources, editorial approach & further reading</summary>
              <p>
                Original concise summaries informed by your supplied topic
                guides, with outdated shortcuts corrected. Adapted community
                guide credit:{" "}
                <a
                  href="https://github.com/RonitSachdev/aws-saa-c03-guides"
                  target="_blank"
                  rel="noreferrer"
                >
                  RonitSachdev — AWS SAA-C03 Guides
                </a>
                , under{" "}
                <a
                  href="https://creativecommons.org/licenses/by/4.0/"
                  target="_blank"
                  rel="noreferrer"
                >
                  CC BY 4.0
                </a>
                . Source guide: {topic.guide}. The summaries shorten and
                reorganise the source, add examples, and correct outdated
                details.
              </p>
              <a href={topic.reference} target="_blank" rel="noreferrer">
                Verify the underlying AWS behaviour ↗
              </a>
            </details>
          </article>
        </div>
      )}
    </div>
  );
}

function Comparison({ topic }: { topic: RevisionTopic }) {
  return (
    <div
      className="comparison-scroll"
      tabIndex={0}
      role="region"
      aria-label={`${topic.title} comparison`}
    >
      <table className="comparison-table">
        <thead>
          <tr>
            <th>Tool / pattern</th>
            <th>Choose when…</th>
            <th>Check before choosing</th>
          </tr>
        </thead>
        <tbody>
          {topic.choices.map((c) => (
            <tr key={c.service}>
              <th scope="row">{c.service}</th>
              <td data-label="Choose when">{c.when}</td>
              <td data-label="Check before choosing">{c.watch}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function Recall({
  topicIds,
  state,
  now,
  open,
}: {
  topicIds: string[];
  state: StudyState;
  now: number;
  open: (id: string) => void;
}) {
  const cards = RECALL_CARDS.filter((c) => topicIds.includes(c.topicId));
  const [queue, setQueue] = useState(() =>
    [...cards]
      .sort(
        (a, b) =>
          (state.recall?.[a.id]?.due ?? 0) - (state.recall?.[b.id]?.due ?? 0),
      )
      .map((c) => c.id),
  );
  const [revealed, setRevealed] = useState(false);
  const [done, setDone] = useState(0);
  const card = cards.find((c) => c.id === queue[0]);
  const due = cards.filter(
    (c) => !state.recall?.[c.id] || state.recall[c.id].due <= now,
  ).length;
  function rate(rating: "again" | "known") {
    if (!card || !revealed) return;
    const at = Date.now();
    updateStudy((s) => ({
      ...s,
      recall: {
        ...s.recall,
        [card.id]: {
          rating,
          at,
          due: at + (rating === "again" ? 10 * 60_000 : 12 * 60 * 60_000),
        },
      },
    }));
    setQueue((q) => q.slice(1));
    setDone((n) => n + 1);
    setRevealed(false);
  }
  return (
    <section className="recall-card">
      <div className="section-heading">
        <span className="chip blue">ACTIVE RECALL</span>
        <span className="quiet-note">
          {done} checked this round · {due} due now
        </span>
      </div>
      {card ? (
        <>
          <span className="eyebrow">
            {REVISION_TOPICS.find((t) => t.id === card.topicId)!.title}
          </span>
          <h3>{card.prompt}</h3>
          {revealed ? (
            <div className="recall-answer" aria-live="polite">
              <h4>{card.answer}</h4>
              <p>{card.why}</p>
              <p>{card.contrast}</p>
              <div className="button-row">
                <button className="button" onClick={() => rate("again")}>
                  <RotateCcw size={16} /> Again in 10 min
                </button>
                <button
                  className="button primary"
                  onClick={() => rate("known")}
                >
                  <Check size={17} /> Got it · revisit in 12h
                </button>
              </div>
              <button
                className="text-button"
                onClick={() => open(card.topicId)}
              >
                Rebuild the mental model <ArrowRight size={15} />
              </button>
            </div>
          ) : (
            <>
              <p className="quiet-note">
                Name the solution and the constraint that rules out the tempting
                alternative.
              </p>
              <button
                className="button primary"
                onClick={() => setRevealed(true)}
              >
                Reveal & check my reasoning <Lightbulb size={17} />
              </button>
            </>
          )}
        </>
      ) : (
        <div className="recall-complete">
          <Check size={35} />
          <h3>A few more connections made.</h3>
          <p>
            You checked {done} cards. Come back for due reviews or choose
            another stack.
          </p>
          <button
            className="button"
            onClick={() => {
              setQueue(cards.map((c) => c.id));
              setDone(0);
            }}
          >
            Start another round <RotateCcw size={16} />
          </button>
        </div>
      )}
      <p className="recall-footnote">
        <Clock3 size={14} /> Due cards appear first; you can study ahead.
        Ratings are self-checks, not exam scores.
      </p>
    </section>
  );
}

function LastLap({
  topics,
  open,
}: {
  topics: RevisionTopic[];
  open: (id: string) => void;
}) {
  return (
    <section className="last-lap">
      <div className="section-heading">
        <div>
          <div className="eyebrow">A COMPACT FINAL PASS</div>
          <h2>Requirements first. Tradeoffs second.</h2>
          <p>
            Your weak concepts plus the core distinctions. Cover the right
            column and recall it first.
          </p>
        </div>
        <button className="button small" onClick={() => window.print()}>
          <Printer size={16} /> Print sheet
        </button>
      </div>
      <div className="last-lap-grid">
        {topics.map((t) => (
          <article key={t.id}>
            <h3>
              <button onClick={() => open(t.id)}>
                {t.title} <ArrowRight size={14} />
              </button>
            </h3>
            <dl>
              {t.choices.map((c) => (
                <div key={c.service}>
                  <dt>{c.when}</dt>
                  <dd>{c.service}</dd>
                </div>
              ))}
            </dl>
            <p>
              <strong>Watch:</strong> {t.rules[0]}
            </p>
          </article>
        ))}
      </div>
      <p className="quiet-note">
        Last editorial pass: {REVISION_REVIEWED}. This sheet uses the same
        content as the full guides and recall cards.
      </p>
    </section>
  );
}

export function ConceptConnections({ question: q }: { question: Question }) {
  const topics = questionConcepts(q);
  return (
    <section className="concept-connections">
      <span className="eyebrow">
        <Lightbulb size={16} /> REPAIR THE CONCEPT
      </span>
      <p>{objective(q)}</p>
      <div className="concept-links">
        {topics.map((t) => (
          <a href={`#revision/${t.id}/compare`} key={t.id}>
            {t.title}
            <ArrowRight size={15} />
          </a>
        ))}
      </div>
      <details>
        <summary>Practise the reasoning, not the answer letter</summary>
        <p>
          <strong>The decisive idea:</strong> {q.takeaway}
        </p>
        <p>
          <strong>A useful contrast:</strong> {topics[0].scenario.instead}
        </p>
        <p>
          Identify the exact requirement that eliminated your closest
          alternative. Then change one requirement and ask whether your choice
          would change.
        </p>
      </details>
    </section>
  );
}
