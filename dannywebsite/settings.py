"""
Django settings for dannywebsite project.
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    from dannywebsite.secret_settings import *
except ImportError:
    # this is a automatically generated secret key included for convinence
    # via http://www.miniwebtool.com/django-secret-key-generator
    SECRET_KEY = 'j_gzy0)rmux=@s4$m%v(3@mdhpvd6m$@l^tw8vaws+y=fj)315'

try:
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
    from production_settings import *
except ImportError:
    DEBUG = True

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []

    DEV_APPS = tuple()

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'danny.db'),
        }
    }
else:
    DEV_APPS = tuple()

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

LOCAL_APPS = (
    'dannywebsite',
    'about',
    'blog',
)

THIRD_PARTY_APPS = (
    'crispy_forms',
    'disqus',
    'pagedown',
)

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'blog.context_processors.select_list_data',
    'about.context_processors.social_network_links',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'dannywebsite.urls'

WSGI_APPLICATION = 'dannywebsite.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

DATE_FORMAT = "F Y"

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'dannywebsite', 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

SITE_ID = 1

INTERNAL_IPS = ('127.0.0.1',)

# Social Media Links

GMAIL_ADDRESS = 'dannysmilsom@gmail.com'
TWITTER_PROFILE_URL = 'https://twitter.com/DannyMilsom'
GITHUB_PROFILE_URL = 'https://github.com/dannymilsom'
LINKEDIN_PROFILE_URL = 'http://uk.linkedin.com/pub/danny-milsom/51/20b/7250'
STACKOVERFLOW_PROFILE_URL = 'http://stackoverflow.com/users/1178602/dannymilsom'
INSTAGRAM_PROFILE_URL = 'http://instagram.com/dannymilsom'

