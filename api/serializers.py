from django.core import serializers
from content import models as content_models


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
    print(is_clap)
    if is_clap == "on":
        query.claps.add(request.user)
        query.save()
        query.clap_count = query.claps.all().count()
        query.save()
        
    if not is_clap:
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
    
    
    
   