'''from crawler.spider import extract_links

# url = "https://example.com"
url = "https://books.toscrape.com/"

links = extract_links(url)

for link in links[:5]:
    print(link)

print(f"Total links found: {len(links)}")'''

from crawler.spider import extract_links
from crawler.checker import check_link

url = "https://www.eddymens.com/blog/page-with-broken-pages-for-testing-53049e870421"

links = extract_links(url)

broken_links = []

for link in links[:10]:  # limit for testing
    result = check_link(link)
    if result:
        broken_links.append(result)

print(f"Broken links found: {len(broken_links)}")

for b in broken_links:
    print(b)
