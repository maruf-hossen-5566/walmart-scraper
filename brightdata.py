import requests
from config import (
    BRIGHTDATA_API_KEY as api_key,
    BRIGHTDATA_ENDPOINT as endpoint,
    BRIGHTDATA_ZONE as zone,
    TIMEOUT as timeout,
)


def fetch_html(target_url):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "zone": f"{zone}",
        "url": target_url,
        "format": "raw",
    }

    response = requests.post(
        endpoint,  # type: ignore
        json=data,
        headers=headers,
        timeout=timeout,
    )

    response.raise_for_status()
    return response.text
