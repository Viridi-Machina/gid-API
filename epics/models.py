from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from tasks.models import Task

STATUS_CHOICES = (
    (1, 'To-do'),
    (2, 'In Progress'),
    (3, 'Completed'),
    (4, 'Backlog')
)

class Epic(models.Model):
    """
    Model for Epic creation.
    Relates to profile, user and task models.
    """
    title = models.CharField(max_length=255)
    image = models.ImageField( 
        upload_to='images/', default='../default_post_hu4wuf'
    )
    profile_list = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile_list'
        )
    task_list = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task_list'
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE
        )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Ordering for epic based on time created
        """
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'