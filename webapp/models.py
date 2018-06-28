from django.db import models
from django.conf import settings
from colorful.fields import RGBColorField


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
