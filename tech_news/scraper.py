# Requisito 1
import requests
import time
from parsel import Selector


def fetch(
    url: str, wait: int = 3, header: dict = {"User-agent": "Fake user-agent"}
) -> str:
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=wait, headers=header)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content: str) -> list:
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_url = selector.css("h2.entry-title a::attr(href)").getall()
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    response = fetch("https://blog.betrybe.com/")
    for new in scrape_novidades(response):
        print(new)
