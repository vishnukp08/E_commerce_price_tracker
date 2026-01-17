import requests
from bs4 import BeautifulSoup


def get_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    price_tag = soup.select_one("p.price_color")

    if price_tag:
        price_text = price_tag.text

        # Clean unwanted characters
        price_text = (
            price_text.replace("£", "")
            .replace("Â", "")
            .strip()
        )

        return float(price_text)

    return None
