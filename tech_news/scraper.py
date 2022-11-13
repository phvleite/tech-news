# Requisito 1
import time

import requests
from parsel import Selector


def fetch(
    url: str, wait: int = 3, header: dict = {"User-agent": "Fake user-agent"}
) -> str:
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
    selector = Selector(text=html_content)
    news_url = selector.css("h2.entry-title a::attr(href)").getall()
    return news_url


# Requisito 3
def scrape_next_page_link(html_content: str) -> str:
    selector = Selector(text=html_content)
    next_url = selector.css("a.next.page-numbers::attr(href)").get()
    return next_url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("head link[rel*='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    title = title.split(" ")
    title = " ".join(title)
    timestamp = selector.css("li.meta-date::text").get()
    if len(timestamp) == 0:
        timestamp = selector.css("p.post-modified-info::text").get()[:10]
    writer = selector.css("a.url.fn.n::text").get()
    comments_count = selector.css("h5.title-block::text").re(r"\d")
    if len(comments_count) == 0:
        comments_count = 0
    else:
        comments_count = int(comments_count[0])
    category = selector.css("a.category-style > span.label::text").get()

    print(url, title, timestamp, writer, comments_count, category, sep=",")


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    # response = fetch("https://blog.betrybe.com/")
    # for new in scrape_novidades(response):
    #     print(new)
    # news = []
    # url = "https://blog.betrybe.com/"
    # while url:
    #     response = fetch(url)
    #     news.extend(scrape_novidades(response))
    #     url = scrape_next_page_link(response)
    #     print(url)
    URL_BASE = "https://blog.betrybe.com/"
    URL_EXTENSAO = (
        "carreira/tudo-sobre-tecnologia-da-informacao/"
    )
    URL_EXT = ""
    URL_EXTENSAO = URL_EXTENSAO + URL_EXT
    response = fetch(URL_BASE + URL_EXTENSAO)
    selector = Selector(text=response)
    url_current = selector.css("head link[rel*='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    title = title.split(" ")
    title = " ".join(title)
    timestamp = selector.css("li.meta-date::text").get()
    if len(timestamp) == 0:
        timestamp = selector.css("p.post-modified-info::text").get()[:10]
    writer = selector.css("a.url.fn.n::text").get()
    comments_count = selector.css("h5.title-block::text").re(r"\d")
    if len(comments_count) == 0:
        comments_count = 0
    else:
        comments_count = int(comments_count[0])
    category = selector.css("a.category-style > span.label::text").get()

    print(
        f"""
url - {url_current}
título - {title}
data - {timestamp}
escritor - {writer}
comentários - {comments_count}
categoria - {category}
"""
    )
