from django.conf.urls import patterns, url

from register import views

urlpatterns = patterns('',
        (r'^$', views.index, name='index'),
)
