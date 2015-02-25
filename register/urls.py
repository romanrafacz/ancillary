from django.conf.urls import patterns, url

from register import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^newaccount/$', views.newaccount, name='newaccount'),
        url(r'^check_email/$', views.check_email, name='check_email'),
        url(r'^confirm_data/$', views.confirm_data, name='confirm_data'),
        url(r'^final_signup/$', views.final_signup, name='final_signup'),
        url(r'^submit_form/$', views.submit_form, name='submit_form'),
        url(r'^user_data/$', views.user_data, name='user_data'),
        url(r'^confirmation_page/$', views.confirmation_page, name='confirmation_page'),
)
