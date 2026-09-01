#!/usr/bin/env python3
"""Extract the Search-relevant signals from an HTML page.

Works identically on a live response body and a local build-output file, so
the same checks run in live and static mode.

    python3 extract_signals.py FILE [--base-url URL]
    python3 extract_signals.py -            < page.html
    python3 fetch_page.py URL | python3 extract_signals.py --from-fetch -

Stdlib only. Never writes files. JSON on stdout.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from html.parser import HTMLParser

# Elements HTML permits inside <head>. Anything else ends the head early, so
# metadata after it can be missed. See crawling-indexing/valid-page-metadata.md.
VALID_HEAD_ELEMENTS = {"title", "meta", "link", "script", "style", "base",
                       "noscript", "template", "head", "html"}
GENERIC_ANCHORS = {"click here", "here", "read more", "more", "link", "this",
                   "learn more", "this page", "continue"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}
APP_SHELL_IDS = {"root", "__next", "app", "__nuxt", "svelte"}


class SignalParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_head = False
        self.head_done = False
        self.stack: list[str] = []
        self.title_parts: list[str] = []
        self.in_title = False
        self.metas: list[dict] = []
        self.links: list[dict] = []
        self.anchors: list[dict] = []
        self.images: list[dict] = []
        self.scripts: list[dict] = []
        self.jsonld_raw: list[str] = []
        self.in_jsonld = False
        self.jsonld_buf: list[str] = []
        self.microdata: list[str] = []
        self.text_parts: list[str] = []
        self.in_skipped_text = 0
        self.invalid_head_elements: list[str] = []
        self.metadata_after_invalid = False
        self.script_bytes = 0
        self.style_bytes = 0
        self.in_style = False
        self.in_script = False
        self.app_shell_containers: list[dict] = []
        self.open_container: dict | None = None
        self.html_lang: str | None = None
        self.base_href: str | None = None
        self.current_anchor: dict | None = None
        self.anchor_text: list[str] = []
        self.inline_styles: list[str] = []

    # -- helpers ---------------------------------------------------------
    @staticmethod
    def _attrs(attrs) -> dict:
        return {k.lower(): (v or "") for k, v in attrs}

    def handle_starttag(self, tag, attrs):  # noqa: C901
        tag = tag.lower()
        a = self._attrs(attrs)
        if tag not in VOID:
            self.stack.append(tag)

        if tag == "html":
            self.html_lang = a.get("lang")
        elif tag == "head":
            self.in_head = True
        elif tag == "body":
            self.in_head = False
            self.head_done = True

        if self.in_head and not self.head_done:
            if tag not in VALID_HEAD_ELEMENTS:
                if tag not in self.invalid_head_elements:
                    self.invalid_head_elements.append(tag)
            elif self.invalid_head_elements and tag in ("meta", "link", "title"):
                self.metadata_after_invalid = True

        if a.get("style"):
            self.inline_styles.append(a["style"])

        if tag == "title" and not self.head_done and not self.title_parts:
            # Only the document title; SVG icons carry <title> elements too.
            self.in_title = True
        elif tag == "base" and a.get("href"):
            self.base_href = a["href"]
        elif tag == "meta":
            self.metas.append(a)
        elif tag == "link":
            self.links.append(a)
        elif tag == "a":
            self.current_anchor = a
            self.anchor_text = []
        elif tag == "img":
            self.images.append(a)
        elif tag == "script":
            self.in_script = True
            self.scripts.append(a)
            if a.get("type", "").lower() == "application/ld+json":
                self.in_jsonld = True
                self.jsonld_buf = []
        elif tag == "style":
            self.in_style = True
        elif tag in ("noscript", "template"):
            self.in_skipped_text += 1

        if a.get("itemtype"):
            self.microdata.append(a["itemtype"])

        if a.get("id", "").lower() in APP_SHELL_IDS:
            self.open_container = {"id": a["id"], "depth": len(self.stack), "text": 0}

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
        elif tag == "head":
            self.in_head = False
            self.head_done = True
        elif tag == "script":
            self.in_script = False
            if self.in_jsonld:
                self.jsonld_raw.append("".join(self.jsonld_buf))
                self.in_jsonld = False
        elif tag == "style":
            self.in_style = False
        elif tag in ("noscript", "template"):
            self.in_skipped_text = max(0, self.in_skipped_text - 1)
        elif tag == "a" and self.current_anchor is not None:
            self.current_anchor["_text"] = "".join(self.anchor_text).strip()
            self.anchors.append(self.current_anchor)
            self.current_anchor = None

        while self.stack and tag in self.stack:
            popped = self.stack.pop()
            if popped == tag:
                break
        if (self.open_container is not None
                and len(self.stack) < self.open_container["depth"]):
            self.app_shell_containers.append(self.open_container)
            self.open_container = None

    def handle_data(self, data):
        if self.in_jsonld:
            self.jsonld_buf.append(data)
            return
        if self.in_script:
            self.script_bytes += len(data)
            return
        if self.in_style:
            self.style_bytes += len(data)
            return
        if self.in_title:
            self.title_parts.append(data)
            return
        if self.in_skipped_text:
            return
        stripped = data.strip()
        if stripped:
            self.text_parts.append(stripped)
            if self.current_anchor is not None:
                self.anchor_text.append(data)
            if self.open_container is not None:
                self.open_container["text"] += len(stripped)


def _meta(metas: list[dict], name: str) -> str | None:
    for m in metas:
        if m.get("name", "").lower() == name:
            return m.get("content")
    return None


def _absolute(href: str, base: str | None) -> str:
    return urllib.parse.urljoin(base, href) if base else href


def analyze(html: str, base_url: str | None) -> dict:
    parser = SignalParser()
    try:
        parser.feed(html)
        parser.close()
    except Exception as exc:  # malformed HTML should not kill the audit
        return {"parse_error": str(exc)}

    base = parser.base_href or base_url
    metas = parser.metas

    canonical = next((_absolute(l["href"], base) for l in parser.links
                      if l.get("rel", "").lower() == "canonical" and l.get("href")), None)
    amphtml = next((_absolute(l["href"], base) for l in parser.links
                    if l.get("rel", "").lower() == "amphtml" and l.get("href")), None)
    hreflang = [{"lang": l.get("hreflang"), "href": _absolute(l.get("href", ""), base)}
                for l in parser.links
                if l.get("hreflang") and l.get("rel", "").lower() == "alternate"]
    favicons = [{"rel": l.get("rel"), "href": _absolute(l.get("href", ""), base),
                 "sizes": l.get("sizes"), "type": l.get("type")}
                for l in parser.links if "icon" in l.get("rel", "").lower()]

    jsonld = []
    for raw in parser.jsonld_raw:
        try:
            jsonld.append({"raw_ok": True, "parsed": json.loads(raw)})
        except json.JSONDecodeError as exc:
            jsonld.append({"raw_ok": False, "parse_error": str(exc),
                           "excerpt": raw.strip()[:200]})

    internal = external = nofollow = sponsored = ugc = empty_anchor = generic = 0
    non_crawlable = []
    host = urllib.parse.urlparse(base).netloc if base else None
    for a in parser.anchors:
        href = (a.get("href") or "").strip()
        rel = a.get("rel", "").lower()
        text = a.get("_text", "")
        if not href:
            non_crawlable.append({"href": href, "reason": "anchor without href"})
            continue
        low = href.lower()
        if low.startswith("javascript:") or low == "#":
            non_crawlable.append({"href": href[:120], "reason": "javascript: or empty fragment"})
            continue
        if low.startswith(("mailto:", "tel:")):
            continue
        absolute = _absolute(href, base)
        if host and urllib.parse.urlparse(absolute).netloc not in ("", host):
            external += 1
        else:
            internal += 1
        nofollow += "nofollow" in rel
        sponsored += "sponsored" in rel
        ugc += "ugc" in rel
        if not text:
            empty_anchor += 1
        elif text.lower() in GENERIC_ANCHORS:
            generic += 1

    missing_alt = sum(1 for i in parser.images if not i.get("alt", "").strip())
    lazy_native = sum(1 for i in parser.images if i.get("loading", "").lower() == "lazy")
    missing_dims = sum(1 for i in parser.images
                       if not (i.get("width") and i.get("height")))

    text = " ".join(parser.text_parts)
    shell = next((c for c in parser.app_shell_containers if c["text"] < 50), None)

    mixed = []
    if base and base.startswith("https://"):
        for collection, key in ((parser.images, "src"), (parser.scripts, "src"),
                                (parser.links, "href")):
            for item in collection:
                value = item.get(key, "")
                if value.startswith("http://"):
                    mixed.append(value[:160])

    meta_refresh = next((m.get("content") for m in metas
                         if m.get("http-equiv", "").lower() == "refresh"), None)

    return {
        "title": "".join(parser.title_parts).strip() or None,
        "title_length": len("".join(parser.title_parts).strip()),
        "meta_description": _meta(metas, "description"),
        "meta_robots": _meta(metas, "robots"),
        "meta_googlebot": _meta(metas, "googlebot"),
        "meta_keywords_present": _meta(metas, "keywords") is not None,
        "canonical": canonical,
        "amphtml": amphtml,
        "hreflang": hreflang,
        "viewport": _meta(metas, "viewport"),
        "lang_attr": parser.html_lang,
        "favicons": favicons,
        "og": {m.get("property"): m.get("content") for m in metas
               if m.get("property", "").startswith("og:")},
        "h1_count": html.lower().count("<h1"),
        "meta_refresh": meta_refresh,
        "jsonld": jsonld,
        "microdata_itemtypes": parser.microdata,
        "links": {
            "internal": internal, "external": external, "nofollow": nofollow,
            "sponsored": sponsored, "ugc": ugc,
            "non_crawlable": non_crawlable[:20],
            "non_crawlable_count": len(non_crawlable),
            "empty_anchor": empty_anchor, "generic_anchor": generic,
        },
        "images": {"count": len(parser.images), "missing_alt": missing_alt,
                   "lazy_native": lazy_native, "missing_dimensions": missing_dims},
        "head_validity": {
            "invalid_elements": parser.invalid_head_elements,
            "metadata_after_invalid": parser.metadata_after_invalid,
        },
        "text_chars": len(text),
        "text_excerpt": text[:1500],
        "script_bytes": parser.script_bytes,
        "style_bytes": parser.style_bytes,
        "app_shell_suspect": bool(shell) and len(text) < 200,
        "app_shell_container": shell["id"] if shell else None,
        "inline_style_hidden_hints": [s[:120] for s in parser.inline_styles
                                      if re.search(r"display\s*:\s*none|visibility\s*:\s*hidden"
                                                   r"|font-size\s*:\s*0|text-indent\s*:\s*-\d{4}",
                                                   s, re.I)][:10],
        "mixed_content_urls": mixed[:20],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", default="-",
                        help="HTML file path, or - for stdin")
    parser.add_argument("--base-url", default=None,
                        help="base URL for resolving relative links")
    parser.add_argument("--from-fetch", action="store_true",
                        help="input is fetch_page.py JSON; use its body and final_url")
    parser.add_argument("--json", action="store_true",
                        help="accepted for symmetry; output is always JSON")
    args = parser.parse_args()

    raw = sys.stdin.read() if args.source == "-" else open(
        args.source, encoding="utf-8", errors="replace").read()

    base = args.base_url
    if args.from_fetch:
        payload = json.loads(raw)
        if payload.get("error"):
            json.dump({"error": payload["error"]}, sys.stdout, indent=1)
            print()
            return 2
        raw = payload.get("body") or ""
        base = base or payload.get("final_url")

    result = analyze(raw, base)
    if args.source != "-":
        result["source_file"] = args.source
    json.dump(result, sys.stdout, indent=1, default=str)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
