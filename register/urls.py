from django.conf.urls import patterns, url

from register import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^newaccount/$', views.newaccount, name='newaccount'),
        url(r'^check_email/$', views.check_email, name='check_email'),
        url(r'^confirm_data/$', views.confirm_data, name='confirm_data'),
        url(r'^final_signup/$', views.final_signup, name='final_signup'),
)
