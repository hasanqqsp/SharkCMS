from django.db import models
from django.contrib.auth.models import User,Group

from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_uploads/')
    role = models.JSONField(default=list('moderator'))
    bio = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now_add=True)
    
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
    def __str__(self):
        return self.user.username