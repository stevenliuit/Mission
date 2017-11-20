# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect,render
from .forms import *
from django.db.models.aggregates import Count
from copy import copy
from django.http import JsonResponse
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
from api import *

#add eproject
def eproject_add(request):
    jump_view = 'eproject_list'
    if request.method == 'POST':
        form = eprojectForm(request.POST)
        if form.is_valid():
            pname = form.cleaned_data['pname']


            pids = request.POST.getlist('pids', [])
            print pids

            ##授权
            if pids:
                ea = form.save()
                tm = eproject.objects.in_bulk(pids)
                ea.admin = tm

                ea.save()
                jump_view = 'eproject_list'
                message = '添加成功'
                return render_to_response('eproject/success.html', locals())
            else:
                jump_view = 'eproject_add'
                message = '添加失败'
                return render_to_response('eproject/error.html', locals())

    ad=Admin.objects.all()
    return render_to_response('eproject/eproject_add.html', locals())

#环境列表
def eproject_list(request):
    if get_current_admin_id(request)==Admin.objects.get(name='admin').id:
        pt=eproject.objects.all()
    else:
        pt=eproject.objects.filter(eproject_admin__admin_id=get_current_admin_id(request))
    ##分页
    query_string = request.META.get('QUERY_STRING', '')

    # 搜索功能
    pname = request.GET.get('pname', '')
    if len(pname) > 0:
        pt = eproject.objects.filter(pname__contains=pname).order_by('-id')

    page_objects = pages(pt, request, 10)  ##分页
    return render_to_response('eproject/eproject_list.html', locals())


#环境编辑
def eproject_edit(request):
    pk_id = request.GET.get('id', '')
    project_group = eproject.objects.get(id=pk_id)
    if request.method == 'POST':
        form = eprojectForm(request.POST, instance=project_group)
        if form.is_valid():
            name = form.cleaned_data['pname']
            print name
            val_module = eproject.objects.filter(pname=name).exclude(id=pk_id)
            if val_module:
                emg = u'修改失败, 此环境%s 已存在!' % name
            else:
                epro = form.save()
                pids = request.POST.getlist('pids', [])
                print pids
                if pids:
                    pev_server = eproject.objects.in_bulk(pids)
                    epro.admin = pev_server
                    epro.save()
                return redirect('eproject_list')
        else:
            emg = u'环境: 修改失败'

    admin=Admin.objects.all()
    eproject_ids = []
    for t in project_group.admin.all():
        eproject_ids.append(t.id)

    return render_to_response('eproject/eproject_edit.html', locals(), request)


#server列表
def eserver_list(request):
    if get_current_admin_id(request) == Admin.objects.get(name='admin').id:
        pt=eserver.objects.all()
    else:
        pt=eserver.objects.filter(eproject__eproject_admin__admin_id=get_current_admin_id(request))

    ##分页
    query_string = request.META.get('QUERY_STRING', '')

    # 搜索功能
    host = request.GET.get('host', '')
    epname=request.GET.get('epname','')



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
        v_pass = request.POST.get('c')
        v_user = request.POST.get('d')
        v_hport = request.POST.get('e')
        print v_host, v_port, v_user, v_pass, v_hport
        status = mysqlping(int(v_port), v_host)
        sshstat= sshping(v_host,int(v_hport),v_user,v_pass)
        print 'yyyyyyyyy',sshstat
        if status == 'SUCCESS' and sshstat=='success':
            ret['status'] = True
        else:
            ret['status'] = False
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

            if eserver.objects.filter(host=ehost,hport=hport):
                emg = u'添加失败, 此服务器 %s:%s 已存在!' % (ehost,hport)
                return render_to_response('eproject/eserver_add.html', locals())
            else:
                es=form.save()
                epassword = form.cleaned_data['hpassword']
                trans_cut_slow(ehost, hport, huser,epassword)   ####推送慢日志切割脚本
                es.hpassword=jiami(epassword)                  ###加密
                es.save()
                return redirect('eserver_list')
        else:
            emg = u'项目环境: 添加失败'

    ep_j = eproject.objects.all()
    return render_to_response('eproject/eserver_add.html', locals())


#server编辑
def eserver_edit(request):
    pk_id = request.GET.get('id', '')
    print 'ttttttttttttttt',pk_id
    veserver = eserver.objects.get(id=pk_id)
    if request.is_ajax():
        ret = {}
        v_host = request.POST.get('a')
        v_port = request.POST.get('b')
        v_pass = request.POST.get('c')
        v_user = request.POST.get('d')
        v_hport = request.POST.get('e')
        status = mysqlping(int(v_port), v_host)
        sshstat = sshping(v_host, int(v_hport), v_user, v_pass)
        if status == 'SUCCESS' and sshstat == 'success':
            ret['status'] = True
        else:
            ret['status'] = False
        return HttpResponse(json.dumps(ret))


    if request.method == 'POST':
        form = eserverForm(request.POST, instance=veserver)
        if form.is_valid():
            ehost = form.cleaned_data['host']
            eport = form.cleaned_data['dport']
            val_module = eserver.objects.filter(host=ehost,dport=eport).exclude(id=pk_id)
            if val_module:
                emg = u'修改失败, 此%s:%s 已存在!' % (ehost,eport)
            else:
                es = form.save()
                epassword = form.cleaned_data['hpassword']
                es.hpassword = jiami(epassword)  ###加密
                es.save()
                return redirect('eserver_list')
        else:
            emg = u'环境: 修改失败'

    ep_j = eproject.objects.all()
    return render_to_response('eproject/eserver_edit.html', locals(), request)

