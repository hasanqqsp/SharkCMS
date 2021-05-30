from django.core import serializers
from rest_framework import serializers as rf_serializers
from content import models as content_models
from user.models import UserProfile
from django.contrib.auth.models import User
def getFavoriteArticle(count):
    query = content_models.Article.objects.filter(is_published=True).order_by('-clap_count')[:count]
    return serializers.serialize('json',query)
    
def getNewestArticle(count):
    query = content_models.Article.objects.filter(is_published=True).order_by('-published_on')[:count]
    return serializers.serialize('json',query)
    
def getClapsInfo(request,id):
    query = content_models.Article.objects.get(article_id=id)
    is_clap = query.claps.filter(id=request.user.id).exists()
    clap_count = query.clap_count
    return {"data":{
        "is_clap" : is_clap,
        "clap_count" : clap_count
    }}
    
def giveClaps(request,id, is_clap):
    query = content_models.Article.objects.get(article_id=id)
    
    if is_clap == "on":
        query.claps.add(request.user)
        query.save()
        query.clap_count = query.claps.all().count()
        query.save()
        
    if is_clap == 'null':
        query.claps.remove(request.user)
        query.save()
        print(query.claps.all())
        query.clap_count = query.claps.all().count()
        query.save()
        
    clap_count = query.clap_count
    return {"data":{
        "is_clap" : is_clap,
        "clap_count" : clap_count
    }}    
    

class UserProfileSerializer(rf_serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'

class AuthorSerializer(rf_serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(rf_serializers.ModelSerializer):
    class Meta:
        model = content_models.Category
        fields = '__all__'

class ArticleSerializer(rf_serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    author  = AuthorSerializer()
    approved_by = AuthorSerializer()
    status_changed_by = AuthorSerializer()
    
    class Meta:
        model = content_models.Article
        fields = '__all__'
        depth = 3
        many = True