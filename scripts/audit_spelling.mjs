import { createRequire } from "node:module";
import { readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
const require = createRequire(import.meta.url);
const root = process.env.COPYEDIT_TOOLS;
const nspell = require(join(root, "nspell"));
const spell = nspell({
  aff: readFileSync(join(root, "dictionary-en/index.aff")),
  dic: readFileSync(join(root, "dictionary-en/index.dic")),
});
const bank = JSON.parse(readFileSync("data/questions.json", "utf8")).questions;
const words = new Map();
for (const q of bank) {
  if (q.status !== "ready") continue;
  const fields = {
    prompt: q.prompt,
    ...Object.fromEntries(q.options.map((v, i) => [`option-${i}`, v])),
    ...Object.fromEntries(
      q.explanations.map((v, i) => [`explanation-${i}`, v]),
    ),
    takeaway: q.takeaway,
    note: q.note,
  };
  for (const [field, value] of Object.entries(fields)) {
    const clean = value.replace(
      /https?:\/\/\S+|arn:\S+|\b[a-z0-9_.-]+\.(?:com|org|net)\b/gi,
      " ",
    );
    for (const word of clean.match(/[A-Za-z][A-Za-z'-]{2,}/g) ?? []) {
      if (spell.correct(word) || /^[A-Z]+$/.test(word)) continue;
      const found = words.get(word) ?? {
        word,
        count: 0,
        locations: [],
        suggestions: [],
      };
      found.count++;
      if (found.locations.length < 8)
        found.locations.push(`${q.number}:${field}`);
      words.set(word, found);
    }
  }
}
const result = [...words.values()].sort((a, b) => b.count - a.count);
for (const row of result)
  if (!/^[A-Z]/.test(row.word) || /[A-Z].*[A-Z]/.test(row.word.slice(1)))
    row.suggestions = spell.suggest(row.word).slice(0, 4);
writeFileSync("data/copyedit-spelling.json", JSON.stringify(result, null, 2));
writeFileSync(
  "data/copyedit-spelling.txt",
  result
    .map(
      (r) =>
        `${r.word} (${r.count}) ${r.locations.join(" ")} -> ${r.suggestions.join(", ")}`,
    )
    .join("\n"),
);
console.log(
  `${result.length} distinct dictionary misses (including service names and technical terms); reviewed in context, never autocorrected.`,
);
