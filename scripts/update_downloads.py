"""Sum release-asset downloads across Roylyl's public repositories."""
import json
import os
from pathlib import Path
from html import escape
from urllib.request import Request, urlopen

OWNER = "Roylyl"
TOKEN = os.environ.get("GH_TOKEN")


def write_badge(message, target):
    """Render the saved total directly, without a third-party badge service."""
    label_width = 105
    value_width = max(52, len(message) * 8 + 20)
    width = label_width + value_width
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="26" '
        f'viewBox="0 0 {width} 26" role="img" aria-label="Downloads: {escape(message)}">'
        f'<title>公开仓库Release附件累计下载量：{escape(message)}</title>'
        f'<defs><clipPath id="round"><rect width="{width}" height="26" rx="4"/></clipPath></defs>'
        '<g clip-path="url(#round)">'
        f'<rect width="{width}" height="26" fill="#6e6e73"/>'
        f'<rect x="{label_width}" width="{value_width}" height="26" fill="#0071e3"/>'
        '<path d="M14 6v9m-4-4 4 4 4-4M8 17v3h12v-3" fill="none" '
        'stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '<g fill="#fff" font-family="Verdana,Arial,sans-serif" font-size="12" text-anchor="middle">'
        '<text x="63" y="17">Downloads</text>'
        f'<text x="{label_width + value_width / 2}" y="17">{escape(message)}</text>'
        '</g></g></svg>\n'
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
