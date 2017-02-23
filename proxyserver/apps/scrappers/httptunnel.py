import requests
from bs4 import BeautifulSoup


def scrap_httptunnel():
    proxies = []
    r = requests.get("http://www.httptunnel.ge/ProxyListForFree.aspx")
    soup = BeautifulSoup(r.content)
    list_ip_port = []
    ip = []
    port = []
    anon = []
    anonymity = []

    for i in soup.find_all('a', {'target': '_new'}):
        for l in i:
            list_ip_port.append(l.split(":"))

    for i in list_ip_port:
        ip.append(i[0])
        port.append(i[1])

    for i in soup.find_all('a', {'align': 'center'}):
        if (i.text):
            if (i.text[0].isalpha()):
                anon.append(i.text[0])

    for i in anon:
        if (i == 'A' or 'E'):
            anonymity.append(True)
        else:
            anonymity.append(False)

    for i in range(100):
        proxies.append({
            'ip': ip[i],
            'port': port[i],
            'connection_type': "-",
            'anonymity': anonymity[i],
            'country': 'UD'
        })
    return proxies