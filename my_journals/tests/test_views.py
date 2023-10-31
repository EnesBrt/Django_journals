# Dans test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from my_journals.models import Articles  # Utilisez le chemin d'importation absolu
from django.core import mail


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.article = Articles.objects.create(headline="Test Article", content="Test Content")

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_list_articles_view(self):
        response = self.client.get(reverse('list_articles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_articles.html')
        self.assertIn('articles', response.context)

    def test_article_detail_view(self):
        response = self.client.get(reverse('article_detail', args=[self.article.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_detail.html')
        self.assertEqual(response.context['article'], self.article)

    def test_contact_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_view_post_success(self):
        mail.outbox = []
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'subject': 'Test Subject',
            'message': 'Test message'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Test Subject')
