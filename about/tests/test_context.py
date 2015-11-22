from django.core.urlresolvers import reverse
from django.test import Client, TestCase


class ContextProcessorTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_social_media_links_in_context(self):

        resp = self.client.get(reverse('homepage'))
        context = resp.context

        self.assertIn('TWITTER_URL', context)
        self.assertIn('GITHUB_URL', context)
        self.assertIn('LINKEDIN_URL', context)
        self.assertIn('STACKOVERFLOW_URL', context)
        self.assertIn('INSTAGRAM_URL', context)
        self.assertIn('SOUNDCLOUD_URL', context)
