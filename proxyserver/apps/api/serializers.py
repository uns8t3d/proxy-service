from rest_framework import serializers
from proxyserver.apps.core.models import Proxy


class ProxySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proxy
        fields = ('pk', 'ip_address', 'port', 'connect_type', 'status', 'anonymity', 'ping', 'last_checked')
