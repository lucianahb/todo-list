from django.db import models
from .choices import ACTIVITY_CHOICES, PRIORITY_CHOICES, STATUS_CHOICES
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)


class Activity(models.Model):
    choices = models.CharField(max_length=64, choices=ACTIVITY_CHOICES)
    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False, null=False, blank=False)
    responsible_user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=64, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=64, choices=STATUS_CHOICES)
