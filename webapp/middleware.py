from re import compile

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

# compiles regex expressions that for paths that do not require
# authentication
EXEMPT_URLS = [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class AuthRequiredMiddleware(object):
    """
    Middleware that requires a user to be authenticated to access any views.
    Unauthenticated users will be redirected to the login page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            # gets the path after the slash
            path = request.path_info.lstrip('/')

            # checks if the path is in exempt urls
            if not any(m.match(path) for m in EXEMPT_URLS):
                # redirects to login page
                return HttpResponseRedirect(reverse('account_login'))
        # user is authenticated, allow through
        return self.get_response(request)
