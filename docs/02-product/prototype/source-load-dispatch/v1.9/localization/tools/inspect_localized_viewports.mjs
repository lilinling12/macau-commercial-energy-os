import { createRequire } from "node:module";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const previewPath = path.resolve(process.argv[2] ?? "work/locale-v19/localization-study-v0.3/index.html");
const outDir = path.resolve(process.argv[3] ?? "outputs/locale-preview-v0.3-viewports");
await fs.mkdir(outDir, { recursive: true });
const tempRoot = await fs.mkdtemp(path.join(outDir, ".playwright-"));
Object.defineProperty(os, "tmpdir", { value: () => tempRoot });
const browser = await chromium.launch({ channel: "msedge", headless: true });
const locales = ["zh-Hant", "en", "pt"];
const stages = ["evidence-check", "site-model", "dispatchComparison", "constraint-analysis", "shadow-review", "outcome-replay"];
const viewports = [
  { width: 320, height: 800 },
  { width: 375, height: 812 },
  { width: 768, height: 900 },
  { width: 1024, height: 900 },
  { width: 1440, height: 900 },
];
const rows = [];

for (const locale of locales) {
  for (const stage of stages) {
    for (const viewport of viewports) {
      const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
      const errors = [];
      page.on("pageerror", error => errors.push(String(error)));
      const url = `${pathToFileURL(previewPath).href}?locale=${locale}#${stage}`;
      await page.goto(url, { waitUntil: "load" });
      await page.evaluate(() => document.fonts.ready);
      await page.evaluate(stage => document.getElementById(stage)?.scrollIntoView({ block: "start" }), stage);
      await page.waitForTimeout(100);
      const measurement = await page.evaluate(({ stage, locale }) => {
        const section = document.getElementById(stage);
        const rect = section?.getBoundingClientRect();
        const horizontalScrollRegions = [...document.querySelectorAll(".flow-table,[role='region']")]
          .filter(el => el.scrollWidth > el.clientWidth + 1)
          .map(el => ({ label: el.getAttribute("aria-label") || el.innerText?.slice(0, 80), clientWidth: el.clientWidth, scrollWidth: el.scrollWidth }));
        return {
          locale,
          stage,
          viewport: `${innerWidth}x${innerHeight}`,
          document: `${document.documentElement.scrollWidth}x${document.documentElement.scrollHeight}`,
          pageOverflowX: document.documentElement.scrollWidth > innerWidth + 1,
          activeSectionWidth: rect ? Math.round(rect.width) : null,
          sectionOverflowX: rect ? rect.width > innerWidth + 1 : null,
          tableScrollRegions: horizontalScrollRegions,
          untranslatedSvgText: locale === "zh-Hant" ? [] : [...document.querySelectorAll("svg text,svg title,svg desc,svg tspan")]
            .map(el => el.textContent?.replace(/\s+/g, " ").trim())
            .filter(text => text && /[\u3400-\u9fff]/.test(text)),
          pager: document.querySelector(".flow-current")?.innerText?.replace(/\s+/g, " ").trim() ||
            document.querySelector(".stage-nav")?.innerText?.replace(/\s+/g, " ").trim() || null,
        };
      }, { stage, locale });
      rows.push({ ...measurement, pageErrors: errors });

      if ((stage === "dispatchComparison" && [320, 375, 768, 1440].includes(viewport.width)) ||
          (stage === "constraint-analysis" && [320, 375].includes(viewport.width))) {
        const name = `${stage}-${locale}-${viewport.width}x${viewport.height}.png`;
        await page.screenshot({ path: path.join(outDir, name), fullPage: false });
      }
      await page.close();
    }
  }
}

await browser.close();
await fs.rm(tempRoot, { recursive: true, force: true });
const report = { sampleCount: rows.length, locales, stages, viewports, rows };
await fs.writeFile(path.join(outDir, "measurements.json"), JSON.stringify(report, null, 2));
const problems = rows.filter(r => r.pageOverflowX || r.sectionOverflowX || r.pageErrors.length || r.untranslatedSvgText.length);
console.log(JSON.stringify({ sampleCount: rows.length, problems, screenshots: (await fs.readdir(outDir)).filter(name => name.endsWith(".png")) }, null, 2));

