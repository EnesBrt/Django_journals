from django.contrib import admin
from .models import Articles
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'date_of_publication')
    search_fields = ('headline',)

admin.site.register(Articles, ArticleAdmin)