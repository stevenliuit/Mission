from django.conf.urls import url
from views import *

from django.contrib import admin
from apps.serman import views as serman_views

urlpatterns = [
    url(r'^serman/list/$', serman_views.slowlog_list, name='slowlog_list'),
]
