#!/usr/bin/env python3
"""
Distribute Crowdin output into ReadMe's per-language branches.

Crowdin writes every language to ONE branch:
    translations/<crowdin-lang>/docs/<EnglishCategory>/...
ReadMe expects each language on its OWN branch:
    v1.0-<lang>:  docs/<TranslatedCategory>/...

English on v1.0 is the source of truth for WHICH pages exist. For each enabled
language the script builds a PR into v1.0-<lang> that:

  * writes every translated page from translations/<lang>/   (links localized)
  * adds an English fallback for pages that are new in English and not yet
    translated                                                 (english_fallback)
  * removes pages that no longer exist in English (deletes / renames), and
    ignores stale translation files for them                   (mirror_deletions)
  * copies _order.yaml menus from English, except the root
    docs/_order.yaml that holds the translated category name   (sync_order_files)
  * renames the category folder Marketers -> <translated name>
  * optionally auto-merges the PR                              (auto_merge)

Usage:
    python3 scripts/distribute_translations.py [--langs ja,fr] [--dry-run] [--no-pr] [--auto-merge]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
CONFIG = json.loads((ROOT / ".github" / "crowdin-readme.json").read_text(encoding="utf-8"))
WORK_BRANCH = "crowdin-sync/{target}"
ORDER = "_order.yaml"
TEXT_SUFFIXES = {".md", ".mdx"}


def sh(*args: str, cwd: Path | None = None, check: bool = True, capture: bool = False) -> str:
    res = subprocess.run(args, cwd=cwd, check=check, text=True,
                         stdout=subprocess.PIPE if capture else None,
                         stderr=subprocess.PIPE if capture else None)
    return (res.stdout or "").strip() if capture else ""


def log(msg: str) -> None:
    print(msg, flush=True)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(msg + "\n")


def opt(name: str, default):
    return CONFIG.get(name, default)


def files_under(root: Path) -> dict[str, Path]:
    if not root.is_dir():
        return {}
    return {p.relative_to(root).as_posix(): p for p in root.rglob("*") if p.is_file()}


def category_name(lang: str, worktree: Path) -> str:
    override = opt("category_names", {}).get(lang)
    if override and not lang.startswith("_"):
        return override
    order = worktree / "docs" / ORDER
    if order.exists():
        for line in order.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\s*-\s*['\"]?(.+?)['\"]?\s*$", line)
            if m:
                return m.group(1)
    return CONFIG["english_category"]


def link_rewriter(lang: str):
    """
    /marketers/docs/x                       -> /marketers/<lang>/docs/x
    /partners/reference/x                   -> /partners/<lang>/reference/x
    https://<site_domain>/marketers/docs/x  -> https://<site_domain>/marketers/<lang>/docs/x
    Anchors (#...) and query strings are kept. Already-localized links,
    same-project links (/docs/x) and external links are left alone.
    """
    slugs = "|".join(map(re.escape, CONFIG["cross_project_slugs"]))
    sections = "|".join(map(re.escape, opt("link_sections", ["docs"])))
    domains = "|".join(map(re.escape, opt("site_domains", [])))
    dom = rf"(?:https?://(?:{domains}))?" if domains else ""
    pat = re.compile(rf'(?P<pre>href="|href=\'|\]\()(?P<dom>{dom})(?P<proj>/(?:{slugs}))/(?P<sec>{sections})/')

    def rewrite(text: str) -> tuple[str, int]:
        return pat.subn(lambda m: f'{m["pre"]}{m["dom"]}{m["proj"]}/{lang}/{m["sec"]}/', text)
    return rewrite


def crowdin_dir_for(lang: str) -> Path | None:
    tdir = ROOT / CONFIG["translations_dir"]
    for code, mapped in CONFIG["languages"].items():
        if mapped == lang and (tdir / code / "docs").is_dir():
            return tdir / code / "docs" / CONFIG["english_category"]
    return None


def process_language(lang: str, args) -> dict:
    target = CONFIG["target_branch_pattern"].format(lang=lang)
    if sh("git", "ls-remote", "--heads", "origin", target, capture=True) == "":
        log(f"- `{lang}`: target branch `{target}` does not exist, skipped")
        return {"lang": lang, "status": "no-target-branch"}

    en_root = ROOT / "docs" / CONFIG["english_category"]
    en_files = files_under(en_root)
    tr_dir = crowdin_dir_for(lang)
    tr_files = files_under(tr_dir) if tr_dir else {}

    work = WORK_BRANCH.format(target=target)
    tmp = Path(tempfile.mkdtemp(prefix=f"wt-{lang}-"))
    sh("git", "fetch", "-q", "origin", target)
    sh("git", "worktree", "add", "-q", "-B", work, str(tmp), f"origin/{target}")
    try:
        cat = category_name(lang, tmp)
        lang_root = tmp / "docs" / cat
        lang_files = files_under(lang_root)
        rewrite = link_rewriter(lang)
        stats = {"translated": 0, "fallback": 0, "menus": 0, "deleted": 0, "stale_ignored": 0, "links": 0}

        def write(dest: Path, src: Path, localize: bool):
            dest.parent.mkdir(parents=True, exist_ok=True)
            if localize and src.suffix in TEXT_SUFFIXES:
                text, n = rewrite(src.read_text(encoding="utf-8"))
                stats["links"] += n
                dest.write_text(text, encoding="utf-8")
            else:
                shutil.copyfile(src, dest)

        for rel, en_src in sorted(en_files.items()):
            dest = lang_root / rel
            if en_src.name == ORDER:
                if opt("sync_order_files", True):
                    write(dest, en_src, localize=False)
                    stats["menus"] += 1
            elif rel in tr_files:
                write(dest, tr_files[rel], localize=True)
                stats["translated"] += 1
            elif not dest.exists() and opt("english_fallback", True):
                write(dest, en_src, localize=True)
                stats["fallback"] += 1

        stats["stale_ignored"] = len([r for r in tr_files if r not in en_files and not r.endswith(ORDER)])

        if opt("mirror_deletions", True):
            for rel, path in lang_files.items():
                if rel not in en_files:
                    path.unlink()
                    stats["deleted"] += 1
            # tidy up empty folders left behind
            for d in sorted((p for p in lang_root.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)):
                if not any(d.iterdir()):
                    d.rmdir()

        sh("git", "add", "-A", "docs", cwd=tmp)
        status = sh("git", "-c", "core.quotepath=off", "diff", "--cached", "--name-status", cwd=tmp, capture=True).splitlines()
        if not status:
            log(f"- `{lang}`: no changes vs `{target}`")
            return {"lang": lang, "status": "unchanged"}

        summary = (f"{len(status)} file change(s): {stats['translated']} translated, {stats['fallback']} English fallback, "
                   f"{stats['deleted']} deleted, menus synced, {stats['links']} links localized"
                   + (f", {stats['stale_ignored']} stale translation(s) ignored" if stats["stale_ignored"] else ""))
        log(f"- `{lang}` -> `{target}` (folder `{cat}`): {summary}")
        for line in status[:40]:
            log(f"    - {line}")
        if args.dry_run:
            return {"lang": lang, "status": "dry-run", "changes": len(status)}

        src_sha = sh("git", "rev-parse", "--short", "HEAD", capture=True)
        sh("git", "-c", "user.name=crowdin-readme-sync[bot]",
           "-c", "user.email=crowdin-readme-sync@users.noreply.github.com",
           "commit", "-q", "-m", f"Crowdin: sync {lang} from {CONFIG['source_branch']}@{src_sha}", cwd=tmp)
        sh("git", "push", "-q", "--force", "origin", f"{work}:{work}", cwd=tmp)
        if args.no_pr:
            return {"lang": lang, "status": "pushed"}

        body = (f"Automated sync of **{lang}** from `{CONFIG['source_branch']}` @ `{src_sha}`.\n\n"
                f"- Category folder: `{CONFIG['english_category']}` → `{cat}`\n"
                f"- Translated pages written: {stats['translated']}\n"
                f"- English fallback pages added (new, not yet translated): {stats['fallback']}\n"
                f"- Pages removed (deleted/renamed in English): {stats['deleted']}\n"
                f"- Stale translations ignored: {stats['stale_ignored']}\n"
                f"- Menus (`_order.yaml`) synced from English, root category menu untouched\n"
                f"- Links localized: {stats['links']}\n\n"
                "<details><summary>Files</summary>\n\n```\n" + "\n".join(status) + "\n```\n</details>\n\n"
                "Merging this PR lets ReadMe sync the language site.")
        url = sh("gh", "pr", "list", "--head", work, "--base", target, "--state", "open",
                 "--json", "url", "-q", ".[0].url", capture=True)
        if url:
            sh("gh", "pr", "edit", url, "--body", body)
            log(f"    updated PR {url}")
        else:
            url = sh("gh", "pr", "create", "--head", work, "--base", target,
                     "--title", f"Crowdin → ReadMe: {lang}", "--body", body, capture=True)
            log(f"    opened PR {url}")

        if args.auto_merge or opt("auto_merge", False):
            # Prefer GitHub auto-merge (waits for required checks); fall back to a direct merge
            # when the repo has no required checks or auto-merge is disabled.
            if subprocess.run(["gh", "pr", "merge", url, "--auto", "--merge"], capture_output=True).returncode != 0:
                sh("gh", "pr", "merge", url, "--merge", "--delete-branch")
            log("    merged (auto_merge)")
        return {"lang": lang, "status": "pr", "url": url, "changes": len(status)}
    finally:
        sh("git", "worktree", "remove", "--force", str(tmp), check=False)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--langs", help="comma-separated ReadMe language codes (default: enabled_languages)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-pr", action="store_true")
    ap.add_argument("--auto-merge", action="store_true", help="merge the PRs (overrides config auto_merge)")
    args = ap.parse_args()

    langs = ([l.strip() for l in args.langs.split(",") if l.strip()] if args.langs
             else opt("enabled_languages", sorted(set(CONFIG["languages"].values()))))
    log(f"### Crowdin → ReadMe sync ({', '.join(langs)})")
    results = [process_language(l, args) for l in langs]
    print(json.dumps(results, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
