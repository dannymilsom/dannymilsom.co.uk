from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'latest_posts', name='latest_posts'),
    url(r'^tags/(?P<category>[-a-zA-Z0-9]+)/$', 'category_posts', name='category_posts'),
    url(r'^(?P<slug>[-a-zA-Z0-9]+)/?$', 'individual_post', name='post'),
)