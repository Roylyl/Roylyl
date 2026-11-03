"""Sum release-asset downloads across Roylyl's public repositories."""
import json
import os
from pathlib import Path
from html import escape
from urllib.request import Request, urlopen

OWNER = "Roylyl"
TOKEN = os.environ.get("GH_TOKEN")


def write_badge(message, target):
    """Match the adjacent Shields flat badges: a 20px canvas and 11px type."""
    label_width = 89
    value_width = max(20, sum(4 if c == "," else 7 for c in message) + 10)
    width = label_width + value_width
    github_path = "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
    value_x = label_width + value_width / 2
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20" '
        f'viewBox="0 0 {width} 20" role="img" aria-label="Downloads: {escape(message)}">'
        f'<title>公开仓库Release附件累计下载量：{escape(message)}</title>'
        '<linearGradient id="shade" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" '
        'stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient>'
        f'<clipPath id="round"><rect width="{width}" height="20" rx="3"/></clipPath>'
        '<g clip-path="url(#round)">'
        f'<path fill="#6e6e73" d="M0 0h{label_width}v20H0z"/>'
        f'<path fill="#0071e3" d="M{label_width} 0h{value_width}v20H{label_width}z"/>'
        f'<path fill="url(#shade)" d="M0 0h{width}v20H0z"/></g>'
        f'<path fill="#fff" transform="translate(5 3) scale(.583333)" d="{github_path}"/>'
        '<g fill="#fff" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11" '
        'text-anchor="middle" text-rendering="geometricPrecision">'
        '<g fill="#010101" fill-opacity=".3">'
        '<text x="52.5" y="15">Downloads</text>'
        f'<text x="{value_x}" y="15">{escape(message)}</text></g>'
        '<text x="52.5" y="14">Downloads</text>'
        f'<text x="{value_x}" y="14">{escape(message)}</text>'
        '</g></svg>\n'
    )
    temporary = target.with_suffix(".svg.tmp")
    temporary.write_text(svg, encoding="utf-8")
    temporary.replace(target)


def pages(path):
    page = 1
    while True:
        request = Request(
            f"https://api.github.com/{path}?per_page=100&page={page}",
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "Roylyl-profile-downloads",
                **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
            },
        )
        with urlopen(request, timeout=30) as response:
            items = json.load(response)
        yield from items
        if len(items) < 100:
            break
        page += 1


def main():
    total = 0
    for repo in pages(f"users/{OWNER}/repos"):
        if repo["private"]:
            continue
        for release in pages(f"repos/{OWNER}/{repo['name']}/releases"):
            if release["draft"]:
                continue
            # Use the assets endpoint so releases with many assets are complete.
            for asset in pages(f"repos/{OWNER}/{repo['name']}/releases/{release['id']}/assets"):
                total += asset["download_count"]
    # Write only after every request succeeds; failures preserve the last total.
    target = Path(__file__).resolve().parents[1] / "assets" / "downloads.json"
    target.write_text(json.dumps({
        "schemaVersion": 1,
        "label": "Downloads",
        "message": f"{total:,}",
        "color": "0071e3",
        "namedLogo": "github",
    }, indent=2) + "\n", encoding="utf-8")
    write_badge(f"{total:,}", target.with_suffix(".svg"))
    print(f"Public release-asset downloads: {total:,}")


if __name__ == "__main__":
    main()
