from tech_news.database import search_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    query = {"comments_count": {"$gt": 0}}
    news_top_5 = []
    result = search_news(query)
    new_result = multisort(
        result, (("comments_count", True), ("title", False))
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
    query = {}

    categories = {}
    categories_top_5 = []
    result = search_news(query)

    for category in result:
        if category["category"] not in categories:
            categories[category["category"]] = 0
        categories[category["category"]] += 1

    for chave in categories.keys():
        categories_top_5.append(
            {"category": chave, "qtde": categories[chave]}
        )

    order_list = multisort(
        categories_top_5, (("qtde", True), ("category", False))
    )

    list_categories_top_5 = qtd_top_categories(order_list)

    return list_categories_top_5


# solução encontrada em: https://docs.python.org/pt-br/dev/howto/sorting.html
# xs -> lista que se quer ordenar
# specs -> especificações - campo e ordem
def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=itemgetter(key), reverse=reverse)
    return xs


def qtd_top_categories(data):
    list_categories_top_5 = []
    count = 0
    for category in data:
        if count < 5:
            list_categories_top_5.append((category["category"]))
        count += 1

    return list_categories_top_5


if __name__ == "__main__":
    # top_5 = top_5_news()
    # for new in top_5:
    #     print(new)
    # result = top_5_categories()
    # print(result)
    # for category in result:
    #     print(category)
    pass
