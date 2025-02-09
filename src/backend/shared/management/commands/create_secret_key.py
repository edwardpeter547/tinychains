import secrets
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generates a new SECRET_KEY for Django settings" 

    def handle(self, *args, **options):
        secret_key = secrets.token_urlsafe(50)
        self.stdout.write(self.style.SUCCESS(f"Generated SECRET_KEY: \n\n{secret_key}"))
    
