from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from colorfield.fields import ColorField

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    schedule = models.CharField(
        default='daily',
        max_length = 20,
        choices = [
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
        max_length = 20,
        choices = [('open', 'Open'), ('achieved', 'Achieved'),],
    )
    color = ColorField(
        max_length=100,
        default='#663399',
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

class LogEntry(models.Model):
    note = models.TextField(null=True)
    logged = models.DateTimeField(
        null=False,
        blank=False,
    )
    created = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(
        Habit,
        on_delete = models.CASCADE,
    )
