# import requests
# from bs4 import BeautifulSoup
#
#
# def scrap_free_proxy_sale():
#     proxies = []
#     fps = "http://free.proxy-sale.com"
#     r = requests.get(fps)
#     soup = BeautifulSoup(r.content)
#     last_page = (int((soup.find_all("ul", {"class": "pagination"})[0]).find_all("li")[5].text))
#     urls = []
#     server = []
#     for i in range(1, last_page):
#         urls.append("http://free.proxy-sale.com/?pg=" + str(i))
#     for url in urls:
#         r = requests.get(url)
#         soup = BeautifulSoup(r.content)
#         server_rows = soup.find_all("tbody")[0].find_all("tr")
#         for server_row in server_rows:
#             for c in server_row.find_all("td"):
#                 server.append(c)
#             port = (server[1].img['src']).replace('/imgport.php?port=', '')
#             if "Anonimous" in server[3]:
#                 anonymity = True
#             else:
#                 anonymity = False
#             proxies.append({"ip": server[0].text,
#                             "port": port,
#                             "connection_type": server[5].text.upper(),
#                             "anonymity": anonymity,
#                             "country": server[2].text})
#             server.clear()
#     return proxies
