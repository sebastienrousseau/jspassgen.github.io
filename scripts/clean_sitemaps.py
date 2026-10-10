#!/usr/bin/env python3
"""Strip 404 error routes from generated sitemaps and feeds."""
import json
import re
import sys

def clean_feeds():
    for f in ['docs/sitemap.xml']:
        try:
            content = open(f).read()
            content = re.sub(r'\s*<url>(?:(?!</url>).)*?404.*?</url>', '', content, flags=re.DOTALL)
            content = re.sub(r'<lastmod></lastmod>', '<lastmod>2026-10-10</lastmod>', content)
            open(f, 'w').write(content)
        except Exception:
            pass

    for f in ['docs/news-sitemap.xml']:
        try:
            content = open(f).read()
            content = re.sub(r'\s*<url>(?:(?!</url>).)*?404.*?</url>', '', content, flags=re.DOTALL)
            content = re.sub(r'<news:publication_date></news:publication_date>', '<news:publication_date>2026-10-10T12:00:00+00:00</news:publication_date>', content)
            open(f, 'w').write(content)
        except Exception:
            pass

    for f in ['docs/rss.xml']:
        try:
            content = open(f).read()
            content = re.sub(r'\s*<item>(?:(?!</item>).)*?404.*?</item>', '', content, flags=re.DOTALL)
            content = re.sub(r'<pubDate></pubDate>', '<pubDate>Sat, 10 Oct 2026 12:00:00 +0000</pubDate>', content)
            open(f, 'w').write(content)
        except Exception:
            pass

    for f in ['docs/atom.xml']:
        try:
            content = open(f).read()
            content = re.sub(r'\s*<entry>(?:(?!</entry>).)*?404.*?</entry>', '', content, flags=re.DOTALL)
            content = re.sub(r'<updated></updated>', '<updated>2026-10-10T12:00:00+00:00</updated>', content)
            content = re.sub(r'<published></published>', '<published>2026-10-10T12:00:00+00:00</published>', content)
            open(f, 'w').write(content)
        except Exception:
            pass

    try:
        data = json.load(open('docs/feed.json'))
        data['items'] = [it for it in data.get('items', []) if '404' not in it.get('url', '') and '404' not in it.get('id', '')]
        json.dump(data, open('docs/feed.json', 'w'), indent=2)
    except Exception:
        pass

if __name__ == '__main__':
    clean_feeds()

