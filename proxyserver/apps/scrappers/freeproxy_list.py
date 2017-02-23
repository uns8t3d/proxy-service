import requests
from bs4 import BeautifulSoup
from .tools import is_ip


def scrap_freeproxy_list():
    proxies = []
    urls = ["https://free-proxy-list.net/"]
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        sip = soup.find_all("div", {"class": "col-md-2 td"})
        ip = []
        for list in sip:
            if is_ip(str(list.text)):
                ip.append(
                    list.text
                )

        s_port = soup.find_all("div", {"class": "col-md-1 td"})
        port = []
        port_list = []
        for list in s_port:
            port.append(list.text)

        for i in range(2, len(port), 4):
            port_list.append(port[i])

        anonymity_list = []
        for i in range(1, len(port), 4):
            if port[i] == "Да":
                anonymity = True
            else:
                anonymity = False
            anonymity_list.append(anonymity)

        s_country = soup.find_all("div", {"class": "col-md-4 td"})
        country = []
        country_list = []
        for list in s_country:
            country.append(list.text)

        for list in country:
            country.append(list[-3:-1])
            country_list.append(country)

        for i in range(10):
            proxies.append({
                'ip': ip[i],
                'port': port_list[i],
                'connection_type': "-",
                'anonymity': anonymity_list[i],
                'country': country_list[i]
            })
    return proxies