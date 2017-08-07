from django.conf.urls import url
from views import *

from django.contrib import admin
from apps.eproject import views as eproject_views

urlpatterns = [
    url(r'^eproject/list/$',eproject_views.eproject_list, name='eproject_list'),
    url(r'^eserver/list/$', eproject_views.eserver_list, name='eserver_list'),
    url(r'^eserver/add/$', eproject_views.eserver_add, name='eserver_add'),
    url(r'^eprivs/add/$', eproject_views.eprivs_add, name='eprivs_add'),
    url(r'^eprivs/list/$', eproject_views.eprivs_list, name='eprivs_list'),
    url(r'^mycat/dml/$', eproject_views.mycat_dml, name='mycat_dml'),
]
