from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import os
import json
from webapp.mailer.mailer import Mailer

from habitfarm.users.models import User


class Command(BaseCommand):
    help = 'Send email'

    def add_arguments(self, parser):
        parser.add_argument(
            '--test',
            help="Send a test email",
            action='store_true'
            )
        parser.add_argument(
            '--daily',
            help="Send daily emails",
            action='store_true'
            )
        parser.add_argument(
            '--weekly',
            help="Send weekly emails",
            action='store_true'
            )
        parser.add_argument(
            '--monthly',
            help="Send monthly emails",
            action='store_true'
            )
        parser.add_argument(
            '--yearly',
            help="Send yearly emails",
            action='store_true'
            )

    def mailer_wrapper(self):
        pass

    def handle(self, *args, **options):
        print('Sending ', end='')
        # user = User

        if options['test']:
            print('a test email')
            mail_data = {
                'account': settings.MAILGUN_ACCOUNT,
                'key': settings.MAILGUN_KEY,
                'url': 'https://api.mailgun.net/v3/{0}.mailgun.org/messages'.format(
                    settings.MAILGUN_ACCOUNT
                    ),
                'addr_from': "habitfarm.app<habitfarm.app@{0}.mailgun.org>".format(
                    settings.MAILGUN_ACCOUNT
                    ),
                'addr_to': 'bigpow@gmail.com',
                'mail_subject': 'Test Email',
                'mail_text': 'This is a test email',
                'mail_html': open(
                    'webapp/mailer/templates_email/slate/Stationery/stationery.html',
                    'r'
                    ).read(),
                'test_only': False,
            }

            mailer = Mailer(**mail_data)
            mailer.send()
            self.stdout.write(
                self.style.SUCCESS('Sent = {}'.format(mailer.success))
            )

        elif options['daily']:
            print('daily emails')

        elif options['weekly']:
            print('weekly emails')

        elif options['monthly']:
            print('monthly emails')

        elif options['yearly']:
            print('yearly emails')

        return

