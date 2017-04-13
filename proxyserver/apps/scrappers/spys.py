import requests
from bs4 import BeautifulSoup


def Spys_ru():
    proxies = []
    proxies.append({"ip": get_ip(),
                            "port": get_port(),
                            "connection_type": get_connection_type(),
                            "anonymity": get_anonymity(),
                            "country": get_country()})
    return proxies


def get_ip():
    url = "http://spys.ru/en/free-proxy-list/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    links = soup.find_all("font", {"class": "spy14"})
    ip_list = []

    for i in links:
        if len(i) > 1:
            ip_list.append(i.contents[0])
    return ip_list


def get_port():
    url = "http://spys.ru/en/free-proxy-list/"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "lxml")

    link_port = soup.find_all("script", {"type": "text/javascript"})
    detail_link = link_port[2].contents[0]

    ports = {}
    splited = detail_link.split(';')
    for i in splited:
        val = i.split('=')
        if len(val[0]) > 5:
            ports[val[0]] = val[1][0]

    for i in link_port:
        val1 = soup.find_all('font', class_='spy14')[1].contents[1].contents[0].split('<\\/font>"+')[1].replace('(', '').replace(')', '').split('+')
        port = ''
        for j in val1:
            key = j[:6]
            port += str(ports[key])

    j = soup.find_all("font", {"class": "spy14"})

    port_list = []
    for i in j:
        try:
            port_str = ''
            a = i.contents[1].text[44:-1].split('+')
            for k in a:
                port_str += ports[k[1:-6]]

            port_list.append(port_str)

        except IndexError:
            continue
    return port_list


def get_connection_type():
    url = "http://spys.ru/en/free-proxy-list/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    link_type = soup.find_all("a", {"href": ["/en/https-ssl-proxy/", "/en/http-proxy-list/", "/en/socks-proxy-list", "/en/socks-proxy-list/"]})
    link_type.pop(0)
    detail_link = []
    list_connection_type = []

    for i in link_type:
        detail_link.append(i.find_all("font", {"class": ["spy1", "spy14"]}))

    for i in detail_link:
        if len(i) > 1:
            list_connection_type.append('%s%s' % (i[0].contents[0], i[1].contents[0]))
        elif len(i) == 0:
            continue
        else:
            list_connection_type.append(i[0].contents[0])
    return list_connection_type


def get_anonymity():
    url = "http://spys.ru/en/free-proxy-list/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    links = soup.find_all("a", {"href": ["/en/anonymous-proxy-list/", "/en/non-anonymous-proxy-list/"]})
    links.pop(0)
    links.pop(0)
    anonymity_list = []

    for i in links:
        anonymity_list.append(i.find_all("font")[0].contents[0])
    return anonymity_list


def get_country():
    url = "http://spys.ru/en/free-proxy-list/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    links = soup.find_all("font", {"class": "spy14"})
    country_list = []

    for i in links:
        if is_country(i.contents[0]):
            country_list.append(i.contents[0])
    country_list.pop(0)
    return country_list


def is_country(country):
    int_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if len(country) > 2 and (country[0] not in int_list):
        return True
    else:
        return False

print(Spys_ru())