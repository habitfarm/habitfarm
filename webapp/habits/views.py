from datetime import (
    datetime,
    timedelta,
)
import json

from colorful.widgets import ColorFieldWidget
from django.contrib import messages
from django import forms
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from webapp.models import (
    LogEntry,
    Habit,
)


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'
    format = '%m/%d/%Y %H:%M'
    input_formats = ('%m/%d/%Y %H:%M',)


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'color', 'schedule', 'description', ]
        widgets = {
            'color': ColorFieldWidget()
        }


class LogEntryForm(forms.ModelForm):
    note = forms.TextInput(attrs={'required': False})
    logged = forms.DateTimeField(
        label='When did you do it?',
        widget=DateTimeInput(),
    )

    class Meta:
        model = LogEntry
        fields = ['logged', 'note', ]
        widgets = {
            'logged': DateTimeInput(),
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
    habit_create_form = HabitForm()
    log_entry_create_form = LogEntryForm()
    today = datetime.now()
    context = {
        'habits': habits,
        'habit_create_form': habit_create_form,
        'log_entry_create_form': log_entry_create_form,
        'today': today,
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


def calendar(request):
    """
    For bootstrap-calendar to get calendar 'events' in their specifed
    format.
    see: https://github.com/Serhioromano/bootstrap-calendar#feed-url
    """
    log_entries_json = {
        'success': 1,
        'result': [],
    }

    if request.GET:
        # extract start/end dates from bootstrap calendar request
        start = int(request.GET.get('from'))
        end = int(request.GET.get('to'))

        # convert millisecond timestamps to datetime objects
        if start and end:
            start = datetime.fromtimestamp(start/1000)
            end = datetime.fromtimestamp(end/1000)
        else:
            # default to last two months
            end = timezone.now()
            start = end - timedelta(months=2)

        habit_ids = Habit.objects.filter(user=request.user)
        habit_ids = habit_ids.values_list('id', flat=True)
        log_entries = LogEntry.objects.filter(
            habit_id__in=habit_ids,
            logged__gte=start,
            logged__lte=end,
        )

        # FIXME: timezone are hard and time is short so we're just
        # assuming PST for now...
        OFFSET_HOURS = timedelta(hours=7)
        DURATION = timedelta(hours=1)

        # create list of log entries and convert to json
        for log_entry in log_entries:
            # bootstrap-calendar needs a start/end time so
            # make it arbitrarily an hour in length
            logged_start = log_entry.logged + OFFSET_HOURS
            logged_end = logged_start + DURATION

            # convert to milliseconds for bootstrap-calendar
            logged_start = int(logged_start.timestamp() * 1000)
            logged_end = int(logged_end.timestamp() * 1000)

            # get habit color for calendar icon
            color = log_entry.habit.color

            # add note to title if present
            title = log_entry.habit.name
            if log_entry.note:
                title += ': %s' % log_entry.note

            log_entries_json['result'].append({
                'id': log_entry.id,
                # 'title': log_entry.habit.name,
                'title': title,
                'start': logged_start,
                'end': logged_end,
                'style': 'background-color: %s;' % color,
            })

    log_entries_json = json.dumps(log_entries_json)
    return HttpResponse(log_entries_json, content_type='application/json')
