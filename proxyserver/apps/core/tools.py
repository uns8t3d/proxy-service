import requests
import os
import pytz
import pygeoip
from datetime import datetime, timedelta

#from django.http import HttpResponse

from .models import Proxy

from proxyserver.apps.scrappers import free_proxy_sale, freeproxy_list, hide_me, httptunnel, proxylife, \
    proxyprivat, sslproxies

from django_countries import countries


def get_unchecked_proxies():
    unchecked_list = Proxy.objects.filter(last_checked__lt=datetime.now() - timedelta(minutes=5))
    return [unchecked_list[d:d + 50] for d in range(0, len(unchecked_list), 50)]


def check_proxy_for_available(proxies):
    for proxy in proxies:
        try:
            proxy_server = {"http": 'http://' + proxy.ip_address + ':' + str(proxy.port)}
            r = requests.get("http://google.com", proxies=proxy_server, timeout=5)
        except IOError:
            proxy.status = 'Unreachable'
            proxy.last_checked = datetime.now(pytz.timezone('Europe/Kiev'))
            proxy.ping = '-'
            proxy.save()
            continue
        if r.status_code == 200:
            proxy.status = 'Available'
            proxy.last_checked = datetime.now(pytz.timezone('Europe/Kiev'))
            # make ping test via bash
            ping = str(os.popen("ping -c1 %s | awk 'FNR == 2 { print $(NF-1) }'" % proxy.ip_address).read()) \
                .replace('time=', '')
            if ping != '':
                proxy.ping = ping + ' ms'
            else:
                proxy.ping = 'UD'

        else:
            proxy.status = 'Unreachable'
            # proxy.delete()
            proxy.save()

def take_proxy_from_scrapper(proxies):
    country_list = []
    for code, name in list(countries):
        country_list.append(code)
    for proxy in proxies:
        try:
            proxy_server = {"http": 'http://' + proxy['ip'] + ':' + str(proxy['port'])}
            requests.get("http://google.com", proxies=proxy_server, timeout=5)
        except IOError:
            print('Not working, maybe another time')
        else:
            if not Proxy.objects.filter(ip_address=proxy['ip'], port=proxy['port']).exists():
                country_code = get_country_by_ip(proxy['ip'])
                if country_code in country_list:
                    country = country_code
                else:
                    country = 'UD'
                Proxy.objects.create(ip_address=proxy['ip'],
                                     port=proxy['port'],
                                     country=country,
                                     connect_type=proxy['connection_type'].upper(),
                                     status='Available',
                                     anonymity=proxy['anonymity'],
                                     last_checked=datetime.now(pytz.timezone('Europe/Kiev')))


def call_scrappers():
    list_of_proxy = []
    try:
        for proxy in sslproxies.scrap_sslproxies():
            list_of_proxy.append(proxy)
    except Exception as e:
        pass
    try:
        for proxy in hide_me.scrap_hide_me():
            list_of_proxy.append(proxy)
    except Exception as e:
        pass
    try:
        for proxy in proxylife.scrap_proxylife():
            list_of_proxy.append(proxy)
    except Exception as e:
        pass
    try:
        for proxy in proxyprivat.scrap_proxyprivat():
            list_of_proxy.append(proxy)
    except Exception as e:
        pass
    try:
        for proxy in free_proxy_sale.scrap_free_proxy_sale():
            list_of_proxy.append(proxy)
    except Exception as e:
        pass
    try:
        for proxy in httptunnel.scrap_httptunnel():
            list_of_proxy.append(proxy)
    except Exception as e:
        pass
    return [list_of_proxy[d:d + 50] for d in range(0, len(list_of_proxy), 50)]


def get_country_by_ip(ip_address):
    path = './geoip/GeoIP.dat'
    gi = pygeoip.GeoIP(path)
    return gi.country_code_by_addr(ip_address)
