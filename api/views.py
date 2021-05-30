from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from .serializers import *
import json
# Create your views here.

#Endpoints GET /api/article/favorite
def favoriteArticleView(request):
    print(JsonResponse(getFavoriteArticle(6),safe=False))
    return JsonResponse(getFavoriteArticle(6),safe=False)
#Endpoints GET /api/article/newest    
def newestArticleView(request):
    return JsonResponse(getNewestArticle(6),safe=False)
    



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import *


class ArticleView(ListCreateAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        slug = self.kwargs['slug']
        return content_models.Article.objects.filter(slug=slug)
#@api_view(['GET','POST'])       
def clapsView(request):
# Endpoints GET /api/article/claps
    if request.method == "GET":
        article_id = request.GET.get('id')
        print(getClapsInfo(request,article_id))
        return JsonResponse(getClapsInfo(request,article_id),safe=False)
# Endpoints GET /api/article/claps       
    if request.method == "POST" and request.user.is_authenticated:
        data = json.loads(request.body.decode("utf-8"))
        
        print(data['id'])
        

        print(request.POST)
        article_id = request.POST.get('id')
        is_clap = request.POST.get('is-clap')
        
        return JsonResponse(giveClaps(request,data['id'],data['is-clap']),safe=False)
    return HttpResponseForbidden("You're not have access to this feature please login")