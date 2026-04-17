
from crawler.spider import extract_links
from crawler.checker import check_link
from wayback.archive_api import get_wayback_snapshot, fetch_archived_text


url = "https://www.eddymens.com/blog/page-with-broken-pages-for-testing-53049e870421"

links = extract_links(url)

broken_links = []

for link in links[:20]:  # limit for testing
    result = check_link(link)
    if result:
        broken_links.append(result)

print(f"Broken links found: {len(broken_links)}")

for b in broken_links:
    print(b)

for b in broken_links:
    print("\nChecking:", b["broken_url"])

    snapshot = get_wayback_snapshot(b["broken_url"])

    if snapshot:#this will get snapshot url from wayback machine
        print("✅ Snapshot found:", snapshot)

        text = fetch_archived_text(snapshot)#this will fetch and clean text from archived page
        print("📄 Sample text:", text[:200])
    else:
        print("❌ No snapshot found")
