from datetime import datetime
from webapp.models import Habit
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from webapp.models import LogEntry, Habit
from django.forms import ModelForm

class HabitForm(ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'color', 'schedule', 'description',]

class LogEntryForm(ModelForm):
    class Meta:
        model = LogEntry
        fields= ['note', 'logged',]

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
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, 'Habit added!')
        return HttpResponseRedirect(reverse('webapp:habits:list'))
    else:
        form = HabitForm()

    context = {
        'form': form,
    }
    return render(request, reverse('webapp:habits:list'), context)

def log_entry_create(request, habit_id):
    if request.POST:
        form = LogEntryForm(request.POST)
        if form.is_valid():
            logentry = form.save(commit=False)
            form.save()
            messages.success(request, 'Logged entry for %s!' % habit.name)
        return HttpResponseRedirect(reverse('webapp:habits:list'))    
    else:
        form = LogEntryForm()

    context = {
        'form': form
    }
    return render(request, reverse('webapp:habits:list'), context)
