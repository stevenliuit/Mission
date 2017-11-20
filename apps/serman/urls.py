from django.conf.urls import url
from views import *

from django.contrib import admin
from apps.serman import views as serman_views

urlpatterns = [
    url(r'^serman/list/$', serman_views.ptslow_list, name='slowlog_list'),
    url(r'^etable/list/$', serman_views.etable_list, name='etable_list'),
    url(r'^ptslow/list/$', serman_views.ptslow_list, name='ptslow_list'),
    url(r'^etable/graph/$',serman_views.etable_graph, name='etable_graph'),
]
