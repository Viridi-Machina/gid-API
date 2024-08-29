from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from tasks.models import Task

STATUS = (
    (1, 'To-do'),
    (2, 'In Progress'),
    (3, 'Completed'),
    (4, 'Backlog')
)

class Task(models.Model):
    """
    Model for task creation.
    Lists tasks and assigned users.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    assigned_to = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='assignee'
        )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='profile_list'
        )
    status = models.IntegerField(STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_date = models.DateField

    class Meta:
        """
        Ordering for epic based on time created
        """
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'