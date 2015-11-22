from django.conf import settings

def social_network_links(request):
    """Adds social network URLs used in the navbar to the template context."""

    return {
        'TWITTER_URL': settings.TWITTER_PROFILE_URL,
        'GITHUB_URL': settings.GITHUB_PROFILE_URL,
        'LINKEDIN_URL': settings.LINKEDIN_PROFILE_URL,
        'STACKOVERFLOW_URL': settings.STACKOVERFLOW_PROFILE_URL,
        'INSTAGRAM_URL': settings.INSTAGRAM_PROFILE_URL,
        'SOUNDCLOUD_URL': settings.SOUNDCLOUD_URL,
    }