from django.conf import settings
from django.shortcuts import render

def social_network_links(request):
	"""
	Adds social network URLs to every template via context processor. These 
	values are stored in the settings.py file.
	"""

	return {
		'TWITTER_URL': settings.TWITTER_PROFILE_URL,
		'GITHUB_URL': settings.GITHUB_PROFILE_URL,
		'LINKEDIN_URL': settings.LINKEDIN_PROFILE_URL,
		'STACKOVERFLOW_URL': settings.STACKOVERFLOW_PROFILE_URL,
		'INSTAGRAM_URL': settings.INSTAGRAM_PROFILE_URL,
	}