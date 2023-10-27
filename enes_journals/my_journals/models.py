from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify

class Articles(models.Model):
    headline = models.CharField(max_length=255)
    slug = models.SlugField(default='', blank=True)
    content = HTMLField()
    date_of_publication = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # vérifie si le slug est vide
            self.slug = slugify(self.headline)  # génère un slug à partir du titre
        super().save(*args, **kwargs)  # appelle la méthode save() originale
    
    def __str__(self):
        return self.headline