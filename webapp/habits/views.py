from datetime import datetime
from webapp.models import Habit
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def habit_list(request):
    """
    Place holder for habits list view so we can do the html click-through.
    This view will eventually provide data for the main habits page.

    This is a function based view, but we may want to look into a
    django.views.generic.ListView class based view when we get our
    model going. An example can be found at
    habitfarm.users.views.UserListView
    """
    habits = Habit.objects.filter(user=request.user)
    print(habits)
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
    habits = Habit.objects.filter(user=request.user)

    if request.POST:
        Habit.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            schedule=request.POST.get('schedule'),
            color=request.POST.get('color'),
        )

        messages.success(request, 'Habit added!')

    return HttpResponseRedirect(reverse('webapp:habits:list'))


def log_entry_create(request, habit_id):
    if request.POST:
        habit = Habit.objects.get(id=habit_id)
        LogEntry.objects.create(
            note=request.POST.get('note'),
            logged=request.POST.get('logged'),
            habit=habit,
        )
        messages.success(request, 'Logged entry for %s!' % habit.name)
    return HttpResponseRedirect(reverse('webapp:habits:list'))
