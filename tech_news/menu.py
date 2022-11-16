from tech_news.analyzer.search_engine import (
    # search_by_category,
    # search_by_tag,
    search_by_date,
    search_by_title,
)
from tech_news.scraper import get_tech_news

MENU = [
    "Popular o banco com notícias;",
    "Buscar notícias por título;",
    "Buscar notícias por data;",
    "Buscar notícias por tag;",
    "Buscar notícias por categoria;",
    "Listar top 5 notícias;",
    "Listar top 5 categorias;",
    "Sair.",
]


# Requisito 12
def analyzer_menu():
    print("Selecione uma das opções a seguir:")
    for ind, op in enumerate(MENU):
        print(f" {ind} - {op}")

    select = ""
    while select != 7:
        select = int(input("Digite sua opção: "))
        if 0 <= select < 7:
            REQUESTS[select]()


def get_news():
    qtde = int(input("Digite quantas notícias serão buscadas: "))
    get_tech_news(qtde)


def get_news_by_title():
    title = input("Digite o título: ")
    result = search_by_title(title)
    print(result)


def get_news_by_date():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    result = search_by_date(date)
    print(result)


REQUESTS = {
    0: get_news,
    1: get_news_by_title,
    2: get_news_by_date,
}


if __name__ == "__main__":
    analyzer_menu()
