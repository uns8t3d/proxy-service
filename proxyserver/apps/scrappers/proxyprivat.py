import requests
from bs4 import BeautifulSoup


def scrap_proxyprivat():
    proxies = []
    proxyprivat = "http://proxyprivat.com/freeproxies"
    r = requests.get(proxyprivat)
    soup = BeautifulSoup(r.content)
    server_rows = soup.find_all("tbody")[0].find_all("tr")
    server = []
    for server_row in server_rows:
        for c in server_row.find_all("td"):
            server.append(c.text)
        ip_port = server[0].split(':')
        if "1" in server[4]:
            anonymity = False
        else:
            anonymity = True
        if 'SSL' in server[5]:
            connection_type = 'SSL'
        elif 'SOCKS4' in server[5]:
            connection_type = 'SOCKS4'
        elif 'SOCKS5' in server[5]:
            connection_type = 'SOCKS5'
        else:
            connection_type = 'HTTP'
        proxies.append({"ip": ip_port[0],
                        "port": ip_port[1],
                        "connection_type": connection_type,
                        "anonymity": anonymity,
                        "country": server[2]})
        server.clear()
    return proxies
