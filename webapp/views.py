from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    if not request.user.is_authenticated:
        print('VIEW')
        return HttpResponseRedirect(reverse('account_login'))
    else:
        return HttpResponseRedirect(reverse('webapp:habits:list'))
