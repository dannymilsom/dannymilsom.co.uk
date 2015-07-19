from django.conf.urls import patterns, url

from about.views import Homepage, Music

urlpatterns = patterns('about.views',
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^music$', Music.as_view(), name='music'),
    url(r'^contact$', 'contact', name='contact')
)