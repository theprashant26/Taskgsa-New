from django.db import models
from django.contrib.auth.models import User

status_choices = [
    ('Pending', 'Pending'),
    ('Working', 'Working'),
    ('Completed', 'Completed'),
]

class Task(models.Model):
    taskname = models.CharField(max_length=200, null=True)
    task_date = models.DateField()
    task_time = models.TimeField()
    assigned_by = models.CharField(max_length=200, null=True)
    task_status = models.CharField(max_length=200, null=True,choices=status_choices)