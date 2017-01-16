import requests
import socket
from bs4 import BeautifulSoup


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


def throw_td(data):
    curr_ip = str(data).replace('<td>', '')
    curr_ip = curr_ip.replace('</td>', '')
    return curr_ip


def is_ip(address):
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False


def scrap_freeproxy_list():
    proxies = []
    urls = ["http://www.freeproxy-list.ru/", "http://www.freeproxy-list.ru/proxy-list/2"]
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


# def scrap_samair():
#     urls = []
#     proxies = []
#     r1 = requests.get('http://www.samair.ru/proxy/proxy-01.htm')
#     soup1 = BeautifulSoup(r1.content)
#
#     for a in soup1.find_all('a', href=True):
#         urls.append(a['href'])
#
#     del urls[0:12]
#     del urls[30:]
#
#     for url in urls:
#         r = requests.get('http://www.samair.ru/proxy/' + url)
#         soup = BeautifulSoup(r.content)
#
#         link = ''
#         for i in soup1.find_all('link'):
#             if ('/styles/' in i['href']):
#                 link = i['href']
#         r2 = requests.get("http://www.samair.ru" + link)
#         soup2 = BeautifulSoup(r2.content)
#         ip = []
#         classes_wrong = []
#         classes = []
#         anonymity = []
#
#         for i in soup.find_all('span'):
#             if (i.text[0].isdigit()):
#                 ip.append(i.text.replace(':', ''))
#                 classes_wrong.append(i['class'])
#
#         for i in classes_wrong:
#             classes.append(i[0])
#
#         for a in soup.find_all("tr"):
#             if ('anonymous ' or 'high-anonymous ') in a.text:
#                 anonymity.append(True)
#             elif 'transparent ' in a.text:
#                 anonymity.append(False)
#
#         p = str(soup2).split(".")
#         del p[0]
#
#         l1 = []
#         for i in p:
#             l1.append(i.split(":"))
#
#         l2 = []
#         for i in l1:
#             l2.append(i[0])
#             l2.append(i[2])
#
#         c_port = {}
#         class_port = []
#         ports = []
#         port2 = []
#         for i in l2:
#             if i[0] == 'r':
#                 class_port.append(i)
#             else:
#                 ports.append(i.replace('"', ''))
#
#         for i in range(len(ports)):
#             port2.append(ports[i].replace("}\n", ''))
#
#         for i in range(len(port2)):
#             c_port[class_port[i]] = port2[i]
#
#         port_list = []
#         for i in classes:
#             port_list.append(c_port[i])
#
#         for i in range(34):
#             proxies.append({
#                 'ip': ip[i],
#                 'port': port_list[i],
#                 'connection_type': "-",
#                 'anonymity': anonymity[i],
#                 'country': 'UD'
#             })
#
#     return proxies


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
            if server[5] == "Нет":
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


def scrap_free_proxy_sale():
    proxies = []
    fps = "http://free.proxy-sale.com"
    r = requests.get(fps)
    soup = BeautifulSoup(r.content)
    last_page = (int((soup.find_all("ul", {"class": "pagination"})[0]).find_all("li")[5].text))
    urls = []
    server = []
    for i in range(1, last_page):
        urls.append("http://free.proxy-sale.com/?pg=" + str(i))
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        server_rows = soup.find_all("tbody")[0].find_all("tr")
        for server_row in server_rows:
            for c in server_row.find_all("td"):
                server.append(c)
            port = (server[1].img['src']).replace('/imgport.php?port=', '')
            if "Анонимный" in server[3]:
                anonymity = True
            else:
                anonymity = False
            proxies.append({"ip": server[0].text,
                            "port": port,
                            "connection_type": server[5].text.upper(),
                            "anonymity": anonymity,
                            "country": server[2].text})
            server.clear()
    return proxies
