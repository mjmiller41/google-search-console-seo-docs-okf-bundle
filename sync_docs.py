#!/usr/bin/env python3
"""Sync this OKF bundle with the live Google Search Central documentation.

Re-discovers every page in the site's left navigation (``nav.devsite-book-nav``),
fetches each one, rebuilds it as an OKF v0.2 concept, and writes only the
concepts whose content actually changed. Pages that disappear from the
navigation are marked ``status: deprecated`` rather than deleted, per OKF v0.2
§5.4. Finishes by running the maintenance chain (validate, index, log, viz).

Usage:
    python3 sync_docs.py                 # sync the bundle in place
    python3 sync_docs.py --check         # report drift, write nothing (exit 2 if drift)
    python3 sync_docs.py --force         # rewrite every concept
    python3 sync_docs.py --only /search/docs/appearance/structured-data/recipe

Requires: beautifulsoup4, PyYAML, and pandoc on PATH. See requirements.txt.
"""
from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

try:
    import bs4
    import yaml
    from bs4 import BeautifulSoup, Comment
except ImportError as exc:  # pragma: no cover
    sys.exit(f"Missing dependency: {exc}. Install with: pip install -r requirements.txt")

# Change detection compares rendered concepts byte for byte, so the parse must
# be reproducible. beautifulsoup4 < 4.15 mishandles void elements in
# html.parser (a <textarea> after an <input> is nested *inside* it), which
# alters the HTML that complex tables pass through verbatim and would make
# every sync report phantom updates.
if tuple(int(p) for p in bs4.__version__.split(".")[:2]) < (4, 15):
    sys.exit(
        f"beautifulsoup4 >= 4.15 required for reproducible output "
        f"(found {bs4.__version__}). Upgrade with: pip install -r requirements.txt"
    )

BASE = "https://developers.google.com"
ROOT_DOC = "/search/docs"
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
GENERATOR = "okf-sync/1.0"
VERIFIER = "process:google-docs-sync"
ARTICLE_SELECTOR = "div.devsite-article-body"

# Elements removed outright: chrome, telemetry, and interactive widgets.
DROP_SELECTORS = [
    "script", "style", "svg", "button", "template", "noscript",
    "devsite-feedback", "devsite-thumb-rating", "devsite-page-rating",
    "devsite-toc", "devsite-hats-survey", ".nocontent", ".devsite-banner",
]
# Layout wrappers unwrapped so pandoc emits markdown instead of raw HTML.
UNWRAP_TAGS = ("section", "article", "span", "header", "footer", "nav", "hgroup", "main")
# Attributes kept per tag; everything else is presentation noise.
KEEP_ATTRS = {
    "a": {"href"},
    "img": {"src", "alt", "title"},
    "pre": {"class"},
    "code": {"class"},
    "td": {"colspan", "rowspan"},
    "th": {"colspan", "rowspan"},
}
# Cells holding these need real HTML; pandoc would flatten them into a lossy
# single-column pipe table, so such tables pass through verbatim.
BLOCK_IN_CELL = ["p", "ul", "ol", "pre", "blockquote", "table", "h1", "h2", "h3", "h4", "img"]

VOID_ELEMENTS = ("area", "base", "br", "col", "embed", "hr", "img", "input",
                 "link", "meta", "param", "source", "track", "wbr")
VOID_CLOSE_RE = re.compile(r"</(?:%s)\s*>" % "|".join(VOID_ELEMENTS), re.I)
VOID_OPEN_RE = re.compile(
    r"<((?:%s))\b((?:[^>\"']|\"[^\"]*\"|'[^']*')*?)\s*/?>" % "|".join(VOID_ELEMENTS), re.I
)

FOOTNOTE_RE = re.compile(r"\[\^([A-Za-z0-9_\-]+)\]")
LAST_UPDATED_RE = re.compile(r"Last updated (\d{4}-\d{2}-\d{2}) UTC")
RETRIEVED_RE = re.compile(r"Retrieved \d{4}-\d{2}-\d{2}\.")
GENERATED_AT_RE = re.compile(r"^(\s*at: ).*$", re.M)


