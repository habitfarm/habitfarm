import urllib.request
import urllib.parse


class Mailer(object):
    """
    Mailer class

    Keywords/parameters:
    ====================
    {
        'account': '',
        'key': '',
        'url': '',
        'addr_from': '',
        'addr_to': '',
        'mail_subject': '',
        'mail_text': '',
        'mail_html': '',
    }
    """

    def __init__(self, **kwargs):
        # Mail header
        self.account = kwargs['account']
        self.key = kwargs['key']
        self.url = kwargs['url']
        self.addr_from = kwargs['addr_from']
        # Mail data
        self.addr_to = kwargs['addr_to']
        self.mail_subject = kwargs['mail_subject']
        self.mail_text = kwargs['mail_text']
        self.mail_html = kwargs['mail_html']
        # Delivery status
        self.success = False

    def send_email(self):
        """Sends email"""
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
        d = urllib.request.urlopen(self.url, data)
        # Checking the status
        # ret_code = str(d.code) + " " + d.reason

        # 200 : Successful delivery
        if d.code == 200:
            self.success = True


def main():
    """
    Mailer Test: Send test email
    Command-line executed

    1) Load MailGun credentials:
        a) from json
        b) from env
    1') Load from address & URL
    2) Load email address to spam:
        a) from textfile
        b) from env
        * Otherwise, would be passed on from other module(s)
    3) Load dummy email data:
        a) from text
        b) from html
        * Otherwise, would be passed on from other module(s)
    4) Wrap the package (dictionary)
        mail_data = {
            'account': '',
            'key': '',
            'url': '',
            'addr_from': '',
            'addr_to': '',
            'mail_subject': '',
            'mail_text': '',
            'mail_html': '',
        }
    5) Send the package to mailer
    """
    DEBUG = False
    # 1) Load MailGun credentials:
    #     a) from json
    import json
    # with open('creds.json', 'r') as f:
    #     creds_json = json.load(f)
    # if DEBUG:
    #     print("{}:\n{}".format('creds.json', json.dumps(creds_json, indent=2)))
    #     b) from env
    import os
    creds_env = {
        'account': os.getenv('MAILGUN_ACCOUNT'),
        'key': os.getenv('MAILGUN_KEY')
    }
    if DEBUG:
        print("{}:\n{}".format('env', json.dumps(creds_env, indent=2)))

    # 1') Load from address & URL
    url = 'https://api.mailgun.net/v3/{0}.mailgun.org/messages'.format(
        creds_env['account']
    )
    addr_from = "user <user@{0}.mailgun.org>".format(creds_env['account'])

    # 2) Load email address to spam:
    #     a) from textfile
    # emailto_text = {
    #     'addr_to': open('mail_to.txt', 'r').read()
    # }
    # if DEBUG:
    #     print("{}:\n{}".format(
    #         'mail_to.txt',
    #         json.dumps(emailto_text, indent=2))
    #         )
    #     b) from env
    emailto_env = {
        'addr_to': os.getenv('MAILGUN_TO')
    }
    if DEBUG:
        print("{}:\n{}".format('env', json.dumps(emailto_env, indent=2)))

    # 3) Load dummy email data:
    #     a) from text
    mail_payload_text = {
        'mail_text': open('mail_payload_simple.txt', 'r').read()
    }
    if DEBUG:
        print("{}:\n{}".format(
            'mail_payload_simple.txt',
            json.dumps(mail_payload_text, indent=2))
        )
    # 3) Load dummy email data:
    #     b) from html
    mail_payload_html = {
        'mail_html': open('mail_payload_simple.html', 'r').read()
    }
    if DEBUG:
        print("{}:\n{}".format(
            'mail_payload_simple.html',
            json.dumps(mail_payload_html, indent=2))
        )

    # 4) Wrap the package
    mail_data = {
        'account': creds_env['account'],
        'key': creds_env['key'],
        'url': url,
        'addr_from': addr_from,
        'addr_to': emailto_env['addr_to'],
        'mail_subject': 'Test Email',
        'mail_text': '',
        'mail_html': mail_payload_html['mail_html'],
    }
    if DEBUG:
        print("{}:\n{}".format('mail_data', json.dumps(mail_data, indent=2)))

    # 5) Send the package to mailer
    mailer = Mailer(**mail_data)
    mailer.send_email()
    if 1:
        print('SENT =', mailer.success)


if __name__ == "__main__":
    main()
