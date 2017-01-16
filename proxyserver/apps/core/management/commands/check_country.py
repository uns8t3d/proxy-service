from django.core.management.base import BaseCommand
from proxyserver.apps.core.models import Proxy
from proxyserver.apps.core.tools import get_country_by_ip


class Command(BaseCommand):
    '''
    this script is for make all ping fields with error status empty
    '''
    def handle(self, *args, **options):
        for p in Proxy.objects.filter(country='UD'):
            p.country = get_country_by_ip(p.ip_address)
            print(p.country)
            p.save()
        print('DONE')