# --------------------------------------------------------------------------
# Fetching
# --------------------------------------------------------------------------

def fetch(url: str, retries: int = 3, timeout: int = 30) -> str:
    """GET a URL as text, retrying transient failures with backoff."""
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = Request(url, headers={"User-Agent": USER_AGENT})
            with urlopen(request, timeout=timeout) as response:
                return response.read().decode("utf-8", errors="replace")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = exc
            if isinstance(exc, HTTPError) and exc.code in (404, 410):
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def discover_pages(nav_html: str) -> list[str]:
    """Return every documentation path linked from nav.devsite-book-nav."""
    match = re.search(r'<nav class="devsite-book-nav[^"]*".*?</nav>', nav_html, re.S)
    if not match:
        raise RuntimeError(
            "Could not locate nav.devsite-book-nav; the site layout may have changed."
        )
    pages: list[str] = []
    for href in re.findall(r'href="([^"]+)"', match.group(0)):
        if href.startswith(BASE):
            href = href[len(BASE):]
        if not href.startswith("/"):
            continue
        path = href.split("#")[0].split("?")[0].rstrip("/")
        if not (path.startswith("/search/docs") or path.startswith("/crawling/docs")):
            continue
        if path and path not in pages:
            pages.append(path)
    if not pages:
        raise RuntimeError("Navigation parsed but yielded no documentation pages.")
    return pages


# --------------------------------------------------------------------------
# URL / path mapping
# --------------------------------------------------------------------------

def concept_path_for(url: str, page_set: set[str]) -> str:
    """Map a devsite URL to its bundle-relative concept path.

    A page that is also the parent of other pages becomes ``<dir>/overview.md``
    so it can coexist with its children in the directory tree.
    """
    if url == ROOT_DOC:
        return "overview.md"
    if url.startswith("/crawling/docs/"):
        rest = "crawling-indexing/" + url[len("/crawling/docs/"):]
    else:
        rest = url[len("/search/docs/"):]
    if any(other != url and other.startswith(url + "/") for other in page_set):
        return f"{rest}/overview.md"
    return f"{rest}.md"


def source_id_for(url: str) -> str:
    return f"google-{url.rstrip('/').split('/')[-1]}"[:60]


def internal_target(href: str, page_url: str, page_set: set[str]) -> str | None:
    """Return the devsite path if href resolves to a page we mirror, else None."""
    if href.startswith("#"):
        return None
    absolute = urljoin(f"{BASE}{page_url}/", href)
    parsed = urlparse(absolute)
    if parsed.netloc not in ("developers.google.com", ""):
        return None
    path = parsed.path.rstrip("/")
    return path if path in page_set else None


# --------------------------------------------------------------------------
# HTML -> Markdown
# --------------------------------------------------------------------------

def clean_body(body, page_url: str, concept_paths: dict[str, str]):
    page_set = set(concept_paths)
    for selector in DROP_SELECTORS:
        for element in body.select(selector):
            element.decompose()
    for comment in body.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()
    # The article carries its own h1; the concept renders the title itself.
    if body.find("h1"):
        body.find("h1").decompose()
    for aside in body.find_all("aside"):
        aside.name = "blockquote"
    for link in body.find_all("a", href=True):
        target = internal_target(link["href"], page_url, page_set)
        link["href"] = (
            "/" + concept_paths[target] if target
            else urljoin(f"{BASE}{page_url}/", link["href"])
        )
    for tag in UNWRAP_TAGS:
        for element in body.find_all(tag):
            element.unwrap()
    # Custom elements (<devsite-code> and friends) hide their contents from
    # pandoc, which silently drops them.
    for element in body.find_all(lambda t: "-" in t.name):
        element.unwrap()
    while body.find("div"):
        body.find("div").unwrap()
    for image in body.find_all("img"):
        src = image.get("src") or image.get("data-src")
        if not src:
            image.decompose()
            continue
        image["src"] = urljoin(f"{BASE}/", src)
    for element in body.find_all(True):
        allowed = KEEP_ATTRS.get(element.name, set())
        for attribute in list(element.attrs):
            if attribute not in allowed:
                del element[attribute]
    return body


