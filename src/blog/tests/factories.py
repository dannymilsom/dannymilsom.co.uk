from datetime import timedelta

from factory import django, fuzzy

from django.utils import timezone


from ..constants import BLOG_POST_CATEGORIES


class PostFactory(django.DjangoModelFactory):

    class Meta:
        model = 'blog.Post'

    title = fuzzy.FuzzyText(length=20)
    slug = ''
    summary = fuzzy.FuzzyText(length=100)
    message = fuzzy.FuzzyText(length=500)
    date = fuzzy.FuzzyDate(timezone.now().date() - timedelta(weeks=10))
    author = fuzzy.FuzzyText(length=20)
    tags = fuzzy.FuzzyChoice(BLOG_POST_CATEGORIES)
