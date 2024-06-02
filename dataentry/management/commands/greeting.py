from django.core.management.base import BaseCommand 


class Command(BaseCommand):
    help = "Greets the User"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies User name')


    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f"Hi {name}, GM"
        self.stdout.write(self.style.SUCCESS(greeting))