def html_to_markdown(html: str) -> str:
    result = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=html.encode("utf-8"), capture_output=True, check=True,
    )
    return re.sub(r"\n{3,}", "\n\n", result.stdout.decode("utf-8")).strip()


def needs_html_passthrough(table) -> bool:
    """Whether a table must be carried through as HTML rather than converted.

    Two kinds cannot survive as a GitHub-flavored pipe table: cells holding
    block content, and merged cells. Pandoc's handling of the latter changed
    between releases (3.1 flattens a colspan header into an empty extra
    column; 3.7 emits HTML), so deciding here keeps output identical across
    pandoc versions instead of inheriting whichever policy is installed.
    """
    if table.find(BLOCK_IN_CELL):
        return True
    return any(
        cell.has_attr("colspan") or cell.has_attr("rowspan")
        for cell in table.find_all(["td", "th"])
    )


def canonical_html(markup: str) -> str:
    """Write void elements one fixed way, so serialization changes in a future
    beautifulsoup release cannot rewrite passthrough tables on their own."""
    return VOID_OPEN_RE.sub(r"<\1\2/>", VOID_CLOSE_RE.sub("", markup))


def render_body(soup, body, page_url: str, concept_paths: dict[str, str]) -> str:
    body = clean_body(body, page_url, concept_paths)
    passthrough: list[tuple[str, str]] = []
    for table in body.find_all("table"):
        if needs_html_passthrough(table):
            token = f"OKFTABLE{len(passthrough)}TOKEN"
            passthrough.append((token, canonical_html(str(table))))
            table.replace_with(soup.new_string(f"\n\n{token}\n\n"))
    markdown = html_to_markdown(body.decode_contents())
    for token, table_html in passthrough:
        markdown = markdown.replace(token, table_html)
    return markdown


# --------------------------------------------------------------------------
# Concept assembly
# --------------------------------------------------------------------------

def build_concept(page_url: str, html: str, concept_paths: dict[str, str],
                  now: str, today: str) -> tuple[str, str, str | None]:
    """Return (concept_path, document_text, google_last_updated)."""
    soup = BeautifulSoup(html, "html.parser")
    body = soup.select_one(ARTICLE_SELECTOR)
    if body is None:
        raise RuntimeError(f"No {ARTICLE_SELECTOR} found for {page_url}")

    heading = soup.select_one("h1.devsite-page-title") or soup.find("h1")
    # Join text nodes without stripping each one, so spaces around inline
    # <code> in a heading survive ("Block Search indexing with noindex").
    title = (re.sub(r"\s+", " ", heading.get_text()).strip() if heading
             else page_url.rsplit("/", 1)[-1].replace("-", " ").title())

    meta = soup.find("meta", attrs={"name": "description"})
    description = (meta["content"].strip() if meta and meta.get("content")
                   else f"Google Search Central documentation page: {title}.")

    updated_match = LAST_UPDATED_RE.search(html)
    last_updated = updated_match.group(1) if updated_match else None

    content = render_body(soup, body, page_url, concept_paths)
    url = f"{BASE}{page_url}"
    source_id = source_id_for(page_url)

    # Documentation prose can contain "[^...]" inside examples; neutralize any
    # token that is not our real footnote so validation stays clean.
    for stray in {f for f in FOOTNOTE_RE.findall(content) if f != source_id}:
        content = content.replace(f"[^{stray}]", f"[ ^{stray}]")

    concept_path = concept_paths[page_url]
    category = concept_path.split("/")[0].removesuffix(".md")
    tags = ["google-search", "documentation"]
    if category and category != "overview":
        tags.append(category)

    source: dict[str, object] = {
        "id": source_id,
        "resource": url,
        "title": title,
        "author": "Google Search Central (Google LLC)",
    }
    if last_updated:
        source["last_modified"] = f"{last_updated}T00:00:00Z"

    frontmatter = {
        "type": "Reference",
        "title": title,
        "description": description,
        "resource": url,
        "tags": tags,
        "status": "stable",
        "generated": {"by": GENERATOR, "at": now},
        "sources": [source],
    }
    frontmatter_text = yaml.safe_dump(
        frontmatter, sort_keys=False, allow_unicode=True, width=1000
    ).rstrip()

    year = (last_updated or today)[:4]
    attribution = (
        f"> Mirrored from the official Google Search Central documentation at "
        f"[{url}]({url}). Page content, including any embedded figures, is authored by "
        f"Google and was last updated by Google on {last_updated or 'n.d.'}.[^{source_id}]"
    )
    references = (
        "# References & Citations\n\n"
        f'[^{source_id}]: Google Search Central ({year}). "{title}". '
        f"*Google for Developers*. {url}. Retrieved {today}."
    )
    document = (
        f"---\n{frontmatter_text}\n---\n\n# {title}\n\n{attribution}\n\n"
        f"{content}\n\n{references}\n"
    )
    return concept_path, document, last_updated


