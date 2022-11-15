from tech_news.database import search_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    query = {"comments_count": {"$gt": 0}}
    news_top_5 = []
    result = search_news(query)
    new_result = sorted(
        result, key=itemgetter("comments_count", "title"), reverse=True
    )

    if len(new_result) > 5:
        for ind in range(5):
            news_top_5.append(
                (new_result[ind]["title"], new_result[ind]["url"])
            )
    elif len(new_result) > 0:
        for ind in range(len(new_result)):
            news_top_5.append(
                (new_result[ind]["title"], new_result[ind]["url"])
            )

    return news_top_5


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    # top_5 = top_5_news()
    # for new in top_5:
    #     print(new)
    pass
