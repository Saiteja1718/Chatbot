import urllib.parse
import requests


def get_images_links(search_term: str) -> str:
    """
    Return a food image URL for the given recipe name using Unsplash.

    If we can't retrieve a valid image URL, return an empty string so
    the UI will show only the dish name with **no image frame**.
    """
    cleaned = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in search_term)
    cleaned = " ".join(cleaned.split())
    query = urllib.parse.quote(f"{cleaned} food recipe")
    url = f"https://source.unsplash.com/400x300/?{query}"

    try:
        # Follow redirects and ensure we get a 200 OK for an image.
        resp = requests.get(url, timeout=5, allow_redirects=True)
        if resp.ok:
            # Use final URL so the browser can load it directly.
            return resp.url
    except Exception:
        pass

    # No valid image → let the frontend skip the image entirely.
    return ""


