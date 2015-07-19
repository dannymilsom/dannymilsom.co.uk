from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('about.views',
	url(r'', include('about.urls'))
)

urlpatterns += patterns('blog.views',
    url(r'^blog/', include('blog.urls')),
)

urlpatterns += patterns('',
	url(r'^admin/', include(admin.site.urls), name='admin'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()