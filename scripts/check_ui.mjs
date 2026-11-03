// Run against a built server with PLAYWRIGHT_MODULE pointing at an installed playwright package.
import assert from "node:assert/strict";
import { createRequire } from "node:module";
import { join } from "node:path";
import { spawn } from "node:child_process";
import { setTimeout as delay } from "node:timers/promises";
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || "playwright");
const { questions } = require("../data/questions.json");
const base = process.env.UI_BASE_URL || "http://localhost:3100";
const artifacts = process.env.UI_ARTIFACTS;
const server = process.env.UI_START_SERVER === "1" ? spawn(process.execPath, ["node_modules/next/dist/bin/next", "start", "-p", new URL(base).port || "3100"], { stdio: "pipe" }) : null;
let serverOutput = "";
server?.stdout.on("data", chunk => { serverOutput += chunk; });
server?.stderr.on("data", chunk => { serverOutput += chunk; });
if (server) {
  let ready = false;
  for (let n = 0; n < 100; n++) {
    try { const response = await fetch(base); if (response.ok) { ready = true; break; } } catch { /* Wait for startup. */ }
    if (server.exitCode !== null) break;
    await delay(100);
  }
  if (!ready) { server.kill(); throw new Error(`Preview server did not start: ${serverOutput}`); }
}
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 1000 },
});
const page = await context.newPage();
const errors = [];
page.on("pageerror", (e) => errors.push(e.message));
const old = {
  version: 1,
  examDate: "2026-11-05",
  dailyTarget: 40,
  attempts: [],
  bookmarks: [questions[0].id],
  completedTasks: ["day-0"],
  sessions: [],
  activeSession: null,
  storageError: "",
};
await context.addInitScript((state) => {
  if (!localStorage.getItem("cloudbound-study-v1"))
    localStorage.setItem("cloudbound-study-v1", JSON.stringify(state));
}, old);
const saved = () =>
  page.evaluate(() => JSON.parse(localStorage.getItem("cloudbound-study-v1")));
