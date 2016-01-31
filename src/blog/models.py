from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify

from .constants import BLOG_POST_CATEGORIES

class Post(models.Model):

    TAG_CHOICES = BLOG_POST_CATEGORIES

    class Meta:
        ordering = ['-date']

    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=500)
    message = models.TextField(max_length=1000)
    date = models.DateField()
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40)
    tags = models.CharField(
        max_length=20,
        choices=TAG_CHOICES,
        default='Python',
    )

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'blog.views.individual_post',
            kwargs={'slug': self.slug}
        )
