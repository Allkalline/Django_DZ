from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Create a new client'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone_number', type=str, help='Client phone number')
        parser.add_argument('address', type=str, help='Client address')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        phone_number = kwargs['phone_number']
        address = kwargs['address']

        client = Client(name=name, email=email, phone_number=phone_number, address=address)

        client.save()

        self.stdout.write(f'{client} created')