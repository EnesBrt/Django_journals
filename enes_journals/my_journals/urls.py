from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_articles, name='list_articles'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]
