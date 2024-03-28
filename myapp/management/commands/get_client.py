from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Get client by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']

        client = Client.objects.get(pk=pk)

        self.stdout.write(f'Client: {client}')
