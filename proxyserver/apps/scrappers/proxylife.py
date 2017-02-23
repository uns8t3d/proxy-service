import requests
from bs4 import BeautifulSoup


def scrap_proxylife():
    proxies = []
    proxylife = "http://proxylife.org/proxy/"
    r = requests.get(proxylife)
    soup = BeautifulSoup(r.content)
    server_rows = (soup.find_all("table")[1]).find_all("tr")[3:]
    server = []
    for server_row in server_rows:
        for c in server_row.find_all("td"):
            server.append(c)
        country = (server[4].img['src']).replace('images/flags/', '').replace('.gif%20', '')
        ip_port = server[0].text.split(':')
        if "elite" in server[1].text:
            anonymity = True
        else:
            anonymity = False
        proxies.append({"ip": ip_port[0].replace('\n', ''),
                        "port": ip_port[1],
                        "connection_type": server[2].text.upper(),
                        "anonymity": anonymity,
                        "country": country})
        server.clear()
    return proxies