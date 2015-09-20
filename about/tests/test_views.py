from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import Client, TestCase


class HomepageTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_context_provided(self):

        resp = self.client.get(reverse('homepage'))

        self.assertEqual(200, resp.status_code)
        self.assertIn('form', resp.context)
        self.assertIn('gmail_address', resp.context)

    def test_missing_contact_form_fields_validated(self):

        resp = self.client.post(reverse('homepage'), {},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(400, resp.status_code)
        for field in ['name', 'email', 'message']:
            self.assertIn(field, resp.content)

    def test_invalid_email_field_validated(self):

        form_data = {
            'name': 'Steve Jones',
            'message': 'Nice tan son!',
        }
        resp = self.client.post(reverse('homepage'), form_data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(400, resp.status_code)
        self.assertIn('email', resp.content)

    def test_valid_contact_form_submission_sends_email(self):

        form_data = {
            'name':'Brian Tinnion',
            'email': 'brian@bcfc.com',
            'message': 'Best left foot in the south west!',
        }
        resp = self.client.post(reverse('homepage'), form_data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(200, resp.status_code)

        self.assertEquals(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].recipients(), [settings.GMAIL_ADDRESS])

