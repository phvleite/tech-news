import datetime

from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": f"{title}", "$options": "i"}}
    result = search_news(query)
    news_result = []
    for new in result:
        news_result.append((new["title"], new["url"]))
    return news_result


# Requisito 7
def search_by_date(date):
    news_result = []
    try:
        date_iso = datetime.date.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
    else:
        date_str_db = date_iso.strftime("%d/%m/%Y")
        query = {"timestamp": f"{date_str_db}"}
        result = search_news(query)
        for new in result:
            news_result.append((new["title"], new["url"]))
        return news_result


# Requisito 8
def search_by_tag(tag):
    cap_tag = tag.capitalize()
    query = {"tags": {"$all": [f"{cap_tag}"]}}
    result = search_news(query)
    news_result = []
    for new in result:
        news_result.append((new["title"], new["url"]))
    return news_result


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": f"{category}", "$options": "i"}}
    result = search_news(query)
    news_result = []
    for new in result:
        news_result.append((new["title"], new["url"]))
    return news_result


if __name__ == "__main__":
    # news = search_by_title("gates")
    # for new in news:
    #     print(new)
    # news = search_by_date("2021-04-04")
    # for new in news:
    #     print(new)
    # news = search_by_tag("tecnologia")
    # for new in news:
    #     print(new)
    # news = search_by_category("ferramentas")
    # for new in news:
    #     print(new)
    pass
