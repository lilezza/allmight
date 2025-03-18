from django.contrib.auth.management.commands.createsuperuser import Command as BaseCommand
from django.core.management import CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--first_name', type=str, help="First name of the superuser")
        parser.add_argument('--last_name', type=str, help="Last name of the superuser")
        parser.add_argument('--phone_number', type=str, help="Phone number of the superuser")

    def handle(self, *args, **options):
        first_name = options.get('first_name')
        last_name = options.get('last_name')
        phone_number = options.get('phone_number')

        if not first_name:
            raise CommandError('You must provide a first name using --first_name')
        if not last_name:
            raise CommandError('You must provide a last name using --last_name')
        if not phone_number:
            raise CommandError('You must provide a phone number using --phone_number')

        options['first_name'] = first_name
        options['last_name'] = last_name
        options['phone_number'] = phone_number

        super().handle(*args, **options)
