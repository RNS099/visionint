import requests
from pathlib import Path
from urllib.parse import quote_plus


CATBOX_API = "https://catbox.moe/user/api.php"


def upload_to_catbox(image_path: str) -> str:
    """
    Upload image to Catbox and return direct image URL.
    """

    image_file = Path(image_path)

    if not image_file.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    if not image_file.is_file():
        raise ValueError(f"Invalid file: {image_path}")

    data = {
        "reqtype": "fileupload"
    }

    try:
        with open(image_file, "rb") as file:
            response = requests.post(
                CATBOX_API,
                data=data,
                files={"fileToUpload": file},
                timeout=30
            )

        response.raise_for_status()

        uploaded_url = response.text.strip()

        if not uploaded_url.startswith("https://"):
            raise Exception(f"Upload failed: {uploaded_url}")

        return uploaded_url

    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error: {e}")


def generate_reverse_search_links(image_url: str) -> dict:
    """
    Generate Google and Yandex reverse image search URLs.
    """

    encoded_url = quote_plus(image_url)

    return {
        "google": (
            f"https://www.google.com/searchbyimage?image_url={encoded_url}"
        ),
        "yandex": (
            f"https://yandex.com/images/search?rpt=imageview&url={encoded_url}"
        ),

        "bing": (
            f"https://www.bing.com/images/search?q=imgurl:{encoded_url}&view=detailv2&iss=sbi"
        ),

        "tineye": (
            f"https://tineye.com/search?url={encoded_url}"
        ),

        "saucenao": (
            f"https://saucenao.com/search.php?url={encoded_url}"
        ),

        "iqdb": (
            f"https://iqdb.org/?url={encoded_url}"
        ),

        "pinterest": (
            f"https://www.pinterest.com/search/pins/?q={encoded_url}"
        ),

        "baidu": (
            f"https://graph.baidu.com/details?image={encoded_url}"
        ),

        "karmadecay": (
            f"https://karmadecay.com/search?q={encoded_url}"
        )
    }


def reverse_search(image_path: str):
    """
    Upload image and print reverse search links.
    """

    try:
        uploaded_url = upload_to_catbox(image_path)

        print(f"\n[+] Uploaded Successfully:")
        print(f"{uploaded_url}\n")

        links = generate_reverse_search_links(uploaded_url)
        return links

    except Exception as e:
        print(f"\n[-] Error: {e}")


if __name__ == "__main__":
    reverse_search(r".\images\sample.jpg")