# -*- coding: utf-8 -*-

from django.forms import ModelForm
from apps.models import *



class eprojectForm(ModelForm):
    class Meta:
        model = eproject
        fields = ['pname']

class eserverForm(ModelForm):
    class Meta:
        model = eserver
        fields = ['eproject','hostname','host','dport','hport','huser','hpassword','descr']


class eprivsForm(ModelForm):
    class Meta:
        model = eprivs
        fields = ['dname','dpass','ptype']

class releaseForm(ModelForm):
    class Meta:
        model = release
        fields = ['releaser_id','eserver','edatabase','sql','description','exec_time']

class edatabaseForm(ModelForm):
    class Meta:
        model = edatabase
        fields = ['eserver','dbname','dport','descr']

