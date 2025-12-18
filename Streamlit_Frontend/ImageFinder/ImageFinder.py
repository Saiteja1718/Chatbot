import urllib.parse


def get_images_links(search_term: str) -> str:
    """
    Return a food image URL for the given recipe name using Unsplash.

    We simply return a `source.unsplash.com` URL and let the browser
    fetch the image directly. This keeps behavior identical between
    local runs and Streamlit Cloud (no server‑side HTTP needed).
    """
    cleaned = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in search_term)
    cleaned = " ".join(cleaned.split())
    query = urllib.parse.quote(f"{cleaned} food recipe")
    return f"https://source.unsplash.com/400x300/?{query}"


