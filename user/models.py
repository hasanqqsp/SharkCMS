from django.db import models
from django.contrib.auth.models import User,Group

from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_uploads/',null=True,blank=True)
    is_writer = models.BooleanField(default = True)
    is_trusted_writer = models.BooleanField(default = False)
    is_moderator = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    is_disabled = models.BooleanField(default = False)
    is_muted = models.BooleanField(default = False)
    bio = models.TextField(blank=True, null=True)
    short_bio = models.CharField(blank=True, null=True, max_length=256)
    registered = models.DateTimeField(auto_now_add=True)
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
    def __str__(self):
        return self.user.username