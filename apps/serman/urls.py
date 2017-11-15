from django.conf.urls import url
from views import *

from django.contrib import admin
from apps.serman import views as serman_views

urlpatterns = [
    url(r'^serman/list/$', serman_views.ptslow_list, name='slowlog_list'),
    url(r'^serman/test/$', serman_views.serman_test, name='serman_test'),
    url(r'^ptslow/list/$', serman_views.ptslow_list, name='ptslow_list'),
]
