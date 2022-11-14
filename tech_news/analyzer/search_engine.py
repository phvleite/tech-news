from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": f"{title}", "$options": "i"}}
    result = search_news(query)
    news_result = []
    for new in result:
        news_result.append((new["title"], new["url"]))
    return news_result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    news = search_by_title("gates")
    for new in news:
        print(new)
