from django.conf.urls import url, include
from proxyserver.apps.authorization.views import login_view, logout_view
from . import views

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'contact/$', views.post_new, name='post_new'),
    url(r'users/$', views.users, name='users')
]
