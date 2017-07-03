from django.db import models
from django_countries.fields import CountryField


class Proxy(models.Model):
    AVAILABLE = 'Available'
    UNREACHABLE = 'Unreachable'
    UNCHECKED = 'Unchecked'

    STATUS_CHOICES = (
        (AVAILABLE, "available"),
        (UNREACHABLE, "unreachable"),
        (UNCHECKED, "unchecked")
    )

    HTTP = 'HTTP'
    HTTPS = 'HTTPS'
    SOCKS4 = 'SOCKS4'
    SOCKS5 = 'SOCKS5'
    SSL = 'SSL'

    CONNECTION_TYPE_CHOICES = (
        (HTTP, "http"),
        (HTTPS, "https"),
        (SOCKS4, "socks4"),
        (SOCKS5, "socks5"),
        (SSL, "ssl")
    )

    id = models.AutoField(primary_key=True)
    ip_address = models.CharField(max_length=15, blank=False)
    port = models.IntegerField(blank=False)
    country = CountryField()
    connect_type = models.CharField(max_length=16, choices=CONNECTION_TYPE_CHOICES, default=HTTP)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=UNCHECKED)
    anonymity = models.BooleanField(default=False)
    ping = models.CharField(max_length=64, blank=True)
    last_checked = models.DateTimeField(blank=True)

    def __str__(self):
        return self.ip_address + ':' + str(self.port)

