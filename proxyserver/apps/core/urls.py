from django.conf.urls import url
from proxyserver.apps.core.views import dashboard, ajax_get_country_list, ajax_get_proxy_list
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(dashboard), name='dashboard'),
    url(r'^ajax_get_proxy_list/$', login_required(ajax_get_proxy_list), name='get_proxy_list'),
    url(r'^ajax_get_country_list/$', login_required(ajax_get_country_list), name='get_country_list')
]
