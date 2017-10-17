# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from .forms import *
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
from api import mysqlgrant_read,mysqlgrant_write,mysqlping



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
    if request.is_ajax():
        ret = {}
        v_host = request.POST.get('a')
        v_port = request.POST.get('b')
        print v_port, v_host
        status = mysqlping(int(v_port), v_host)
        print status
        if status == 'SUCCESS':
            ret['status'] = True
        else:
            ret['status'] = False
        print ret
        return HttpResponse(json.dumps(ret))
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
def eprivs_add(request):
    jump_view = 'eprivs_list'
    if request.method == 'POST':
        form = eprivsForm(request.POST)
        if form.is_valid():
            dname = form.cleaned_data['dname']
            dpass=form.cleaned_data['dname']
            ptype=form.cleaned_data['ptype']
            epivs = form.save()

            pids = request.POST.getlist('pids', [])
            print pids

            ##授权
            if pids:
                for i in pids:
                    tar_port = eserver.objects.get(id=i).dport
                    tar_host = eserver.objects.get(id=i).host
                    print tar_port, tar_host
                    if ptype == 0:
                        mysqlgrant_read(tar_port, tar_host, dname, dpass)
                    else:
                        mysqlgrant_write(tar_port, tar_host, dname, dpass)

                tm=eserver.objects.in_bulk(pids)
                epivs.servers=tm

                epivs.save()
                jump_view = 'eprivs_list'
                message = '授权成功'
                return render_to_response('eproject/success.html', locals())
            else:
                jump_view = 'eprivs_add'
                message = '授权失败'
                return render_to_response('eproject/error.html', locals())


    es=eserver.objects.all()
    return render_to_response('eproject/eprivs_add.html', locals())


## 授权记录
def eprivs_list(request):
    pt = eprivs_eserver.objects.all().order_by('-id')
    ##分页
    query_string = request.META.get('QUERY_STRING', '')
    page_objects = pages(pt, request, 5)  ##分页
    return render_to_response('eproject/eprivs_list.html', locals())


## 分库分表处理
def mycat_dml(request):
    if request.method == 'POST':
        sql=request.POST.get('a')
        pids = request.POST.getlist('pids', [])
        print '55555',pids,sql
    es=mycat_server.objects.all()
    return render_to_response('eproject/mycat_dml.html', locals())

