from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class ArticleDetailView(TemplateView):
    template_name = 'content/article_detail_view.html'