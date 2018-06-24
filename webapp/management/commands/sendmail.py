from django.core.management.base import BaseCommand, CommandError

from webapp.mailer.mailer import Mailer


class Command(BaseCommand):
    help = 'Send email'

    def add_arguments(self, parser):
        # intervals = [
        #     'daily',
        #     'weekly',
        #     'monthly',
        #     'yearly',
        #     'test'
        # ]
        parser.add_argument(
            'test',
            help="Send test email",
            nargs='+',
            type=str
            )

    def handle(self, *args, **options):
        self.stdout.write('Sending email')

        import json

        mail_data = json.loads(
            open('webapp/mailer/mail_data_bulk.json', 'r+').read()
            )
        if 0:
            print(json.dumps(mail_data, indent=2))

        mailer = Mailer(**mail_data)
        mailer.send_email()
        if 1:
            self.stdout.write(
                self.style.SUCCESS(
                    'Test email requested. SENT ={}'.format(
                        mailer.success
                    )
                )
            )

        # users = User.objects.get(all)
        # for user in users:
        #     send stf
