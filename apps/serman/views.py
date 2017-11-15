# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
import json
from devops.settings import DEBUG
from common.utils.sessions import *
from common.utils.paginator import pages
from common.utils.email import *
from apps.models import *
from common.utils.crypt import md5, gen_rand_password,jiami,jiemi
import re
import base64
import os,sys
import  MySQLdb
from django.http import HttpResponse
from django.http import HttpResponseRedirect



#slow_log list
def ptslow_list(request):
    pt=global_query_review_history.objects.all().order_by('-ts_max')
    ##分页
    query_string = request.META.get('QUERY_STRING', '')



    # 搜索功能
    begin_date = request.GET.get('begin_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()
    pname = request.GET.get('pname', '')
    database = request.GET.get('database', '')
    bycol = request.GET.get('bycol', '')

    try:
        phostname=eserver.objects.filter(eproject__pname=pname)[0].hostname
    except Exception,e:
        phostname=''
    if not begin_date:
        begin_date='2000-01-01'
    if not end_date:
        end_date='2100-01-01'
    if not bycol:
        bycol='ts_max'
    print '666666666666666',phostname,database,begin_date,end_date,bycol
    if len(phostname) > 0 and len(database)==0:
        pt = global_query_review_history.objects.filter(hostname_max__contains=phostname,ts_min__gte=begin_date, ts_max__lte=end_date).order_by('-%s' % bycol)
    elif len(database) > 0 and len(phostname)==0 :
        pt = global_query_review_history.objects.filter(db_max__contains=database,ts_min__gte=begin_date, ts_max__lte=end_date).order_by('-%s' % bycol)
    elif len(database) > 0 and len(phostname)>0:
        pt = global_query_review_history.objects.filter(db_max__contains=database,hostname_max__contains=phostname,ts_min__gte=begin_date, ts_max__lte=end_date).order_by('-%s' % bycol)  ##分页
    else:
        pt = global_query_review_history.objects.filter(ts_min__gte=begin_date, ts_max__lte=end_date).order_by('-%s' % bycol)


    page_objects = pages(pt, request, 10)  ##分页
    vser=eserver.objects.all()
    # vser=eserver.objects.filter(eproject__eproject_admin__admin_id=get_current_admin_id(request))
    return render_to_response('serman/ptslow_list.html', locals())

def serman_test(request):
    return render_to_response('serman/serman_test.html', locals())





