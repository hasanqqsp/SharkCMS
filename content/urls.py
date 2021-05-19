from django.urls import path
from django.conf.urls import url, include
from . import views as article_view
app_name = 'article'
urlpatterns = [
    path('<str:pk>',article_view.ArticleDetailView.as_view())
    ]