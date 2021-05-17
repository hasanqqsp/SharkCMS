from django.db import models
from django.utils.text import slugify
from content.utils import generate_id
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=256)
class Article(models.Model):
    article_id = models.CharField(unique=True, primary_key=True,editable=True,max_length=16)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='approved_by')
    moderator_note = models.TextField(blank=True,null=True)
    status_changed_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True,related_name='status_changed_by')
    content = models.TextField()
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)
    
