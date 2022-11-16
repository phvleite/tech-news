from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_tag,
    search_by_date,
    search_by_title,
)
from tech_news.analyzer.ratings import (
    top_5_news,
    top_5_categories,
)
from tech_news.scraper import get_tech_news
import sys


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
OPTIONS = [str(n) for n in range(7)]


# Requisito 12
def analyzer_menu():
    print("Selecione uma das opções a seguir:")
    for ind, op in enumerate(MENU):
        print(f" {ind} - {op}")

    select = input("Digite sua opção:\n")
    if select in OPTIONS:
        REQUESTS[select]()
    elif select != "7":
        print("Opção inválida", file=sys.stderr)
    elif select == "7":
        print("Encerrando script\n")


def get_news():
    qtde = int(input("Digite quantas notícias serão buscadas:\n"))
    get_tech_news(qtde)


def get_news_by_title():
    title = input("Digite o título:\n")
    result = search_by_title(title)
    for new in result:
        print(f"Notícia: {new[0]}\nURL....: {new[1]}\n")


def get_news_by_date():
    date = input("Digite a data no formato aaaa-mm-dd:\n")
    result = search_by_date(date)
    for new in result:
        print(f"Notícia: {new[0]}\nURL....: {new[1]}\n")


def get_news_by_tag():
    tag = input("Digite a tag:\n")
    result = search_by_tag(tag)
    for new in result:
        print(f"Notícia: {new[0]}\nURL....: {new[1]}\n")


def get_news_by_category():
    category = input("Digite a categoria:\n")
    result = search_by_category(category)
    for new in result:
        print(f"Notícia: {new[0]}\nURL....: {new[1]}\n")


def get_top_5_news():
    result = top_5_news()
    for new in result:
        print(new)


def get_top_5_news_by_category():
    result = top_5_categories()
    for new in result:
        print(new)


REQUESTS = {
    "0": get_news,
    "1": get_news_by_title,
    "2": get_news_by_date,
    "3": get_news_by_tag,
    "4": get_news_by_category,
    "5": get_top_5_news,
    "6": get_top_5_news_by_category,
}
