"""Validate research packaging, not application behavior. Python 3.10+, stdlib only."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import csv
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def validate():
    tracked = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT, text=True, encoding="utf-8"
    ).splitlines()
    paths = [ROOT / p for p in sorted(set(tracked)) if (ROOT / p).is_file()]
    errors, counts = [], {"csv_files": 0, "csv_rows": 0, "json_files": 0,
                           "markdown_links": 0, "markdown_anchors": 0, "source_records": 0,
                           "source_ids": 0, "preserved_files": 0}
    source_ids = set()
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix == ".csv":
            with path.open(encoding="utf-8-sig", newline="") as f:
                rows = list(csv.reader(f))
            counts["csv_files"] += 1
            counts["csv_rows"] += max(0, len(rows) - 1)
            if not rows:
                errors.append(f"Empty CSV: {rel}")
                continue
            for i, row in enumerate(rows[1:], 2):
                if len(row) != len(rows[0]):
                    errors.append(f"CSV width {rel}:{i}: {len(row)} != {len(rows[0])}")
            if rel.count("/") == 2 and path.name == "sources.csv":
                seen = set()
                for row in rows[1:]:
                    if not row:
                        continue
                    key = row[0]
                    if key in seen:
                        errors.append(f"Duplicate source ID {rel}: {key}")
                    seen.add(key)
                    source_ids.add(key)
                    counts["source_records"] += 1
        if path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8-sig"))
                counts["json_files"] += 1
            except Exception as exc:
                errors.append(f"JSON {rel}: {exc}")
        if path.suffix == ".md" and not any(x in rel for x in ("/original-", "/notion-original/", "provenance/notion/")):
            content = path.read_text(encoding="utf-8-sig")
            for label, target in re.findall(r"\[([^\]]+)\]\(([^\s)]+)\)", content):
                target = target.strip("<>")
                if urlsplit(target).scheme or target.startswith("#"):
                    continue
                destination = unquote(target.split("#")[0])
                if not destination:
                    continue
                counts["markdown_links"] += 1
                if not (path.parent / destination).exists():
                    errors.append(f"Missing local link {rel}: {target}")
                elif '#' in target and (path.parent / destination).suffix == '.md':
                    anchor = unquote(target.split('#', 1)[1])
                    headings = re.findall(r'^#{1,6}\s+(.+?)\s*#*$', (path.parent / destination).read_text(encoding='utf-8-sig'), re.M)
                    slugs = [re.sub(r'\s', '-', re.sub(r'[^\w\- ]', '', h.lower())) for h in headings]
                    counts['markdown_anchors'] += 1
                    if anchor not in slugs:
                        errors.append(f"Missing heading anchor {rel}: {target}")
            if re.search(r"X-Amz-(?:Signature|Credential)=|[?&]token=gh[pousr]_", content, re.I):
                errors.append(f"Expiring/sensitive URL in {rel}")
    manifest = ROOT / "research/provenance/preserved-files.json"
    if manifest.exists():
        for record in json.loads(manifest.read_text(encoding="utf-8"))["files"]:
            p = ROOT / record["path"]
            if hashlib.sha256(p.read_bytes()).hexdigest() != record["sha256"]:
                errors.append(f"Preserved-file hash mismatch: {record['path']}")
            counts["preserved_files"] += 1
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix == ".md" and path.name != "README.md" and (rel.startswith("docs/") or rel.startswith("research/")) and not any(x in rel for x in ("/original-", "/notion-original/", "provenance/notion/")):
            for sid in set(re.findall(r"(?<![\w-])(?:GOP|SUD|PRA|DHA|SUH|KAN)-\d{3}\b", path.read_text(encoding="utf-8-sig"))):
                if sid not in source_ids:
                    errors.append(f"Unknown source ID {rel}: {sid}")
    counts["source_ids"] = len(source_ids)
    result = {"scope": "Documentation structure and preserved-file integrity only; no application or live-provider testing", "counts": counts, "errors": errors, "passed": not errors}
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    raise SystemExit(0 if validate()["passed"] else 1)
