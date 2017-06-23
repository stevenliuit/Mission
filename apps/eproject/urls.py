from django.conf.urls import url
from views import *

from django.contrib import admin
from apps.eproject import views as eproject_views

urlpatterns = [
    url(r'^eproject/list/$',eproject_views.eproject_list, name='eproject_list'),
    url(r'^eserver/list/$', eproject_views.eserver_list, name='eserver_list'),
    url(r'^eserver/add/$', eproject_views.eserver_add, name='eserver_add'),
    url(r'^eserver/grantprivs/$', eproject_views.grantprivs, name='grantprivs'),
]
