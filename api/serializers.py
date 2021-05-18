from django.core import serializers
from content import models as content_models

def getFavoriteArticle():
    query = content_models.Article.objects.filter(is_published=True).order_by('-clap_count')[:6]
    #return serializers.serialize('json',query)
    return query
    
print(getFavoriteArticle())