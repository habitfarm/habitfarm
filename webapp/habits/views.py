from datetime import datetime
from dateutil.relativedelta import relativedelta

from colorful.widgets import ColorFieldWidget
from django.contrib import messages
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webapp.models import (
    LogEntry,
    Habit,
)


class DateInput(forms.DateInput):
    input_type = 'date'


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'color', 'schedule', 'description', ]
        widgets = {
            'color': ColorFieldWidget()
        }


class LogEntryForm(forms.ModelForm):
    note = forms.TextInput(attrs={'required': False})

    class Meta:
        model = LogEntry
        fields = ['logged', 'note', ]
        widgets = {
            'logged': DateInput(),
        }


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
    recent_log_entries = LogEntry.objects.filter(
        habit__in=habits,
        logged__gt=datetime.now() - relativedelta(months=2),
    )
    habit_create_form = HabitForm()
    log_entry_create_form = LogEntryForm()
    context = {
        'habits': habits,
        'log_entries': recent_log_entries,
        'habit_create_form': habit_create_form,
        'log_entry_create_form': log_entry_create_form,
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
        'habit_create_form': form,
    }
    return render(request, reverse('webapp:habits:list'), context)


def log_entry_create(request, habit_id):
    if request.POST:
        habit = Habit.objects.get(id=habit_id)
        form = LogEntryForm(request.POST)
        if form.is_valid():
            log_entry = form.save(commit=False)
            log_entry.habit = habit
            form.save()
            messages.success(request, 'Logged entry for %s!' % habit.name)
        return HttpResponseRedirect(reverse('webapp:habits:list'))
    else:
        form = LogEntryForm()

    context = {
        'log_entry_create_form': form
    }
    return render(request, reverse('webapp:habits:list'), context)
