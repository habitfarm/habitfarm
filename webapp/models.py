from django.db import models
from django.conf import settings
from colorful.fields import RGBColorField
from django.utils import timezone
from datetime import timedelta

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
        if self.habit.last_log_entry < self.logged:
            self.habit.last_log_entry = self.logged

        current_streak = self.current_streak()
        longest_streak = self.habit.longest_streak
        if current_streak > longest_streak:
            longest_streak = current_streak
        self.habit.current_streak = current_streak
        self.habit.longest_streak = longest_streak
        self.habit.save()

    def current_streak(self):
        current_streak = 0
        today = timezone.now().date()
        compareDate = today + timezone.timedelta(1)
        entry_dates = LogEntry.objects.filter(habit=self.habit).values_list('logged', flat=True).order_by('-logged')
        previous_date = None
        for date in entry_dates:
            date = date.date()
            if previous_date != date:
                delta = compareDate - date
                if delta.days == 1:
                    current_streak += 1
                elif delta.days == 0:
                    current_streak = 0
                else:
                    break

                    compareDate = date
            previous_date = date
        print("Look here")
        print(current_streak)
        return current_streak
