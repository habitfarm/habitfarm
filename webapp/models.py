from django.db import models
from django.conf import settings
from colorful.fields import RGBColorField
from django.utils import timezone
from datetime import datetime, timedelta
import datetime

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        null=True,
        blank=True,
    )
    schedule = models.CharField(
        default='daily',
        max_length=20,
        choices=[
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
        ],
    )
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_log_entry = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[('open', 'Open'), ('achieved', 'Achieved'), ],
    )
    color = RGBColorField(
        default='#663399',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class LogEntry(models.Model):
    note = models.TextField(
        null=True,
        blank=True,
    )
    logged = models.DateTimeField(
        null=False,
        blank=False,
    )
    created = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def save(self):
        super().save()
        if not self.habit.last_log_entry:
            self.habit.last_log_entry = self.logged
        elif self.habit.last_log_entry < self.logged:
            self.habit.last_log_entry = self.logged


        current_streak = self.current_streak(LogEntry.objects.filter(habit=self.habit).values_list('logged', flat=True).order_by('-logged'))
        longest_streak = self.habit.longest_streak
        if current_streak > longest_streak:
            longest_streak = current_streak
        self.habit.current_streak = current_streak
        self.habit.longest_streak = longest_streak
        self.habit.save()

    def current_streak(self, object_list):
        def date_list_from_object_list(object_list):
            date_list = []
            for date_time in object_list:
                date_list.append(date_time.date())
            return date_list

        check_day = datetime.datetime.now().date()
        streak_unbroken = True

        current_streak = 0
        while streak_unbroken:
            if check_day in date_list_from_object_list(object_list):
                current_streak += 1
                streak_unbroken = True
            else:
                streak_unbroken = False

            check_day = check_day - timedelta(days=1)
        return current_streak
