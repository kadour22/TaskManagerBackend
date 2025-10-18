from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Challenge(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    is_done     = models.BooleanField(default=False)

    def __str__(self):
        return self.name