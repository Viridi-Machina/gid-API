from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

STATUS_CHOICES = (
    ('TODO', 'To-do'),
    ('IPRO', 'In Progress'),
    ('COMP', 'Completed'),
    ('BLOG', 'Backlog')
)

PRIORITY_CHOICES = (
    ('LOW', 'LOW'),
    ('MED', 'MEDIUM'),
    ('HGH', 'HIGH')
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
    # profile_list = models.ForeignKey(
    #     Profile, on_delete=models.CASCADE, related_name='profile_list'
    #     )
    # task_list = models.ForeignKey(
    #     Task, on_delete=models.CASCADE, related_name='task_list'
    #     )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE
        )
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default=1
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Ordering for epic based on time created
        """
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'
    

class Task(models.Model):
    """
    Model for task creation.
    Relates to profile and user models.
    """
    epic = models.ForeignKey(
        Epic, on_delete=models.CASCADE, related_name='tasks'
        )
    title = models.CharField(
        max_length=255
        )
    description = models.TextField(
        max_length=255, blank=True, null=True
        )
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assignee'
        )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE
        )
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default=1
        )
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=1
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_date = models.DateField(null=True)

    class Meta:
        """
        Ordering for task based on epic, then time created
        """
        ordering = ['-epic', '-created_at']

    def __str__(self):
        return f'{self.epic}: {self.title}'