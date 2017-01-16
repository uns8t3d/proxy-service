from django.db import models
from django.contrib.auth.models import User
from proxyserver.apps.core.models import Proxy


class UserProxies(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='users proxy')
    proxy = models.ForeignKey(Proxy, verbose_name='Proxy for user', null=True)
