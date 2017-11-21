from django.conf.urls import url
from views import *

from django.contrib import admin
from apps.eproject import views as eproject_views

urlpatterns = [
    url(r'^eproject/list/$',eproject_views.eproject_list, name='eproject_list'),
    url(r'^eproject/add/$',eproject_views.eproject_add, name='eproject_add'),
    url(r'^eproject/edit/$',eproject_views.eproject_edit, name='eproject_edit'),
    url(r'^eserver/list/$', eproject_views.eserver_list, name='eserver_list'),
    url(r'^eserver/add/$', eproject_views.eserver_add, name='eserver_add'),
    url(r'^eserver/edit/$', eproject_views.eserver_edit, name='eserver_edit'),
    url(r'^eserver/del/$', eproject_views.eserver_del, name='eserver_del'),
    url(r'^release/apply/$', eproject_views.release_apply, name='release_apply'),
    url(r'^release/list/$', eproject_views.release_list, name='release_list'),
    url(r'^eprivs/add/$', eproject_views.eprivs_add, name='eprivs_add'),
    url(r'^eprivs/list/$', eproject_views.eprivs_list, name='eprivs_list'),
    url(r'^eprivs/del/$', eproject_views.eprivs_del, name='eprivs_del'),
    url(r'^edatabase/list/$', eproject_views.edatabase_list, name='edatabase_list'),
    url(r'^edatabase/add/$', eproject_views.edatabase_add, name='edatabase_add'),
    url(r'^mycat/dml/$', eproject_views.mycat_dml, name='mycat_dml'),

]
