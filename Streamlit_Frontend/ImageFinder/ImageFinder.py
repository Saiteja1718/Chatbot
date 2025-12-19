import base64
import os
import urllib.parse

import requests


# Simple in-process cache so we don't refetch the same term repeatedly
_CACHE: dict[str, str] = {}


def _clean_query(search_term: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in search_term)
    return " ".join(cleaned.split())


def _to_data_url(image_bytes: bytes, content_type: str | None) -> str:
    ct = (content_type or "image/jpeg").split(";")[0].strip() or "image/jpeg"
    b64 = base64.b64encode(image_bytes).decode("ascii")
    return f"data:{ct};base64,{b64}"


def get_images_links(search_term: str) -> str:
    """
    Return a recipe image as a small base64 **data URL**.

    Why:
    - On Streamlit Cloud, the user's browser may be blocked/rate-limited from fetching
      `source.unsplash.com` directly, causing broken images after deployment.
    - Returning a data URL makes the image load from the app response itself.

    How:
    - If `UNSPLASH_ACCESS_KEY` is set, use the official Unsplash Search API to get a
      stable image URL (recommended).
    - Otherwise fall back to `source.unsplash.com` (less reliable).

    If anything fails, return an empty string so the UI shows the recipe-name placeholder.
    """
    if not search_term:
        return ""

    query_clean = _clean_query(search_term)
    cache_key = query_clean.lower()
    if cache_key in _CACHE:
        return _CACHE[cache_key]

    access_key = os.getenv("UNSPLASH_ACCESS_KEY", "").strip()

    try:
        img_url = None

        if access_key:
            # Official API: https://unsplash.com/documentation#search-photos
            params = {
                "query": f"{query_clean} food recipe",
                "per_page": 1,
                "content_filter": "high",
                "orientation": "landscape",
            }
            headers = {"Authorization": f"Client-ID {access_key}"}
            r = requests.get(
                "https://api.unsplash.com/search/photos",
                params=params,
                headers=headers,
                timeout=10,
            )
            r.raise_for_status()
            data = r.json()
            results = data.get("results") or []
            if results:
                urls = results[0].get("urls") or {}
                # "small" keeps payload reasonable for base64
                img_url = urls.get("small") or urls.get("regular") or urls.get("thumb")

        if not img_url:
            # Fallback: random image source (can be rate limited)
            q = urllib.parse.quote(f"{query_clean} food recipe")
            img_url = f"https://source.unsplash.com/400x300/?{q}"

        img_resp = requests.get(img_url, timeout=15, allow_redirects=True)
        img_resp.raise_for_status()
        ct = img_resp.headers.get("content-type")

        data_url = _to_data_url(img_resp.content, ct)
        _CACHE[cache_key] = data_url
        return data_url
    except Exception:
        return ""


