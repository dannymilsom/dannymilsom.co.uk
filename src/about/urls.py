from django.conf.urls import patterns, url

from about.views import Homepage

urlpatterns = patterns('about.views',
    url(r'^$', Homepage.as_view(), name='homepage'),
)