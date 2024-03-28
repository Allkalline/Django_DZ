from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    def handle(self, *args, **options):
        Client.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted all clients'))