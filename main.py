from crawler.spider import extract_links

# url = "https://example.com"
url = "https://books.toscrape.com/"

links = extract_links(url)

for link in links[:5]:
    print(link)

print(f"Total links found: {len(links)}")
