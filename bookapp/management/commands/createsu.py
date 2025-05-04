from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Create default superuser if not exists"

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='1234'
            )
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created"))
        else:
            self.stdout.write("Superuser already exists")
