from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.sign_in, name='sign_in'),
    url(r'^new_member$', views.new_member, name='new_member'),
    url(r'^staff_login$', views.staff_login, name='staff_login'),
    url(r'^staff_dash$', views.staff_dash, name='staff_dash'),
    url(r'^staff_dash-view-all-users$', views.staff_dash, name='view_all_users'),
    url(r'^staff_dash-attendance$', views.staff_dash, name='attendance'),
    url(r'^staff_dash-whos-here$', views.staff_dash, name='whos_here'),
    url(r'^staff_dash-send-mail$', views.staff_dash, name='send_mail'),
]
