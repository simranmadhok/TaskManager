import datetime
import os
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from .helpers import get_attachment_path

class TaskComments(models.Model):
    comments = models.TextField(
        null=True,
        blank=True
    )
    attachment = models.FileField(
        max_length=255,
        null=True,
        blank=True,
        upload_to=get_attachment_path
    )
    ckpt_date = models.DateTimeField(
        default=datetime.now
    )

    def __str__(self):
        return self.comments

    class Meta:
        verbose_name_plural = 'Task Comments'


class Task(models.Model):
    PRIORITY = (
        ('high','high'),
        ('medium','medium'),
        ('low','low')
    )
    title = models.CharField(
        max_length=120
    )
    date_created = models.DateField(
        default=timezone.now
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='User'
    )
    comment = models.OneToOneField(
        TaskComments,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comment'
    )
    date_due = models.DateField(
        default=timezone.now
    )
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY,
        default='medium'
    )
    completed = models.BooleanField(
        default=False
    )
    expired = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title
    
    def expired(self):
        if datetime.date.today() > self.date_due:
            return True

    class Meta:
        verbose_name_plural = 'Tasks'
        ordering = ['date_due']
