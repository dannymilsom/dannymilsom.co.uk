from django.test import TestCase
from django.utils.text import slugify

from .factories import PostFactory


class PostModelTests(TestCase):

    def test_slug_auto_generated_if_missing(self):
        blog_post = PostFactory(title='Test slug generation')
        self.assertEqual(blog_post.slug, slugify(blog_post.title))

    def test_slug_not_overridden_if_passed(self):
        forced_slug = 'not-the-generated-slug'
        blog_post = PostFactory(title='Test slug generation', slug=forced_slug)

        self.assertNotEqual(blog_post.slug, slugify(blog_post.title))
        self.assertEqual(blog_post.slug, forced_slug)
