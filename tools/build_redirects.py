#!/usr/bin/env python3
import re, sys, csv
from pathlib import Path
from difflib import get_close_matches

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
BUILD = ROOT / "build"
BUILD.mkdir(exist_ok=True)

# Простой индекс md-файлов: {basename: relative_path}
def index_md():
    idx = {}
    for p in DOCS.rglob("*.md"):
        rel = p.relative_to(DOCS).as_posix()
        base = p.stem.lower()  # file name without .md
        idx.setdefault(base, set()).add(rel)
    return idx

def normalize_old(url: str) -> tuple[str, str|None]:
    url = url.strip()
    if not url or url.startswith("#"):
        return "", None
    url = re.sub(r"^https?://[^/]+", "", url)  # drop domain
    if not url.startswith("/"):
        url = "/" + url
    path, anchor = (url.split("#", 1) + [None])[:2]
    path = path.rstrip("/")
    return path, anchor

def guess_target(path: str, idx: dict) -> str|None:
    # 1) try 1:1 html->md in similar folders
    base = Path(path).with_suffix("").name.lower()  # "buttons" from /ui/buttons.html
    # 2) fuzzy by basename
    cands = list(idx.get(base, []))
    if cands:
        return sorted(cands, key=lambda s: len(s))[0]
    # 3) special known cases
    special = {
        "/getting-started.html": "learn/index.md",
        "/overview/index.html": "overview/getting-started.md",
    }
    if path in special:
        return special[path]
    # 4) fuzzy among all
    all_basenames = list(idx.keys())
    m = get_close_matches(base, all_basenames, n=1, cutoff=0.9)
    if m:
        return sorted(idx[m[0]])[0]
    return None

def main():
    src = DATA / "old_urls.txt"
    if not src.exists():
        print("Put old paths into data/old_urls.txt (one per line).", file=sys.stderr)
        sys.exit(2)

    idx = index_md()
    redirs = {}
    unmapped = []

    for raw in src.read_text(encoding="utf-8").splitlines():
        path, anchor = normalize_old(raw)
        if not path:
            continue
        target = guess_target(path, idx)
        if not target:
            unmapped.append({"old": path, "reason": "no-target"})
            continue
        if anchor:
            # перенаправляем на целевую страницу + сохраняем якорь (если есть/будет легаси-якорь)
            redirs[f"{path}#{anchor}"] = f"{target}#{anchor}"
        else:
            redirs[path] = target

    # write redirects.yml (sorted)
    out = ROOT / "redirects.yml"
    lines = []
    for k in sorted(redirs.keys()):
        v = redirs[k]
        lines.append(f"\"{k.lstrip('/')}\": \"{v}\"")
    out.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")

    # report
    with (BUILD / "redirects_unmapped.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["old", "reason"])
        w.writeheader()
        for r in unmapped:
            w.writerow(r)

    print(f"Mapped: {len(redirs)}; Unmapped: {len(unmapped)}; wrote {out}")

if __name__ == "__main__":
    main()
