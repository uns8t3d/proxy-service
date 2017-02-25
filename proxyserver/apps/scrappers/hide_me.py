import requests
from bs4 import BeautifulSoup


def scrap_hide_me():
    proxies = []
    hide_me = "http://hideme.ru/proxy-list/"
    rh = requests.get(hide_me)
    s = BeautifulSoup(rh.content)
    pages = s.find_all("div", {"class": "proxy__pagination"})[0].find_all("a")
    urls = []
    server = []
    for page in pages:
        if ('http://hideme.ru/' + page.get("href")) not in urls:
            urls.append('http://hideme.ru/' + page.get("href"))
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        server_rows = soup.find_all("tr")
        for server_row in server_rows[1:]:
            for c in server_row.find_all("td"):
                server.append(c.text)
            if server[5] == "No":
                anonymity = False
            else:
                anonymity = True
            proxies.append({"ip": server[0],
                            "port": server[1],
                            "connection_type": server[4],
                            "anonymity": anonymity,
                           "country": server[2]})
            server.clear()
    return proxies
