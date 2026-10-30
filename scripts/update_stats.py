"""Generate the profile statistics card from GitHub's public repository data."""
import json
import os
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

OWNER = "Roylyl"
TARGET = Path(__file__).resolve().parents[1] / "assets" / "github-stats.svg"


def get(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "Roylyl-profile"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(f"https://api.github.com{path}", headers=headers), timeout=30) as response:
        return json.load(response)


def render(user, repos):
    def text(x, y, value, size, color="#1c1c1e", weight=400):
        return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
                f'font-weight="{weight}">{escape(str(value))}</text>')

    metrics = [("公开仓库获星", sum(r["stargazers_count"] for r in repos)),
               ("关注者", user["followers"]),
               ("公开仓库", len(repos)),
               ("公开仓库被Fork", sum(r["forks_count"] for r in repos))]
    body = text(28, 38, "GitHub动态", 21, weight=600)
    for i, (label, value) in enumerate(metrics):
        x, y = 28 + (i % 2) * 250, 78 + (i // 2) * 57
        body += text(x, y, f"{value:,}", 26, weight=600)
        body += text(x, y + 19, label, 12, "#6e6e73")
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    body += text(28, 180, f"更新于{date} · GitHub公开数据", 10, "#86868b")
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="520" height="195" '
            'viewBox="0 0 520 195" role="img"><title>Roylyl的GitHub公开统计</title>'
            '<rect width="520" height="195" rx="27.313131" fill="#f5f5f7"/>'
            '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Microsoft YaHei,Arial,sans-serif">'
            + body + '</g></svg>\n')


def main():
    user = get(f"/users/{OWNER}")
    repos = []
    page = 1
    while True:
        batch = get(f"/users/{OWNER}/repos?type=owner&per_page=100&page={page}")
        repos.extend(r for r in batch if not r["private"])
        if len(batch) < 100:
            break
        page += 1
    # Fetch everything first; a failed request must retain the last good card.
    result = render(user, repos)
    temporary = TARGET.with_suffix(".svg.tmp")
    temporary.write_text(result, encoding="utf-8")
    temporary.replace(TARGET)
    print(f"Updated public statistics for {len(repos)} repositories.")


if __name__ == "__main__":
    main()
