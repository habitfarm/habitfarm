from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
# Django built-in send_mail function
from django.core.mail import send_mail

# Home made mailer
import os
import json
from webapp.mailer.mailer import Mailer

# From habit models
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
            '--reminder',
            help="Send reminder email(s)",
            action='store_true'
            )

    def sand_mail(self, addr_to, subject, m_text='', m_html=''):
        mail_data = {
            'account': settings.MAILGUN_ACCOUNT,
            'key': settings.MAILGUN_KEY,
            'url': 'https://api.mailgun.net/v3/{0}.mailgun.org/messages'.format(
                settings.MAILGUN_ACCOUNT
                ),
            'addr_from': "habitfarm.app<habitfarm.app@{0}.mailgun.org>".format(
                settings.MAILGUN_ACCOUNT
                ),
            'addr_to': addr_to,
            'mail_subject': subject,
            'mail_text': m_text,
            'mail_html': m_html,
            'test_only': False,
        }
        # print(json.dumps(mail_data, indent=4))
        mailer = Mailer(**mail_data)
        mailer.send()
        self.stdout.write(
            self.style.SUCCESS('Sent = {}'.format(mailer.success))
        )

    def handle(self, *args, **options):
        print('Sending ', end='')

        if options['test']:
            # send a test email
            print('a test email')
            # make email content
            addr_to = 'bigpow@gmail.com'
            subject = 'This is a test'
            m_text = 'This is a test'
            m_html = open(
                    'webapp/mailer/templates_email/slate/Stationery/stationery.html',
                    'r'
                    ).read()

            # send with mailgun sandbox
            self.sand_mail(addr_to, subject, m_text, m_html)

            # send with django email (mailgun domain smtp)
            # send_mail(subject, m_text, 'noreply@mg.habitfarm.io', [addr_to])

        elif options['reminder']:
            # send reminder emails
            print('reminders')

        return

