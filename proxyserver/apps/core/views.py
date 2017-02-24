from django.shortcuts import render

from .models import Proxy
import json
from django.http import HttpResponse
from django_countries import countries


def dashboard(request):
    return render(request, 'dashboard.html')


def ajax_get_proxy_list(request):
    proxy_list = Proxy.objects.all()
    counter = 0
    ajax_response = {"sEcho": 10, "aaData": [],
                     'iTotalRecords': counter,
                     'iTotalDisplayRecords': counter}
    for proxy in proxy_list:
        counter += 1
        ajax_response['aaData'].append([
            proxy.ip_address,
            proxy.port,
            str(proxy.country.name),
            proxy.connect_type.upper(),
            proxy.status,
            proxy.anonymity,
            proxy.ping,
            proxy.last_checked.strftime('%d-%m-%Y - %H:%M:%S'),
        ])
    ajax_response['iTotalRecords'] = counter
    ajax_response['iTotalDisplayRecords'] = counter
    return HttpResponse(json.dumps(ajax_response), content_type='application/json')


def ajax_get_country_list(request):
    country_list = []
    for name in list(countries):
        country_list.append(name[1])
    return HttpResponse(json.dumps(country_list))
