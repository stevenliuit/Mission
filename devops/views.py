# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render_to_response, redirect, HttpResponse

from apps.models import *
from apps.account.forms import ProfileEditForm
from common.utils.account import is_authenticated
from common.utils.crypt import md5
from common.utils.sessions import get_current_admin


def index(request):
    current_admin = get_current_admin(request)
    project_count = eproject.objects.all().count()
    server_count = eserver.objects.all().count()
    # server_count = Server.objects.filter(projectenv__project__leader_id=current_admin.id).count()
    # auth_count = OsAuth.objects.filter(admin_id=current_admin.id).count()
    login_count=Admin.objects.get(id=current_admin.id).last_login_time

    return render_to_response('index.html', locals())


def login(request):
    if is_authenticated(request):
        return redirect('index')

    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            users = Admin.objects.filter(name=username, pwd=md5(password))
            if users:
                user = users[0]
                if user.status == Admin.STATUS_CLOSE:
                    error = u'该用户已经停用,请联系管理员'
                else:
                    request.session.flush()
                    request.session['current_admin_id'] = user.id
                    request.session['current_role_id'] = user.role_id

                    user.last_login_ip = request.META['REMOTE_ADDR']
                    user.last_login_time = datetime.now()
                    user.save()

                    return redirect('index')
            else:
                error = u'用户名或密码错误'
        else:
            error = u'用户名或密码错误'
    return render_to_response('login.html', locals())


def logout(request):
    del request.session['current_admin_id']
    del request.session['current_role_id']

    return redirect('login')


def profile(request):
    """
    编辑账号 VIEW
    """
    current_admin = get_current_admin(request)
    if not current_admin:
        jump_view = 'login'
        message = '对不起, 您还没有登陆'
        return render_to_response('error.html', locals())

    pk_id = current_admin.id

    admin = Admin.objects.get(id=pk_id)
    org_role_id = admin.role_id
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=admin)
        if form.is_valid():
            admin = form.save(commit=False)

            pwd = request.POST.get('pwd')
            if pwd:
                admin.pwd = md5(pwd)

            admin.save()
            form.save_m2m()
            return redirect('index')
        else:
            emg = u'账号: 修改个人信息失败'

    roles = Role.objects.all()
    return render_to_response('profile.html', locals(), request)


def down_key(request):
    import os
    from common.utils.account import get_ssh_key
    uuid = request.GET.get('uuid', '')
    if uuid:
        user = Admin.objects.get(uuid=uuid)
        if user:
            username = user.name
            private_key_file = get_ssh_key(username)
            if private_key_file:
                f = open(private_key_file)
                data = f.read()
                f.close()

                response = HttpResponse(data, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(private_key_file)
                os.unlink(private_key_file)

                return response
    return HttpResponse('No Key File. Contact Admin.')
