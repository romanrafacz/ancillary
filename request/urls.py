from django.conf.urls import patterns, url

from request import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^submit_request/$', views.submit_request, name="submit_request"),


)
