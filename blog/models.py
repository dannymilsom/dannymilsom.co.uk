from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import permalink

class Post(models.Model):

	TAG_CHOICES = (
		('Python', 'Python'),
		('Linux', 'Linux'),
		('HTML', 'HTML'),
		('CSS', 'CSS'),
		('Django', 'Django'),
		('JavaScript', 'JavaScript'), 
		('jQuery', 'jQuery'), 
		('Web', 'Web'),
		('Bootstrap', 'Bootstrap'),
		('Apache HTTP', 'Apache HTTP'),
		('PostgreSQL', 'PostgreSQL'),
	)

	title = models.CharField(max_length=100)
	summary = models.TextField(max_length=500)
	message = models.TextField(max_length=1000)
	date = models.DateField()
	author = models.CharField(max_length=100)
	slug = models.SlugField(max_length=40)
	tags = models.CharField(max_length=20, choices=TAG_CHOICES,
	                          default='Python')

	def __unicode__(self):
	    return self.title

	@permalink
	def get_absolute_url(self):
		return ('Post', None, { 'slug': self.slug })