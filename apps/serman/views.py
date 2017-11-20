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
from copy import copy



#slow_log list
def ptslow_list(request):
    pt=global_query_review_history.objects.all().order_by('-ts_max')
    ##分页
    query_string = request.META.get('QUERY_STRING', '')



    # 搜索功能
    begin_date = request.GET.get('begin_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()
    pname = request.GET.get('pname', '')
    print 'ppppppppppp',pname
    database = request.GET.get('database', '')
    bycol = request.GET.get('bycol', '')

    try:
        phostname=eserver.objects.get(descr=pname).hostname
    except Exception,e:
        phostname=''

    ##如果传了pname但却没有eserver.desc
    if len(pname)>0 and len(phostname)==0:
        phostname = '9999999!@#'

    ###默认值
    if not begin_date:
        begin_date='2000-01-01'
    if not end_date:
        end_date='2100-01-01'
    if not bycol:
        bycol='ts_max'
    print '666666666666666',phostname,database,begin_date,end_date,bycol

    ###组合判断
    if len(phostname) > 0 and len(database)==0:
        pt = global_query_review_history.objects.filter(hostname_max=phostname,ts_min__gte=begin_date, ts_max__lte=end_date).order_by('-%s' % bycol)
    elif len(database) > 0 and len(phostname)==0 :
        pt = global_query_review_history.objects.filter(db_max__contains=database,ts_min__gte=begin_date, ts_max__lte=end_date).order_by('-%s' % bycol)
    elif len(database) > 0 and len(phostname)>0:
        pt = global_query_review_history.objects.filter(db_max__contains=database,hostname_max=phostname,ts_min__gte=begin_date, ts_max__lte=end_date).order_by('-%s' % bycol)  ##分页
    else:
        pt = global_query_review_history.objects.filter(ts_min__gte=begin_date, ts_max__lte=end_date).order_by('-%s' % bycol)


    page_objects = pages(pt, request, 10)  ##分页
    ese=eserver.objects.all()
    return render_to_response('serman/ptslow_list.html', locals())

def etable_list(request):
    hts=history_tab_sum.objects.all()
    page_objects = pages(hts, request, 10)  ##分页
    return render_to_response('serman/etable_list.html', locals())



def etable_graph(request):
    pk_id=request.GET.get('id','')
    print 'ooooooooooooooooooooooooo',pk_id
    tabnum = history_tab_sum.objects.get(id=pk_id)
    msgS = tabnum
    daydata = msgS.data
    tmm = eval(daydata)

    data = {}
    ulist = []
    vlist = {}
    tmp = []
    for i, j in tmm.items():
        ulist.append(i)
    ulist.sort()
    data['categories'] = ulist

    for i, j in tmm.items():
        vlist['value'] = j
        vlist['name'] = i
        tmp.append(copy(vlist))
    data['data'] = tmp
    print 'asdadasdasdasdasdas',data

    return render_to_response('serman/etable_graph.html',locals())






