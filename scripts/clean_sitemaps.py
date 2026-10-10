#!/usr/bin/env python3
"""Strip 404 error routes from generated sitemaps and feeds."""
import json
import re
import sys

def clean_feeds():
    for f in ['docs/sitemap.xml', 'docs/news-sitemap.xml']:
        try:
            content = open(f).read()
            content = re.sub(r'\s*<url>(?:(?!</url>).)*?404.*?</url>', '', content, flags=re.DOTALL)
            open(f, 'w').write(content)
        except Exception:
            pass

    for f in ['docs/rss.xml']:
        try:
            content = open(f).read()
            content = re.sub(r'\s*<item>(?:(?!</item>).)*?404.*?</item>', '', content, flags=re.DOTALL)
            open(f, 'w').write(content)
        except Exception:
            pass

    for f in ['docs/atom.xml']:
        try:
            content = open(f).read()
            content = re.sub(r'\s*<entry>(?:(?!</entry>).)*?404.*?</entry>', '', content, flags=re.DOTALL)
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
