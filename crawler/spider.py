import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List, Dict


def fetch_html(url: str) -> str:
    """
    Fetch HTML content from a URL.
    """

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch {url} -> {e}")
        return ""

def extract_links(page_url: str) -> List[Dict]:
    """
    Extract all links (<a> tags) from a webpage.

    Returns:
        List of dictionaries:
        [
            {
                "source_url": str,
                "href": str,
                "text": str
            }
        ]
    """

    html = fetch_html(page_url)

    if not html:
        return []

    soup = BeautifulSoup(html, "lxml")

    links_data = []#this is a list of dictionaries

    seen = set()

    for link in soup.find_all("a"):
        href = link.get("href")
        text = link.get_text(strip=True)

        if not href:
            continue

        if href.startswith("#") or href.startswith("mailto:") or href.startswith("javascript:"):
            continue

        absolute_url = urljoin(page_url, href)

        if absolute_url in seen:
            continue
        seen.add(absolute_url)

        links_data.append({
            "source_url": page_url,
            "href": absolute_url,
            "text": text if text else "No text"
        })

    return links_data