async function noOverflow() {
  assert.ok(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth + 1,
    ),
    "page has horizontal overflow",
  );
}
async function navigate(hash) {
  await page.goto(`${base}/#${hash}`);
  await page.locator("main").waitFor();
}
try {
  await navigate("revision/vpc/compare");
  await page.getByRole("heading", { name: "Your revision desk." }).waitFor();
  await page
    .getByRole("heading", {
      name: "VPC: routes, NAT, and endpoints",
      exact: true,
    })
    .waitFor();
  await noOverflow();
  await page
    .getByRole("textbox", { name: "Search revision guides" })
    .fill("private S3 access");
  assert.ok(
    (await page.locator(".revision-topic-list button").count()) > 0,
    "multiword concept search failed",
  );
  await page.getByRole("textbox", { name: "Search revision guides" }).fill("");
  if (artifacts)
    await page.screenshot({
      path: join(artifacts, "revision-desktop.png"),
      fullPage: true,
      animations: "disabled",
    });
  await page.getByRole("button", { name: /^Quick recall/ }).click();
  await page.getByLabel("Recall stack").selectOption("vpc");
  await page.getByRole("button", { name: /Reveal & check/ }).click();
  await page.getByRole("button", { name: /Got it/ }).click();
  assert.equal(Object.keys((await saved()).recall).length, 1);
  assert.equal(
    (await saved()).attempts.length,
    0,
    "recall contaminated question accuracy",
  );
  await navigate("revision/vpc/last-lap");
  await page
    .getByRole("heading", { name: "Requirements first. Tradeoffs second." })
    .waitFor();
  await page.emulateMedia({ media: "print" });
  assert.equal(await page.locator(".sidebar").isVisible(), false);
  await page.emulateMedia({ media: "screen" });
  await navigate("practice");
  await page.getByLabel("Question selection").selectOption("new");
  await page.getByRole("button", { name: /Let.s practice/ }).click();
  await page.locator(".question-prompt").waitFor();
  const practice = (await saved()).activeSession;
  assert.ok(
    practice.questionIds.every(
      (id) => questions.find((q) => q.id === id)?.batch === "november",
    ),
  );
  const q = questions.find((q) => q.id === practice.questionIds[0]);
  await page.getByLabel(/Guessed \/ unsure/).check();
  for (const i of q.correct)
    await page.locator(".answer-option").nth(i).click();
  await page.getByRole("button", { name: "Check my answer" }).click();
  await page.locator(".concept-connections").waitFor();
  const evidenceHref = await page.locator(".source-details a").first().getAttribute("href");
  assert.ok(evidenceHref.startsWith("/new%20set/"));
  const evidence = await context.request.get(`${base}${evidenceHref}`);
  assert.equal(evidence.status(), 200, "new screenshot source link is broken");
  assert.ok(evidence.headers()["content-type"].startsWith("image/"));
  await page.locator(".mistake-note select").selectOption("services");
  assert.ok((await saved()).uncertain.includes(q.id));
  await page.locator(".concept-links a").first().click();
  await page.getByRole("heading", { name: "Your revision desk." }).waitFor();
  await page.getByRole("button", { name: /^Resume/ }).click();
  await page.getByRole("button", { name: "Finish & review" }).click();
  await page.getByRole("button", { name: /Submit & see results/ }).click();
  await page
    .getByRole("heading", { name: "Look at you, making progress." })
    .waitFor();
  await navigate("review");
  await page.getByRole("button", { name: /Guessed \/ unsure/ }).click();
  assert.ok((await page.locator(".review-layout .library-item").count()) >= 1);
  await navigate("exams");
  await page.getByRole("button", { name: /Start full mock/ }).click();
  await page.locator(".question-prompt").waitFor();
  const exam = (await saved()).activeSession;
  assert.equal(exam.questionIds.length, 65);
  assert.equal(
    await page.locator(".explanation, .concept-connections").count(),
    0,
    "exam leaked explanations",
  );
  await page.getByLabel(/Guessed \/ unsure/).check();
  await page.reload();
  assert.equal((await saved()).activeSession.deadline, exam.deadline);
  await page.getByRole("button", { name: /^Resume/ }).click();
  assert.equal(
    await page.locator(".explanation, .concept-connections").count(),
    0,
  );
  await page.getByRole("button", { name: "Finish & review" }).click();
  await page.getByRole("button", { name: /Submit & see results/ }).click();
  await page
    .getByRole("heading", { name: "Look at you, making progress." })
    .waitFor();
  const final = await saved();
  assert.ok(final.bookmarks.includes(old.bookmarks[0]));
  assert.equal(final.examDate, old.examDate);
  assert.equal(final.attempts.length, 66);
  assert.ok(Object.keys(final.recall).length === 1);
  assert.equal(final.mistakes[q.id], "services");
  await page.setViewportSize({ width: 390, height: 844 });
  await navigate("revision/rds/compare");
  await page
    .getByRole("heading", {
      name: "RDS and Aurora: availability vs reads",
      exact: true,
    })
    .waitFor();
  await noOverflow();
  if (artifacts)
    await page.screenshot({
      path: join(artifacts, "revision-mobile.png"),
      fullPage: true,
      animations: "disabled",
    });
  await page.getByRole("button", { name: /^Quick recall/ }).click();
  await page.getByRole("button", { name: /Reveal & check/ }).click();
  await noOverflow();
  await navigate("revision/rds/last-lap");
  await page
    .getByRole("heading", { name: "Requirements first. Tradeoffs second." })
    .waitFor();
  await noOverflow();
  assert.deepEqual(errors, []);
  console.log(
    "UI passed: desktop/mobile revision, multiword search, recall persistence, print, new-question practice, uncertainty review, old progress, and mock deadline/explanation boundaries.",
  );
} finally {
  await browser.close();
  server?.kill();
}
