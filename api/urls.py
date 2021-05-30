from django.urls import path
from django.conf.urls import url, include
from . import views as api_view
app_name = 'api'
urlpatterns = [
    path('article/favorite',api_view.favoriteArticleView,name='favorite_article'),
    path('article/newest',api_view.newestArticleView,name='newest_article'),
    path('article/claps',api_view.clapsView,name='claps'),
    path('article/<str:slug>',api_view.ArticleView.as_view(),name='articleDetail')
    ]