from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ancillary.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'ancillary.views.index', name='index'),
    url(r'^register/$', include('register.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^request/', include('request.urls')),
    url(r'^manager/', include('manager.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
