from django.conf.urls import url
from views import *

from django.contrib import admin
from apps.serman import views as serman_views

urlpatterns = [
    url(r'^ptslow/list/$', serman_views.ptslow_list, name='ptslow_list'),
]
