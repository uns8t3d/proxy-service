from django.contrib import admin
from .models import UserProxies


class UserProxiesAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'proxy_id']
    list_filter = ('user_id', 'proxy_id')


admin.site.register(UserProxies, UserProxiesAdmin)
