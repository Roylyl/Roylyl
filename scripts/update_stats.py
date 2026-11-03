"""Generate the profile statistics card from GitHub's public repository data."""
import json
import os
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

OWNER = "Roylyl"
TARGET = Path(__file__).resolve().parents[1] / "assets" / "github-stats.svg"
LANGUAGES_TARGET = TARGET.with_name("languages.svg")


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


def render_languages(languages):
    total = sum(languages.values())
    items = languages.most_common(6)
    remainder = total - sum(value for _, value in items)
    if remainder:
        items.append(("其他", remainder))
    colors = ["#007aff", "#5ac8fa", "#5856d6", "#34c759", "#ff9500", "#af52de", "#aeaeb2"]
    body = '<text x="28" y="38" font-size="21" font-weight="600" fill="#1c1c1e">公开仓库语言分布</text>'
    body += '<defs><clipPath id="bar"><rect x="28" y="64" width="464" height="10" rx="5"/></clipPath></defs>'
    x = 28
    for i, (name, value) in enumerate(items):
        width = 464 * value / total
        body += f'<rect x="{x:.3f}" y="64" width="{width:.3f}" height="10" fill="{colors[i]}" clip-path="url(#bar)"/>'
        x += width
        col, row = i % 2, i // 2
        cx, cy = 33 + col * 244, 96 + row * 19
        body += f'<circle cx="{cx}" cy="{cy-4}" r="4" fill="{colors[i]}"/>'
        body += (f'<text x="{cx+10}" y="{cy}" font-size="11" fill="#6e6e73">'
                 f'{escape(name)} {value / total:.1%}</text>')
    if not total:
        body += '<text x="28" y="106" font-size="14" fill="#6e6e73">暂无公开语言数据</text>'
    body += '<text x="28" y="180" font-size="10" fill="#86868b">按GitHub代码字节数汇总，不含Fork仓库</text>'
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="520" height="195" '
            'viewBox="0 0 520 195" role="img"><title>公开仓库语言分布</title>'
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
    languages = Counter()
    originals = [repo for repo in repos if not repo["fork"]]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(lambda repo: get(f'/repos/{repo["full_name"]}/languages'), originals):
            languages.update(result)
    # Fetch everything first; a failed request must retain the last good cards.
    result = render(user, repos)
    language_result = render_languages(languages)
    for target, content in [(TARGET, result), (LANGUAGES_TARGET, language_result)]:
        temporary = target.with_suffix(".svg.tmp")
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(target)
    print(f"Updated public statistics for {len(repos)} repositories.")


if __name__ == "__main__":
    main()
