# -*- coding: utf-8 -*-

from django.forms import ModelForm
from apps.models import *

class htsForm(ModelForm):
    class Meta:
        model = history_tab_sum
        fields = ['dbname','tbname']