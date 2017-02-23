import socket


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