def comparable(document: str) -> str:
    """Strip the fields that move on every run so diffs reflect real changes."""
    text = GENERATED_AT_RE.sub(r"\1<normalized>", document, count=1)
    return RETRIEVED_RE.sub("Retrieved <normalized>.", text)


def preserve_generated_at(new_document: str, old_document: str) -> str:
    """Carry the previous generated.at forward when content is unchanged."""
    old_match = GENERATED_AT_RE.search(old_document)
    if not old_match:
        return new_document
    return GENERATED_AT_RE.sub(old_match.group(0), new_document, count=1)


def record_verification(path: Path, timestamp: str) -> None:
    """Stamp a machine verification event, replacing this process's prior one."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return
    _, frontmatter_text, body = text.split("---\n", 2)
    frontmatter = yaml.safe_load(frontmatter_text) or {}
    existing = frontmatter.get("verified")
    events = [existing] if isinstance(existing, dict) else list(existing or [])
    events = [e for e in events if isinstance(e, dict) and e.get("by") != VERIFIER]
    events.append({"by": VERIFIER, "at": timestamp})
    # Keep `verified` next to `generated`, matching the documented field order.
    ordered: dict[str, object] = {}
    for key, value in frontmatter.items():
        if key == "verified":
            continue
        ordered[key] = value
        if key == "generated":
            ordered["verified"] = events
    if "verified" not in ordered:
        ordered["verified"] = events
    rendered = yaml.safe_dump(ordered, sort_keys=False, allow_unicode=True, width=1000).rstrip()
    path.write_text(f"---\n{rendered}\n---\n{body}", encoding="utf-8")


def is_mirrored_concept(path: Path) -> bool:
    """Whether a file is a concept this sync produced, as opposed to repo docs
    such as README.md that happen to be markdown."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    if not text.startswith("---\n"):
        return False
    try:
        frontmatter = yaml.safe_load(text.split("---\n", 2)[1]) or {}
    except yaml.YAMLError:
        return False
    return str(frontmatter.get("resource", "")).startswith(BASE)


