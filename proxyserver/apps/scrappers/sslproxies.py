import requests
from bs4 import BeautifulSoup
from .tools import is_ip, throw_td


def scrap_sslproxies():
    urls = ["https://free-proxy-list.net/", "http://www.sslproxies.org/", "http://www.us-proxy.org/",
            "http://free-proxy-list.net/uk-proxy.html", "http://www.socks-proxy.net/",
            "http://free-proxy-list.net/anonymous-proxy.html"]
    proxies = []
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        lists = soup.find_all("tr")

        for list in lists:
            if is_ip(str(throw_td(list.contents[0]))) and (str(throw_td(list.contents[1])).isdigit()):
                if str(throw_td(list.contents[6])) == 'yes':
                    connection_type = 'HTTPS'
                else:
                    connection_type = 'HTTP'

                if str(throw_td(list.contents[4])) == 'anonymous':
                    anonymity = True
                else:
                    anonymity = False

                proxies.append({
                    'ip': throw_td(list.contents[0]),
                    'port': throw_td(list.contents[1]),
                    'connection_type': connection_type,
                    'anonymity': anonymity,
                    'country': throw_td(list.contents[2])
                })
    return proxies