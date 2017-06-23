# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from .forms import *
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



#项目列表
def eproject_list(request):
    pt=eproject.objects.all()
    ##分页
    query_string = request.META.get('QUERY_STRING', '')

    # 搜索功能
    pname = request.GET.get('pname', '')
    if len(pname) > 0:
        pt = eproject.objects.filter(pname__contains=pname).order_by('-id')

    page_objects = pages(pt, request, 5)  ##分页
    return render_to_response('eproject/eproject_list.html', locals())



#server列表
def eserver_list(request):



    pt=eserver.objects.all()
    ##分页
    query_string = request.META.get('QUERY_STRING', '')

    # 搜索功能
    host = request.GET.get('host', '')
    epname=request.GET.get('epname','')
    print host,'6666666666'


    if epname:
        try:
            temp=eproject.objects.get(pname=epname)
            pt=temp.eserver_set.all()
        except eproject.DoesNoeExist:
            pass
    elif len(host) > 0:
        pt = eserver.objects.filter(host__contains=host).order_by('-id')
    else:
        page_objects = pages(pt, request, 5)  ##分页
    page_objects = pages(pt, request, 5)  ##分页


    pname=eproject.objects.all()
    return render_to_response('eproject/eserver_list.html', locals())


## 添加server
def eserver_add(request):
    if request.method == 'POST':
        form = eserverForm(request.POST)
        if form.is_valid():
            hostname = form.cleaned_data['hostname']
            ehost = form.cleaned_data['host']
            eport = form.cleaned_data['dport']
            hport = form.cleaned_data['hport']
            huser = form.cleaned_data['huser']

            descr = form.cleaned_data['descr']
            # values = request.POST.getlist('chk')
            # print '777777777 values',values

            print ehost

            if eserver.objects.filter(host=ehost,dport=eport):
                emg = u'添加失败, 此服务器 %s:%s 已存在!' % (ehost,eport)
                return render_to_response('eproject/eserver_add.html', locals())
            else:
                es=form.save()
                epassword = form.cleaned_data['hpassword']
                es.hpassword=jiami(epassword)                  ###加密
                es.save()
                return redirect('eserver_list')
        else:
            emg = u'项目环境: 添加失败'

    ep_j = eproject.objects.all()
    return render_to_response('eproject/eserver_add.html', locals())


## 批量授权
def grantprivs(request):
   pass



