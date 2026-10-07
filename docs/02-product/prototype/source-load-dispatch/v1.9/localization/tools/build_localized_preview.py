"""Build a separate language-switching study from the exact v1.9 source."""
from __future__ import annotations

import hashlib
import json
import argparse
from pathlib import Path

ROOT = Path(__file__).parent

JS = r"""
<script id="localeStudyRuntime">
(() => {
  const localeNames = {"zh-Hant":"繁體中文介面語言","en":"Interface language","pt":"Idioma da interface"};
  const documentTitles = {
    "zh-Hant":"Macau Energy OS — 調度流程研究 v1.9",
    "en":"Macau Energy OS — Dispatch workflow study v1.9",
    "pt":"Macau Energy OS — Estudo do fluxo de despacho v1.9"
  };
  const reviewCopy = {
    "zh-Hant":"翻譯研究稿 · 待澳門語言及能源領域審閱",
    "en":"Translation study · pending Macau language and energy-domain review",
    "pt":"Estudo de tradução · aguarda revisão linguística e energética de Macau"
  };
  const messages = __MESSAGES__;
  const svgMessages = __SVG_MESSAGES__;
  const select = document.getElementById("localeStudySelect");
  const label = document.getElementById("localeStudyLabel");
  const review = document.getElementById("localeStudyReview");
  const announce = document.getElementById("localeStudyAnnounce");
  const originalText = new WeakMap();
  const lastText = new WeakMap();
  const originalAttrs = new WeakMap();
  const lastAttrs = new WeakMap();
  let locale = "zh-Hant";

  const valueFor = (source, svgPlotText = false) => {
    if (source === null || source === undefined) return source;
    const entry = (svgPlotText ? svgMessages : messages)[source];
    return entry && entry[locale] ? entry[locale] : source;
  };
  const excluded = node => {
    const parent = node.parentElement;
    if (!parent) return true;
    if (parent.closest("script,style,code,pre,#localeStudySelect")) return true;
    const svg = parent.closest("svg");
    return !!svg && !parent.matches("title,desc,text,tspan");
  };
  function translateText(node) {
    if (excluded(node)) return;
    const now = node.nodeValue;
    let source = originalText.get(node);
    const last = lastText.get(node);
    if (source === undefined || now !== last) {
      source = now;
      originalText.set(node, source);
    }
    const leading = (source.match(/^\s*/) || [""])[0];
    const trailing = (source.match(/\s*$/) || [""])[0];
    const core = source.slice(leading.length, source.length - trailing.length || source.length);
    const translated = valueFor(core, node.parentElement.matches("text,tspan"));
    const result = leading + translated + trailing;
    if (node.nodeValue !== result) node.nodeValue = result;
    lastText.set(node, result);
  }
  function translateAttributes(element) {
    for (const attr of ["aria-label", "title", "placeholder", "data-label"]) {
      if (!element.hasAttribute(attr)) continue;
      let originals = originalAttrs.get(element);
      let applied = lastAttrs.get(element);
      if (!originals) { originals = {}; originalAttrs.set(element, originals); }
      if (!applied) { applied = {}; lastAttrs.set(element, applied); }
      const now = element.getAttribute(attr);
      if (originals[attr] === undefined || now !== applied[attr]) originals[attr] = now;
      const result = valueFor(originals[attr]);
      if (now !== result) element.setAttribute(attr, result);
      applied[attr] = result;
    }
  }
  function translateTree(root) {
    if (root.nodeType === Node.TEXT_NODE) { translateText(root); return; }
    if (root.nodeType === Node.ELEMENT_NODE) {
      translateAttributes(root);
      if (root.matches("script,style,code,pre,#localeStudySelect")) return;
      for (const element of root.querySelectorAll("*")) translateAttributes(element);
    }
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) translateText(walker.currentNode);
  }
  function localizePager() {
    const position = document.querySelector(".stage-position");
    if (!position) return;
    const current = document.querySelector(".flow-current .current-step-count")?.textContent.trim();
    const stageName = document.querySelector(".flow-current .current-step-label")?.textContent.trim();
    const total = document.querySelectorAll(".flow-step").length;
    if (!current || !stageName || !total) return;
    const currentIndex = current.split("/")[0].trim().padStart(2, "0");
    const totalLabel = String(total).padStart(2, "0");
    const token = locale + "|" + currentIndex + "|" + totalLabel + "|" + stageName;
    if (position.dataset.localeToken === token) return;
    const labelText = locale === "pt" ? "Etapa " + currentIndex + " de " + totalLabel + ": " :
      locale === "en" ? "Stage " + currentIndex + " of " + totalLabel + ": " : "第 " + currentIndex + " / " + totalLabel + " 階段：";
    const strong = document.createElement("strong");
    strong.textContent = stageName;
    position.replaceChildren(document.createTextNode(labelText), strong);
    position.dataset.localeToken = token;
  }
  function apply(nextLocale) {
    locale = nextLocale;
    select.value = locale;
    document.documentElement.lang = locale;
    document.title = documentTitles[locale];
    label.textContent = localeNames[locale];
    label.setAttribute("aria-label", localeNames[locale]);
    review.textContent = reviewCopy[locale];
    select.setAttribute("aria-label", localeNames[locale]);
    translateTree(document.body);
    localizePager();
    announce.textContent = locale === "zh-Hant" ? "已切換至繁體中文" : locale === "pt" ? "Idioma alterado para português" : "Language changed to English";
  }
  const observer = new MutationObserver(records => {
    for (const record of records) {
      if (record.type === "characterData") translateText(record.target);
      else {
        if (record.target.nodeType === Node.ELEMENT_NODE) translateAttributes(record.target);
        for (const node of record.addedNodes) translateTree(node);
      }
    }
    localizePager();
  });
  observer.observe(document.body, {subtree:true, childList:true, characterData:true, attributes:true, attributeFilter:["aria-label","title","placeholder"]});
  select.addEventListener("change", () => apply(select.value));
  const requested = new URLSearchParams(location.search).get("locale");
  apply(Object.prototype.hasOwnProperty.call(localeNames, requested) ? requested : "zh-Hant");
})();
</script>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "index.html", help="Pinned source prototype HTML")
    parser.add_argument("--catalog", type=Path, default=ROOT / "locale-catalog-draft-full-workflow-v0.3.json", help="Full-workflow draft locale catalog")
    parser.add_argument("--output", type=Path, default=ROOT / "localized-preview-v0.1.html", help="Generated standalone study page")
    args = parser.parse_args()
    source_path, catalog_path, output_path = args.source.resolve(), args.catalog.resolve(), args.output.resolve()
    source = source_path.read_bytes()
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    source_sha = hashlib.sha1(b"blob " + str(len(source)).encode("ascii") + b"\0" + source).hexdigest()
    expected = catalog["source"]["blob"]
    if source_sha != expected:
        raise SystemExit(f"Pinned HTML mismatch: expected {expected}, got {source_sha}")
    messages = {}
    svg_messages = {}
    conflicts = []
    for message in catalog["messages"]:
        source_text = message["sourceText"]
        translated = message["translations"]
        pair = {"en": translated.get("en"), "pt": translated.get("pt")}
        target = svg_messages if message.get("channel") == "svg-text" else messages
        if source_text in target and target[source_text] != pair:
            conflicts.append(source_text)
        target[source_text] = pair
    if conflicts:
        raise SystemExit(f"Context-dependent duplicate text requires a scoped renderer: {len(conflicts)} collisions")

    html = source_path.read_text(encoding="utf-8")
    control = '''<span class="locale-study-control"><label id="localeStudyLabel" for="localeStudySelect">介面語言</label><select class="select" id="localeStudySelect" aria-label="介面語言"><option value="zh-Hant" lang="zh-Hant">繁體中文 · 原文</option><option value="pt" lang="pt">Português · rascunho</option><option value="en" lang="en">English · draft</option></select><span id="localeStudyReview" class="locale-study-review">翻譯研究稿 · 待澳門語言及能源領域審閱</span></span>'''
    anchor = '<div class="topright"><span class="badge">'
    if html.count(anchor) != 1:
        raise SystemExit("Could not locate unique top-right locale control anchor")
    html = html.replace(anchor, '<div class="topright">' + control + '<span class="badge">', 1)
    css = '''\n.locale-study-control{display:grid;grid-template-columns:auto minmax(150px,auto);align-items:center;gap:4px 8px;font-size:11px;color:var(--muted)}.locale-study-control label{font-weight:650}.locale-study-control select{min-height:40px;padding:7px 10px}.locale-study-review{grid-column:1/-1;max-width:310px;font-size:10px;line-height:1.35;color:#80551b}.topright{flex-wrap:wrap}@media(max-width:900px){.content{grid-template-columns:minmax(0,1fr)}.plot .plotlabel{display:none}}@media(max-width:760px){.locale-study-control{grid-template-columns:auto minmax(150px,1fr)}.locale-study-review{max-width:none}.controls>*{min-width:0;max-width:100%}}@media(max-width:430px){.canvashead{align-items:flex-start;flex-direction:column;gap:8px}.canvashead .small{text-align:left;max-width:none}}@media(max-width:390px){.railnav{gap:9px}.railnav button .rail-label,.railnav button:hover .rail-label,.railnav button:focus-visible .rail-label{max-width:46px;white-space:normal;overflow-wrap:normal;text-align:center;font-size:10px;line-height:1.05}}@media(max-width:360px){.frame{grid-template-columns:minmax(0,1fr);min-width:0}.rail,.main{min-width:0}.topright{width:100%;min-width:0}.locale-study-control{width:100%;min-width:0;grid-template-columns:minmax(0,1fr)}.locale-study-control select{width:100%;min-width:0;max-width:100%}.locale-study-review{grid-column:1}.railnav button .rail-label,.railnav button:hover .rail-label,.railnav button:focus-visible .rail-label{max-width:46px;white-space:normal;overflow-wrap:normal;text-align:center;font-size:9px;line-height:1.05}}\n'''
    style_end = html.rfind("</style>")
    if style_end < 0:
        raise SystemExit("Could not locate a style block for study-specific responsive rules")
    html = html[:style_end] + css + html[style_end:]
    html = html.replace("</body>", '<span class="sr" id="localeStudyAnnounce" aria-live="polite"></span>\n' + JS.replace("__MESSAGES__", json.dumps(messages, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")).replace("__SVG_MESSAGES__", json.dumps(svg_messages, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")) + "\n</body>", 1)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"Created {output_path}; source blob {source_sha}; mapped unique strings {len(messages)}; contexts {len(catalog['messages'])}.")


if __name__ == "__main__":
    main()
