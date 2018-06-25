from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    current_streak = models.PositiveIntegerField()
    longest_streak = models.PositiveIntegerField()
    last_log_entry = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length = 20,
        choices = [('open', 'Open'), ('achieved', 'Achieved'),],
    )
    color = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

class LogEntry(models.Model):
    note = models.TextField()
    logged = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(
        Habit,
        on_delete = models.CASCADE,
    )
