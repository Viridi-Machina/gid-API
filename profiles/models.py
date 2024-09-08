from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Profile model, taken from the DRF code institute tutorial ---------|
class Profile(models.Model):
    """
    Model for extending the default django user model.
    Allows for custom user profiles with profile images.
    """
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE
        )
    name = models.CharField(
        max_length=255, blank=True
        )
    title = models.CharField(
        max_length=255, blank=True
        )
    image = models.ImageField(
        upload_to='images/', default='../default_profile_bjwimv'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        """
        Order profiles based on time created
        """
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}'
    

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)