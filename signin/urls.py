from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views


urlpatterns = [
    url(r'^$', views.sign_in, name='sign_in'),
    url(r'^new$', views.sign_in_new, name='sign_in_new'),
    url(r'^new_member$', views.new_member, name='new_member'),
    url(r'^staff_login$', views.staff_login, name='staff_login'),
    url(r'^staff_dash$', views.staff_dash, name='staff_dash'),
    url(r'^staff_dash-view-all-users$', views.view_all_users, name='view_all_users'),
    url(r'^staff_dash-attendance$', views.attendance, name='attendance'),
    url(r'^staff_dash-whos-here$', views.whos_here, name='whos_here'),
    url(r'^staff_dash-send-mail$', views.email, name='send_mail'),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': '/'}),
]
