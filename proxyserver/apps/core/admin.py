from django.contrib import admin
from .models import Proxy


class ProxyAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'port', 'country', 'connect_type', 'status', 'anonymity', 'last_checked']
    list_filter = ('ip_address', 'port', 'country', 'connect_type', 'status', 'anonymity')
    search_fields = ['ip_address', 'country', 'connect_type']

admin.site.register(Proxy, ProxyAdmin)
