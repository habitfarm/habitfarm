from django.core.management.base import BaseCommand, CommandError

import json
from webapp.mailer.mailer import Mailer


class Command(BaseCommand):
    help = 'Send email'

    def add_arguments(self, parser):
        parser.add_argument(
            'test',
            help="Send test email",
            nargs='+',
            type=str
            )

    def handle(self, *args, **options):
        self.stdout.write('Sending email')

        mail_data = json.loads(
            open('webapp/mailer/liam.tset', 'r+').read()[::-1]
            )

        mailer = Mailer(**mail_data)
        mailer.send()
        self.stdout.write(
            self.style.SUCCESS('Sent = {}'.format(mailer.success))
        )
