from django.core.management.base import BaseCommand
from proxyserver.apps.core.models import Proxy


class Command(BaseCommand):
    '''
    this script is for make all ping fields with error status empty
    '''
    def handle(self, *args, **options):
        for p in Proxy.objects.all():
            p.ping = ''
            print(p.ip_address)
            p.save()
        print('DONE')


