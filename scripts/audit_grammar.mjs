// Local-only LanguageTool audit. Suggestions are editorial flags, never automatic edits.
import { spawn } from "node:child_process";
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { createHash } from "node:crypto";
import { setTimeout as delay } from "node:timers/promises";
const base = "http://127.0.0.1:8093";
const server = spawn(
  process.env.COPYEDIT_JAVA,
  ["-Xmx1200m", "-jar", process.env.COPYEDIT_LT, "--port", "8093"],
  { stdio: "pipe" },
);
let diagnostics = "";
server.stdout.on("data", (chunk) => {
  diagnostics += chunk;
});
server.stderr.on("data", (chunk) => {
  diagnostics += chunk;
});
const bank = JSON.parse(
  readFileSync("data/questions.json", "utf8"),
).questions.filter((q) => q.status === "ready");
const cacheFile = "data/copyedit-grammar.json";
const cache = existsSync(cacheFile)
  ? JSON.parse(readFileSync(cacheFile, "utf8"))
  : {};
const disabledRules =
  "MORFOLOGIK_RULE_EN_US,EN_QUOTES,WHITESPACE_RULE,ENGLISH_WORD_REPEAT_BEGINNING_RULE";
try {
  let ready = false;
  for (let n = 0; n < 300; n++) {
    try {
      const r = await fetch(`${base}/v2/languages`);
      if (r.ok) {
        ready = true;
        break;
      }
    } catch {}
    if (server.exitCode !== null) break;
    await delay(200);
  }
  if (!ready) throw new Error(diagnostics);
  for (let i = 0; i < bank.length; i++) {
    const q = bank[i];
    const fields = {
      prompt: q.prompt,
      ...Object.fromEntries(q.options.map((v, i) => [`option-${i}`, v])),
      ...Object.fromEntries(
        q.explanations.map((v, i) => [`explanation-${i}`, v]),
      ),
      takeaway: q.takeaway,
      note: q.note,
      ...q.reasoning,
    };
    let text = "";
    const spans = [];
    for (const [field, value] of Object.entries(fields)) {
      if (typeof value !== "string" || !value) continue;
      spans.push({
        field,
        start: text.length,
        end: text.length + value.length,
      });
      text += value + "\n\n";
    }
    const hash = createHash("sha256")
      .update(disabledRules + "\n" + text)
      .digest("hex");
    if (cache[q.id]?.hash !== hash) {
      const r = await fetch(`${base}/v2/check`, {
        method: "POST",
        body: new URLSearchParams({ text, language: "en-US", disabledRules }),
      });
      if (!r.ok) throw new Error(await r.text());
      const { matches } = await r.json();
      cache[q.id] = {
        number: q.number,
        hash,
        matches: matches.map((m) => ({
          rule: m.rule.id,
          message: m.message,
          field: spans.find((s) => m.offset >= s.start && m.offset < s.end)
            ?.field,
          offset:
            m.offset -
            (spans.find((s) => m.offset >= s.start && m.offset < s.end)
              ?.start ?? 0),
          length: m.length,
          found: text.slice(m.offset, m.offset + m.length),
          context: m.context.text,
          suggestions: m.replacements.slice(0, 4).map((r) => r.value),
        })),
      };
    }
    if ((i + 1) % 25 === 0 || i === bank.length - 1) {
      writeFileSync(cacheFile, JSON.stringify(cache, null, 2));
      console.log(`Grammar checked ${i + 1}/${bank.length}`);
    }
  }
  const lines = bank.flatMap((q) =>
    cache[q.id].matches.map(
      (m) =>
        `#${q.number} ${m.field} [${m.rule}] ${JSON.stringify(m.found)} -> ${m.suggestions.join(" | ")}\n${m.message}\n${m.context}\n`,
    ),
  );
  writeFileSync("data/copyedit-grammar.txt", lines.join("\n"));
  console.log(
    `${bank.length} complete ready records checked locally; ${lines.length} suggestions for editorial review.`,
  );
} finally {
  server.kill();
}
