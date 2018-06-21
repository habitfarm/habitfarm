from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# sample data for html click-through
habits = [
    {
        'name': 'Floss',
        'description': 'Dentist says I should do it, so I\'m gonna do it, damn it!',
        'currentStreak': 6,
        'schedule': 'days',
        'lastLogEntry': datetime.now(),
        'weeklyAverage': 3.2,
    },
    {
        'name': 'Go to the gym',
        'description': 'Gotta get back in shape.',
        'currentStreak': 0,
        'schedule': 'days',
        'lastLogEntry': datetime.now() - relativedelta(days=3),
        'weeklyAverage': 1.6,
    },
]


def habit_list(request):
    """
    Place holder for habits list view so we can do the html click-through.
    This view will eventually provide data for the main habits page.

    This is a function based view, but we may want to look into a
    django.views.generic.ListView class based view when we get our
    model going. An example can be found at
    habitfarm.users.views.UserListView
    """
    context = {
        'habits': habits,
    }
    return render(request, 'habits/habit_list.html', context)


def habit_create(request):
    """
    Place holder for habits create view so we can do the html click-through.
    This will eventually validate the form and add a new Habit object.

    This is a function based view, but we may want to look into a
    django.views.generic.CreateView class based view when we get our model
    going.
    """
    if request.POST:
        habits.append({
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'schedule': request.POST.get('schedule'),
            'currentStreak': 0,
            'lastLogEntry': '-',
            'weeklyAverage': '-',
        })
        messages.success(request, 'Habit added!')
        return HttpResponseRedirect(reverse('webapp:habits:list'))
    else:
        return render(request, 'habits/habit_create.html')
