from django.test import TestCase
from .models import Articles
from django.utils import timezone

class ArticlesModelTest(TestCase):

    def create_article(self, headline="Test headline"):
        return Articles.objects.create(headline=headline, content="Some content")

    def test_article_creation(self):
        article = self.create_article()
        self.assertTrue(isinstance(article, Articles))
        self.assertEqual(article.__str__(), article.headline)

    def test_slug_generation_on_save(self):
        article = self.create_article()
        article.save()
        self.assertEqual(article.slug, "test-headline")

    def test_date_of_publication(self):
        article = self.create_article()
        article.save()
        self.assertTrue(isinstance(article.date_of_publication, timezone.datetime))
