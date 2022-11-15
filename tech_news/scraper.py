# Requisito 1
import time
import requests
import re
from parsel import Selector
from tech_news.database import create_news, find_news


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
def scrape_noticia(html_content: str) -> object:
    selector = Selector(text=html_content)

    news = {}

    url = selector.css("head link[rel='canonical']::attr(href)").get()
    news["url"] = url

    title = selector.css("h1.entry-title::text").get()
    title = title.strip()
    news["title"] = title

    timestamp = selector.css("li.meta-date::text").get()
    if timestamp:
        if len(timestamp) == 0:
            regex_data = r"([0-9]{2}/[0-9]{2}/[0-9]{4})"
            timestamp = re.search(
                regex_data, selector.css("p.post-modified-info::text").get()
            )
        news["timestamp"] = timestamp

    writer = selector.css("a.url.fn.n::text").get()
    news["writer"] = writer

    comments_count = selector.css("h5.title-block::text").re(r"\d")
    if len(comments_count) == 0:
        comments_count = 0
    else:
        comments_count = int(comments_count[0])
    news["comments_count"] = comments_count

    summary = selector.css(
        "div.entry-content > p:nth-of-type(1) *::text"
    ).getall()
    summary = "".join(summary)
    summary = summary.strip()
    news["summary"] = summary

    tags = selector.css("section.post-tags > ul > li > a::text").getall()
    news["tags"] = tags

    category = selector.css("a.category-style > span.label::text").get()
    news["category"] = category

    return news


# Requisito 5
def get_tech_news(amount: int) -> list:
    list_news = []
    url_news = []
    URL = "https://blog.betrybe.com"
    while len(url_news) < amount and URL:
        page_html = fetch(URL)
        url_news.extend(scrape_novidades(page_html))
        if len(url_news) < amount:
            URL = scrape_next_page_link(page_html)

    for ind in range(len(url_news)):
        page_html_new = fetch(url_news[ind])
        new = scrape_noticia(page_html_new)
        list_news.append(new)

    create_news(list_news)
    db_news = find_news()
    return db_news


if __name__ == "__main__":
    URL_BASE = "https://blog.betrybe.com"
    URL_EXTENSAO = (
        "/bootstrap/"
    )
    # URL_EXTENSAO_PLUS = ""
    # response = fetch(URL_BASE + URL_EXTENSAO)
    # print(scrape_noticia(response))
    # db = get_tech_news(756)
    # db = find_news()
    # print(len(db))
    # print(db)
