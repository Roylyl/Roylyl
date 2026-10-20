"""Generate an animated heatmap from GitHub's public contribution calendar."""
from datetime import date, datetime, timedelta, timezone
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.request import Request, urlopen

OWNER = "Roylyl"

ASSETS = Path(__file__).resolve().parents[1] / 'assets'


def get(url, api=True):
    headers = {'User-Agent': 'Roylyl-profile-art', 'Accept': 'application/vnd.github+json' if api else 'text/html'}
    with urlopen(Request(url, headers=headers), timeout=30) as response:
        raw = response.read().decode('utf-8')
    return json.loads(raw) if api else raw


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'data-date' in attrs and 'data-level' in attrs:
            day = date.fromisoformat(attrs['data-date'])
            level = int(attrs['data-level'])
            if not 0 <= level <= 4 or day in self.days:
                raise ValueError('Invalid or duplicate contribution day')
            self.days[day] = level

    def validate(self):
        ordered = sorted(self.days)
        if not 350 <= len(ordered) <= 380:
            raise ValueError('Incomplete contribution calendar; preserve previous images')
        if any(b - a != timedelta(days=1) for a, b in zip(ordered, ordered[1:])):
            raise ValueError('Contribution calendar has missing days')
        today = datetime.now(timezone.utc).date()
        if abs((today - ordered[-1]).days) > 2:
            raise ValueError('Stale contribution calendar')
        return ordered


def text(x, y, value, size=16, color='#1d1d1f', extra=''):
    return f'<text x="{x}" y="{y}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Microsoft YaHei,Arial,sans-serif" font-size="{size}" fill="{color}" {extra}>{escape(str(value))}</text>'


def svg(w, h, title, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title)}</title><defs><clipPath id="module-corners"><rect width="{w}" height="{h}" rx="{w * .026}"/></clipPath></defs><g clip-path="url(#module-corners)"><rect width="{w}" height="{h}" fill="#f5f5f7"/>{body}</g></svg>\n'


def heatmap(calendar, stamp):
    days = calendar.validate()
    start = days[0] - timedelta(days=(days[0].weekday() + 1) % 7)
    body = text(26, 34, '创造的足迹', 20, '#1c1c1e', 'font-weight="600"')
    palette = ['#e5e5ea', '#c2dcfa', '#82b9f3', '#3690ea', '#0071e3']
    last_month = None
    for day in days:
        col, row = divmod((day - start).days, 7)
        x, y = 53 + col * 17, 75 + row * 17
        if day.month != last_month and day.day <= 7:
            body += text(x, 62, day.strftime('%b'), 10, '#6e6e73')
            last_month = day.month
        body += f'<rect x="{x}" y="{y}" width="13" height="13" rx="3" fill="{palette[calendar.days[day]]}"><title>{day.isoformat()} · level {calendar.days[day]}/4</title></rect>'
    for row, name in [(1, 'Mon'), (3, 'Wed'), (5, 'Fri')]:
        body += text(15, 85 + row * 17, name, 10, '#6e6e73')
    body += '<style>@keyframes radar{from{transform:translateX(0)}to{transform:translateX(901px)}}.scan{animation:radar 8s linear infinite}@media(prefers-reduced-motion:reduce){.scan{animation:none;display:none}}</style><rect class="scan" x="53" y="72" width="3" height="122" rx="1.5" fill="#0071e3" opacity=".7"/>'
    body += text(26, 225, f'{days[0]}至{days[-1]} · GitHub公开展示的贡献强度', 12, '#6e6e73')
    body += text(26, 251, f'更新于{stamp}', 11, '#86868b')
    for i, color in enumerate(palette):
        body += f'<rect x="{850+i*18}" y="218" width="13" height="13" rx="3" fill="{color}"/>'
    return svg(1000, 272, 'Roylyl贡献热力图：真实贡献等级与动态扫描线', body)



def main():
    calendar = Calendar()
    calendar.feed(get(f'https://github.com/users/{OWNER}/contributions', api=False))
    stamp = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d')
    result = heatmap(calendar, stamp)
    (ASSETS / 'contributions.svg').write_text(result, encoding='utf-8')
    print(f'Generated animated heatmap from {len(calendar.days)} public contribution days.')


if __name__ == '__main__':
    main()
