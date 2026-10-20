"""Sum release-asset downloads across Roylyl's public repositories."""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

OWNER = "Roylyl"
TOKEN = os.environ.get("GH_TOKEN")


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
    print(f"Public release-asset downloads: {total:,}")


if __name__ == "__main__":
    main()
