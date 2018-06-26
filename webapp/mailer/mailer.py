import urllib.request
import urllib.parse


class Mailer(object):
    """
    Mailer class wrapper for MailGun API

    Parameters:
    ===========
    {
        'account': '',
        'key': '',
        'url': '',
        'addr_from': '',
        'addr_to': '',
        'mail_subject': '',
        'mail_text': '',
        'mail_html': '',
        'test_only': <bool>,
    }
    """

    def __init__(self, **kwargs):
        # Mail data
        self.account = kwargs['account']
        self.key = kwargs['key']
        self.url = kwargs['url']
        self.addr_from = kwargs['addr_from']
        self.addr_to = kwargs['addr_to']
        self.mail_subject = kwargs['mail_subject']
        self.mail_text = kwargs['mail_text']
        self.mail_html = kwargs['mail_html']
        # Test only
        self.test_only = kwargs['test_only']
        # Delivery status
        self.success = False
        self.d = None

    def send(self):
        """Sends an email"""
        self.success = False
        data = urllib.parse.urlencode(
            {
                "from": self.addr_from,
                "to": self.addr_to,
                "subject": self.mail_subject,
                "text": self.mail_text,
                "html": self.mail_html,
            }
        )
        data = data.encode('ascii')
        auth_handler = urllib.request.HTTPBasicAuthHandler()
        auth_handler.add_password(
            user="api",
            realm='MG API',
            passwd=self.key,
            uri=self.url
        )
        opener = urllib.request.build_opener(auth_handler)
        urllib.request.install_opener(opener)

        if self.test_only:
            print(self.url, data)

        else:
            try:
                self.d = urllib.request.urlopen(self.url, data)
            except Exception as e:
                print(e.message, e.args)

            # Checking the status
            # 200 : Successful delivery
            if self.d.code == 200:
                self.success = True


def main():
    """
    Mailer Test: Send test email
    - Command-line executed
    - Loads some vars from env
    """
    import os
    import json

    mail_data = {
        'account': os.getenv('MAILGUN_ACCOUNT'),
        'key': os.getenv('MAILGUN_KEY'),
        'url': 'https://api.mailgun.net/v3/{0}.mailgun.org/messages'.format(
            os.getenv('MAILGUN_ACCOUNT')
            ),
        'addr_from': "habitfarm.app<habitfarm.app@{0}.mailgun.org>".format(
            os.getenv('MAILGUN_ACCOUNT')
            ),
        'addr_to': os.getenv('MAILGUN_TO'),
        'mail_subject': 'Test Email',
        'mail_text': 'This is a test email',
        'mail_html': open(
            'templates_email/slate/Stationery/stationery.html',
            'r'
            ).read(),
        'test_only': False,
    }

    mailer = Mailer(**mail_data)
    mailer.send()
    print('Sent =', mailer.success)


if __name__ == "__main__":
    main()
