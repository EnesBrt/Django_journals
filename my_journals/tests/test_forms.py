from django.test import TestCase
from my_journals.forms import ContactForm  # Utilisez le chemin d'importation absolu

class ContactFormTest(TestCase):

    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'name': 'John Doe',
            'subject': 'Test Subject',
            'message': 'Hello, this is a test message.'
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_no_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # There should be three fields with errors

    def test_contact_form_partial_data(self):
        # Only 'name' is provided, 'subject' and 'message' are missing
        form = ContactForm(data={'name': 'Jane Doe'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # 'subject' and 'message' fields have errors
