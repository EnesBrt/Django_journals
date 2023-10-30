from django.shortcuts import render
from .models import Articles
from django.shortcuts import get_object_or_404

def home_view(request):
    return render(request, 'home.html')

def list_articles(request):
    articles = Articles.objects.all()
    return render(request, 'list_articles.html', {'articles': articles})

def article_detail(request, article_slug):
    article = get_object_or_404(Articles, slug=article_slug)
    return render(request, 'article_detail.html', {'article': article})