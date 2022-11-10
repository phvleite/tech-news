# Requisito 1
import requests
import time


def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(
            url, timeout=3, headers={"User-agent": "Fake user-agent"}
        )
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# if __name__ == "__main__":
#     for ind in range(1):
#         print(ind)
#         response1 = fetch("https://blog.betrybe.com/")
#         print(f"1 - {response1}")
#         response2 = fetch("http://httpbin.org/delay/2")
#         print(f"2 - {response2}")
#         response3 = fetch("http://httpbin.org/status/404")
#         print(f"3 - {response3}")
