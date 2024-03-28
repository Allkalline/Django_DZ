from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Update client name by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='New client name')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        name = kwargs['name']

        client = Client.objects.get(pk=pk)
        client.name = name
        client.save()

        self.stdout.write(f'{client} updated')

