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
from api import *

#add eproject
def eproject_add(request):
    jump_view = 'eproject_list'
    if request.method == 'POST':
        form = eprojectForm(request.POST)
        if form.is_valid():
            pname = form.cleaned_data['pname']
            ea = form.save()

            pids = request.POST.getlist('pids', [])
            print pids

            ##授权
            if pids:
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

    page_objects = pages(pt, request, 5)  ##分页
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

            if eserver.objects.filter(host=ehost,dport=eport):
                emg = u'添加失败, 此服务器 %s:%s 已存在!' % (ehost,eport)
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



###发布申请
def release_apply(request):
    current_admin_id = get_current_admin(request).id  ##获取当前登录用户的id
    pk_id = request.GET.get('id', '')
    eserverall=eserver.objects.get(id=pk_id)

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
    pt = release.objects.all()
    ##分页
    query_string = request.META.get('QUERY_STRING', '')

    # 搜索功能
    # pname = request.GET.get('pname', '')
    # if len(pname) > 0:
    #     pt = eproject.objects.filter(pname__contains=pname).order_by('-id')

    page_objects = pages(pt, request, 5)  ##分页
    return  render_to_response('eproject/release_list.html', locals())


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
    return render_to_response('eproject/ptslow_list.html', locals())





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

