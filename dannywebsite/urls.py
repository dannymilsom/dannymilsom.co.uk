from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

#http://stackoverflow.com/questions/5201346/how-do-i-go-straight-to-template-in-djangos-urls-py

urlpatterns = patterns('about.views',
	url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
	url(r'^music$', TemplateView.as_view(template_name='music.html'), name='music'),
	url(r'^contact$', 'contact', name='contact'),
)

urlpatterns += patterns('blog.views',
    url(r'^blog/', include('blog.urls')),
)

urlpatterns += patterns('',
	url(r'^admin/', include(admin.site.urls), name='admin'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()