###删除server
def eserver_del(request):
    pk_id = request.GET.get('id', '')
    eserver.objects.get(id=pk_id).delete()
    return  redirect('eserver_list')

###edatabase_list
def edatabase_list(request):
    if get_current_admin_id(request) == Admin.objects.get(name='admin').id:
        pt=edatabase.objects.all()
    else:
        pt=edatabase.objects.filter(eserver__eproject__eproject_admin__admin_id=get_current_admin_id(request))

    ##分页
    query_string = request.META.get('QUERY_STRING', '')

    page_objects = pages(pt, request, 5)  ##分页


    # pname=eproject.objects.all()
    return render_to_response('eproject/edatabase_list.html', locals())

###发布申请
def release_apply(request):
    current_admin_id = get_current_admin(request).id  ##获取当前登录用户的id
    pk_id = request.GET.get('id', '')
    eserverall=eserver.objects.get(id=pk_id)
    eda=eserverall.edatabase_set.all()

    jump_view = 'release_list'

    if request.method == 'POST':
        form = releaseForm(request.POST)
        if form.is_valid():
            form.save()
            message = "申请成功!"
            return render_to_response('success.html', locals())
        else:
            emg = u'申请失败'



    return render_to_response('eproject/release_apply.html', locals(), request)



###发布列表
def release_list(request):
    if get_current_admin_id(request) == Admin.objects.get(name='admin').id:
        pt = release.objects.all().order_by('-id')
    else:
        pt = release.objects.filter(eserver__eproject__eproject_admin__admin_id=get_current_admin_id(request))

    ##分页
    query_string = request.META.get('QUERY_STRING', '')

    # 搜索功能
    # pname = request.GET.get('pname', '')
    # if len(pname) > 0:
    #     pt = eproject.objects.filter(pname__contains=pname).order_by('-id')

    page_objects = pages(pt, request, 5)  ##分页
    return  render_to_response('eproject/release_list.html', locals())



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
                # for i in pids:
                #     tar_port = eserver.objects.get(id=i).dport
                #     tar_host = eserver.objects.get(id=i).host
                #     print tar_port, tar_host
                    # if ptype == 0:
                    #     mysqlgrant_read(tar_port, tar_host, dname, dpass)
                    # else:
                    #     mysqlgrant_write(tar_port, tar_host, dname, dpass)

                tm=edatabase.objects.in_bulk(pids)
                epivs.databases=tm

                epivs.save()
                jump_view = 'eprivs_list'
                message = '授权成功'
                return render_to_response('eproject/success.html', locals())
            else:
                jump_view = 'eprivs_add'
                message = '授权失败'
                return render_to_response('eproject/error.html', locals())


    ed=edatabase.objects.all()
    return render_to_response('eproject/eprivs_add.html', locals())


## 授权记录
def eprivs_list(request):
    pt = eprivs.objects.all().order_by('-id')
    ##分页
    query_string = request.META.get('QUERY_STRING', '')

    # # 搜索功能
    username = request.GET.get('username', '')
    if username:
        pt=eprivs.objects.filter(dname__contains=username)
    page_objects = pages(pt, request, 5)  ##分页
    return render_to_response('eproject/eprivs_list.html', locals())

#### 权限回收
def eprivs_del(request):
    pk_id = request.GET.get('id', '')
    dport= eserver.objects.get(eprivs_eserver__e_privs_id=pk_id).dport
    host = eserver.objects.get(eprivs_eserver__e_privs_id=pk_id).host
    dname=eprivs.objects.get(id=pk_id).dname
    print dport,host,dname
    try:
        mysqlgrant_revoke(dport,host,dname)
    except Exception,e:
        pass

    eprivs.objects.get(id=pk_id).delete()
    return redirect('eprivs_list')


## 分库分表处理
def mycat_dml(request):
    if request.method == 'POST':
        sql=request.POST.get('a')
        pids = request.POST.getlist('pids', [])
        print '55555',pids,sql
    es=mycat_server.objects.all()
    return render_to_response('eproject/mycat_dml.html', locals())

## edatabase_graph
def edatabase_graph(request):
    # 搜索功能
    dbname = request.GET.get('dbname', '')
    tbname = request.GET.get('tbname', '')

    if len(dbname) > 0 and len(tbname)==0:
        tabnum = history_tab_sum.objects.filter(dbname=dbname)
    elif len(dbname) == 0 and len(tbname)>0:
        tabnum = history_tab_sum.objects.filter(tbname__contains=tbname)
    elif len(dbname) > 0 and len(tbname) > 0:
        tabnum = history_tab_sum.objects.filter(dbname=dbname,tbname__contains=tbname)
    else:
        tabnum = history_tab_sum.objects.all()[0:10]
    if request.method == 'GET' and request.GET.get('data') == '1' :
        msgS=tabnum
        alldata = {}
        for hts in msgS:
            daydata=hts.data
            tmm = eval(daydata)

            data={}
            ulist=[]
            vlist={}
            tmp=[]
            for i,j in tmm.items():
                ulist.append(i)
            ulist.sort()
            data['categories'] = ulist


            for i,j in tmm.items():
                vlist['value']=j
                vlist['name']=i
                tmp.append(copy(vlist))
            data['data']= tmp

            alldata[hts.tbname]=data
        return  JsonResponse(alldata)  ###将数据传递给网页的ret

    alldb=edatabase.objects.all()
    return render_to_response('eproject/edatabase_graph.html', locals())

