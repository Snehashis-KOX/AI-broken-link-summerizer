# crawler/checker.py

import requests
from typing import Dict, Optional


def check_link(link_data: Dict) -> Optional[Dict]:
    """
    Checks if a link is broken (404 or request failure).

    Args:
        link_data (dict):
            {
                "source_url": str,
                "href": str,
                "text": str
            }

    Returns:
        dict or None:
            {
                "broken_url": str,
                "context": str,
                "source_url": str
            }
    """

    url = link_data.get("href")

    if not url:
        return None

    try:
        response = requests.get(url, timeout=5)

        # If link is broken
        if response.status_code >= 400:
            return {
                "broken_url": url,
                "context": link_data.get("text", ""),
                "source_url": link_data.get("source_url", "")
            }

    except requests.exceptions.RequestException:
        # Treat request errors as broken links
        return {
            "broken_url": url,
            "context": link_data.get("text", ""),
            "source_url": link_data.get("source_url", "")
        }

    return None