def deprecate(path: Path, timestamp: str) -> bool:
    """Mark a concept deprecated; returns False if it already was."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False
    _, frontmatter_text, body = text.split("---\n", 2)
    frontmatter = yaml.safe_load(frontmatter_text) or {}
    if frontmatter.get("status") == "deprecated":
        return False
    frontmatter["status"] = "deprecated"
    frontmatter["deprecated_at"] = timestamp
    frontmatter["deprecation_reason"] = (
        "Page is no longer listed in the Google Search Central navigation."
    )
    rendered = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=1000).rstrip()
    path.write_text(f"---\n{rendered}\n---\n{body}", encoding="utf-8")
    return True


# --------------------------------------------------------------------------
# Maintenance chain
# --------------------------------------------------------------------------

def okf_command() -> list[str] | None:
    """Locate the okf CLI: $OKF_CLI, then PATH, then an importable module."""
    override = os.environ.get("OKF_CLI")
    if override:
        return shlex.split(override)
    if shutil.which("okf"):
        return ["okf"]
    probe = subprocess.run(
        [sys.executable, "-m", "okf_cli.cli", "--help"], capture_output=True
    )
    return [sys.executable, "-m", "okf_cli.cli"] if probe.returncode == 0 else None


def run_maintenance(bundle: Path, summary: str) -> bool:
    """Run validate/index/log/viz. Returns False if validation fails."""
    okf = okf_command()
    if okf is None:
        print("\nokf CLI not found; skipping maintenance chain.")
        print("  Install it from https://github.com/mjmiller41/cli-agent-okf (or set")
        print("  OKF_CLI to the command that runs it), then run:")
        print(f"    okf validate --bundle {bundle} --strict && okf index --bundle {bundle}")
        return True

    steps = [
        (["validate", "--bundle", str(bundle), "--strict"], "validate"),
        (["index", "--bundle", str(bundle)], "index"),
        (["log", "Update", summary, "--bundle", str(bundle)], "log"),
        (["viz", "--bundle", str(bundle)], "viz"),
    ]
    for args, label in steps:
        print(f"\n$ okf {label}")
        result = subprocess.run(okf + args, capture_output=True, text=True)
        output = (result.stdout + result.stderr).strip()
        print("\n".join(output.splitlines()[-6:]) if output else "(no output)")
        if result.returncode != 0:
            print(f"\nokf {label} failed (exit {result.returncode}).")
            return False
    return True


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync the OKF bundle with live Google Search Central docs."
    )
    parser.add_argument("--bundle", type=Path, default=Path(__file__).resolve().parent,
                        help="Bundle root (default: this script's directory).")
    parser.add_argument("--check", action="store_true",
                        help="Report drift without writing; exit 2 if updates exist.")
    parser.add_argument("--force", action="store_true",
                        help="Rewrite every concept even when unchanged.")
    parser.add_argument("--only", nargs="+", metavar="PATH",
                        help="Limit the sync to these devsite paths.")
    parser.add_argument("--jobs", type=int, default=4,
                        help="Parallel fetches (default: 4).")
    parser.add_argument("--record-verification", action="store_true",
                        help="Stamp unchanged concepts with a machine verification event.")
    parser.add_argument("--no-maintenance", action="store_true",
                        help="Skip the validate/index/log/viz chain.")
    args = parser.parse_args()

    bundle: Path = args.bundle.resolve()
    if not bundle.is_dir():
        print(f"Bundle directory not found: {bundle}", file=sys.stderr)
        return 1
    if shutil.which("pandoc") is None:
        print("pandoc not found on PATH; install it to convert documentation HTML.",
              file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    today = now[:10]

    print(f"Discovering pages from {BASE}{ROOT_DOC} ...")
    try:
        pages = discover_pages(fetch(f"{BASE}{ROOT_DOC}"))
    except Exception as exc:
        print(f"Navigation discovery failed: {exc}", file=sys.stderr)
        return 1

    concept_paths = {page: concept_path_for(page, set(pages)) for page in pages}
    collisions = len(pages) - len(set(concept_paths.values()))
    if collisions:
        print(f"{collisions} concept path collision(s) in the navigation.", file=sys.stderr)
        return 1
    print(f"Found {len(pages)} pages in the navigation.")

    targets = pages
    if args.only:
        wanted = {p.rstrip("/") for p in args.only}
        targets = [p for p in pages if p in wanted]
        missing = wanted - set(targets)
        if missing:
            print(f"Not in navigation: {', '.join(sorted(missing))}", file=sys.stderr)
        if not targets:
            return 1

    print(f"Fetching {len(targets)} page(s) with {args.jobs} worker(s) ...")

    def load(page: str) -> tuple[str, str | None, str | None]:
        try:
            return page, fetch(f"{BASE}{page}"), None
        except Exception as exc:
            return page, None, str(exc)

    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        fetched = list(pool.map(load, targets))

    added: list[str] = []
    updated: list[str] = []
    unchanged: list[Path] = []
    failed: list[tuple[str, str]] = []

    for page, html, error in fetched:
        if error or html is None:
            failed.append((page, error or "unknown error"))
            print(f"  FAIL    {page}: {error}")
            continue
        try:
            concept_path, document, _ = build_concept(
                page, html, concept_paths, now, today
            )
        except Exception as exc:
            failed.append((page, str(exc)))
            print(f"  FAIL    {page}: {exc}")
            continue

        destination = bundle / concept_path
        if not destination.exists():
            if not args.check:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(document, encoding="utf-8")
            added.append(concept_path)
            print(f"  ADD     {concept_path}")
            continue

        current = destination.read_text(encoding="utf-8")
        if not args.force and comparable(current) == comparable(document):
            unchanged.append(destination)
            continue

        if not args.check:
            if args.force and comparable(current) == comparable(document):
                document = preserve_generated_at(document, current)
            destination.write_text(document, encoding="utf-8")
        updated.append(concept_path)
        print(f"  UPDATE  {concept_path}")

    # Concepts whose upstream page left the navigation.
    deprecated: list[str] = []
    if not args.only:
        live = set(concept_paths.values())
        for existing in sorted(bundle.rglob("*.md")):
            relative = existing.relative_to(bundle).as_posix()
            if existing.name in ("index.md", "log.md") or relative in live:
                continue
            if not is_mirrored_concept(existing):
                continue  # repo documentation, not a mirrored page
            if args.check:
                # Already-deprecated concepts are settled, not outstanding drift.
                frontmatter = yaml.safe_load(
                    existing.read_text(encoding="utf-8").split("---\n", 2)[1]
                ) or {}
                if frontmatter.get("status") == "deprecated":
                    continue
                deprecated.append(relative)
                print(f"  GONE    {relative}")
            elif deprecate(existing, now):
                deprecated.append(relative)
                print(f"  DEPRECATE {relative}")

    if args.record_verification and not args.check:
        for path in unchanged:
            record_verification(path, now)

    print(
        f"\n{len(added)} added, {len(updated)} updated, {len(unchanged)} unchanged, "
        f"{len(deprecated)} deprecated, {len(failed)} failed"
    )
    if failed:
        print("\nFailures:")
        for page, error in failed:
            print(f"  {page}: {error}")

    if args.check:
        drift = len(added) + len(updated) + len(deprecated)
        print("\nBundle is up to date." if not drift else f"\n{drift} page(s) need syncing.")
        return 2 if drift else 0

    changed = len(added) + len(updated) + len(deprecated)
    if not changed and not args.record_verification and not args.force:
        print("\nBundle already up to date; skipping maintenance chain.")
        return 1 if failed else 0

    if not args.no_maintenance:
        parts = []
        if added:
            parts.append(f"added {len(added)} concept(s)")
        if updated:
            parts.append(f"refreshed {len(updated)} concept(s)")
        if deprecated:
            parts.append(f"deprecated {len(deprecated)} concept(s)")
        if args.record_verification:
            parts.append(f"verified {len(unchanged)} unchanged concept(s)")
        summary = (
            "Synced bundle against Google Search Central documentation: "
            + (", ".join(parts) if parts else "no content changes")
        )
        if not run_maintenance(bundle, summary):
            return 1

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
