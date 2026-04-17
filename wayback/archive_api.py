# wayback/archive_api.py

import requests
from typing import Optional


WAYBACK_API = "http://archive.org/wayback/available"


def get_wayback_snapshot(url: str) -> Optional[str]:
    """
    Fetch the latest archived snapshot URL from Wayback Machine.

    Args:
        url (str): Broken URL

    Returns:
        snapshot_url (str) or None
    """

    try:
        params = {"url": url}#params is a dictionary that contains the URL of the broken link
        response = requests.get(WAYBACK_API, params=params, timeout=5)
        data = response.json()

        snapshots = data.get("archived_snapshots", {})

        if "closest" in snapshots:
            return snapshots["closest"]["url"]

    except requests.exceptions.RequestException:
        pass

    return None


def fetch_archived_text(snapshot_url: str) -> str:
    """
    Fetch and clean text from archived page.

    Args:
        snapshot_url (str)

    Returns:
        cleaned text (str)
    """

    try:
        response = requests.get(snapshot_url, timeout=5)

        if response.status_code == 200:
            # Simple text extraction (no BeautifulSoup needed yet)
            text = response.text

            # Limit size for AI (VERY IMPORTANT)
            return text[:1500]

    except requests.exceptions.RequestException:
        pass

    return ""
