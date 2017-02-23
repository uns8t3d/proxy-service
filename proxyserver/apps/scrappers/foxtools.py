import requests
from bs4 import BeautifulSoup


def scrap_foxtools():
    try:
        proxies = []
        foxtools = "http://foxtools.ru/Proxy?page=1"
        rf = requests.get(foxtools)
        s = BeautifulSoup(rf.content)
        urls = [foxtools]
        last_page = int(s.find_all("div", {"class": "pager"})[0].find_all("a")[-1].text.replace("[", '').replace("]", ''))
        for i in range(1, last_page):
            urls.append("http://foxtools.ru/Proxy?page=" + str(i))
        for url in urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.content)
            server_rows = soup.find_all("tbody")[0].find_all("tr")
            server = []
            for server_row in server_rows:
                for c in server_row.find_all("td"):
                    server.append(c.text)
                if "низкая" in server[4]:
                    anonymity = False
                else:
                    anonymity = True
                proxies.append({"ip": server[1],
                                "port": server[2],
                                "connection_type": server[5],
                                "anonymity": anonymity,
                                "country": server[3]})
                server.clear()
        return proxies
    except (''):
        print("foxtools failed")