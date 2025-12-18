import os
from pathlib import Path


def get_images_links(search_term: str) -> str:
    """
    Return a local placeholder image path for the given recipe.

    For reliability on Streamlit Cloud (where some external image
    providers or data URLs may not render correctly), we always return
    the bundled logo image in Assets. This guarantees that every card
    shows a valid image even if it's not recipe-specific.
    """
    root = Path(__file__).resolve().parents[2]
    logo_path = root / "Assets" / "logo_img1.jpg"

    if logo_path.is_file():
        return str(logo_path)
    return ""


