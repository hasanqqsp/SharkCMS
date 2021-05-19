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
    
def clapsView(request):
   
# Endpoints GET /api/article/claps
    if request.method == "GET":
        article_id = request.GET.get('id')
        print(getClapsInfo(request,article_id))
        return JsonResponse(getClapsInfo(request,article_id),safe=False)
 # Endpoints GET /api/article/claps       
    if request.method == "POST" and request.user.is_authenticated:
        article_id = request.POST.get('id')
        is_clap = request.POST.get('is-clap')
        
        return JsonResponse(giveClaps(request,article_id,is_clap),safe=False)
        
    return HttpResponseForbidden("Forbidden")