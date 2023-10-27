from django.db import models
from tinymce.models import HTMLField

class Articles(models.Model):
    headline = models.CharField(max_length=255)
    content = HTMLField()
    date_of_publication = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.headline