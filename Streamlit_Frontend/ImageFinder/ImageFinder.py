import urllib.parse


def get_images_links(search_term: str) -> str:
    """
    Return a food image URL for the given recipe name using Unsplash.

    We use the free `source.unsplash.com` endpoint, which returns a
    random but relevant image for the given query. This avoids HTML
    scraping and works well on Streamlit Cloud.
    """
    cleaned = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in search_term)
    cleaned = " ".join(cleaned.split())
    query = urllib.parse.quote(f"{cleaned} food recipe")
    return f"https://source.unsplash.com/400x300/?{query}"


