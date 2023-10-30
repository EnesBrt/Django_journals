# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('list_articles/', views.list_articles, name='list_articles'),
    path('article/<slug:article_slug>/', views.article_detail, name='article_detail'),
]
